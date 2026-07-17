---
title: "[Solution] Ruby RSpec Expectation Failed Fix"
description: "Fix RSpec expectation failures. Learn why RSpec tests fail and how to write correct test expectations."
languages: ["ruby"]
severities: ["error"]
error-types: ["test-error"]
weight: 5
---

## What This Error Means

An RSpec expectation failure occurs when an assertion in your test doesn't match the actual result. RSpec compares expected vs actual values and reports the mismatch with detailed diff output.

## Common Causes

- Wrong expected value in test
- Side effects changing test state
- Asynchronous operations not awaited
- Stub/mock not configured correctly

## How to Fix

```ruby
# WRONG: Wrong expected value
expect(2 + 2).to eq(5)  # Expected: 5, got: 4

# CORRECT: Match actual behavior
expect(2 + 2).to eq(4)
```

```ruby
# WRONG: Missing block expectation
expect(-> { raise "error" }).to raise_error  # Missing block

# CORRECT: Use block form for method calls
expect { raise "error" }.to raise_error(RuntimeError, "error")
```

```ruby
# WRONG: Stub not matching
allow(Service).to receive(:call).and_return("ok")
result = Service.call("wrong arg")  # Stub not matched

# CORRECT: Match arguments or use receive_any_instance_of
allow(Service).to receive(:call).and_return("ok")
result = Service.call(anything)  # Matches any argument
```

## Examples

```ruby
# Example 1: Common matchers
expect(value).to eq(42)
expect(value).to be > 10
expect(value).to include("hello")
expect { code }.to change { count }.by(1)

# Example 2: Failure messages
# Expected: 5
# Got: 4
# Diff:
# - 5
# + 4

# Example 3: Custom matcher
RSpec::Matchers.define :be_valid_user do
  match { |user| user.valid? && user.persisted? }
end
expect(user).to be_valid_user
```

## Related Errors

- [Minitest assertion failed](minitest-error) — Minitest test failure
- [RSpec setup error] — test environment issue
- [RSpec mock error] — mock/stub failure
