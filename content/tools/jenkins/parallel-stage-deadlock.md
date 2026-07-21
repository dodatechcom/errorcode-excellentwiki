---
title: "[Solution] Jenkins Parallel Stage Deadlock"
description: "Fix Jenkins parallel stage deadlock errors when parallel branches in a pipeline wait on each other indefinitely."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Parallel Stage Deadlock

Parallel stage deadlock errors occur when two or more parallel branches in a Jenkins Pipeline wait for each other to complete, creating an unresolvable dependency cycle.

## Common Causes

- Two parallel stages both use `lock` on the same resource
- Parallel branches use `waitUntil` or `input` that never resolves
- Shared nodes with exclusive labels block parallel execution
- One parallel branch waits for another branch that is stuck

## How to Fix

### Solution 1: Remove shared locks from parallel stages

```groovy
pipeline {
    stages {
        stage('Parallel Work') {
            parallel {
                stage('Branch A') {
                    steps {
                        sh './task-a.sh'
                    }
                }
                stage('Branch B') {
                    steps {
                        sh './task-b.sh'
                    }
                }
            }
        }
    }
}
```

### Solution 2: Use lock only on serial stages

```groovy
pipeline {
    stages {
        stage('Deploy') {
            steps {
                lock('deploy-lock') {
                    sh './deploy.sh'
                }
            }
        }
    }
}
```

### Solution 3: Set timeouts on parallel branches

```groovy
parallel {
    stage('Branch A') {
        steps {
            timeout(time: 30, unit: 'MINUTES') {
                sh './long-task.sh'
            }
        }
    }
    stage('Branch B') {
        steps {
            timeout(time: 30, unit: 'MINUTES') {
                sh './other-task.sh'
            }
        }
    }
}
```

## Examples

```
ERROR: Stage 'Branch A' is waiting for an input step that will never be submitted
WARNING: Parallel stage deadlock detected
```

## Prevent It

- Avoid shared locks in parallel branches
- Set timeouts on all long-running steps
- Use separate labels for parallel agents
