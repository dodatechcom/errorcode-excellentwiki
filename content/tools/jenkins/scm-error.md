---
title: "[Solution] Jenkins SCM Checkout Failed"
description: "Fix Jenkins SCM checkout errors. Resolve Git, SVN, and source code management failures."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "scm", "checkout", "git", "svn", "source"]
weight: 5
---

# Jenkins SCM Checkout Failed

An SCM checkout failure means Jenkins cannot retrieve source code from the configured repository. This is typically a network, authentication, or repository configuration issue.

## Common Causes

- The repository URL is incorrect or unreachable
- Authentication credentials (SSH key or token) are missing or expired
- The branch, tag, or commit reference does not exist
- A firewall or proxy is blocking access to the repository

## How to Fix

### Verify Repository URL

```bash
# Test SSH access
ssh -T git@github.com

# Test HTTPS access
git ls-remote https://github.com/user/repo.git
```

### Configure Git Credentials in Pipeline

```groovy
stage('Checkout') {
    steps {
        checkout([
            $class: 'GitSCM',
            branches: [[name: '*/main']],
            userRemoteConfigs: [[
                url: 'https://github.com/user/repo.git',
                credentialsId: 'github-credentials'
            ]]
        ])
    }
}
```

### Fix SSH Key Access

```bash
# Generate key on Jenkins server
ssh-keygen -t ed25519 -C "jenkins@server"

# Add public key to GitHub/GitLab
```

### Check Branch Reference

```bash
# Verify branch exists
git ls-remote --heads https://github.com/user/repo.git main
```

### Fix Git Permissions

```bash
sudo chown -R jenkins:jenkins $JENKINS_HOME/workspace/
```

## Examples

```bash
# Authentication failed
# ERROR: Cannot retrieve revision from git repository
# Fix: update credentialsId with valid token or SSH key

# Branch not found
# ERROR: Could not find remote branch main
# Fix: check branch name — use master, main, or the actual branch
```

## Related Errors

- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax issue
- [Timeout Error]({{< relref "/tools/jenkins/timeout-error9" >}}) — build timed out
