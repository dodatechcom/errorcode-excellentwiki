---
title: "[Solution] AWS SAML Provider"
description: "InvalidInput for SAML providers."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SAML Provider` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Metadata invalid
- Name duplicate

## How to Fix

### Create SAML

```bash
aws iam create-saml-provider --saml metadata.xml --name MySAML
```

## Examples

- Example scenario: metadata invalid
- Example scenario: name duplicate

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
