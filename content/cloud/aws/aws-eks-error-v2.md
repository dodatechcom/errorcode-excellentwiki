---
title: "[Solution] AWS EKS — cluster health check failed"
description: "Fix AWS EKS cluster health check failed. Resolve EKS control plane and node health issues."
cloud: ["aws"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["aws", "eks", "cluster", "health", "check", "failed", "control-plane"]
weight: 5
---

An EKS cluster health check failed means the EKS control plane or managed node group is unhealthy. The cluster may not respond to API requests, and workloads may be affected.

## What This Error Means

EKS clusters have health checks at two levels: the managed control plane (API server, etcd) and the managed node groups. A failed health check indicates the control plane is degraded, nodes are not joining the cluster, or the cluster is unable to schedule pods. EKS reports this through the AWS console, CloudWatch, and the Kubernetes API. Node group health checks validate that nodes are registered, ready, and passing health probes.

## Common Causes

- EKS control plane is experiencing an AWS-side issue
- Managed node group launching instances that fail to join the cluster
- Node IAM role missing required EKS policies
- Cluster version is out of support or incompatible with node version
- VPC networking misconfigured (subnet CIDR too small, missing NAT gateway)
- Add-on version incompatibility (VPC CNI, CoreDNS, kube-proxy)

## How to Fix

### Check Cluster Status

```bash
aws eks describe-cluster --name my-cluster \
  --query 'cluster.[status,version,platformVersion]'
```

### Check Node Group Health

```bash
aws eks describe-nodegroup \
  --cluster-name my-cluster \
  --nodegroup-name my-nodes \
  --query 'nodegroup.[status,health]'
```

### Check Cluster Health Events

```bash
aws eks describe-cluster --name my-cluster \
  --query 'cluster.health'
```

### Update Cluster Version

```bash
aws eks update-cluster-version \
  --name my-cluster \
  --kubernetes-version 1.29
```

### Verify Node IAM Role

```bash
aws iam list-attached-role-policies --role-name my-node-role
```

### Add Required EKS Policies

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "PolicyArns": [
      "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
      "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
      "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
    ],
    "Action": "sts:AssumeRole"
  }]
}
```

### Check Node Connectivity

```bash
kubectl get nodes
kubectl describe node <node-name>
```

### Update Add-ons

```bash
aws eks update-addon \
  --cluster-name my-cluster \
  --addon-name vpc-cni \
  --resolve-conflicts OVERWRITE
```

## Related Errors

- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
- [Kubernetes API Server Error]({{< relref "/tools/kubernetes/k8s-api-server-error-v2" >}}) — API server timeout
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error-v2" >}}) — instance limit exceeded
