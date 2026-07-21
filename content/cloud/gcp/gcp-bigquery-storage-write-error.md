---
title: "[Solution] GCP BigQuery Storage Write API Error"
description: "Fix BigQuery Storage Write API errors. Resolve write stream failures, append conflicts, and data format issues in BigQuery Storage Write."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Storage Write API Error

The BigQuery Storage Write API error occurs when streaming writes via the Storage Write API fail due to schema mismatches, row limits, or commit conflicts.

## Common Causes

- Row count exceeds the per-request limit of 10,000 rows
- Data format does not match the destination table schema
- Write stream is not properly finalized or committed
- Table is being concurrently modified by another writer
- Buffer size exceeds the 10 MB request limit

## How to Fix

### 1. Check write stream status
```bash
bq show --format=json PROJECT_ID:DATASET.TABLE > table_info.json
```

### 2. Validate schema alignment
```python
from google.cloud import bigquery
bq_client = bigquery.Client()
table = bq_client.get_table("PROJECT_ID.DATASET.TABLE")
for field in table.schema:
    print(f"{field.name}: {field.field_type}")
```

### 3. Create a write stream
```python
from google.cloud import bigquery_storage_v1
client = bigquery_storage_v1.BigQueryWriteClient()
parent = "projects/PROJECT_ID/datasets/DATASET/tables/TABLE"
stream = client.create_write_stream(parent=parent)
```

### 4. Flush and finalize write
```python
write_request = bigquery_storage_v1.AppendRowsRequest(
    write_stream=stream.name,
    proto_rows=bigquery_storage_v1.ProtoRows(
        writer_schema=schema,
        rows=[row1, row2]
    )
)
client.append_rows(request=write_request)
```

## Examples

### Append rows via Storage Write
```python
from google.cloud import bigquery_storage_v1
from google.protobuf import descriptor_pb2

client = bigquery_storage_v1.BigQueryWriteClient()
parent = "projects/my-project/datasets/my_dataset/tables/my_table"
stream = client.create_write_stream(parent=parent)
```

### Check table schema
```bash
bq show --format=prettyjson PROJECT_ID:DATASET.TABLE | jq '.schema.fields'
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Query Execution Error]({{< relref "/cloud/gcp/gcp-query-execution-error" >}})
