# 📚 Study Tracker

A command-line Study Tracker application built using Python to help record, organize, search, and review daily study sessions.

This project is part of my software engineering learning journey, focusing on writing clean, maintainable code while learning core Python concepts through hands-on projects.

---

# Features

- ✅ Add a study session
- ✅ View all study sessions
- ✅ Search sessions by subject
- ✅ Calculate total study hours
- ✅ View today's study sessions
- ✅ Delete a study session
- ✅ Save study sessions using JSON
- ✅ Automatically load saved sessions when the application starts

---

# Technologies Used

- Python
- JSON
- datetime module

---

# Project Structure

Current major functions:

- add_session()
- view_session()
- search_session()
- total_session_hour()
- today_session()
- delete_session()

---

# Version History

## Version 1.0

### Initial Implementation

Implemented the complete Study Tracker application with:

- Study session creation
- JSON storage
- Search functionality
- Delete functionality
- Total study hours
- Today's study
- Input validation
- Persistent storage

---

## Version 1.1

### Function Refactoring

### Objective

Improve code readability and maintainability by refactoring large menu blocks into dedicated functions without changing the application's behavior.

### Completed Refactoring

- Refactored Add Session into `add_session()`
- Refactored View Session into `view_session()`
- Refactored Search Subject into `search_session()`
- Refactored Total Study Hours into `total_session_hour()`
- Refactored Today's Study into `today_session()`
- Refactored Delete Session into `delete_session()`

### Engineering Concepts Practiced

- Functions
- Parameters
- Return Values
- Local Variables
- Mutable vs Immutable Objects
- Separation of Responsibilities
- Behavior-Preserving Refactoring
- Incremental QA Testing

### QA Testing

Every refactored function was tested individually.

| Feature | Status |
|----------|--------|
| Add Session | ✅ Passed |
| View Session | ✅ Passed |
| Search Subject | ✅ Passed |
| Total Study Hours | ✅ Passed |
| Today's Study | ✅ Passed |
| Delete Session | ✅ Passed |

Result:

- No functionality changed after refactoring.
- Existing features continued working correctly.

---

# Learning Outcomes

Through this project I practiced:

- Python Functions
- Lists
- Dictionaries
- JSON File Handling
- Loops
- Conditional Statements
- Input Validation
- Error Handling
- Refactoring
- Software Testing
- Debugging
- Writing Maintainable Code

---

# Current Limitations

These improvements are intentionally left for future versions:

- Delete session currently removes data based on list position instead of searching by session ID.
- Validation logic is duplicated across multiple functions.
- JSON loading and saving can be separated into dedicated helper functions.
- Session output formatting can be improved.
- The current project structure is procedural and will later be migrated to Object-Oriented Programming after learning OOP.

---

# Future Roadmap

Version 1.2

Planned improvements:

- Refactor repeated validation logic
- Create helper functions
- Improve session display formatting
- Separate JSON loading and saving logic
- Improve delete session logic

Version 2.0

Planned improvements:

- Convert the application to Object-Oriented Programming (OOP)
- Better project architecture
- Improved code organization
- Enhanced user experience

---

# Purpose of this Project

The goal of this project is not only to build a Study Tracker, but also to learn professional software engineering practices through incremental development, refactoring, testing, and continuous improvement.

Each version of this project focuses on learning a new programming concept while maintaining working software.
