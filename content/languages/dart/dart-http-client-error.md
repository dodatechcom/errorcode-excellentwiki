---
title: "[Solution] Dart HTTP Client Error — Connection Pool, Idle Timeout"
description: "Fix Dart HTTP client errors from connection pool exhaustion, idle timeout, and client lifecycle management."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 141
---

HTTP client errors involve connection pool exhaustion, idle timeout misconfiguration, and improper client lifecycle management.

## Common Causes

1. Creating new `Client` instances per request instead of reusing.
2. Not closing the client, causing connection pool exhaustion.
3. Idle connections being dropped by the server.
4. Too many concurrent requests overwhelming the connection pool.
5. `Client.send` being used incorrectly without proper request construction.

## How to Fix It

**Solution 1: Reuse a single HTTP client**

```dart
import 'package:http/http.dart' as http;

class ApiClient {
  final http.Client _client;
  
  ApiClient() : _client = http.Client();
  
  Future<http.Response> get(String url) {
    return _client.get(Uri.parse(url));
  }
  
  void close() => _client.close();
}

void main() async {
  final api = ApiClient();
  
  final response = await api.get('https://jsonplaceholder.typicode.com/posts');
  print('Status: ${response.statusCode}');
  
  api.close();
}
```

**Solution 2: Handle idle connection drops**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  
  try {
    // First request
    var response = await client.get(
      Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
    );
    print('First: ${response.statusCode}');
    
    // Wait longer than typical idle timeout
    await Future.delayed(Duration(seconds: 60));
    
    // Second request may fail if connection was dropped
    response = await client.get(
      Uri.parse('https://jsonplaceholder.typicode.com/posts/2'),
    );
    print('Second: ${response.statusCode}');
  } catch (e) {
    print('Connection may have been dropped: $e');
  } finally {
    client.close();
  }
}
```

**Solution 3: Limit concurrent requests**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  final semaphore = _Semaphore(5); // Max 5 concurrent
  
  try {
    List<Future> futures = [];
    
    for (int i = 0; i < 20; i++) {
      futures.add(semaphore.acquire().then((_) async {
        try {
          var response = await client.get(
            Uri.parse('https://jsonplaceholder.typicode.com/posts/$i'),
          );
          print('Post $i: ${response.statusCode}');
        } finally {
          semaphore.release();
        }
      }));
    }
    
    await Future.wait(futures);
  } finally {
    client.close();
  }
}

class _Semaphore {
  int _count;
  final int _max;
  final List<Completer<void>> _queue = [];
  
  _Semaphore(this._max) : _count = _max;
  
  Future<void> acquire() {
    if (_count > 0) {
      _count--;
      return Future.value();
    }
    Completer<void> completer = Completer();
    _queue.add(completer);
    return completer.future;
  }
  
  void release() {
    if (_queue.isNotEmpty) {
      _queue.removeAt(0).complete();
    } else {
      _count++;
    }
  }
}
```

**Solution 4: Use retry logic for transient failures**

```dart
import 'package:http/http.dart' as http;

Future<http.Response> retryRequest(
  Uri url, {
  int maxRetries = 3,
  Duration delay = const Duration(seconds: 1),
}) async {
  for (int attempt = 0; attempt < maxRetries; attempt++) {
    try {
      final response = await http.get(url);
      if (response.statusCode < 500) return response;
    } catch (e) {
      if (attempt == maxRetries - 1) rethrow;
    }
    await Future.delayed(delay * (attempt + 1));
  }
  throw Exception('Max retries exceeded');
}

void main() async {
  final response = await retryRequest(
    Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
  );
  print('Status: ${response.statusCode}');
}
```

**Solution 5: Set timeouts on requests**

```dart
import 'package:http/http.dart' as http;

void main() async {
  final client = http.Client();
  
  try {
    final response = await client.get(
      Uri.parse('https://jsonplaceholder.typicode.com/posts'),
    ).timeout(Duration(seconds: 10));
    
    print('Status: ${response.statusCode}');
  } catch (e) {
    print('Request failed or timed out: $e');
  } finally {
    client.close();
  }
}
```

## Examples

The `http` package's default `Client` maintains a connection pool. Creating a new `Client` per request wastes resources and can lead to port exhaustion on the local machine.

## Related Errors

- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart HTTP Response Error](/languages/dart/dart-http-response-error/)
- [Dart HTTP Multipart Error](/languages/dart/dart-http-multipart-error/)
