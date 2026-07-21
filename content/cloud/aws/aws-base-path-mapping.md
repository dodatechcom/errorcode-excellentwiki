---
title: "[Solution] AWS Base Path Mapping"
description: "NotFoundException for base path."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Base Path Mapping` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Path doesn't match mapping
- Domain not found

## How to Fix

### Get mappings

```bash
aws apigateway get-base-path-mappings --domain my-api.com
```

## Examples

- Example scenario: path doesn't match mapping
- Example scenario: domain not found

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
