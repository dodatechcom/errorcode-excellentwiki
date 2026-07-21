---
title: "[Solution] Xcode Error: Resource Bundle Missing"
description: "Fix missing resource bundle errors in Xcode iOS projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Resource Bundle Missing

Resource bundle errors occur when your app cannot find resources at runtime because the bundle was not properly included in the build.

## Common Causes
- Resource bundle not added to Copy Bundle Resources
- Framework containing resources not included in the build
- Resource bundle target not built before main target
- Incorrect bundle path used in code

## How to Fix
1. Verify the resource bundle appears in Copy Bundle Resources build phase
2. Ensure the resource bundle target is listed as a dependency
3. Use Bundle.module for Swift Package Manager resources
4. Check the bundle path in code matches the actual structure

```swift
// For Swift Package Manager resources:
// In Package.swift, declare resources:
// .resource(bundle: "MyResources")

// Access in code:
// Bundle.module.url(forResource: "image", withExtension: "png")

// For framework resources:
// Bundle(for: type(of: self)).url(forResource: "image", withExtension: "png")
```

## Examples
```swift
// Example: Loading resources from a framework bundle
class ResourceManager {
    static let bundle = Bundle(for: ResourceManager.self)

    static func loadImage(named name: String) -> UIImage? {
        guard let url = bundle.url(forResource: name, withExtension: "png") else {
            return nil
        }
        return UIImage(contentsOfFile: url.path)
    }

    static func loadConfig() -> [String: Any]? {
        guard let url = bundle.url(forResource: "config", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any] else {
            return nil
        }
        return json
    }
}
```
