---
title: "[Solution] Swift Core Data + CloudKit Sync Error"
description: "Fix Swift NSPersistentCloudKitContainer errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 137
---

Core Data + CloudKit sync errors occur when `NSPersistentCloudKitContainer` is misconfigured, sync isn't enabled properly, or CloudKit container doesn't match.

## Common Causes

```swift
// Using NSPersistentContainer instead of CloudKit container
let container = NSPersistentContainer(name: "MyApp") // Not CloudKit-enabled

// CloudKit container identifier mismatch
// App uses "iCloud.com.app.other" but container is "iCloud.com.app"
```

## How to Fix

**1. Use NSPersistentCloudKitContainer**

```swift
let container = NSPersistentCloudKitContainer(name: "MyApp")

container.loadPersistentStores { description, error in
    if let error = error {
        print("CloudKit store failed: \(error)")
    }
}

container.viewContext.automaticallyMergesChangesFromParent = true
```

**2. Enable CloudKit in capabilities**

```swift
// In Xcode: Target > Signing & Capabilities > + CloudKit
// Container: iCloud.com.yourapp.container
```

**3. Handle CloudKit sync errors**

```swift
NotificationCenter.default.addObserver(
    forName: .NSPersistentCloudKitContainerEventDidChange,
    object: container,
    queue: .main
) { notification in
    print("CloudKit sync event: \(notification.userInfo ?? [:])")
}
```

**4. Configure CloudKit identifier**

```swift
let description = NSPersistentStoreDescription()
description.cloudKitContainerOptions = NSPersistentCloudKitContainerOptions(
    containerIdentifier: "iCloud.com.yourapp.container"
)
```

**5. Handle conflicts**

```swift
context.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
// Or NSMergeByPropertyStoreTrumpMergePolicy for store-wins
```

## Examples

Complete CloudKit setup:
```swift
class CloudKitStack {
    static let shared = CloudKitStack()
    
    lazy var container: NSPersistentCloudKitContainer = {
        let container = NSPersistentCloudKitContainer(name: "MyApp")
        
        let description = NSPersistentStoreDescription()
        description.cloudKitContainerOptions = NSPersistentCloudKitContainerOptions(
            containerIdentifier: "iCloud.com.myapp.container"
        )
        
        container.persistentStoreDescriptions = [description]
        
        container.loadPersistentStores { _, error in
            if let error = error {
                print("CloudKit load failed: \(error)")
            }
        }
        
        container.viewContext.automaticallyMergesChangesFromParent = true
        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
        
        return container
    }()
    
    func save() {
        guard container.viewContext.hasChanges else { return }
        try? container.viewContext.save()
    }
}
```

## Related Errors

- [NSPersistentContainer Error](/languages/swift/swift-nspersistentcontainer-error)
- [CoreData Fetch Error](/languages/swift/swift-coredata-fetch-request)
- [CoreData Derived Data Error](/languages/swift/swift-coredata-derived-data)
