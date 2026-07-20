---
title: "[Solution] Dart HTTP Redirect Error — maxRedirects, followRedirects"
description: "Fix Dart HTTP redirect errors from maxRedirects exceeded, followRedirects configuration, and redirect loops."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 143
---

HTTP redirect errors occur when requests hit too many redirects, redirect loops, or when `followRedirects` is disabled.

## Common Causes

1. Server returning redirect loops (A → B → A).
2. `maxRedirects` exceeded on deeply nested redirects.
3. `followRedirects: false` but code expects the final response.
4. Cross-origin redirects being blocked.
5. HTTP to HTTPS redirect chains consuming the limit.

## How to Fix It

**Solution 1: Handle redirects with the http package**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  
  try {
    final response = await client.get(
      Uri.parse('https://example.com/old-page'),
    );
    
    print('Final URL: ${response.request?.url}');
    print('Status: ${response.statusCode}');
  } finally {
    client.close();
  }
}
```

**Solution 2: Disable redirect following**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  
  try {
    final request = http.Request('GET', Uri.parse('https://example.com/redirect'));
    request.followRedirects = false;
    
    final response = await client.send(request);
    
    print('Status: ${response.statusCode}');
    print('Location: ${response.headers['location']}');
  } finally {
    client.close();
  }
}
```

**Solution 3: Increase max redirects**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  
  try {
    final request = http.Request('GET', Uri.parse('https://example.com/chain'));
    request.maxRedirects = 10; // Default is 5
    
    final response = await client.send(request);
    print('Status: ${response.statusCode}');
  } on http.ClientException catch (e) {
    print('Too many redirects: ${e.message}');
  } finally {
    client.close();
  }
}
```

**Solution 4: Detect redirect loops**

```dart
import 'package:http/http.dart' as http;

Future<http.Response> followRedirectsSafely(
  Uri url, {
  int maxRedirects = 5,
}) async {
  final client = http.Client();
  Set<String> visitedUrls = {};
  
  try {
    Uri currentUrl = url;
    
    for (int i = 0; i < maxRedirects; i++) {
      if (visitedUrls.contains(currentUrl.toString())) {
        throw Exception('Redirect loop detected at $currentUrl');
      }
      visitedUrls.add(currentUrl.toString());
      
      final request = http.Request('GET', currentUrl);
      request.followRedirects = false;
      final response = await client.send(request);
      
      if (response.statusCode >= 300 && response.statusCode < 400) {
        String? location = response.headers['location'];
        if (location == null) break;
        currentUrl = Uri.parse(location);
      } else {
        return response;
      }
    }
    
    throw Exception('Too many redirects');
  } finally {
    client.close();
  }
}
```

**Solution 5: Use dart:io for redirect control**

```dart
import 'dart:io';
import 'package:http/http.dart' as http;

void main() async {
  HttpClient client = HttpClient();
  
  try {
    client.maxRedirects = 10;
    
    HttpClientRequest request = await client.getUrl(
      Uri.parse('https://example.com/page'),
    );
    
    HttpClientResponse response = await request.close();
    
    print('Final status: ${response.statusCode}');
    print('Redirects followed: ${response.redirects.length}');
    
    String body = await response.transform(utf8.decoder).join();
    print(body);
  } finally {
    client.close();
  }
}
```

## Examples

The default `maxRedirects` in the `http` package is 5. Redirect responses are typically 301 (Moved Permanently), 302 (Found), or 307 (Temporary Redirect).

## Related Errors

- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart HTTP Response Error](/languages/dart/dart-http-response-error/)
- [Dart URI Encode Error](/languages/dart/dart-uri-encode-error/)
