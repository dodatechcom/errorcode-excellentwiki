---
title: "[Solution] Ruby Timeout::Error — Operation Timeout Fix"
description: "Fix Ruby Timeout::Error. Handle operation timeouts using the Timeout module and custom timeout logic."
languages: ["ruby"]
severities: ["error"]
error_types: ["timeout"]
tags: ["timeout_error", "timeout", "deadline", "deadline_exceeded"]
weight: 280
---

# Timeout::Error — Operation Timeout Fix

A `Timeout::Error` is raised when an operation exceeds its time limit. Ruby's `Timeout` module provides timeout functionality for any operation.

## Description

`Timeout::Error` is raised by the `Timeout` module when a block doesn't complete within the specified time. This is useful for network operations, external commands, and any potentially long-running code.

Common scenarios:

- **Network request timeout** — server taking too long to respond.
- **Database query timeout** — slow query exceeds time limit.
- **External command timeout** — subprocess hanging.
- **API call timeout** — third-party service slow.

## Common Causes

```ruby
# Cause 1: Network request timeout
require 'timeout'
require 'net/http'

Timeout::timeout(5) do
  response = Net::HTTP.get(URI('http://slow-server.com'))  # Timeout::Error
end

# Cause 2: Database query timeout
Timeout::timeout(30) do
  ActiveRecord::Base.connection.execute("SELECT * FROM large_table")
end

# Cause 3: External command timeout
Timeout::timeout(10) do
  system("sleep 100")  # Timeout::Error
end

# Cause 4: Recursive or infinite loop
Timeout::timeout(1) do
  loop { }  # Timeout::Error
end
```

## Solutions

### Fix 1: Rescue Timeout::Error

```ruby
# Wrong
Timeout::timeout(5) do
  response = Net::HTTP.get(URI('http://example.com'))
end

# Correct
begin
  Timeout::timeout(5) do
    response = Net::HTTP.get(URI('http://example.com'))
  end
rescue Timeout::Error
  puts "Request timed out after 5 seconds"
  response = nil
end
```

### Fix 2: Use appropriate timeout values

```ruby
# Wrong — too short
Timeout::timeout(0.1) do
  complex_calculation
end

# Correct — match expected duration
Timeout::timeout(30) do
  complex_calculation
end
```

### Fix 3: Use Timeout.timeout with cleanup

```ruby
begin
  Timeout::timeout(10) do
    risky_operation
  end
rescue Timeout::Error
  puts "Operation timed out, cleaning up..."
  cleanup
end
```

### Fix 4: Use system timeout command

```ruby
# Wrong — Ruby timeout may not kill external process
Timeout::timeout(5) do
  system("long_running_command")
end

# Correct — use system timeout
system("timeout 5 long_running_command")
```

## Related Errors

- [IOError](io-error) — stream closed during timeout.
- [Errno::ECONNREFUSED](connection-refused) — connection refused.
- [Interrupt](interrupt) — user interrupt during timeout.
