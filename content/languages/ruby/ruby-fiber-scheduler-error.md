---
title: "[Solution] Ruby Fiber Scheduler — Non-Blocking IO, Scheduler Not Set Errors"
description: "Fix Ruby Fiber scheduler errors. Handle non-blocking IO issues, missing scheduler, and scheduler configuration."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, fiber, scheduler, non_blocking, io"]
severity: "error"
---

# Ruby Fiber Scheduler Errors

## Error Message

```
FiberError: fiber called from scheduler not set
# or
RuntimeError: can't yield from main fiber
# or
IO::EINPROGRESSWaitWritable: Operation now in progress
```

## Common Causes

- Using `Fiber.schedule` without setting a fiber scheduler
- Calling `Fiber.yield` from the main fiber
- Mixing blocking and non-blocking IO in scheduled fibers
- Scheduler not implementing required hooks (`block`, `unblock`, `io_wait`, etc.)

## Solutions

### Solution 1: Set a Fiber Scheduler Before Using Fiber.schedule

Install a scheduler gem (like `async` or `ruby-vis`) before using non-blocking IO.

```ruby
require "async"

Async do |task|
  task.async do
    sleep(1)  # non-blocking sleep
    puts "Task 1 done"
  end

  task.async do
    sleep(0.5)
    puts "Task 2 done"
  end
end
# Both tasks run concurrently

# Or manually with a custom scheduler
class SimpleScheduler
  def block(blocker, timeout = nil)
    # Implement blocking
  end

  def unblock(blocker, fiber)
    fiber.transfer
  end
end

Fiber.set_scheduler(SimpleScheduler.new)
```

### Solution 2: Use Async Gem for Fiber Scheduling

Use the `async` gem which provides a complete fiber scheduler.

```ruby
# Gemfile: gem "async"

require "async"

Async do
  # All blocking operations are automatically non-blocking
  response = Net::HTTP.get(URI("https://api.example.com/data"))
  puts response

  # Multiple concurrent operations
  Async do
    Net::HTTP.get(URI("https://api.example.com/a"))
  end
  Async do
    Net::HTTP.get(URI("https://api.example.com/b"))
  end
end
```

### Solution 3: Handle Fiber Errors in Scheduled Code

Rescue `FiberError` when working with fibers and schedulers.

```ruby
require "async"

begin
  Async do
    fiber = Fiber.new { Fiber.yield }
    fiber.resume
  end
rescue FiberError => e
  puts "Fiber error: #{e.message}"
end

# Check if scheduler is set
if Fiber.scheduler
  puts "Scheduler active"
else
  puts "No scheduler — use Async or set one manually"
end
```

### Solution 4: Implement a Custom Fiber Scheduler

Create a minimal scheduler for non-blocking IO operations.

```ruby
class IOScheduler
  def initialize
    @ready = []
  end

  def block(blocker, timeout = nil)
    @ready << Fiber.current
    Fiber.yield
  end

  def unblock(blocker, fiber)
    @ready << fiber
  end

  def io_wait(io, event)
    Fiber.yield
  end

  def fiber(&block)
    fiber = Fiber.new(&block)
    @ready << fiber
    fiber
  end
end

Fiber.set_scheduler(IOScheduler.new)
```

## Prevention Tips

- Use the `async` gem instead of implementing custom schedulers
- Set `Fiber.set_scheduler` before any `Fiber.schedule` calls
- Avoid `Fiber.yield` from the main fiber
- Test scheduled code with `Async { ... }` blocks

## Related Errors

- [Ruby Fiber Error]({{< relref "/languages/ruby/ruby-fiber-error" >}})
- [Ruby Thread Error]({{< relref "/languages/ruby/ruby-thread-error" >}})
- [FiberError]({{< relref "/languages/ruby/fiber-error" >}})
