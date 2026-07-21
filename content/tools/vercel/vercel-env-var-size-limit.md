---
title: "[Solution] Vercel Environment Variable Size Limit"
description: "Fix Vercel environment variable size limit errors when env vars exceed the maximum allowed size."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Vercel deployment fails or environment variables are rejected because a single variable or total env vars exceed the size limit.

## Common Causes

- Single env var exceeds 4 KB limit
- Total environment variables exceed project limit
- Encrypted env vars have additional overhead
- Base64-encoded data stored in env vars
- Large JSON blobs in single variable

## How to Fix

- Split large values into multiple env vars
- Store large data in Vercel KV or Blob storage instead
- Compress or truncate env var values
- Use Vercel Blob for files and large data

## Examples

```json
// Instead of one large JSON env var
// Split into logical parts
{
  "APP_CONFIG_API_URL": "https://api.example.com",
  "APP_CONFIG_TIMEOUT": "30000"
}
```

For large data, use Vercel Blob:

```typescript
import { put } from '@vercel/blob';

await put('config.json', JSON.stringify(largeConfig), {
  contentType: 'application/json',
});
```
