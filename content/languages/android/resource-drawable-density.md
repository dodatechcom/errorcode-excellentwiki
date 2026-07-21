---
title: "Drawable Density Resource Missing"
description: "Fix missing drawable density resource errors and image display issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Image does not display correctly because density-specific drawable is missing

## Common Causes

- Only one density version of drawable provided
- Drawable placed in wrong density folder
- Vector drawable not properly configured
- Image dimensions too large for device memory

## Fixes

- Provide drawables in multiple density buckets
- Use vector drawables for scalable graphics
- Place drawables in correct density folders
- Compress large bitmap images appropriately

## Code Example

```kotlin
# Correct density folders:
res/drawable-mdpi/    (48x48 for icons)
res/drawable-hdpi/    (72x72)
res/drawable-xhdpi/   (96x96)
res/drawable-xxhdpi/  (144x144)
res/drawable-xxxhdpi/ (192x192)

# Or use vector drawable (recommended):
res/drawable/ic_arrow.xml
```

# For vector drawable:
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path android:fillColor="#FF0000"
          android:pathData="M12,2L2,22h20z"/>
</vector>
