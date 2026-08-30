# Python and Software Development Research Assignment

## Introduction

This document covers the main Python programming concepts and software development practices assigned during the internship.

The aim is to understand not only Python syntax, but also how Python programs are written, tested, organized, maintained, and used for tasks such as data processing and web scraping.

The second part focuses on software development processes, version control, documentation, coding standards, testing, and code quality tools.

---

# PART A – PYTHON RESEARCH TOPICS

## 1. Indentation and Comments

Indentation is one of the most important features of Python. Unlike languages that commonly use braces to define blocks, Python uses spaces or tabs to show which statements belong to a block.

- A common convention is **four spaces** for each indentation level.
- Incorrect indentation can produce an `IndentationError` or change the logical structure of code.
- Comments are notes written in source code to explain logic and improve maintainability.
- A single-line comment normally begins with `#`.
- Comments should explain **why** something is done when the code itself is not obvious.

### Example

```python
if marks >= 40:
    print("Pass")

# Calculate the final amount after discount
```

---

## 2. Functions

A function is a reusable block of code designed to perform a particular task.

Functions:

- Reduce repetition.
- Make programs easier to understand.
- Make code easier to test and maintain.
- Can accept parameters.
- Can return values using `return`.
- Can use default arguments.
- Should ideally have one clear responsibility.
- Should have meaningful names.

### Example

```python
def calculate_total(price, quantity):
    return price * quantity

amount = calculate_total(100, 3)
print(amount)
```

---

## 3. OOPs – Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming approach that organizes software around **objects and classes**.

Python supports concepts such as:

- Classes
- Objects
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

### Basic Concepts

- **Class:** A blueprint for creating objects.
- **Object:** An instance of a class.
- **Encapsulation:** Keeps related data and behavior together.
- **Inheritance:** Allows a class to reuse or extend behavior from another class.
- **Polymorphism:** Allows a common interface to work with different object types.

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"


student = Student("Rahul")
print(student.introduce())
```

---

## 4. File Handling

File handling is used when a program needs to read data from or write data to files.

Python provides the `open()` function and supports modes such as:

- `r` – Read
- `w` – Write
- `a` – Append
- Read/write combinations

### Important Points

- `with open(...)` is preferred because it automatically closes the file.
- Large text files can be processed line by line.
- CSV and JSON are common structured formats.
- File paths should be handled carefully to avoid missing-file and permission errors.

### Example

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

---

## 5. Exception Handling

Exception handling allows a program to respond to unexpected situations without abruptly terminating.

Python provides:

- `try`
- `except`
- `else`
- `finally`

### Meaning

- `try` contains code that may raise an exception.
- `except` handles a specific exception.
- `else` runs when no exception occurs.
- `finally` is useful for cleanup operations.

It is better to catch specific exceptions instead of using a broad `except` without a reason.

### Example

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
```

---

## 6. NumPy and Pandas

**NumPy** and **Pandas** are widely used Python libraries for data processing.

### NumPy

NumPy provides efficient array-based numerical operations.

Useful for:

- Numerical calculations
- Matrix operations
- Array processing

### Pandas

Pandas provides high-level data structures such as:

- `Series`
- `DataFrame`

Useful for:

- Filtering
- Sorting
- Grouping
- Joining
- Cleaning data
- Reading CSV and Excel files

Vectorized operations are generally more efficient than manually looping through every value.

### Example

```python
import pandas as pd

df = pd.read_csv("students.csv")
passed = df[df["marks"] >= 40]

print(passed)
```

---

## 7. Selenium for Web Scraping

Selenium is a browser automation framework that can control a real web browser.

It is useful when a website relies heavily on JavaScript and the required content is not easily available from a simple HTTP request.

### Features

- WebDriver controls the browser.
- Can locate elements.
- Can click buttons.
- Can fill forms.
- Can retrieve page content.
- Explicit waits are preferable to arbitrary `sleep()` calls.
- Scraping should respect website terms, robots policies where applicable, rate limits, and legal requirements.
- For simple static pages, `requests` and an HTML parser may be lighter than Selenium.

### Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://example.com")

heading = browser.find_element(By.TAG_NAME, "h1")
print(heading.text)

