---
title: "Badge Display Error"
description: "Fix Material 3 Badge and progress badge display errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Badge does not show correct count or disappears unexpectedly

## Common Causes

- Badge not visible when count is zero
- Badge overflow not showing correctly
- Badge position not aligned with icon
- Badge color not matching theme

## Fixes

- Show badge only when count > 0
- Use Badge with content for custom display
- Position badge relative to parent icon
- Use BadgeDefaults for theme colors

## Code Example

```kotlin
// Badge on icon
BadgedBox(
    badge = {
        if (notificationCount > 0) {
            Badge {
                Text(if (notificationCount > 99) "99+" else "$notificationCount")
            }
        }
    }
) {
    Icon(Icons.Default.Notifications, null)
}

// Badge without count (dot):
BadgedBox(
    badge = { Badge() }
) {
    Icon(Icons.Default.Mail, null)
}
```

# Badge: notification count indicator
# Badge(): dot indicator (no count)
# Badge { Text("5") }: count indicator
# BadgedBox: positions badge on content
