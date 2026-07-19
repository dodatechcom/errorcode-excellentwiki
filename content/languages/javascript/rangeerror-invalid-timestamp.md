---
title: "[Solution] RangeError Invalid Date — Timestamp Range Fix"
description: "Fix RangeError: Invalid time value when creating Date with out-of-range timestamp."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# RangeError: Invalid Date

```javascript
new Date(NaN);        // Invalid Date
new Date(8.64e15 + 1); // RangeError: timestamp too large

// Fix — validate input
function safeDate(value) {
  const date = new Date(value);
  if (isNaN(date.getTime())) {
    throw new RangeError('Invalid date value');
  }
  return date;
}
```
