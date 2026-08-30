# Problem 21 — OS and Software Version Normalization Engine

## Problem Statement

Build a normalization engine for operating-system information received from different sources, such as:

- Ubuntu 22.04
- ubuntu_22.04
- Ubuntu Linux 22.04 LTS
- Windows_Server_2022
- Microsoft Windows Server 2022
- win_2022
- RHEL-9.3
- RedHat Enterprise Linux 9.3

Convert each input into a standard structure containing:

- `os_family`
- `os_name`
- `os_version`

The system should allow new normalization rules to be added without modifying existing rules.

---

## Solution

The program uses an object-oriented rule-based approach.

Each operating system has its own normalization rule. The input is checked against the rules and converted into a standard format.

### Processing Flow

```text
Input OS Information
        ↓
Check Normalization Rules
        ↓
Identify OS Family
        ↓
Extract OS Name & Version
        ↓
Standard Output
```

### Example Output

```text
Input: Ubuntu Linux 22.04 LTS

{
    "os_family": "Linux",
    "os_name": "Ubuntu",
    "os_version": "22.04"
}
```

## Features

- Supports different OS naming formats
- Extracts OS name and version
- Uses regular expressions
- Uses object-oriented programming
- Allows new rules to be added easily
- Produces a standard output format

## Source Code

📄 **Python Implementation:**  
[View Problem_21.py](Solution.py)
