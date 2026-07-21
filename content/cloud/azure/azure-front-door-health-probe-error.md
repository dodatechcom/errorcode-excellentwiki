---
title: "[Solution] Azure Front Door Health Probe Error"
description: "Fix Azure Front Door health probe failures that cause endpoint unavailability."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Health probe errors cause Front Door to mark healthy backends as unhealthy. This redirects all traffic to remaining backends and can cause overload.

## Common Causes

- Health probe path returns a non-200 HTTP status code
- Backend is not configured to respond to health probe requests
- Health probe interval is too aggressive and overwhelms the backend
- Custom health probe settings override default probe behavior incorrectly

## How to Fix

### Check origin health status

```bash
az afd origin list \
  --profile-name myFrontDoor \
  --resource-group myRG \
  --query "[].{Name:name,Health:healthProbeSettings.enabled,State:enabledState}"
```

### Update health probe settings

```bash
az afd origin update \
  --profile-name myFrontDoor \
  --resource-group myRG \
  --origin-group-name myOriginGroup \
  --origin-name myOrigin \
  --health-probe-path "/health" \
  --health-probe-protocol HTTPS \
  --health-probe-interval-in-seconds 30
```

### Check health probe response

```bash
curl -I https://myBackend.azurewebsites.net/health
```

### List load balancing settings

```bash
az afd origin-group show \
  --profile-name myFrontDoor \
  --resource-group myRG \
  --origin-group-name myOriginGroup \
  --query "loadBalancingSettings"
```

## Examples

- All origins show unhealthy because the health probe path `/` returns a redirect to login
- Health probe times out because the backend firewall blocks the Front Door probe IP range
- Origin is healthy but Front Door still sends traffic elsewhere because the sample size is too low

## Related Errors

- [Azure Front Door Error]({{< relref "/cloud/azure/azure-front-door-error" >}}) -- General Front Door errors.
- [Azure CDN Error]({{< relref "/cloud/azure/azure-cdn-error" >}}) -- CDN issues.
