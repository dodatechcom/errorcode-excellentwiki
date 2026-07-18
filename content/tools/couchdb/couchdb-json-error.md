---
title: "[Solution] CouchDB JSON Error — How to Fix"
description: "Fix CouchDB JSON errors by validating document payloads, correcting encoding issues, and handling malformed request bodies"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB JSON Error

CouchDB JSON errors occur when request or response bodies contain invalid JSON. CouchDB requires all document bodies and API payloads to be valid JSON.

## Why It Happens

- Request body contains trailing commas
- Document body uses single quotes instead of double quotes
- Non-ASCII characters are not properly escaped
- Request body is empty or truncated
- Binary data is sent without proper encoding
- Content-Type header does not indicate JSON

## Common Error Messages

```
{ "error": "bad_request", "reason": "invalid_json" }
```

```
{ "error": "bad_request", "reason": "invalid request body" }
```

```
{ "error": "bad_request", "reason": "invalid京津" }
```

```
SyntaxError: Unexpected token in JSON
```

## How to Fix It

### 1. Validate JSON Before Sending

```bash
# Use jq to validate
echo '{"name": "test", "value": 42}' | jq .

# Common issues to fix:
# 1. Trailing commas: {"a": 1,}  -> {"a": 1}
# 2. Single quotes: {'a': 1}  -> {"a": 1}
# 3. Unquoted keys: {a: 1}  -> {"a": 1}
```

```python
import json

def validate_couchdb_doc(payload):
    try:
        doc = json.loads(payload)
        # Validate it's a dict (CouchDB documents must be objects)
        if not isinstance(doc, dict):
            raise ValueError("Document must be a JSON object")
        return doc
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        raise
```

### 2. Fix Encoding Issues

```bash
# Ensure proper UTF-8 encoding
curl -X POST http://localhost:5984/mydb \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{"name": "José", "city": "São Paulo"}'

# For binary-safe data, use base64 encoding
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: application/json" \
  -d '{"data": "'$(base64 -w0 image.png)'"}'
```

### 3. Handle Large JSON Payloads

```bash
# For large documents, use a file
cat > /tmp/couchdoc.json << 'EOF'
{
  "_id": "large_doc",
  "data": [1, 2, 3, "...thousands of items..."]
}
EOF

curl -X PUT http://localhost:5984/mydb/large_doc \
  -H "Content-Type: application/json" \
  -d @/tmp/couchdoc.json

# Verify the document was created correctly
curl http://localhost:5984/mydb/large_doc | jq '._id'
```

### 4. Debug JSON Parsing Errors

```bash
# Check what CouchDB received
curl -v -X POST http://localhost:5984/mydb \
  -H "Content-Type: application/json" \
  -d '{"broken: json}'

# Use Python for complex payloads
python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(json.dumps(data, indent=2))
except json.JSONDecodeError as e:
    print(f'Error at line {e.lineno}, col {e.colno}: {e.msg}')
    sys.exit(1)
" < payload.json
```

## Common Scenarios

- **Copy-paste introduces smart quotes**: Replace curly quotes with straight quotes.
- **JavaScript template literal has unescaped JSON**: Use `JSON.stringify()` to serialize.
- **API gateway modifies request body**: Check that the proxy does not alter the JSON payload.

## Prevent It

- Use `JSON.stringify()` in JavaScript rather than manual JSON construction
- Validate all payloads with a JSON schema validator
- Set `Content-Type: application/json` on all CouchDB API requests

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
- [CouchDB Bulk Error](/tools/couchdb/couchdb-bulk-error)
