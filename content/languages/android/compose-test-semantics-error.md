---
title: "Compose Test Semantics Error"
description: "Fix Compose test semantics tree traversal and node matching errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose UI tests fail to find nodes or match semantics properties correctly

## Common Causes

- Node not found by text or content description
- Test matcher too broad matching multiple nodes
- Semantics properties not matching test expectations
- Test failing intermittently because of async content

## Fixes

- Use specific semantic matchers: onNodeWithText, onNodeWithTag
- Add testTag to unique composables
- Use semantically { } for custom semantics
- Use waitUntil or waitUntilNodeCount for async content

## Code Example

```kotlin
@Composable
fun UserCard(user: User) {
    Card(
        modifier = Modifier.testTag("user_card_${user.id}")
    ) {
        Text(text = user.name)
        Text(text = user.email)
    }
}

// Test:
composeTestRule.onNodeWithTag("user_card_123")
    .assertExists()
    .performClick()

// Multiple matches:
composeTestRule.onAllNodesWithText("Item")
    .assertCountEquals(5)
```

# testTag: unique identifier for testing
# onNodeWithTag: find by test tag
# onAllNodesWithText: find all matching nodes
# waitUntil: wait for async content
