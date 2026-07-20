---
title: "[Solution] Python InterruptedError — I/O Interrupted by Signal"
description: "Fix Python InterruptedError when system calls are interrupted by signals. Learn about SA_RESTART, signal handling, and retry patterns for interrupted I/O."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 20
---

# Python InterruptedError — I/O Interrupted by Signal

An `InterruptedError` is raised when a system call is interrupted by a signal before it could complete. On Linux, this is `errno.EINTR`. Python 3.3+ raises `InterruptedError` (a subclass of `OSError`) instead of returning `None` as in Python 2.

## Common Causes

```python
# Cause 1: Signal arriving during blocking I/O
import socket

s = socket.socket()
s.connect(("example.com", 80))
# A SIGALRM or other signal during recv() can cause InterruptedError
data = s.recv(1024)

# Cause 2: time.sleep() interrupted by signal
import time
try:
    time.sleep(60)  # Signal during sleep raises InterruptedError
except InterruptedError:
    print("Sleep was interrupted")

# Cause 3: File read/write interrupted
with open("large_file.bin", "rb") as f:
    data = f.read(1024 * 1024)  # Large read can be interrupted

# Cause 4: subprocess.wait() interrupted
import subprocess
proc = subprocess.Popen(["long_running_command"])
proc.wait()  # Signal during wait raises InterruptedError

# Cause 5: os.system() interrupted
import os
exit_code = os.system("sleep 10")  # SIGINT during system() call
```

## How to Fix

### Fix 1: Retry interrupted system calls

```python
import socket
import errno

def reliable_recv(sock, bufsize):
    while True:
        try:
            return sock.recv(bufsize)
        except InterruptedError:
            continue  # Retry the interrupted call

# Or more concisely
def reliable_recv_v2(sock, bufsize):
    while True:
        try:
            return sock.recv(bufsize)
        except OSError as e:
            if e.errno != errno.EINTR:
                raise
```

### Fix 2: Use signal-specific handling for sleep()

```python
import signal
import time

def safe_sleep(seconds):
    try:
        time.sleep(seconds)
        return True  # Completed normally
    except InterruptedError:
        return False  # Was interrupted

# Or handle the signal explicitly
def alarm_handler(signum, frame):
    print("Alarm fired!")

signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(5)
try:
    time.sleep(60)
except InterruptedError:
    print("Sleep interrupted by alarm")
```

### Fix 3: Use select/poll for interruptible I/O with timeouts

```python
import select

def read_with_timeout(fd, timeout=5.0):
    ready, _, _ = select.select([fd], [], [], timeout)
    if ready:
        return os.read(fd, 4096)
    return None  # Timeout — no data available
```

### Fix 4: Wrap subprocess calls to handle interrupts

```python
import subprocess
import signal

def run_command(cmd):
    proc = subprocess.Popen(cmd, shell=True)
    try:
        proc.wait()
    except InterruptedError:
        proc.terminate()
        proc.wait()
        raise
    return proc.returncode
```

### Fix 5: Use SA_RESTART flag to auto-restart interrupted calls (C extension)

```python
# In Python, SA_RESTART is handled by the interpreter for most calls.
# For manual signal handling, explicitly manage retry logic:
import signal

def handle_sigusr1(signum, frame):
    print("Received SIGUSR1")

signal.signal(signal.SIGUSR1, handle_sigusr1)

# Blocking I/O after setting handler may be auto-restarted,
# but always be prepared for InterruptedError
```

## Prevention Checklist

- Always handle `InterruptedError` in code that performs blocking I/O.
- Retry interrupted system calls rather than abandoning the operation.
- Use `signal.signal()` with `SA_RESTART` behavior awareness for long-running programs.
- Test signal handling by sending `SIGINT` or `SIGALRM` during I/O operations.
- Use `select()`, `poll()`, or `asyncio` for non-blocking I/O that avoids interruption issues.

## Related Errors

- [OSError](/languages/python/oserror/) — parent class for I/O errors including interrupted calls.
- [BrokenPipeError](/languages/python/brokenpipeerror/) — pipe closed by the other end.
- [BlockingIOError](/languages/python/blockingioerror/) — non-blocking I/O would block.
- [TimeoutError](/languages/python/timeouterror/) — operation timed out.
