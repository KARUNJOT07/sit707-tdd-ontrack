"""
Unit tests for Task Submission Status Tracker
Tests written FIRST, before implementation (TDD - RED phase)
"""

import pytest
from datetime import datetime, timedelta
from src.submission_tracker import SubmissionTracker


class TestSubmissionTracker:
    """Test cases for submission status tracking"""
    
    def setup_method(self):
        """Initialize tracker before each test"""
        self.tracker = SubmissionTracker()
        self.due_date = datetime(2026, 5, 7)
        self.on_time_date = datetime(2026, 5, 5)
        self.late_date = datetime(2026, 5, 10)
    
    def test_tracker_initializes(self):
        """Test that tracker initializes without errors"""
        tracker = SubmissionTracker()
        assert tracker is not None
    
    def test_on_time_submission_returns_correct_status(self):
        """Test that on-time submissions are identified correctly"""
        result = self.tracker.check_submission_status(
            student_id="STU001",
            task_id="TASK001",
            submission_date=self.on_time_date,
            due_date=self.due_date
        )
        
        assert result['status'] == "On Time"
        assert result['days_late'] == 0
        assert "on time" in result['message'].lower()
    
    def test_late_submission_returns_correct_status(self):
        """Test that late submissions are identified correctly"""
        result = self.tracker.check_submission_status(
            student_id="STU002",
            task_id="TASK001",
            submission_date=self.late_date,
            due_date=self.due_date
        )
        
        assert result['status'] == "Late"
        assert result['days_late'] == 3
        assert "late" in result['message'].lower()
    
    def test_late_submission_calculates_days_late_correctly(self):
        """Test accurate calculation of days late"""
        late_date_5_days = self.due_date + timedelta(days=5)
        
        result = self.tracker.check_submission_status(
            student_id="STU003",
            task_id="TASK002",
            submission_date=late_date_5_days,
            due_date=self.due_date
        )
        
        assert result['days_late'] == 5
    
    def test_submission_exactly_on_due_date_is_on_time(self):
        """Test that submission on exact due date is on time"""
        result = self.tracker.check_submission_status(
            student_id="STU004",
            task_id="TASK003",
            submission_date=self.due_date,
            due_date=self.due_date
        )
        
        assert result['status'] == "On Time"
        assert result['days_late'] == 0
    
    def test_not_submitted_returns_correct_status(self):
        """Test that missing submissions are identified"""
        result = self.tracker.check_submission_status(
            student_id="STU005",
            task_id="TASK004",
            submission_date=None,
            due_date=self.due_date
        )
        
        assert result['status'] == "Not Submitted"
        assert result['days_late'] is None
        assert "not submitted" in result['message'].lower()
    
    def test_invalid_student_id_raises_error(self):
        """Test that invalid student ID raises ValueError"""
        with pytest.raises(ValueError):
            self.tracker.check_submission_status(
                student_id="",
                task_id="TASK001",
                submission_date=self.on_time_date,
                due_date=self.due_date
            )
    
    def test_invalid_task_id_raises_error(self):
        """Test that invalid task ID raises ValueError"""
        with pytest.raises(ValueError):
            self.tracker.check_submission_status(
                student_id="STU001",
                task_id=None,
                submission_date=self.on_time_date,
                due_date=self.due_date
            )
    
    def test_submission_date_after_due_date_raises_error(self):
        """Test that invalid date comparison is caught"""
        with pytest.raises(ValueError):
            self.tracker.check_submission_status(
                student_id="STU001",
                task_id="TASK001",
                submission_date="invalid-date",
                due_date=self.due_date
            )
    
    def test_returns_dictionary_with_required_keys(self):
        """Test that return value contains all required keys"""
        result = self.tracker.check_submission_status(
            student_id="STU001",
            task_id="TASK001",
            submission_date=self.on_time_date,
            due_date=self.due_date
        )
        
        assert isinstance(result, dict)
        assert 'status' in result
        assert 'days_late' in result
        assert 'message' in result
    
    def test_message_field_is_string(self):
        """Test that message field contains a string"""
        result = self.tracker.check_submission_status(
            student_id="STU001",
            task_id="TASK001",
            submission_date=self.on_time_date,
            due_date=self.due_date
        )
        
        assert isinstance(result['message'], str)
        assert len(result['message']) > 0
    
    def test_one_day_late_is_calculated_correctly(self):
        """Test edge case: exactly one day late"""
        one_day_late = self.due_date + timedelta(days=1)
        
        result = self.tracker.check_submission_status(
            student_id="STU006",
            task_id="TASK005",
            submission_date=one_day_late,
            due_date=self.due_date
        )
        
        assert result['status'] == "Late"
        assert result['days_late'] == 1