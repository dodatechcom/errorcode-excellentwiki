---
title: "Bitmap Memory Error"
description: "Fix Android image memory errors from large bitmap loading and processing"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App crashes with OutOfMemoryError when loading or displaying images

## Common Causes

- Loading full-resolution bitmap into memory
- Bitmap not recycled after use
- Multiple large images loaded simultaneously
- Gallery image not sampled before display

## Fixes

- Use image loading library with automatic sampling
- Set inSampleSize for large images
- Use RGB_565 for photos without transparency
- Load images with appropriate size for ImageView

## Code Example

```kotlin
// WRONG: load full image
val bitmap = BitmapFactory.decodeFile(filePath)

// CORRECT: sample large image
val options = BitmapFactory.Options().apply {
    inJustDecodeBounds = true
}
BitmapFactory.decodeFile(filePath, options)

options.inSampleSize = calculateInSampleSize(options, reqWidth, reqHeight)
options.inJustDecodeBounds = false
val bitmap = BitmapFactory.decodeFile(filePath, options)

// Or use Glide/Coil (recommended):
Glide.with(imageView)
    .load(uri)
    .override(200, 200)  // Resize
    .into(imageView)
```

# Use Glide/Coil for automatic memory management
# Never load full-resolution images into memory
# Recycle bitmaps when done (if not using library)
