---
title: "[Solution] GitLab CI Kubernetes Pod Scheduling"
description: "Fix GitLab CI Kubernetes pod scheduling failures when runner pods cannot be scheduled on cluster nodes."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Kubernetes Pod Scheduling

Pod scheduling failures occur when the Kubernetes executor cannot schedule runner pods due to resource constraints, taints, or node affinity mismatches.

## Common Causes

- Insufficient CPU or memory resources on cluster nodes
- Node taints without matching pod tolerations
- Persistent volume claims cannot be bound
- Image pull secret not available in the pod namespace
- Node selector labels do not match available nodes

## How to Fix

### Solution 1: Check cluster resource availability

```bash
kubectl describe nodes | grep -A 5 "Allocated resources"
kubectl top nodes
```

### Solution 2: Configure resource requests in runner

Adjust resource requests in `config.toml`:

```toml
[[runners]]
  [runners.kubernetes]
    cpu_request = "500m"
    memory_request = "1Gi"
    cpu_limit = "2"
    memory_limit = "4Gi"
```

### Solution 3: Add tolerations and node selectors

```toml
[[runners]]
  [runners.kubernetes]
    node_selector = {"runners" = "true"}
    [runners.kubernetes.pod_security_context]
```

## Examples

```
0/3 nodes are available: 3 Insufficient cpu
Failed to create pod: insufficient memory
```

## Prevent It

- Monitor cluster resource usage regularly
- Set appropriate resource requests and limits
- Use node pools dedicated to CI workloads
