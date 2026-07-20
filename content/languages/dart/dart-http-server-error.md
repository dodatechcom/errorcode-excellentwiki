---
title: "[Solution] Dart HTTP Server Error — HttpServer bind, response, content type"
description: "Fix Dart HTTP server errors from bind failures, response handling, content type configuration, and connection management."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 134
---

HTTP server errors occur when `HttpServer.bind` fails, responses are not properly closed, or content types are misconfigured.

## Common Causes

1. `HttpServer.bind` failing due to port already in use.
2. Not calling `response.close()` causing hanging connections.
3. Missing `content-type` header causing client parsing errors.
4. Not handling exceptions from `listen` callbacks.
5. Binding to a specific address that is not available.

## How to Fix It

**Solution 1: Create a basic HTTP server**

```dart
import 'dart:io';

void main() async {
  HttpServer server = await HttpServer.bind('127.0.0.1', 8080);
  
  print('Server running on http://127.0.0.1:8080');
  
  await for (HttpRequest request in server) {
    request.response
      ..headers.contentType = ContentType.html
      ..write('<h1>Hello from Dart!</h1>')
      ..close();
  }
}
```

**Solution 2: Handle routing and methods**

```dart
import 'dart:io';

void main() async {
  HttpServer server = await HttpServer.bind('127.0.0.1', 8080);
  
  await for (HttpRequest request in server) {
    if (request.method == 'GET' && request.uri.path == '/api/data') {
      request.response
        ..headers.contentType = ContentType.json
        ..write('{"status": "ok"}')
        ..close();
    } else {
      request.response
        ..statusCode = HttpStatus.notFound
        ..write('Not Found')
        ..close();
    }
  }
}
```

**Solution 3: Serve static files**

```dart
import 'dart:io';

void main() async {
  HttpServer server = await HttpServer.bind('127.0.0.1', 8080);
  
  await for (HttpRequest request in server) {
    String filePath = 'public${request.uri.path}';
    File file = File(filePath);
    
    if (await file.exists()) {
      request.response.headers.contentType = ContentType.binary;
      await file.openRead().pipe(request.response);
    } else {
      request.response
        ..statusCode = HttpStatus.notFound
        ..close();
    }
  }
}
```

**Solution 4: Set appropriate content types**

```dart
import 'dart:io';

void main() async {
  HttpServer server = await HttpServer.bind('127.0.0.1', 8080);
  
  await for (HttpRequest request in server) {
    String path = request.uri.path;
    
    ContentType contentType;
    if (path.endsWith('.json')) {
      contentType = ContentType.json;
    } else if (path.endsWith('.html')) {
      contentType = ContentType.html;
    } else if (path.endsWith('.xml')) {
      contentType = ContentType('application', 'xml', charset: 'utf-8');
    } else {
      contentType = ContentType.text;
    }
    
    request.response
      ..headers.contentType = contentType
      ..write('Response data')
      ..close();
  }
}
```

**Solution 5: Close the server gracefully**

```dart
import 'dart:io';

void main() async {
  HttpServer server = await HttpServer.bind('127.0.0.1', 8080);
  
  print('Server started');
  
  // Handle server errors
  server.listen(
    (request) {
      request.response
        ..write('OK')
        ..close();
    },
    onError: (error) => print('Server error: $error'),
  );
  
  // Graceful shutdown
  ProcessSignal.sigterm.watch().listen((_) async {
    print('Shutting down...');
    await server.close();
    exit(0);
  });
}
```

## Examples

`HttpServer` extends `Stream<HttpRequest>`. Each incoming request is an `HttpRequest` object that includes the method, URI, headers, and a response object to write back.

## Related Errors

- [Dart IO Socket Error](/languages/dart/dart-io-socket-error/)
- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart HTTP Response Error](/languages/dart/dart-http-response-error/)
