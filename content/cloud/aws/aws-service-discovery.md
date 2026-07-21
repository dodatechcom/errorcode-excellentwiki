---
title: "[Solution] AWS Service Discovery"
description: "ServiceDiscoveryDisabled."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Discovery` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Private zone not created
- Namespace not exist

## How to Fix

### List services

```bash
aws servicediscovery list-services
```

## Examples

- Example scenario: private zone not created
- Example scenario: namespace not exist

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
