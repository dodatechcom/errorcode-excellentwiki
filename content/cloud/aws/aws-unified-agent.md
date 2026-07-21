---
title: "[Solution] AWS Unified Agent"
description: "CWAgentConfigurationError."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Unified Agent` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Agent version mismatch
- Plugins invalid

## How to Fix

### Restart agent

```bash
sudo systemctl restart amazon-cloudwatch-agent
```

## Examples

- Example scenario: agent version mismatch
- Example scenario: plugins invalid

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
