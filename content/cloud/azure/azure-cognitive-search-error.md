---
title: "[Solution] Azure Cognitive Search Error — index, indexer, and datasource failures"
description: "Fix Azure Cognitive Search error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 137
---

Cognitive Search errors involve index creation failures, indexer pipeline timeouts, or data source connection issues that prevent search document ingestion.

## Common Causes
- Search service SKU Free tier index field limit exceeded
- Indexer schedule running while data source is unreachable
- Skillset skill failing due to Cognitive Services quota exhaustion
- Index schema field type incompatible with source data format
- Knowledge store projection exceeding storage quota

## How to Fix
### Check search service status
```bash
az search service show \
  --resource-group myResourceGroup \
  --name mySearchService \
  --query "provisioningState"
```

### List index status
```bash
az search index list \
  --resource-group myResourceGroup \
  --search-service-name mySearchService \
  --query "[].{name:name, fields:fields, documentCount:documentCount}"
```

### Create search index
```bash
az search index create \
  --resource-group myResourceGroup \
  --search-service-name mySearchService \
  --name myIndex \
  --definition '{"fields":[{"name":"id","type":"Edm.String","key":true,"searchable":true,"filterable":true},{"name":"title","type":"Edm.String","searchable":true}]'
```

### Run indexer on-demand
```bash
az search indexer run \
  --resource-group myResourceGroup \
  --search-service-name mySearchService \
  --indexer-name myIndexer
```

## Examples
### Create search service
```bash
az search service create \
  --resource-group myResourceGroup \
  --name mySearchService \
  --location eastus \
  --sku Standard
```

### Check indexer execution history
```bash
az search indexer status \
  --resource-group myResourceGroup \
  --search-service-name mySearchService \
  --indexer-name myIndexer
```

## Related Errors
- {{< relref "/cloud/azure/azure-cognitive-services-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
