---
title: "[Solution] Dart URI Encode Error — encodeFull, encodeComponent, Query Parameters"
description: "Fix Dart URI encoding errors with encodeFull, encodeComponent, query parameters, and fragment handling."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 111
---

URI encoding errors occur when using the wrong encoding function, double-encoding values, or mishandling query parameters and fragments.

## Common Causes

1. Using `Uri.encodeFull` when `encodeComponent` is needed (or vice versa).
2. Double-encoding already-encoded values.
3. Manually building query strings instead of using `Uri` query parameters.
4. Encoding the entire URI instead of individual components.
5. Forgetting to encode non-ASCII characters in path segments.

## How to Fix It

**Solution 1: Understand the difference between encode methods**

```dart
import 'dart:io';

void main() {
  String raw = 'hello world&foo=bar';
  
  // encodeFull preserves / : @ ! $ & ' ( ) * + , ; =
  print(Uri.encodeFull(raw)); // hello%20world&foo=bar
  
  // encodeComponent encodes everything except letters, digits, - _ . ~
  print(Uri.encodeComponent(raw)); // hello%20world%26foo%3Dbar
}
```

**Solution 2: Use `Uri` class for proper construction**

```dart
void main() {
  Uri uri = Uri(
    scheme: 'https',
    host: 'example.com',
    path: '/search',
    queryParameters: {
      'q': 'dart programming',
      'page': '1',
    },
  );
  
  print(uri.toString()); // https://example.com/search?q=dart+programming&page=1
}
```

**Solution 3: Avoid double-encoding**

```dart
void main() {
  String alreadyEncoded = 'hello%20world';
  
  // Wrong: double encodes
  // String doubleEncoded = Uri.encodeComponent(alreadyEncoded);
  // Results in: hello%2520world
  
  // Correct: decode first, then encode, or use as-is
  String decoded = Uri.decodeComponent(alreadyEncoded);
  print(decoded); // hello world
  
  String reEncoded = Uri.encodeComponent(decoded);
  print(reEncoded); // hello%20world
}
```

**Solution 4: Handle fragments properly**

```dart
void main() {
  Uri uri = Uri.parse('https://example.com/page#section');
  print(uri.fragment); // section
  
  Uri withFragment = uri.replace(fragment: 'new section');
  print(withFragment); // https://example.com/page#new%20section
}
```

**Solution 5: Encode path segments individually**

```dart
void main() {
  List<String> segments = ['files', 'my document.pdf'];
  
  String path = segments.map(Uri.encodeComponent).join('/');
  print(path); // files/my%20document.pdf
  
  Uri uri = Uri(scheme: 'https', host: 'example.com', path: path);
  print(uri);
}
```

## Examples

`Uri.encodeFull` is designed for encoding a full URI path, while `Uri.encodeComponent` is for encoding a single parameter value. Using the wrong one leads to malformed URLs or double-encoding.

## Related Errors

- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart RegExp Error](/languages/dart/dart-regexp-error/)
- [Dart Date Time Error](/languages/dart/dart-date-time-error/)
