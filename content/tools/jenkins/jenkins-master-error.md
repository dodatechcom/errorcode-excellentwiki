---
title: "Jenkins Master Error"
description: "Jenkins controller/master node encounters critical errors."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Master Error

A Jenkins master (controller) error occurs when the main Jenkins server encounters critical issues affecting its operation. This can impact all jobs and agents connected to the controller.

## Common Causes

- Jenkins service crashed or stopped
- Disk space exhaustion on controller
- Database corruption (JENKINS_HOME)
- Java heap space exhaustion
- Plugin causing controller instability

## How to Fix

### Check Jenkins Service Status

```bash
systemctl status jenkins
```

### Check Disk Space

```bash
df -h /var/lib/jenkins
# Jenkins needs at least 1GB free space
```

### Check Jenkins Logs

```bash
tail -100 /var/log/jenkins/jenkins.log
```

### Increase Java Heap

```bash
# Edit /etc/default/jenkins or /etc/sysconfig/jenkins
JAVA_OPTS="-Xmx4g -XX:MaxMetaspaceSize=512m"
```

### Restart Jenkins

```bash
systemctl restart jenkins
```

### Check for Plugin Issues

```bash
# Disable problematic plugins
ls /var/lib/jenkins/plugins/
# Move problematic plugin .jpi files to disable them
```

### Recover from Corruption

```bash
# Backup JENKINS_HOME
cp -r /var/lib/jenkins /var/lib/jenkins-backup

# Check for corruption
ls -la /var/lib/jenkins/*.xml
# Recreate corrupted files from backup
```

## Examples

```text
SEVERE: Jenkins instance is temporarily offline
java.lang.OutOfMemoryError: Java heap space
```

## Related Errors

- [Plugin Error]({{< relref "/tools/jenkins/jenkins-plugin-error" >}}) — plugin issues
- [Agent Error]({{< relref "/tools/jenkins/agent-error" >}}) — agent connection issues
