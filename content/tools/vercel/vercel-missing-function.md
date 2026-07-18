---
title: "[Solution] Vercel Missing Function Error — Fix Function Not Found or Not Exported"
description: "Fix Vercel missing function errors when serverless functions cannot be found. Export functions correctly and configure the serverless function directory."
tools: ["vercel"]
error-types: ["function-error"]
severities: ["error"]
weight: 5
---

A Vercel missing function error occurs when a serverless function file is not found or does not export the expected handler. The deployment succeeds but requests to the function route return errors.

## What This Error Means

Vercel looks for serverless functions in the `api/` directory (default) or a configured functions directory. If the file is missing or the export is incorrect:

```
Error: The request could not be handled by the Serverless Function.
Function not found at /api/users
```

## Why It Happens

- The function file does not exist at the expected path
- The function does not export a default handler (for Node.js) or the correct handler name
- The function file has a syntax error or runtime error preventing the export from being read
- The functions directory is configured in vercel.json but the path is wrong
- The function uses an unsupported runtime or file extension
- The file was excluded by `.vercelignore` or build configuration

## How to Fix It

### Check Function Path

```bash
ls -la api/
```

### Export Correct Handler for Node.js

```javascript
// api/users.js — correct export
export default function handler(req, res) {
  res.status(200).json({ users: [] });
}
```

### Export Correct Handler for Python

```python
# api/users.py
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"users": []}')
```

### Export Correct Handler for Go

```go
// api/users.go
package handler

import (
    "encoding/json"
    "net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(map[string]interface{}{"users": []string{}})
}
```

### Configure Functions Directory in vercel.json

```json
{
  "functions": {
    "api/**/*.py": {
      "runtime": "@vercel/python@3.9"
    }
  }
}
```

### Verify Build Includes Functions

```bash
vercel build
ls -la .vercel/output/functions/
```

## Common Mistakes

- Forgetting to export a default handler from the function file
- Placing function files outside the api/ directory without configuration
- Using `.ts` files without proper Vercel TypeScript support configuration
- Not handling both GET and POST methods in the function
- Including the function file in .vercelignore

## Related Pages

- [Vercel Build Error]({{< relref "/tools/vercel/vercel-build-error" >}}) -- Build failures
- [Vercel Edge Function Error]({{< relref "/tools/vercel/vercel-edge-function-error" >}}) -- Edge function issues
- [Vercel Serverless Error]({{< relref "/tools/vercel/vercel-serverless-error" >}}) -- Serverless function errors
