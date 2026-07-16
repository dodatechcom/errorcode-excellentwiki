---
title: "[Solution] Jenkins Node Offline"
description: "Fix Jenkins node offline errors. Resolve agent connectivity and workspace issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "node", "offline", "agent", "connection"]
weight: 5
---

# Jenkins Node Offline

A node offline error means Jenkins cannot communicate with a build agent. The agent machine may be down, the JNLP connection may have dropped, or the agent's disk is full.

## Common Causes

- The agent machine is powered off or unreachable
- The JNLP agent process has crashed or been killed
- The agent's disk is full, preventing communication
- Network or firewall changes block the connection

## How to Fix

### Check Node Status

```
Jenkins > Manage Jenkins > Manage Nodes
```

### Reconnect JNLP Agent

```bash
# On the agent machine
java -jar agent.jar \
  -url http://jenkins.example.com \
  -secret @secret-file \
  -name agent-name \
  -workDir /home/jenkins
```

### Restart Agent via SSH

```bash
ssh agent-user@agent-host "sudo systemctl restart jenkins-agent"
```

### Set Node to Launch Agents via SSH

```groovy
// In node configuration
// Launch method: Launch agents via SSH
// Host: agent-host.example.com
// Credentials: SSH credentials for agent
```

### Verify Agent Can Reach Jenkins

```bash
# On the agent machine
curl -I http://jenkins.example.com:8080
telnet jenkins.example.com 8080
```

## Examples

```bash
# Agent machine restarted, JNLP not running
# Node 'build-agent' is offline
# Fix: re-launch the agent JNLP jar

# Disk full on agent
# Node 'build-agent' is offline: No space left on device
# Fix: free disk space and restart agent
```

## Related Errors

- [Build Failed]({{< relref "/tools/jenkins/build-failed" >}}) — build step returned error
- [Credential Error]({{< relref "/tools/jenkins/credential-error2" >}}) — credential not found
