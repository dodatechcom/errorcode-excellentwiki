---
title: "[Solution] Kubectl Cannot Retrieve Pod Logs — How to Fix"
description: "Fix kubectl logs errors by checking pod status, verifying container names, using previous logs for crashed pods, accessing node-level container logs, and debugging log rotation issues."
tools: ["kubectl"]
error-types: ["logs-error"]
severities: ["error"]
weight: 5
comments: true
---

A kubectl logs error occurs when you cannot retrieve container logs from a pod. This can happen because the pod is not running, the container has crashed, the log request is malformed, or the kubelet is experiencing issues.

## What This Error Means

`kubectl logs` retrieves logs from a specific container in a pod. It reads the container's stdout and stderr streams, which are captured by the container runtime (containerd, Docker, CRI-O) and exposed through the kubelet API. When the pod is not running, or the container runtime is misconfigured, the log retrieval fails.

The error can also occur when the pod has multiple containers and you do not specify which one, or when the log file has been rotated or deleted before the request completes.

## Why It Happens

- The pod is in a Pending, CrashLoopBackOff, or ImagePullBackOff state and has no logs yet
- The pod has multiple containers and you did not specify which container to fetch logs from
- The container has restarted and the previous container's logs are requested without the `--previous` flag
- The kubelet or container runtime is not functioning correctly on the node
- The log file has been rotated and the kubelet cannot access the rotated file
- The pod has been evicted or deleted, removing its log files
- The log request exceeds the maximum log size limit
- RBAC permissions prevent you from accessing pod logs

## Common Error Messages

```
error: container "app" is in pod "my-pod" but it is not running
# or
error: a container name must be specified for pod my-pod, choose one of: [app sidecar]
# or
error: previous terminated container "app" in pod "my-pod" not found
# or
error: unable to retrieve container logs: log file is too large
```

## How to Fix It

### 1. Check Pod Status

```bash
# Check if the pod is running
kubectl get pod my-pod

# If the pod is Pending, wait for it to start
# If CrashLoopBackOff, fix the crash first, then check logs

# Describe the pod for details
kubectl describe pod my-pod
```

### 2. Specify Container Name for Multi-Container Pods

```bash
# List containers in the pod
kubectl get pod my-pod -o jsonpath='{.spec.containers[*].name}'
# Returns: app sidecar

# Fetch logs from a specific container
kubectl logs my-pod -c app

# Fetch logs from all containers
kubectl logs my-pod --all-containers
```

### 3. Get Logs from Crashed/Previous Containers

```bash
# Get logs from the previous (crashed) instance
kubectl logs my-pod --previous

# Get logs from a specific previous container
kubectl logs my-pod -c app --previous

# Follow logs from the previous instance
kubectl logs my-pod --previous -f
```

### 4. Stream Logs with Tail and Since

```bash
# Get the last 100 lines
kubectl logs my-pod --tail=100

# Get logs from the last hour
kubectl logs my-pod --since=1h

# Get logs since a specific time
kubectl logs my-pod --since-time="2025-07-18T10:00:00Z"

# Follow logs in real-time
kubectl logs my-pod -f
```

### 5. Access Logs at the Node Level

```bash
# When kubectl logs fails, access logs directly on the node
# SSH into the node:
ssh admin@worker-node-1

# For containerd runtime:
crictl logs <container-id>

# For Docker runtime:
docker logs <container-id>

# Node-level log files (usually):
# /var/log/pods/<namespace>_<pod-name>_<pod-uid>/<container-name>/
ls /var/log/pods/
```

### 6. Check Kubelet Logs

```bash
# If the kubelet is having issues, check its logs:
# On the node:
sudo journalctl -u kubelet -n 100 --no-pager

# Look for errors related to log retrieval
sudo journalctl -u kubelet | grep -i log
```

### 7. Fix RBAC Permissions

```bash
# Check if you have permission to get pod logs
kubectl auth can-i get pods/log

# If not, create a role with pod/log access:
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-log-reader
rules:
- apiGroups: [""]
  resources: ["pods/log"]
  verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  namespace: default
  name: pod-log-reader-binding
subjects:
- kind: User
  name: your-username
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-log-reader
  apiGroup: rbac.authorization.k8s.io
```

### 8. Handle Large Log Files

```bash
# If log files are too large, limit the output:
kubectl logs my-pod --tail=50

# Or use a logging sidecar with log rotation:
# Configure log rotation in the application:
# - Use a logging library that supports rotation
# - Limit log verbosity in production
# - Use a sidecar container for log management

# Example: sidecar that rotates logs
# - name: log-rotator
#   image: busybox
#   command:
#   - /bin/sh
#   - -c
#   - |
#     while true; do
#       logrotate /etc/logrotate.conf
#       sleep 3600
#     done
```

### 9. Use Stern or Kail for Multi-Pod Logs

```bash
# Install stern for multi-pod log tailing
# stern allows filtering by pod name pattern
stern my-app --tail=10

# Install kail for streaming logs from multiple pods
kail --deployment=my-app

# Both tools handle pod restarts gracefully and follow new pods
```

## Common Scenarios

### Pod in CrashLoopBackOff with No Logs

A pod crashes immediately at startup. `kubectl logs my-pod` returns "container is not running" because the container exits before the logs can be captured. Use `kubectl logs my-pod --previous` to see the logs from the terminated container instance.

### Multi-Container Pod Without Container Flag

A pod has both an `app` container and a `sidecar` container. Running `kubectl logs my-pod` fails with "a container name must be specified." Specify the container with `-c app` or use `--all-containers`.

### Log File Too Large Causes Timeout

A container that has been running for months produces a log file that is gigabytes in size. `kubectl logs my-pod` times out or returns an error about the log file being too large. Use `kubectl logs my-pod --tail=100` to read the last 100 lines, or implement log rotation in the application.

## Prevent It

- Use `--tail` and `--since` flags to limit log output for long-running containers
- Implement log rotation at the application level or use a sidecar container
- Use a centralized logging solution (Elasticsearch, Loki, CloudWatch) for long-term log storage
- Set resource limits on log file sizes through the container runtime configuration
- Use `kubectl logs --previous` in debugging scripts when expecting crashes
- Add logging sidecars for pods that need log management
- Set up RBAC for pod/log access to match your team's access requirements
- Use structured logging (JSON format) for easier log aggregation

## Related Pages

- [Kubectl CrashLoopBackOff Error](/tools/kubectl/kubectl-crash-loop-error)
- [Kubectl Image Pull Backoff Error](/tools/kubectl/kubectl-image-pull-error)
- [Kubectl Context Not Found](/tools/kubectl/kubectl-context-error)
