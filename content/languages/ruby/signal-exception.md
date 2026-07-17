---
title: "[Solution] Ruby SignalException — Signal Handling Fix"
description: "Handle Ruby SignalException. Catch and manage Unix signals in Ruby programs for proper signal handling."
languages: ["ruby"]
severities: ["error"]
error_types: ["signal"]
weight: 180
---

# SignalException — Signal Handling Fix

A `SignalException` is raised when a signal is received by the Ruby process. `Interrupt` is a subclass raised by `SIGINT` (Ctrl+C).

## Description

`SignalException` is the parent class for signal-related exceptions. When the process receives a signal (like `SIGTERM`, `SIGINT`, `SIGHUP`), Ruby raises `SignalException`. The `Interrupt` class is a specific subclass for `SIGINT`.

Common scenarios:

- **SIGTERM** — graceful shutdown signal from process managers.
- **SIGINT** — user interrupt (Ctrl+C).
- **SIGHUP** — terminal hangup, often used for config reload.
- **SIGUSR1/SIGUSR2** — user-defined signals for custom actions.

## Common Causes

```ruby
# Cause 1: Default signal handling
# Most signals have default handlers that terminate the process

# Cause 2: Custom signal handlers that raise
Signal.trap("USR1") { raise SignalException, "USR1" }

# Cause 3: Unhandled signals
# If no handler is set, default behavior applies

# Cause 4: Signal during critical section
# Signal arrives while holding a lock
```

## Solutions

### Fix 1: Handle specific signals

```ruby
Signal.trap("TERM") { puts "Received SIGTERM, shutting down..."; exit 0 }
Signal.trap("INT")  { puts "Received SIGINT, shutting down..."; exit 0 }
Signal.trap("HUP")  { reload_config }
Signal.trap("USR1") { rotate_logs }
```

### Fix 2: Use graceful shutdown pattern

```ruby
@running = true

Signal.trap("TERM") { @running = false }
Signal.trap("INT")  { @running = false }

while @running
  process_next_item
  sleep 0.1
end

puts "Shutting down gracefully..."
cleanup
```

### Fix 3: Block signals during critical sections

```ruby
def critical_operation
  mutex = Mutex.new

  Signal.trap("USR1") do
    mutex.synchronize { perform_action }
  end

  mutex.synchronize do
    perform_sensitive_operation
  end
end
```

### Fix 4: Handle signals with cleanup

```ruby
Signal.trap("INT") do
  begin
    cleanup
  rescue => e
    puts "Error during cleanup: #{e.message}"
  end
  exit 0
end
```

## Related Errors

- [Interrupt](interrupt) — SIGINT (Ctrl+C) specifically.
- [SystemExit](systemexit) — program exit via `exit` method.
- [Errno::EPIPE](broken-pipe) — broken pipe (related to SIGPIPE).
