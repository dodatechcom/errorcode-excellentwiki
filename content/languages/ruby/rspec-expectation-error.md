---
title: "[Solution] RSpec Expectation — Matcher Chain, Block Expectation, Compound Errors"
description: "Fix RSpec expectation errors. Handle matcher chains, block expectations, and compound assertion failures."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rspec, expectations, matchers, assertion"]
severity: "error"
---

# RSpec Expectation Errors

## Error Message

```
RSpec::Expectations::ExpectationNotMetError: expected: ... got: ...
# or
NoMethodError: undefined method `to' for ...
# or
RSpec::Expectations::BlockExpectationNeeded: ...
```

## Common Causes

- Using value matchers on blocks (need block expectations)
- Using block expectations on non-block expressions
- Wrong matcher chain for the assertion
- Incorrect `include`, `contain_exactly`, or `match` usage

## Solutions

### Solution 1: Use Block Expectations for Code That Raises or Changes State

Use `expect { }` (block) instead of `expect(value)` for side effects.

```ruby
# BAD: value expectation for method that raises
expect { raise "error" }.to raise_error  # wrong!

# GOOD: block expectation
expect { raise("error") }.to raise_error(RuntimeError, "error")

# BAD: checking side effects
expect(queue.size).to change(queue, :size).by(1)

# GOOD: block expectation for change
expect { queue.push("item") }.to change(queue, :size).by(1)
```

### Solution 2: Chain Matchers Correctly

Use proper matcher syntax and chaining.

```ruby
# Equality
expect(result).to eq(42)
expect(result).to eql(42)
expect(result).to be(42)  # same object

# Comparison
expect(value).to be > 10
expect(value).to be_within(0.1).of(3.14)

# String matching
expect(output).to include("success")
expect(name).to start_with("test")
expect(name).to end_with("_spec.rb")
```

### Solution 3: Use Compound Expectations

Combine multiple assertions in one test.

```ruby
# Compound expectations with `and`
expect(user).to be_valid
  .and have_attributes(name: "Alice", email: "alice@example.com")

# Using `and` for multiple assertions
expect(response).to have_http_status(:ok)
expect(response.content_type).to include("json")

# Or use aggregate_failures for multiple failures
aggregate_failures do
  expect(user).to be_valid
  expect(user.email).to be_present
  expect(user.name).to eq("Alice")
end
```

### Solution 4: Use Custom Matchers for Complex Assertions

Build reusable matchers for repeated patterns.

```ruby
# spec/support/matchers/be_valid_with.rb
RSpec::Matchers.define :be_valid_with do |expected|
  match do |record|
    record.assign_attributes(expected)
    record.valid?
  end

  failure_message do |record|
    "expected #{record.class} to be valid with #{expected}, but got: #{record.errors.full_messages}"
  end
end

# Usage
expect(user).to be_valid_with(email: "test@example.com", name: "Test")
```

## Prevention Tips

- Use `expect { }` for block expectations, `expect(value)` for value expectations
- Use `aggregate_failures` to see all failures in one run
- Chain matchers in the order: `expect(value).to matcher1.and matcher2`
- Read error messages carefully — they show expected vs actual values

## Related Errors

- [RSpec Mock Error]({{< relref "/languages/ruby/rspec-mock-error" >}})
- [RSpec Stub Error]({{< relref "/languages/ruby/rspec-stub-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
