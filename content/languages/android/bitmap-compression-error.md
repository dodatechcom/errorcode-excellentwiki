---
title: "Bitmap Compression Error"
description: "Fix Android bitmap compression and format conversion errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bitmap compression produces corrupted images or files too large

## Common Causes

- Using PNG for photographs instead of JPEG
- Quality too low for JPEG compression
- WebP not supported on target API level
- Compression method not matching image content

## Fixes

- Use JPEG for photographs, PNG for transparency
- Set appropriate quality level (80-95 for JPEG)
- Use WebP for better compression on API 14+
- Choose format based on image characteristics

## Code Example

```kotlin
// Compress bitmap to file
val outputStream = FileOutputStream(file)
bitmap.compress(Bitmap.CompressFormat.JPEG, 90, outputStream)
outputStream.close()

// Or to byte array:
val byteArrayOutputStream = ByteArrayOutputStream()
bitmap.compress(Bitmap.CompressFormat.PNG, 100, byteArrayOutputStream)
val byteArray = byteArrayOutputStream.toByteArray()

// WebP (better compression):
bitmap.compress(Bitmap.CompressFormat.WEBP_LOSSY, 85, outputStream)
```

# JPEG: photos, no transparency, lossy
# PNG: graphics, transparency, lossless
# WEBP: best compression, API 14+
# WebP_LOSSY: API 30+
