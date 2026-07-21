---
title: "[Solution] Flutter Image Cache Error"
description: "Fix Flutter image cache errors when cached images fail to load, display stale data, or cause memory issues."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An image cache error in Flutter occurs when `Image.network` or `CachedNetworkImage` serves stale or broken images, or when the image cache grows too large and causes out-of-memory errors.

## Common Causes

- Network images not reloaded when the URL changes
- Image cache not cleared after user logout
- `MemoryCache` fills up and evicts frequently used images
- Cache key collisions between different image sizes
- No placeholder shown while image loads from cache

## How to Fix

1. Clear image cache on logout:

```dart
void logout() {
  imageCache.clear();
  imageCache.clearLiveImages();
  Navigator.pushReplacement(
    context,
    MaterialPageRoute(builder: (_) => LoginScreen()),
  );
}
```

2. Use cache-busting for updated images:

```dart
Image.network(
  '${imageUrl}?v=${DateTime.now().millisecondsSinceEpoch}',
  fit: BoxFit.cover,
  errorBuilder: (context, error, stackTrace) {
    return const Icon(Icons.broken_image);
  },
);
```

3. Configure cache limits:

```dart
import 'package:flutter_cache_manager/flutter_cache_manager.dart';

final customCacheManager = CacheManager(
  Config(
    'customCache',
    maxNrOfCacheObjects: 100,
    stalePeriod: const Duration(days: 7),
  ),
);

CachedNetworkImage(
  imageUrl: url,
  cacheManager: customCacheManager,
  placeholder: (context, url) => const CircularProgressIndicator(),
  errorWidget: (context, url, error) => const Icon(Icons.error),
);
```

## Examples

```dart
// Bug: image URL updated but old image cached
Image.network('https://example.com/avatar?v=1');
// Later
Image.network('https://example.com/avatar?v=2'); // Shows v1 from cache

// Fixed: use unique key
Image.network(
  'https://example.com/avatar?v=$version',
  key: ValueKey('avatar_$version'),
);
```

```text
ImageCodecException: Failed to decode image
```
