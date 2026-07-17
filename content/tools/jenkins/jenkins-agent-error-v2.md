---
title: "Jenkins Agent Connection Lost"
description: "Jenkins agent node loses connection to the controller."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Agent — Connection Lost

This error occurs when a Jenkins agent (node) loses its connection to the controller. Jobs assigned to the agent fail or remain pending until the connection is restored.

## Common Causes

- Agent machine crashed or restarted
- Network connectivity issues
- Agent JVM ran out of memory
- SSH tunnel or JNLP connection dropped
- Firewall blocking agent traffic

## How to Fix

### Check Agent Status

Go to **Manage Jenkins > Nodes** and check the agent status.

### Restart Agent Service

```bash
# On the agent machine
sudo systemctl restart jenkins-agent
```

### Reconnect JNLP Agent

```bash
# On the agent machine
java -jar agent.jar \
  -url http://jenkins-server:8080 \
  -secret @secret-file \
  -name my-agent \
  -workDir /var/jenkins
```

### Verify SSH Agent Configuration

```groovy
// In Jenkins pipeline
node('my-remote-agent') {
    sh 'hostname'
}
```

### Configure Agent Retry

```groovy
// CasC agent configuration
jenkins:
  nodes:
    - remoteFS: /var/jenkins
      numExecutors: 4
      name: my-agent
      launcher:
        ssh:
          host: agent.example.com
          credentialsId: agent-ssh-key
          sshHostKeyVerificationStrategy: nonVerifyingKeyVerificationStrategy
```

### Increase Agent Heartbeat

```bash
# On agent machine, check JNLP connectivity
curl -v http://jenkins-server:8080/computer/my-agent/
```

## Examples

```text
Agent my-agent went offline during build.
Building remotely on my-agent in workspace /var/jenkins/workspace
Agent went offline during the build
```

## Related Errors

- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Pipeline Error]({{< relref "/tools/jenkins/jenkins-pipeline-error" >}}) — pipeline syntax error
- [Jenkins Master Error]({{< relref "/tools/jenkins/jenkins-master-error" >}}) — controller issues
