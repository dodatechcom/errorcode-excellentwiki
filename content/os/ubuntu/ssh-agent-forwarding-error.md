---
title: "SSH Agent Forwarding Error"
description: "SSH agent forwarding fails preventing use of local keys on remote server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Agent Forwarding Error

SSH agent forwarding fails preventing use of local keys on remote server

## Common Causes

- Agent forwarding not enabled in ssh_config
- Remote server has AgentForwarding disabled in sshd_config
- SSH_AUTH_SOCK not set in remote shell environment
- Key not added to local ssh-agent

## How to Fix

1. Enable forwarding: `ssh -A user@host`
2. Check agent: `ssh-add -l`
3. Verify on remote: `ssh user@host "echo $SSH_AUTH_SOCK"`
4. Add key to agent: `ssh-add ~/.ssh/id_rsa`

## Examples

```bash
# Add key to local agent
eval $(ssh-agent) && ssh-add ~/.ssh/id_rsa

# Connect with agent forwarding
ssh -A user@remote-host

# Verify agent on remote
ssh -A user@host "ssh-add -l"
```
