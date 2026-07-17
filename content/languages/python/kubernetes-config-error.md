---
title: "[Solution] Kubernetes config.load_incluster_config Failed Fix"
description: "Fix Kubernetes config.load_incluster_config failed. Verify in-cluster service account, check pod status, and handle config loading correctly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Kubernetes config.load_incluster_config Failed Fix

A `config.load_incluster_config()` failure occurs when the Kubernetes Python client cannot load the in-cluster service account configuration, typically because the code is not running inside a Kubernetes pod.

## What This Error Means

Common messages:

- `config.ConfigException: InClusterConfig: unable to load in-cluster configuration`
- `config.ConfigException: could not find a required file: /var/run/secrets/kubernetes.io/serviceaccount/token`
- `config.ConfigException: InClusterConfig: not running in a cluster`

The Kubernetes client expects specific service account files at `/var/run/secrets/kubernetes.io/serviceaccount/` when running inside a pod. These files are missing when running outside the cluster.

## Common Causes

```python
from kubernetes import config, client

# Cause 1: Running outside Kubernetes cluster
config.load_incluster_config()  # Fails — not in a pod

# Cause 2: Service account not mounted
# Pod spec missing automountServiceAccountToken: true

# Cause 3: Running in a container but not in Kubernetes
# Docker Compose — no service account mounted

# Cause 4: Pod not scheduled yet or in pending state
config.load_incluster_config()  # Pod initializing, files not ready
```

## How to Fix

### Fix 1: Use fallback to kubeconfig

```python
from kubernetes import config

try:
    config.load_incluster_config()
    print("Loaded in-cluster config")
except config.ConfigException:
    config.load_kube_config()
    print("Loaded kubeconfig")
```

### Fix 2: Verify service account is mounted

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      serviceAccountName: my-service-account
      automountServiceAccountToken: true
      containers:
        - name: app
          image: my-image
```

### Fix 3: Check required service account files

```python
import os

sa_path = "/var/run/secrets/kubernetes.io/serviceaccount"
required_files = ["token", "ca.crt", "namespace"]

for f in required_files:
    path = os.path.join(sa_path, f)
    exists = os.path.exists(path)
    print(f"{f}: {'exists' if exists else 'MISSING'}")
```

### Fix 4: Create minimal service account for the pod

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-account
  namespace: default
```

### Fix 5: Handle both local and cluster environments

```python
from kubernetes import config, client

def get_k8s_client():
    try:
        config.load_incluster_config()
    except config.ConfigException:
        config.load_kube_config()
    return client.CoreV1Api()

v1 = get_k8s_client()
pods = v1.list_namespaced_pods("default")
```

## Related Errors

- {{< relref "connectionrefusederror" >}} — Connection refused to Kubernetes API server.
- {{< relref "docker-python-sdk-error" >}} — Docker SDK connection error.
