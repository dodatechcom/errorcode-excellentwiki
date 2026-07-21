---
title: "[Solution] React Native Android Fresco Library Error"
description: "react-native Android Fresco image loading library fails with memory or decode errors when rendering images in React Native apps on Android devices"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Fresco library error occurs when React Native's built-in image loader on Android encounters decode, memory, or disk cache corruption. Fresco is the default image pipeline for React Native on Android and errors surface as image placeholders, crashes, or warnings in logcat.

## Common Causes

- Corrupted image cache in Fresco's disk cache directory
- Out of memory decoding very large bitmap images
- Malformed animated WebP or GIF files
- Fresco pipeline configured with insufficient memory limits
- Image URL returns an HTTP redirect or wrong content type

## How to Fix

1. Clear Fresco cache programmatically:

```java
import com.facebook.drawee.backends.pipeline.Fresco;
import com.facebook.imagepipeline.core.ImagePipeline;

ImagePipeline pipeline = Fresco.getImagePipeline();
pipeline.clearCaches();
```

2. Use cache busting query parameters for problematic images:

```javascript
<Image
  source={{ uri: `${baseUrl}/photo.jpg?t=${Date.now()}` }}
  style={{ width: 200, height: 200 }}
/>
```

3. Increase Fresco memory config in your Application class:

```java
ImagePipelineConfig config = ImagePipelineConfig.newBuilder(this)
  .setBitmapMemoryCacheMaxSize(2 * ByteConstants.MB)
  .build();
Fresco.initialize(this, config);
```

## Examples

```javascript
// Error: image shows blank placeholder on Android
<Image source={{ uri: 'https://example.com/huge-image.png' }} />

// Fix: resize the image server-side or use resizeMode
<Image
  source={{ uri: 'https://example.com/huge-image.png' }}
  style={{ width: 300, height: 300 }}
  resizeMode="contain"
/>
```

## Related Errors

- [Storage Error]({{< relref "/frameworks/react-native/rn-storage-error" >}})
