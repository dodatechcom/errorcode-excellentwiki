---
title: "GCP BigQuery: Access Denied to Table"
description: "BigQuery: Access denied to table — Fix Google BigQuery authorization and permission errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "bigquery", "bq", "access-denied", "table", "dataset", "iam"]
weight: 5
---

The `Access denied to table` error occurs when a BigQuery user or service account attempts to query, export, or modify a table without the required dataset or table-level IAM permissions. BigQuery uses a hierarchy of project → dataset → table permissions.

## Common Causes

- The identity lacks `bigquery.dataViewer` or `bigquery.dataEditor` on the dataset
- Table-level access controls override dataset-level permissions
- The identity is not in the correct Google Group for shared access
- The query uses a cross-project dataset reference without proper permissions
- Legacy table ACLs conflict with IAM policies

## How to Fix

Check dataset-level permissions:

```bash
bq show --format=prettyjson my-project:my_dataset | jq '.access'
```

Grant dataset-level access:

```bash
bq update --set_iam_policy - my-project:my_dataset <<EOF
{
  "bindings": [
    {
      "role": "roles/bigquery.dataViewer",
      "members": ["user:analyst@example.com"]
    }
  ]
}
EOF
```

Or using gcloud:

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:analyst@example.com" \
  --role="roles/bigquery.dataViewer"
```

Grant table-level access:

```bash
bq update --transfer_config \
  --source=TRANSFER_CONFIG \
  my-project:my_dataset.my_table
```

Check table permissions:

```bash
bq show --format=prettyjson my-project:my_dataset.my_table | jq '.access'
```

## Examples

- A service account can query tables in `dataset_a` but not `dataset_b` because only `dataset_a` has a policy binding
- Cross-project query fails because the reader identity does not have `bigquery.dataViewer` on the source project
- BigQuery Data Transfer Service cannot write to the destination table

## Related Errors

- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied10" >}}) — general permission errors.
- [GCP Firebase Error]({{< relref "/cloud/gcp/firebase-error" >}}) — Firebase project errors.
- [AWS IAM Error]({{< relref "/cloud/aws/iam-error" >}}) — AWS IAM authorization.
