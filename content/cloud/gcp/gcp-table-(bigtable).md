---
title: "[Solution] GCP Table (Bigtable)"
description: "BigtableTableError for tables."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Table (Bigtable)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Table already exists in instance
- Column family not defined
- Single cluster routing needed for transactions

## How to Fix

### Create table

```bash
cbt createtable myTable --families=cf1
```

## Examples

- Example scenario: table already exists in instance
- Example scenario: column family not defined
- Example scenario: single cluster routing needed for transactions

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
