---
title: "[Solution] Kubectl Service Endpoint Not Found — How to Fix"
description: "Fix kubectl service endpoint errors by verifying service selectors match pod labels, checking endpoint objects, validating port configurations, and troubleshooting DNS resolution."
tools: ["kubectl"]
error-types: ["service-error"]
severities: ["error"]
weight: 5
comments: true
---

A service endpoint error occurs when a Kubernetes Service has no endpoints — meaning there are no pods matching the service's label selector to receive traffic. This results in connection refused or timeout errors when trying to reach the service.

## What This Error Means

Kubernetes Services provide a stable IP address and DNS name for accessing a set of pods. The service uses a label selector to identify which pods should receive traffic. The endpoint controller continuously monitors pods and updates the service's Endpoints (or EndpointSlice) object. When no pods match the selector, the endpoints list is empty, and connections to the service fail.

This can happen because the pods have not been created, the labels do not match, the pods are not ready, or the service is pointing to external endpoints incorrectly.

## Why It Happens

- The service's label selector does not match any pod's labels
- The pods exist but are not in a Ready state
- The pods are in a different namespace from the service
- The service port name or number does not match the container port
- The service is using a custom endpoint that does not exist or is unreachable
- The pods have not been created yet (deployment not scaled up)
- Network policies are blocking traffic to the pods
- The service type is ClusterIP but accessed from outside the cluster

## Common Error Messages

```
error: unable to find endpoints for service "my-service": no endpoints available
# or
dial tcp: lookup my-service on <dns>: no such host
# or
Connection refused — my-service:8080
# or
service "my-service" not found
```

## How to Fix It

### 1. Check Service Endpoints

```bash
# List endpoints for the service
kubectl get endpoints my-service

# Check endpoint details
kubectl describe endpoints my-service

# If the endpoints list is empty, the selector is not matching any pods
# Expected: Addresses: 172.17.0.3, 172.17.0.4
# Problem: Addresses: <none>
```

### 2. Verify Service Selector Matches Pod Labels

```bash
# Check service selector
kubectl get service my-service -o jsonpath='{.spec.selector}'
# Returns: {"app": "my-app", "tier": "backend"}

# Check pod labels
kubectl get pods --show-labels | grep my-app
# Pod labels must match ALL selectors

# If labels don't match, fix the service or pod labels
kubectl label pods my-pod app=my-app
```

### 3. Check Pod Readiness

```bash
# Check if pods are running and ready
kubectl get pods -l app=my-app

# The READY column should show 1/1 (or more)
# If 0/1, the pod is not passing readiness probes

# Check pod conditions
kubectl get pod my-pod -o jsonpath='{.status.conditions[?(@.type=="Ready")]}'

# Describe the pod for more detail
kubectl describe pod my-pod
```

### 4. Validate Port Configuration

```bash
# Check service ports
kubectl get service my-service -o yaml | grep -A 10 "ports:"

# Check container ports
kubectl get pod my-pod -o yaml | grep -A 5 "ports:"

# The service targetPort must match the container port
# If container port is 3000, service targetPort should be 3000

# Example fix:
kubectl edit service my-service
# Change spec.ports[0].targetPort to match the container port
```

### 5. Debug with Ephemeral Container

```bash
# Start a debug pod in the same namespace
kubectl run debug --image=busybox --rm -it --restart=Never -- /bin/sh

# Inside the pod, test DNS resolution
nslookup my-service

# Test connectivity
wget -O- http://my-service:8080/healthz
telnet my-service 8080

# Check if the service IP is reachable
env | grep MY_SERVICE_SERVICE_HOST
```

### 6. Check for Network Policies

```bash
# List network policies in the namespace
kubectl get networkpolicies

# If a network policy is blocking traffic, check its rules
kubectl describe networkpolicy default-deny

# Temporarily delete the policy to test
kubectl delete networkpolicy default-deny
```

### 7. Fix ExternalName Service

```bash
# If using ExternalName type, verify DNS resolution
kubectl get service my-service -o yaml

# The spec.externalName must be a valid DNS name
# Test from within the cluster:
kubectl run debug --image=busybox --rm -it --restart=Never -- nslookup api.example.com
```

### 8. Recreate Endpoints Manually (for headless services)

```yaml
# For headless services (clusterIP: None), you can create endpoints manually
apiVersion: v1
kind: Endpoints
metadata:
  name: my-service
subsets:
- addresses:
  - ip: 192.168.1.100
  - ip: 192.168.1.101
  ports:
  - port: 8080
```

## Common Scenarios

### Labels Don't Match After Deployment Update

A deployment is updated with new labels (e.g., `app: my-app-v2`) but the service still uses the old selector (`app: my-app-v1`). The service has no endpoints. Update the service selector or the deployment labels to match.

### Pods Not Ready Due to Failing Readiness Probe

A service has the correct selector, but all matching pods show `0/1 READY` because their readiness probes are failing. The pods exist but are not included in the service endpoints. Fix the readiness probe configuration or the application's health endpoint.

### Network Policy Blocks Cross-Namespace Access

An application in `namespace-a` tries to reach `my-service.namespace-b.svc.cluster.local`, but a network policy in `namespace-b` denies ingress from other namespaces. The DNS resolves, but connections time out. Update the network policy to allow cross-namespace traffic.

## Prevent It

- Use shared labels consistently across deployments and services (e.g., `app.kubernetes.io/name`)
- Keep service selectors in version control alongside deployment manifests
- Use `kubectl describe service` to verify endpoints after creating services
- Set up monitoring to alert when a service has zero endpoints
- Use readiness probes to ensure only healthy pods receive traffic
- Test service discovery with ephemeral debug pods after deployment
- Use service meshes (Istio, Linkerd) for advanced traffic management
- Define network policies that explicitly allow service-to-service communication

## Related Pages

- [Kubectl CrashLoopBackOff Error](/tools/kubectl/kubectl-crash-loop-error)
- [Kubectl ConfigMap Mount Error](/tools/kubectl/kubectl-configmap-error)
- [Kubectl DaemonSet Scheduling Error](/tools/kubectl/kubectl-daemonset-error)
