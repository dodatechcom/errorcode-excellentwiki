---
title: "[Solution] HomeKit Accessory Not Found Error"
description: "Fix HomeKit accessory discovery and pairing failures in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# HomeKit Accessory Not Found Error

HomeKit accessories fail to appear during discovery or pairing fails due to network issues or unsupported accessory protocols.

## Common Causes
- Accessory not in pairing mode
- Network configuration blocking mDNS/Bonjour
- Accessory not compatible with HomeKit
- Pairing code entered incorrectly

## How to Fix
1. Ensure accessory is in pairing mode
2. Verify local network has mDNS enabled
3. Check accessory HomeKit compatibility
4. Use correct pairing code from accessory

```swift
import HomeKit

let homeManager = HMHomeManager()
homeManager.delegate = self

// Discover accessories:
func homeManagerDidUpdateHomes(_ manager: HMHomeManager) {
    if let home = manager.homes.first {
        let browser = HMAccessoryBrowser()
        browser.startSearchingForNewAccessories()
    }
}
```

## Examples
```swift
// Accessory browser delegate:
func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory) {
    print("Found: \(accessory.name)")
    // Start pairing
    home.addAccessory(accessory) { error in
        if let error = error {
            print("Pairing failed: \(error)")
        }
    }
}
```
