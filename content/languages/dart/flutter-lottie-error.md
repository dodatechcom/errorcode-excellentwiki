---
title: "[Solution] Flutter Lottie Error — animation, composition, repeat, frame rate"
description: "Fix Flutter Lottie animation errors from composition loading, repeat configuration, frame rate, and asset issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 177
---

Lottie errors occur when animation files fail to load, composition is null, repeat behavior is misconfigured, or frame rate causes performance issues.

## Common Causes

1. Lottie JSON file not included in assets.
2. `LottieComposition` being null (invalid JSON).
3. `repeat` not working as expected.
4. High frame rate causing jank on low-end devices.
5. `Lottie.network` failing due to CORS or network issues.

## How to Fix It

**Solution 1: Load Lottie from assets**

```dart
import 'package:flutter/material.dart';
// import 'package:lottie/lottie.dart';

// Lottie.asset(
//   'assets/animations/loading.json',
//   width: 200,
//   height: 200,
//   fit: BoxFit.fill,
// );

// pubspec.yaml:
// flutter:
//   assets:
//     - assets/animations/
```

**Solution 2: Handle composition loading**

```dart
import 'package:flutter/material.dart';
// import 'package:lottie/lottie.dart';

Widget buildLottieAnimation() {
  return Lottie.asset(
    'assets/animations/loading.json',
    errorBuilder: (context, error, stackTrace) {
      return Container(
        width: 100,
        height: 100,
        child: Icon(Icons.animation, size: 48),
      );
    },
  );
}
```

**Solution 3: Control playback**

```dart
import 'package:flutter/material.dart';
// import 'package:lottie/lottie.dart';

class LottiePlayer extends StatefulWidget {
  @override
  State<LottiePlayer> createState() => _LottiePlayerState();
}

class _LottiePlayerState extends State<LottiePlayer>
    with TickerProviderStateMixin {
  // late AnimationController _controller;
  
  @override
  void initState() {
    super.initState();
    // _controller = AnimationController(
    //   vsync: this,
    //   duration: Duration(seconds: 2),
    // );
  }
  
  @override
  void dispose() {
    // _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Lottie.asset(
        //   'assets/animations/animation.json',
        //   controller: _controller,
        //   onLoaded: (composition) {
        //     _controller.duration = composition.duration;
        //     _controller.forward();
        //   },
        // ),
        Row(
          children: [
            ElevatedButton(
              onPressed: () {}, // _controller.forward(),
              child: Text('Play'),
            ),
            ElevatedButton(
              onPressed: () {}, // _controller.stop(),
              child: Text('Pause'),
            ),
            ElevatedButton(
              onPressed: () {}, // _controller.reset(),
              child: Text('Reset'),
            ),
          ],
        ),
      ],
    );
  }
}
```

**Solution 4: Load from network with error handling**

```dart
import 'package:flutter/material.dart';
// import 'package:lottie/lottie.dart';

Widget loadFromNetwork() {
  return Lottie.network(
    'https://assets2.lottiefiles.com/packages/lf20_abc123.json',
    width: 200,
    height: 200,
    errorBuilder: (context, exception, stackTrace) {
      return Text('Failed to load animation');
    },
  );
}
```

**Solution 5: Optimize frame rate**

```dart
import 'package:flutter/material.dart';
// import 'package:lottie/lottie.dart';

Widget buildOptimizedLottie() {
  return Lottie.asset(
    'assets/animations/animation.json',
    frameRate: FrameRate.composition,
    // or FrameRate(30) for custom frame rate
  );
}
```

## Examples

Add `lottie: ^3.1.0` to your `pubspec.yaml` dependencies. Lottie files are JSON-based animations exported from Adobe After Effects via the Bodymovin plugin.

## Related Errors

- [Flutter Image Error](/languages/dart/flutter-image-error/)
- [Flutter SVG Error](/languages/dart/flutter-svg-error/)
- [Flutter Animation Controller Error](/languages/dart/flutter-animation-controller-error/)
