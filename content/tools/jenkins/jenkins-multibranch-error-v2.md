---
title: "Jenkins Multibranch Branch Indexing Error"
description: "Jenkins multibranch pipeline fails during branch indexing."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "multibranch", "branch", "indexing", "scm"]
weight: 5
---

# Jenkins Multibranch — Branch Indexing Error

This error occurs when a Jenkins multibranch pipeline fails during branch indexing. Jenkins cannot scan the repository for branches or detect Jenkinsfiles.

## Common Causes

- SCM repository URL is incorrect
- SCM credentials are invalid or missing
- Branch indexing timeout
- Repository contains too many branches
- Jenkinsfile not found in branches

## How to Fix

### Verify SCM Configuration

Go to **Multibranch Pipeline > Configure > Branch Sources** and verify the repository URL.

### Configure Credentials

```groovy
// In multibranch pipeline configuration
// Add SCM credentials for private repositories
```

### Set Branch Indexing Behaviors

```groovy
// Configure which branches to index
// Add include/exclude patterns
```

### Fix Branch Discovery

Go to **Multibranch Pipeline > Configure > Branch Sources > Behaviors**

Add:
- **Discover branches**: All branches
- **Discover pull requests from origin**

### Check Repository Access

```bash
# Test git access
git ls-remote https://github.com/org/repo.git
```

### Limit Branch Count

```yaml
# In repository settings
# Limit branches scanned to reduce indexing time
```

### Trigger Reindex

Go to **Multibranch Pipeline > Scan Repository Now**

## Examples

```text
Branch indexing failed for org/repo
  java.io.IOException: Cannot run program "git":
    error=2, No such file or directory
```

## Related Errors

- [Jenkins SCM Error]({{< relref "/tools/jenkins/scm-error" >}}) — SCM connection issues
- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Permission Error]({{< relref "/tools/jenkins/jenkins-permission-error" >}}) — permission issues
