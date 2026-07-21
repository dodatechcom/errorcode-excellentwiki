---
title: "[Solution] AWS Provisioned Concurrency"
description: "ProvisionedConcurrencyConfigNotFoundException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Provisioned Concurrency` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Alias/version missing
- Account limit reached

## How to Fix

### Put PC

```bash
aws lambda put-provisioned-concurrency-config --function m-f --qual prod --count 100
```

## Examples

- Example scenario: alias/version missing
- Example scenario: account limit reached

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
