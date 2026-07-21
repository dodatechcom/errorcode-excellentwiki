---
title: "[Solution] Vercel Blob Store Error"
description: "Fix Vercel Blob store errors when uploading or reading files from Blob storage fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Blob Store Error

Vercel Blob operations fail during upload or retrieval.

```
Error: @vercel/blob: Upload failed
```

## Common Causes

- Blob store not created
- File exceeds size limit (4.5MB per upload)
- Invalid pathname
- Authentication token invalid
- Network timeout during upload

## How to Fix

### Upload to Blob

```typescript
import { put } from '@vercel/blob';

export default async function handler(req, res) {
  const { pathname, contentType } = req.body;
  
  const blob = await put(pathname, req.body, {
    contentType,
    access: 'public'
  });

  res.status(200).json(blob);
}
```

### Read from Blob

```typescript
import { list } from '@vercel/blob';

export default async function handler(req, res) {
  const { blobs } = await list();
  res.status(200).json({ blobs });
}
```

### Delete Blob

```typescript
import { del } from '@vercel/blob';

export default async function handler(req, res) {
  const { url } = req.body;
  await del(url);
  res.status(200).json({ deleted: true });
}
```

### Check Blob Store

```bash
# List blobs
vercel blob ls

# Check env vars
echo $BLOB_READ_WRITE_TOKEN
```

### Handle Large Files

```typescript
// For files > 4.5MB, use multipart upload
import { upload } from '@vercel/blob/client';

const blob = await upload(file, {
  access: 'public',
  handleUploadUrl: '/api/blob-upload'
});
```

## Examples

```typescript
// Complete Blob upload example
export default async function handler(req, res) {
  try {
    const formData = await req.formData();
    const file = formData.get('file');
    
    if (!file) {
      return res.status(400).json({ error: 'No file' });
    }

    const blob = await put(file.name, file, {
      access: 'public',
      contentType: file.type
    });

    res.status(200).json({ url: blob.url });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```
