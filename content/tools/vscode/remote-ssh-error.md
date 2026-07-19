---
title: "[Solution] VS Code Failed to connect to remote host"
description: "Fix VS Code Remote SSH errors. Resolve connection failures when using VS Code's Remote-SSH extension."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "remote", "ssh", "connection"]
severity: "error"
---

# Failed to connect to remote host

## Error Message

```
Failed to connect to remote host: Connection timed out after 30000ms. Unable to establish SSH connection to user@remote-server. Please verify your SSH configuration.
```

## Common Causes

- SSH server on the remote host is not running or not accepting connections
- Incorrect SSH host, port, or credentials in the remote configuration
- Firewall blocking SSH port 22 on either end
- SSH key authentication failing due to incorrect key permissions

## Solutions

### Solution 1: Test SSH Connection

Verify SSH connectivity from the terminal before using VS Code's Remote-SSH.

```
ssh -o ConnectTimeout=10 user@remote-server echo 'Connection successful'
```

### Solution 2: Configure SSH Host

Add or update the SSH host configuration in your SSH config file with correct connection parameters.

```
Host remote-server
  HostName remote-server.example.com
  User deploy
  Port 22
  IdentityFile ~/.ssh/id_rsa
  ForwardAgent yes
```

### Solution 3: Fix SSH Key Permissions

Ensure SSH key files have the correct permissions required for key-based authentication.

```
chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_rsa && chmod 644 ~/.ssh/id_rsa.pub
```

## Prevention Tips

- Add SSH keepalive settings to prevent connection timeouts
- Use SSH multiplexing for faster reconnections
- Verify the remote VS Code server is compatible with your local version

## Related Errors

- [Failed to attach to container]({{< relref "/tools/vscode/remote-container-error" >}})
- [WSL connection failed]({{< relref "/tools/vscode/remote-wsl-error" >}})
- [Remote development error]({{< relref "/tools/vscode/remote-development-error" >}})
