---
title: "[Solution] Git Branch Not Found in Jenkins Pipeline"
description: "Fix git branch not found errors in Jenkins. Resolve branch checkout failures in multibranch pipelines."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Branch Not Found in Jenkins Pipeline

Jenkins fails when trying to check out a branch that does not exist in the remote repository.

## Common Causes

- Branch was deleted
- Typo in the branch name (`main` vs `master`)
- Default branch name changed

## How to Fix

```groovy
branches: [[name: 'main']]
```

```bash
git ls-remote --heads https://github.com/org/repo.git
```

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: params.BRANCH, url: 'https://github.com/org/repo.git'
            }
        }
    }
}
```
