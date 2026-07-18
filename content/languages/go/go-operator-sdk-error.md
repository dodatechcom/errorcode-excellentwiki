---
title: "[Solution] Go Operator SDK Error — How to Fix"
description: "Fix Go Operator SDK errors. Handle CRD generation, controller setup, reconciliation, and deployment."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Operator SDK Error

Fix Go Operator SDK errors. Handle CRD generation, controller setup, reconciliation, and deployment.

## Why It Happens

- CRD generation fails because of incorrect API type definitions
- Controller does not reconcile because of missing RBAC permissions
- Operator deployment fails because of wrong container image configuration
- Controller-runtime client cannot list resources because of cluster role issues

## Common Error Messages

```
operator-sdk: CRD generation failed
```
```
operator-sdk: controller not found
```
```
operator-sdk: reconciliation error
```
```
operator-sdk: RBAC denied
```

## How to Fix It

### Solution 1: Define API types

```go
// api/v1/myapp_types.go
type MyAppSpec struct {
    Replicas int32  `json:"replicas"`
    Image    string `json:"image"`
}
type MyAppStatus struct {
    Ready bool `json:"ready"`
}
```

### Solution 2: Generate CRDs

```bash
operator-sdk generate crd
# Or with controller-gen
controller-gen crd paths="./api/..." output:crd:dir=config/crd/bases
```

### Solution 3: Set up controller

```go
func (r *MyAppReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    var myapp v1.MyApp
    if err := r.Get(ctx, req.NamespacedName, &myapp); err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }
    // Reconcile logic
    return ctrl.Result{RequeueAfter: 5 * time.Minute}, nil
}
```

### Solution 4: Deploy operator

```bash
operator-sdk generate kustomize manifests
operator-sdk bundle create
make docker-build docker-push
make deploy
```

## Common Scenarios

- CRD generation produces invalid YAML
- Controller cannot access cluster resources because of missing RBAC annotations
- Reconciliation loop runs infinitely because of incorrect status updates

## Prevent It

- Use kubebuilder markers for RBAC annotations
- ['Always check for NotFound errors in Reconcile', '```go\nif err := r.Get(ctx, req.NamespacedName, &myapp); err != nil {\n    return ctrl.Result{}, client.IgnoreNotFound(err)\n}\n```']
- Update status after each successful reconciliation
