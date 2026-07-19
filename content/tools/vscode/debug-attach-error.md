---
title: "[Solution] VS Code Cannot attach to target process"
description: "Fix VS Code debug attach errors. Resolve issues when the debugger cannot attach to a running process."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "debugging", "attach", "process"]
severity: "error"
---

# Cannot attach to target process

## Error Message

```
Cannot attach to target process: connect ECONNREFUSED 127.0.0.1:9229. The target process may not be running in debug mode.
```

## Common Causes

- Target process was not started with the --inspect flag
- Firewall or network policy blocking the debug port
- Process ID in the attach configuration is incorrect
- Remote debugging requires SSH tunnel or port forwarding

## Solutions

### Solution 1: Enable Inspector Protocol

Restart the target application with Node.js inspector enabled to allow debugger attachment.

```
node --inspect=0.0.0.0:9229 src/server.js
```

### Solution 2: Configure SSH Tunnel for Remote Debugging

Set up an SSH tunnel to forward the debug port from the remote server to your local machine.

```
ssh -L 9229:localhost:9229 user@remote-server
```

### Solution 3: Update Attach Configuration

Set the correct process ID or port in your attach configuration in launch.json.

```
{"configurations": [{"type": "node", "request": "attach", "name": "Attach to Process", "port": 9229, "restart": true, "protocol": "inspector"}]}
```

## Prevention Tips

- Use '0.0.0.0' instead of 'localhost' for remote debugging
- Ensure the debug port is not blocked by firewalls
- Use process IDs for more reliable attach configurations

## Related Errors

- [Cannot launch debug target]({{< relref "/tools/vscode/debug-launch-error" >}})
- [Breakpoint could not be set]({{< relref "/tools/vscode/debug-breakpoint-error" >}})
- [Remote SSH error]({{< relref "/tools/vscode/remote-ssh-error" >}})
