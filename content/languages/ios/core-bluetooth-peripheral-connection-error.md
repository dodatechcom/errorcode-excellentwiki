---
title: "[Solution] Core Bluetooth Peripheral Connection Error"
description: "Fix Core Bluetooth peripheral connection and disconnection errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Bluetooth Peripheral Connection Error

Bluetooth peripheral connection errors occur when the peripheral is not in range, the central manager is not powered on, or connection limits are reached.

## Common Causes
- Bluetooth not enabled on device
- Peripheral out of range
- Too many simultaneous connections
- Central manager not in correct state

## How to Fix
1. Check centralManager.state before connecting
2. Handle connection timeouts
3. Limit concurrent connections
4. Implement didDisconnectPeripheral for recovery

```swift
func centralManagerDidUpdateState(_ central: CBCentralManager) {
    switch central.state {
    case .poweredOn: central.scanForPeripherals(withServices: nil)
    case .poweredOff: print("Bluetooth is off")
    default: break
    }
}
```

## Examples
```swift
// Connection management:
func connect(_ peripheral: CBPeripheral) {
    guard centralManager.state == .poweredOn else { return }
    peripheral.delegate = self
    centralManager.connect(peripheral, options: [
        CBConnectPeripheralOptionNotifyOnConnectionKey: true
    ])
}

func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error: Error?) {
    // Attempt reconnection after delay
    DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
        self.connect(peripheral)
    }
}
```
