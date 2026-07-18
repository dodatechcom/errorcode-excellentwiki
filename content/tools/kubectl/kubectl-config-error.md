---
title: "[Solution] Kubectl Config Error - Fix current-context Is Not Set"
description: "Fix kubectl error when current-context is not set. Configure kubeconfig contexts, merge configs, and switch between clusters."
tools: ["kubectl"]
error-types: ["config-error"]
severities: ["error"]
weight: 5
---

This error means kubectl cannot determine which cluster to connect to because no current context is set in your kubeconfig file.

## What This Error Means

When kubectl has no active context, it cannot send commands to any cluster:

```
error: current-context is not set
# or
error: no configuration has been provided, try setting KUBECONFIG
# or
The connection to the server <server> was refused
```

kubectl relies on the kubeconfig file to know which cluster, user, and namespace to use. Without a context, it has no connection information.

## Why It Happens

- `~/.kube/config` does not exist or is empty
- The `current-context` field was removed or was never set
- You have multiple kubeconfig files and the correct one is not loaded
- The KUBECONFIG environment variable is not set
- A tool modified the kubeconfig and removed the context
- You are in a fresh shell session without the expected kubeconfig

## How to Fix It

### Check current kubeconfig

```bash
kubectl config view
kubectl config current-context
```

This shows what contexts exist and which is active.

### Set the current context

```bash
kubectl config use-context my-cluster
```

This switches to the named context in your default kubeconfig.

### Merge multiple kubeconfig files

```bash
export KUBECONFIG=~/.kube/config:~/.kube/other-config
kubectl config view --merge --flatten > merged-config.yaml
```

This combines multiple kubeconfig files into one.

### Create a kubeconfig from scratch

```bash
kubectl config set-cluster my-cluster --server=https://k8s.example.com:6443
kubectl config set-credentials my-user --token=my-token
kubectl config set-context my-context --cluster=my-cluster --user=my-user
kubectl config use-context my-context
```

### Use a specific kubeconfig file

```bash
kubectl --kubeconfig=/path/to/kubeconfig get pods
```

### Set KUBECONFIG in your shell profile

```bash
echo 'export KUBECONFIG=~/.kube/config' >> ~/.bashrc
source ~/.bashrc
```

### Copy kubeconfig from a running cluster

```bash
aws eks update-kubeconfig --name my-cluster --region us-east-1
```

Cloud provider CLIs can generate kubeconfig automatically.

## Common Mistakes

- Not backing up kubeconfig before making changes
- Assuming kubectl always reads from `~/.kube/config`
- Having multiple kubeconfig files without using KUBECONFIG to merge them
- Forgetting that `kubectl config use-context` changes the context permanently
- Not verifying the kubeconfig is valid after editing it manually

## Related Pages

- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- API server connectivity
- [Kubectl Permission Error]({{< relref "/tools/kubectl/kubectl-permission-error" >}}) -- RBAC issues
- [Kubectl Exec Error]({{< relref "/tools/kubectl/kubectl-exec-error" >}}) -- exec failures
