---
title: "[Solution] SwiftUI NavigationPath Codable Error"
description: "Fix SwiftUI NavigationPath encoding and decoding errors for state restoration."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI NavigationPath Codable Error

NavigationPath Codable conformance fails when the path contains types that are not Codable, when encoding fails, or when decoding encounters unknown types.

## Common Causes
- Path values do not conform to Codable
- Type information lost during encoding
- Decoding fails with unknown type identifier
- Path contains values from different modules

## How to Fix
1. Ensure all types appended to NavigationPath conform to Codable
2. Use stable type identifiers
3. Handle decoding errors gracefully
4. Save and restore path state properly

```swift
// NavigationPath with Codable types:
struct Route: Hashable, Codable {
    let id: UUID
    let screen: String
}

@State private var path = NavigationPath()

// Encode path:
let data = try? JSONEncoder().encode(path.codable)

// Decode path:
if let data = data, let codable = try? JSONDecoder().decode(NavigationPath.CodableRepresentation.self, from: data) {
    path = NavigationPath(codable)
}
```

## Examples
```swift
// State restoration:
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List {
                ForEach(items) { item in
                    NavigationLink(item.name, value: item)
                }
            }
            .navigationDestination(for: Item.self) { item in
                ItemDetail(item: item)
            }
        }
        .onAppear { restorePath() }
        .onDisappear { savePath() }
    }

    func savePath() {
        guard let representation = path.codable else { return }
        if let data = try? JSONEncoder().encode(representation) {
            UserDefaults.standard.set(data, forKey: "navPath")
        }
    }
}
```
