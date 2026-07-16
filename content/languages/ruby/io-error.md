---
title: "[Solution] Ruby IOError — Stream Closed Fix"
description: "Fix Ruby IOError: stream closed. Handle closed IO streams and manage file I/O lifecycle properly."
languages: ["ruby"]
severities: ["error"]
error_types: ["io"]
tags: ["ioerror", "stream", "closed", "file", "io"]
weight: 190
---

# IOError — Stream Closed Fix

An `IOError` is raised when an I/O operation is attempted on a stream that has been closed, or when an operation is invalid for the current stream state.

## Description

Ruby I/O streams (files, sockets, pipes) must be open to read or write. Attempting to read from or write to a closed stream raises `IOError`. This commonly happens when file handles aren't properly managed.

Common scenarios:

- **Reading from closed file** — file was closed but read attempted.
- **Writing to closed stream** — output stream closed but write attempted.
- **Using `gets` after `close`** — reading from closed `STDIN`.
- **Socket closed prematurely** — network stream closed before read/write.

## Common Causes

```ruby
# Cause 1: Reading after close
file = File.open("data.txt")
file.close
file.read  # IOError: stream closed

# Cause 2: Writing after close
file = File.open("output.txt", "w")
file.close
file.write("data")  # IOError: stream closed

# Cause 3: Using gets after close
$stdin.close
gets  # IOError: stream closed

# Cause 4: Closed socket
socket = TCPSocket.new("example.com", 80)
socket.close
socket.read  # IOError: stream closed
```

## Solutions

### Fix 1: Use block form of File.open

```ruby
# Wrong — must remember to close
file = File.open("data.txt")
data = file.read
file.close

# Correct — automatically closes when block exits
File.open("data.txt") do |file|
  data = file.read
end

# Or use File.read for simple reads
data = File.read("data.txt")
```

### Fix 2: Check if stream is open before operating

```ruby
file = File.open("data.txt")
if !file.closed?
  data = file.read
end
file.close
```

### Fix 3: Use ensure for cleanup

```ruby
file = File.open("data.txt")
begin
  process(file)
ensure
  file.close
end
```

### Fix 4: Use IO.pipe for inter-process communication

```ruby
reader, writer = IO.pipe
writer.write("data")
writer.close
data = reader.read  # "data"
reader.close
```

## Related Errors

- [EOFError](eof-error) — end of file reached during read.
- [Errno::EPIPE](broken-pipe) — broken pipe error.
- [IO::WaitReadable](io-wait-error) — non-blocking read would block.
