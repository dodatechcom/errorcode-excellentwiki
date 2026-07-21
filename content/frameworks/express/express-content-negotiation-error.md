---
title: "[Solution] Express Content Negotiation Error"
description: "Fix Express content negotiation errors when the server returns a format the client does not accept."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A content negotiation error in Express occurs when the server and client cannot agree on a response format. This happens when the `Accept` header is not checked, or the server returns a Content-Type that does not match what the client expects.

## Common Causes

- Server always returns JSON regardless of `Accept` header
- No `res.format()` used for multi-format responses
- Content-Type set incorrectly before the body is sent
- Client sends `Accept: */*` but server expects a specific type
- API returns HTML when client expects JSON (or vice versa)

## How to Fix

1. Use `res.format()` for multi-format responses:

```javascript
app.get('/api/data', (req, res) => {
  const data = fetchData();

  res.format({
    'application/json': () => res.json(data),
    'text/html': () => res.render('data', { data }),
    'text/csv': () => {
      const csv = convertToCSV(data);
      res.set('Content-Type', 'text/csv');
      res.send(csv);
    },
    default: () => res.status(406).json({ error: 'Not Acceptable' })
  });
});
```

2. Check the `Accept` header manually when needed:

```javascript
app.get('/api/users', (req, res) => {
  const users = User.findAll();
  const accept = req.accepts(['json', 'xml', 'csv']);

  if (!accept) {
    return res.status(406).json({ error: 'Not Acceptable' });
  }

  switch (accept) {
    case 'json':
      return res.json(users);
    case 'xml':
      return res.xml(usersToXML(users));
    case 'csv':
      return res.send(usersToCSV(users));
  }
});
```

3. Set the correct Content-Type for all responses:

```javascript
app.get('/api/report', (req, res) => {
  res.type('pdf');
  generatePDF().pipe(res);
});

app.get('/api/image', (req, res) => {
  res.type('png');
  generateImage().pipe(res);
});
```

## Examples

```javascript
// Bug: always returns JSON even when client wants HTML
app.get('/api/report', (req, res) => {
  res.json(reportData); // Browser requesting HTML gets JSON
});

// Fixed: content negotiation
app.get('/api/report', (req, res) => {
  if (req.accepts('html')) {
    return res.render('report', { data: reportData });
  }
  res.json(reportData);
});
```

```text
406 Not Acceptable
```
