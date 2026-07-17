---
title: "[Solution] Azure AKS Cluster Error"
description: "Fix Azure AKS cluster errors. Resolve Azure Kubernetes Service issues."
cloud: ["azure"]
error-types: ["api-error"]
severities: ["error"]
tags: ["azure", "aks", "kubernetes", "cluster", "node"]
weight: 5
---

An Azure AKS cluster error occurs when the AKS cluster or its components are not functioning properly. This affects container orchestration and application deployment.

## Common Causes

- Cluster is in a failed state
- Node pool not ready or scaling
- Service principal credentials expired
- Network plugin misconfigured
- Azure CNI or kubenet issues

## How to Fix

### Check Cluster Status

```bash
az aks show --name mycluster --resource-group myRG --query 'powerState'
```

### Get Credentials

```bash
az aks get-credentials --name mycluster --resource-group myRG
```

### Check Nodes

```bash
kubectl get nodes
kubectl describe node <node-name>
```

### Check Node Pool

```bash
az aks nodepool list --cluster-name mycluster --resource-group myRG
```

### Scale Node Pool

```bash
az aks nodepool scale --name mypool --cluster-name mycluster \
  --resource-group myRG --node-count 5
```

### Restart Cluster

```bash
az aks stop --name mycluster --resource-group myRG
az aks start --name mycluster --resource-group myRG
```

## Examples

```bash
# Example 1: Cluster not ready
# Current state of cluster: Stopped
# Fix: az aks start --name mycluster --resource-group myRG

# Example 2: Node not ready
# Node status: NotReady
# Fix: check kubelet and network plugin
```

## Related Errors

- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error" >}}) — EKS cluster error
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready" >}}) — node not ready
