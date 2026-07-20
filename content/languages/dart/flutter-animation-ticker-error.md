---
title: "[Solution] Flutter Animation Ticker Error — Ticker mode, dispose, vsync"
description: "Fix Flutter Ticker errors from Ticker mode issues, dispose misuse, vsync problems, and TickerProviderStateMixin."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 158
---

Ticker errors occur when `Ticker` is not properly managed, vsync is unavailable, or the ticker is not disposed.

## Common Causes

1. Using `TickerProviderStateMixin` without calling `dispose` on controllers.
2. Creating a `Ticker` without a vsync provider.
3. Not handling `TickerMode` changes when widgets go offscreen.
4. Using `vsync: this` in a `StatelessWidget`.
5. Multiple `AnimationController`s not all getting the same vsync.

## How to Fix It

**Solution 1: Use TickerProviderStateMixin correctly**

```dart
import 'package:flutter/material.dart';

class MultiAnimation extends StatefulWidget {
  @override
  State<MultiAnimation> createState() => _MultiAnimationState();
}

// Use TickerProviderStateMixin for multiple controllers
class _MultiAnimationState extends State<MultiAnimation>
    with TickerProviderStateMixin {
  late AnimationController _controller1;
  late AnimationController _controller2;
  
  @override
  void initState() {
    super.initState();
    _controller1 = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    );
    _controller2 = AnimationController(
      duration: Duration(seconds: 2),
      vsync: this,
    );
  }
  
  @override
  void dispose() {
    _controller1.dispose();
    _controller2.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ScaleTransition(
          scale: Tween<double>(begin: 0, end: 1).animate(_controller1),
          child: Text('Scale'),
        ),
        RotationTransition(
          turns: Tween<double>(begin: 0, end: 1).animate(_controller2),
          child: Text('Rotate'),
        ),
      ],
    );
  }
}
```

**Solution 2: Handle TickerMode changes**

```dart
import 'package:flutter/material.dart';

class TickerAwareWidget extends StatefulWidget {
  @override
  State<TickerAwareWidget> createState() => _TickerAwareWidgetState();
}

class _TickerAwareWidgetState extends State<TickerAwareWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    )..repeat();
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return Opacity(
          opacity: _controller.value,
          child: child,
        );
      },
      child: Text('Pulsing'),
    );
  }
}
```

**Solution 3: Create standalone Ticker**

```dart
import 'package:flutter/material.dart';
import 'dart:async';

class StandaloneTickerDemo extends StatefulWidget {
  @override
  State<StandaloneTickerDemo> createState() => _StandaloneTickerDemoState();
}

class _StandaloneTickerDemoState extends State<StandaloneTickerDemo> {
  Ticker? _ticker;
  int _tickCount = 0;
  
  @override
  void initState() {
    super.initState();
    _ticker = Ticker((Duration elapsed) {
      setState(() => _tickCount++);
    });
    _ticker!.start();
  }
  
  @override
  void dispose() {
    _ticker?.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Text('Ticks: $_tickCount');
  }
}
```

**Solution 4: Pause and resume tickers**

```dart
import 'package:flutter/material.dart';

class PauseableAnimation extends StatefulWidget {
  @override
  State<PauseableAnimation> createState() => _PauseableAnimationState();
}

class _PauseableAnimationState extends State<PauseableAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 5),
      vsync: this,
    )..forward();
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        LinearProgressIndicator(value: _controller.value),
        Row(
          children: [
            ElevatedButton(
              onPressed: () => _controller.forward(),
              child: Text('Play'),
            ),
            ElevatedButton(
              onPressed: () => _controller.stop(),
              child: Text('Pause'),
            ),
            ElevatedButton(
              onPressed: () => _controller.reset(),
              child: Text('Reset'),
            ),
          ],
        ),
      ],
    );
  }
}
```

**Solution 5: Use Ticker with custom intervals**

```dart
import 'package:flutter/material.dart';

class CountUpTimer extends StatefulWidget {
  @override
  State<CountUpTimer> createState() => _CountUpTimerState();
}

class _CountUpTimerState extends State<CountUpTimer>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(seconds: 60),
    )..forward();
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    int seconds = (_controller.value * 60).toInt();
    return Text('$seconds seconds elapsed');
  }
}
```

## Examples

A `Ticker` calls its callback on every frame (approximately 60 times per second). `AnimationController` wraps a `Ticker` and provides higher-level animation control. Always dispose controllers to stop the underlying ticker.

## Related Errors

- [Flutter Animation Controller Error](/languages/dart/flutter-animation-controller-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
- [Flutter Scroll Controller Error](/languages/dart/flutter-scroll-controller-error/)
