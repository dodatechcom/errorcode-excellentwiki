---
title: "[Solution] SwiftUI PhotosPicker Selection Binding Error"
description: "Fix SwiftUI PhotosPicker selection binding type mismatch errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI PhotosPicker Selection Binding Error

Selection binding type mismatch occurs when the PhotosPicker selection binding does not match PhotosPickerItem type, or when the selection array type is incorrect.

## Common Causes
- Selection binding not using [PhotosPickerItem]
- Single item binding used for multi-select
- Binding type not matching PhotosPickerItem
- Selection not cleared after processing

## How to Fix
1. Use [PhotosPickerItem] binding for multi-select
2. Use PhotosPickerItem? for single select
3. Clear selection after processing
4. Match binding type exactly with picker configuration

```swift
// Single selection:
@State private var selected: PhotosPickerItem?

PhotosPicker(selection: $selected, matching: .images) {
    Text("Select Photo")
}

// Multi selection:
@State private var selected: [PhotosPickerItem] = []

PhotosPicker(selection: $selected, maxSelectionCount: 5, matching: .images) {
    Text("Select Photos")
}
```

## Examples
```swift
// Process selection:
 PhotosPicker(selection: $selectedItems, maxSelectionCount: 3, matching: .images) {
     Label("Choose Photos", systemImage: "photo.on.rectangle")
 }
 .onChange(of: selectedItems) { items in
     Task {
         images.removeAll()
         for item in items {
             if let data = try? await item.loadTransferable(type: Data.self) {
                 if let uiImage = UIImage(data: data) {
                     images.append(uiImage)
                 }
             }
         }
         selectedItems.removeAll()
     }
 }
```
