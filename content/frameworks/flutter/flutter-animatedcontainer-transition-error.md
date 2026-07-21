---
title: "[Solution] Flutter AnimatedContainer Transition Error"
description: "Fix Flutter AnimatedContainer errors when animations do not run or properties snap without transitioning."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An AnimatedContainer transition error in Flutter occurs when the container snaps to new properties instead of animating smoothly, typically because the animated properties are not changed between builds or the duration is zero.

## Common Causes

- Duration set to `Duration.zero` causing instant snap
- Properties changed in the same build frame as creation
- Animated property (color, size) not actually changing between builds
- `curve` parameter causes unexpected acceleration
- `AnimatedContainer` used where `AnimatedWidget` or `AnimationController` is needed

## How to Fix

1. Ensure properties actually change between builds:

```dart
class _AnimatedBoxState extends State<AnimatedBox> {
  bool _expanded = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => setState(() => _expanded = !_expanded),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
        width: _expanded ? 200 : 100,
        height: _expanded ? 200 : 100,
        color: _expanded ? Colors.blue : Colors.red,
        child: Center(
          child: Text(_expanded ? 'Expanded' : 'Tap'),
        ),
      ),
    );
  }
}
```

2. Animate multiple properties simultaneously:

```dart
AnimatedContainer(
  duration: const Duration(milliseconds: 400),
  curve: Curves.easeOutCubic,
  width: _isExpanded ? 300 : 150,
  height: _isExpanded ? 200 : 100,
  decoration: BoxDecoration(
    color: _isExpanded ? Colors.blue.shade100 : Colors.grey.shade200,
    borderRadius: BorderRadius.circular(_isExpanded ? 16 : 4),
    boxShadow: [
      BoxShadow(
        color: _isExpanded ? Colors.black26 : Colors.transparent,
        blurRadius: _isExpanded ? 8 : 0,
      ),
    ],
  ),
  child: const Center(child: Text('Animated')),
);
```

3. Use AnimatedContainer for loading states:

```dart
bool _isLoading = false;

AnimatedContainer(
  duration: const Duration(milliseconds: 200),
  height: _isLoading ? 60 : 48,
  child: ElevatedButton(
    onPressed: () {
      setState(() => _isLoading = true);
      submitData().then((_) => setState(() => _isLoading = false));
    },
    child: _isLoading
      ? const SizedBox(
          width: 24,
          height: 24,
          child: CircularProgressIndicator(strokeWidth: 2),
        )
      : const Text('Submit'),
  ),
);
```

## Examples

```dart
// Bug: width and height always the same
AnimatedContainer(
  duration: Duration(milliseconds: 300),
  width: 100, // Never changes -- no animation
  height: 100, // Never changes
  child: Text('No animation'),
);

// Fixed: properties change on state update
AnimatedContainer(
  duration: Duration(milliseconds: 300),
  width: _expanded ? 200 : 100,
  height: _expanded ? 200 : 100,
  child: Text(_expanded ? 'Big' : 'Small'),
);
```

```text
AnimatedContainer requires different values to animate between builds
```
