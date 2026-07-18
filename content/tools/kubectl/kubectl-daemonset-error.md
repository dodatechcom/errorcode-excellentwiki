---
title: "[Solution] Kubectl DaemonSet Scheduling Error — How to Fix"
description: "Fix kubectl DaemonSet scheduling errors by checking node selectors, taints and tolerations, resource constraints, pod priority, and node availability for DaemonSet pods."
tools: ["kubectl"]
error-types: ["daemonset-error"]
severities: ["error"]
weight: 5
comments: true
---

A DaemonSet scheduling error occurs when a DaemonSet pod cannot be scheduled on a node. DaemonSets ensure that a copy of a pod runs on all (or a subset of) nodes. Scheduling failures prevent the DaemonSet from running on target nodes.

## What This Error Means

DaemonSets are designed to run exactly one pod per node (or a subset specified by node selectors). The Kubernetes scheduler places DaemonSet pods on nodes as they join the cluster. Scheduling errors occur when no available node matches the DaemonSet's scheduling constraints, or when the node lacks sufficient resources.

Unlike deployments, DaemonSets bypass the normal scheduler for initial placement. The DaemonSet controller directly assigns pods to nodes based on node selectors, taints/tolerations, and resource availability. If the node selector does not match any nodes, or if all matching nodes are full, the DaemonSet pods remain in a Pending state.

## Why It Happens

- The DaemonSet's node selector does not match any nodes in the cluster
- All matching nodes have taints that the DaemonSet pod does not tolerate
- The nodes do not have sufficient CPU, memory, or other resources for the DaemonSet pod
- The DaemonSet has an incorrect or overly restrictive `nodeSelector` or `affinity`
- The node is cordoned (unschedulable) or in a NotReady state
- The DaemonSet pod has a higher priority than expected and is preempting other pods
- The DaemonSet is configured to run on a specific number of nodes but not enough exist
- The `maxUnavailable` setting is preventing rolling updates from progressing

## Common Error Messages

```
0/3 nodes are available: 3 node(s) didn't match Pod's node affinity
# or
0/3 nodes are available: 3 node(s) had taint {node-role.kubernetes.io/master: }, that the pod didn't tolerate
# or
0/3 nodes are available: 3 Insufficient cpu
# or
DaemonSet "my-daemonset" is not scheduled on 2 node(s)
```

## How to Fix It

### 1. Check DaemonSet Status

```bash
# View DaemonSet status
kubectl get daemonset my-daemonset

# Detailed status
kubectl describe daemonset my-daemonset

# Check which nodes have the DaemonSet pod
kubectl get pods -l app=my-daemonset -o wide

# Show nodes that are missing the DaemonSet
kubectl describe daemonset my-daemonset | grep "Nodes"
```

### 2. Check Node Selectors

```bash
# Check the DaemonSet's node selector
kubectl get daemonset my-daemonset -o yaml | grep -A 10 "nodeSelector\|affinity"

# Check node labels
kubectl get nodes --show-labels

# If no node matches the selector, update the DaemonSet
kubectl edit daemonset my-daemonset
# Remove or update the nodeSelector to match existing nodes
```

### 3. Fix Taints and Tolerations

```bash
# Check node taints
kubectl describe nodes | grep -A 5 Taints

# Common taints:
# node-role.kubernetes.io/master:NoSchedule
# node.kubernetes.io/unreachable:NoSchedule

# Add tolerations to the DaemonSet
kubectl patch daemonset my-daemonset -p '{
  "spec": {
    "template": {
      "spec": {
        "tolerations": [
          {
            "key": "node-role.kubernetes.io/master",
            "operator": "Exists",
            "effect": "NoSchedule"
          }
        ]
      }
    }
  }
}'
```

### 4. Check Resource Requirements

```bash
# Check DaemonSet resource requests
kubectl get daemonset my-daemonset -o yaml | grep -A 10 "resources"

# Check node available resources
kubectl describe nodes | grep -A 5 "Allocated resources"

# If resources are insufficient, reduce requests or increase node capacity

# Reduce resource requests:
kubectl set resources daemonset my-daemonset \
    --requests=cpu=100m,memory=128Mi \
    --limits=cpu=500m,memory=512Mi
```

### 5. Check Node Conditions

```bash
# Check node status
kubectl get nodes

# Check for cordoned nodes
kubectl get nodes | grep SchedulingDisabled

# If nodes are cordoned, uncordon them:
kubectl uncordon <node-name>

# Check for NotReady nodes
kubectl get nodes | grep NotReady
# Fix the node's kubelet or wait for it to recover
```

### 6. Use Rolling Update Parameters

```yaml
# DaemonSets have rolling update parameters that can block scheduling
apiVersion: apps/v1
kind: DaemonSet
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1  # How many pods can be unavailable during update
      maxSurge: 0        # How many extra pods can be created (DaemonSets typically 0)
```

### 7. Debug with Ephemeral Container

```bash
# Check scheduler events for the DaemonSet pod
kubectl describe pod my-daemonset-xxxxx | grep -A 10 Events

# Test if a pod can be scheduled on a specific node
kubectl run test-scheduling --image=busybox --rm -it --restart=Never \
    --overrides='{"apiVersion":"v1","spec":{"nodeSelector":{"kubernetes.io/hostname":"worker-1"}}}' \
    -- /bin/sh
```

### 8. Use PodAntiAffinity for DaemonSets

```yaml
# Ensure DaemonSet pods are spread across different nodes
apiVersion: apps/v1
kind: DaemonSet
spec:
  template:
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - my-daemonset
            topologyKey: kubernetes.io/hostname
```

## Common Scenarios

### DaemonSet with Specific Node Label That Does Not Exist

A DaemonSet for log collection is configured with `nodeSelector: {tier: logging}` but no nodes have the `tier=logging` label. The DaemonSet pods remain pending. Add the label to target nodes: `kubectl label nodes worker-1 tier=logging`.

### Master Node Taints Blocking DaemonSet

A monitoring DaemonSet needs to run on all nodes including the control plane. The master node has a `node-role.kubernetes.io/master:NoSchedule` taint. Add the corresponding toleration to the DaemonSet to allow scheduling on master nodes.

### Insufficient Resources on Small Nodes

A resource-intensive DaemonSet (e.g., a security scanner requesting 1GB memory) cannot fit on small worker nodes with only 512MB available. Reduce resource requests or add larger nodes to the cluster.

## Prevent It

- Test DaemonSet scheduling in a staging cluster before production
- Use `nodeSelector` with labels that are consistently applied to all target nodes
- Add tolerations for common node taints (master, GPU, etc.) proactively
- Set conservative resource requests to fit on the smallest node in the cluster
- Use `priorityClassName` to ensure DaemonSet pods are not preempted
- Monitor DaemonSet scheduling status with `kubectl describe daemonset`
- Use `minReadySeconds` to ensure DaemonSet pods are healthy before considering them ready
- Configure `maxUnavailable` to control the pace of DaemonSet rolling updates

## Related Pages

- [Kubectl StatefulSet Update Stuck](/tools/kubectl/kubectl-statefulset-error)
- [Kubectl Service Endpoint Not Found](/tools/kubectl/kubectl-service-error)
- [Kubectl Image Pull Backoff Error](/tools/kubectl/kubectl-image-pull-error)
