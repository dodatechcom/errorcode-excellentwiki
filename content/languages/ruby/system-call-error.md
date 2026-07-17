---
title: "[Solution] Ruby Errno Errors — System Call Error Fix"
description: "Fix Ruby Errno::EACCES, Errno::ENOENT, and other system call errors. Handle OS-level errors in file and network operations."
languages: ["ruby"]
severities: ["error"]
error_types: ["system_call"]
weight: 220
---

# Errno Errors — System Call Error Fix

Ruby `Errno` exceptions represent operating system-level errors. Each `Errno` subclass corresponds to a specific POSIX error code.

## Description

When a system call fails (file operations, network I/O, process management), Ruby raises the appropriate `Errno` exception. These map directly to C `errno` values.

Common scenarios:

- **File not found** — `Errno::ENOENT` (No such file or directory).
- **Permission denied** — `Errno::EACCES` (Permission denied).
- **Connection refused** — `Errno::ECONNREFUSED`.
- **Address in use** — `Errno::EADDRINUSE`.
- **Broken pipe** — `Errno::EPIPE`.

## Common Causes

```ruby
# Cause 1: File doesn't exist
File.read("missing.txt")  # Errno::ENOENT

# Cause 2: Permission denied
File.read("/etc/shadow")  # Errno::EACCES

# Cause 3: Connection refused
TCPSocket.new("localhost", 9999)  # Errno::ECONNREFUSED

# Cause 4: Address already in use
server = TCPServer.new("0.0.0.0", 80)  # Errno::EADDRINUSE

# Cause 5: Broken pipe
pipe = IO.pipe
pipe[1].close
pipe[0].write("data")  # Errno::EPIPE
```

## Solutions

### Fix 1: Rescue specific Errno exceptions

```ruby
# Wrong — rescuing all exceptions
begin
  file = File.read("data.txt")
rescue => e
  puts e.message
end

# Correct — rescue specific Errno
begin
  file = File.read("data.txt")
rescue Errno::ENOENT
  puts "File not found"
rescue Errno::EACCES
  puts "Permission denied"
rescue Errno::ECONNREFUSED
  puts "Connection refused"
end
```

### Fix 2: Check file existence before access

```ruby
# Wrong
data = File.read("data.txt")  # May raise Errno::ENOENT

# Correct
if File.exist?("data.txt")
  data = File.read("data.txt")
else
  puts "File not found"
end
```

### Fix 3: Handle network errors gracefully

```ruby
begin
  socket = TCPSocket.new("example.com", 80)
  socket.write("GET / HTTP/1.0\r\n\r\n")
  response = socket.read
rescue Errno::ECONNREFUSED
  puts "Server refused connection"
rescue Errno::ECONNRESET
  puts "Connection reset by server"
rescue Errno::EHOSTUNREACH
  puts "Host unreachable"
ensure
  socket&.close
end
```

### Fix 4: Use error codes for custom handling

```ruby
begin
  File.delete("file.txt")
rescue Errno::ENOENT => e
  puts "File not found: #{e.message}"
  puts "Errno code: #{e.errno}"
rescue Errno::EACCES => e
  puts "Permission denied: #{e.message}"
end
```

## Related Errors

- [Errno::ENOENT](file-not-found) — file or directory not found.
- [Errno::EACCES](permission-denied) — permission denied.
- [IOError](io-error) — stream closed or invalid I/O.
