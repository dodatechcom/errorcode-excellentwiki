---
title: "[Solution] SwiftUI @FocusState External Focus Control Error"
description: "Fix SwiftUI @FocusState external focus control and coordination errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState External Focus Control Error

External focus control errors occur when the focus is controlled from outside the view, when the external control conflicts with internal state, or when the control does not propagate properly.

## Common Causes
- External focus not controlled
- External control conflicts with state
- Control does not propagate
- Control not updating

## How to Fix
1. Control focus from outside properly
2. Ensure external control is compatible with state
3. Propagate control properly
4. Update control

```swift
struct ParentView: View {
    @State private var focusChild = false

    var body: some View {
        ChildView(focus: $focusChild)
        Button("Focus Child") { focusChild = true }
    }
}

struct ChildView: View {
    @Binding var focus: Bool
    @FocusState private var isFocused: Bool

    var body: some View {
        TextField("Enter", text: $text)
            .focused($isFocused)
            .onChange(of: focus) { newValue in
                isFocused = newValue
            }
    }
}
```

## Examples
```swift
// Parent controlling child focus:
@Binding var focus: Bool
@FocusState private var isFocused: Bool

.onChange(of: focus) { newValue in
    isFocused = newValue
}

// Sibling focus coordination:
@FocusState private var focusedField: Field?

// Pass to sibling view
SiblingView(focusedField: $focusedField)
```
