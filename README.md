# 📚 Study Tracker (Python CLI)

A command-line Study Tracker application built using Python.

This project is part of my Python learning journey, where I am building everything independently to strengthen my programming fundamentals, problem-solving skills, debugging ability, and software development practices.

---

## 🚀 Current Version

**Version:** v1.1 (In Progress)

---

## ✅ Features Completed

### 1. Add Study Session
- Add a new study session.
- Stores:
  - Session Number
  - Subject Name
  - Study Date
  - Hours Studied
  - Topic Covered
  - Difficulty Level

---

### 2. View All Sessions
- Displays every study session stored in the application.

---

### 3. Search a Subject
- Search for a subject by its name.
- Displays whether the subject exists.

---

### 4. Total Study Hours
- Calculates the total number of study hours.

---

### 5. Show Today's Study
- Displays today's study sessions.
- Calculates today's total study hours.

---

### 6. Delete Session
- Delete a session using its session number.

---

### 7. Persistent Storage
- Saves all sessions into a JSON file.
- Loads previous sessions automatically when the application starts.

---

### 8. Empty JSON File Handling
- Detects an empty or invalid JSON file.
- Automatically creates an empty study session list instead of crashing.

---

### 9. Date Serialization
- Converts `datetime.date` objects into strings before saving.
- Converts them back into `date` objects while loading.

---

### 10. Improved Input Validation
The application now provides clearer and more user-friendly error messages for:

- Invalid menu choices
- Empty subject names
- Invalid date formats
- Future dates
- Invalid study hours
- Negative or zero study hours
- Invalid topic names
- Invalid difficulty levels
- Invalid delete requests
- Subject search failures

The goal is to guide the user instead of only reporting an error.

---

# 🛠 Technologies Used

- Python 
- JSON
- datetime module

---

# 📖 Learning Objectives

This project is helping me practice:

- Variables
- Data Types
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Functions (planned)
- Exception Handling
- JSON File Handling
- Date & Time Handling
- Input Validation
- Program Debugging
- Writing cleaner user-friendly CLI applications

---

# 📌 Next Tasks (v1.1)

The remaining work planned before moving to Version 1.2 is:

- Refactor repetitive code to improve readability and maintainability.
- Improve the display format of session data instead of printing raw dictionaries.
- Perform complete end-to-end testing of every menu option.
- Fix any bugs discovered during testing.

---

# 🎯 Project Goal

This project is focused on learning core Python programming by building a real application from scratch without relying on external frameworks.

Each version emphasizes writing cleaner code, improving user experience, handling edge cases, and following better programming practices.
