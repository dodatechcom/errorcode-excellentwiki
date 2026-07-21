---
title: "[Solution] SwiftUI PhotosPicker Error"
description: "Fix SwiftUI PhotosPicker configuration and selection errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI PhotosPicker Error

PhotosPicker fails when the selection binding type does not match the transferable type, when photo library access is denied, or when the picker configuration is incorrect.

## Common Causes
- Selection binding type mismatch with PhotosPickerItem
- Photo library access denied by user
- Missing privacy description for photo library
- Picker presentation conflicts with other sheets

## How to Fix
1. Use correct binding type with PhotosPickerItem
2. Handle photo library authorization status
3. Add NSPhotoLibraryUsageDescription to Info.plist
4. Ensure no conflicting sheet presentations

```swift
// PhotosPicker setup:
PhotosPicker(selection: $selectedItems, matching: .images) {
    Label("Select Photo", systemImage: "photo")
}

// Handle selection:\.onChange(of: selectedItems) { newSelection in
    Task {
        for item in newSelection {
            if let data = try? await item.loadTransferable(type: Data.self) {
                imageData = data
            }
        }
    }
}
```

## Examples
```swift
// PhotosPicker with multiple selection:
@State private var selectedItems: [PhotosPickerItem] = []
@State private var images: [UIImage] = []

PhotosPicker(selection: $selectedItems, maxSelectionCount: 5, matching: .images) {
    Text("Choose Photos")
}
.onChange(of: selectedItems) { items in
    Task {
        images.removeAll()
        for item in items {
            if let data = try? await item.loadTransferable(type: Data.self),
               let uiImage = UIImage(data: data) {
                images.append(uiImage)
            }
        }
    }
}
```
