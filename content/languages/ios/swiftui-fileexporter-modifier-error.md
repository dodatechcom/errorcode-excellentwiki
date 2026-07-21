---
title: "[Solution] SwiftUI .fileExporter Modifier Error"
description: "Fix SwiftUI .fileExporter modifier document export errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .fileExporter Modifier Error

FileExporter modifier errors occur when the file exporter is not properly configured, when the file is not exported, or when the file conflicts with the app sandbox.

## Common Causes
- File exporter not configured
- File not exported
- File conflicts with sandbox
- File not matching design

## How to Fix
1. Configure file exporter properly
2. Ensure file is exported
3. Handle sandbox correctly
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showExporter = false
    @State private var exportData: Data?

    var body: some View {
        Button("Export File") { showExporter = true }
            .fileExporter(isPresented: $showExporter, document: MyDocument(data: exportData!), contentType: .plainText) { result in
                switch result {
                case .success:
                    print("Exported")
                case .failure(let error):
                    print(error)
                }
            }
    }
}
```

## Examples
```swift
// With custom name:
.fileExporter(isPresented: $showExporter, document: MyDocument(data: data), contentType: .plainText, defaultFilename: "document")

// Multiple files:
.fileExporter(isPresented: $showExporter, documents: [doc1, doc2], contentType: .plainText)
```
