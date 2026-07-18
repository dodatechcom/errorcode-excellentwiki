---
title: "[Solution] CouchDB Attachment Error — How to Fix"
description: "Fix CouchDB attachment errors by resolving content-type mismatches, fixing multipart parsing issues, and handling large binary uploads"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Attachment Error

CouchDB attachment errors occur when uploading, reading, or serving document attachments fails. Issues range from content-type mismatches to multipart parsing failures.

## Why It Happens

- Content-Type header does not match actual attachment data
- Multipart MIME boundaries are malformed
- Attachment exceeds document size limits
- Binary data is corrupted during upload
- Missing or incorrect Content-Type in multipart request
- Attachment revision does not match document revision

## Common Error Messages

```
{ "error": "bad_request", "reason": "invalid_content_type" }
```

```
{ "error": "bad_request", "reason": "invalid_multipart" }
```

```
{ "error": "conflict", "reason": "Document update conflict." }
```

```
{ "error": "not_found", "reason": "attachment" }
```

## How to Fix It

### 1. Upload Attachment with Correct Content-Type

```bash
# Upload attachment directly
curl -X PUT http://localhost:5984/mydb/doc123/attachment.pdf \
  -H "Content-Type: application/pdf" \
  --data-binary @report.pdf

# Update attachment with revision
curl -X PUT http://localhost:5984/mydb/doc123/attachment.pdf?rev=2-abc123 \
  -H "Content-Type: application/pdf" \
  --data-binary @report.pdf
```

### 2. Use Multipart for Multiple Attachments

```bash
# Upload multiple attachments via multipart
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: multipart/related; boundary=abc123" \
  --data-binary @multipart_body.txt
```

```
--abc123
Content-Type: application/json

{"_id": "doc123", "_rev": "2-abc123"}
--abc123
Content-Type: image/png
Content-Disposition: attachment; filename="photo.png"

<binary data here>
--abc123--
```

### 3. Read and Delete Attachments

```bash
# Download attachment
curl http://localhost:5984/mydb/doc123/attachment.pdf -o local.pdf

# Delete attachment
curl -X DELETE http://localhost:5984/mydb/doc123/attachment.pdf?rev=2-abc123

# List all attachments for a document
curl http://localhost:5984/mydb/doc123 | jq '.attachments'
```

### 4. Fix Attachment Size Limits

```ini
; In local.ini - increase max_document_size for large attachments
[couchdb]
max_document_size = 500000000  ; 500MB
```

```bash
# Check current attachment size
curl http://localhost:5984/mydb/doc123/attachment.pdf \
  -I | grep Content-Length
```

## Common Scenarios

- **Image upload fails with 400**: Ensure `Content-Type: image/png` or correct MIME type is set.
- **Stale attachment after revision change**: Always include `?rev=` matching the current document revision.
- **Large file upload times out**: Use chunked transfer encoding or increase proxy timeout.

## Prevent It

- Validate file types and sizes before uploading to CouchDB
- Use `Content-Disposition` header with correct filenames
- Implement retry logic for large file uploads

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
- [CouchDB Conflict Error](/tools/couchdb/couchdb-conflict-error)
