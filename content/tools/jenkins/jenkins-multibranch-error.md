---
title: "Jenkins Multibranch Pipeline Error"
description: "Jenkins Multibranch pipeline fails to scan, build, or index branches."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Jenkins Multibranch Pipeline Error

A Jenkins Multibranch pipeline error occurs when the pipeline fails to scan branches, create jobs for branches, or build branch-specific pipelines. Multibranch pipelines automatically detect and build branches from a Git repository.

## Common Causes

- Jenkinsfile not found in branch
- Branch scanning fails due to repository access issues
- Multiple Jenkinsfiles cause confusion
- Branch indexing fails with timeout

## How to Fix

### Verify Jenkinsfile Exists

```bash
git ls-remote --heads origin
git checkout feature-branch
ls Jenkinsfile
```

### Configure Branch Sources

Go to **Multibranch Pipeline > Configure > Branch Sources**:
- Add Git repository URL
- Configure credentials for private repos

### Fix Branch Scanning

```groovy
// Jenkinsfile in branch
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}
```

### Handle Scan Failures

```groovy
// In Jenkinsfile
pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}
```

### Fix Indexing Timeout

```groovy
// Configure in Multibranch Pipeline settings
// Scan Multibranch Pipeline Triggers: Periodically if not otherwise run
```

### Check Repository Permissions

```bash
# Verify Jenkins can access the repository
git clone https://github.com/owner/repo.git
```

## Examples

```text
Finished: SUCCESS (scanned 5 branches, found 2 with Jenkinsfile)
Finished: FAILURE (unable to access repository)
```

## Related Errors

- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax error
- [SCM Error]({{< relref "/tools/jenkins/scm-error" >}}) — source control error
- [Credential Error]({{< relref "/tools/jenkins/credential-error2" >}}) — credential issues
