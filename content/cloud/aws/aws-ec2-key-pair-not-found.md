---
title: "[Solution] AWS EC2 Key Pair Not Found"
description: "InvalidKeyPair.NotFound when the specified key pair does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Key Pair Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The key pair name is incorrect
- The key pair was deleted
- The key pair is in a different region
- Using key file name instead of key pair name

## How to Fix

### Describe key pairs

```bash
aws ec2 describe-key-pairs --region us-east-1
```
### Create new key pair

```bash
aws ec2 create-key-pair --key-name my-new-key --query 'KeyMaterial' --output text > my-new-key.pem
```
### Import existing key

```bash
aws ec2 import-key-pair --key-name my-key --public-key-material fileb://~/.ssh/id_rsa.pub
```

## Examples

- Launching with --key-name mykey but key was named my-key
- Key pair deleted from us-east-1 but launch targets us-west-2

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Instance Not Found]({{< relref "/cloud/aws/aws-ec2-instance-not-found" >}}) -- Instance errors
