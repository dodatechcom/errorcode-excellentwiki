---
title: "[Solution] React Native Object.keys Enumeration Order Error"
description: "react-native Object.keys returns different enumeration order on Hermes vs JavaScriptCore when iterating over integer-like keys in JavaScript objects"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Object.keys enumeration error occurs when code relies on the property order of an object. While the ECMAScript specification requires integer-like keys to be sorted, edge cases with mixed integer and string keys produce different results between Hermes and JSC.

## Common Causes

- Object keys that are string numbers ('0', '1', '2') sorted differently
- Hermes returns keys in insertion order for all property types
- JSC sorts integer-like keys numerically before string keys
- Relying on object iteration order for rendering lists
- JSON.parse producing objects where the original JSON had a specific key order

## How to Fix

1. Use Map for ordered key-value pairs:

```javascript
// Instead of:
const data = { '2024-01': 10, '2024-02': 20 };
Object.keys(data).forEach(key => ...);

// Use:
const data = new Map([
  ['2024-01', 10],
  ['2024-02', 20],
]);
data.forEach((value, key) => ...);
```

2. Use explicit sort when order matters:

```javascript
const sortedKeys = Object.keys(data).sort((a, b) => parseInt(a) - parseInt(b));
sortedKeys.forEach(key => process(data[key]));
```

3. Use arrays instead of objects for ordered data:

```javascript
const items = [
  { period: '2024-01', value: 10 },
  { period: '2024-02', value: 20 },
];
items.forEach(item => process(item));
```

## Examples

```javascript
// Error: object keys order changes between Hermes and JSC emulator
// { '1': 'a', '2': 'b' } -> Hermes: 1, 2 / JSC: 1, 2 (same)
// { 'b': 1, 'a': 2 } -> Hermes: b, a / JSC: b, a (same)
// { '1': 'a', 'b': 'c' } -> Hermes: 1, b / JSC: 1, b (mostly same in ES2019+)
// Fix: use Map to guarantee order
```

## Related Errors

- [TypeError Undefined Object]({{< relref "/frameworks/react-native/rn-typeerror-undefined-object" >}})
