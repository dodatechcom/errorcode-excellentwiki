---
title: "[Solution] Azure Synapse Error — workspace, pipeline, and Spark pool failures"
description: "Fix Azure Synapse error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 135
---

Synapse errors involve workspace provisioning failures, pipeline activity timeouts, or Spark pool startup issues that delay analytics workloads.

## Common Causes
- Managed private endpoint not established for data sources
- Spark pool node count hitting autoscale maximum during heavy workloads
- Linked service connection string expired or misconfigured
- Pipeline activity failing due to input/output format mismatch
- SQL pool DWU scaling not completing within maintenance window

## How to Fix
### Check workspace status
```bash
az synapse workspace show \
  --resource-group myResourceGroup \
  --name mySynapseWorkspace \
  --query "provisioningState"
```

### List pipeline run status
```bash
az synapse pipeline-run list \
  --resource-group myResourceGroup \
  --workspace-name mySynapseWorkspace \
  --query "[].{runId:runId,status:status,startTime:startTime}"
```

### Update Spark pool autoscale
```bash
az synapse spark-pool update \
  --resource-group myResourceGroup \
  --workspace-name mySynapseWorkspace \
  --name mySparkPool \
  --node-count 3 \
  --node-size Standard_D3_v2
```

### Create linked service
```bash
az synapse linked-service create \
  --resource-group myResourceGroup \
  --workspace-name mySynapseWorkspace \
  --name myLinkedService \
  --type LinkedService \
  --properties '{"type":"AzureBlobStorage","typeProperties":{"connectionString":"DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey"}}'
```

## Examples
### Create Synapse workspace
```bash
az synapse workspace create \
  --resource-group myResourceGroup \
  --name mySynapseWorkspace \
  --storage-account myStorageAccount \
  --file-system myFileSystem \
  --sql-admin-login-user sqladmin \
  --sql-admin-login-password Password123!
```

### Submit Spark job
```bash
az synapse spark session create \
  --resource-group myResourceGroup \
  --workspace-name mySynapseWorkspace \
  --spark-pool-name mySparkPool \
  --name mySession
```

## Related Errors
- {{< relref "/cloud/azure/azure-data-factory-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-sql-error" >}}
