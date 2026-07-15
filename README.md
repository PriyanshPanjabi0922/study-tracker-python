# 📚 Study Tracker

A command-line Python application to record, manage, and review study sessions.

This project is being built as an independent learning project to strengthen Python programming fundamentals, problem-solving, debugging, and software engineering practices.

---

## 🚀 Current Version

**Version:** v1.1 (In Progress)

---

## ✅ Features Completed

### Menu System
- Add Study Session
- View All Sessions
- Search Subject
- Total Study Hours
- Show Today's Study
- Delete Session
- Exit Application

---

### Input Validation

Implemented validation for:

- Menu selection
- Subject name (cannot be empty)
- Date format
- Future dates
- Study hours
    - Prevents invalid text input
    - Prevents negative hours
    - Prevents zero hours
    - Prevents unrealistic hours (>12)
- Topic name
    - Prevents empty input
    - Allows only alphabets and spaces
- Difficulty level
    - Easy
    - Medium
    - Hard
- Delete session input validation
- Search subject handling

---

### JSON Storage

- Save study sessions into JSON
- Load previous study sessions automatically
- Session counter persists after restarting application

---

### JSON Error Handling

Implemented handling for:

- Empty JSON files
- Invalid JSON data (`JSONDecodeError`)
- Safe initialization of study session list

---

### Date Handling

Implemented proper conversion between:

- `date` → `string` before saving to JSON
- `string` → `date` after loading from JSON

This keeps the internal program logic consistent while allowing JSON storage.

---

### Testing Completed

Successfully tested:

- Empty JSON file
- First application launch
- Adding first session
- Saving sessions
- Reloading sessions
- Restarting application
- Adding additional sessions
- Showing today's study
- Searching subjects
- Deleting sessions
- Session persistence across multiple runs

---

## 🛠 Technologies Used

- Python 3
- JSON
- datetime module

---

## 📖 Learning Goals

This project focuses on learning:

- Python fundamentals
- Functions
- Lists
- Dictionaries
- Loops
- Conditional logic
- Exception handling
- File handling
- JSON persistence
- Debugging
- Data validation
- Working with date objects
- Software testing

---

## 🚧 Planned for Next Version

Remaining work before completing v1.1:

- Improve handling when JSON file does not exist (`FileNotFoundError`)
- Final code cleanup and refactoring
- Improve output formatting for viewing sessions
- Complete end-to-end QA testing
- Fix any bugs discovered during testing

---

## 👨‍💻 Author

Priyansh Panjabi

Independent Python Learning Project
