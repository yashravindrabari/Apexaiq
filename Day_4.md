# Linux – Short Notes

## 1. What is Linux?
Linux is an **open-source operating system**. It is used to manage computer hardware, software, files, memory, processes, and networks.

**Simple example:** Ubuntu, Fedora, Debian, and Red Hat Enterprise Linux (RHEL) are Linux-based operating systems.

---

## 2. Why is Linux Used?
- Free and open-source
- Secure and stable
- Fast and lightweight
- Highly customizable
- Commonly used on servers and cloud systems
- Widely used in DevOps and cybersecurity

---

## 3. Linux Kernel
The **kernel** is the core part of Linux.

It works as a bridge between:
**Hardware ↔ Kernel ↔ Applications**

It manages:
- CPU
- Memory
- Devices
- Processes
- File systems

---

## 4. Linux Shell
A **shell** allows us to communicate with Linux using commands.

Common shells:
- Bash
- Zsh
- Fish

**Example:**
```bash
ls
```
This command shows files and folders.

---

## 5. Important Linux Commands

| Command | Use |
|---|---|
| `pwd` | Shows current directory |
| `ls` | Lists files and folders |
| `cd` | Changes directory |
| `mkdir` | Creates a directory |
| `touch` | Creates a file |
| `cp` | Copies files/folders |
| `mv` | Moves or renames files |
| `rm` | Removes files/folders |
| `cat` | Displays file content |
| `nano` | Opens a simple text editor |
| `clear` | Clears terminal |
| `whoami` | Shows current user |
| `sudo` | Runs a command with administrator privileges |
| `chmod` | Changes file permissions |
| `ps` | Shows running processes |
| `top` | Shows system/process activity |

---

## 6. Linux File System
Linux uses a hierarchical file system.

Important directories:
- `/` → Root directory
- `/home` → User files
- `/etc` → Configuration files
- `/var` → Logs and changing data
- `/tmp` → Temporary files
- `/bin` → Important commands/programs
- `/root` → Home directory of the root user

---

## 7. File Permissions
Linux controls who can read, write, or execute a file.

Three basic permissions:
- `r` → Read
- `w` → Write
- `x` → Execute

Three common users/groups:
- User
- Group
- Others

Example:
```bash
chmod 755 file.sh
```

---

## 8. Root User
The **root user** is the administrator of a Linux system.

Root has high-level permissions and can perform system-level operations.

---

## 9. Process
A **process** is a running program.

Example:
If you open a browser, the browser runs as one or more processes.

Useful commands:
```bash
ps
top
kill
```

---

## 10. Linux in Docker and Cloud
Linux is very common in:
- Docker containers
- Cloud servers
- Web servers
- DevOps
- Cybersecurity
- Networking

**Interview line:**

> "Linux is an open-source operating system widely used for servers, cloud, Docker, DevOps, and cybersecurity because it is secure, stable, lightweight, and customizable."

## Quick Revision
**Linux = Operating System**

**Kernel = Core of Linux**

**Shell = Interface for commands**

**Root = Administrator**

**Process = Running program**

**`ls` = List files**

**`cd` = Change directory**

**`pwd` = Current directory**

**`sudo` = Administrator-level command**
