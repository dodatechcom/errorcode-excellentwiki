---
title: "[Solution] AWS Lambda Provisioned Concurrency Error"
description: "ProvisionedConcurrencyConfigNotFoundException when PC fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Provisioned Concurrency Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Function does not have a published version or alias
- Provisioned concurrency quota per function exhausted
- Account-level provisioned concurrency limit reached
- Function has resolved concurrency conflicting
- Alias or version does not exist

## How to Fix

### Put PC config

```bash
aws lambda put-provisioned-concurrency-config --function-name my-function --qualifier prod --provisioned-concurrent-executions 100
```

### Check PC status

```bash
aws lambda get-provisioned-concurrency-config --function-name my-function --qualifier prod
```

## Examples

- Example scenario: function does not have a published version or alias
- Example scenario: provisioned concurrency quota per function exhausted
- Example scenario: account-level provisioned concurrency limit reached
- Example scenario: function has resolved concurrency conflicting

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
