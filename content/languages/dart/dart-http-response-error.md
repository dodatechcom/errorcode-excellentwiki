---
title: "[Solution] Dart HTTP Response Error — Status Code, reasonPhrase, Headers"
description: "Fix Dart HTTP response errors from status code handling, reasonPhrase parsing, and header access."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 144
---

HTTP response errors occur when status codes are not handled, headers are accessed incorrectly, or response bodies fail to parse.

## Common Causes

1. Not checking `response.statusCode` before parsing the body.
2. Accessing headers that don't exist without null checks.
3. `response.body` being empty or malformed JSON.
4. `reasonPhrase` being null on some platforms.
5. Assuming all responses have a `Content-Type` header.

## How to Fix It

**Solution 1: Check status codes properly**

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
  );
  
  switch (response.statusCode) {
    case 200:
      Map<String, dynamic> data = jsonDecode(response.body);
      print('Post: ${data['title']}');
      break;
    case 404:
      print('Resource not found');
      break;
    case 500:
      print('Server error');
      break;
    default:
      print('Unexpected status: ${response.statusCode}');
  }
}
```

**Solution 2: Parse response body safely**

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/posts'),
  );
  
  if (response.body.isEmpty) {
    print('Empty response body');
    return;
  }
  
  try {
    dynamic data = jsonDecode(response.body);
    print('Data type: ${data.runtimeType}');
  } on FormatException catch (e) {
    print('Invalid JSON: ${e.message}');
    print('Raw body: ${response.body.substring(0, 100)}');
  }
}
```

**Solution 3: Access headers safely**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
  );
  
  // Access with null check
  String? contentType = response.headers['content-type'];
  String? cacheControl = response.headers['cache-control'];
  
  print('Content-Type: $contentType');
  print('Cache-Control: ${cacheControl ?? "not set"}');
  
  // Check if header exists
  if (response.headers.containsKey('x-request-id')) {
    print('Request ID: ${response.headers['x-request-id']}');
  }
}
```

**Solution 4: Handle different response formats**

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
  );
  
  String contentType = response.headers['content-type'] ?? '';
  
  if (contentType.contains('application/json')) {
    Map<String, dynamic> json = jsonDecode(response.body);
    print('JSON: $json');
  } else if (contentType.contains('text/html')) {
    print('HTML response: ${response.body.length} chars');
  } else if (contentType.contains('text/plain')) {
    print('Text: ${response.body}');
  } else {
    print('Unknown content type: $contentType');
  }
}
```

**Solution 5: Convert response to stream for large responses**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final request = http.Request('GET', Uri.parse('https://example.com/large'));
  final response = await http.Client().send(request);
  
  int bytesReceived = 0;
  
  await for (Chunk chunk in response.stream) {
    bytesReceived += chunk.length;
    print('Received $bytesReceived bytes');
  }
  
  print('Total: $bytesReceived bytes');
  print('Status: ${response.statusCode}');
}
```

## Examples

`http.Response` has `statusCode`, `body` (as String), `bodyBytes` (as List<int>), `headers`, and `request`. The `reasonPhrase` property may be null on some HTTP versions.

## Related Errors

- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart HTTP Client Error](/languages/dart/dart-http-client-error/)
- [Dart HTTP Redirect Error](/languages/dart/dart-http-redirect-error/)
