---
title: "[Solution] AWS DynamoDB Table Not Found"
description: "ResourceNotFoundException when the specified table does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DynamoDB Table Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Table name incorrect (case-sensitive)
- Table was deleted
- Table in different region
- IAM role lacks dynamodb:DescribeTable permission

## How to Fix

### Describe table

```bash
aws dynamodb describe-table --table-name my-table
```
### List tables

```bash
aws dynamodb list-tables --query TableNames --output table
```
### Create table

```bash
aws dynamodb create-table --table-name my-table --attribute-definitions AttributeName=pk,AttributeType=S --key-schema AttributeName=pk,KeyType=HASH --billing-mode PAY_PER_REQUEST
```

## Examples

- Calling describe-table with MyTable but actual name is mytable
- Table deleted last week

## Related Errors

- [DynamoDB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General DynamoDB errors
- [Table Active]({{< relref "/cloud/aws/aws-dynamodb-table-active" >}}) -- Table status
