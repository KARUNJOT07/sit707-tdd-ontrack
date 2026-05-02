"""
Task Submission Status Tracker for OnTrack
Checks if student submissions are on time, late, or not submitted
"""

from datetime import datetime
from typing import Optional, Dict, Any


class SubmissionTracker:
    """
    Tracks and validates task submission status and timeliness.
    """
    
    def __init__(self):
        """Initialize the submission tracker"""
        pass
    
    def check_submission_status(
        self,
        student_id: str,
        task_id: str,
        submission_date: Optional[datetime],
        due_date: datetime
    ) -> Dict[str, Any]:
        """
        Check the submission status and timeliness for a student task.
        
        Args:
            student_id (str): Unique identifier for the student
            task_id (str): Unique identifier for the task
            submission_date (datetime or None): When the student submitted
            due_date (datetime): When the task was due
        
        Returns:
            dict: Contains keys:
                - 'status': "On Time", "Late", or "Not Submitted"
                - 'days_late': Integer (0 if on time, None if not submitted)
                - 'message': Human-readable status message
        
        Raises:
            ValueError: If student_id, task_id are invalid or dates are invalid
        """
        
        # Validate inputs
        self._validate_inputs(student_id, task_id, submission_date, due_date)
        
        # Handle not submitted case
        if submission_date is None:
            return {
                'status': 'Not Submitted',
                'days_late': None,
                'message': 'Not submitted - no submission found for this task.'
            }
        
        # Calculate days late
        days_late = self._calculate_days_late(submission_date, due_date)
        
        # Determine status
        if days_late <= 0:
            status = 'On Time'
            message = f'Submission received on time (submitted on {submission_date.strftime("%Y-%m-%d")}).'
        else:
            status = 'Late'
            message = f'Submission is {days_late} day{"s" if days_late != 1 else ""} late.'
        
        return {
            'status': status,
            'days_late': days_late if days_late > 0 else 0,
            'message': message
        }
    
    def _validate_inputs(
        self,
        student_id: str,
        task_id: str,
        submission_date: Optional[datetime],
        due_date: datetime
    ) -> None:
        """Validate all input parameters."""
        
        if not student_id or not isinstance(student_id, str):
            raise ValueError("student_id must be a non-empty string")
        
        if task_id is None or not isinstance(task_id, str):
            raise ValueError("task_id must be a valid string")
        
        if not isinstance(due_date, datetime):
            raise ValueError("due_date must be a datetime object")
        
        if submission_date is not None and not isinstance(submission_date, datetime):
            raise ValueError("submission_date must be a datetime object or None")
    
    def _calculate_days_late(self, submission_date: datetime, due_date: datetime) -> int:
        """Calculate the number of days a submission is late."""
        delta = submission_date - due_date
        return delta.days