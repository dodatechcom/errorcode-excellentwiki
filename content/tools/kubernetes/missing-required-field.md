---
title: "[Solution] Missing required field"
description: "Fix Kubernetes 'missing required field' error. Resolve resource creation failures when required fields are not specified."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Missing Required Field

`error: validation failure: missing required field "<field>" in <resource>`

This error occurs when a Kubernetes resource manifest is missing a required field. The API server validates the schema and rejects incomplete resources.

### Common Causes

- Missing `apiVersion` or `kind` fields
- Missing `name` in metadata
- Missing `containers` in pod spec
- Missing `selector` in deployment or service

### How to Fix

Add the missing field to the manifest.

Use the explain command to see required fields:
```bash
kubectl explain deployment.spec
kubectl explain pod.spec.containers
```

### Examples

```bash
# Check required fields for a deployment
kubectl explain deployment
# metadata.name, spec.selector.matchLabels, spec.template.metadata.labels, spec.template.spec.containers
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})