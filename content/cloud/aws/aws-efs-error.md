---
title: "[Solution] AWS EFS Mount Error"
description: "Fix AWS EFS mount errors. Resolve Elastic File System mounting issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS EFS mount error occurs when you cannot mount or access an EFS file system from an EC2 instance or container.

## Common Causes

- Security group does not allow NFS traffic (port 2049)
- Mount target is in a different AZ than the instance
- EFS file system is in a different VPC
- NFS client not installed on the instance
- Mount point permissions are incorrect

## How to Fix

### Check Mount Target Status

```bash
aws efs describe-mount-targets --file-system-id fs-xxx
```

### Verify Security Group

```bash
aws ec2 describe-security-groups --group-ids sg-xxx \
  --query 'SecurityGroups[*].IpPermissions[?FromPort==`2049`]'
```

### Install NFS Client

```bash
# Amazon Linux
sudo yum install -y nfs-utils

# Ubuntu
sudo apt-get install -y nfs-common
```

### Mount EFS

```bash
sudo mount -t nfs4 fs-xxx.efs.us-east-1.amazonaws.com:/ /mnt/efs
```

### Test Mount

```bash
touch /mnt/efs/test.txt
ls -la /mnt/efs/
```

## Examples

```bash
# Example 1: Connection timed out
mount.nfs4: Connection timed out
# Fix: add inbound rule for port 2049

# Example 2: Permission denied
mount.nfs4: access denied by server
# Fix: check file system policy and VPC settings
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance error
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
