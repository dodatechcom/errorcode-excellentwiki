---
title: "[Solution] Kubectl Pod Stuck Terminating - Fix Pod Stuck in Terminating State"
description: "Fix Kubernetes pod stuck in Terminating state. Resolve finalizers, node failures, and force deletion to clear stuck pods."
tools: ["kubectl"]
error-types: ["stuck-terminating"]
severities: ["warning"]
weight: 5
---

This error means a Kubernetes pod is stuck in the `Terminating` state and will not be removed. The pod's termination process is blocked by finalizers, node unavailability, or unresponsive containers.

## What This Error Means

When you run `kubectl delete pod` and the pod remains in Terminating state, you see:

```
NAME        READY   STATUS        RESTARTS   AGE
my-pod      0/1     Terminating   0          5m
```

After the grace period expires, the pod may still remain if the kubelet on the node cannot complete termination or if a finalizer is preventing deletion.

## Why It Happens

- A finalizer on the pod is waiting for an external action that never completes
- The node hosting the pod is down or unreachable
- The container is ignoring SIGTERM signals and the grace period has not expired
- A PersistentVolumeClaim is bound and cannot be released
- The API server cannot communicate with the kubelet on the node
- A webhook or admission controller is blocking the deletion

## How to Fix It

### Check for finalizers

```bash
kubectl get pod my-pod -o json | jq .metadata.finalizers
```

If finalizers exist, they must complete before the pod can be deleted.

### Remove finalizers

```bash
kubectl patch pod my-pod -p '{"metadata":{"finalizers":null}}'
```

This clears all finalizers and allows immediate deletion.

### Force delete the pod

```bash
kubectl delete pod my-pod --grace-period=0 --force
```

Use `--force` with `--grace-period=0` as a last resort to immediately remove the pod.

### Check node status

```bash
kubectl get nodes
kubectl describe node <node-name>
```

If the node is NotReady, the kubelet cannot process pod termination.

### Delete pods on an unreachable node

```bash
kubectl delete pod my-pod --force --grace-period=0 --namespace=default
```

Or use node eviction:

```bash
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data --force
```

### Check for stuck containers

```bash
kubectl describe pod my-pod
```

Look at the Events section for termination-related messages.

### Restart the kubelet on the node

```bash
ssh <node>
sudo systemctl restart kubelet
```

A restarted kubelet can clear stuck pod states.

## Common Mistakes

- Waiting too long before force deleting stuck pods
- Not checking for finalizers before assuming the node is the problem
- Force deleting pods without understanding that PVCs or other resources may be affected
- Forgetting that StatefulSets will recreate terminated pods automatically
- Not addressing the root cause (node failure, bad finalizer) after force deletion

## Related Pages

- [Kubectl Pod Pending]({{< relref "/tools/kubectl/kubectl-pod-pending" >}}) -- pod scheduling issues
- [Kubectl Node Not Ready]({{< relref "/tools/kubectl/kubectl-node-not-ready" >}}) -- node health problems
- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- API server connectivity
