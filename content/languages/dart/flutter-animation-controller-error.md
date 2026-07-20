---
title: "[Solution] Flutter AnimationController Error — forward, reverse, duration"
description: "Fix Flutter AnimationController errors from missing duration, forward/reverse misuse, and dispose issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 157
---

AnimationController errors occur when controllers are not initialized with a duration, used after disposal, or forward/reverse is called incorrectly.

## Common Causes

1. `AnimationController` created without `duration` parameter.
2. Calling `forward()` on a disposed controller.
3. Not implementing `TickerProviderStateMixin` for vsync.
4. Calling `reverse()` when the animation is already at lowerBound.
5. Not disposing the controller, causing memory leaks.

## How to Fix It

**Solution 1: Create AnimationController with proper setup**

```dart
import 'package:flutter/material.dart';

class FadeWidget extends StatefulWidget {
  @override
  State<FadeWidget> createState() => _FadeWidgetState();
}

class _FadeWidgetState extends State<FadeWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    );
    _animation = CurvedAnimation(
      parent: _controller,
      curve: Curves.easeIn,
    );
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _animation,
      child: Text('Hello Animation!'),
    );
  }
}
```

**Solution 2: Control forward and reverse**

```dart
import 'package:flutter/material.dart';

class SlideAnimation extends StatefulWidget {
  @override
  State<SlideAnimation> createState() => _SlideAnimationState();
}

class _SlideAnimationState extends State<SlideAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(milliseconds: 500),
      vsync: this,
    );
  }
  
  void _toggleAnimation() {
    if (_controller.isCompleted) {
      _controller.reverse();
    } else {
      _controller.forward();
    }
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return SlideTransition(
      position: Tween<Offset>(
        begin: Offset.zero,
        end: Offset(1.0, 0.0),
      ).animate(_controller),
      child: ElevatedButton(
        onPressed: _toggleAnimation,
        child: Text('Toggle'),
      ),
    );
  }
}
```

**Solution 3: Use repeat for looping animations**

```dart
import 'package:flutter/material.dart';

class PulseAnimation extends StatefulWidget {
  @override
  State<PulseAnimation> createState() => _PulseAnimationState();
}

class _PulseAnimationState extends State<PulseAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    )..repeat(reverse: true);
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ScaleTransition(
      scale: Tween<double>(begin: 0.8, end: 1.2).animate(_controller),
      child: Container(
        width: 100,
        height: 100,
        color: Colors.blue,
      ),
    );
  }
}
```

**Solution 4: Chain animations with AnimationController**

```dart
import 'package:flutter/material.dart';

class ChainedAnimation extends StatefulWidget {
  @override
  State<ChainedAnimation> createState() => _ChainedAnimationState();
}

class _ChainedAnimationState extends State<ChainedAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 2),
      vsync: this,
    );
    
    _controller.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        _controller.reverse();
      } else if (status == AnimationStatus.dismissed) {
        _controller.forward();
      }
    });
    
    _controller.forward();
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
        return Transform.rotate(
          angle: _controller.value * 3.14159,
          child: child,
        );
      },
      child: Icon(Icons.refresh, size: 64),
    );
  }
}
```

**Solution 5: Safe disposal pattern**

```dart
import 'package:flutter/material.dart';

class SafeAnimation extends StatefulWidget {
  @override
  State<SafeAnimation> createState() => _SafeAnimationState();
}

class _SafeAnimationState extends State<SafeAnimation>
    with SingleTickerProviderStateMixin {
  AnimationController? _controller;
  bool _disposed = false;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    );
  }
  
  @override
  void dispose() {
    _disposed = true;
    _controller?.dispose();
    _controller = null;
    super.dispose();
  }
  
  void _animate() {
    if (!_disposed && _controller != null) {
      _controller!.forward();
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _animate,
      child: Text('Animate'),
    );
  }
}
```

## Examples

`AnimationController` requires a `TickerProvider` for vsync. Use `SingleTickerProviderStateMixin` for one controller, or `TickerProviderStateMixin` for multiple controllers in the same state.

## Related Errors

- [Flutter Animation Ticker Error](/languages/dart/flutter-animation-ticker-error/)
- [Flutter Custom Paint Error](/languages/dart/flutter-custom-paint-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
