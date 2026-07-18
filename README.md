# 📚 Study Tracker

A command-line Study Tracker application built with Python.

The project is being developed incrementally to practice Python fundamentals, software engineering principles, refactoring techniques, testing, and clean code practices.

---

# Current Version

**Version 1.3**

---

# Features

- Add study sessions
- View all study sessions
- Search study sessions by subject
- Calculate total study hours
- Display today's study sessions
- Delete study sessions
- Persistent data storage using JSON
- Input validation for all user inputs

---

# Technologies Used

- Python 3
- JSON
- datetime module

---

# Project Structure

```
Study Tracker
│
├── main.py
├── storing_session.json
└── README.md
```

---

# Version History

## Version 1.0

### Initial Project

Implemented the basic Study Tracker application.

Features:

- Add study session
- View sessions
- Search subject
- Total study hours
- Today's study
- Delete session
- Save data using JSON

---

## Version 1.1

### Input Validation

Added comprehensive input validation.

Improvements:

- Subject validation
- Date validation
- Study hour validation
- Topic validation
- Difficulty validation
- Better error messages
- Prevent invalid data entry

---

## Version 1.2

### Validation Refactoring

Refactored repeated validation logic into reusable helper functions.

New helper functions:

- get_valid_subject()
- get_valid_session_date()
- get_valid_session_hour()
- get_valid_session_topic()
- get_valid_session_difficulty()

Benefits:

- Cleaner add_session()
- Better readability
- Improved maintainability
- Reduced code duplication

---

## Version 1.3

### Data Persistence Refactoring

Refactored JSON file handling into dedicated helper functions.

New helper functions:

- load_session()
- save_session()

Improvements:

- Separated file operations from the main application logic
- Encapsulated JSON loading and saving responsibilities
- Preserved automatic conversion between JSON date strings and Python datetime.date objects
- Simplified application startup and exit flow
- Improved maintainability and readability

---

# Testing Performed

## Version 1.3 Testing

Completed the following tests successfully:

- Loaded valid JSON data
- Loaded empty JSON file
- Loaded invalid JSON file
- Verified date conversion from JSON string to datetime.date
- Verified date conversion back to JSON string during saving
- Verified newly added sessions persist after restarting the application
- Verified empty session list saves correctly
- Regression tested all existing features

---

# Software Engineering Concepts Practiced

Throughout this project:

- Functions
- Lists
- Dictionaries
- Input Validation
- Exception Handling
- File Handling
- JSON Serialization
- Data Persistence
- Refactoring
- Helper Functions
- Separation of Concerns
- Single Responsibility Principle
- Code Reusability
- Regression Testing
- Defensive Programming

---

# What I Learned

## Version 1.2

- Breaking large functions into smaller helper functions
- Writing reusable validation logic
- Improving readability without changing functionality

## Version 1.3

- Separating persistence logic from application logic
- Designing helper functions with clear responsibilities
- Returning data from functions correctly
- Passing data through function parameters
- Performing regression testing after refactoring
- Maintaining application behavior while improving code structure

---

# Planned Improvements

Future versions may include:

- Better session display formatting
- Session editing
- Statistics dashboard
- CSV export
- Object-Oriented Programming (OOP)
- SQLite database support
- Unit testing
- Logging
- Configuration management

---

# Author

**Priyansh Panjabi**

