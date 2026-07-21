---
title: "[Solution] Express res.format Error"
description: "Content negotiation failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Content negotiation failing.

## Common Causes

No matching format.

## How to Fix

Add formats.

## Example

```javascript
app.get('/api', (req, res) => {
  res.format({
    'application/json': () => res.json({ d: 'ok' }),
    'text/html': () => res.send('<h1>Hi</h1>')
  });
});
```
