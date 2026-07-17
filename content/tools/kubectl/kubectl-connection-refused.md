---
title: "[Solution] Kubectl Connection Refused — Fix API Server Access"
description: "Fix kubectl connection refused to API server. Resolve kubeconfig issues, network problems, and certificate errors with clear solutions."
---

## What This Error Means

The `connection refused` error means kubectl cannot reach the Kubernetes API server at the configured endpoint. The API server may be down, the kubeconfig may point to the wrong address, or network connectivity is broken.

A typical error:

```
The connection to the server localhost:8080 was refused - did you specify
the right host or port?
```

Or:

```
Unable to connect to the server: dial tcp 10.0.0.1:6443: connect:
connection refused
```

## Why It Happens

Connection refused errors happen when:

- **API server is down**: The control plane or API server process is not running.
- **Wrong kubeconfig**: The configuration points to an incorrect endpoint or port.
- **Network issues**: Firewall, VPN, or routing problems between your machine and the cluster.
- **Certificate problems**: Expired or invalid TLS certificates causing connection rejection.
- **Minikube or kind not started**: Local development cluster is not running.

## How to Fix It

**Step 1: Verify the current context and cluster**

```bash
kubectl config current-context
kubectl config view
```

**Step 2: Check if the API server is reachable**

```bash
curl -k https://localhost:6443/healthz
# Or for remote clusters
curl -k https://api.example.com:6443/healthz
```

**Step 3: Start your local cluster if using Minikube**

```bash
minikube start
# Or for kind
kind create cluster
```

**Step 4: Update the kubeconfig for remote clusters**

```bash
# Reconfigure for the correct cluster
kubectl config set-cluster my-cluster --server=https://api.example.com:6443 --certificate-authority=/path/to/ca.crt

# Or use a cloud provider's context
aws eks update-kubeconfig --name my-cluster --region us-west-2
gcloud container clusters get-credentials my-cluster --zone us-central1-a
az aks get-credentials --resource-group myRG --name myAKSCluster
```

**Step 5: Verify network connectivity**

```bash
# Check if the port is open
nc -zv api.example.com 6443
# Check DNS resolution
nslookup api.example.com
```

## Common Mistakes

- **Using localhost for remote clusters**: Ensure the server address matches the actual cluster endpoint.
- **Expired certificates**: Check certificate expiry with `openssl x509 -in ca.crt -noout -dates`.
- **Not running `minikube start`**: Local clusters must be explicitly started before using kubectl.
- **Using wrong kubeconfig file**: Set `KUBECONFIG` environment variable to point to the correct file.

## Related Pages

- [Kubectl Context Error](/tools/kubectl/kubectl-context-error/) — Context configuration issues
- [Kubectl Timeout](/tools/kubectl/kubectl-timeout/) — Request timeout errors
- [Ansible Connection Refused](/tools/ansible/ansible-connection-refused/) — SSH connection issues
