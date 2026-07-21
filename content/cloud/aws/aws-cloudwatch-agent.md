---
title: "[Solution] AWS CloudWatch Agent"
description: "CloudWatchAgentConfigurationError."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `CloudWatch Agent` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Config file invalid
- Agent not running
- Firewall blocking

## How to Fix

### Check agent

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```

## Examples

- Example scenario: config file invalid
- Example scenario: agent not running
- Example scenario: firewall blocking

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
