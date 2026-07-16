---
title: "[Solution] Ruby ThreadError: deadlock; recursive locking Fix"
description: "Fix Ruby ThreadError: deadlock; recursive locking. Resolve mutex deadlocks with proper lock ordering and Monitor."
languages: ["ruby"]
severities: ["error"]
error_types: ["thread", "deadlock"]
tags: ["deadlock", "recursive_locking", "mutex", "thread", "concurrency"]
weight: 390
---

# ThreadError: deadlock; recursive locking Fix

A `ThreadError: deadlock; recursive locking` is raised when a thread tries to lock a mutex that it already holds, or when multiple threads are waiting on each other's locks.

## Description

Deadlock occurs when two or more threads are blocked forever, each waiting for the other to release a lock. Ruby detects this and raises `ThreadError`. Recursive locking happens when a non-reentrant mutex is locked twice by the same thread.

Common scenarios:

- **Inconsistent lock ordering** — thread A locks mutex1 then mutex2, thread B locks mutex2 then mutex1.
- **Same mutex locked twice** — non-reentrant mutex locked by same thread.
- **Self-deadlock** — thread waiting on itself.
- **Lock in exception handler** — holding a lock when exception occurs.

## Common Causes

```ruby
# Cause 1: Inconsistent lock ordering
mutex1 = Mutex.new
mutex2 = Mutex.new

t1 = Thread.new { mutex1.synchronize { mutex2.synchronize { } } }
t2 = Thread.new { mutex2.synchronize { mutex1.synchronize { } } }

# Cause 2: Recursive locking with non-reentrant mutex
mutex = Mutex.new
mutex.synchronize do
  mutex.synchronize do  # ThreadError: deadlock
  end
end

# Cause 3: Lock in exception handler while holding lock
mutex = Mutex.new
mutex.synchronize do
  begin
    raise "error"
  rescue
    mutex.synchronize { }  # Deadlock
  end
end

# Cause 4: Calling method that acquires same lock
mutex = Mutex.new
def do_something(mutex)
  mutex.synchronize do
    do_something_else(mutex)  # Calls mutex.synchronize again
  end
end
```

## Solutions

### Fix 1: Always lock in consistent order

```ruby
# Wrong — inconsistent order
t1 = Thread.new { mutex1.synchronize { mutex2.synchronize { } } }
t2 = Thread.new { mutex2.synchronize { mutex1.synchronize { } } }

# Correct — consistent order everywhere
t1 = Thread.new { mutex1.synchronize { mutex2.synchronize { } } }
t2 = Thread.new { mutex1.synchronize { mutex2.synchronize { } } }
```

### Fix 2: Use Monitor for reentrant locking

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

### Fix 3: Use try_lock with timeout

```ruby
mutex1 = Mutex.new
mutex2 = Mutex.new

# Try to acquire both locks with timeout
def acquire_locks(mutex1, mutex2, timeout = 5)
  deadline = Time.now + timeout

  loop do
    if mutex1.try_lock
      if mutex2.try_lock
        return true  # Both locks acquired
      else
        mutex1.unlock
      end
    end

    if Time.now > deadline
      return false  # Timeout
    end

    sleep 0.01
  end
end
```

### Fix 4: Ensure locks are released in ensure blocks

```ruby
mutex = Mutex.new

mutex.synchronize do
  begin
    risky_operation
  ensure
    # Mutex automatically released when synchronize block exits
  end
end

# Manual lock/unlock with ensure
mutex.lock
begin
  risky_operation
ensure
  mutex.unlock
end
```

## Related Errors

- [ThreadError](thread-error) — general thread errors.
- [FiberError](fiber-error) — fiber-related errors.
- [NoMemoryError](memory-error) — memory issues from threads.
