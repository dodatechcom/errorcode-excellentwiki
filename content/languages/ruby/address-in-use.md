---
title: "[Solution] Ruby Errno::EADDRINUSE — Address Already in Use Fix"
description: "Fix Ruby Errno::EADDRINUSE. Handle address already in use errors when binding to ports."
languages: ["ruby"]
severities: ["error"]
error_types: ["network"]
tags: ["eaddrinuse", "address_in_use", "port", "socket", "server"]
weight: 260
---

# Errno::EADDRINUSE — Address Already in Use Fix

An `Errno::EADDRINUSE` is raised when trying to bind to a port or address that's already in use by another process.

## Description

`Errno::EADDRINUSE` means the port or address you're trying to use is already bound by another socket. This is common when starting servers.

Common scenarios:

- **Server already running** — another instance is using the port.
- **Port in TIME_WAIT** — previous connection hasn't fully closed.
- **Wrong bind address** — trying to bind to a specific IP that's taken.
- **SO_REUSEADDR not set** — socket option not configured.

## Common Causes

```ruby
# Cause 1: Server already running
server = TCPServer.new("0.0.0.0", 8080)  # Errno::EADDRINUSE

# Cause 2: Port in TIME_WAIT state
# Previous server instance closed but port not released yet

# Cause 3: Another process using the port
# Different application listening on same port

# Cause 4: Trying to bind to both 0.0.0.0 and specific IP
# Already bound to 0.0.0.0:8080, trying 127.0.0.1:8080
```

## Solutions

### Fix 1: Check if port is in use

```ruby
def port_in_use?(port)
  begin
    server = TCPServer.new("0.0.0.0", port)
    server.close
    false
  rescue Errno::EADDRINUSE
    true
  end
end

if port_in_use?(8080)
  puts "Port 8080 is already in use"
else
  server = TCPServer.new("0.0.0.0", 8080)
end
```

### Fix 2: Use SO_REUSEADDR

```ruby
require 'socket'

server = TCPServer.new("0.0.0.0", 8080)
server.setsockopt(Socket::SOL_SOCKET, Socket::SO_REUSEADDR, 1)
```

### Fix 3: Kill existing process using the port

```bash
# Find process using port 8080
lsof -i :8080

# Or use netstat
netstat -tlnp | grep 8080

# Kill the process
kill -9 <PID>
```

### Fix 4: Wait and retry

```ruby
def start_server(port, retries = 5)
  retries.times do |i|
    begin
      return TCPServer.new("0.0.0.0", port)
    rescue Errno::EADDRINUSE
      puts "Port #{port} in use, retrying in #{i + 1} seconds..."
      sleep(i + 1)
    end
  end
  raise "Could not bind to port #{port} after #{retries} retries"
end
```

## Related Errors

- [Errno::ECONNREFUSED](connection-refused) — connection refused.
- [Errno::EPIPE](broken-pipe) — broken pipe.
- [IOError](io-error) — stream closed or invalid I/O.
