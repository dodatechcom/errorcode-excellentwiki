---
title: "[Solution] Swift AttributedString Error — Markdown & Attributes"
description: "Fix Swift AttributedString errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 124
---

`AttributedString` errors occur when Markdown parsing fails, attribute operations produce invalid results, or bridging between NSAttributedString and AttributedString breaks.

## Common Causes

```swift
// Invalid Markdown
let attrStr = try AttributedString(markdown: "[invalid**") // Throws

// Attribute span mismatch
var str = AttributedString("Hello")
str[str.startIndex..<str.endIndex].font = .body
// Font attribute set on wrong span
```

## How to Fix

**1. Parse Markdown safely**

```swift
do {
    let attrStr = try AttributedString(markdown: "Hello **world**")
    print(attrStr)
} catch {
    print("Markdown parse error: \(error)")
}
```

**2. Apply attributes to ranges**

```swift
var str = AttributedString("Hello World")
if let range = str.range(of: "World") {
    str[range].font = .boldSystemFont(ofSize: 18)
    str[range].foregroundColor = .blue
}
```

**3. Concatenate AttributedStrings**

```swift
var result = AttributedString("Hello ")
var world = AttributedString("World")
world.font = .boldSystemFont(ofSize: 16)
result.append(world)
```

**4. Bridging with NSAttributedString**

```swift
let nsString = NSAttributedString(string: "Hello", attributes: [
    .font: UIFont.boldSystemFont(ofSize: 16)
])
let attrStr = AttributedString(nsString)

let backToNS = NSAttributedString(attrStr)
```

**5. Custom attributes**

```swift
struct CustomAttribute: AttributedStringKey {
    typealias Value = String
    static let name = "customAttribute"
}

var str = AttributedString("Hello")
str.customAttribute = "value"
```

## Examples

Rich text construction:
```swift
func makeRichText(title: String, body: String) -> AttributedString {
    var result = AttributedString()
    
    var titleAttr = AttributedString(title)
    titleAttr.font = .largeTitle
    result.append(titleAttr)
    
    result.append(AttributedString("\n\n"))
    
    var bodyAttr = AttributedString(body)
    bodyAttr.font = .body
    result.append(bodyAttr)
    
    return result
}
```

## Related Errors

- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
- [UIKit Auto Layout Error](/languages/swift/swift-autolayout-error)
