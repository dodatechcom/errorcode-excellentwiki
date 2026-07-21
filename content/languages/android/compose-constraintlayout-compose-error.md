---
title: "Compose ConstraintLayout Error"
description: "Fix Compose ConstraintLayout usage and constraint errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ConstraintLayout in Compose does not constrain elements correctly

## Common Causes

- Constraint references not created properly
- Constraints not connecting elements
- Chain not working as expected in Compose
- Guideline not positioned correctly

## Fixes

- Use createRefs() to create references
- Connect constraints with linkTo
- Use createHorizontalChain/createVerticalChain
- Use guideline with percentage or dp

## Code Example

```kotlin
ConstraintLayout(modifier = Modifier.fillMaxSize()) {
    val (title, subtitle, button) = createRefs()

    Text(
        text = "Title",
        modifier = Modifier.constrainAs(title) {
            top.linkTo(parent.top, margin = 16.dp)
            start.linkTo(parent.start)
            end.linkTo(parent.end)
        }
    )

    Text(
        text = "Subtitle",
        modifier = Modifier.constrainAs(subtitle) {
            top.linkTo(title.bottom, margin = 8.dp)
            start.linkTo(parent.start)
        }
    )

    Button(
        onClick = { /* click */ },
        modifier = Modifier.constrainAs(button) {
            top.linkTo(subtitle.bottom, margin = 16.dp)
            centerHorizontallyTo(parent)
        }
    ) {
        Text("Click me")
    }
}
```

# createRefs(): create constraint references
# constrainAs: apply constraints to element
# linkTo: connect elements
# centerHorizontallyTo/centerVerticallyTo
