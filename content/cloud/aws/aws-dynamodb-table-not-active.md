---
title: "[Solution] AWS DynamoDB Table Not Active"
description: "ResourceInUseException when table not ACTIVE."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DynamoDB Table Not Active` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Table in CREATING or UPDATING
- CloudFormation rollback

## How to Fix

### Wait for Active

```bash
aws dynamodb wait table-exists --table my-table
```

## Examples

- Example scenario: table in creating or updating
- Example scenario: cloudformation rollback

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
