---
title: "[Solution] Kubectl Exec Error — Fix stdin/stdout Copy"
description: "Fix kubectl exec error copying stdin/stdout. Resolve TTY allocation issues, container access problems, and streaming errors."
---

## What This Error Means

The `error copying stdin/stdout` error occurs when kubectl cannot establish a bidirectional stream to a container. This happens during `kubectl exec`, `kubectl attach`, or `kubectl port-forward` operations.

A typical error:

```
error: unable to upgrade connection: container not running (web-app)
```

Or:

```
Error: error copying stdin/stdout: Post http://localhost:8001/exec:
dial tcp 127.0.0.1:8001: connect: connection refused
```

## Why It Happens

stdin/stdout errors occur when:

- **Container is not running**: The target container has crashed or is not yet started.
- **Pod is in Pending state**: The pod has not been scheduled or started yet.
- **No TTY allocated**: The `-t` flag is used but the terminal cannot be allocated.
- **Network issues**: The API server cannot proxy the connection to the kubelet.
- **WebSocket upgrade failure**: The streaming connection upgrade from HTTP to WebSocket fails.
- **RBAC restrictions**: The user lacks permissions to exec into pods.

## How to Fix It

**Step 1: Verify the container is running**

```bash
kubectl get pods
kubectl describe pod web-app-7f8b6c5d4-abc
```

**Step 2: Use the correct container name for multi-container pods**

```bash
# List containers in a pod
kubectl get pod web-app-7f8b6c5d4-abc -o jsonpath='{.spec.containers[*].name}'

# Exec into specific container
kubectl exec -it web-app-7f8b6c5d4-abc -c sidecar -- /bin/sh
```

**Step 3: Allocate a TTY properly**

```bash
# With TTY allocation
kubectl exec -it web-app-7f8b6c5d4-abc -- /bin/sh

# Without TTY (for non-interactive commands)
kubectl exec -i web-app-7f8b6c5d4-abc -- cat /etc/hosts
```

**Step 4: Use debug containers for crashed pods**

```bash
# Kubernetes 1.23+ ephemeral containers
kubectl debug -it web-app-7f8b6c5d4-abc --image=busybox --target=web-app

# Or use a temporary pod
kubectl run debug --image=busybox --rm -it -- /bin/sh
```

**Step 5: Check kubelet connectivity**

```bash
# Verify the kubelet is running on the node
ssh node1 "systemctl status kubelet"
# Check kubelet logs
ssh node1 "journalctl -u kubelet -f"
```

## Common Mistakes

- **Not checking if the pod is running first**: Always verify pod status before attempting exec.
- **Forgetting `-t` for interactive sessions**: The `-t` flag allocates a TTY and is needed for interactive shells.
- **Not specifying container in multi-container pods**: Use `-c containername` when the pod has multiple containers.
- **Assuming exec works on InitContainers**: InitContainers complete before main containers start and may not be accessible.

## Related Pages

- [Kubectl Pod CrashLoopBackOff](/tools/kubectl/kubectl-pod-crashloopbackoff/) — Pod crash restart issues
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server connectivity
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Task execution errors
