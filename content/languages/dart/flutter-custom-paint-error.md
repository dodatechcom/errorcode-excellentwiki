---
title: "[Solution] Flutter CustomPaint Error — shouldRepaint, Canvas size, Clip"
description: "Fix Flutter CustomPaint errors from shouldRepaint logic, Canvas sizing, and clipping issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 156
---

CustomPaint errors occur when `shouldRepaint` returns incorrect values, Canvas operations exceed bounds, or clipping is not configured properly.

## Common Causes

1. `shouldRepaint` always returning `true`, causing unnecessary repaints.
2. Painting outside the canvas bounds without clipping.
3. Canvas size being zero or unexpected.
4. Using `Paint` objects without proper initialization.
5. Not handling `semanticsBuilder` for accessibility.

## How to Fix It

**Solution 1: Implement shouldRepaint correctly**

```dart
import 'package:flutter/material.dart';

class CirclePainter extends CustomPainter {
  final double radius;
  final Color color;
  
  CirclePainter({required this.radius, required this.color});
  
  @override
  void paint(Canvas canvas, Size size) {
    Paint paint = Paint()
      ..color = color
      ..style = PaintingStyle.fill;
    
    canvas.drawCircle(
      Offset(size.width / 2, size.height / 2),
      radius,
      paint,
    );
  }
  
  @override
  bool shouldRepaint(CirclePainter oldDelegate) {
    return radius != oldDelegate.radius || color != oldDelegate.color;
  }
}

// Usage
Widget build(BuildContext context) {
  return CustomPaint(
    painter: CirclePainter(radius: 50, color: Colors.blue),
    size: Size(200, 200),
  );
}
```

**Solution 2: Clip canvas to prevent overflow**

```dart
import 'package:flutter/material.dart';

class ClipDemoPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    // Clip to bounds
    canvas.clipRect(Rect.fromLTWH(0, 0, size.width, size.height));
    
    Paint paint = Paint()..color = Colors.red;
    canvas.drawRect(
      Rect.fromLTWH(-10, -10, size.width + 20, size.height + 20),
      paint,
    );
  }
  
  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
```

**Solution 3: Draw dynamic content with CustomPainter**

```dart
import 'package:flutter/material.dart';

class BarChartPainter extends CustomPainter {
  final List<double> values;
  final Color barColor;
  
  BarChartPainter({required this.values, required this.barColor});
  
  @override
  void paint(Canvas canvas, Size size) {
    Paint paint = Paint()..color = barColor;
    
    double barWidth = size.width / values.length;
    double maxValue = values.reduce((a, b) => a > b ? a : b);
    
    for (int i = 0; i < values.length; i++) {
      double barHeight = (values[i] / maxValue) * size.height;
      double x = i * barWidth;
      double y = size.height - barHeight;
      
      canvas.drawRect(
        Rect.fromLTWH(x + 2, y, barWidth - 4, barHeight),
        paint,
      );
    }
  }
  
  @override
  bool shouldRepaint(BarChartPainter oldDelegate) {
    return values != oldDelegate.values || barColor != oldDelegate.barColor;
  }
}
```

**Solution 4: Use CustomPaint with child widget**

```dart
import 'package:flutter/material.dart';

class DecoratedBox extends StatelessWidget {
  final Widget child;
  
  const DecoratedBox({super.key, required this.child});
  
  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      painter: _BorderPainter(),
      child: Padding(
        padding: EdgeInsets.all(16),
        child: child,
      ),
    );
  }
}

class _BorderPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    Paint paint = Paint()
      ..color = Colors.blue
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2;
    
    canvas.drawRect(
      Rect.fromLTWH(0, 0, size.width, size.height),
      paint,
    );
  }
  
  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
```

**Solution 5: Handle canvas save/restore**

```dart
import 'package:flutter/material.dart';

class RotationPainter extends CustomPainter {
  final double angle;
  
  RotationPainter({required this.angle});
  
  @override
  void paint(Canvas canvas, Size size) {
    canvas.save();
    
    canvas.translate(size.width / 2, size.height / 2);
    canvas.rotate(angle);
    
    Paint paint = Paint()..color = Colors.green;
    canvas.drawRect(
      Rect.fromCenter(center: Offset.zero, width: 50, height: 50),
      paint,
    );
    
    canvas.restore();
  }
  
  @override
  bool shouldRepaint(RotationPainter oldDelegate) => angle != oldDelegate.angle;
}
```

## Examples

`CustomPainter` is used with `CustomPaint` widget. The `paint` method receives a `Canvas` and `Size`. Always use `canvas.save()` and `canvas.restore()` when applying transformations.

## Related Errors

- [Flutter Layout Builder Error](/languages/dart/flutter-layout-builder-error/)
- [Flutter Animation Controller Error](/languages/dart/flutter-animation-controller-error/)
- [Flutter Custom Scroll Error](/languages/dart/flutter-custom-scroll-error/)
