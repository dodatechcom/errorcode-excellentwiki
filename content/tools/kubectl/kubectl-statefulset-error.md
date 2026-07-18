---
title: "[Solution] Kubectl StatefulSet Update Stuck — How to Fix"
description: "Fix stuck StatefulSet updates by checking pod status, PersistentVolumeClaim issues, rolling update parameters, pod management policies, and storage availability for stateful workloads."
tools: ["kubectl"]
error-types: ["statefulset-error"]
severities: ["error"]
weight: 5
comments: true
---

A StatefulSet update gets stuck when the rolling update cannot proceed because pods fail to start, PersistentVolumeClaims cannot be bound, or the update strategy prevents progress. StatefulSets manage stateful applications with ordered, graceful deployment and scaling.

## What This Error Means

StatefulSets provide guarantees about the ordering and uniqueness of pods. Unlike Deployments, StatefulSet pods are created in order (from index 0 to N-1), deleted in reverse order, and each pod gets a unique identity and persistent storage. A stuck update means the StatefulSet controller cannot proceed to the next pod because the current pod is not healthy.

The update can get stuck at any pod index. The controller waits for the pod to become Ready before updating the next one (for `RollingUpdate` strategy) or for all pods to be deleted (for `OnDelete` strategy).

## Why It Happens

- A pod fails to start after update (CrashLoopBackOff, ImagePullBackOff)
- The PersistentVolumeClaim (PVC) is stuck in Pending state
- The PersistentVolume cannot be provisioned (StorageClass not found, quota exceeded)
- The `podManagementPolicy` is `OrderedReady` and the previous pod is not Ready
- The `partition` parameter prevents updates for pods below the partition index
- The `maxUnavailable` setting blocks the update from proceeding
- The StatefulSet has a `serviceName` that does not match an existing Headless Service
- The pod's readiness probe is failing, preventing the controller from marking it Ready

## Common Error Messages

```
statefulset "my-statefulset" is waiting for pod "my-statefulset-0" to become ready
# or
persistentvolumeclaim "data-my-statefulset-0" is stuck in Pending state
# or
Error: StatefulSet update is stuck because pod "my-statefulset-1" failed readiness check
# or
waiting for statefulset "my-statefulset" to finish rolling update (0/3 pods updated)
```

## How to Fix It

### 1. Check StatefulSet Status

```bash
# View StatefulSet status
kubectl get statefulset my-statefulset

# Detailed status including current revision and update revision
kubectl describe statefulset my-statefulset

# Check pod status
kubectl get pods -l app=my-statefulset

# Check which pods have been updated
kubectl rollout status statefulset my-statefulset
```

### 2. Check PersistentVolumeClaims

```bash
# List PVCs for the StatefulSet
kubectl get pvc -l app=my-statefulset

# Check if PVCs are bound
kubectl describe pvc data-my-statefulset-0

# If PVC is Pending, check StorageClass:
kubectl get storageclass

# If the PVC cannot be bound, check events:
kubectl get events | grep -i persistentvolume

# Create a PV manually if needed (for static provisioning)
```

### 3. Fix Rolling Update Configuration

```bash
# Check update strategy
kubectl get statefulset my-statefulset -o yaml | grep -A 5 "updateStrategy"

# Set the update strategy to OnDelete for manual control:
kubectl patch statefulset my-statefulset -p '{
  "spec": {
    "updateStrategy": {
      "type": "OnDelete"
    }
  }
}'

# Then delete pods manually to force recreation:
kubectl delete pod my-statefulset-0
```

### 4. Use Partitioned Rolling Update

```bash
# Set a partition to update only specific pods
# Pods with index >= partition are updated
# Pods with index < partition remain at the old version

kubectl patch statefulset my-statefulset -p '{
  "spec": {
    "updateStrategy": {
      "type": "RollingUpdate",
      "rollingUpdate": {
        "partition": 2
      }
    }
  }
}'

# To resume full rollout, set partition to 0:
kubectl patch statefulset my-statefulset -p '{
  "spec": {
    "updateStrategy": {
      "type": "RollingUpdate",
      "rollingUpdate": {
        "partition": 0
      }
    }
  }
}'
```

### 5. Check Pod Management Policy

```bash
# podManagementPolicy: OrderedReady (default)
# This requires pods to be created in order 0, 1, 2, ...
# If pod-0 is not Ready, pod-1 cannot be created

# For parallel pod management (faster but riskier):
kubectl patch statefulset my-statefulset -p '{
  "spec": {
    "podManagementPolicy": "Parallel"
  }
}'
```

### 6. Debug Individual Pod Failures

```bash
# Check logs for the failing pod
kubectl logs my-statefulset-0

# Describe the failed pod
kubectl describe pod my-statefulset-0

# Check if the pod's readiness probe is failing
kubectl get pod my-statefulset-0 -o jsonpath='{.status.conditions[?(@.type=="Ready")]}'

# Restart a specific pod
kubectl delete pod my-statefulset-0 --wait=false
```

### 7. Force Rollback to Previous Revision

```bash
# List rollout history
kubectl rollout history statefulset my-statefulset

# Rollback to a specific revision
kubectl rollout undo statefulset my-statefulset --to-revision=2

# Rollback to the previous revision
kubectl rollout undo statefulset my-statefulset
```

### 8. Verify Headless Service

```bash
# StatefulSets require a Headless Service with the matching serviceName
kubectl get service my-statefulset

# Check if the service is headless (clusterIP: None)
kubectl get service my-statefulset -o yaml | grep "clusterIP: None"

# If missing, create the Headless Service:
apiVersion: v1
kind: Service
metadata:
  name: my-statefulset
spec:
  clusterIP: None
  selector:
    app: my-statefulset
  ports:
  - port: 8080
    name: http
```

## Common Scenarios

### PVC Cannot Be Provisioned

A StatefulSet references a StorageClass that requires a specific cloud provisioner (e.g., `ebs-sc` on AWS), but the cluster does not have the CSI driver installed. PVCs remain Pending, and the StatefulSet update is stuck. Install the appropriate CSI driver or change to a supported StorageClass.

### OrderedReady Policy Blocks Update After Pod-0 Fails

Pod-0 crashes after update, and the StatefulSet controller cannot proceed to update pod-1, pod-2, etc. Fix the issue causing pod-0 to crash (e.g., missing config, wrong image), and the rollout resumes automatically.

### Partition Parameter Prevents Full Rollout

A developer sets `partition: 3` during a canary deployment to test the update on one pod. After testing, they forget to set `partition: 0`, leaving the remaining pods at the old version. Set the partition to 0 to complete the rollout.

## Prevent It

- Use canary deployments with `partition` parameter to test updates on a single pod first
- Ensure StorageClass and provisioner are properly configured before StatefulSet creation
- Use `podManagementPolicy: Parallel` for applications that do not require ordered readiness
- Set `maxUnavailable` to 1 or higher to allow faster rolling updates
- Implement robust readiness probes that accurately reflect application health
- Test StatefulSet updates in a staging environment before production
- Monitor PVC binding status and set up alerts for Pending PVCs
- Use `rollout history` to track revisions and enable easy rollbacks

## Related Pages

- [Kubectl DaemonSet Scheduling Error](/tools/kubectl/kubectl-daemonset-error)
- [Kubectl CrashLoopBackOff Error](/tools/kubectl/kubectl-crash-loop-error)
- [Kubectl Service Endpoint Not Found](/tools/kubectl/kubectl-service-error)
