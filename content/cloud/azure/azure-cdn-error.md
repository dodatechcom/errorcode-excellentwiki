---
title: "[Solution] Azure CDN Error"
description: "Fix Azure CDN errors. Resolve CDN configuration and caching issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An Azure CDN error occurs when the CDN cannot serve content or is misconfigured. This can cause 4xx/5xx errors or stale content delivery.

## Common Causes

- Origin server is not accessible
- CDN endpoint is disabled
- SSL certificate not configured
- Cache rules are too aggressive or not set
- Origin path is incorrect

## How to Fix

### Check CDN Profile

```bash
az cdn profile show --name mycdn --resource-group myRG
```

### Check Endpoint Status

```bash
az cdn endpoint show --name myendpoint --profile-name mycdn --resource-group myRG
```

### Purge CDN Cache

```bash
az cdn endpoint purge --name myendpoint --profile-name mycdn --resource-group myRG \
  --content-paths "/*"
```

### Test CDN Endpoint

```bash
curl -I https://myendpoint.azureedge.net/
```

### Configure Origin

```bash
az cdn endpoint create --name myendpoint --profile-name mycdn --resource-group myRG \
  --origin myorigin.blob.core.windows.net --origin-path /
```

## Examples

```bash
# Example 1: Origin not accessible
# 502 Bad Gateway
# Fix: verify origin server is running and accessible

# Example 2: Stale content
# CDN serving old version
# Fix: purge cache after deployment
```

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) — Storage error
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) — App Service error
