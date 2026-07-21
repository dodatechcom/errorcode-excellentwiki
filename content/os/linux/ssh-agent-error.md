---
title: "[Solution] Linux: ssh-agent-error -- SSH agent failure"
description: "Fix Linux SSH agent errors. SSH agent forwarding or key management failure."
os: ["linux"]
error-types: ["ssh-error"]
severities: ["error"]
---

# Linux: SSH Agent Error

SSH agent errors prevent key-based authentication forwarding through agent.

## Common Causes

- SSH agent not running (SSH_AUTH_SOCK not set)
- Agent forwarding not enabled in SSH config
- Key not added to agent with ssh-add
- Agent socket permissions preventing connection
- gpg-agent not providing SSH agent

## How to Fix

### 1. Check Agent Status

```bash
echo $SSH_AUTH_SOCK
ssh-add -l
ssh-agent -k
```

### 2. Start and Configure Agent

```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
# Add to server config: ForwardAgent yes
```

### 3. Fix Socket Permissions

```bash
ls -la $SSH_AUTH_SOCK
chmod 700 /tmp/agent-*
```

## Examples

```bash
$ ssh-add -l
error: Could not open a connection to your authentication agent.
$ eval $(ssh-agent -s)
Agent pid 12345
$ ssh-add ~/.ssh/id_rsa
Identity added: /home/user/.ssh/id_rsa
```
