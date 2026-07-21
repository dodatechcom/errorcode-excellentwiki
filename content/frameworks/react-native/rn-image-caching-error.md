---
title: "[Solution] React Native Image Caching Not Working"
description: "react-native Image component returns old or no image after URL changes, due to caching policies that prevent fetching updated content on Android and iOS"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The image caching error occurs when the React Native Image component serves a stale cached image even after the image URL has changed or the content at the URL has been updated. The default behavior for Android (Fresco) and iOS (URL Loading System) differs, leading to inconsistent cache results.

## Common Causes

- Images loaded with the same URL but different content (no cache busting)
- Fresco cache on Android ignores Cache-Control headers
- iOS URL loading policy default (.useProtocolCachePolicy) holds static image
- Server sends an aggressive Cache-Control header
- Using require() for images that need runtime updates

## How to Fix

1. Add cache busting with query parameters or file hashes:

```javascript
<Image
  source={{ uri: `https://example.com/photo.jpg?v=${photoVersion}` }}
/>
```

2. Set custom cache policy for iOS in Info.plist:

```xml
<key>NSURLRequestCachePolicy</key>
<integer>1</integer>
```

3. Clear Fresco caches on Android when images change:

```java
// Application.java
Fresco.getImagePipeline().clearCaches();
```

## Examples

```javascript
// Error: old image persists after avatar URL change
<Image source={{ uri: user.avatar }} />;

// Fix: add a key prop that changes
<Image key={user.id} source={{ uri: user.avatar }} />
```

## Related Errors

- [Fresco Library Error]({{< relref "/frameworks/react-native/rn-android-frescolib-error" >}})
