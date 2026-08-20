"""
Standalone Application Launcher for XYZ AI School Assistant Ecosystem
Starts the Python backend server and opens the interactive dashboard in your web browser.
"""

import subprocess
import webbrowser
import time
import sys
import os

SERVER_SCRIPT = os.path.join(os.path.dirname(__file__), "05. XYZ AI Repository", "xyz-ai", "server", "app.py")

def main():
    print("=" * 60)
    print("🚀 Starting XYZ AI Human-Like School Assistant Engine...")
    print("=" * 60)
    
    if not os.path.exists(SERVER_SCRIPT):
        print(f"❌ Error: Server script not found at {SERVER_SCRIPT}")
        sys.exit(1)

    print(f"Launching server: {SERVER_SCRIPT}")
    server_process = subprocess.Popen([sys.executable, SERVER_SCRIPT])
    
    # Wait for server to bind to port 8000
    time.sleep(1.5)
    
    url = "http://localhost:8000"
    print(f"🌐 Opening XYZ AI Assistant interface in browser: {url}")
    webbrowser.open(url)
    
    print("\nSystem active! Press Ctrl+C in this console to terminate the server.\n")
    try:
        server_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down server process...")
        server_process.terminate()

if __name__ == "__main__":
    main()
