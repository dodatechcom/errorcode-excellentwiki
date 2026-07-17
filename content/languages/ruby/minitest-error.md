---
title: "[Solution] Ruby Minitest Assertion Failed Fix"
description: "Fix Minitest assertion failures. Learn why Minitest tests fail and how to write correct test assertions."
languages: ["ruby"]
severities: ["error"]
error-types: ["test-error"]
weight: 5
---

## What This Error Means

A Minitest assertion failure occurs when a test assertion doesn't match the actual result. Minitest compares expected vs actual values and reports the mismatch with a failure message.

## Common Causes

- Wrong expected value in assertion
- Test state not properly isolated
- Missing setup or teardown
- Asynchronous operation not completed

## How to Fix

```ruby
# WRONG: Wrong expected value
assert_equal 5, 2 + 2  # Expected: 5, got: 4

# CORRECT: Match actual behavior
assert_equal 4, 2 + 2
```

```ruby
# WRONG: Wrong assertion method
assert "hello"  # This always passes (non-nil is truthy)

# CORRECT: Use specific assertion
assert_equal "hello", result
```

```ruby
# WRONG: Not cleaning up test state
def test_create_user
  User.create(name: "Alice")
  assert_equal 1, User.count  # May fail if other tests created users
end

# CORRECT: Use setup/teardown
def setup
  User.delete_all
end

def test_create_user
  User.create(name: "Alice")
  assert_equal 1, User.count
end
```

## Examples

```ruby
# Example 1: Common assertions
assert_equal expected, actual
assert_nil result
assert_includes array, item
assert_raises(ArgumentError) { bad_method }

# Example 2: Refute assertions
refute_nil result
refute_equal a, b
refute_includes array, item

# Example 3: Custom assertion
def assert_valid(record)
  assert record.valid?, "Expected record to be valid: #{record.errors.full_messages.join(', ')}"
end
```

## Related Errors

- [RSpec expectation failed](rspec-error) — RSpec test failure
- [Test setup error] — test environment issue
- [Assertion error] — general assertion failure
