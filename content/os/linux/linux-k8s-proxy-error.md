---
title: "[Solution] k8s: kube-proxy Error — Service Proxy Failures"
description: "Fix Kubernetes kube-proxy errors. Resolve kube-proxy iptables/IPVS failures, service routing issues, and proxy misconfigurations."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "kube-proxy", "iptables", "ipvs", "service", "proxy"]
weight: 5
---

# k8s: kube-proxy Error — Service Proxy Failures

A kube-proxy error occurs when `kube-proxy` fails to maintain the service proxy rules on a node. Pods cannot reach Services via ClusterIP, and service load balancing breaks.

> "Failed to execute iptables" or

> "could not sync rules"

## What This Error Means

kube-proxy runs on every node and maintains network rules (iptables or IPVS) that route traffic from Service ClusterIPs/NodePorts to the backing pod endpoints. When kube-proxy fails, the rules become stale and traffic to Services is dropped or misrouted. NodePort and LoadBalancer Services stop working.

## Common Causes

- kube-proxy Pod crashed or is not running
- iptables or IPVS mode misconfigured
- iptables lock contention (too many rules)
- Conntrack table full
- Node network configuration changed
- RBAC permissions for kube-proxy service account
- IPVS module not loaded on the node

## How to Fix

### Check kube-proxy Status

```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
kubectl logs -n kube-system -l k8s-app=kube-proxy
```

### Check iptables Rules

```bash
# Check Kubernetes iptables chains
sudo iptables -t nat -L KUBE-SERVICES -n
sudo iptables -t nat -L KUBE-SEP-* -n | head -20

# Check for rule count
sudo iptables-save | wc -l
```

### Check Conntrack Table

```bash
# Check conntrack table usage
sudo sysctl net.netfilter.nf_conntrack_count
sudo sysctl net.netfilter.nf_conntrack_max

# Increase if full
sudo sysctl -w net.netfilter.nf_conntrack_max=262144
```

### Check kube-proxy Mode

```bash
kubectl get configmap kube-proxy -n kube-system -o yaml | grep mode
```

### Restart kube-proxy

```bash
kubectl rollout restart daemonset kube-proxy -n kube-system
```

### Load IPVS Module (if using IPVS mode)

```bash
sudo modprobe ip_vs
sudo modprobe ip_vs_rr
sudo modprobe ip_vs_wrr
sudo modprobe ip_vs_sh
sudo modprobe nf_conntrack
```

### Verify Service Endpoints

```bash
kubectl get endpoints <service-name>
kubectl get svc <service-name>
```

## Related Errors

- [k8s Service Unavailable]({{< relref "/os/linux/linux-k8s-service-unavailable" >}}) — Service has no endpoints
- [k8s DNS Resolution Failed]({{< relref "/os/linux/linux-k8s-dns-resolution" >}}) — DNS lookup failures
- [k8s NetworkPolicy Error]({{< relref "/os/linux/linux-k8s-network-policy" >}}) — Network policy issues
