# 📚 Study Tracker

A command-line Python application for recording, managing, and analyzing study sessions.

This project is being built as an independent learning project to strengthen my Python fundamentals, problem-solving skills, input validation, exception handling, JSON file handling, and overall software development practices.

---

# Current Version

**Version:** v1.1

---

# Features

## 1. Add Study Session

Users can add a study session with:

- Subject Name
- Study Date
- Study Hours
- Topic Covered
- Difficulty Level

Each study session is automatically assigned a unique Session Number.

---

## 2. View All Sessions

Displays every study session stored in the application.

---

## 3. Search a Subject

Allows users to search whether a subject exists in the stored study sessions.

---

## 4. Total Study Hours

Calculates and displays the total study hours across all recorded sessions.

---

## 5. Show Today's Study

Displays all study sessions recorded for today's date along with the total study hours for today.

---

## 6. Delete Session

Allows users to delete a study session using its Session Number.

---

# Input Validation

The application performs validation to maintain correct and meaningful data.

## Subject Name

- Cannot be empty

## Study Date

- Must follow the format: `DD-MM-YYYY`
- Invalid dates are rejected
- Future dates are not allowed

## Study Hours

- Accepts numeric values only
- Rejects text input
- Cannot be zero
- Cannot be negative
- Cannot be greater than 12 hours

## Topic Covered

- Cannot be empty
- Allows only alphabets and spaces

## Difficulty Level

Accepts only:

- easy
- medium
- hard

Input is case-insensitive.

## Delete Session

- Rejects invalid session numbers
- Rejects negative numbers
- Handles non-numeric input safely using `try/except`

## Menu Choice

- Handles invalid menu input
- Uses exception handling for non-numeric values

---

# Data Storage

All study sessions are stored in:

```
storing_session.json
```

Data is automatically saved when the user exits the application.

---

# Technologies Used

- Python
- JSON
- datetime module

---

# Python Concepts Practiced

- Variables
- Data Types
- Conditional Statements
- Loops
- Lists
- Dictionaries
- Nested Data Structures
- Exception Handling (`try` / `except`)
- Input Validation
- JSON File Handling
- Date & Time Handling (`datetime`)
- Program Design
- Debugging

---

# Completed in Version 1.1

- ✅ Menu System
- ✅ Add Study Session
- ✅ Session Counter
- ✅ JSON Storage
- ✅ Subject Validation
- ✅ Date Validation
- ✅ Study Hour Validation
- ✅ Topic Validation
- ✅ Difficulty Level Validation
- ✅ View All Sessions
- ✅ Search Subject
- ✅ Total Study Hours
- ✅ Show Today's Study
- ✅ Delete Session
- ✅ Exception Handling for Numeric Inputs

---

# Remaining Work for Version 1.1

The following tasks will be completed before starting Version 1.2:

- Handle empty JSON file safely
- Handle missing or corrupted JSON file
- Improve View All Sessions formatting
- Perform complete end-to-end testing
- Fix bugs discovered during testing
- Final code cleanup and refactoring

---

# Future Versions

Planned improvements after Version 1.1:

- Better formatted output using tables
- Edit existing study sessions
- Subject-wise statistics
- Monthly and weekly study reports
- CSV export
- Improved search options
- Refactor code into functions and multiple files
- Object-Oriented Design improvements

---

# Author

**Priyansh Panjabi**

Independent Python Learning Project

Learning by building real-world projects.
