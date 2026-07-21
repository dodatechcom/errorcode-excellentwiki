---
title: "Bluetooth LE Scan Error"
description: "Fix Android Bluetooth LE scanning errors and callback issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bluetooth LE scan does not find devices or stops prematurely

## Common Causes

- BluetoothAdapter not enabled
- Scan settings not configured for low power
- Scan callback not properly registered
- Scan timeout not handled

## Fixes

- Ensure BluetoothAdapter is enabled
- Configure ScanSettings for desired mode
- Register ScanCallback with proper methods
- Implement scan timeout with stopScan

## Code Example

```kotlin
val scanner = bluetoothAdapter.bluetoothLeScanner
val settings = ScanSettings.Builder()
    .setScanMode(ScanSettings.SCAN_MODE_LOW_LATENCY)
    .setReportDelay(0)
    .build()

val callback = object : ScanCallback() {
    override fun onScanResult(callbackType: Int, result: ScanResult) {
        val device = result.device
        Log.d("BLE", "Found: ${device.name} ${device.address}")
    }

    override fun onScanFailed(errorCode: Int) {
        Log.e("BLE", "Scan failed: $errorCode")
    }
}

scanner.startScan(null, settings, callback)

// Stop after timeout:
handler.postDelayed({
    scanner.stopScan(callback)
}, 10000)
```

# SCAN_MODE_LOW_POWER: battery friendly
# SCAN_MODE_BALANCED: balanced
# SCAN_MODE_LOW_LATENCY: fastest, battery drain
