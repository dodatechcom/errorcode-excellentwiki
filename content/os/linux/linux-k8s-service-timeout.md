---
title: "[Solution] Linux Kubernetes Service Connection Timeout"
description: "Fix Linux Kubernetes service connection timeout errors. Resolve service DNS issues, endpoint problems, and network policy blocks."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: Kubernetes — service connection timeout

The Kubernetes service connection timeout error such as `dial tcp <cluster-ip>:<port>: i/o timeout` or `connection timed out` means a pod cannot establish a network connection to a Kubernetes Service. This indicates a network layer issue within the cluster, not necessarily a problem with the backend pods.

## What This Error Means

Kubernetes Services provide a stable virtual IP (ClusterIP) that routes traffic to backend pods via selectors and endpoints. A connection timeout means the kube-proxy or CNI plugin is not correctly routing traffic from the client pod to the target Service. The Service may have no ready endpoints, DNS resolution may be failing, or network policies may be blocking the traffic.

## Common Causes

- No pods matching the Service selector are ready
- Service DNS name not resolving (CoreDNS issue)
- Network policies blocking traffic between namespaces
- kube-proxy or CNI plugin misconfigured
- Target pods are on a different node with network issues
- iptables/IPVS rules not updated after pod changes
- Service and client pods in different namespaces without proper routing

## How to Fix

### 1. Check Service and Endpoints

```bash
# Verify the service exists and has endpoints
kubectl get svc <service-name> -n <namespace>
kubectl get endpoints <service-name> -n <namespace>

# Endpoints should show pod IPs — if empty, no matching pods
# Check selector matches pod labels
kubectl get pods -n <namespace> --show-labels
```

### 2. Test DNS Resolution

```bash
# From inside a client pod
kubectl exec -it <client-pod> -- nslookup <service-name>
kubectl exec -it <client-pod> -- nslookup <service-name>.<namespace>.svc.cluster.local

# Check CoreDNS pods
kubectl get pods -n kube-system -l k8s-app=kube-dns

# Test DNS with a debug pod
kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup kubernetes.default
```

### 3. Test Connectivity Directly

```bash
# Test connection to the service IP
kubectl exec -it <client-pod> -- wget -qO- --timeout=5 http://<service-name>:<port>

# Test using the pod IP directly (bypasses service)
kubectl exec -it <client-pod> -- wget -qO- --timeout=5 http://<target-pod-ip>:<port>

# Test with curl for more detail
kubectl exec -it <client-pod> -- curl -v --connect-timeout 5 http://<service-name>:<port>
```

### 4. Check Network Policies

```bash
# List network policies in the namespace
kubectl get networkpolicy -n <namespace>

# Check if any policy blocks traffic
kubectl describe networkpolicy <policy-name> -n <namespace>

# Temporarily remove restrictive policies for testing
kubectl delete networkpolicy <policy-name> -n <namespace>
```

### 5. Verify kube-proxy

```bash
# Check kube-proxy is running
kubectl get pods -n kube-system -l k8s-app=kube-proxy

# Check kube-proxy mode
kubectl logs -n kube-system -l k8s-app=kube-proxy | head -20

# Verify iptables rules
sudo iptables -t nat -L KUBE-SERVICES | grep <service-port>
```

### 6. Check CNI Plugin

```bash
# Verify CNI pods are running
kubectl get pods -n kube-system | grep -i 'calico\|flannel\|cilium\|weave'

# Check CNI logs for errors
kubectl logs -n kube-system -l k8s-app=<cni-plugin> | tail -20

# Restart CNI if needed
kubectl rollout restart daemonset <cni-daemonset> -n kube-system
```

### 7. Check Node Network

```bash
# Verify nodes are Ready
kubectl get nodes

# Check node conditions
kubectl describe node <node-name> | grep -A5 Conditions

# Check node network connectivity
kubectl exec -it <pod-on-node> -- ping -c 3 <service-cluster-ip>
```

## Examples

```bash
$ kubectl get svc myservice
NAME         TYPE        CLUSTER-IP      PORT(S)   AGE
myservice    ClusterIP   10.96.100.200   80/TCP    1d

$ kubectl get endpoints myservice
NAME         ENDPOINTS   AGE
myservice    <none>      1d    # No endpoints — no matching pods

$ kubectl get pods --show-labels | grep app=myapi
# No pods with label app=myapi

$ kubectl apply -f deployment.yaml
$ kubectl get endpoints myservice
NAME         ENDPOINTS                     AGE
myservice    10.244.1.5:8080,10.244.2.3:8080  30s

$ kubectl exec -it debug-pod -- curl --connect-timeout 5 http://myservice:80
{"status":"ok"}
```

## Related Errors

- [K8s pod crash]({{< relref "/os/linux/linux-k8s-pod-crash" >}}) — Pod crashing with exit codes
- [K8s RBAC error]({{< relref "/os/linux/linux-k8s-rbac-error" >}}) — Permission and RBAC issues
- [K8s OOM killed]({{< relref "/os/linux/linux-k8s-oom-killed" >}}) — Out of memory kills
