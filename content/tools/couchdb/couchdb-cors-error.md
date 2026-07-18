---
title: "[Solution] CouchDB CORS Error — How to Fix"
description: "Fix CouchDB CORS errors by configuring allowed origins, setting proper headers, and resolving preflight request failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB CORS Error

CouchDB CORS errors occur when browser-based applications cannot make cross-origin requests to the CouchDB API. Proper CORS configuration is essential for web client access.

## Why It Happens

- CORS is not enabled in CouchDB configuration
- Origin is not in the allowed origins list
- Required headers (Authorization, Content-Type) are not allowed
- Preflight (OPTIONS) request is not handled correctly
- Credentials are not enabled for authenticated requests
- Reverse proxy strips CORS headers

## Common Error Messages

```
Access to XMLHttpRequest at 'http://localhost:5984/' from origin 'http://localhost:3000'
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present
```

```
Access to fetch has been blocked by CORS policy: Response to preflight request
does not pass access control check: No 'Access-Control-Allow-Origin' header
```

```
XMLHttpRequest cannot load http://localhost:5984/_session.
Origin http://localhost:3000 is not allowed by Access-Control-Allow-Origin
```

```
CORS preflight channel did not succeed
```

## How to Fix It

### 1. Enable CORS in CouchDB

```ini
; In local.ini
[httpd]
enable_cors = true

[cors]
origins = http://localhost:3000,https://example.com
methods = GET, PUT, POST, HEAD, DELETE
headers = accept, authorization, content-type, origin, referer, x-csrf-token
credentials = true
max_age = 3600
```

```bash
# Restart CouchDB after CORS changes
sudo systemctl restart couchdb

# Verify CORS headers
curl -v -X OPTIONS http://localhost:5984/mydb \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: GET"
```

### 2. Allow Multiple Origins

```ini
[cors]
; Comma-separated list of allowed origins
origins = http://localhost:3000,http://localhost:8080,https://app.example.com,https://admin.example.com

; Or use * for all origins (NOT recommended for production)
; origins = *
```

### 3. Fix Preflight Request Issues

```javascript
// In your web application
async function couchRequest(method, path, body) {
  const response = await fetch(`http://localhost:5984${path}`, {
    method: method,
    credentials: 'include',  // Required for CORS with cookies
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: body ? JSON.stringify(body) : undefined
  });
  return response.json();
}

// Test CORS connection
couchRequest('GET', '/_session').then(data => {
  console.log('CORS working:', data);
});
```

### 4. Fix Reverse Proxy CORS Headers

```nginx
# nginx CORS configuration
location / {
    # Add CORS headers
    add_header Access-Control-Allow-Origin $http_origin always;
    add_header Access-Control-Allow-Methods "GET, PUT, POST, HEAD, DELETE" always;
    add_header Access-Control-Allow-Headers "accept, authorization, content-type, origin, referer" always;
    add_header Access-Control-Allow-Credentials true always;

    # Handle preflight
    if ($request_method = 'OPTIONS') {
        add_header Access-Control-Allow-Origin $http_origin;
        add_header Access-Control-Allow-Methods "GET, PUT, POST, HEAD, DELETE";
        add_header Access-Control-Allow-Headers "accept, authorization, content-type, origin, referer";
        add_header Access-Control-Max-Age 3600;
        return 204;
    }

    proxy_pass http://couchdb;
}
```

## Common Scenarios

- **Browser blocks requests from frontend app**: Add the app's origin to the CouchDB CORS `origins` list.
- **Authenticated requests fail**: Set `credentials = true` in CORS config.
- **Preflight fails through nginx**: Ensure nginx handles OPTIONS requests and returns CORS headers.

## Prevent It

- List specific origins instead of using wildcards in production
- Test CORS configuration with browser developer tools
- Use a reverse proxy to centralize CORS handling

## Related Pages

- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
- [CouchDB Security Error](/tools/couchdb/couchdb-security-error)
- [CouchDB SSL Error](/tools/couchdb/couchdb-ssl-error)
