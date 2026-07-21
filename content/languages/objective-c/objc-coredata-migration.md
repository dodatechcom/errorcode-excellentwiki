---
title: "[Solution] Core Data Migration"
description: "Core Data model migration errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Data Migration

Core Data model migration errors.

### Common Causes
Wrong mapping model; lightweight migration

### How to Fix
```objc
NSDictionary *options = @{
    NSMigratePersistentStoresAutomaticallyOption: @YES,
    NSInferMappingModelAutomaticallyOption: @YES
};
[persistentStoreCoordinator addPersistentStoreWithType:NSSQLiteStoreType
    configuration:nil URL:storeURL options:options error:&error];
```

### Examples
```objc
// Enable lightweight migration
NSDictionary *options = @{
    NSMigratePersistentStoresAutomaticallyOption: @YES,
    NSInferMappingModelAutomaticallyOption: @YES
};
```
