---
title: "[Solution] SwiftUI @Observable Class Error"
description: "Fix SwiftUI @Observable class macro and observation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Observable Class Error

Observable class errors occur when the class is not properly marked with @Observable, when properties are not properly observed, or when the observation does not work across views.

## Common Causes
- Class not marked with @Observable
- Properties not observed
- Observation not working
- Conformance issues

## How to Fix
1. Mark class with @Observable
2. Ensure properties are observed
3. Verify observation works
4. Check conformance

```swift
@Observable class UserProfile {
    var name = ""
    var email = ""
    var isLoggedIn = false

    func login() {
        isLoggedIn = true
    }
}

struct ProfileView: View {
    var profile = UserProfile()

    var body: some View {
        Text(profile.name)
    }
}
```

## Examples
```swift
// With @Observable macro
@Observable class Settings {
    var darkMode = false
    var notifications = true
}

// Observation tracking
@Observable class DataSource {
    var items: [String] = []
    
    func load() async {
        items = try await fetchData()
    }
}
```
