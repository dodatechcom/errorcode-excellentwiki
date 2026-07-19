---
title: "[Solution] ERR_INVALID_CHAR_INDEX — String Index Out of Range Fix"
description: "Fix ERR_INVALID_CHAR_INDEX when accessing string characters at invalid positions in Node.js."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_INVALID_CHAR_INDEX

Attempting to access a character at an invalid index.

## Causes

- Multi-byte character handling with `charAt()`
- Buffer offset beyond bounds
- Encoding issues

```javascript
// Safe string access
const str = 'Hello 🌍';
console.log(str[7]); // undefined

// Use for...of for Unicode-safe iteration
for (const char of str) {
  console.log(char);
}
```
