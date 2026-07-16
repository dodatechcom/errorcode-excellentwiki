---
title: "Quick Reference — All Error Codes at a Glance"
description: "Quick reference table of all error codes across Windows, Linux, macOS, Python, C, PHP, Java, and JavaScript. Filter and search."
---

## Quick Reference

This page lists all error codes covered on this site. Use your browser's search (Ctrl+F) to find a specific code.

### Windows Errors

| Code | Description | Fix |
|------|-------------|-----|
| [0x80004005](/os/windows/0x80004005/) | Unspecified Error | Windows Update troubleshooter, SFC/DISM |
| [0x80070005](/os/windows/0x80070005/) | Access Denied | Take ownership, permissions fix |
| [0x80070002](/os/windows/0x80070002/) | File Not Found (Update) | Clear SoftwareDistribution cache |
| [0x8000FFFF](/os/windows/0x8000ffff/) | Catastrophic Failure | wsreset.exe, re-register Store |
| [DPC Watchdog Violation](/os/windows/bsod-dpc-watchdog-violation/) | BSOD | Update storage drivers, SSD firmware |
| [IRQL_NOT_LESS_OR_EQUAL](/os/windows/bsod-irql-not-less-or-equal/) | BSOD | Update drivers, memory diagnostics |

### Linux Errors

| Code | Name | Description | Fix |
|------|------|-------------|-----|
| [errno-1](/os/linux/errno-1/) | EPERM | Operation not permitted | sudo, chmod, chown |
| [errno-2](/os/linux/errno-2/) | ENOENT | No such file or directory | Verify path, find command |
| [errno-5](/os/linux/errno-5/) | EIO | Input/output error | Check disk, fsck |
| [errno-12](/os/linux/errno-12/) | ENOMEM | Out of memory | Check free, add swap |
| [errno-13](/os/linux/errno-13/) | EACCES | Permission denied | chmod, check ACLs |
| [errno-28](/os/linux/errno-28/) | ENOSPC | No space left on device | df -h, find large files |

### macOS Errors

| Code | Name | Description | Fix |
|------|------|-------------|-----|
| [-43](/os/macos/-43/) | FNFErr | File not found | Reset Finder, Spotlight |
| [-36](/os/macos/-36/) | ioErr | Input/output error | Disk Utility First Aid |
| [-50](/os/macos/-50/) | paramErr | Parameter error | Check syntax, reset NVRAM |

### Python Errors

| Error | Description | Fix |
|-------|-------------|-----|
| [TypeError](/languages/python/typeerror/) | Wrong type operation | Type conversion |
| [ValueError](/languages/python/valueerror/) | Invalid argument | Input validation |
| [KeyError](/languages/python/keyerror/) | Dict key not found | .get(), 'in' check |
| [IndexError](/languages/python/indexerror/) | List index out of range | Check len() |
| [AttributeError](/languages/python/attributeerror/) | No attribute | hasattr(), type check |
| [ImportError](/languages/python/importerror/) | Module not found | pip install, sys.path |
| [IndentationError](/languages/python/indentationerror/) | Bad indentation | 4 spaces, autopep8 |
| [SyntaxError](/languages/python/syntaxerror/) | Invalid syntax | Check syntax |
| [ZeroDivisionError](/languages/python/zerodivisionerror/) | Division by zero | Validate divisor |
| [FileNotFoundError](/languages/python/filenotfounderror/) | File not found | Check path, os.path.exists |

### C/C++ Errors

| Error | Description | Fix |
|-------|-------------|-----|
| [Segmentation Fault](/languages/c/segmentation-fault/) | Memory access violation | gdb, null checks, valgrind |
| [malloc NULL](/languages/c/errno-enomem/) | Memory allocation failed | Check return, free memory |
| [Stack Overflow](/languages/c/stack-overflow/) | Infinite recursion | Base case, iteration |
| [std::out_of_range](/languages/cpp/stdout-of-range/) | Index out of range | .at(), check size() |
| [std::bad_alloc](/languages/cpp/std-bad-alloc/) | Allocation failed | try/catch, smart pointers |

### PHP Errors

| Error | Description | Fix |
|-------|-------------|-----|
| [Parse Error](/languages/php/parse-error/) | Syntax error | Check syntax |
| [Fatal Error](/languages/php/fatal-error/) | Uncaught error | Define functions, memory |
| [Undefined Index](/languages/php/notice-undefined-index/) | Array key missing | isset(), ?? operator |

### Java Errors

| Error | Description | Fix |
|-------|-------------|-----|
| [NullPointerException](/languages/java/nullpointerexception/) | Null reference | null check, Optional |
| [ClassNotFoundException](/languages/java/classnotfoundexception/) | Class not found | Check classpath |
| [OutOfMemoryError](/languages/java/outofmemoryerror/) | Heap space | -Xmx, fix leaks |
| [ClassCastException](/languages/java/classcastexception/) | Wrong cast | instanceof, generics |
| [StackOverflowError](/languages/java/stackoverflowerror/) | Infinite recursion | Base case, -Xss |

### JavaScript/Node.js Errors

| Error | Description | Fix |
|-------|-------------|-----|
| [ReferenceError](/languages/javascript/referenceerror/) | Variable not defined | Declare variable |
| [TypeError](/languages/javascript/typeerror/) | Cannot read property | Optional chaining ?. |
| [SyntaxError](/languages/javascript/syntaxerror/) | Unexpected token | Check syntax |
| [ENOENT](/languages/javascript/enosuchfileordirectory/) | File not found | path.join(), __dirname |
| [CORS Error](/languages/javascript/cors-error/) | Cross-origin blocked | Server headers, proxy |

### Deprecated Functions

| Function | Language | Replacement |
|----------|----------|-------------|
| [ereg()](/deprecated/php/ereg-to-preg-match/) | PHP | preg_match() |
| [split()](/deprecated/php/split-to-explode/) | PHP | explode() |
| [each()](/deprecated/php/each-to-foreach/) | PHP | foreach |
| [mysql_*](/deprecated/php/mysql-to-mysqli/) | PHP | mysqli_* / PDO |
| [create_function()](/deprecated/php/create-function/) | PHP | Anonymous functions |
| [print statement](/deprecated/python/print-statement/) | Python | print() |
| [raw_input()](/deprecated/python/raw-input-to-input/) | Python | input() |
| [has_key()](/deprecated/python/has-key/) | Python | 'in' operator |
| [escape()/unescape()](/deprecated/javascript/escape-unescape/) | JavaScript | encodeURI() |
| [substr()](/deprecated/javascript/substr-to-slice/) | JavaScript | slice() |
| [execCommand()](/deprecated/javascript/exec-command/) | JavaScript | Clipboard API |
| [Thread.stop()](/deprecated/java/thread-stop/) | Java | Thread.interrupt() |
| [Date methods](/deprecated/java/date-methods/) | Java | java.time API |
