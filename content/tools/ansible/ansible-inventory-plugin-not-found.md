---
title: "[Solution] Ansible Inventory Plugin Not Found"
description: "Fix Ansible inventory plugin configuration and availability errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the specified inventory plugin.

```
ERROR! Could not find inventory plugin 'aws_ec2'
```

## Common Causes

- Plugin not installed
- Collection not installed
- Plugin name incorrect

## How to Fix

```bash
# Install required collection
ansible-galaxy collection install amazon.aws

# List available inventory plugins
ansible-doc -t inventory -l
```

```yaml
# aws_ec2.yml inventory
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
keyed_groups:
  - key: tags.Name
    prefix: tag
filters:
  tag:Environment: production
```

```ini
# Use in ansible.cfg
[defaults]
inventory = aws_ec2.yml
```
