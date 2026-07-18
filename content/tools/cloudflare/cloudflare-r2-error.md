---
title: "[Solution] Cloudflare R2 Object Storage Error — How to Fix"
description: "Fix Cloudflare R2 object storage errors. Resolve upload failures, access denied issues, bucket configuration, and presigned URL problems."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Cloudflare R2 object storage error occurs when operations on your R2 bucket fail due to misconfiguration, permission issues, or exceeding storage limits. R2 is Cloudflare's S3-compatible object storage service with zero egress fees.

## What This Error Means

R2 errors can occur at the API level (S3-compatible), during access via custom domains and Workers, or within the Cloudflare dashboard. Common failure points include authentication, bucket policies, CORS configuration, storage limits, and presigned URL generation.

## Why It Happens

- API token lacks the required R2 permissions
- Bucket name contains invalid characters or is already taken
- Object key exceeds the maximum length (1024 bytes)
- File size exceeds the single object limit (5 GB for single PUT, 5 TB for multipart)
- CORS is not configured for browser-based uploads
- The account has exceeded free tier storage or operations limits
- Custom domain binding is misconfigured
- Presigned URL has expired or was generated with wrong parameters
- The bucket public access settings block reads

## Common Error Messages

- `Access Denied` — API token or bucket policy denies the operation
- `NoSuchBucket` — The bucket does not exist or is in a different account
- `EntityTooLarge` — Upload exceeds the object size limit
- `InvalidAccessKeyId` — The API token is invalid or revoked
- `NoSuchKey` — The requested object does not exist
- `BucketAlreadyExists` — The bucket name is already taken globally
- `RequestTimeout` — The upload took too long

## How to Fix It

### Verify API Token Permissions

```bash
# Check your R2 API token has these permissions:
# Object Read, Object Write, Bucket Read, Bucket Write

# Test the token with a simple list operation
aws s3 ls s3://your-bucket-name \
  --endpoint-url https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com \
  --aws-access-key-id YOUR_ACCESS_KEY \
  --aws-secret-access-key YOUR_SECRET_KEY

# If you get Access Denied, create a new token in:
# Cloudflare Dashboard > R2 > Manage R2 API Tokens
```

### Upload Objects Correctly

```bash
# Upload a small file (< 100 MB)
aws s3 cp ./local-file.pdf s3://your-bucket/path/to/file.pdf \
  --endpoint-url https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com \
  --aws-access-key-id YOUR_ACCESS_KEY \
  --aws-secret-access-key YOUR_SECRET_KEY

# Upload large file (multipart for files > 100 MB)
aws s3 cp ./large-video.mp4 s3://your-bucket/videos/large-video.mp4 \
  --endpoint-url https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com \
  --aws-access-key-id YOUR_ACCESS_KEY \
  --aws-secret-access-key YOUR_SECRET_KEY \
  --expected-size 5368709120

# Or use presigned URLs for browser uploads
curl -X PUT "https://your-bucket.r2.dev/path/to/file.pdf" \
  --upload-file ./file.pdf \
  -H "Content-Type: application/pdf"
```

### Configure CORS for Browser Uploads

```json
// R2 CORS configuration via API
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://your-domain.com", "https://app.your-domain.com"],
      "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
      "AllowedHeaders": ["*"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```

```bash
# Apply CORS via API
curl -X PUT "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/r2/buckets/BUCKET_NAME/cors" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "CORSRules": [{
      "AllowedOrigins": ["https://your-domain.com"],
      "AllowedMethods": ["GET", "PUT", "POST"],
      "AllowedHeaders": ["*"]
    }]
  }'
```

### Use Workers for Fine-Grained Access

```javascript
// Worker to handle R2 uploads with validation
export default {
  async fetch(request, env) {
    if (request.method === 'PUT') {
      const url = new URL(request.url);
      const key = url.pathname.slice(1);

      // Validate file type
      const contentType = request.headers.get('Content-Type');
      const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
      if (!allowedTypes.includes(contentType)) {
        return new Response('Unsupported file type', { status: 400 });
      }

      // Validate file size
      const contentLength = parseInt(request.headers.get('Content-Length') || '0');
      if (contentLength > 10 * 1024 * 1024) {
        return new Response('File too large', { status: 413 });
      }

      // Upload to R2
      await env.MY_BUCKET.put(key, request.body, {
        httpMetadata: { contentType },
      });

      return new Response('Uploaded', { status: 201 });
    }

    return new Response('Method not allowed', { status: 405 });
  }
};
```

### Generate Presigned URLs

```javascript
// Generate a presigned URL for browser upload
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const key = url.searchParams.get('key');

    if (!key) {
      return new Response('Missing key parameter', { status: 400 });
    }

    // Generate presigned URL for PUT operation
    const presignedUrl = await env.MY_BUCKET.createPresignedRequest(key, {
      method: 'PUT',
      expiresIn: 3600, // 1 hour
    });

    return new Response(JSON.stringify({ uploadUrl: presignedUrl }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
```

## Common Scenarios

- **Presigned URL expired:** A presigned URL generated for browser upload has a short TTL and expires before the user completes the upload.
- **Bucket policy too restrictive:** A bucket policy allows read access but denies write access, so Workers or uploads fail with Access Denied.
- **Egress charges unexpected:** While R2 has zero egress fees, the free tier for operations and storage may be exceeded during high-traffic events.

## Prevent It

1. Always verify R2 API token permissions in the Cloudflare dashboard before debugging other issues
2. Use multipart uploads for files larger than 100 MB to avoid timeout and size limit errors
3. Set up R2 bucket notifications and monitoring to track storage usage before hitting limits

## Related Pages

- [Cloudflare D1 Error]({{< relref "/tools/cloudflare/cloudflare-d1-error" >}}) — D1 database query failures
- [Cloudflare Worker Error]({{< relref "/tools/cloudflare/cloudflare-worker-error" >}}) — Worker script exceptions
