---
title: "[Solution] Azure Traffic Routing Error"
description: "Fix Azure Traffic Manager DNS routing failures for geo-based and performance-based traffic distribution."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Traffic routing errors prevent Azure Traffic Manager from distributing traffic correctly across endpoints. This leads to uneven load distribution and poor user experience.

## Common Causes

- Endpoint health checks are failing and the endpoint is marked as degraded
- Routing method is configured incorrectly for the use case
- DNS TTL is too high and cached responses bypass healthy endpoints
- Endpoint weight is set to zero, excluding it from traffic distribution

## How to Fix

### Check endpoint health

```bash
az network traffic-manager endpoint list \
  --profile-name myTMProfile \
  --resource-group myRG \
  --query "[].{Name:name,Health:endpointStatus,Weight:weight}"
```

### Update endpoint status

```bash
az network traffic-manager endpoint update \
  --name myEndpoint \
  --profile-name myTMProfile \
  --resource-group myRG \
  --type azureEndpoints \
  --status Enabled
```

### Set routing method

```bash
az network traffic-manager profile update \
  --name myTMProfile \
  --resource-group myRG \
  --routing-method Performance
```

### Check DNS resolution

```bash
nslookup myapp.trafficmanager.net
```

## Examples

- Traffic routes to all endpoints even though one is unhealthy due to incorrect health probe path
- Weighted routing sends 100% traffic to one endpoint because the other has weight 0
- Performance routing selects the wrong region because the health probe interval is too long

## Related Errors

- [Azure Traffic Manager Error]({{< relref "/cloud/azure/azure-traffic-manager-error" >}}) -- General TM errors.
- [Azure DNS Error]({{< relref "/cloud/azure/azure-dns-error" >}}) -- DNS issues.
