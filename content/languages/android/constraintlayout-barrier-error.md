---
title: "ConstraintLayout Barrier Error"
description: "Fix ConstraintLayout barrier and guideline positioning errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ConstraintLayout barriers do not constrain views correctly

## Common Causes

- Barrier not referencing correct views
- Barrier direction not set properly
- Guideline percentage not working as expected
- Barrier not updated when views resize

## Fixes

- Set barrier references to correct view IDs
- Set app:barrierDirection to left/right/start/end/top/bottom
- Use app:layout_constraintGuide_percent for guidelines
- Barrier updates automatically with view changes

## Code Example

```kotlin
<!-- Guideline at 30% from left -->
<androidx.constraintlayout.widget.Guideline
    android:id="@+id/guideline"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    app:layout_constraintGuide_percent="0.3" />

<!-- Barrier after tallest view -->
<androidx.constraintlayout.widget.Barrier
    android:id="@+id/barrier"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:barrierDirection="end"
    app:constraint_referenced_ids="view1,view2" />

<!-- View constrained to barrier -->
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:layout_constraintStart_toEndOf="@+id/barrier" />
```

# Guidelines: fixed position (percent or dp)
# Barriers: dynamic position based on referenced views
# Barriers update when referenced views change size
