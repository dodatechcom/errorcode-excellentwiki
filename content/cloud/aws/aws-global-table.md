---
title: "[Solution] AWS Global Table"
description: "GlobalTableNotFoundException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Global Table` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Table not global
- Region not in replication

## How to Fix

### Describe global table

```bash
aws dynamodb describe-global-table --global-table-name my-table
```

## Examples

- Example scenario: table not global
- Example scenario: region not in replication

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
