---
title: "[Solution] Invalid YAML or JSON in Kubernetes manifest"
description: "Fix Kubernetes invalid YAML or JSON errors. Resolve resource creation failures caused by malformed manifest files."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Invalid YAML / JSON

`error: error parsing <file>: error converting YAML to JSON: yaml: line <n>: did not find expected key`

This error occurs when kubectl cannot parse a Kubernetes manifest file due to YAML or JSON syntax errors.

### Common Causes

- Incorrect indentation (YAML is space-sensitive)
- Tab characters used instead of spaces
- Missing colons or commas
- Mismatched quotes or brackets

### How to Fix

Validate the YAML file:
```bash
kubectl apply -f manifest.yaml --dry-run=server
python3 -c "import yaml; yaml.safe_load(open('manifest.yaml'))"
```

Use a YAML linter:
```bash
yamllint manifest.yaml
```

### Examples

```yaml
# Correct YAML
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.25
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})