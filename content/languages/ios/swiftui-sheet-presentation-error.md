---
title: "[Solution] SwiftUI Sheet Presentation Error"
description: "Fix SwiftUI sheet not presenting or dismissing correctly in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Sheet Presentation Error

Sheets fail to present when the isPresented binding is incorrect, when the sheet content throws, or when presentation detents conflict with the sheet style.

## Common Causes
- Binding value not toggling correctly
- Sheet presented during animation
- Presentation detents incompatible with sheet style
- Multiple sheets trying to present simultaneously

## How to Fix
1. Ensure the binding properly reflects presentation state
2. Present sheets after animations complete
3. Use compatible detents with sheet presentation style
4. Manage sheet presentation queue properly

```swift
// Correct sheet presentation:
.sheet(isPresented: $showSheet) {
    ContentView()
}

// With detents (iOS 16+):
.sheet(isPresented: $showSheet) {
    ContentView()
        .presentationDetents([.medium, .large])
}
```

## Examples
```swift
// Sheet with custom presentation:
struct ContentView: View {
    @State private var showSheet = false
    @State private var selected: Item?

    var body: some View {
        Button("Show Sheet") { showSheet = true }
        .sheet(isPresented: $showSheet) {
            NavigationStack {
                SheetContent()
                    .toolbar {
                        ToolbarItem(placement: .navigationBarTrailing) {
                            Button("Done") { showSheet = false }
                        }
                    }
            }
        }
    }
}
```
