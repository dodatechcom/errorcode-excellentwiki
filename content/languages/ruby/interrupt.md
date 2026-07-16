---
title: "[Solution] Ruby Interrupt — User Interrupt Fix"
description: "Handle Ruby Interrupt (SignalException). Catch Ctrl+C and manage graceful shutdown in scripts and servers."
languages: ["ruby"]
severities: ["error"]
error_types: ["signal"]
tags: ["interrupt", "signal", "ctrl_c", "shutdown", "signal_exception"]
weight: 160
---

# Interrupt — User Interrupt Fix

An `Interrupt` is raised when the user sends an interrupt signal (typically Ctrl+C) to a running Ruby program.

## Description

`Interrupt` is a subclass of `SignalException`. It's raised when the process receives a `SIGINT` signal, usually from pressing Ctrl+C. By default, this terminates the program.

Common scenarios:

- **Ctrl+C in terminal** — user interrupts a long-running script.
- **Long computation** — script takes too long and user cancels.
- **Network operations** — user interrupts during I/O wait.
- **Interactive programs** — user wants to exit gracefully.

## Common Causes

```ruby
# Cause 1: Long-running loop without interrupt handling
loop do
  heavy_computation  # User presses Ctrl+C
end

# Cause 2: Blocking I/O
socket.read  # User presses Ctrl+C while waiting

# Cause 3: Sleep without interrupt handling
sleep 100  # User presses Ctrl+C to skip wait

# Cause 4: Signal handling not implemented
# Most Ruby scripts don't handle Interrupt by default
```

## Solutions

### Fix 1: Rescue Interrupt for graceful shutdown

```ruby
# Wrong — no graceful shutdown
loop do
  process_next_item
end

# Correct — handle Interrupt gracefully
begin
  loop do
    process_next_item
  end
rescue Interrupt
  puts "\nShutting down gracefully..."
  cleanup
  exit 0
end
```

### Fix 2: Use signal handlers

```ruby
# Wrong — relying on default behavior
loop do
  work
end

# Correct — install signal handler
Signal.trap("INT") do
  puts "\nReceived interrupt, cleaning up..."
  cleanup
  exit 0
end

loop do
  work
end
```

### Fix 3: Use ensure for cleanup

```ruby
# Wrong — cleanup may not run
begin
  do_work
rescue Interrupt
  puts "Interrupted"
end

# Correct — ensure runs even on Interrupt
begin
  do_work
ensure
  cleanup  # Always runs, even on Interrupt
end
```

### Fix 4: Handle Interrupt in servers

```ruby
require 'webrick'

server = WEBrick::HTTPServer.new(Port: 8080)

# Handle shutdown gracefully
['INT', 'TERM'].each do |signal|
  Signal.trap(signal) do
    puts "\nShutting down server..."
    server.shutdown
  end
end

server.start
```

## Related Errors

- [SignalException](signal-exception) — parent class for signal-based errors.
- [SystemExit](systemexit) — program exit via `exit` method.
- [IOError](io-error) — stream closed during interrupt.
