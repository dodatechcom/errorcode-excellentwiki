---
title: "Flutter Web - CORS error"
description: "Flutter Web application encounters Cross-Origin Resource Sharing errors when making API requests"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A CORS error in Flutter Web occurs when the browser blocks HTTP requests to a different origin (domain, port, or protocol) that does not include the proper CORS headers. This only affects the web platform and is a browser security restriction.

## Common Causes

- API server does not return CORS headers
- API called from Flutter Web without proper headers
- Development server not configured for CORS
- Preflight OPTIONS request rejected by server
- Using `http://` to call an `https://` API

## How to Fix

1. Configure the API server to return CORS headers:

```nginx
# nginx configuration
location /api/ {
  add_header Access-Control-Allow-Origin *;
  add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
  add_header Access-Control-Allow-Headers "Content-Type, Authorization";
  if ($request_method = OPTIONS) {
    return 204;
  }
}
```

2. Use a proxy in development:

```yaml
# web/index.html or use a proxy server
```

```bash
# Flutter dev proxy
flutter run -d chrome --web-browser-flag="--disable-web-security"
```

3. Use a proxy server to avoid CORS:

```dart
// Use a backend proxy instead of direct API calls
final response = await http.get(
  Uri.parse('https://your-proxy.com/api/data'),
);
```

4. Enable CORS in Express.js:

```javascript
const cors = require('cors');
app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
}));
```

5. Check the browser console for specific CORS errors:

```bash
flutter run -d chrome
# Open browser DevTools > Console tab
```

## Examples

```dart
// Error: Access to XMLHttpRequest has been blocked by CORS policy
final response = await http.get(
  Uri.parse('https://api.example.com/data'),
);
// No 'Access-Control-Allow-Origin' header is present

// Fix: configure server or use proxy
final response = await http.get(
  Uri.parse('https://api.example.com/data'),
  headers: {'Origin': 'https://your-flutter-web-app.com'},
);
```

## Related Errors

- [Network error]({{< relref "/frameworks/flutter/flutter-network-error-v2" >}})
- [Platform error]({{< relref "/frameworks/flutter/flutter-platform-error-v2" >}})
