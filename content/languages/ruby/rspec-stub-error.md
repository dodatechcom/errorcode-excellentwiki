---
title: "[Solution] RSpec Stubs — and_return, and_raise, and_call_original Errors"
description: "Fix RSpec stub errors. Handle and_return, and_raise, stub chains, and call original method issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rspec, stubs, mock, test"]
severity: "error"
---

# RSpec Stub Errors

## Error Message

```
NoMethodError: undefined method `and_return' for ...
# or
RSpec::Mocks::MockExpectationError: ... received :method but originally received :method
# or
RuntimeError: already initialized as a double
```

## Common Causes

- Using `and_return` on the wrong expectation type
- Stubbing a method that doesn't exist on the object
- Re-stubbing a method without clearing the original stub
- Not using `and_call_original` when you need the real behavior

## Solutions

### Solution 1: Use and_return for Stubbing

Return specific values from stubbed methods.

```ruby
# Stub a method to return a value
allow(service).to receive(:fetch).and_return({ status: "ok" })

# Multiple return values (called in sequence)
allow(queue).to receive(:pop).and_return("first", "second", "third")
queue.pop  # => "first"
queue.pop  # => "second"
queue.pop  # => "third"

# Return based on arguments
allow(calculator).to receive(:add).and_return(0)
allow(calculator).to receive(:add).with(1, 1).and_return(2)
```

### Solution 2: Use and_raise and and_yield

Simulate exceptions and block behavior.

```ruby
# Raise an exception
allow(api).to receive(:request).and_raise(Net::TimeoutError, "timed out")

# Yield a value
allow(File).to receive(:open).and_yield(StringIO.new("content"))

# Yield multiple times
allow(iterator).to receive(:each).and_yield(1).and_yield(2)
```

### Solution 3: Use and_call_original to Preserve Real Behavior

Keep the original method behavior while adding spy capability.

```ruby
# Spy on a real method
allow(service).to receive(:process).and_call_original
service.process("data")

# Verify it was called
expect(service).to have_received(:process).with("data")

# Partial double: stub some methods, keep others real
real_user = User.new(name: "Alice")
allow(real_user).to receive(:save).and_call_original
real_user.save  # calls the real save method
```

### Solution 4: Clear Stubs Between Tests

Avoid stub leaks by clearing stubs properly.

```ruby
before do
  allow(service).to receive(:call).and_return("stubbed")
end

after do
  # Stubs are automatically cleared between examples
  # But if using around blocks, clear manually:
  RSpec::Mocks.space.proxy_for(service).reset
end

# Or use verify_partial_doubles to ensure stubs match real interface
config.verify_partial_doubles = true
```

## Prevention Tips

- Use `and_return` for return values, `and_raise` for exceptions
- Use `and_call_original` when you need the real method behavior
- Set `config.verify_partial_doubles = true` in `rails_helper.rb`
- Stubs are auto-cleared between examples — no manual cleanup needed

## Related Errors

- [RSpec Mock Error]({{< relref "/languages/ruby/rspec-mock-error" >}})
- [RSpec Expectation Error]({{< relref "/languages/ruby/rspec-expectation-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
