---
title: "[Solution] RSpec Mocks — allow/receive, Message Expectation, Spy vs Double Errors"
description: "Fix RSpec mock errors. Handle allow/receive, message expectations, doubles, and spy issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rspec, mocks, doubles, spies"]
severity: "error"
---

# RSpec Mock Errors

## Error Message

```
RSpec::Mocks::MockExpectationError: ... received :method with unexpected arguments
# or
RSpec::Mocks::ExpectationNotMetError: ... expected not to receive :method, but received it
# or
RSpec::Mocks::DoubleCrossReference: ...
```

## Common Causes

- Expecting a method call that never happens
- Mock receiving unexpected arguments
- Using `double` without defining expected methods
- Mixing doubles with real objects incorrectly

## Solutions

### Solution 1: Use allow and expect for Message Expectations

Set up expectations on what messages an object should receive.

```ruby
# Allow a method call
allow(service).to receive(:process).and_return(true)
service.process  # => true

# Expect a method call
expect(logger).to receive(:info).with("Processing")
service.process

# Expect a call with any arguments
expect(notifier).to receive(:send_message).at_least(:once)

# Don't allow unexpected calls
allow(object).to receive(:allowed_method)
object.allowed_method  # works
object.disallowed_method  # raises MockExpectationError
```

### Solution 2: Create Proper Doubles

Define expected methods on doubles for type safety.

```ruby
# Basic double
user = double("User", name: "Alice", email: "alice@example.com")
user.name  # => "Alice"

# Instance double (verifies against the real class)
user = instance_double(User)
allow(user).to receive(:name).and_return("Alice")

# Partial double (wraps real object)
real_user = User.new(name: "Bob")
allow(real_user).to receive(:save).and_return(true)
```

### Solution 3: Use Spies to Verify After the Fact

Check that a method was called after it has already been called.

```ruby
# Spy: records calls without setting up expectation
spy = spy("service")
spy.process  # calls the real method

# Verify after the fact
expect(spy).to have_received(:process)

# With arguments
expect(spy).to have_received(:process).with("data")

# Spy on a real object
allow(service).to receive(:process).and_call_original
service.process("data")
expect(service).to have_received(:process).with("data")
```

### Solution 4: Handle Unexpected Arguments Gracefully

Use argument matchers for flexible matching.

```ruby
# Match any arguments
expect(service).to receive(:call).with(anything)

# Match specific types
expect(logger).to receive(:log).with(a_string_matching(/error/))

# Match hash arguments
expect(api).to receive(:request).with(hash_including(method: :get))

# Match compound arguments
expect(service).to receive(:process).with(
  a_hash_including(name: "test"),
  an_instance_of(Integer)
)
```

## Prevention Tips

- Use `instance_double` over `double` for type checking against real classes
- Prefer `allow` + `expect` (message expectation) over `expect` (call expectation)
- Use `and_call_original` to spy on real methods without changing behavior
- Verify argument matchers match what the actual code sends

## Related Errors

- [RSpec Stub Error]({{< relref "/languages/ruby/rspec-stub-error" >}})
- [RSpec Expectation Error]({{< relref "/languages/ruby/rspec-expectation-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
