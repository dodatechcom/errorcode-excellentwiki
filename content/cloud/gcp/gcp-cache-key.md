---
title: "[Solution] GCP Cache Key"
description: "CacheKeyError for cache keys."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cache Key` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Include protocol in cache key (should be off)
- Query string whitelist/blacklist conflict
- Cache key includes host

## How to Fix

### Update cache key

```bash
gcloud compute backend-buckets update myBucket --cache-key-include-protocol=false
```

## Examples

- Example scenario: include protocol in cache key (should be off)
- Example scenario: query string whitelist/blacklist conflict
- Example scenario: cache key includes host

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
