---
title: "[Solution] Jenkins Node Label Not Available"
description: "Fix Jenkins node label not available errors when no build agents match the required label expression for a pipeline stage."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Node Label Not Available

Node label not available errors occur when a pipeline stage requires a specific agent label but no online agents in the Jenkins cluster match that label.

## Common Causes

- No agents are configured with the required label
- All agents with the required label are offline
- Label expression is misspelled
- Agent labels were changed after pipeline creation

## How to Fix

### Solution 1: Check available agents

Navigate to **Manage Jenkins > Nodes** and verify agents with the required label are online.

### Solution 2: Use a fallback label expression

```groovy
pipeline {
    agent {
        label 'linux || docker'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building on available agent'
            }
        }
    }
}
```

### Solution 3: Use any available agent

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building on any available agent'
            }
        }
    }
}
```

## Examples

```
Required label: 'gpu' - but no agent is either: online, matching this label, or in the quiet period
```

## Prevent It

- Maintain agents with commonly used labels
- Use label expressions with fallback options
- Monitor agent availability in Jenkins dashboard
