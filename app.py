"""
XYZ AI Backend Application Server
Provides REST API endpoints for Chat, Voice Processing, Security Audit, and ERP Services.
Uses standard Python http.server for 100% zero-dependency compatibility.
"""

import http.server
import socketserver
import json
import urllib.parse
import os
import sys

# Ensure local imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.persona_engine import PersonaEngine, PERSONA_CONFIGS, SUPPORTED_LANGUAGES
from backend.mock_erp import MockERPService
from backend.security_app import SecurityGuard
PORT=8000
CLIENT_DIR=os.path.join(os.path.dirname(__file__), "client")
# Global security audit log buffer
SECURITY_AUDIT_LOGS = []

class XYZAIRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=CLIENT_DIR, **kwargs)

    def log_security_event(self, role: str, action: str, status: str, details: str):
        event = {
            "timestamp": self.date_time_string(),
            "role": role,
            "action": action,
            "status": status,
            "details": details
        }
        SECURITY_AUDIT_LOGS.insert(0, event)
        if len(SECURITY_AUDIT_LOGS) > 100:
            SECURITY_AUDIT_LOGS.pop()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path == "/api/personas":
            self.send_json_response({
                "personas": PERSONA_CONFIGS,
                "supported_languages": SUPPORTED_LANGUAGES,

            })
        elif path == "/api/security-logs":
            self.send_json_response({"logs": SECURITY_AUDIT_LOGS})
        elif path == "/api/attendance":
            query_params = urllib.parse.parse_qs(parsed_url.query)
            role = query_params.get("role", ["Student"])[0]
            student_id = query_params.get("student_id", ["STD101"])[0]

            auth_ok, auth_msg = SecurityGuard.authorize_action(role, "view_own_attendance" if role=="Student" else "view_child_attendance")
            self.log_security_event(role, "FETCH_ATTENDANCE_API", "SUCCESS" if auth_ok else "DENIED", auth_msg)

            if not auth_ok and role not in ["Teacher", "Principal"]:
                self.send_json_response({"error": auth_msg}, status=403)
                return

            if role == "Parent":
                data = MockERPService.get_child_attendance("PRN501")
            elif role == "Principal":
                data = MockERPService.get_school_analytics()
            else:
                data = MockERPService.get_student_attendance(student_id)

            self.send_json_response({"data": data})
        else:
            # Serve static files from client directory
            super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        try:
            body = json.loads(post_data) if post_data else {}
        except Exception:
            body = {}

        if path == "/api/chat":
            role = body.get("role", "Student")
            message = body.get("message", "")
            language = body.get("language", "English")
            context = body.get("context", {})

            # Log incoming request event
            self.log_security_event(role, "CHAT_REQUEST", "INSPECTING", f"Query: '{message}' | Lang: {language}")

            res = PersonaEngine.process_request(role, message, language, context)
            
            # Log security result
            if not res.get("success", True):
                self.log_security_event(role, "SECURITY_BLOCK", "BLOCKED", res.get("response", ""))
            else:
                self.log_security_event(role, res.get("action_taken", "CHAT"), "AUTHORIZED", f"Response generated in {language}")

            self.send_json_response(res)

        elif path == "/api/escalate":
            role = body.get("role", "Parent")
            target = body.get("target", "Teacher")
            reason = body.get("reason", "")

            auth_ok, auth_msg = SecurityGuard.authorize_action(role, "request_escalation")
            if not auth_ok:
                self.log_security_event(role, "ESCALATION_CALL", "DENIED", auth_msg)
                self.send_json_response({"error": auth_msg}, status=403)
                return

            ticket = MockERPService.create_escalation_request(role, f"User ({role})", target, reason)
            self.log_security_event(role, "ESCALATION_TICKET_CREATED", "CONFIRMED", f"Ticket #{ticket['ticket_id']} created for target '{target}'")
            self.send_json_response({"success": True, "ticket": ticket})

        elif path == "/api/mark-attendance":
            role = body.get("role", "Teacher")
            student_name = body.get("student_name", "Rahul")
            status = body.get("status", "Absent")

            auth_ok, auth_msg = SecurityGuard.authorize_action(role, "mark_attendance")
            if not auth_ok:
                self.log_security_event(role, "MARK_ATTENDANCE", "DENIED", auth_msg)
                self.send_json_response({"error": auth_msg, "security_violation": True}, status=403)
                return

            result = MockERPService.mark_attendance("TCH301", student_name, "", status)
            self.log_security_event(role, "MARK_ATTENDANCE", "SUCCESS", result["message"])
            self.send_json_response(result)

        else:
            self.send_json_response({"error": "Endpoint not found"}, status=404)

    def send_json_response(self, data: dict, status: int = 200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server():
    print(f"Starting XYZ AI Backend Server on http://localhost:{PORT}")
    server_address = ('', PORT)
    httpd = socketserver.TCPServer(server_address, XYZAIRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down XYZ AI Server.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
