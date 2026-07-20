---
title: "[Solution] Python EOFError — End of File Reached"
description: "Fix Python EOFError when input() is called at end of file, readline() returns empty, or iterators are exhausted. Handle stdin and file reading safely."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 19
---

# Python EOFError — End of File Reached

An `EOFError` is raised when `input()`, `readline()`, or similar functions reach the end of input without reading any data. This commonly happens when scripts are run non-interactively (piped input, CI pipelines) or when reading past the end of a file.

## Common Causes

```python
# Cause 1: input() in non-interactive environment
data = input("Enter your name: ")  # EOFError when stdin is piped or closed

# Cause 2: readline() at end of file
with open("data.txt") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()  # Returns '' — next call would raise EOFError

# Cause 3: Calling next() on an exhausted iterator in a REPL-like loop
def interactive_reader():
    while True:
        try:
            line = input(">>> ")
            process(line)
        except EOFError:
            break

# Cause 4: os.read() on a closed or empty pipe
import os
fd = os.pipe()
os.close(fd[1])  # Close write end
data = os.read(fd[0], 1024)  # Returns b'' — signals EOF

# Cause 5: socket.recv() on a closed connection
import socket
s = socket.socket()
s.connect(("example.com", 80))
s.close()
data = s.recv(1024)  # May raise or return empty bytes
```

## How to Fix

### Fix 1: Catch EOFError from input() in scripts

```python
# Wrong
name = input("Enter name: ")  # Crashes in non-interactive mode

# Correct
try:
    name = input("Enter name: ")
except EOFError:
    name = "default_user"
```

### Fix 2: Read all lines with a for loop instead of readline()

```python
# Wrong
with open("data.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)

# Correct
with open("data.txt") as f:
    for line in f:
        process(line)
```

### Fix 3: Use sys.stdin for robust non-interactive input

```python
import sys

if sys.stdin.isatty():
    name = input("Enter name: ")
else:
    name = sys.stdin.readline().strip()
    if not name:
        name = "default_user"
```

### Fix 4: Handle EOFError in interactive loops

```python
def repl():
    while True:
        try:
            line = input(">>> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        eval(line)
```

### Fix 5: Check for empty reads before processing

```python
import os

def read_until_closed(fd):
    chunks = []
    while True:
        chunk = os.read(fd, 4096)
        if not chunk:  # Empty bytes means EOF
            break
        chunks.append(chunk)
    return b"".join(chunks)
```

## Prevention Checklist

- Always catch `EOFError` when using `input()` in scripts that may run non-interactively.
- Use `for line in file:` instead of manual `readline()` loops to avoid EOF handling.
- Check `sys.stdin.isatty()` before relying on interactive input.
- Handle `EOFError` alongside `KeyboardInterrupt` in REPL-like loops.
- Use `read()` or `readlines()` when you need the full file content at once.

## Related Errors

- [StopIteration](/languages/python/stopiteration/) — iterator exhausted in `next()` calls.
- [BrokenPipeError](/languages/python/brokenpipeerror/) — pipe closed by the reading end.
- [OSError](/languages/python/oserror/) — general I/O failures including pipe and socket errors.
- [InterruptedError](/languages/python/interruptederror/) — I/O operation interrupted by signal.