browser.quit()
```

---

## 8. Regular Expressions (Regex)

Regular expressions are patterns used to:

- Search text
- Match text
- Validate text
- Extract text

Python provides the `re` module for regular-expression operations.

### Common Functions

- `re.search()` – Finds a matching pattern.
- `re.findall()` – Returns all matching occurrences.
- `re.sub()` – Replaces text that matches a pattern.

Regex can be used to extract:

- Emails
- Phone numbers
- IDs
- Dates
- Log values
- Other structured text

Complex regex patterns should be documented because they can become difficult to maintain.

### Example

```python
import re

text = "Contact: student@example.com"
email = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

print(email)
```

---

## 9. Multithreading and Multiprocessing

### Multithreading

Multithreading means running multiple threads within a process.

It is often useful for **I/O-bound work**, such as waiting for network responses.

### Multiprocessing

Multiprocessing uses separate processes and can be useful for **CPU-intensive work** because each process can execute independently.

### Differences

- Threads share process memory.
- Shared memory makes communication convenient but requires care with shared state.
- Processes have separate memory spaces.
- Processes usually have higher startup and communication costs.
- Python's Global Interpreter Lock (GIL) affects CPU-bound execution of Python bytecode in typical CPython implementations.
- The correct choice depends on whether the workload is mainly I/O-bound or CPU-bound.

### Example

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(
        executor.map(str.upper, ["a", "b", "c", "d"])
    )
```

---

## 10. Concurrency vs Parallelism

**Concurrency** is the ability to make progress on multiple tasks during overlapping periods.

**Parallelism** means executing multiple tasks at the same time, usually using multiple CPU cores.

### Concurrency

Useful when tasks spend time waiting, such as:

- Network I/O
- File I/O

### Parallelism

Useful when independent CPU-heavy tasks can run simultaneously.

### Important Difference

A program can be concurrent without executing tasks in true parallel at the same instant.

Asynchronous programming is another way to manage concurrency for suitable I/O workloads.

---

# PART B – OTHER SOFTWARE DEVELOPMENT TOPICS

## 11. SDLC – Software Development Life Cycle

SDLC is a structured approach for developing and maintaining software.

### Stages of SDLC

1. **Planning**
   - Identify objectives, resources, schedule, and feasibility.

2. **Requirement Analysis**
   - Understand what users and stakeholders need.

3. **Design**
   - Decide architecture, components, interfaces, data flow, and technologies.

4. **Implementation**
   - Write and integrate the code.

5. **Testing**
   - Verify functionality, reliability, security, and other requirements.

6. **Deployment**
   - Release software to users or the production environment.

7. **Maintenance**
   - Fix defects, improve performance, and add required changes.

---

## 12. Agile and Scrum

**Agile** is a software-development approach that emphasizes:

- Iterative delivery
- Customer feedback
- Collaboration
- Adapting to changing requirements

**Scrum** is a popular framework used to apply Agile ideas through defined roles, events, and artifacts.

### Scrum Concepts

- **Sprint:** A short, fixed development cycle.
- **Product Backlog:** Contains work that may be needed in the product.
- **Sprint Backlog:** Contains selected work for a Sprint.
- **Daily Scrum:** Short team event for inspecting progress and planning the next work.
- **Sprint Review:** Focuses on the increment and stakeholder feedback.
- **Sprint Retrospective:** Focuses on improving the team's process.

### Scrum Accountabilities

1. Product Owner
2. Scrum Master
3. Developers

---

## 13. Code Version Control

Version control records changes to source code so developers can collaborate and recover earlier versions.

**Git** is a distributed version-control system commonly used with:

- GitHub
- GitLab
- Bitbucket

### Important Terms

- **Repository:** Stores project history.
- **Commit:** Records a set of changes.
- **Branch:** Allows developers to work on features or fixes independently.
- **Merge:** Combines changes from branches.
- **Pull/Merge Request:** Provides a review process before changes are integrated.

### Typical Git Workflow

```text
1. git pull
2. Create a feature branch
3. Make changes
4. Run tests and quality checks
5. git add / git commit
6. git push
7. Open a pull request
```

---

## 14. Documentation

Documentation explains how a software system works and how it should be used or maintained.

Good documentation:

- Reduces dependency on individual team members.
- Makes onboarding easier.
- Helps developers understand the system.

### Types of Documentation

#### README

Explains:

- Project purpose
- Setup
- Usage
- Basic contribution information

#### API Documentation

Describes:

- Endpoints
- Inputs
- Outputs
- Authentication
- Errors

