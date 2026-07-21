---
title: "Bluetooth GATT Error"
description: "Fix Android Bluetooth GATT connection and characteristic read/write errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bluetooth GATT connection fails or characteristic operations fail

## Common Causes

- GATT connection not established before operations
- Characteristic not found on remote device
- Write operation failing with GATT error
- GATT connection dropping randomly

## Fixes

- Wait for onConnectionStateChange before operations
- Discover services before accessing characteristics
- Check characteristic properties before read/write
- Handle reconnection with exponential backoff

## Code Example

```kotlin
val gattCallback = object : BluetoothGattCallback() {
    override fun onConnectionStateChange(gatt: BluetoothGatt, status: Int, newState: Int) {
        if (newState == BluetoothProfile.STATE_CONNECTED) {
            gatt.discoverServices()
        }
    }

    override fun onServicesDiscovered(gatt: BluetoothGatt, status: Int) {
        if (status == BluetoothGatt.GATT_SUCCESS) {
            val characteristic = gatt.getService(uuid)
                ?.getCharacteristic(characteristicUuid)
            gatt.readCharacteristic(characteristic)
        }
    }

    override fun onCharacteristicRead(
        gatt: BluetoothGatt, characteristic: BluetoothGattCharacteristic, status: Int
    ) {
        if (status == BluetoothGatt.GATT_SUCCESS) {
            val value = characteristic.value
        }
    }
}

device.connectGatt(context, false, gattCallback)
```

# Connection flow: connect -> discover services -> read/write
# Always check status in callbacks
# Handle GATT_ERROR status codes
