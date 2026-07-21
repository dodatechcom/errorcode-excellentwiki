---
title: "[Solution] Azure AKS Node Not Ready Error"
description: "Fix Azure Kubernetes Service nodes stuck in NotReady state preventing pod scheduling."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Nodes in NotReady state cannot schedule new pods and existing pods may be evicted. This reduces cluster capacity and can cause service disruptions.

## Common Causes

- Node has run out of disk space or memory
- kubelet on the node has stopped communicating with the API server
- Node pool upgrade is in progress and node is rebooting
- Virtual network misconfiguration prevents node from reaching the control plane

## How to Fix

### Check node status

```bash
kubectl get nodes -o wide
```

### Describe the problematic node

```bash
kubectl describe node <node-name>
```

### Restart the node by cordoning and draining

```bash
kubectl cordon <node-name>
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
```

### Check AKS node pool health

```bash
az aks show \
  --name myAKSCluster \
  --resource-group myRG \
  --query "agentPoolProfiles[].{Name:name,Count:count,State:provisioningState}"
```

## Examples

- Node shows NotReady after a kernel panic and kubelet service crashed
- All nodes in the pool become NotReady during an AKS version upgrade
- Node is NotReady because the subnet it runs in has no available IP addresses

## Related Errors

- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error" >}}) -- General AKS errors.
- [Azure AKS Node Pool]({{< relref "/cloud/azure/azure-aks-node-pool" >}}) -- Node pool issues.
