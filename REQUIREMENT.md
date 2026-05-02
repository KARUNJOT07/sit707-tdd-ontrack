REQUIREMENT: TASK SUBMISSION STATUS TRACKER
=============================================

Feature: Check Task Submission Status and Timeliness

User Story:
-----------
As a tutor on OnTrack,
I want to quickly check if a student's task submission is on time or late,
So that I can track submission compliance and inform grading decisions.

Problem Statement:
-------------------
OnTrack needs to identify which student submissions are:
- On time (submitted before or on due date)
- Late (submitted after due date)
- Not submitted (no submission on record)

This helps tutors understand submission patterns and apply late penalties if needed.

Functional Requirements:
------------------------
INPUT:
  - student_id (string): Unique student identifier (e.g., "STU001")
  - task_id (string): Unique task identifier (e.g., "TASK001")
  - submission_date (datetime): When the student submitted
  - due_date (datetime): When the task was due

OUTPUT:
  - status (string): One of ["On Time", "Late", "Not Submitted"]
  - days_late (int): Number of days late (0 if on time, None if not applicable)
  - message (string): Human-readable status message

Acceptance Criteria:
---------------------
✓ System accepts valid student ID and task ID
✓ System correctly identifies on-time submissions (submitted <= due_date)
✓ System correctly identifies late submissions (submitted > due_date)
✓ System calculates days late accurately
✓ System handles missing submissions gracefully
✓ System validates input dates

Example Scenarios:
-------------------

Scenario 1: On-Time Submission
  INPUT: student_id="STU001", task_id="TASK001", 
          submission_date=2026-05-01, due_date=2026-05-07
  OUTPUT: status="On Time", days_late=0, 
          message="Submission received on time"

Scenario 2: Late Submission
  INPUT: student_id="STU002", task_id="TASK001",
          submission_date=2026-05-10, due_date=2026-05-07
  OUTPUT: status="Late", days_late=3,
          message="Submission is 3 days late"

Scenario 3: Not Submitted
  INPUT: student_id="STU003", task_id="TASK001",
          submission_date=None, due_date=2026-05-07
  OUTPUT: status="Not Submitted", days_late=None,
          message="No submission found"