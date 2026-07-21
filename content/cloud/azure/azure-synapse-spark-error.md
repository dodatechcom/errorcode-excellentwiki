---
title: "[Solution] Azure Synapse Spark Pool Error"
description: "Fix Azure Synapse Analytics Spark pool startup failures and notebook execution errors."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Spark pool errors in Synapse prevent data processing notebooks from executing. This blocks ETL pipelines and ad-hoc data analysis.

## Common Causes

- Spark pool has no running nodes and cannot auto-scale due to quota limits
- Notebook code uses a library that is not installed in the pool
- Managed identity does not have access to the data source
- Spark version is outdated and incompatible with the notebook code

## How to Fix

### Check Spark pool status

```bash
az synapse spark pool show \
  --workspace-name myWorkspace \
  --name mySparkPool \
  --resource-group myRG \
  --query "provisioningState"
```

### Update Spark pool version

```bash
az synapse spark pool update \
  --workspace-name myWorkspace \
  --name mySparkPool \
  --resource-group myRG \
  --spark-version 3.4
```

### List available node sizes

```bash
az synapse spark pool list \
  --workspace-name myWorkspace \
  --resource-group myRG \
  --query "[].{Name:name,NodeSize:nodeSize,AutoScale:autoScale}
```

### Check Spark application logs

```bash
az synapse spark session list \
  --workspace-name myWorkspace \
  --spark-pool-name mySparkPool
```

## Examples

- Spark pool fails to start with `InsufficientQuota` because the vCore limit is reached
- Notebook throws `ClassNotFoundException` because a required library JAR is missing
- Spark session crashes with `OutOfMemoryError` because the node size is too small for the workload

## Related Errors

- [Azure Synapse Error]({{< relref "/cloud/azure/azure-synapse-error" >}}) -- General Synapse errors.
- [Azure Data Factory Error]({{< relref "/cloud/azure/azure-data-factory-error" >}}) -- Data Factory issues.
