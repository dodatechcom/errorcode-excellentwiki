---
title: "[Solution] RangeError Invalid repeat count — String.repeat() Fix"
description: "Fix RangeError when calling String.repeat() with negative or too-large count."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Invalid Repeat Count

```javascript
'hello'.repeat(-1);    // RangeError
'hello'.repeat(2**53); // RangeError

// Fix — validate count
function safeRepeat(str, count) {
  if (count < 0 || count > str.length * 1000) {
    throw new RangeError('Invalid repeat count');
  }
  return str.repeat(count);
}
```
