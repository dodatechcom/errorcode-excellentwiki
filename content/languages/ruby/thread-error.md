---
title: "[Solution] Ruby ThreadError — Thread Error Fix"
description: "Fix Ruby ThreadError. Handle thread-related errors including deadlock, joining dead threads, and mutex issues."
languages: ["ruby"]
severities: ["error"]
error_types: ["thread"]
weight: 380
---

# ThreadError — Thread Error Fix

A `ThreadError` is raised when there's an error with a Thread, such as joining a dead thread, deadlock detection, or mutex issues.

## Description

`ThreadError` covers various thread-related errors in Ruby. This includes deadlock detection, trying to join a thread that's already been joined, and mutex-related issues.

Common scenarios:

- **Deadlock detected** — threads waiting on each other.
- **Join dead thread** — trying to join a thread that has finished.
- **Mutex not locked** — trying to unlock a mutex that isn't locked.
- **Thread already joined** — joining a thread twice.

## Common Causes

```ruby
# Cause 1: Deadlock
mutex1 = Mutex.new
mutex2 = Mutex.new

t1 = Thread.new do
  mutex1.synchronize do
    sleep 0.1
    mutex2.synchronize { }  # Waits for mutex2
  end
end

t2 = Thread.new do
  mutex2.synchronize do
    sleep 0.1
    mutex1.synchronize { }  # Waits for mutex1
  end
end

t1.join  # ThreadError: deadlock detected

# Cause 2: Join dead thread
thread = Thread.new { "done" }
thread.join
thread.join  # ThreadError: dead thread

# Cause 3: Unlock without lock
mutex = Mutex.new
mutex.unlock  # ThreadError: unlocked from non-owner thread

# Cause 4: Double lock (not reentrant)
mutex = Mutex.new
mutex.synchronize do
  mutex.synchronize do  # ThreadError: deadlock
  end
end
```

## Solutions

### Fix 1: Avoid deadlock with lock ordering

```ruby
# Wrong — inconsistent lock order
mutex1.synchronize do
  mutex2.synchronize { }
end

# Correct — consistent lock order
mutex1.synchronize do
  mutex2.synchronize { }
end

# Always lock in the same order everywhere
```

### Fix 2: Check thread status before joining

```ruby
thread = Thread.new { "done" }
thread.join

# Wrong
thread.join  # ThreadError

# Correct
if thread.status == false || thread.status.nil?
  puts "Thread has already finished"
else
  thread.join
end
```

### Fix 3: Use Mutex#try_lock for non-blocking

```ruby
mutex = Mutex.new

# Wrong — may deadlock
mutex.synchronize do
  # Long operation
end

# Correct — try lock with timeout
if mutex.try_lock
  begin
    # Operation
  ensure
    mutex.unlock
  end
else
  puts "Could not acquire lock"
end
```

### Fix 4: Use Monitor for reentrant locking

```ruby
require 'monitor'

monitor = Monitor.new

# This works (Monitor is reentrant)
monitor.synchronize do
  monitor.synchronize do
    # Works fine
  end
end
```

## Related Errors

- [ThreadError: deadlock](deadlock-lock) — deadlock specifically.
- [FiberError](fiber-error) — fiber-related errors.
- [NoMemoryError](memory-error) — memory issues from threads.
