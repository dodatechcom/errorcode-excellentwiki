---
title: "[Solution] Ruby Errno::EPIPE — Broken Pipe Fix"
description: "Fix Ruby Errno::EPIPE: broken pipe. Handle broken pipe errors in IO operations and process communication."
languages: ["ruby"]
severities: ["error"]
error_types: ["io"]
tags: ["epipe", "broken_pipe", "pipe", "io", "signal"]
weight: 270
---

# Errno::EPIPE — Broken Pipe Fix

An `Errno::EPIPE` is raised when writing to a pipe or socket whose reading end has been closed.

## Description

`Errno::EPIPE` means the process tried to write to a pipe or socket, but the other end has been closed. This commonly happens with pipes, sockets, and when writing to STDOUT after a pipe closes.

Common scenarios:

- **Pipe reader closed** — writing to a pipe after reader exits.
- **STDOUT closed** — output redirected and receiver closes.
- **Socket closed by peer** — writing to socket after remote close.
- **Process terminated** — writing to process that has exited.

## Common Causes

```ruby
# Cause 1: Writing to closed pipe
reader, writer = IO.pipe
reader.close
writer.write("data")  # Errno::EPIPE

# Cause 2: STDOUT closed after pipe
# command | ruby script.rb
# If 'command' exits, STDOUT pipe closes
puts "data"  # Errno::EPIPE

# Cause 3: Socket closed by peer
socket = TCPSocket.new("example.com", 80)
socket.close
socket.write("data")  # IOError (related)

# Cause 4: Writing to terminated process
IO.popen("exit 0", "w") do |io|
  io.write("data")  # Errno::EPIPE
end
```

## Solutions

### Fix 1: Check if pipe is open before writing

```ruby
reader, writer = IO.pipe
begin
  writer.write("data")
rescue Errno::EPIPE
  puts "Pipe reader has closed"
ensure
  reader.close rescue nil
  writer.close rescue nil
end
```

### Fix 2: Handle STDOUT pipe closure

```ruby
# Wrong
loop do
  puts "heartbeat"  # Errno::EPIPE when pipe closes
end

# Correct
begin
  loop do
    puts "heartbeat"
    $stdout.flush
  end
rescue Errno::EPIPE
  # Pipe closed, exit gracefully
  exit 0
end
```

### Fix 3: Use IO.popen correctly

```ruby
# Wrong — writing to closed process
IO.popen("exit 0", "w") do |io|
  io.write("data")
end

# Correct — check process status
IO.popen("cat", "w") do |io|
  io.write("data")
  io.close_write
  result = io.read
end
```

### Fix 4: Rescue Errno::EPIPE in signal handlers

```ruby
Signal.trap("PIPE") do
  # Handle broken pipe gracefully
  exit 0
end

# Or suppress SIGPIPE
Signal.trap("PIPE") { "DEFAULT" }
```

## Related Errors

- [IOError](io-error) — stream closed during operation.
- [Errno::ECONNREFUSED](connection-refused) — connection refused.
- [SignalException](signal-exception) — signal-based exceptions.
