---
title: "[Solution] Azure DPS Registration Error"
description: "Fix Azure Device Provisioning Service registration failures for IoT device onboarding."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

DPS registration errors prevent IoT devices from being automatically provisioned to IoT Hub. This blocks zero-touch device onboarding at scale.

## Common Causes

- DPS enrollment does not match the device identity (X.509 or SAS token)
- Allocation policy cannot find a suitable IoT Hub for the device
- Device certificate chain is incomplete or untrusted
- DPS instance has reached the maximum enrollment limit

## How to Fix

### Check enrollment status

```bash
az iot dps enrollment list \
  --dps-name myDPS \
  --resource-group myRG \
  --query "[].{RegistrationId:registrationId,Status:provisioningStatus}"
```

### Create an enrollment

```bash
az iot dps enrollment create \
  --dps-name myDPS \
  --resource-group myRG \
  --enrollment-id myDevice \
  --provisioning-status enabled \
  --device-id myDevice \
  --iot-hubs "[{hubName:myHub,connectionString:HostName=myHub.azure-devices.net}]"
```

### Test provisioning

```bash
az iot dps enrollment show \
  --dps-name myDPS \
  --resource-group myRG \
  --enrollment-id myDevice \
  --query "attestation"
```

### Check DPS linked IoT Hubs

```bash
az iot dps linked-hub list \
  --dps-name myDPS \
  --resource-group myRG \
  --query "[].{HostName:hostName,AllocationWeight:allocationWeight}"
```

## Examples

- Device registration fails with `EnrollmentNotFound` because the enrollment ID does not match
- Allocation fails because no IoT Hubs are linked to the DPS instance
- Device certificate validation fails because the root CA is not uploaded to the DPS

## Related Errors

- [Azure IoT Hub Error]({{< relref "/cloud/azure/azure-iot-hub-quota" >}}) -- IoT Hub issues.
- [Azure IoT Device Twin Error]({{< relref "/cloud/azure/azure-iot-device-twin-error" >}}) -- Twin issues.
