---
title: "[Solution] Azure Data Factory Pipeline Error"
description: "Fix Azure Data Factory pipeline execution failures for ETL and data integration workflows."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Pipeline errors occur when ADF pipelines fail during execution. This disrupts data integration schedules and downstream analytics.

## Common Causes

- Linked service connection string is invalid or references a deleted resource
- Integration runtime is offline and cannot execute the activity
- Source data has schema changes that break the mapping
- Pipeline timeout is reached for long-running copy or transform activities

## How to Fix

### Check pipeline run history

```bash
az datafactory pipeline-run query-by-workspace \
  --factory-name myADF \
  --resource-group myRG \
  --last-updated-after "2026-01-01T00:00:00Z"
```

### Get failed activity details

```bash
az datafactory activity-run query-by-pipeline-run \
  --factory-name myADF \
  --resource-group myRG \
  --run-id "runId"
```

### Check integration runtime status

```bash
az datafactory integration-runtime list \
  --factory-name myADF \
  --resource-group myRG \
  --query "[].{Name:name,Type:type,State:state}"
```

### Test linked service connection

```bash
az datafactory linked-service test-connection \
  --factory-name myADF \
  --resource-group myRG \
  --linked-service-name myLinkedService
```

## Examples

- Pipeline fails with `LinkedServiceConnectionError` because the SQL server was moved to a different resource group
- Self-hosted integration runtime is offline and the pipeline cannot reach on-premises data sources
- Copy activity fails with `SchemaMismatch` because the source table added a new column

## Related Errors

- [Azure Data Factory Error]({{< relref "/cloud/azure/azure-data-factory-error" >}}) -- General ADF errors.
- [Azure Integration Runtime]({{< relref "/cloud/azure/azure-integration-runtime" >}}) -- IR issues.
