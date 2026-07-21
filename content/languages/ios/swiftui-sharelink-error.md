---
title: "[Solution] SwiftUI ShareLink Error"
description: "Fix SwiftUI ShareLink sharing configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI ShareLink Error

ShareLink fails when the share content is not properly configured, when the item does not conform to Transferable, or when sharing services are unavailable.

## Common Causes
- Item does not conform to Transferable protocol
- Share content type not supported by sharing services
- Item provider fails to load data
- Sharing sheet not presented due to view lifecycle

## How to Fix
1. Ensure item conforms to Transferable
2. Support multiple content types
3. Handle item provider loading errors
4. Present ShareLink from visible view

```swift
// ShareLink with text:
ShareLink(item: "Check out this content!")

// ShareLink with custom transferable:
struct ShareableItem: Transferable {
    let text: String
    static var transferRepresentation: some TransferRepresentation {
        ExportedContentType(text) { item in
            Data(item.text.utf8)
        }
    }
}
```

## Examples
```swift
// ShareLink with image:
ShareLink(item: image, preview: SharePreview("Photo", image: image))

// ShareLink with multiple items:
ShareLink(items: [image, URL(string: "https://example.com")!])
```
