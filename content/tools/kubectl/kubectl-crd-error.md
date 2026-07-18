---
title: "[Solution] Kubectl CRD Not Found or Malformed — How to Fix"
description: "Fix kubectl CRD errors by verifying CustomResourceDefinition registration, checking API versions, validating CRD schema, resolving naming conflicts, and ensuring CRD is established before use."
tools: ["kubectl"]
error-types: ["crd-error"]
severities: ["error"]
weight: 5
comments: true
---

A CustomResourceDefinition (CRD) error occurs when kubectl cannot find a CRD, or the CRD definition is malformed. This prevents you from creating, reading, or managing custom resources in your Kubernetes cluster.

## What This Error Means

CustomResourceDefinitions extend the Kubernetes API by allowing you to define your own resource types. Once a CRD is registered, you can create custom resources using `kubectl apply` and interact with them like built-in resources. CRD errors occur when the CRD itself is not registered, the schema is invalid, or the API version is incorrect.

CRDs must be created before any custom resources can be used. The CRD goes through an `Established` phase before it can serve requests. If the CRD schema is malformed, the API server rejects the CRD creation or the custom resource creation.

## Why It Happens

- The CRD has not been applied to the cluster yet
- The CRD has a naming conflict with an existing CRD or built-in resource
- The CRD schema is invalid (wrong JSON Schema structure, missing required fields)
- The CRD uses an API version that the cluster does not support
- The CRD is stuck in a non-Established phase (e.g., NamesAccepted, NotAccepted)
- The custom resource references a CRD that does not exist in the cluster
- The CRD was deleted but custom resources still exist
- The CRD contains validation rules that are too restrictive
- The CRD's `scope` (Namespaced vs Cluster) is used incorrectly

## Common Error Messages

```
error: the server doesn't have a resource type "myresources"
# or
unable to recognize "custom-resource.yaml": no matches for kind "MyResource" in version "example.com/v1"
# or
CustomResourceDefinition "myresources.example.com" is invalid: spec.names.singular: Invalid value
# or
the CustomResourceDefinition "myresources.example.com" is not ready: Established condition is False
```

## How to Fix It

### 1. List Available CRDs

```bash
# List all CRDs in the cluster
kubectl get crd

# Check if your CRD exists
kubectl get crd myresources.example.com

# Describe the CRD for details
kubectl describe crd myresources.example.com
```

### 2. Apply the CRD

```bash
# Apply the CRD definition from a file
kubectl apply -f my-crd.yaml

# Verify the CRD was created
kubectl get crd myresources.example.com

# Wait for the CRD to be established
kubectl wait --for=condition=Established crd/myresources.example.com --timeout=60s
```

### 3. Fix CRD Naming

```yaml
# CRD names must follow the format: <plural>.<group>
# The plural must match spec.names.plural
# The group must be a valid DNS subdomain

# Correct naming example:
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: myresources.example.com  # Must be: plural.group
spec:
  group: example.com              # DNS subdomain
  names:
    plural: myresources           # Must match the prefix in metadata.name
    singular: myresource
    kind: MyResource
    shortNames:
    - mr
```

### 4. Validate CRD Schema

```bash
# Check if the CRD has a valid OpenAPI v3 schema
kubectl get crd myresources.example.com -o yaml | grep -A 30 "openAPIV3Schema"

# Common schema issues:
# - Missing required fields in openAPIV3Schema
# - Using unsupported JSON Schema keywords
# - Incorrect type definitions

# Test the schema with a sample resource:
kubectl apply -f sample-resource.yaml
```

### 5. Check CRD Status Conditions

```bash
# Check the CRD's status conditions
kubectl get crd myresources.example.com -o jsonpath='{.status.conditions}' | jq .

# Conditions include:
# - Established: true/false
# - NamesAccepted: true/false
# - NonStructuralSchema: true/false

# If NamesAccepted is false, there is a naming conflict
# If NonStructuralSchema is true, the schema needs to be fixed
```

### 6. Fix NonStructural Schema Errors

```yaml
# Kubernetes 1.16+ requires structural schemas
# A structural schema has:
# - type defined for each object
# - properties that define nested types
# - proper x-kubernetes-* extensions

# Non-structural example (wrong):
openAPIV3Schema:
  type: object
  properties:
    spec:
      # Missing type: object
      properties:
        replicas:
          type: integer

# Structural example (correct):
openAPIV3Schema:
  type: object
  properties:
    spec:
      type: object
      properties:
        replicas:
          type: integer
          minimum: 1
```

### 7. Use Correct API Version

```bash
# CRDs use apiextensions.k8s.io/v1 (stable in 1.16+)
# Older clusters may need apiextensions.k8s.io/v1beta1

# Check cluster version:
kubectl version

# For clusters >= 1.22, use v1:
apiVersion: apiextensions.k8s.io/v1

# For clusters < 1.22, you may need v1beta1 (deprecated in 1.22):
apiVersion: apiextensions.k8s.io/v1beta1
```

### 8. Delete and Recreate a Stuck CRD

```bash
# If a CRD is stuck, delete all custom resources first:
kubectl delete myresources --all

# Delete the CRD
kubectl delete crd myresources.example.com

# Reapply the CRD
kubectl apply -f my-crd.yaml

# Recreate custom resources
kubectl apply -f my-resources.yaml
```

### 9. Handle CRD Versioning

```yaml
# CRDs can have multiple API versions with conversion
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
spec:
  versions:
  - name: v1alpha1
    served: true
    storage: false
    schema: ...
  - name: v1
    served: true
    storage: true  # Only one version can be the storage version
    schema: ...
  conversion:
    strategy: Webhook  # Or None
```

## Common Scenarios

### CRD Name Does Not Match Plural

A CRD YAML defines `metadata.name: mythings.example.com` but `spec.names.plural` is `myresources`. The API server rejects this because the name must be `{plural}.{group}`. Fix the metadata.name to match the plural: `myresources.example.com`.

### CRD Not Established Before Custom Resources Applied

A CI/CD pipeline applies a CRD and immediately tries to create custom resources. The CRD is not yet `Established` and the custom resources fail. Add `kubectl wait --for=condition=Established crd/myresources.example.com` between the CRD and custom resource creation.

### CRD Schema Missing Type for Nested Fields

A CRD defines `spec.properties.replicas` with `type: integer` but does not define `type: object` for the `spec` property itself. This results in a `NonStructuralSchema` error. Add `type: object` to the `spec` property.

## Prevent It

- Always wait for CRD `Established` condition before creating custom resources
- Use structural schemas with proper `type` definitions for all properties
- Follow CRD naming conventions: `{plural}.{group}` in metadata.name
- Test CRD definitions with `kubectl explain` before applying
- Use `kubectl apply --server-side` for CRD creation
- Set up RBAC to prevent accidental CRD deletion
- Version CRDs carefully and plan for schema migrations
- Use `preserveUnknownFields: false` to enforce schema validation

## Related Pages

- [Kubectl Config Error](/tools/kubectl/kubectl-config-error)
- [Kubectl API Server Unreachable](/tools/kubectl/kubectl-api-server-unreachable)
- [Kubectl Context Not Found](/tools/kubectl/kubectl-context-error)
