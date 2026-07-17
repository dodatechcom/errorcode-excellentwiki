---
title: "GitHub Actions SSH Deploy Key Error"
description: "GitHub Actions workflow fails with SSH deploy key authentication error."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — SSH Deploy Key Error

This error occurs when a GitHub Actions workflow fails to authenticate using an SSH deploy key. The key may not be configured correctly or may lack the required permissions.

## Common Causes

- Deploy key not added to repository
- Deploy key does not have write access
- SSH agent not configured in workflow
- Key file format is incorrect
- Known hosts not configured

## How to Fix

### Set Up SSH Agent

```yaml
steps:
  - uses: webfactory/ssh-agent@v0.9.0
    with:
      ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
```

### Configure Known Hosts

```yaml
- name: Add known hosts
  run: |
    mkdir -p ~/.ssh
    ssh-keyscan github.com >> ~/.ssh/known_hosts
```

### Deploy Key Setup

1. Go to **Settings > Deploy keys > Add deploy key**
2. Check "Allow write access" if needed
3. Add the public key to the repository

### Use SSH for Git Operations

```yaml
steps:
  - uses: webfactory/ssh-agent@v0.9.0
    with:
      ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
  - run: |
      git config user.name "GitHub Actions"
      git config user.email "actions@github.com"
      git push origin main
```

### Test SSH Connection

```yaml
- run: ssh -T git@github.com
```

## Examples

```text
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

## Related Errors

- [GitHub Actions Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [GitHub Actions Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [GitHub Actions YAML Error]({{< relref "/tools/github-actions/github-actions-yaml-error" >}}) — YAML syntax error
