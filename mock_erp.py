""
Mock ERP Ecosystem Database & Service Engine
Handles mock data for Students, Parents, Teachers, Principal, Attendance, Marks, and Escalations.
"""

import datetime
from typing import Dict, Any, List, Optional

# Pre-populated Mock Database
STUDENTS_DB = {
    "STD101": {
        "id": "STD101",
        "name": "Rahul Sharma",
        "grade": "Class 10-A",
        "roll_number": 24,
        "parent_id": "PRN501",
        "parent_name": "Mr. Rajesh Sharma",
        "teacher_id": "TCH301",
        "attendance": {
            "percentage": 91.2,
            "present_days": 146,
            "total_days": 160,
            "recent_records": [
                {"date": "2026-08-18", "status": "Present"},
                {"date": "2026-08-17", "status": "Present"},
                {"date": "2026-08-16", "status": "Sunday"},
                {"date": "2026-08-15", "status": "Holiday (Independence Day)"},
                {"date": "2026-08-14", "status": "Absent", "reason": "Sick Leave"},
                {"date": "2026-08-13", "status": "Present"},
                {"date": "2026-08-12", "status": "Present"}
            ]
        },
        "marks": {
            "Mathematics": {"unit_test_1": 88, "unit_test_2": 91, "final": 94},
            "Science": {"unit_test_1": 76, "unit_test_2": 80, "final": 85},
            "English": {"unit_test_1": 82, "unit_test_2": 85, "final": 88},
            "Social Science": {"unit_test_1": 79, "unit_test_2": 83, "final": 86}
        },
        "academic_summary": "Rahul is performing exceptionally well in Mathematics (94%) and Science (85%). Active in Basketball."
    },
    "STD102": {
        "id": "STD102",
        "name": "Ananya Verma",
        "grade": "Class 10-A",
        "roll_number": 12,
        "parent_id": "PRN502",
        "parent_name": "Mrs. Priya Verma",
        "teacher_id": "TCH301",
        "attendance": {
            "percentage": 96.5,
            "present_days": 154,
            "total_days": 160,
            "recent_records": [
                {"date": "2026-08-18", "status": "Present"},
                {"date": "2026-08-17", "status": "Present"},
                {"date": "2026-08-16", "status": "Sunday"},
                {"date": "2026-08-15", "status": "Holiday"},
                {"date": "2026-08-14", "status": "Present"}
            ]
        },
        "marks": {
            "Mathematics": {"unit_test_1": 95, "unit_test_2": 97, "final": 98},
            "Science": {"unit_test_1": 91, "unit_test_2": 93, "final": 95},
            "English": {"unit_test_1": 89, "unit_test_2": 90, "final": 92},
            "Social Science": {"unit_test_1": 87, "unit_test_2": 88, "final": 90}
        },
        "academic_summary": "Ananya tops in English Literature (92%) and Computer Science (95%)."
    },
    "STD103": {
        "id": "STD103",
        "name": "Rohan Patel",
        "grade": "Class 10-B",
        "roll_number": 31,
        "parent_id": "PRN503",
        "parent_name": "Mr. Suresh Patel",
        "teacher_id": "TCH302",
        "attendance": {
            "percentage": 82.0,
            "present_days": 131,
            "total_days": 160,
            "recent_records": [
                {"date": "2026-08-18", "status": "Absent"},
                {"date": "2026-08-17", "status": "Present"},
                {"date": "2026-08-16", "status": "Sunday"}
            ]
        },
        "marks": {
            "Mathematics": {"unit_test_1": 62, "unit_test_2": 65, "final": 70},
            "Science": {"unit_test_1": 58, "unit_test_2": 61, "final": 66},
            "English": {"unit_test_1": 70, "unit_test_2": 72, "final": 75},
            "Social Science": {"unit_test_1": 60, "unit_test_2": 63, "final": 68}
        },
        "academic_summary": "Rohan shows great potential in Art & Music. Math and Science need improvement."
    },
    "STD104": {
        "id": "STD104",
        "name": "Priya Nair",
        "grade": "Class 10-B",
        "roll_number": 18,
        "parent_id": "PRN504",
        "parent_name": "Mr. Vinod Nair",
        "teacher_id": "TCH302",
        "attendance": {
            "percentage": 89.5,
            "present_days": 143,
            "total_days": 160,
            "recent_records": [
                {"date": "2026-08-18", "status": "Present"},
                {"date": "2026-08-17", "status": "Present"},
                {"date": "2026-08-16", "status": "Sunday"}
            ]
        },
        "marks": {
            "Mathematics": {"unit_test_1": 78, "unit_test_2": 81, "final": 84},
            "Science": {"unit_test_1": 85, "unit_test_2": 87, "final": 90},
            "English": {"unit_test_1": 92, "unit_test_2": 94, "final": 96},
            "Social Science": {"unit_test_1": 80, "unit_test_2": 82, "final": 85}
        },
        "academic_summary": "Priya excels in English and shows strong overall consistency."
    },
    "STD105": {
        "id": "STD105",
        "name": "Aditya Kumar",
        "grade": "Class 10-C",
        "roll_number": 7,
        "parent_id": "PRN505",
        "parent_name": "Mrs. Kavita Kumar",
        "teacher_id": "TCH302",
        "attendance": {
            "percentage": 78.0,
            "present_days": 125,
            "total_days": 160,
            "recent_records": [
                {"date": "2026-08-18", "status": "Absent"},
                {"date": "2026-08-17", "status": "Absent"},
                {"date": "2026-08-16", "status": "Sunday"}
            ]
        },
        "marks": {
            "Mathematics": {"unit_test_1": 55, "unit_test_2": 58, "final": 60},
            "Science": {"unit_test_1": 64, "unit_test_2": 67, "final": 70},
            "English": {"unit_test_1": 68, "unit_test_2": 70, "final": 72},
            "Social Science": {"unit_test_1": 72, "unit_test_2": 74, "final": 76}
        },
        "academic_summary": "Aditya shows steady improvement but needs focus on Mathematics and attendance."
    }
}

TEACHERS_DB = {
    "TCH301": {
        "id": "TCH301",
        "name": "Mrs. Sunita Rao",
        "subject": "Mathematics",
        "class_assigned": "Class 10-A",
        "contact": "+91 98765 43210",
        "email": "sunita.rao@school.edu"
    },
    "TCH302": {
        "id": "TCH302",
        "name": "Mr. Amit Kumar",
        "subject": "Science",
        "class_assigned": "Class 10-B",
        "contact": "+91 98765 43211",
        "email": "amit.kumar@school.edu"
    }
}

# Escalation Call / Ticket Requests Database
ESCALATION_TICKETS = {}


class MockERPService:
    @staticmethod
    def get_student_attendance(student_id: str) -> Optional[Dict[str, Any]]:
        """Used by Student persona to view own attendance."""
        if student_id in STUDENTS_DB:
            st = STUDENTS_DB[student_id]
            return {
                "student_id": st["id"],
                "student_name": st["name"],
                "grade": st["grade"],
                "percentage": st["attendance"]["percentage"],
                "present_days": st["attendance"]["present_days"],
                "total_days": st["attendance"]["total_days"],
                "recent_records": st["attendance"]["recent_records"]
            }
        return None

    @staticmethod
    def get_child_attendance(parent_id: str) -> List[Dict[str, Any]]:
        """Used by Parent persona to view child's attendance."""
        results = []
        for st_id, st in STUDENTS_DB.items():
            if st["parent_id"] == parent_id or parent_id in ["PRN501", "PRN_DEMO"]:
                results.append({
                    "student_id": st["id"],
                    "student_name": st["name"],
                    "grade": st["grade"],
                    "percentage": st["attendance"]["percentage"],
                    "present_days": st["attendance"]["present_days"],
                    "total_days": st["attendance"]["total_days"],
                    "recent_records": st["attendance"]["recent_records"],
                    "assigned_teacher": TEACHERS_DB.get(st["teacher_id"], {}).get("name", "Class Teacher")
                })
        return results

    @staticmethod
    def mark_attendance(teacher_id: str, student_identifier: str, date_str: str, status: str, reason: str = "") -> Dict[str, Any]:
        """Used by Teacher persona to mark attendance."""
        target_student = None
        for st_id, st in STUDENTS_DB.items():
            if (st_id.lower() == student_identifier.lower() or
                st["name"].lower() in student_identifier.lower() or
                student_identifier.lower() in st["name"].lower()):
                target_student = st
                break

        if not target_student:
            return {"success": False, "message": f"Student '{student_identifier}' not found in database."}

        # Update record
        today = date_str or datetime.date.today().strftime("%Y-%m-%d")
        records = target_student["attendance"]["recent_records"]

        # Check if record for today exists
        updated = False
        for rec in records:
            if rec["date"] == today:
                rec["status"] = status
                if reason:
                    rec["reason"] = reason
                updated = True
                break

        if not updated:
            records.insert(0, {"date": today, "status": status, "reason": reason})

        # Recalculate mock total
        if status == "Absent":
            target_student["attendance"]["present_days"] = max(0, target_student["attendance"]["present_days"] - 1)
        target_student["attendance"]["percentage"] = round(
            (target_student["attendance"]["present_days"] / target_student["attendance"]["total_days"]) * 100, 1
        )

        return {
            "success": True,
            "message": f"Attendance marked as '{status}' for {target_student['name']} on {today}.",
            "student_name": target_student["name"],
            "new_percentage": target_student["attendance"]["percentage"]
        }

    @staticmethod
    def get_school_analytics() -> Dict[str, Any]:
        """Used by Principal persona to view school-wide analytics."""
        total_students = len(STUDENTS_DB)
        avg_attendance = round(
            sum(st["attendance"]["percentage"] for st in STUDENTS_DB.values()) / max(1, total_students), 1
        )
        class_wise = {
            "Class 10-A": {"students": 2, "avg_attendance": 93.85, "present_today": 2, "absent_today": 0},
            "Class 10-B": {"students": 2, "avg_attendance": 85.75, "present_today": 1, "absent_today": 1},
            "Class 10-C": {"students": 1, "avg_attendance": 78.0, "present_today": 0, "absent_today": 1},
            "Overall School": {"total_enrolled": 450, "avg_attendance": 94.2, "present_today": 424, "absent_today": 26}
        }
        return {
            "overall_attendance_percentage": avg_attendance,
            "school_wide_average": 94.2,
            "total_students": 450,
            "present_today": 424,
            "absent_today": 26,
            "class_breakdown": class_wise,
            "low_attendance_alerts": [
                {"student": "Rohan Patel (Class 10-B)", "percentage": 82.0, "warning": "Below 85% threshold"},
                {"student": "Aditya Kumar (Class 10-C)", "percentage": 78.0, "warning": "Below 85% threshold"}
            ]
        }

    @staticmethod
    def create_escalation_request(requester_role: str, requester_name: str, target: str, reason: str = "") -> Dict[str, Any]:
        """Triggers a mock call/support request to teacher or school management."""
        ticket_id = f"ESC-{len(ESCALATION_TICKETS) + 101}"
        ticket_data = {
            "ticket_id": ticket_id,
            "status": "CONFIRMED",
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "requester_role": requester_role,
            "requester_name": requester_name,
            "target": target,  # "Teacher" or "Management"
            "reason": reason or "User requested human escalation after chat interaction.",
            "estimated_callback_minutes": 15 if target == "Teacher" else 30
        }
        ESCALATION_TICKETS[ticket_id] = ticket_data
        return ticket_data

    # ------------------------------------------------------------
    # NEW: Records / Marks lookup methods
    # ------------------------------------------------------------
    @staticmethod
    def find_student_by_name(name: str) -> Optional[Dict[str, Any]]:
        """Fuzzy match a student by name or ID, used for 'records' lookups."""
        name_lower = name.lower().strip()
        for st_id, st in STUDENTS_DB.items():
            if st_id.lower() == name_lower or name_lower in st["name"].lower():
                return st
        return None

    @staticmethod
    def get_student_full_record(identifier: str) -> Optional[Dict[str, Any]]:
        """Returns combined attendance + marks record for a student by name or ID."""
        st = MockERPService.find_student_by_name(identifier)
        if not st:
            return None
        return {
            "student_id": st["id"],
            "student_name": st["name"],
            "grade": st["grade"],
            "attendance_percentage": st["attendance"]["percentage"],
            "marks": st.get("marks", {}),
            "academic_summary": st.get("academic_summary", "")
        }

    @staticmethod
    def get_student_marks(identifier: str) -> Optional[Dict[str, Any]]:
        """Returns just the marks for a student by name or ID."""
        st = MockERPService.find_student_by_name(identifier)
        if not st:
            return None
        return {
            "student_id": st["id"],
            "student_name": st["name"],
            "grade": st["grade"],
            "marks": st.get("marks", {})
        }
