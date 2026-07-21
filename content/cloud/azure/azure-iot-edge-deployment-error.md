---
title: "[Solution] Azure IoT Edge Deployment Error"
description: "Fix Azure IoT Edge module deployment failures for edge computing scenarios."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

IoT Edge deployment errors prevent modules from being deployed and started on edge devices. This breaks edge computing workloads and device management.

## Common Causes

- Edge device is offline and cannot pull the deployment manifest
- Module image is not accessible from the device network
- Deployment manifest has syntax errors or missing required fields
- Edge runtime is outdated and incompatible with the module SDK

## How to Fix

### Check deployment status

```bash
az iot hub device-twin show \
  --device-id myEdgeDevice \
  --hub-name myHub \
  --resource-group myRG \
  --query "properties.designed"
```

### Deploy modules via CLI

```bash
az iot hub set-modules \
  --device-id myEdgeDevice \
  --hub-name myHub \
  --resource-group myRG \
  --content deployment.json
```

### Check module logs

```bash
az iot hub device-twin show \
  --device-id myEdgeDevice \
  --hub-name myHub \
  --resource-group myRG \
  --query "properties.reported"
```

### List edge devices

```bash
az iot hub device-identity list \
  --hub-name myHub \
  --resource-group myRG \
  --query "[?capabilities.iotEdge].deviceId"
```

## Examples

- Edge device reports `MODULE_NOT_FOUND` because the container image tag does not exist in ACR
- Deployment fails with `EdgeAgentDesireMismatch` because the desired and reported properties are out of sync
- Edge device cannot pull images because the network has no internet access

## Related Errors

- [Azure IoT Hub Error]({{< relref "/cloud/azure/azure-iot-hub-quota" >}}) -- IoT Hub issues.
- [Azure IoT Device Twin Error]({{< relref "/cloud/azure/azure-iot-device-twin-error" >}}) -- Twin issues.
