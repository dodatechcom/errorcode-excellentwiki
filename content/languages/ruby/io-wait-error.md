---
title: "[Solution] Ruby IO::WaitReadable — Non-Blocking Read Fix"
description: "Fix Ruby IO::WaitReadable. Handle non-blocking I/O operations and use IO.select for readiness notifications."
languages: ["ruby"]
severities: ["error"]
error_types: ["io"]
weight: 210
---

# IO::WaitReadable — Non-Blocking Read Fix

An `IO::WaitReadable` is raised when a non-blocking read operation would block because no data is currently available.

## Description

`IO::WaitReadable` (also `IO::EAGAINWaitReadable`) is raised by non-blocking I/O operations when no data is available to read. This is common with non-blocking sockets and pipes.

Common scenarios:

- **Non-blocking socket read** — no data available yet.
- **Non-blocking pipe read** — writer hasn't sent data.
- **EAGAIN/EWOULDBLOCK** — system resource temporarily unavailable.
- **IO.select timeout** — no descriptors ready within timeout.

## Common Causes

```ruby
# Cause 1: Non-blocking read without data available
socket = TCPSocket.new("example.com", 80)
socket.read_nonblock(1024)  # IO::WaitReadable if no data ready

# Cause 2: Using IO.select with timeout
ready = IO.select([socket], [], [], 1)  # 1 second timeout
ready  # nil if timeout expires

# Cause 3: Non-blocking gets
$stdin.read_nonblock(1024)  # IO::WaitReadable

# Cause 4: Pipe read without writer
reader, writer = IO.pipe
reader.read_nonblock(1024)  # IO::WaitReadable
```

## Solutions

### Fix 1: Use IO.select to wait for readiness

```ruby
# Wrong — may raise IO::WaitReadable
socket = TCPSocket.new("example.com", 80)
data = socket.read_nonblock(1024)

# Correct — wait for socket to be readable
socket = TCPSocket.new("example.com", 80)
ready = IO.select([socket], [], [], 5)
if ready
  data = socket.read_nonblock(1024)
else
  puts "Read timed out"
end
```

### Fix 2: Rescue IO::WaitReadable

```ruby
begin
  data = socket.read_nonblock(1024)
rescue IO::WaitReadable
  IO.select([socket])
  retry
end
```

### Fix 3: Use blocking reads for simple cases

```ruby
# Wrong — non-blocking for no reason
socket = TCPSocket.new("example.com", 80)
data = socket.read_nonblock(1024)

# Correct — blocking read for simple cases
socket = TCPSocket.new("example.com", 80)
data = socket.read
```

### Fix 4: Use with_timeout for non-blocking operations

```ruby
require 'timeout'

socket = TCPSocket.new("example.com", 80)
begin
  Timeout::timeout(5) do
    data = socket.read
  end
rescue Timeout::Error
  puts "Read timed out"
end
```

## Related Errors

- [IOError](io-error) — stream closed during operation.
- [EOFError](eof-error) — end of file reached.
- [Timeout::Error](timeout-error) — operation timed out.
