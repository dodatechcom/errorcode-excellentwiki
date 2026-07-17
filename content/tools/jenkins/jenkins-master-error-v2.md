---
title: "Jenkins Controller Disk Space Error"
description: "Jenkins controller node runs out of disk space."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "controller", "master", "disk-space", "storage"]
weight: 5
---

# Jenkins Controller — Disk Space Error

This error occurs when the Jenkins controller (master) node runs out of disk space. Build artifacts, logs, and workspace data can consume significant storage.

## Common Causes

- Build artifacts not cleaned up
- Workspace directories accumulating
- Log files growing without rotation
- Old builds not archived or deleted
- Temporary files not cleaned

## How to Fix

### Check Disk Space

Go to **Manage Jenkins > System Information** and check `hudson.model.DiskSpaceMonitor`.

### Configure Build Discarder

```groovy
pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
}
```

### Clean Workspace Automatically

```groovy
post {
    always {
        cleanWs()
    }
}
```

### Set Disk Space Threshold

```groovy
// In manage Jenkins > System Configuration
// Set disk space threshold to trigger warnings
```

### Clean Old Builds

```bash
# Delete old build directories
find /var/jenkins/jobs/my-project/builds -maxdepth 1 -type d | \
  sort -rn | tail -n +11 | xargs rm -rf
```

### Configure Log Rotation

```groovy
// In Jenkinsfile
pipeline {
    options {
        buildDiscarder(logRotator(
            numToKeepStr: '10',
            artifactNumToKeepStr: '5'
        ))
    }
}
```

### Move Workspace to Separate Disk

```bash
# Create symlink for workspace
ln -s /data/jenkins/workspace /var/jenkins/workspace
```

## Examples

```text
Low Disk Space:
  The disk space is below the threshold of 1024 MB.
  Currently at: 512 MB free
```

## Related Errors

- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Plugin Error]({{< relref "/tools/jenkins/jenkins-plugin-error" >}}) — plugin issues
- [Jenkins Agent Error]({{< relref "/tools/jenkins/jenkins-agent-error" >}}) — agent connection issues
