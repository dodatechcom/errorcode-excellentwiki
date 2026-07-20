---
title: "[Solution] Unable to connect to the server"
description: "Fix kubectl 'Unable to connect to the server' error. Resolve connection failures between kubectl and the Kubernetes API server."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Unable to Connect to the Server

`Unable to connect to the server: dial tcp <ip>:<port>: connect: connection refused`

This error occurs when kubectl cannot connect to the Kubernetes API server. The connection may be blocked, the server may be down, or the kubeconfig may be misconfigured.

### Common Causes

- API server is not running or has crashed
- kubectl is pointing to the wrong cluster or port
- Network connectivity issues (firewall, VPN)
- TLS certificate errors
- Cluster endpoint changed

### How to Fix

Check your current context:
```bash
kubectl config current-context
kubectl config view
```

Ping the API server:
```bash
curl -k https://<server>:<port>/healthz
```

### Examples

```bash
# Check connectivity
curl -k https://your-cluster:6443/healthz
# {"ok"}

# View current kubeconfig
kubectl config view --minify
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})