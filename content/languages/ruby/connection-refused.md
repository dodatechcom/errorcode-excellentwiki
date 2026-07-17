---
title: "[Solution] Ruby Errno::ECONNREFUSED — Connection Refused Fix"
description: "Fix Ruby Errno::ECONNREFUSED. Handle connection refused errors in TCP/UDP socket connections."
languages: ["ruby"]
severities: ["error"]
error_types: ["network"]
weight: 250
---

# Errno::ECONNREFUSED — Connection Refused Fix

An `Errno::ECONNREFUSED` is raised when a TCP connection attempt is refused by the server.

## Description

`Errno::ECONNREFUSED` means the target machine actively refused the connection. This typically means no process is listening on the specified port, or a firewall is blocking the connection.

Common scenarios:

- **Server not running** — no process listening on the port.
- **Wrong port** — connecting to a port that's not in use.
- **Firewall blocking** — firewall dropping connection attempts.
- **Server backlog full** — server can't accept more connections.

## Common Causes

```ruby
# Cause 1: Server not running
socket = TCPSocket.new("localhost", 8080)  # Errno::ECONNREFUSED

# Cause 2: Wrong port number
socket = TCPSocket.new("localhost", 3000)  # Errno::ECONNREFUSED

# Cause 3: Firewall blocking
socket = TCPSocket.new("192.168.1.100", 22)  # Errno::ECONNREFUSED

# Cause 4: Server backlog full
# Under high load, connections may be refused
100.times { TCPSocket.new("localhost", 80) }
```

## Solutions

### Fix 1: Check if server is running

```ruby
# Wrong
socket = TCPSocket.new("localhost", 8080)

# Correct
begin
  socket = TCPSocket.new("localhost", 8080)
rescue Errno::ECONNREFUSED
  puts "Server is not running on port 8080"
  puts "Start the server first"
end
```

### Fix 2: Retry with backoff

```ruby
def connect_with_retry(host, port, max_retries = 3)
  retries = 0
  begin
    TCPSocket.new(host, port)
  rescue Errno::ECONNREFUSED
    retries += 1
    if retries <= max_retries
      sleep(retries)  # Exponential backoff
      retry
    else
      raise "Could not connect after #{max_retries} retries"
    end
  end
end
```

### Fix 3: Verify port is listening

```ruby
# Check if port is open before connecting
def port_open?(host, port, timeout = 1)
  begin
    socket = TCPSocket.new(host, port)
    socket.close
    true
  rescue Errno::ECONNREFUSED, Errno::ETIMEDOUT
    false
  end
end

if port_open?("localhost", 8080)
  socket = TCPSocket.new("localhost", 8080)
else
  puts "Port 8080 is not open"
end
```

### Fix 4: Use Net::HTTP for HTTP connections

```ruby
require 'net/http'

begin
  response = Net::HTTP.get_response(URI('http://localhost:8080'))
rescue Errno::ECONNREFUSED
  puts "HTTP server not available"
rescue Net::OpenTimeout
  puts "Connection timed out"
end
```

## Related Errors

- [Errno::EADDRINUSE](address-in-use) — address already in use.
- [Errno::EPIPE](broken-pipe) — broken pipe.
- [Timeout::Error](timeout-error) — connection timed out.
