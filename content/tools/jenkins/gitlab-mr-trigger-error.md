---
title: "[Solution] Jenkins GitLab Merge Request Trigger Error"
description: "Fix Jenkins GitLab merge request trigger errors. Resolve GitLab webhook and MR build configuration issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins GitLab Merge Request Trigger Error

GitLab merge request triggers fail when Jenkins cannot receive or process webhook events from GitLab.

## Common Causes

- GitLab plugin not installed or misconfigured
- Jenkins URL not accessible from GitLab
- Secret token mismatch

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "GitLab"
```

```groovy
properties([
    gitLabConnection('gitlab.example.com'),
    [pipelineTriggers: [[$class: 'GitLabTrigger', triggerOnPush: true, triggerOnMergeRequest: true, branchFilterType: 'AllBranches']]]
])
```
