---
title: "[Solution] Express URL Encoding Error"
description: "Fix Express URL encoding errors when percent-encoded characters in URLs are not decoded correctly."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A URL encoding error in Express occurs when percent-encoded characters in the URL path or query string are decoded incorrectly, causing route mismatches or broken parameter values.

## Common Causes

- Client sends unencoded special characters in URLs
- Double-encoded characters in path or query parameters
- `req.params` contains `%20` instead of spaces
- Unicode characters not properly encoded
- Middleware modifies the URL without re-encoding

## How to Fix

1. Configure Express to handle URL encoding properly:

```javascript
app.set('query parser', 'extended');

// Ensure body parser handles URL-encoded data
app.use(express.urlencoded({ extended: true }));
```

2. Decode and validate URL parameters:

```javascript
app.get('/api/search/:query', (req, res) => {
  const query = decodeURIComponent(req.params.query);
  const results = searchIndex(query);
  res.json(results);
});

// Or use Express's built-in decoding
app.get('/api/files/:filename', (req, res) => {
  // Express decodes %20 to spaces automatically
  const filename = req.params.filename;
  res.sendFile(path.join(__dirname, 'files', filename));
});
```

3. Handle double encoding:

```javascript
function safeDecode(str) {
  try {
    let decoded = decodeURIComponent(str);
    // Handle double encoding
    if (decoded.includes('%')) {
      decoded = decodeURIComponent(decoded);
    }
    return decoded;
  } catch {
    return str;
  }
}

app.get('/api/items/:name', (req, res) => {
  const name = safeDecode(req.params.name);
  const item = findByName(name);
  res.json(item);
});
```

## Examples

```javascript
// Bug: raw URL contains encoded characters
app.get('/api/users/:name', (req, res) => {
  console.log(req.params.name); // "John%20Doe" instead of "John Doe"
  const user = findByName(req.params.name); // No match
});

// Fixed: Express auto-decodes params
app.get('/api/users/:name', (req, res) => {
  console.log(req.params.name); // "John Doe"
  const user = findByName(req.params.name);
  res.json(user);
});
```

```text
GET /api/users/John%20Doe
// Client sends: /api/users/John%2520Doe (double-encoded)
```
