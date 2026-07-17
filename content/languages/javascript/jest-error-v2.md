---
title: "[Solution] Jest: Test Assertion Failed Fix"
description: "Fix Jest test assertion failures. Handle expect mismatches, async test issues, and snapshot failures."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jest", "testing", "assertion", "expect", "unit-test"]
weight: 5
---

# Jest: Test Assertion Failed

This error occurs when a Jest test's `expect()` assertion does not match the expected value. It indicates a mismatch between what the code produces and what the test expects.

## What This Error Means

Common error messages:

- `expect(received).toEqual(expected): Expected equality`
- `expect(received).toBeDefined(): Received undefined`
- `expect(received).toHaveLength(3): Received length 0`
- `expect(received).rejects.toThrow(): Didn't throw`
- `Snapshot mismatch`

Jest compares actual values against expected values. When the comparison fails, Jest shows a diff between received and expected values.

## Common Causes

```javascript
// Cause 1: Wrong return value expected
test('adds numbers', () => {
  expect(add(2, 3)).toBe(6); // actual result is 5
});

// Cause 2: Async test not awaited
test('fetches data', () => {
  const result = fetchData(); // returns Promise
  expect(result).toEqual({ name: 'Alice' }); // comparing Promise, not data
});

// Cause 3: Side effect not accounted for
test('increments counter', () => {
  counter.increment();
  expect(counter.value).toBe(1); // counter started at 1, now 2
});

// Cause 4: Mock not configured correctly
jest.mock('./api');
test('gets user', async () => {
  const user = await getUser(1);
  expect(user.name).toBe('Alice'); // mock returns undefined
});

// Cause 5: Snapshot outdated after code change
test('renders correctly', () => {
  expect(renderComponent()).toMatchSnapshot(); // snapshot stale
});
```

## How to Fix

### Fix 1: Handle async tests properly

```javascript
// ❌ Bad — comparing Promise
test('fetches data', () => {
  const result = fetchData();
  expect(result).toEqual({ name: 'Alice' });
});

// ✅ Good — use async/await
test('fetches data', async () => {
  const result = await fetchData();
  expect(result).toEqual({ name: 'Alice' });
});

// ✅ Good — use resolves
test('fetches data', async () => {
  await expect(fetchData()).resolves.toEqual({ name: 'Alice' });
});
```

### Fix 2: Reset state between tests

```javascript
let counter;

beforeEach(() => {
  counter = new Counter();
});

test('increments counter', () => {
  counter.increment();
  expect(counter.value).toBe(1);
});
```

### Fix 3: Mock return values correctly

```javascript
jest.mock('./api');
import { getUser } from './api';

test('gets user', async () => {
  getUser.mockResolvedValue({ name: 'Alice', age: 30 });

  const user = await getUser(1);
  expect(user).toEqual({ name: 'Alice', age: 30 });
});
```

### Fix 4: Use specific matchers

```javascript
// Instead of generic toEqual
expect(result).toEqual({ name: 'Alice' });

// Use more specific matchers
expect(result).toMatchObject({ name: 'Alice' });
expect(result).toHaveProperty('email');
expect(result.name).toBeTypeOf('string');
```

### Fix 5: Update snapshots after intentional changes

```bash
# Update specific snapshot
npx jest --updateSnapshot

# Or delete and regenerate
npx jest --ci -u
```

## Examples

```
FAIL  src/utils/add.test.js
  add
    ✕ adds two numbers (12 ms)

    expect(received).toBe(expected)
    Expected: 6
    Received: 5

    at Object.<anonymous> (src/utils/add.test.js:4:19)
```

```javascript
// Fix: debug by printing received value
test('adds numbers', () => {
  const result = add(2, 3);
  console.log('Result:', result); // 5
  expect(result).toBe(5);
});
```

## Related Errors

- [Jest Error]({{< relref "/languages/javascript/jest-error" >}}) — basic Jest error
- [Playwright Error V2]({{< relref "/languages/javascript/playwright-error-v2" >}}) — browser page crash
- [ReferenceError]({{< relref "/languages/javascript/referenceerror" >}}) — variable not defined
