---
title: "[Solution] Flutter Image Error — network/asset/file loading, errorBuilder, frameBuilder"
description: "Fix Flutter Image errors from loading failures, error builder configuration, asset not found, and frame builder issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 175
---

Image errors occur when images fail to load, assets are not found, network images timeout, or error builders are not configured.

## Common Causes

1. `Image.asset` referencing a non-existent asset path.
2. `Image.network` URL returning a 404 or invalid image data.
3. Missing `errorBuilder` for graceful error handling.
4. `Image.file` pointing to a non-existent file.
5. Image loading in ListView without caching.

## How to Fix It

**Solution 1: Load images with error handling**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Image.network(
    'https://example.com/image.jpg',
    errorBuilder: (context, error, stackTrace) {
      return Container(
        color: Colors.grey[300],
        child: Icon(Icons.broken_image, size: 48),
      );
    },
    loadingBuilder: (context, child, loadingProgress) {
      if (loadingProgress == null) return child;
      return Center(
        child: CircularProgressIndicator(
          value: loadingProgress.expectedTotalBytes != null
              ? loadingProgress.cumulativeBytesLoaded /
                  loadingProgress.expectedTotalBytes!
              : null,
        ),
      );
    },
  );
}
```

**Solution 2: Use asset images safely**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Image.asset(
    'assets/images/logo.png',
    errorBuilder: (context, error, stackTrace) {
      return Text('Asset not found');
    },
    width: 200,
    height: 200,
    fit: BoxFit.cover,
  );
}
```

**Solution 3: Use frameBuilder for transitions**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Image.network(
    'https://example.com/photo.jpg',
    frameBuilder: (context, child, frame, wasSynchronouslyLoaded) {
      if (wasSynchronouslyLoaded) return child;
      return AnimatedOpacity(
        opacity: frame == null ? 0 : 1,
        duration: Duration(milliseconds: 500),
        child: child,
      );
    },
    errorBuilder: (context, error, stackTrace) {
      return Icon(Icons.error);
    },
  );
}
```

**Solution 4: Load file images**

```dart
import 'dart:io';
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Image.file(
    File('/path/to/image.jpg'),
    errorBuilder: (context, error, stackTrace) {
      return Container(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            Icon(Icons.error_outline, size: 48, color: Colors.red),
            Text('Failed to load image'),
          ],
        ),
      );
    },
  );
}
```

**Solution 5: Use CachedNetworkImage for caching**

```dart
import 'package:flutter/material.dart';
// import 'package:cached_network_image/cached_network_image.dart';

// With cached_network_image package:
Widget buildCachedImage(String url) {
  return CachedNetworkImage(
    imageUrl: url,
    placeholder: (context, url) => CircularProgressIndicator(),
    errorWidget: (context, url, error) => Icon(Icons.error),
    fit: BoxFit.cover,
  );
}

// Without the package:
Widget buildBasicImage(String url) {
  return Image.network(
    url,
    fit: BoxFit.cover,
    errorBuilder: (context, error, stackTrace) => Icon(Icons.error),
  );
}
```

## Examples

`Image.network` requires internet access. On Android, add `<uses-permission android:name="android.permission.INTERNET"/>` to `AndroidManifest.xml`. Images are cached by the default Flutter image cache.

## Related Errors

- [Flutter SVG Error](/languages/dart/flutter-svg-error/)
- [Flutter Lottie Error](/languages/dart/flutter-lottie-error/)
- [Flutter File Open Error](/languages/dart/dart-file-open-error/)
