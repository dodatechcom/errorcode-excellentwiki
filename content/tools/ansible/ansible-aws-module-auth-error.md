---
title: "[Solution] Ansible AWS Module Authentication Error"
description: "Fix Ansible AWS module authentication failures for EC2, S3, and other services"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible AWS modules fail due to authentication issues.

```
FAILED! => AuthFailure: AWS was not able to validate the provided access credentials
```

## Common Causes

- AWS credentials not configured
- Expired access keys
- Incorrect region
- IAM permissions insufficient

## How to Fix

```bash
aws configure
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-east-1
```

```yaml
- name: Create EC2 instance
  amazon.aws.ec2_instance:
    name: my-server
    instance_type: t3.micro
    image_id: ami-12345678
    region: us-east-1
    aws_access_key: "{{ vault_aws_access_key }}"
    aws_secret_key: "{{ vault_aws_secret_key }}"
```
