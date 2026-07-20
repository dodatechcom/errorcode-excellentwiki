---
title: "[Solution] Jenkins Cloud Agent Provisioning Failed"
description: "Fix Jenkins cloud agent provisioning failures. Resolve Kubernetes, Docker, and EC2 agent provisioning issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Cloud Agent Provisioning Failed

Cloud agent provisioning fails when Jenkins cannot create dynamic agents.

## How to Fix

```bash
# Manage Jenkins > Manage Clouds > Select cloud > Verify connection
kubectl get pods
aws sts get-caller-identity
```
