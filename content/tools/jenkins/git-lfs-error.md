---
title: "[Solution] Jenkins Git LFS Error"
description: "Fix Git LFS errors in Jenkins pipeline. Resolve Large File Storage checkout and pull failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Git LFS Error

Git LFS errors occur when Jenkins cannot properly checkout or pull large files tracked by Git LFS.

## Common Causes

- Git LFS not installed on the agent
- LFS credentials not configured
- LFS storage quota exceeded

## How to Fix

```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
```

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: env.GIT_URL, credentialsId: 'git-lfs-creds']],
    extensions: [[$class: 'LfsCheckout']]
])
```
