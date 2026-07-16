---
title: "[Solution] Ruby EOFError — End of File Fix"
description: "Fix Ruby EOFError: end of file reached. Handle end-of-file conditions in gets, readline, and IO operations."
languages: ["ruby"]
severities: ["error"]
error_types: ["io"]
tags: ["eoferror", "eof", "end_of_file", "gets", "readline"]
weight: 200
---

# EOFError — End of File Fix

An `EOFError` is raised when the end of a file or stream is reached during a read operation like `gets` or `readline`.

## Description

`EOFError` occurs when you try to read beyond the end of a stream. This is common with interactive input (`STDIN`), network sockets, and sequential file reads.

Common scenarios:

- **STDIN at EOF** — input redirected from file or pipe ends.
- **Socket closed by peer** — remote end closed connection.
- **Reading past end of file** — multiple reads without checking EOF.
- **gets on empty stream** — no data available.

## Common Causes

```ruby
# Cause 1: STDIN at EOF (piped input)
line1 = gets  # "hello"
line2 = gets  # EOFError if only one line available

# Cause 2: Socket closed by remote end
socket = TCPSocket.new("example.com", 80)
socket.gets  # EOFError if connection closed

# Cause 3: Reading after all data consumed
file = File.open("data.txt")
file.gets  # First line
file.gets  # Second line
file.gets  # EOFError if file has only 2 lines
```

## Solutions

### Fix 1: Check for nil return from gets

```ruby
# Wrong — doesn't handle EOF
line = gets
puts line.upcase  # NoMethodError on nil

# Correct — gets returns nil at EOF
while (line = gets)
  puts line.chomp
end
```

### Fix 2: Use readline with EOF rescue

```ruby
begin
  line = STDIN.readline
rescue EOFError
  break
end
```

### Fix 3: Use IO.foreach for file iteration

```ruby
# Correct — handles EOF automatically
File.foreach("data.txt") do |line|
  process(line)
end
```

### Fix 4: Handle socket EOF

```ruby
socket = TCPSocket.new("example.com", 80)
begin
  while (line = socket.gets)
    process(line)
  end
rescue EOFError
  puts "Connection closed by remote end"
ensure
  socket.close
end
```

## Related Errors

- [IOError](io-error) — stream closed during operation.
- [Errno::ECONNRESET](connection-refused) — connection reset by peer.
- [IO::WaitReadable](io-wait-error) — read would block (non-blocking I/O).
