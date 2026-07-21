---
title: "[Solution] Express Query String Error"
description: "Fix Express query string errors when URL parameters are parsed incorrectly or contain unexpected values."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A query string error in Express occurs when `req.query` contains malformed, missing, or unexpected values due to incorrect URL encoding, array syntax, or parsing issues.

## Common Causes

- Query parameters not URL-encoded by the client
- Array parameters sent without bracket syntax (`ids=1&ids=2`)
- Nested objects in query strings parsed as flat keys
- Special characters in query values break parsing
- `req.query` returns string instead of expected number or array

## How to Fix

1. Configure the query parser in Express:

```javascript
// Default parser (qs library)
app.set('query parser', 'extended');

// Simple parser (no nested objects)
app.set('query parser', 'simple');

// Disable query parsing
app.set('query parser', false);
```

2. Validate and transform query parameters:

```javascript
const { z } = require('zod');

const SearchSchema = z.object({
  query: z.string().min(1),
  page: z.coerce.number().int().min(1).default(1),
  limit: z.coerce.number().int().min(1).max(100).default(20),
  tags: z.array(z.string()).default([]),
  sort: z.enum(['asc', 'desc']).default('asc')
});

app.get('/api/search', (req, res) => {
  const result = SearchSchema.safeParse(req.query);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.flatten().fieldErrors });
  }
  const { query, page, limit, tags, sort } = result.data;
  res.json(search(query, { page, limit, tags, sort }));
});
```

3. Properly encode array parameters on the client:

```javascript
// Client sends: /api/filter?colors=red&colors=blue&colors=green
const params = new URLSearchParams();
params.append('colors', 'red');
params.append('colors', 'blue');
params.append('colors', 'green');
fetch(`/api/filter?${params.toString()}`);
```

## Examples

```javascript
// Bug: assumes page is a number but receives a string
app.get('/api/users', (req, res) => {
  const page = req.query.page; // "abc" -- not a number
  const users = User.findAll({ offset: page * 20 }); // NaN
});

// Fixed: coerce and validate
app.get('/api/users', (req, res) => {
  const page = parseInt(req.query.page, 10) || 1;
  const users = User.findAll({ offset: (page - 1) * 20 });
  res.json(users);
});
```

```text
TypeError: Cannot convert "abc" to a number
```
