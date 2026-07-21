---
title: "[Solution] React createRoot Error"
description: "Error when createRoot called incorrectly."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when createRoot called incorrectly.

## Common Causes

Calling on null.

## How to Fix

Ensure container exists.

## Example

```javascript
const c = document.getElementById('root');
if (!c) throw new Error('No root');
createRoot(c).render(<App />);
```
