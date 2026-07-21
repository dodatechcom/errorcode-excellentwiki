---
title: "[Solution] Prometheus EC2 Service Discovery Error"
description: "How to fix Prometheus EC2-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- AWS credentials missing or invalid
- IAM role permissions insufficient
- Wrong AWS region specified
- EC2 instances not tagged properly

## How to Fix

Configure EC2 SD:

```yaml
scrape_configs:
  - job_name: 'ec2'
    ec2_sd_configs:
      - region: us-east-1
        access_key: YOUR_ACCESS_KEY
        secret_key: YOUR_SECRET_KEY
        filters:
          - name: tag:prometheus
            values: ['true']
        port: 9090
```

Use IAM role instead of keys:

```yaml
    ec2_sd_configs:
      - region: us-east-1
        role_arn: arn:aws:iam::ACCOUNT:role/prometheus-discovery
```

## Examples

```bash
# Test AWS credentials
aws sts get-caller-identity

# List EC2 instances
aws ec2 describe-instances --filters "Name=tag:prometheus,Values=true"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_ec2_tag_prometheus != null)'
```
