---
title: "[Solution] GCP Cloud Storage CORS Error"
description: "Fix Cloud Storage CORS errors. Resolve cross-origin resource sharing configuration, preflight, and access control issues in GCS buckets."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Storage CORS Error

The Cloud Storage CORS error occurs when cross-origin requests to a GCS bucket are blocked due to missing or incorrect CORS configuration.

## Common Causes

- CORS configuration is not set on the bucket
- Allowed origins do not include the requesting domain
- Requested HTTP method is not in the allowed methods list
- Preflight OPTIONS request fails before the actual request
- Uniform bucket-level access overrides CORS settings

## How to Fix

### 1. Check existing CORS configuration
```bash
gsutil cors get gs://BUCKET_NAME
```

### 2. Set CORS configuration
```bash
cat > cors.json << EOF
[
  {
    "origin": ["https://example.com"],
    "method": ["GET", "POST", "PUT"],
    "responseHeader": ["Content-Type"],
    "maxAgeSeconds": 3600
  }
]
EOF
gsutil cors set cors.json gs://BUCKET_NAME
```

### 3. Clear CORS if misconfigured
```bash
echo "[]" > cors.json
gsutil cors set cors.json gs://BUCKET_NAME
```

### 4. Test CORS preflight
```bash
curl -I -X OPTIONS \
  -H "Origin: https://example.com" \
  -H "Access-Control-Request-Method: POST" \
  https://storage.googleapis.com/BUCKET_NAME/object
```

## Examples

### Allow multiple origins
```json
[
  {
    "origin": ["https://app.example.com", "https://admin.example.com"],
    "method": ["GET", "POST", "PUT", "DELETE"],
    "responseHeader": ["Content-Type", "Authorization"],
    "maxAgeSeconds": 7200
  }
]
```

### Verify CORS headers in response
```bash
curl -I -H "Origin: https://example.com" \
  https://storage.googleapis.com/BUCKET_NAME/file.txt
```

## Related Errors

- [GCP Storage Error]({{< relref "/cloud/gcp/gcp-storage-error" >}})
- [GCP Bucket Policy GCS]({{< relref "/cloud/gcp/gcp-bucket-policy-(gcs)" >}})
