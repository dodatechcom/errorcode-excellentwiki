---
title: "[Solution] Ruby ThreadError: deadlock; recursive locking Fix"
description: "Fix ThreadError: deadlock; recursive locking in Ruby. Learn why thread deadlocks happen and how to prevent them."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, thread, deadlock, mutex, concurrency"]
severity: "error"
---

# ThreadError: deadlock; recursive locking

## Error Message

```
ThreadError: deadlock; recursive locking
```

## Common Causes

- Two or more threads acquiring locks in inconsistent order
- A thread trying to lock a Mutex it already holds (recursive locking)
- Thread waiting on another thread that is also waiting (circular dependency)
- Using Mutex with sleep or blocking calls while holding the lock

## Solutions

### Solution 1: Establish a Consistent Lock Ordering

Always acquire multiple locks in the same order across all threads to prevent circular wait conditions.

```ruby
# WRONG: Inconsistent lock ordering — deadlock risk
mutex_a = Mutex.new
mutex_b = Mutex.new

Thread.new do
  mutex_a.synchronize do
    sleep 0.1
    mutex_b.synchronize { puts "Thread 1" }  # DEADLOCK
  end
end

Thread.new do
  mutex_b.synchronize do
    sleep 0.1
    mutex_a.synchronize { puts "Thread 2" }  # DEADLOCK
  end
end

# CORRECT: Always lock in same order
Thread.new do
  mutex_a.synchronize do
    mutex_b.synchronize { puts "Thread 1" }
  end
end

Thread.new do
  mutex_a.synchronize do
    mutex_b.synchronize { puts "Thread 2" }
  end
end
```

### Solution 2: Use try_lock Instead of synchronize When Appropriate

Use try_lock to attempt acquiring a lock without blocking, allowing the thread to handle the case where the lock is unavailable.

```ruby
mutex = Mutex.new

# WRONG: Blocking wait can cause deadlock
mutex.synchronize do
  # Long operation while holding lock
  sleep 10
end

# CORRECT: Use try_lock for non-blocking attempts
if mutex.try_lock
  begin
    # Do work
  ensure
    mutex.unlock
  end
else
  puts "Lock unavailable, retrying later"
end
```

### Solution 3: Use Monitor Instead of Mutex for Reentrant Locking

Monitor allows the same thread to acquire the lock multiple times without deadlocking, unlike Mutex.

```ruby
require 'monitor'

# WRONG: Mutex deadlocks on recursive locking
mutex = Mutex.new
mutex.synchronize do
  mutex.synchronize { }  # DEADLOCK: ThreadError
end

# CORRECT: Monitor supports reentrant locking
monitor = Monitor.new
monitor.synchronize do
  monitor.synchronize do
    puts "Nested locking works"
  end
end
```

### Solution 4: Avoid Holding Locks During I/O Operations

Never perform blocking I/O or sleep while holding a Mutex, as this prevents other threads from progressing.

```ruby
# WRONG: Holding lock during I/O
mutex = Mutex.new
mutex.synchronize do
  HTTP.get("https://api.example.com")  # Blocks while holding lock
end

# CORRECT: Minimize critical section
data = nil
mutex.synchronize do
  # Only protect shared state access
  @cached_data = heavy_computation
end

# I/O outside the lock
response = HTTP.get("https://api.example.com")
mutex.synchronize do
  @cached_data = response.parse
end
```

## Prevention Tips

- Always acquire multiple locks in the same global order
- Prefer Monitor over Mutex when reentrant locking is needed
- Keep critical sections as short as possible — never do I/O inside a lock
- Use try_lock when you need to handle contention gracefully

## Related Errors

- [FiberError]({{< relref "/languages/ruby/ruby-fiber-error" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
