---
title: "[Solution] CouchDB Replication CORS Error — How to Fix"
description: "Fix CouchDB replication CORS errors by resolving cross-origin resource sharing issues during replication, fixing CORS configuration problems, and handling browser-based replication failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication CORS Error

CouchDB replication CORS errors occur when cross-origin requests fail during browser-based or cross-domain replication.

## Why It Happens

- CORS headers are missing from CouchDB response
- Origin is not allowed in CouchDB configuration
- Preflight OPTIONS request is rejected
- Credentials are not allowed with CORS
- Methods not allowed in CORS configuration
- Headers not allowed in CORS configuration

## Common Error Messages

```
Access to XMLHttpRequest blocked by CORS policy
```

```
{ "error": "forbidden", "reason": "CORS request denied" }
```

```
{ "error": "forbidden", "reason": "Origin not allowed" }
```

```
{ "error": "forbidden", "reason": "Method not allowed by CORS" }
```

## How to Fix It

### 1. Check CORS Configuration

```bash
# Check current CORS settings
curl http://localhost:5984/_node/_local/_config/httpd | jq '.enable_cors, .cors_origins'

# Test CORS headers
curl -I -X OPTIONS http://localhost:5984/mydb \
  -H "Origin: http://example.com" \
  -H "Access-Control-Request-Method: GET"
```

### 2. Enable CORS

```bash
# Enable CORS
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/enable_cors \
  -H "Content-Type: text/plain" \
  -d '"true"'

# Allow specific origins
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/cors_origins \
  -H "Content-Type: text/plain" \
  -d '"http://example.com,http://localhost:3000"'

# Allow all origins (not recommended for production)
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/cors_origins \
  -H "Content-Type: text/plain" \
  -d '"*"'
```

### 3. Configure CORS Headers

```bash
# Allow credentials
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/cors_credentials \
  -H "Content-Type: text/plain" \
  -d '"true"'

# Allow methods
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/cors_methods \
  -H "Content-Type: text/plain" \
  -d '"GET, PUT, POST, HEAD, DELETE"'

# Allow headers
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/cors_headers \
  -H "Content-Type: text/plain" \
  -d '"accept, authorization, content-type, origin, referer"'
```

### 4. Test CORS

```bash
# Test CORS request
curl -v -X GET http://localhost:5984/mydb \
  -H "Origin: http://example.com"

# Check response headers
curl -I http://localhost:5984/mydb \
  -H "Origin: http://example.com"
```

## Common Scenarios

- **CORS not enabled**: Enable CORS in CouchDB configuration.
- **Origin not allowed**: Add origin to cors_origins.
- **Credentials blocked**: Enable cors_credentials.

## Prevent It

- Configure CORS properly for your use case
- Use specific origins instead of wildcards in production
- Test CORS configuration before deployment

## Related Pages

- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
- [CouchDB Security Error](/tools/couchdb/couchdb-security-error)
- [CouchDB Configuration Error](/tools/couchdb/couchdb-config-error)
