---
title: "Jenkins Agent Connection Error"
description: "Jenkins agent node cannot connect to the master/controller."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "agent", "node", "connection", "slave"]
weight: 5
---

# Jenkins Agent Connection Error

A Jenkins agent connection error occurs when an agent node cannot establish or maintain a connection to the Jenkins controller. This prevents jobs from being scheduled on the agent.

## Common Causes

- Agent service not running
- Network connectivity issues between agent and controller
- SSH key authentication failure
- Agent JNLP port blocked by firewall
- Agent version mismatch with controller

## How to Fix

### Check Agent Status

Go to **Manage Jenkins > Nodes** and check agent status.

### Verify Network Connectivity

```bash
# From agent machine
telnet jenkins-controller 8080
telnet jenkins-controller 50000  # JNLP port
```

### Restart Agent Service

```bash
# On Linux agent
sudo systemctl restart jenkins-agent

# Or via JNLP
java -jar agent.jar -url http://controller:8080 -secret @secret -name agent1 -workDir /var/jenkins
```

### Fix SSH Agent Connection

```groovy
// In Jenkinsfile
node('remote-agent') {
    stage('Build') {
        sh 'make build'
    }
}
```

### Check Firewall Rules

```bash
# Allow JNLP port
sudo ufw allow 50000/tcp
```

### Verify Agent Credentials

```groovy
// Check agent credentials in Jenkins UI
// Manage Jenkins > Manage Nodes > agent > Configure
```

## Examples

```text
Agent agent1 is offline
java.nio.channels.ClosedChannelException
```

## Related Errors

- [Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — build failure
- [Credential Error]({{< relref "/tools/jenkins/credential-error2" >}}) — credential issues
