---
title: "[Solution] Azure Analysis Services Error — server, model, and refresh failures"
description: "Fix Azure Analysis Services error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 136
---

Analysis Services errors appear as server paused unexpectedly, model refresh timeouts, or data source connection failures during tabular model operations.

## Common Causes
- Server paused automatically due to inactivity or resource limits
- Model refresh failing due to data source credential expiration
- Insufficient memory for large tabular models during processing
- Data source firewall not allowing Analysis Services IP ranges
- Gateway not configured for on-premises data source connectivity

## How to Fix
### Check server state
```bash
az aas server show \
  --resource-group myResourceGroup \
  --name myAasServer \
  --query "state"
```

### Resume paused server
```bash
az aas server resume \
  --resource-group myResourceGroup \
  --name myAasServer
```

### List server role members
```bash
az aas server list-role-members \
  --resource-group myResourceGroup \
  --server-name myAasServer \
  --role-name "Administrator"
```

### Update server SKU
```bash
az aas server update \
  --resource-group myResourceGroup \
  --name myAasServer \
  --sku S1
```

## Examples
### Create Analysis Services server
```bash
az aas server create \
  --resource-group myResourceGroup \
  --name myAasServer \
  --location eastus \
  --sku S1 \
  --admin-user admin@contoso.com
```

### Check model refresh history
```bash
az monitor metrics list \
  --resource /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.AnalysisServices/servers/myAasServer \
  --metric "QueryProcessingUnit"
```

## Related Errors
- {{< relref "/cloud/azure/azure-sql-error" >}}
- {{< relref "/cloud/azure/azure-synapse-error" >}}
- {{< relref "/cloud/azure/azure-data-factory-error" >}}
