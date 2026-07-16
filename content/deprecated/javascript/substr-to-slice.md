---
title: "[Solution] JavaScript String.substr() Deprecated — Use slice() Instead"
description: "Replace deprecated String.substr() with slice() or substring() in JavaScript. Modern string manipulation methods."
deprecated_function: "substr"
replacement_function: "slice"
languages: ["javascript"]
deprecated_since: "ES2015"
error_message: "substr is deprecated"
tags: ["substr", "slice", "substring", "string"]
weight: 100
---

# [Solution] JavaScript String.substr() Deprecated — Use slice() Instead

The `String.prototype.substr()` method was deprecated in the ES2015 (ES6) specification. While it is still available in most JavaScript engines for backward compatibility, it should not be used in new code. The recommended replacement is `slice()`, which is consistent with `Array.prototype.slice()` and handles edge cases more predictably. For some use cases, `substring()` is also appropriate.

## What You'll See

Using `substr()` will not immediately break your code, but linters and static analysis tools will flag it:

```
'substr' is deprecated.
```

Some strict configurations or future ECMAScript versions may throw:

```
ReferenceError: substr is not defined
```

## Why Deprecated

`substr()` was deprecated because:

- **Inconsistent behavior**: It is not part of the core ECMAScript string standard in the same way as `slice()` and `substring()`. It was originally a non-standard extension.
- **Negative start ambiguity**: With a negative `start`, `substr()` treats it as `string.length + start`, while `slice()` does the same but `substring()` does not. This inconsistency causes bugs.
- **Length vs end**: `substr(start, length)` uses a length parameter, while `slice(start, end)` uses an end index. The `end`-based approach is more common and consistent with arrays.
- **Not on Array**: There is no `Array.prototype.substr()`, but there is `Array.prototype.slice()`. Using `slice()` on both strings and arrays makes code more consistent.

## Old Code (Deprecated)

```javascript
var str = "Hello, World!";

// Extract a substring by start and length
console.log(str.substr(0, 5));    // "Hello"
console.log(str.substr(7, 5));    // "World"

// Negative start (count from end)
console.log(str.substr(-6));      // "World!"
console.log(str.substr(-6, 5));   // "World"

// Empty string
console.log(str.substr(100));     // ""

// No arguments
console.log(str.substr());        // "Hello, World!"
```

## New Code (Replacement)

```javascript
var str = "Hello, World!";

// slice() — use end index instead of length
console.log(str.slice(0, 5));     // "Hello"  (start=0, end=5)
console.log(str.slice(7, 12));    // "World"  (start=7, end=12)

// Negative start (count from end) — same behavior as substr
console.log(str.slice(-6));       // "World!"
console.log(str.slice(-6, -1));   // "World"

// substring() — similar to slice but no negative indices
console.log(str.substring(0, 5)); // "Hello"

// If you need substr's length-based behavior with slice():
function substrReplacement(str, start, length) {
  return str.slice(start, start + length);
}
console.log(substrReplacement(str, 7, 5)); // "World"

// Empty string
console.log(str.slice(100));      // ""

// No arguments — returns entire string
console.log(str.slice());         // "Hello, World!"
```

## Key Differences

| Behavior | `substr(start, len)` | `slice(start, end)` | `substring(start, end)` |
|---|---|---|---|
| Second param | Length | End index (exclusive) | End index (exclusive) |
| Negative start | `length + start` | `length + start` | Treated as `0` |
| Negative end | N/A | `length + end` | Treated as `0` |
| Start > End | Normal | Returns `""` | Swaps start and end |
| On Array | Not available | Available | Not available |

### Conversion examples

```javascript
// substr(7, 5) → slice(7, 7 + 5)
"Hello, World!".substr(7, 5) === "Hello, World!".slice(7, 12)  // true

// substr(-6) → slice(-6)
"Hello, World!".substr(-6) === "Hello, World!".slice(-6)  // true

// substr(-6, 5) → slice(-6, -1)
"Hello, World!".substr(-6, 5) === "Hello, World!".slice(-6, -1)  // true

// substr(0, 5) → slice(0, 5)
"Hello, World!".substr(0, 5) === "Hello, World!".slice(0, 5)  // true
```

## Migration Steps

1. **Find all substr() calls**:

```bash
grep -rn "\.substr\s*(" --include="*.js" /path/to/project/
```

2. **Replace `substr(start, length)` with `slice(start, start + length)`**. Add the length to the start index to get the end index.

3. **Replace `substr(start)` (no length)** with `slice(start)`. These are equivalent.

4. **Replace `substr(-n)` (negative start)** with `slice(-n)`. These are also equivalent.

5. **If you use substr frequently**, create a utility function:

```javascript
function substr(str, start, length) {
  if (length === undefined) return str.slice(start);
  return str.slice(start, start + length);
}
```

6. **Run your test suite** to verify substring extraction is correct, especially for edge cases with negative indices.

7. **Check for related deprecated patterns** like `escape()` and `unescape()`:

```bash
grep -rn "\bescape\s*(" --include="*.js" /path/to/project/
```
