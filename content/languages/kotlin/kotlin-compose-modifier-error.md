---
title: "[Solution] Kotlin Compose Modifier Order and Constraint Conflict"
description: "Fix Compose modifier order errors and size/constraint conflicts. Learn correct modifier chaining order and size constraints."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1022
---

## What This Error Means

Modifier order errors cause unexpected layout behavior because Compose applies modifiers from left to right (outermost to innermost). Wrong ordering produces different sizes, positions, or clipping than intended.

## Common Causes

- `padding` before `size` instead of after
- `clip` before `background` (background won't be clipped)
- Multiple conflicting size modifiers (`fillMaxWidth` + `width(100.dp)`)
- `clickable` after `alpha` (clickable area doesn't match visual)

```kotlin
// WRONG: Background won't be clipped
Modifier
    .background(RoundedCornerShape(8.dp))
    .clip(RoundedCornerShape(8.dp))  // Too late

// WRONG: Click area extends beyond visual
Modifier
    .alpha(0.5f)
    .clickable { onClick() }  // Full area clickable
```

## How to Fix

**1. Apply clip before background**

```kotlin
// CORRECT: Clip first, then background
Modifier
    .clip(RoundedCornerShape(8.dp))
    .background(Color.Blue)
```

**2. Place clickable before visual modifiers**

```kotlin
// CORRECT: Clickable is visual-outermost
Modifier
    .clickable { onClick() }
    .alpha(0.5f)
```

**3. Use fixed size instead of conflicting modifiers**

```kotlin
// WRONG: Conflict
Modifier.fillMaxWidth().width(100.dp)

// CORRECT: Choose one
Modifier.width(100.dp)
```

**4. Follow standard modifier order convention**

```kotlin
Modifier
    .padding(16.dp)          // 1. Outer padding
    .clip(RoundedCornerShape(8.dp))  // 2. Clip shape
    .background(Color.White) // 3. Background
    .padding(8.dp)           // 4. Inner padding
    .fillMaxWidth()          // 5. Size
```

## Examples

```kotlin
// Example 1: Card modifier order
@Composable
fun StyledCard(content: @Composable () -> Unit) {
    Box(
        Modifier
            .padding(16.dp)
            .clip(RoundedCornerShape(12.dp))
            .background(MaterialTheme.colorScheme.surface)
            .shadow(4.dp, RoundedCornerShape(12.dp))
            .padding(16.dp)
    ) { content() }
}

// Example 2: ConstraintLayout for complex layouts
@Composable
fun ConstraintLayout() {
    ConstraintLayout(Modifier.fillMaxSize()) {
        val (button, text) = createRefs()
        Text("Hello", Modifier.constrainAs(text) {
            top.linkTo(parent.top, margin = 16.dp)
            centerHorizontallyTo(parent)
        })
        Button(onClick = {}, Modifier.constrainAs(button) {
            top.linkTo(text.bottom, margin = 16.dp)
        }) { Text("Click") }
    }
}

// Example 3: Weight in Row/Column
Row(Modifier.fillMaxWidth()) {
    Box(Modifier.weight(1f).background(Color.Red))
    Box(Modifier.weight(2f).background(Color.Blue))
}
```

## Related Errors

- [Compose recomposition](kotlin-compose-recomposition) — excessive recomposition
- [Compose side effect](kotlin-compose-side-effect) — effect lifecycle
- [Compose preview error](kotlin-compose-preview-error) — preview rendering
