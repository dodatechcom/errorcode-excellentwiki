---
title: "[Solution] Azure Databricks Error"
description: "Resolve Azure Databricks cluster failures, notebook errors, and Spark job issues."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Databricks errors encompass cluster startup failures, notebook execution errors, and Spark job crashes that impact data processing pipelines.

## Common Causes

- Cluster failed to start due to insufficient quota for the selected VM SKU
- Notebook code references a Spark table or mount that does not exist
- Auto-scaling cluster cannot add nodes because the maximum limit is reached
- Secret scope is not configured and code tries to access secrets

## How to Fix

### Check cluster status

```bash
az databricks workspace show \
  --name myWorkspace \
  --resource-group myRG \
  --query "parameters"
```

### Create a cluster via REST API

```bash
az rest --method POST \
  --uri "https://{databricks-instance}/api/2.0/clusters/create" \
  --body '{
    "cluster_name": "myCluster",
    "spark_version": "13.3.x-scala2.12",
    "node_type_id": "Standard_D4s_v3",
    "num_workers": 2
  }'
```

### List available VM SKUs

```bash
az vm list-sizes --location eastus --query "[?name.contains(@,'Standard_D')].name"
```

### Check Spark job logs

```bash
az rest --method GET \
  --uri "https://{databricks-instance}/api/2.0/jobs/runs/list"
```

## Examples

- Cluster creation fails with `RESOURCE_EXHAUSTED` because the subscription has no GPU quota
- Notebook fails with `AnalysisException` because the Delta table path does not exist
- Secret retrieval fails because the Databricks secret scope is not configured

## Related Errors

- [Azure Data Factory Error]({{< relref "/cloud/azure/azure-data-factory-error" >}}) -- Data Factory issues.
- [Azure Data Lake Error]({{< relref "/cloud/azure/azure-data-lake-error" >}}) -- Data Lake access errors.
