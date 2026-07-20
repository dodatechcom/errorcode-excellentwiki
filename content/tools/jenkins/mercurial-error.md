---
title: "[Solution] Jenkins Mercurial SCM Error"
description: "Fix Mercurial SCM errors in Jenkins pipeline. Resolve Hg repository checkout and polling failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Mercurial SCM Error

Mercurial (Hg) SCM errors occur when Jenkins cannot communicate with or checkout from a Mercurial repository.

## Common Causes

- Mercurial plugin not installed or outdated
- `hg` command not available on the agent
- Repository URL is incorrect

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Mercurial"
which hg || apt-get install mercurial
```

```groovy
checkout([
    $class: 'MercurialSCM',
    source: 'ssh://hg@hg.example.com/repo',
    credentialsId: 'hg-ssh-key',
    branches: [[name: 'default']]
])
```
