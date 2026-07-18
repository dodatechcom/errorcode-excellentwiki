---
title: "[Solution] React Native Bluetooth Connection Error — How to Fix"
description: "Fix React Native Bluetooth errors. Resolve Bluetooth scanning, pairing, and BLE connection issues."
frameworks: ["react-native"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A React Native Bluetooth connection error occurs when the app cannot scan for, connect to, or communicate with Bluetooth devices. Bluetooth Low Energy (BLE) is commonly used in IoT and wearable integrations.

## Why It Happens

Bluetooth requires platform-specific permissions and API usage. Errors occur when Bluetooth permissions are not granted, when the Bluetooth adapter is turned off, when the device is not in range, when the BLE library is not properly initialized, when the service UUID is incorrect, or when the connection timeout is too short.

## Common Error Messages

```
BLE: Bluetooth adapter is not available
```

```
Error: Device not found
```

```
BleManager: Connection timeout
```

```
Error: Characteristic not found
```

## How to Fix It

### 1. Set Up BLE Library

Configure `react-native-ble-plx`:

```typescript
import { BleManager } from 'react-native-ble-plx';
import { Platform, PermissionsAndroid } from 'react-native';

const manager = new BleManager();

// Request permissions (Android)
async function requestPermissions() {
    if (Platform.OS === 'android') {
        const granted = await PermissionsAndroid.requestMultiple([
            PermissionsAndroid.PERMISSIONS.BLUETOOTH_SCAN,
            PermissionsAndroid.PERMISSIONS.BLUETOOTH_CONNECT,
            PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
        ]);

        return Object.values(granted).every(
            (result) => result === PermissionsAndroid.RESULTS.GRANTED
        );
    }
    return true; // iOS permissions handled in Info.plist
}
```

### 2. Scan and Connect to Devices

Implement scanning and connection:

```typescript
async function scanAndConnect() {
    const hasPermission = await requestPermissions();
    if (!hasPermission) {
        console.error('Bluetooth permissions not granted');
        return;
    }

    // Scan for devices
    manager.startDeviceScan(null, null, (error, device) => {
        if (error) {
            console.error('Scan error:', error);
            return;
        }

        if (device.name === 'MyDevice') {
            manager.stopDeviceScan();
            connectToDevice(device);
        }
    });

    // Stop scan after 10 seconds
    setTimeout(() => manager.stopDeviceScan(), 10000);
}

async function connectToDevice(device) {
    try {
        const connected = await device.connect();
        console.log('Connected:', connected.name);

        const services = await connected.discoverAllServicesAndCharacteristics();
        console.log('Services:', services.services);

        return connected;
    } catch (error) {
        console.error('Connection failed:', error);
        // Try reconnecting
        await device.cancelConnection();
    }
}
```

### 3. Read and Write Characteristics

Communicate with the device:

```typescript
async function readCharacteristic(device, serviceUUID, characteristicUUID) {
    try {
        const characteristic = await device.readCharacteristicForService(
            serviceUUID,
            characteristicUUID
        );
        return characteristic.value;
    } catch (error) {
        console.error('Read failed:', error);
    }
}

async function writeCharacteristic(device, serviceUUID, characteristicUUID, data) {
    try {
        const base64Data = Buffer.from(data).toString('base64');
        await device.writeCharacteristicWithResponseForService(
            serviceUUID,
            characteristicUUID,
            base64Data
        );
    } catch (error) {
        console.error('Write failed:', error);
    }
}

// Listen for notifications
device.monitorCharacteristicForService(
    serviceUUID,
    characteristicUUID,
    (error, characteristic) => {
        if (error) {
            console.error('Monitor error:', error);
            return;
        }
        const value = Buffer.from(characteristic.value, 'base64').toString();
        console.log('Received:', value);
    }
);
```

### 4. Handle Connection State

Monitor connection state changes:

```typescript
manager.onDeviceDisconnected((error, device) => {
    console.log('Device disconnected:', device.name);
    // Attempt reconnection
    setTimeout(() => reconnect(device), 2000);
});

async function reconnect(device) {
    try {
        await device.connect();
        await device.discoverAllServicesAndCharacteristics();
        console.log('Reconnected successfully');
    } catch (error) {
        console.error('Reconnection failed:', error);
    }
}
```

## Common Scenarios

**Scenario 1: Device not found during scan.**
Ensure Bluetooth is enabled, the device is in pairing mode, and location services are enabled (required on Android).

**Scenario 2: Connection drops frequently.**
Increase the connection interval and handle disconnections with automatic reconnection.

**Scenario 3: Cannot read characteristics.**
Verify the service UUID and characteristic UUID match the device's specification.

## Prevent It

1. **Always check Bluetooth state** before scanning or connecting.

2. **Handle disconnections gracefully** with automatic reconnection logic.

3. **Use the correct UUIDs** from the device's documentation, not hardcoded values.
