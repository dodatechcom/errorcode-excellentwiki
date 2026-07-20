---
title: "[Solution] Python Signal Error — Signal Handling and Process Control Issues"
description: "Fix Python signal errors by correctly registering handlers, managing SIGTERM/SIGINT, and handling signals in threads. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 202
---

# Python Signal Error — Signal Handling and Process Control Issues

Signal errors occur when signal handlers are improperly registered, signals are sent from invalid contexts, or signal handling conflicts with threading and async code. Python's signal module has strict rules about where and how signals can be handled.

## Common Causes

```python
# Calling signal.signal() from a non-main thread
import signal
import threading

def handler(signum, frame):
    print("Caught signal")

def worker():
    signal.signal(signal.SIGTERM, handler)  # ValueError: signal only works in main thread

t = threading.Thread(target=worker)
t.start()
t.join()
```

```python
# Setting signal alarm without handling SIGALRM
import signal

signal.alarm(5)  # SIGALRM will be raised in 5 seconds
# No handler registered — default behavior terminates the process
```

```python
# Invalid signal number
import signal

signal.signal(999, signal.SIG_DFL)  # ValueError: invalid signal value
```

```python
# Sending signal to a process without proper permissions
import os
import signal

os.kill(1, signal.SIGTERM)  # PermissionError: [Errno 1] Operation not permitted
```

```python
# Signal handler raises an exception
import signal

def bad_handler(signum, frame):
    raise RuntimeError("handler error")  # Exception in signal handler disrupts program

signal.signal(signal.SIGINT, bad_handler)
```

## How to Fix

### Fix 1: Always register signal handlers in the main thread

```python
import signal
import threading

def handler(signum, frame):
    print(f"Caught signal {signum}")

# Register in main thread before starting any other threads
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

def worker():
    print(f"Worker running in thread {threading.current_thread().name}")

t = threading.Thread(target=worker)
t.start()
t.join()
```

### Fix 2: Use signal.alarm with a proper SIGALRM handler

```python
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(5)  # Set 5-second alarm

try:
    # Long-running operation
    result = sum(range(10**7))
finally:
    signal.alarm(0)  # Cancel the alarm
    print(f"Result: {result}")
```

### Fix 3: Use contextlib for safe timeout management

```python
import signal
from contextlib import contextmanager

@contextmanager
def timeout(seconds):
    def handler(signum, frame):
        raise TimeoutError(f"Timed out after {seconds} seconds")
    
    original_handler = signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, original_handler)

# Usage
try:
    with timeout(3):
        import time
        time.sleep(10)  # Will raise TimeoutError after 3 seconds
except TimeoutError as e:
    print(e)  # Timed out after 3 seconds
```

### Fix 4: Use event flags for cross-thread signal communication

```python
import signal
import threading
import time

shutdown_event = threading.Event()

def signal_handler(signum, frame):
    print(f"Received signal {signum}, initiating shutdown")
    shutdown_event.set()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def worker():
    while not shutdown_event.is_set():
        print("Working...")
        shutdown_event.wait(timeout=1)
    print("Clean shutdown complete")

t = threading.Thread(target=worker)
t.start()

# In another thread or after a delay, trigger shutdown
# os.kill(os.getpid(), signal.SIGTERM)
t.join()
```

### Fix 5: Handle signal-specific behavior in subprocesses

```python
import signal
import subprocess
import sys

def run_with_timeout(cmd, timeout_seconds):
    def handler(signum, frame):
        raise TimeoutError("Process timed out")
    
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_seconds)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result
    except TimeoutError:
        subprocess.run(["kill", "-9", str(process.pid)])
        return None
    finally:
        signal.alarm(0)

result = run_with_timeout(["sleep", "10"], timeout_seconds=2)
if result is None:
    print("Process was killed due to timeout")
```

## Examples

### Graceful shutdown handler

```python
import signal
import sys
import time

class GracefulKiller:
    def __init__(self):
        self.kill_now = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    
    def exit_gracefully(self, signum, frame):
        print(f"Received signal {signum}")
        self.kill_now = True

killer = GracefulKiller()

while not killer.kill_now:
    print("Running...")
    time.sleep(1)

print("Shutdown complete")
```

### Signal-based inter-process communication

```python
import os
import signal
import time

def child_process():
    def handler(signum, frame):
        print(f"Child {os.getpid()} received signal {signum}")
    
    signal.signal(signal.SIGUSR1, handler)
    
    while True:
        signal.pause()  # Wait for signals

pid = os.fork()
if pid == 0:
    child_process()
else:
    time.sleep(0.1)
    os.kill(pid, signal.SIGUSR1)
    time.sleep(0.1)
    os.kill(pid, signal.SIGTERM)
    os.waitpid(pid, 0)
```

## Related Errors

- [OSError](/languages/python/oserror/) — includes permission errors when sending signals
- [TimeoutError](/languages/python/timeouterror/) — timeout-related signal handling
- [RuntimeError](/languages/python/runtimeerror/) — thread-related signal restrictions
