---
title: "[Solution] Node.js ERR_ASSERTION — Assertion Error Fix"
description: "Fix Node.js ERR_ASSERTION when an assertion expression evaluates to false. Resolve failed assertions in Node.js applications."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_ASSERTION — Assertion Error Fix

The `ERR_ASSERTION` error occurs when an assertion expression evaluates to `false`. Node.js uses the `assert` module to verify assumptions in code, and when an assertion fails, this error is thrown.

## Description

Common ERR_ASSERTION messages include:

- `AssertionError: false == true` — strict equality assertion failed.
- `AssertionError: 0 === 1` — strict equality check failed.
- `AssertionError: Missing expected value` — expected value was not provided.
- `ERR_ASSERTION: "expression"` — a general assertion failure.

## Common Causes

```javascript
const assert = require("node:assert");

// Cause 1: Strict equality check fails
assert.strictEqual(1, 2); // ERR_ASSERTION: 1 === 2

// Cause 2: Deep equality check fails
assert.deepStrictEqual({ a: 1 }, { a: 2 }); // ERR_ASSERTION

// Cause 3: Truthy check fails
assert.ok(null); // ERR_ASSERTION: falsy value

// Cause 4: Throws unexpected error
assert.throws(() => {}, /expected error/); // ERR_ASSERTION: no error thrown
```

## Solutions

### Fix 1: Use proper assertion methods

```javascript
const assert = require("node:assert");

// Instead of assert.ok(value === expected), use assert.strictEqual
assert.strictEqual(actual, expected, "Values should be equal");

// Instead of assert.ok(obj), use assert.ok with a message
assert.ok(value !== null && value !== undefined, "Value must be provided");
```

### Fix 2: Add descriptive assertion messages

```javascript
const assert = require("node:assert");

function processUser(user) {
  assert.ok(user, "User object must be provided");
  assert.strictEqual(typeof user.name, "string", "User name must be a string");
  assert.ok(user.age >= 0, "User age must be non-negative");
  return user;
}

// This gives clear error messages when assertions fail
processUser({ name: "Alice", age: 30 });
```

### Fix 3: Use assert.ifError for error-first callbacks

```javascript
const assert = require("node:assert");

function fetchData(callback) {
  // If err is truthy, assert.ifError throws it
  someAsyncOp((err, data) => {
    assert.ifError(err); // throws ERR_ASSERTION if err is truthy
    callback(null, data);
  });
}
```

### Fix 4: Handle assertions gracefully in production

```javascript
const assert = require("node:assert");

// Use assert in development, validate with throws in production
function validateConfig(config) {
  try {
    assert.ok(config.port > 0, "Port must be positive");
    assert.ok(config.host, "Host must be provided");
    return true;
  } catch (e) {
    console.error("Configuration validation failed:", e.message);
    return false;
  }
}
```

## Examples

```javascript
const assert = require("node:assert");

// ERR_ASSERTION in a test suite
describe("Calculator", () => {
  it("should add two numbers", () => {
    const result = add(1, 2);
    assert.strictEqual(result, 3); // passes
  });

  it("should not return negative", () => {
    const result = add(-1, -2);
    assert.ok(result >= 0); // ERR_ASSERTION: -3 is not >= 0
  });
});
```

## Related Errors

- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — invalid syntax in code.
- [TypeError]({{< relref "/languages/javascript/typeerror" >}}) — wrong type used.
- [ReferenceError]({{< relref "/languages/javascript/referenceerror" >}}) — undefined variable reference.
- [RangeError]({{< relref "/languages/javascript/rangeerror" >}}) — value outside valid range.
