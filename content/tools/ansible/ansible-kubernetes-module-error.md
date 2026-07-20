---
title: "[Solution] Ansible Kubernetes Module Error"
description: "Fix Ansible Kubernetes module errors when managing K8s resources"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Kubernetes module fails to manage cluster resources.

```
FAILED! => "kubernetes.config.load_kube_config failed"
```

## Common Causes

- kubeconfig not found or invalid
- Missing kubernetes collection
- Cluster not accessible
- Insufficient RBAC permissions

## How to Fix

```bash
ansible-galaxy collection install kubernetes.core
pip install kubernetes
```

```yaml
- name: Deploy to Kubernetes
  kubernetes.core.k8s:
    state: present
    definition:
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: nginx-deployment
      spec:
        replicas: 3
        selector:
          matchLabels:
            app: nginx
        template:
          metadata:
            labels:
              app: nginx
          spec:
            containers:
              - name: nginx
                image: nginx:1.19
    kubeconfig: ~/.kube/config
```
