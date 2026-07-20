---
title: "[Solution] AWS WorkSpaces Error — bundle/volume/client failures"
description: "Fix AWS WorkSpaces errors. Resolve bundle, volume, and client connection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 170
---

An AWS WorkSpaces error occurs when WorkSpaces fail to launch, client connections break, or user volumes encounter issues. Amazon WorkSpaces provides persistent desktops but requires proper networking and licensing.

## Common Causes

- WorkSpace bundle not available in the region
- User does not exist in Active Directory
- Client application version outdated
- IP access control group blocking connection
- Root or user volume storage exceeded

## How to Fix

### List WorkSpaces

```bash
aws workspaces describe-workspaces \
  --query 'Workspaces[*].{ID:WorkspaceId,State:State,Bundle:BundleId}'
```

### Describe WorkSpace

```bash
aws workspaces describe-workspaces \
  --workspace-ids ws-xxx
```

### Create WorkSpace

```bash
aws workspaces create-workspaces \
  --workspaces '[{
    "DirectoryId": "d-xxx",
    "UserName": "jdoe",
    "BundleId": "wsb-xxx",
    "RootVolumeSizeGib": 80,
    "UserVolumeSizeGib": 50
  }]'
```

### Reboot WorkSpace

```bash
aws workspaces reboot-workspaces \
  --workspace-ids ws-xxx
```

### Rebuild WorkSpace

```bash
aws workspaces rebuild-workspaces \
  --workspace-ids ws-xxx
```

## Examples

```bash
# Example 1: Bundle not found
# ResourceNotFoundException: Bundle not found
# Fix: use list-workspace-bundles to check available bundles

# Example 2: User not found
# InvalidParameterException: User not found in directory
# Fix: verify user exists in Active Directory
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS Directory Service Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — Directory/IAM errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
