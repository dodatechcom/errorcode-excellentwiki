---
title: "[Solution] solo.io Gateway Error Fix"
description: "Fix solo.io Gloo gateway errors. Handle route configuration, upstream services, and filter chains."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# solo.io Gateway Error

The solo.io Gloo or Istio-based gateway fails during configuration when route tables are invalid, upstream services are unreachable, TLS termination is misconfigured, or virtual services conflict. Gloo uses Envoy under the hood, so errors often come from Envoy proxy configuration.

## Common Causes

```go
// Cause 1: Upstream service not found in discovery
// Gloo cannot find the target Kubernetes service

// Cause 2: Route table references non-existent function
// Function Discovery Service (FDS) did not discover the function

// Cause 3: TLS secret missing or wrong format
// Kubernetes secret does not contain tls.crt/tls.key

// Cause 4: Virtual service conflicts with existing routes
// Two virtual services claim same domain/path combination

// Cause 5: Envoy filter configuration error
// Custom Lua or WASM filter produces invalid config
```

## How to Fix

### Fix 1: Verify upstream discovery

```yaml
# Check Gloo discovery
kubectl get upstreams -n gloo-system
```

### Fix 2: Configure proper TLS

```yaml
apiVersion: networking.gloo.solo.io/v1
kind: VirtualService
metadata:
  name: my-service
spec:
  virtualHost:
    domains:
    - myapp.example.com
    routes:
    - matchers:
      - prefix: /
      routeAction:
        single:
          upstream:
            name: my-service
```

## Examples

```yaml
apiVersion: networking.gloo.solo.io/v1
kind: VirtualService
metadata:
  name: httpbin
spec:
  virtualHost:
    domains:
    - httpbin.example.com
    routes:
    - matchers:
      - prefix: /status
      routeAction:
        single:
          upstream:
            name: httpbin
```

## Related Errors

- [http-status-404]({{< relref "/languages/go/http-status-404" >}}) — gateway returns 404
- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS termination fails
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — upstream unavailable
