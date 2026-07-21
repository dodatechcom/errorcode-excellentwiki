---
title: "[Solution] Express JSONP Callback Error"
description: "Fix Express JSONP callback errors when the callback function name is missing or invalid in the request."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A JSONP callback error in Express occurs when the `callback` query parameter for JSONP responses is missing, empty, or contains invalid characters that could enable cross-site script injection.

## Common Causes

- Client sends request without `callback` query parameter
- Callback function name contains invalid JavaScript characters
- JSONP enabled globally but not all routes support it
- XSS vulnerability through unvalidated callback names
- Content-Type header set incorrectly for JSONP responses

## How to Fix

1. Use Express's built-in JSONP support with validation:

```javascript
app.set('jsonp callback name', 'cb');

app.get('/api/data', (req, res) => {
  res.jsonp({ data: 'value' });
  // If ?cb=myFunc is present, returns: myFunc({"data":"value"})
  // If no callback, returns plain JSON
});
```

2. Validate callback names to prevent XSS:

```javascript
app.get('/api/data', (req, res) => {
  const callback = req.query.callback;

  if (callback) {
    // Only allow valid JavaScript identifiers
    if (!/^[a-zA-Z_$][a-zA-Z0-9_$.]*$/.test(callback)) {
      return res.status(400).json({ error: 'Invalid callback name' });
    }

    res.set('Content-Type', 'application/javascript');
    res.send(`${callback}(${JSON.stringify({ data: 'value' })});`);
  } else {
    res.json({ data: 'value' });
  }
});
```

3. Disable JSONP when not needed:

```javascript
// Remove JSONP callback support entirely
app.set('jsonp callback', false);
```

## Examples

```javascript
// Vulnerable: callback not validated
app.get('/api/data', (req, res) => {
  const callback = req.query.callback;
  res.send(`${callback}(${JSON.stringify(data)});`);
  // Attack: ?callback=alert(document.cookie)//
});

// Safe: validated callback
app.get('/api/data', (req, res) => {
  const callback = req.query.callback;
  if (callback && /^[a-zA-Z_$][a-zA-Z0-9_]*$/.test(callback)) {
    res.set('Content-Type', 'application/javascript');
    res.send(`${callback}(${JSON.stringify(data)});`);
  } else {
    res.json(data);
  }
});
```

```text
GET /api/data?callback=alert(1)
```
