---
title: "[Solution] Azure CDN Cache Error"
description: "Fix Azure CDN cache purge and content delivery failures for static and dynamic content."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

CDN cache errors prevent content from being cached or served from edge locations. This increases latency and origin server load.

## Common Causes

- Cache purge request is still in progress and has not completed
- CDN endpoint origin is unreachable or returning error responses
- Cache control headers prevent CDN from caching content
- Custom domain SSL certificate has expired

## How to Fix

### Purge CDN cache

```bash
az cdn endpoint purge \
  --name myEndpoint \
  --profile-name myCDN \
  --resource-group myRG \
  --content-paths "/*"
```

### Check CDN endpoint status

```bash
az cdn endpoint show \
  --name myEndpoint \
  --profile-name myCDN \
  --resource-group myRG \
  --query "resourceState"
```

### Configure caching rules

```bash
az cdn endpoint update \
  --name myEndpoint \
  --profile-name myCDN \
  --resource-group myRG \
  --caching-settings "CacheDuration=1.00:00:00"
```

### Check custom domain SSL

```bash
az cdn custom-domain show \
  --endpoint-name myEndpoint \
  --profile-name myCDN \
  --resource-group myRG \
  --custom-domain-name mydomain.com \
  --query "customHttpsParameters"
```

## Examples

- CDN returns stale content because the cache purge is still propagating
- Custom domain returns SSL error because the certificate expired 7 days ago
- All requests go to origin because `Cache-Control: no-cache` header is set

## Related Errors

- [Azure CDN Error]({{< relref "/cloud/azure/azure-cdn-error" >}}) -- General CDN errors.
- [Azure Front Door Error]({{< relref "/cloud/azure/azure-front-door-error" >}}) -- Front Door issues.
