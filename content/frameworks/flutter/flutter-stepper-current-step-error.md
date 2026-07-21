---
title: "[Solution] Flutter Stepper Current Step Error"
description: "Fix Flutter Stepper errors when the current step index is out of bounds or step navigation fails."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Stepper current step error in Flutter occurs when the `currentStep` index is invalid (negative or >= steps length), or when step navigation (next/back) fails because the validation callback prevents progression.

## Common Causes

- `currentStep` exceeds the number of steps
- `onStepContinue` does not increment `currentStep`
- Step validation returns `false` blocking navigation
- Steps list modified while stepper is active
- `onStepTapped` allows jumping to future steps without validation

## How to Fix

1. Validate currentStep bounds:

```dart
int _currentStep = 0;
final int _totalSteps = 3;

void _onStepContinue() {
  if (_currentStep < _totalSteps - 1) {
    setState(() => _currentStep++);
  }
}

void _onStepBack() {
  if (_currentStep > 0) {
    setState(() => _currentStep--);
  }
}
```

2. Implement step validation:

```dart
Stepper(
  currentStep: _currentStep,
  onStepContinue: () {
    if (_validateCurrentStep()) {
      if (_currentStep < steps.length - 1) {
        setState(() => _currentStep++);
      }
    }
  },
  onStepBack: () {
    if (_currentStep > 0) {
      setState(() => _currentStep--);
    }
  },
  onStepTapped: (index) {
    // Only allow tapping completed or current steps
    if (index <= _currentStep) {
      setState(() => _currentStep = index);
    }
  },
  steps: [
    Step(
      title: const Text('Personal Info'),
      content: TextField(decoration: InputDecoration(labelText: 'Name')),
      isActive: _currentStep >= 0,
      state: _currentStep > 0 ? StepState.complete : StepState.indexed,
    ),
    Step(
      title: const Text('Address'),
      content: TextField(decoration: InputDecoration(labelText: 'Street')),
      isActive: _currentStep >= 1,
      state: _currentStep > 1 ? StepState.complete : StepState.indexed,
    ),
    Step(
      title: const Text('Confirm'),
      content: const Text('Review your information'),
      isActive: _currentStep >= 2,
    ),
  ],
);
```

## Examples

```dart
// Bug: currentStep set to 5 but only 3 steps exist
Stepper(
  currentStep: 5, // Out of bounds
  steps: [Step(...), Step(...), Step(...)],
);

// Fixed: clamp the value
Stepper(
  currentStep: _currentStep.clamp(0, steps.length - 1),
  steps: steps,
);
```

```text
RangeError (index): Invalid value: Valid value range is 0-2
```
