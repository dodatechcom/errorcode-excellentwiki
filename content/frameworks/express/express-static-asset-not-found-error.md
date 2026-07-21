---
title: "[Solution] Express Static Asset Not Found Error"
description: "Fix Express static asset errors when CSS, JS, or image files return 404 despite being in the public directory."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A static asset not found error in Express occurs when files in the public directory are not accessible via their expected URLs, returning 404 errors for CSS, JavaScript, images, and other static resources.

## Common Causes

- `express.static()` middleware not configured
- Wrong directory path specified in static middleware
- Static middleware registered after route definitions
- File extension not included in the URL
- `index.html` not set as the default file

## How to Fix

1. Configure static file serving correctly:

```javascript
const path = require('path');

app.use(express.static(path.join(__dirname, 'public')));

// Serve from multiple directories
app.use('/assets', express.static(path.join(__dirname, 'assets')));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));
```

2. Set custom options for static files:

```javascript
app.use(express.static('public', {
  index: 'index.html',
  extensions: ['html'],
  dotfiles: 'ignore',
  maxAge: '1d',
  setHeaders: (res, filePath) => {
    if (filePath.endsWith('.css')) {
      res.set('Cache-Control', 'public, max-age=31536000');
    }
  }
}));
```

3. Serve single-page applications with a fallback route:

```javascript
app.use(express.static('public'));

// Fallback for SPA routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
```

## Examples

```javascript
// Bug: static middleware after routes
app.get('/', (req, res) => {
  res.sendFile('index.html');
});

app.use(express.static('public')); // Too late -- HTML references /style.css

// Fixed: static middleware first
app.use(express.static('public'));

app.get('/app', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
```

```text
GET /style.css 404 Not Found
GET /app.js 404 Not Found
```
