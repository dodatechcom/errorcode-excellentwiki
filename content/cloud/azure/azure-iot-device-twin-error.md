---
title: "[Solution] Azure IoT Device Twin Error"
description: "Fix Azure IoT Hub device twin read and write failures for IoT device management."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Device twin errors prevent IoT Hub from synchronizing device state between the cloud and the device. This blocks configuration updates and telemetry correlation.

## Common Causes

- Device is not registered in the IoT Hub and twin does not exist
- Twin write operation exceeds the maximum JSON payload size
- Shared access policy does not have the DeviceConnect permission
- Twin update conflicts occur when multiple services modify the same properties

## How to Fix

### Get device twin

```bash
az iot hub device-twin show \
  --device-id myDevice \
  --hub-name myHub \
  --resource-group myRG
```

### Update desired properties

```bash
az iot hub device-twin update \
  --device-id myDevice \
  --hub-name myHub \
  --resource-group myRG \
  --set properties.desired.temperature=22
```

### List device twins

```bash
az iot hub device-twin list \
  --hub-name myHub \
  --resource-group myRG \
  --query "[].{deviceId:deviceId,status:status}"
```

### Check twin size

```bash
az iot hub device-twin show \
  --device-id myDevice \
  --hub-name myHub \
  --resource-group myRG \
  --query "properties"
```

## Examples

- Device twin update fails with `PreconditionFailed` because the ETag was modified by another service
- Twin desired properties are not applied to the device because the device SDK is outdated
- Twin read returns empty properties because the device was not provisioned correctly

## Related Errors

- [Azure IoT Hub Error]({{< relref "/cloud/azure/azure-iot-hub-quota" >}}) -- IoT Hub issues.
- [Azure Module Twin]({{< relref "/cloud/azure/azure-module-twin" >}}) -- Module twin issues.
