---
title: "[Solution] Azure Data Factory Error — pipeline, linked-service, and trigger failures"
description: "Fix Azure Data Factory error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 152
---

Data Factory errors involve pipeline activity failures, linked service connection issues, or trigger misconfigurations that stop data movement workloads.

## Common Causes
- Linked service connection string expired or credential rotated
- Pipeline activity type incompatible with dataset format
- Self-hosted integration runtime offline or not registered
- Trigger schedule conflicting with pipeline run duration
- Data flow debug session memory limit exceeded

## How to Fix
### Check ADF status
```bash
az datafactory show \
  --resource-group myResourceGroup \
  --factory-name myDataFactory \
  --query "provisioningState"
```

### List pipeline runs
```bash
az datafactory pipeline-run query-by-pipeline \
  --resource-group myResourceGroup \
  --factory-name myDataFactory \
  --pipeline-name myPipeline \
  --query "[].{runId:runId,status=status,startTime:startTime}"
```

### Create linked service
```bash
az datafactory linked-service create \
  --resource-group myResourceGroup \
  --factory-name myDataFactory \
  --name myLinkedService \
  --properties '{"type":"AzureBlobStorage","typeProperties":{"connectionString":"DefaultEndpointsProtocol=https;AccountName=myaccount"}}'
```

### Update pipeline parameters
```bash
az datafactory pipeline create \
  --resource-group myResourceGroup \
  --factory-name myDataFactory \
  --name myPipeline \
  --pipeline @pipeline.json
```

## Examples
### Create integration runtime
```bash
az datafactory integration-runtime self-hosted create \
  --resource-group myResourceGroup \
  --factory-name myDataFactory \
  --name myIR
```

### Check trigger status
```bash
az datafactory trigger list \
  --resource-group myResourceGroup \
  --factory-name myDataFactory \
  --query "[].{name:name,state:runtimeState}"
```

## Related Errors
- {{< relref "/cloud/azure/azure-synapse-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
