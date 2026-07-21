---
title: "[Solution] React Native OKHTTP NetCAB Cache Corruption Error"
description: "react-native Android networking crashes with NetCAB file corruption error in the OkHttp disk cache when making HTTP requests"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The NetCAB cache corruption error occurs when the OkHttp disk cache used by React Native's networking layer on Android becomes corrupted. This manifests as a crash in the caching layer when the app tries to read or write HTTP responses.

## Common Causes

- App killed abruptly while OkHttp was writing a cache entry
- Disk full or file system error while writing cache
- Multiple processes accessing the same cache directory
- OkHttp version mismatch between different native libraries
- Corrupted cached responses from a misconfigured CDN

## How to Fix

1. Clear the OkHttp cache from the Application class:

```java
// MainApplication.java
import okhttp3.Cache;
import java.io.IOException;

Cache cache = new Cache(getCacheDir(), 10 * 1024 * 1024);
try {
  cache.evictAll();
} catch (IOException e) {
  // handle
}
```

2. Use React Native's built-in cache clearing:

```javascript
import NetInfo from '@react-native-community/netinfo';

NetInfo.fetch().then(state => {
  if (!state.isConnected) {
    // Clear network cache on connectivity change
    fetch('https://example.com', { method: 'HEAD', cache: 'no-store' });
  }
});
```

3. Disable OkHttp cache for problematic endpoints:

```javascript
// Add cache: 'no-store' to request options
fetch(url, {
  cache: 'no-store',
});
```

## Examples

```javascript
// Error: java.io.IOException: failed to delete cache entries
// Fix: set cache size limit in OkHttpClient initialization

OkHttpClient client = new OkHttpClient.Builder()
  .cache(new Cache(getCacheDir(), 5 * 1024 * 1024))
  .build();
```

## Related Errors

- [Network Error]({{< relref "/frameworks/react-native/rn-network-error" >}})
