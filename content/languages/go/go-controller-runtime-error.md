---
title: "[Solution] Go controller-runtime Error — How to Fix"
description: "Fix Go controller-runtime errors. Handle manager setup, controller registration, client operations, and reconciler patterns."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go controller-runtime Error

Fix Go controller-runtime errors. Handle manager setup, controller registration, client operations, and reconciler patterns.

## Why It Happens

- Manager does not start because of missing leader election configuration
- Client cannot connect to cluster because of kubeconfig issues
- Controller does not watch for resource changes because of missing watch configuration
- Reconciler errors cause infinite requeue loops

## Common Error Messages

```
controller-runtime: manager not started
```
```
controller-runtime: client not found
```
```
controller-runtime: no kind match
```
```
controller-runtime: unable to get kubeconfig
```

## How to Fix It

### Solution 1: Set up manager

```go
mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
    Scheme: scheme,
    MetricsBindAddress: ":8080",
    LeaderElection: true,
    LeaderElectionID: "myapp-lock",
})
```

### Solution 2: Register controller

```go
if err := (&controllers.MyReconciler{
    Client: mgr.GetClient(),
    Scheme: mgr.GetScheme(),
}).SetupWithManager(mgr); err != nil {
    log.Fatal(err, "unable to create controller")
}
```

### Solution 3: Use client properly

```go
func (r *MyReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    var deployment appsv1.Deployment
    if err := r.Get(ctx, req.NamespacedName, &deployment); err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }
    deployment.Spec.Replicas = pointer.Int32(3)
    if err := r.Update(ctx, &deployment); err != nil {
        return ctrl.Result{}, err
    }
    return ctrl.Result{}, nil
}
```

### Solution 4: Setup watches

```go
func (r *MyReconciler) SetupWithManager(mgr ctrl.Manager) error {
    return ctrl.NewControllerManagedBy(mgr).
        For(&appsv1.Deployment{}).
        Owns(&corev1.Pod{}).
        Complete(r)
}
```

## Common Scenarios

- Manager fails to start because leader election is not configured
- Client cannot list resources because of missing RBAC permissions
- Controller does not reconcile on related resource changes

## Prevent It

- Configure leader election for multi-replica deployments
- Use controller-runtime client with proper RBAC annotations
- Set up Owns() watches to trigger reconciliation on owned resources
