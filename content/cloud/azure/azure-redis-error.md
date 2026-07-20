---
title: "[Solution] Azure Redis Cache Error — connection, persistence, and cluster failures"
description: "Fix Azure Redis Cache error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 129
---

Redis Cache errors involve connection timeouts, cache eviction during persistence operations, or cluster slot migration failures that impact caching performance.

## Common Causes
- Connection limit per client exceeded on Premium/Enterprise tiers
- RDB/AOF persistence causing temporary write unavailability
- Cluster mode slot migration not completing during scaling
- SSL certificate expiry on custom domains
- Memory pressure causing eviction of critical cache entries

## How to Fix
### Check cache status
```bash
az redis show \
  --resource-group myResourceGroup \
  --name myRedisCache \
  --query "provisioningState"
```

### Flush cache to clear stuck keys
```bash
az redis flush \
  --resource-group myResourceGroup \
  --name myRedisCache
```

### Update cache SKU
```bash
az redis update \
  --resource-group myResourceGroup \
  --name myRedisCache \
  --sku Premium \
  --vm-size P1
```

### Export cache data
```bash
az redis export \
  --resource-group myResourceGroup \
  --name myRedisCache \
  --blob-container-uri "https://myaccount.blob.core.windows.net/backups" \
  --prefix myBackup
```

## Examples
### Create Redis cache
```bash
az redis create \
  --resource-group myResourceGroup \
  --name myRedisCache \
  --location eastus \
  --sku Standard \
  --vm-size C1
```

### List cache keys
```bash
az redis list-keys \
  --resource-group myResourceGroup \
  --name myRedisCache
```

## Related Errors
- {{< relref "/cloud/azure/azure-cosmos-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
