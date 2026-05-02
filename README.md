# SIT707 - Task Submission Status Tracker

**Subject**: Software Quality and Testing (SIT707)  
**Assessment**: Pass Task - Test-Driven Development (TDD) and Continuous Integration (CI)  
**Student**: Karun Singh Singh  
**GitHub**: https://github.com/KARUNJOT07/sit707-tdd-ontrack  

## Project Overview

This project implements a **Task Submission Status Tracker** for the OnTrack platform using Test-Driven Development (TDD) methodology with Continuous Integration (CI) pipeline.

### Feature: Check Task Submission Timeliness

Tutors on OnTrack need to quickly identify:
- ✅ On-time submissions (submitted on or before due date)
- ⏰ Late submissions (submitted after due date)
- ❌ Not submitted (no submission on record)

## Setup Instructions

### Prerequisites
- Python 3.10+
- VS Code
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/KARUNJOT07/sit707-tdd-ontrack.git
cd sit707-tdd-ontrack
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run tests**
```bash
pytest tests/ -v
```

## TDD Development Cycle

**RED Phase**: Write failing tests first
**GREEN Phase**: Write minimal code to pass tests
**REFACTOR Phase**: Clean up and improve code

## CI/CD with GitHub Actions

This project uses GitHub Actions for continuous integration. Tests run automatically on every push.

View builds at: https://github.com/KARUNJOT07/sit707-tdd-ontrack/actions