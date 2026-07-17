---
title: "GitHub Actions SSH Error"
description: "GitHub Actions workflow fails to establish SSH connection for deployment or operations."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "ssh", "deploy", "remote", "key"]
weight: 5
---

# GitHub Actions SSH Error

An SSH error occurs when a GitHub Actions workflow fails to establish an SSH connection for remote operations like deployment, cloning private repositories, or running remote commands.

## Common Causes

- SSH private key not configured as secret
- Host key verification fails
- SSH key permissions incorrect
- Target host unreachable or SSH service down
- SSH key algorithm not supported

## How to Fix

### Configure SSH Key

```yaml
- name: Setup SSH
  uses: webfactory/ssh-agent@v0.9.0
  with:
    ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
```

### Add Host Key

```yaml
- name: Add host key
  run: |
    mkdir -p ~/.ssh
    ssh-keyscan -H example.com >> ~/.ssh/known_hosts
```

### Fix SSH Key Permissions

```yaml
- name: Setup SSH
  run: |
    mkdir -p ~/.ssh
    echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
    chmod 600 ~/.ssh/id_rsa
```

### Use SSH Action

```yaml
- name: Deploy via SSH
  uses: appleboy/ssh-action@v1.0.0
  with:
    host: ${{ secrets.SERVER_HOST }}
    username: ${{ secrets.SERVER_USER }}
    key: ${{ secrets.SSH_PRIVATE_KEY }}
    script: cd /app && git pull && pm2 restart all
```

### Verify Connection

```yaml
- name: Test SSH connection
  run: ssh -o StrictHostKeyChecking=no user@host "echo connected"
```

## Examples

```yaml
# Error: host key verification failed
Host key verification failed.
fatal: Could not read from remote repository.

# Fix: add host key
- run: ssh-keyscan example.com >> ~/.ssh/known_hosts
```

## Related Errors

- [Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