#### Architecture Documentation

Explains:

- Major components
- How components interact

#### User Documentation

Focuses on how users operate the product.

Documentation should be updated when important behavior or interfaces change.

---

## 15. Risk Management

Risk management is the process of:

1. Identifying possible problems.
2. Evaluating their impact and probability.
3. Planning responses.

Software project risks may involve:

- Technology
- Schedule
- Security
- People
- Requirements
- Dependencies

### Risk Management Steps

- Identify risks early.
- Assess probability and impact.
- Prioritize risks.
- Create mitigation actions.
- Prepare contingency actions for important risks.
- Review risks throughout the project.

---

## 16. Python Coding Standards

Coding standards are agreed rules for writing consistent, readable, and maintainable code.

Python projects benefit from conventions covering:

- Naming
- Imports
- Formatting
- Functions
- Errors
- Documentation
- Project structure

### Best Practices

- Use clear and descriptive names.
- Keep functions focused and reasonably small.
- Avoid unnecessary duplication.
- Prefer simple and readable solutions.
- Use automated formatting and linting where appropriate.
- Keep dependencies and project configuration organized.

---

## 17. PEP 8

**PEP 8** is Python's style guide.

It provides recommendations for formatting and naming so Python code has a consistent appearance across projects.

### Main Guidelines

- Use four spaces for indentation.
- Keep lines reasonably short.
- Use `snake_case` for functions and variables.
- Use `CapWords` for classes.
- Use blank lines to separate logical sections.
- Keep imports organized.

PEP 8 is a guide rather than a reason to sacrifice readability when a practical exception is justified.

---

## 18. Comments and Docstrings

Comments and docstrings both provide explanations, but they have different purposes.

### Comments

Usually explain a section of implementation.

### Docstrings

Document:

- Modules
- Classes
- Functions

Docstrings can also be accessed programmatically.

### Best Practices

- Write comments for non-obvious decisions.
- Do not simply restate obvious code.
- A function docstring can describe:
  - Purpose
  - Parameters
  - Return value
  - Important exceptions
- Keep documentation accurate when implementation changes.
- Public or reusable functions especially benefit from clear docstrings.

### Example

```python
def calculate_tax(amount, rate):
    """Return tax calculated from an amount and tax rate."""
    return amount * rate
```

---

## 19. Error Handling and Logging

Error handling prevents expected failures from crashing an application without useful information.

Logging records:

- Important events
- Warnings
- Errors

### Best Practices

- Catch specific exceptions whenever possible.
- Do not silently ignore failures.
- Use logging instead of `print()` for application diagnostics.
- Include enough context to understand what happened.
- Avoid exposing sensitive information in logs.

### Common Logging Levels

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

### Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

try:
    value = int("abc")
except ValueError:
    logger.exception("Invalid integer input")
```

---

## 20. Efficient Code

Efficient code uses appropriate:

- Algorithms
- Data structures
- I/O patterns
- Resources

Efficiency should be considered together with readability and correctness.

### Best Practices

- Choose suitable data structures.
- Sets can provide fast membership checks.
- Avoid repeated expensive operations inside loops.
- Process large files in chunks or streams when possible.
- Use vectorized operations in NumPy/Pandas for suitable workloads.
- Profile before optimizing complex performance problems.
- Optimize the real bottleneck instead of making code unnecessarily complicated.

---

## 21. Software Engineering Principles

Software engineering principles provide general guidance for building maintainable systems.

### DRY

**Don't Repeat Yourself**

Avoid unnecessary duplication of knowledge or logic.

### KISS

**Keep It Simple**

Prefer straightforward solutions when they satisfy the requirements.

### YAGNI

**You Aren't Gonna Need It**

Avoid building speculative features without a current need.

### Single Responsibility Principle

A component should have a focused responsibility.

### Separation of Concerns

Keep different responsibilities independent where practical.

### SOLID

SOLID principles provide a set of object-oriented design guidelines for maintainability and extensibility.

---

## 22. Unit Testing and Validation

Unit testing checks small pieces of software, usually individual functions or classes, in isolation from unrelated components.

Validation more broadly checks whether data or behavior meets defined rules.

### Best Practices

- Tests should be repeatable and focused.
- A good unit test checks a specific expected behavior.
- Test normal cases.
- Test boundary cases.
- Test invalid cases.
- Assertions compare actual results with expected results.

### Python Testing Tools

- `unittest` – Included in Python's standard library.
- `pytest` – Popular third-party testing framework.

### Example

```python
def add(a, b):
    return a + b


