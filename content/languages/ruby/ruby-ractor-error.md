---
title: "[Solution] Ruby Ractor — Send/Receive, Shareable Object, Isolation Errors"
description: "Fix Ruby Ractor errors. Handle send/receive failures, shareable objects, and Ractor isolation violations."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, ractor, concurrency, shareable, isolation"]
severity: "error"
---

# Ruby Ractor Errors

## Error Message

```
Ractor::Error: can't send a non shareable object from a Ractor
# or
Ractor::Error: can't move a shareable object
# or
Ractor::ClosedError: can't send to a closed Ractor
```

## Common Causes

- Sending non-shareable objects between Ractors
- Using mutable strings or arrays across Ractor boundaries
- Closing a Ractor and trying to send messages after
- Accessing shared mutable state from multiple Ractors

## Solutions

### Solution 1: Send Shareable Objects Between Ractors

Only share immutable or explicitly shareable objects between Ractors.

```ruby
# Shareable: frozen strings, numbers, symbols, frozen arrays
ractor = Ractor.new do
  msg = Ractor.receive
  puts "Received: #{msg}"
end

# Send a frozen string (shareable)
ractor.send("hello".freeze)
ractor.take  # => "hello"

# Send a number (always shareable)
ractor.send(42)
```

### Solution 2: Use Ractor.make_shareable for Deep Freezing

Deep-freeze nested structures to make them shareable across Ractors.

```ruby
# Non-shareable nested structure
data = { users: [{ name: "Alice" }, { name: "Bob" }] }
Ractor.make_shareable(data)  # deep-freezes

ractor = Ractor.new do
  data = Ractor.receive
  puts data[:users].first[:name]
end

ractor.send(data)
ractor.take  # => "Alice"
```

### Solution 3: Use Ractor Communication Patterns

Use `Ractor.receive`, `Ractor.send`, and `Ractor.select` for communication.

```ruby
# Producer-consumer pattern
producer = Ractor.new do
  5.times do |i|
    Ractor.yield "item_#{i}"
  end
end

consumer = Ractor.new do
  loop do
    item, _ = Ractor.select(producer)
    break unless item
    puts item
  end
end

consumer.take
```

### Solution 4: Handle Ractor Errors Gracefully

Rescue Ractor-specific errors for robust concurrent code.

```ruby
begin
  ractor = Ractor.new { Ractor.receive }
  ractor.send(Object.new)  # non-shareable object
rescue Ractor::Error => e
  puts "Ractor error: #{e.message}"
  ractor.close
end

# Check if Ractor is alive before sending
if ractor.alive?
  ractor.send("data".freeze)
else
  puts "Ractor is closed"
end
```

## Prevention Tips

- Use `Ractor.make_shareable` to deep-freeze data before sharing
- Communicate through messages, not shared mutable state
- Prefer immutable data structures between Ractors
- Check `Ractor.alive?` before sending messages

## Related Errors

- [Ruby Fiber Error]({{< relref "/languages/ruby/ruby-fiber-error" >}})
- [Ruby Thread Error]({{< relref "/languages/ruby/ruby-thread-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
