---
title: "[Solution] Go Kubebuilder Error — How to Fix"
description: "Fix Go Kubebuilder errors. Handle project setup, controller scaffolding, RBAC, and test setup."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Kubebuilder Error

Fix Go Kubebuilder errors. Handle project setup, controller scaffolding, RBAC, and test setup.

## Why It Happens

- Kubebuilder init fails because of missing Go modules or wrong project structure
- Scaffolded controller does not compile because of wrong import paths
- RBAC markers are not correctly placed causing permission denied errors in the cluster
- Envtest cannot start because of missing binaries

## Common Error Messages

```
kubebuilder: project not initialized
```
```
kubebuilder: controller not found
```
```
kubebuilder: RBAC denied
```
```
kubebuilder: envtest binary not found
```

## How to Fix It

### Solution 1: Initialize kubebuilder project

```bash
kubebuilder init --domain my.domain --repo github.com/myorg/myoperator
kubebuilder create api --group app --version v1 --kind MyApp
```

### Solution 2: Add RBAC markers

```go
// +kubebuilder:rbac:groups=apps,resources=deployments,verbs=get;list;watch;create;update;patch;delete
// +kubebuilder:rbac:groups=core,resources=pods,verbs=get;list;watch

func (r *MyAppReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // RBAC markers generate ClusterRole in config/rbac/
}
```

### Solution 3: Use envtest for testing

```go
import "sigs.k8s.io/controller-runtime/pkg/envtest"

func TestMain(m *testing.M) {
    testEnv = &envtest.Environment{
        CRDDirectoryPaths: []string{"config/crd/bases"},
    }
    cfg, _ := testEnv.Start()
    defer testEnv.Stop()
}
```

### Solution 4: Generate manifests

```bash
make manifests  # Generate RBAC and CRD manifests
make generate   # Generate deepcopy methods
make test        # Run envtest tests
```

## Common Scenarios

- Kubebuilder project structure is wrong causing build failures
- RBAC markers do not generate correct permissions
- Envtest tests fail because CRD binaries are not available

## Prevent It

- Run make generate and make manifests after API changes
- Use kubebuilder create api to scaffold new resources
- ['Install envtest binaries before running tests', '```bash\ngo install sigs.k8s.io/controller-runtime/tools/setup-envtest@latest\nsetup-envtest use\n```']
