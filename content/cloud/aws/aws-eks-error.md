---
title: "[Solution] AWS EKS Cluster Error"
description: "Fix AWS EKS cluster errors. Resolve EKS cluster and node group issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "eks", "kubernetes", "cluster", "node"]
weight: 5
---

An AWS EKS cluster error occurs when the EKS cluster or its components are not functioning properly. This can affect pod scheduling and cluster management.

## Common Causes

- Cluster is not in ACTIVE state
- Node group is degraded or unhealthy
- OIDC provider not configured for IRSA
- Add-ons not compatible with cluster version
- IAM permissions for cluster access missing

## How to Fix

### Check Cluster Status

```bash
aws eks describe-cluster --name my-cluster \
  --query 'cluster.status'
```

### Check Node Group Status

```bash
aws eks list-nodegroups --cluster-name my-cluster
aws eks describe-nodegroup \
  --cluster-name my-cluster \
  --nodegroup-name my-nodes
```

### Update Cluster

```bash
aws eks update-cluster-version \
  --name my-cluster \
  --version 1.28
```

### Configure kubectl

```bash
aws eks update-kubeconfig --name my-cluster --region us-east-1
```

### Check Add-ons

```bash
aws eks list-addons --cluster-name my-cluster
aws eks describe-addon \
  --cluster-name my-cluster \
  --addon-name vpc-cni
```

## Examples

```bash
# Example 1: Cluster not active
# Cluster is not in ACTIVE state
# Fix: wait for cluster creation or check CloudFormation events

# Example 2: Node group degraded
# Node group status: DEGRADED
# Fix: check CloudFormation events for node group stack
```

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) — ECS task failed
- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready" >}}) — node not ready
