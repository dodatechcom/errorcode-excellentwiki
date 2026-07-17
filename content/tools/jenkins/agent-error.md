---
title: "Error Connecting to Agent (Offline)"
description: "Jenkins cannot connect to a build agent because it is offline, unreachable, or the connection was refused."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error means the Jenkins controller cannot establish a connection to a configured build agent. Jobs assigned to that agent will remain pending until connectivity is restored.

## Common Causes

- The agent machine is powered off or not reachable over the network
- The Jenkins agent process (JNLP) is not running on the agent machine
- Firewall rules are blocking the required ports between controller and agent
- SSH credentials for the agent have changed or expired

## How to Fix

Check the agent status in **Manage Jenkins > Nodes** and ensure the agent is online. Restart the JNLP agent process on the agent machine:

```bash
java -jar agent.jar \
  -url https://jenkins.example.com \
  -secret @secret-file \
  -name my-agent \
  -workDir /var/jenkins
```

For SSH agents, verify connectivity manually:

```bash
ssh -i /path/to/key user@agent-host echo "connected"
```

Ensure the firewall allows traffic on the required ports (default is 50000 for JNLP):

```bash
sudo ufw allow 50000/tcp
```

## Examples

```
Agent my-agent is offline. Cannot schedule job 'my-project/build'.
hudson.remoting.Channel.call(): my-agent: agent is offline.
Waiting for reconnect...
```

## Related Errors

- [Build Failed]({{< relref "/tools/jenkins/build-failed" >}})
