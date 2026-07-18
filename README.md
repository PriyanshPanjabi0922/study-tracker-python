# 📚 Study Tracker

A command-line Study Tracker built with Python to practice software engineering, clean code principles, input validation, refactoring, and version control.

This project is being developed incrementally, where each version focuses on improving one engineering concept instead of simply adding new features.

---

# 🚀 Current Version

**Version:** 1.2 – Helper Function Refactoring

---

# ✨ Features

- ➕ Add a study session
- 📋 View all study sessions
- 🔍 Search study sessions by subject
- ⏱️ Calculate total study hours
- 📅 View today's study sessions
- 🗑️ Delete a study session
- 💾 Store data persistently using JSON

---

# 🛠️ Technologies Used

- Python 
- JSON
- datetime module

---

# 📂 Project Structure

```text
Study Tracker
│
├── main.py
├── storing_session.json
└── README.md
```

---

# 📌 Version History

## Version 1.0 – Initial Application

### Implemented

- Created Study Tracker CLI
- Add study sessions
- View study sessions
- Search by subject
- Total study hours
- Today's study
- Delete session
- JSON file storage

---

## Version 1.1 – Function Refactoring

### Goal

Improve code organization using functions.

### Refactoring

- Broke large code into smaller functions
- Improved readability
- Improved maintainability
- Applied function decomposition

Functions created:

- `add_session()`
- `view_session()`
- `search_session()`
- `total_session_hour()`
- `today_session()`
- `delete_session()`

---

## Version 1.2 – Helper Function Refactoring

### Goal

Improve internal code quality by extracting repeated validation logic into helper functions.

### Helper Functions Added

- `get_valid_subject()`
- `get_valid_session_date()`
- `get_valid_session_hour()`
- `get_valid_session_topic()`
- `get_valid_session_difficulty()`

### Improvements

- Reduced repeated validation code.
- Simplified `add_session()`.
- Improved readability.
- Improved maintainability.
- Applied the Single Responsibility Principle.
- Kept program behavior unchanged after refactoring.
- Tested each helper function individually before integration.

---

# 🧪 Testing Performed

Validation testing was performed after every helper function was created.

### Subject

- ✅ Valid subject
- ✅ Empty input
- ✅ Spaces only

### Session Date

- ✅ Empty input
- ✅ Invalid format
- ✅ Future date
- ✅ Valid date

### Study Hours

- ✅ Empty input
- ✅ Non-numeric input
- ✅ Zero
- ✅ Negative value
- ✅ Greater than 12
- ✅ Valid value

### Topic

- ✅ Empty input
- ✅ Spaces only
- ✅ Numbers
- ✅ Special characters
- ✅ Mixed text (e.g. Python3)
- ✅ Valid topic names

### Difficulty

- ✅ Empty input
- ✅ Spaces only
- ✅ Numbers
- ✅ Invalid text
- ✅ Valid values (easy, medium, hard)

---

# 🎯 Software Engineering Concepts Practiced

- Input validation
- Function design
- Helper functions
- Single Responsibility Principle (SRP)
- Refactoring
- Clean code
- Code readability
- Debugging
- Testing
- Git workflow
- Incremental software development

---

# 📖 What I Learned in Version 1.2

- Helper functions should exist only when they represent a clear, reusable responsibility.
- Refactoring should improve readability, not just reduce line count.
- Every helper function should have a single responsibility.
- Testing after every refactoring helps detect bugs early.
- Understanding control flow (`return`, `break`, and `continue`) is essential for writing reliable validation loops.

---

# 🔜 Next Version

## Version 1.3 – Data Persistence Refactoring

### Planned Improvements

- Create `load_sessions()`
- Create `save_sessions()`
- Move JSON handling into dedicated helper functions.
- Improve separation of responsibilities.
- Keep program behavior unchanged while improving code quality.

---

# 👨‍💻 Author

**Priyansh Panjabi**

