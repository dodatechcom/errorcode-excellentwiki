---
title: "[Solution] AWS Transaction Error"
description: "TransactionCanceledException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Transaction Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Concurrent modification
- Conditional check failed
- Transaction more than 4MB

## How to Fix

### TransactWrite

```bash
aws dynamodb transact-write-items --transact file://transact.json
```

## Examples

- Example scenario: concurrent modification
- Example scenario: conditional check failed
- Example scenario: transaction more than 4mb

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
