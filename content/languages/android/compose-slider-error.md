---
title: "Slider Configuration Error"
description: "Fix Material 3 Slider and RangeSlider configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Slider does not display value correctly or range selection fails

## Common Causes

- Slider value not updating
- RangeSlider thumbs not independently draggable
- Slider steps not creating discrete positions
- Slider value display not showing current value

## Fixes

- Use onValueChange to update state
- Track start and end values for RangeSlider
- Set steps for discrete slider positions
- Display value with Text outside slider

## Code Example

```kotlin
var sliderValue by remember { mutableStateOf(0.5f) }

Column {
    Text("Value: ${sliderValue.toInt()}")
    Slider(
        value = sliderValue,
        onValueChange = { sliderValue = it },
        valueRange = 0f..100f,
        steps = 9,  // 10 positions
        modifier = Modifier.fillMaxWidth()
    )
}

// Range Slider
var range by remember { mutableStateOf(0.3f..0.7f) }

RangeSlider(
    value = range,
    onValueChange = { range = it },
    valueRange = 0f..1f,
    modifier = Modifier.fillMaxWidth()
)
```

# Slider: single value selection
# RangeSlider: range selection with two thumbs
# steps: discrete positions between min/max
# valueRange: min to max values
