---
title: "Espresso Test Error"
description: "Fix Espresso UI test errors for view interactions and assertions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Espresso tests fail to find views or interact with them correctly

## Common Causes

- View not found with onView matcher
- Timing issue with async data loading
- Incorrect view matcher for target element
- RecyclerView item not accessible with standard matcher

## Fixes

- Use correct ViewMatchers for target view
- Use IdlingResource for async operations
- Use onData for adapter views
- Use RecyclerViewActions for RecyclerView items

## Code Example

```kotlin
// Find view and click
onView(withId(R.id.submitButton))
    .perform(click())

// Type text
onView(withId(R.id.inputField))
    .perform(typeText("Hello"))

// Check text displayed
onView(withId(R.id.resultText))
    .check(matches(withText("Success")))

// RecyclerView item click
onView(withId(R.id.recyclerView))
    .perform(RecyclerViewActions.actionOnItemAtPosition<ViewHolder>(0, click()))
```

# ViewMatchers: byId, withText, withHint
# ViewActions: click, typeText, swipe
# ViewAssertions: matches, doesNotExist
# Use IdlingResource for async
