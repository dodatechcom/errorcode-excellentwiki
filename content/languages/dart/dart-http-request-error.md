---
title: "[Solution] Dart HTTP Request Error — get/post/put/delete, headers, body"
description: "Fix Dart HTTP package request errors from get/post/put/delete failures, header issues, and body encoding."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 140
---

HTTP request errors occur when requests fail due to network issues, invalid URLs, malformed bodies, or incorrect headers.

## Common Causes

1. Missing `package:http` import or dependency.
2. URL not being a valid URI (special characters not encoded).
3. Request body not matching `Content-Type` header.
4. Not closing the `Client`, causing connection leaks.
5. `SocketException` when no internet connection is available.

## How to Fix It

**Solution 1: Make basic HTTP requests**

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  // GET request
  final response = await http.get(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
  );
  
  if (response.statusCode == 200) {
    Map<String, dynamic> data = jsonDecode(response.body);
    print('Title: ${data['title']}');
  } else {
    print('Request failed: ${response.statusCode}');
  }
}
```

**Solution 2: Send POST with JSON body**

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  final response = await http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'title': 'New Post',
      'body': 'Content here',
      'userId': 1,
    }),
  );
  
  print('Status: ${response.statusCode}');
  print('Response: ${response.body}');
}
```

**Solution 3: Handle request errors with try-catch**

```dart
import 'package:http/http.dart' as http;

void main() async {
  try {
    final response = await http.get(
      Uri.parse('https://api.example.com/data'),
    );
    print(response.body);
  } on http.ClientException catch (e) {
    print('Client error: ${e.message}');
  } on FormatException catch (e) {
    print('Invalid URL: ${e.message}');
  } catch (e) {
    print('Unexpected error: $e');
  }
}
```

**Solution 4: Close the HTTP client**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  
  try {
    final response = await client.get(
      Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    );
    print('Got ${response.body.length} bytes');
  } finally {
    client.close(); // Always close to free connections
  }
}
```

**Solution 5: Send PUT and DELETE requests**

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  // PUT
  final putResponse = await http.put(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'title': 'Updated'}),
  );
  print('PUT: ${putResponse.statusCode}');
  
  // DELETE
  final deleteResponse = await http.delete(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
  );
  print('DELETE: ${deleteResponse.statusCode}');
}
```

## Examples

The `http` package is a high-level package that wraps `dart:io` HTTP functionality. Add `http: ^1.1.0` to your `pubspec.yaml` dependencies.

## Related Errors

- [Dart HTTP Client Error](/languages/dart/dart-http-client-error/)
- [Dart HTTP Response Error](/languages/dart/dart-http-response-error/)
- [Dart URI Encode Error](/languages/dart/dart-uri-encode-error/)
