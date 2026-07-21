---
title: "[Solution] SwiftUI TabView Badge Error"
description: "Fix SwiftUI TabView badge configuration and display errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI TabView Badge Error

Tab badges fail to display when the badge modifier is not applied correctly, when the tab identifier does not match, or when the badge value conflicts with system badges.

## Common Causes
- Badge modifier not applied to the correct tab
- Tab identifier mismatch between Tab and badge
- Badge value set to nil or empty string
- System badge overriding custom badge

## How to Fix
1. Apply badge modifier to the content inside Tab
2. Ensure tab tags match between Tab and badge
3. Use non-nil badge values
4. Remove system badge when using custom badge

```swift
// Tab with badge:
Tab("Home", systemImage: "house", tag: 0) {
    HomeView()
        .badge(unreadCount)
}

Tab("Messages", systemImage: "message", tag: 1) {
    MessagesView()
        .badge("New")
}
```

## Examples
```swift
// Tab view with dynamic badges:
TabView(selection: $selectedTab) {
    HomeView()
        .tabItem { Label("Home", systemImage: "house") }
        .badge(homeBadgeCount)
        .tag(0)

    SettingsView()
        .tabItem { Label("Settings", systemImage: "gear") }
        .tag(1)
}

// Remove badge:
HomeView().badge(nil) // or .badge(0)
```
