---
title: "[Solution] Kubectl API Server Unreachable - Fix Connection to Server Refused"
description: "Fix kubectl connection refused errors when the API server is unreachable. Diagnose network, certificate, and API server availability issues."
tools: ["kubectl"]
error-types: ["api-server-unreachable"]
severities: ["critical"]
weight: 5
---

This error means kubectl cannot establish a connection to the Kubernetes API server. The server may be down, the network path may be blocked, or the endpoint may be wrong.

## What This Error Means

When kubectl tries to reach the API server and fails, you see:

```
The connection to the server <host>:<port> was refused
# or
Unable to connect to the server: net/http: TLS handshake timeout
# or
certificate is not valid for any names
```

The API server is the central control plane component that all kubectl commands communicate with. If it is unreachable, no cluster operations can be performed.

## Why It Happens

- The API server process is down or crashing
- A network firewall blocks access to the API server port (typically 6443)
- The kubeconfig points to the wrong API server address
- TLS certificates are expired or do not match the hostname
- The API server pod is not scheduled or is in a CrashLoopBackOff
- A load balancer in front of the API server is unhealthy

## How to Fix It

### Check the API server endpoint

```bash
kubectl cluster-info
kubectl config view | grep server
```

Verify the API server URL is correct and reachable.

### Test connectivity directly

```bash
curl -k https://<api-server>:6443/healthz
```

A response of `ok` confirms the API server is running and reachable.

### Check API server pod status

```bash
kubectl get pods -n kube-system | grep kube-apiserver
kubectl logs -n kube-system kube-apiserver-<node>
```

On managed clusters, check the cloud provider's control plane health.

### Verify certificates

```bash
openssl s_client -connect <api-server>:6443 -showcerts
```

Check that the certificate is valid and matches the hostname.

### Check firewall rules

```bash
# From the client machine
nc -zv <api-server> 6443
```

Ensure port 6443 is open between your client and the API server.

### Restart API server components

For self-managed clusters:

```bash
sudo systemctl restart kubelet
# or
sudo crictl pods | grep kube-apiserver
sudo crictl stopp <pod-id>
```

### Check load balancer health

```bash
aws elb describe-instance-health --load-balancer-name k8s-api-lb
```

Ensure the API server instances are healthy behind the load balancer.

## Common Mistakes

- Assuming the API server is down when it is a firewall issue
- Not checking certificate expiry before assuming a network problem
- Forgetting that VPN or proxy settings affect API server connectivity
- Using the wrong port in the kubeconfig server URL
- Not monitoring API server health proactively

## Related Pages

- [Kubectl Config Error]({{< relref "/tools/kubectl/kubectl-config-error" >}}) -- kubeconfig issues
- [Kubectl Connection Refused]({{< relref "/tools/kubectl/kubectl-connection-refused" >}}) -- general connectivity
- [Kubectl RBAC Error]({{< relref "/tools/kubectl/kubectl-rbac-error" >}}) -- access denied
