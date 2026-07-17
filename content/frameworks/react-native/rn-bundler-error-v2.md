---
title: "Metro bundler - ECONNREFUSED"
description: "React Native Metro bundler fails to connect, causing ECONNREFUSED error during development"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
tags: ["metro", "bundler", "econnrefused", "development", "port", "server"]
weight: 5
---

The Metro bundler ECONNREFUSED error occurs when the React Native development server cannot accept incoming connections. This prevents the bundler from serving JavaScript bundles to your app during development.

## Common Causes

- Metro bundler process crashed or was killed
- Port 8081 already in use by another process
- Firewall or antivirus blocking the bundler port
- Incorrect host configuration for the dev server
- Metro cache corruption preventing startup

## How to Fix

1. Kill the existing Metro process and restart:

```bash
kill $(lsof -t -i:8081)
npx react-native start --reset-cache
```

2. Use a different port if 8081 is occupied:

```bash
npx react-native start --port 8082
# Then run with new port
npx react-native run-android --port 8082
```

3. Reset Metro cache completely:

```bash
rm -rf /tmp/metro-*
rm -rf node_modules/.cache
npx react-native start --reset-cache
```

4. Check what is using port 8081:

```bash
lsof -i :8081
```

5. Configure the bundler to listen on all interfaces:

```bash
npx react-native start --host 0.0.0.0
```

## Examples

```bash
$ npx react-native run-android
info Starting JS server...
error: connect ECONNREFUSED 127.0.0.1:8081
Could not connect to development server.
```

```bash
# Verify Metro is running
curl http://localhost:8081/status
# Should return: {"status":"ok"}
```

## Related Errors

- [Fast Refresh error]({{< relref "/frameworks/react-native/rn-fast-refresh-error" >}})
- [Network error]({{< relref "/frameworks/react-native/rn-network-error" >}})
