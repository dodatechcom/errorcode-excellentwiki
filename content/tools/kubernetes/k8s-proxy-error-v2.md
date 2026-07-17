---
title: "[Solution] Kubernetes kube-proxy — iptables error"
description: "Fix Kubernetes kube-proxy iptables errors. Resolve kube-proxy and service networking issues."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kubernetes", "kube-proxy", "iptables", "proxy", "networking", "service"]
weight: 5
---

A kube-proxy iptables error means the node's service proxy rules are broken or outdated. Pods on the node cannot reach services through ClusterIP, and service load balancing fails.

## What This Error Means

kube-proxy maintains iptables rules on each node to forward traffic from pod IPs to service endpoints. When these rules become stale, corrupted, or fail to sync, service communication breaks down on that node. Pods may see intermittent connection failures to services, or connections may route to terminated pods. This is a node-level networking issue.

## Common Causes

- kube-proxy sync loop is failing or too slow
- iptables rules corrupted after node reboot
- conntrack table is full on the node
- iptables backend incompatibility (legacy vs nftables)
- kube-proxy PodSecurityPolicy or RBAC issues
- Too many services overwhelming iptables rule capacity

## How to Fix

### Check kube-proxy Status

```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
kubectl logs -n kube-system -l k8s-app=kube-proxy --tail=100
```

### Check kube-proxy Mode

```bash
kubectl get configmap kube-proxy -n kube-system -o yaml
```

### Restart kube-proxy

```bash
kubectl rollout restart daemonset kube-proxy -n kube-system
```

### Check iptables Rules

```bash
sudo iptables -t nat -L KUBE-SERVICES -n
sudo iptables -t nat -L KUBE-SEP- -n
```

### Check conntrack Table

```bash
sudo sysctl net.netfilter.nf_conntrack_count
sudo sysctl net.netfilter.nf_conntrack_max
```

### Flush and Rebuild iptables

```bash
sudo iptables -t nat -F
sudo systemctl restart kube-proxy
```

### Switch to IPVS Mode

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-proxy
  namespace: kube-system
data:
  mode: "ipvs"
  ipvs:
    scheduler: "rr"
```

### Increase conntrack Max

```bash
sudo sysctl -w net.netfilter.nf_conntrack_max=262144
```

## Related Errors

- [Kubernetes Service Unavailable]({{< relref "/tools/kubernetes/k8s-service-unavailable-v2" >}}) — no endpoints
- [Kubernetes NetworkPolicy]({{< relref "/tools/kubernetes/k8s-network-policy-v2" >}}) — ingress blocked
- [Kubernetes DNS Resolution]({{< relref "/tools/kubernetes/k8s-dns-resolution-v2" >}}) — CoreDNS failed
