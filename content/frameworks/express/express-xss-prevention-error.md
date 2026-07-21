---
title: "[Solution] Express XSS Prevention Error"
description: "Fix Express XSS prevention errors when user input is rendered unsafely in HTML responses."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An XSS prevention error in Express occurs when user-supplied input is included in HTML output without proper escaping, allowing cross-site scripting attacks. This typically happens when server-side templates render raw user data.

## Common Causes

- Template engine renders unescaped variables using `{{{triple braces}}}`
- JSON responses embed user data in HTML without sanitization
- DOM manipulation inserts user input via `innerHTML`
- HTTP headers contain unsanitized user-controlled values
- Error messages echo back user input without escaping

## How to Fix

1. Escape output in templates using the correct syntax:

```javascript
// EJS -- use <%%= for escaped output
// <%%= userInput %> is safe
// <%%- userInput %> is raw and dangerous

// Handlebars
// {{userInput}} is escaped by default
// {{{userInput}}} is raw -- avoid this
```

2. Sanitize user input with a library:

```javascript
const createDOMPurify = require('dompurify');
const { JSDOM } = require('jsdom');
const window = new JSDOM('').window;
const DOMPurify = createDOMPurify(window);

app.post('/comment', (req, res) => {
  const clean = DOMPurify.sanitize(req.body.comment);
  res.json({ comment: clean });
});
```

3. Set security headers with `helmet`:

```javascript
const helmet = require('helmet');
app.use(helmet());
```

## Examples

```javascript
// Vulnerable template rendering
app.get('/profile', (req, res) => {
  res.send(`<h1>Hello ${req.query.name}</h1>`);
  // URL: /profile?name=<script>alert('xss')</script>
});

// Safe rendering
app.get('/profile', (req, res) => {
  const escaped = escapeHtml(req.query.name);
  res.send(`<h1>Hello ${escaped}</h1>`);
});

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
```

```text
Refused to execute inline script because it violates the Content-Security-Policy directive
```
