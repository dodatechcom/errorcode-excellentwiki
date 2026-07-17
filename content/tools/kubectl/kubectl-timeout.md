---
title: "[Solution] Kubectl Timeout — Fix Request Timeout for Pods"
description: "Fix kubectl request timeout errors. Resolve API server overload, large resource queries, and connection timeouts with practical fixes."
---

## What This Error Means

The `request timeout` error means kubectl did not receive a response from the API server within the configured time limit. This typically happens when the API server is overloaded or when querying a very large number of resources.

A typical error:

```
Unable to connect to the server: request timed out
```

Or:

```
context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

## Why It Happens

Timeout errors occur when:

- **API server overloaded**: Too many concurrent requests overwhelming the control plane.
- **Large resource queries**: Listing thousands of pods, events, or other resources.
- **Network latency**: Slow network connections between kubectl and the API server.
- **etcd performance**: The backing etcd store is slow or overloaded.
- **Webhook timeouts**: Admission webhooks taking too long to respond.
- **Client timeout too low**: Default kubectl timeout is too short for slow operations.

## How to Fix It

**Step 1: Increase the request timeout**

```bash
kubectl get pods --request-timeout=300s
```

Or set in kubeconfig:

```yaml
apiVersion: v1
kind: Config
clusters:
  - cluster:
      server: https://api.example.com:6443
      timeout: 300s
```

**Step 2: Filter queries to reduce load**

```bash
# Instead of listing all pods in all namespaces
kubectl get pods --all-namespaces

# Use labels to filter
kubectl get pods -l app=web --namespace production

# Limit output
kubectl get pods --namespace default --limit=50
```

**Step 3: Use server-side apply for large updates**

```bash
kubectl apply -f manifest.yaml --server-side
```

**Step 4: Check API server health**

```bash
kubectl get --raw /healthz
kubectl get --raw /metrics | grep apiserver_request_duration_seconds
```

**Step 5: Use proxy mode for slow connections**

```bash
# Start kubectl proxy in background
kubectl proxy --port=8001 &

# Use proxy endpoint
kubectl get pods --server=http://localhost:8001
```

## Common Mistakes

- **Not filtering large resource queries**: Always use labels and namespaces to narrow results.
- **Using default timeout for critical operations**: Increase timeout for `apply`, `rollout`, and `delete` operations.
- **Ignoring API server metrics**: Monitor API server latency and request counts regularly.
- **Running kubectl through multiple proxies**: Minimize network hops between kubectl and the API server.

## Related Pages

- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server connectivity
- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) — Pod scheduling delays
- [Ansible Unreachable Host](/tools/ansible/ansible-unreachable-host/) — Network reachability issues
