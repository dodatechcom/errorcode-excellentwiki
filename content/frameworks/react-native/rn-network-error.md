---
title: "Network - fetch timeout in React Native"
description: "React Native fetch or XMLHttpRequest times out, causing network requests to fail"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A network timeout error in React Native occurs when a fetch or XMLHttpRequest does not receive a response within the allowed time. This can happen on both platforms and may be triggered by slow servers, network issues, or incorrect request configuration.

## Common Causes

- Server is slow to respond or overloaded
- No internet connectivity on the device
- DNS resolution failure
- Request timeout is too short for the API
- Android cleartext traffic blocked by default
- Large payloads without streaming

## How to Fix

1. Add timeout to fetch requests using `AbortController`:

```javascript
const fetchWithTimeout = async (url, options = {}, timeout = 10000) => {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    clearTimeout(id);
    return response;
  } catch (error) {
    clearTimeout(id);
    if (error.name === 'AbortError') {
      throw new Error('Request timed out');
    }
    throw error;
  }
};

const data = await fetchWithTimeout('https://api.example.com/data', {}, 15000);
```

2. Enable cleartext traffic on Android in `android/app/src/main/AndroidManifest.xml`:

```xml
<application
  android:usesCleartextTraffic="true"
  ... >
```

3. Check network connectivity before requests:

```javascript
import NetInfo from '@react-native-community/netinfo';

const checkAndFetch = async (url) => {
  const state = await NetInfo.fetch();
  if (!state.isConnected) {
    throw new Error('No internet connection');
  }
  return fetch(url);
};
```

4. Use retry logic for flaky connections:

```javascript
const fetchWithRetry = async (url, retries = 3, delay = 1000) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await fetchWithTimeout(url, {}, 10000);
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(r => setTimeout(r, delay * (i + 1)));
    }
  }
};
```

## Examples

```javascript
// Network timeout error
fetch('https://api.example.com/data')
  .then(res => res.json())
  .catch(err => {
    // TypeError: Network request failed
    // or AbortError: Aborted
  });
```

## Related Errors

- [Bundler error]({{< relref "/frameworks/react-native/rn-bundler-error-v2" >}})
- [RedBox error]({{< relref "/frameworks/react-native/rn-redbox-error-v2" >}})
