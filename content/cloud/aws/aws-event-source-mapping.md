---
title: "[Solution] AWS Event Source Mapping"
description: "InvalidParameter/ResourceConflict for mappings."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Event Source Mapping` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Dynamo/Kinesis access denied
- Mapping limit per function reached
- SQS does not exist

## How to Fix

### List mappings

```bash
aws lambda list-event-source-mappings --function my-function
```

## Examples

- Example scenario: dynamo/kinesis access denied
- Example scenario: mapping limit per function reached
- Example scenario: sqs does not exist

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
