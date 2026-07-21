---
title: "[Solution] AWS Replica Not Found"
description: "ReplicaNotFoundException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Replica Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Replica name does not exist
- Deleted from global table

## How to Fix

### Check replicas

```bash
aws dynamodb describe-global-table --global-table-name my-table
```

## Examples

- Example scenario: replica name does not exist
- Example scenario: deleted from global table

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
