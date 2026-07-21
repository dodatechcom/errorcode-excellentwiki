---
title: "[Solution] SwiftUI .fileImporter Modifier Error"
description: "Fix SwiftUI .fileImporter modifier document import errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .fileImporter Modifier Error

FileImporter modifier errors occur when the file picker is not properly configured, when the file is not imported, or when the file conflicts with the app sandbox.

## Common Causes
- File picker not configured
- File not imported
- File conflicts with sandbox
- File not matching design

## How to Fix
1. Configure file picker properly
2. Ensure file is imported
3. Handle sandbox correctly
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showImporter = false

    var body: some View {
        Button("Import File") { showImporter = true }
            .fileImporter(isPresented: $showImporter, allowedContentTypes: [.plainText]) { result in
                switch result {
                case .success(let url):
                    print(url)
                case .failure(let error):
                    print(error)
                }
            }
    }
}
```

## Examples
```swift
// Multiple content types:
.fileImporter(isPresented: $showImporter, allowedContentTypes: [.plainText, .pdf, .image])

// With allowsMultipleSelection:
.fileImporter(isPresented: $showImporter, allowedContentTypes: [.plainText], allowsMultipleSelection: true)

// With custom title:
.fileImporter(isPresented: $showImporter, allowedContentTypes: [.plainText])
```
