---
title: "[Solution] CouchDB Multipart Error — How to Fix"
description: "Fix CouchDB multipart errors by resolving multipart MIME failures, fixing attachment upload issues, and handling multipart boundary problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Multipart Error

CouchDB multipart errors occur when multipart MIME requests for document updates with attachments fail due to boundary, encoding, or format issues.

## Why It Happens

- Multipart boundary is malformed or missing
- Content-Type header is incorrect for multipart
- Binary data in attachment is corrupted
- Part headers are missing or incorrect
- Multipart body encoding does not match the document
- Attachment size exceeds document size limits

## Common Error Messages

```
{ "error": "bad_request", "reason": "invalid_multipart" }
```

```
{ "error": "bad_request", "reason": "Invalid content type" }
```

```
{ "error": "not_found", "reason": "attachment not found" }
```

```
{ "error": "bad_request", "reason": "Malformed multipart body" }
```

## How to Fix It

### 1. Fix Multipart Upload

```bash
# Correct multipart upload
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: multipart/related; boundary=abc123" \
  --data-binary @multipart_body.txt
```

### 2. Create Correct Multipart Body

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

### 3. Upload Attachment Directly

```bash
# Upload attachment without multipart
curl -X PUT http://localhost:5984/mydb/doc123/attachment.pdf \
  -H "Content-Type: application/pdf" \
  --data-binary @report.pdf

# Update attachment with revision
curl -X PUT http://localhost:5984/mydb/doc123/attachment.pdf?rev=2-abc123 \
  -H "Content-Type: application/pdf" \
  --data-binary @report.pdf
```

### 4. Fix Content-Type Issues

```bash
# Ensure correct Content-Type for each part
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: multipart/related; boundary=myboundary" \
  -H "Accept: application/json" \
  --data-binary @multipart.txt
```

## Common Scenarios

- **Multipart upload fails**: Ensure the boundary string matches in Content-Type and body.
- **Attachment is corrupted**: Verify the binary data is properly encoded.
- **Content-Type mismatch**: Use the correct MIME type for each attachment.

## Prevent It

- Use well-tested multipart generation libraries
- Verify attachment Content-Type before upload
- Test multipart uploads with small files first

## Related Pages

- [CouchDB Attachment Error](/tools/couchdb/couchdb-attachment-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
