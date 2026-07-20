---
title: "[Solution] GitHub Actions Runner Already Registered Error"
description: "Fix GitHub Actions runner already registered errors when re-registering a runner."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Runner already registered errors occur when attempting to register a runner that is already configured:

```
Error: Runner with name 'build-runner-01' is already registered
```

## Common Causes

- Attempting to register a runner that was not properly removed first.
- Previous registration attempt left partial configuration.

## How to Fix

**Remove and re-register:**

```bash
./config.sh remove
./config.sh --url https://github.com/{owner}/{repo} --token {NEW_TOKEN}
```

**Remove via API:**

```bash
gh api repos/{owner}/{repo}/actions/runners/{RUNNER_ID} -X DELETE
```

## Examples

```bash
# Check existing runners
gh api repos/{owner}/{repo}/actions/runners | jq '.runners[].name'

# Remove specific runner
./config.sh remove
```
