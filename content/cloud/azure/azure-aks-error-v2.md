---
title: "[Solution] Azure AKS — node pool not ready"
description: "Fix Azure AKS node pool not ready. Resolve AKS node pool health and provisioning issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An AKS node pool not ready error means nodes in the specified node pool are not in a Ready state. Workloads cannot be scheduled onto these nodes, and existing pods may be disrupted.

## What This Error Means

AKS manages node pools as virtual machine scale sets. When a node pool is "not ready," it means the nodes in the pool are either not joining the Kubernetes cluster, failing health checks, or the AKS control plane cannot communicate with them. This affects pod scheduling, auto-scaling, and workload availability for any deployments targeting the node pool.

## Common Causes

- Node pool VM SKU is out of capacity in the target region
- AKS cluster is upgrading (control plane or node image)
- Node pool configuration error (wrong VNet subnet, NSG blocking traffic)
- kubelet or CNI plugin failure on the nodes
- Insufficient permissions for the node pool managed identity
- Node pool reached maximum node count during scaling

## How to Fix

### Check Node Pool Status

```bash
az aks nodepool list \
  --cluster-name my-cluster \
  --resource-group my-rg \
  --query '[].{name:name,state:state,provisioningState:provisioningState}'
```

### Check Node Health

```bash
az aks node list \
  --cluster-name my-cluster \
  --resource-group my-rg \
  --query '[].{name:name,provisioningState:provisioningState,nodeStatus:nodeStatus}'
```

### View Kubernetes Nodes

```bash
kubectl get nodes -o wide
kubectl describe node <node-name>
```

### Check Cluster Upgrade Status

```bash
az aks show --name my-cluster --resource-group my-rg \
  --query 'azureProfile.upgradeChannel'
```

### Update Node Image

```bash
az aks nodepool upgrade \
  --cluster-name my-cluster \
  --resource-group my-rg \
  --name mynodepool \
  --node-image-only
```

### Scale Node Pool

```bash
az aks nodepool scale \
  --cluster-name my-cluster \
  --resource-group my-rg \
  --name mynodepool \
  --node-count 3
```

### Check VNet Subnet

```bash
az aks show --name my-cluster --resource-group my-rg \
  --query 'agentPoolProfile[*].vnetSubnetId'
az network vnet subnet show \
  --vnet-name my-vnet \
  --name my-subnet \
  --resource-group my-rg
```

### Enable Uptime SLA

```bash
az aks update \
  --name my-cluster \
  --resource-group my-rg \
  --enable-uptime-sla
```

## Related Errors

- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — kubelet unhealthy
- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error-v2" >}}) — EKS health check failed
- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error-v2" >}}) — allocation failed