import unittest


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

---

## 23. Ruff

**Ruff** is a fast Python linter and code-quality tool.

It can:

- Detect common problems.
- Detect style issues.
- Provide automated fixes for supported rules.
- Help maintain consistent code in teams and CI environments.

### Features

- Checks Python files for linting violations.
- Supports many rules in one fast tool.
- Can be configured in project files such as `pyproject.toml`.
- Can complement formatters such as Black.
- Ruff also provides formatting capabilities depending on the workflow.

### Example

```bash
ruff check .
```

---

## 24. Black

**Black** is an opinionated Python code formatter.

It automatically reformats code into a consistent style.

### Benefits

- Reduces formatting arguments.
- Makes code reviews easier to focus on logic.
- Automates formatting.
- Makes large codebases easier to read.
- Can be integrated into editors and CI pipelines.

### Important Difference

- **Formatter:** Changes code presentation.
- **Linter:** Checks code-quality rules.

### Example

```bash
black .
```

---

# 25. How the Topics Fit Together

These topics are connected rather than being separate concepts.

A practical Python project may start with requirements defined through an **SDLC process** and managed through an **Agile/Scrum workflow**.

Developers can then:

- Use **Git** for version control.
- Follow Python standards such as **PEP 8**.
- Use **functions and OOP** for structure.
- Use **file handling** and **Pandas/NumPy** for data processing.
- Use **Regex** for extraction.
- Use **Selenium** when browser automation is required.
- Use **exception handling and logging** to make the system reliable.
- Use **unit tests** to validate behavior.
- Use **Ruff and Black** to improve code quality.
- Use **multithreading, multiprocessing, or other concurrency techniques** when the workload requires better resource utilization.

---

# 26. Suggested Mini Project Architecture

A useful way to combine the assigned concepts is to build a small **data-processing application**.

### Example Workflow

```text
CSV Files
    +
Log Files
    +
API Data
    +
Web Page
    ↓
Collect Data
    ↓
Validate Data
    ↓
Normalize Data
    ↓
Process with Pandas / NumPy
    ↓
Extract Fields using Regex
    ↓
Generate Report
```

### Tools Used

- **Selenium** – For dynamic websites when appropriate.
- **Classes and Functions** – For code organization.
- **Exception Handling** – For reliability.
- **Unit Testing** – For validation.
- **Git** – For version control.
- **Ruff** – For linting and code quality.
- **Black** – For formatting.

---

# 27. Conclusion

The topics covered in this assignment form a practical foundation for **Python development and software engineering**.

Python syntax and programming concepts are important for writing applications, while:

- Standards
- Testing
- Version control
- Documentation
- Development processes

are important for making applications reliable and maintainable.

Understanding when to use tools such as:

- Pandas
- NumPy
- Selenium
- Regex
- Multithreading
- Multiprocessing
- Ruff
- Black

is as important as knowing their basic syntax.

---

## Quick Revision Table

| Topic | Main Purpose |
|---|---|
| Indentation | Defines Python code blocks |
| Comments | Explains code and decisions |
| Functions | Reusable blocks of code |
| OOP | Organizes software using classes and objects |
| File Handling | Reads and writes files |
| Exception Handling | Handles unexpected errors |
| NumPy | Numerical and array operations |
| Pandas | Data processing and analysis |
| Selenium | Browser automation |
| Regex | Pattern matching and text extraction |
| Multithreading | Useful for I/O-bound tasks |
| Multiprocessing | Useful for CPU-intensive tasks |
| Concurrency | Handles overlapping tasks |
| Parallelism | Executes tasks simultaneously |
| SDLC | Software development process |
| Agile/Scrum | Iterative project management |
| Git | Version control |
| Documentation | Explains software usage and structure |
| Risk Management | Identifies and handles project risks |
| PEP 8 | Python coding style guide |
| Logging | Records application events and errors |
| DRY | Avoids unnecessary duplication |
| KISS | Keeps solutions simple |
| YAGNI | Avoids unnecessary features |
| Unit Testing | Tests individual components |
| Ruff | Python linting and code quality |
| Black | Python code formatting |

---

## Source

This README is based on the provided **Python and Software Development Research Assignment** document.
