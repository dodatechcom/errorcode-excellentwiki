---
title: "[Solution] Python sched Module Error — Event Scheduler Failures"
description: "Fix Python sched module errors including scheduler, enter/enterabs, cancel, run, and empty queue errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 253
---

# Python sched Module Error — Event Scheduler Failures

The `sched` module implements a general-purpose event scheduler. Errors occur when events are scheduled in the past, cancelled incorrectly, or when the scheduler encounters empty queues or blocking issues.

## Common Causes

```python
# Cause 1: Scheduling event in the past
import sched
import time

s = sched.scheduler(time.time, time.sleep)
# Enter event with delay=0 in the past
s.enterabs(time.time() - 10, 1, print, ("Event in the past",))  # Runs immediately

# Cause 2: Cancelling a non-existent event
import sched
import time

s = sched.scheduler(time.time, time.sleep)
event = s.enter(10, 1, print, ("Hello",))
s.cancel(event)
s.cancel(event)  # ValueError: Event is not in the queue

# Cause 3: Running scheduler with no events
import sched
import time

s = sched.scheduler(time.time, time.sleep)
s.run()  # No error, but does nothing — may indicate logic issue

# Cause 4: Blocking in scheduled function
import sched
import time

s = sched.scheduler(time.time, time.sleep)

def blocking_task():
    time.sleep(100)  # Blocks the scheduler

s.enter(0, 1, blocking_task)
s.run()  # Scheduler blocked for 100 seconds

# Cause 5: Priority collision
import sched
import time

s = sched.scheduler(time.time, time.sleep)
s.enter(5, 1, print, ("First",))
s.enter(5, 1, print, ("Second"))  # Same priority — order depends on insertion
```

## How to Fix

### Fix 1: Schedule events with correct timing

```python
import sched
import time

s = sched.scheduler(time.time, time.sleep)

# Use enter() for relative time
s.enter(2, 1, print, ("Runs after 2 seconds",))

# Use enterabs() for absolute time
future_time = time.time() + 5
s.enterabs(future_time, 1, print, ("Runs at specific time",))

# Check if event time is in the future
def safe_enterabs(scheduler, timeval, priority, action, argument=()):
    if timeval < time.time():
        print("Warning: scheduling in the past, running immediately")
    scheduler.enterabs(timeval, priority, action, argument)

safe_enterabs(s, time.time() + 1, 1, print, ("Safe event",))
```

### Fix 2: Handle cancellation safely

```python
import sched
import time

s = sched.scheduler(time.time, time.sleep)

def safe_cancel(scheduler, event):
    try:
        scheduler.cancel(event)
        print("Event cancelled")
    except ValueError:
        print("Event not found in queue (may have already run)")

event1 = s.enter(10, 1, print, ("Will be cancelled",))
event2 = s.enter(20, 1, print, ("Will run",))

safe_cancel(s, event1)
safe_cancel(s, event1)  # Safe — won't crash

# Cancel by checking if still pending
def cancel_if_pending(scheduler, event):
    if event in scheduler.queue:
        scheduler.cancel(event)
        return True
    return False
```

### Fix 3: Use non-blocking scheduler pattern

```python
import sched
import time
import select

s = sched.scheduler(time.time, time.sleep)

def non_blocking_run(scheduler, timeout=1.0):
    """Run scheduler without blocking indefinitely."""
    end_time = time.time() + timeout
    while scheduler.queue:
        now = time.time()
        if now >= end_time:
            break
        # Process events that are due
        event = scheduler.queue[0]
        delay = event.time - now
        if delay <= 0:
            scheduler.run(blocking=False)
        else:
            time.sleep(min(delay, 0.1))

s.enter(1, 1, print, ("Quick event",))
s.enter(5, 1, print, ("Slow event"))
non_blocking_run(s, timeout=2)
```

### Fix 4: Handle empty queue gracefully

```python
import sched
import time

s = sched.scheduler(time.time, time.sleep)

def safe_run(scheduler):
    if not scheduler.queue:
        print("No events scheduled")
        return
    print(f"Running {len(scheduler.queue)} events")
    scheduler.run()

safe_run(s)  # "No events scheduled"

s.enter(1, 1, print, ("Event 1",))
safe_run(s)  # "Running 1 events"
```

### Fix 5: Use priorities to control execution order

```python
import sched
import time

s = sched.scheduler(time.time, time.sleep)

# Lower number = higher priority
s.enter(5, 3, print, ("Low priority",))
s.enter(5, 1, print, ("High priority"))
s.enter(5, 2, print, ("Medium priority"))

# Events run in priority order when scheduled at the same time
s.run()
# Output order: High priority, Medium priority, Low priority
```

## Examples

```python
# Real-world: Periodic task scheduler
import sched
import time

class PeriodicScheduler:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.running = False

    def periodic_task(self, interval, task, *args):
        def wrapper():
            if self.running:
                task(*args)
                self.scheduler.enter(interval, 1, periodic_task, (interval, task) + args)
        return wrapper

    def start(self, interval, task, *args):
        self.running = True
        self.scheduler.enter(interval, 1, self.periodic_task(interval, task, *args))
        self.scheduler.run()

    def stop(self):
        self.running = False

# Usage
def log_message(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

# ps = PeriodicScheduler()
# ps.start(5, log_message, "Heartbeat")  # Logs every 5 seconds

# Real-world: Delayed execution with timeout
import sched
import time

def delayed_execution(delay, func, *args, timeout=None):
    result = [None]
    done = [False]

    def wrapper():
        result[0] = func(*args)
        done[0] = True

    s = sched.scheduler(time.time, time.sleep)
    event = s.enter(delay, 1, wrapper)

    if timeout:
        def check_timeout():
            if not done[0]:
                s.cancel(event)
                print("Execution timed out")
        s.enter(timeout, 1, check_timeout)

    s.run()
    return result[0]
```

## Related Errors

- [ValueError](/languages/python/valueerror/) — event not in queue
- [AttributeError](/images/python/attributeerror/) — calling methods on None
- [KeyboardInterrupt](/languages/python/keyboardinterrupt/) — user interrupt during scheduler.run()
