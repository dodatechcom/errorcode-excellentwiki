---
title: "[Solution] Jenkins Workspace Cleanup Permission"
description: "Fix Jenkins workspace cleanup permission errors when the agent cannot delete files from the build workspace after a job completes."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Workspace Cleanup Permission

Workspace cleanup permission errors occur when the Jenkins agent process lacks file system permissions to delete files and directories in the build workspace after a job completes.

## Common Causes

- Build process creates files owned by a different user (e.g., Docker containers)
- Read-only files or directories prevent deletion
- File system is mounted with restricted permissions
- Windows file locking prevents cleanup
- Symlinks point outside the workspace

## How to Fix

### Solution 1: Configure workspace cleanup plugin

```groovy
pipeline {
    agent any
    post {
        always {
            cleanWs()
        }
    }
}
```

### Solution 2: Fix permissions in the build script

```groovy
pipeline {
    stages {
        stage('Build') {
            steps {
                sh '''
                    docker run --user $(id -u):$(id -g) myimage
                '''
            }
        }
    }
}
```

### Solution 3: Use workspace stashing for selective cleanup

```groovy
pipeline {
    stages {
        stage('Build') {
            steps {
                stash includes: 'dist/**', name: 'build-output'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
```

## Examples

```
WARNING: Failed to delete workspace: Permission denied
ERROR: Unable to delete workspace directory
```

## Prevent It

- Use `cleanWs()` plugin for reliable cleanup
- Run Docker containers with matching UID/GID
- Avoid creating files with restricted permissions
