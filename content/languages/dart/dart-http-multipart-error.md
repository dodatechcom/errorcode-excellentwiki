---
title: "[Solution] Dart HTTP Multipart Error — MultipartRequest, file field, boundary"
description: "Fix Dart HTTP multipart request errors from file upload failures, boundary issues, and field encoding."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 142
---

Multipart errors occur when file uploads fail, form fields are not properly encoded, or the multipart boundary is malformed.

## Common Causes

1. `MultipartFile` from bytes failing due to empty data.
2. Content-Type header not set correctly for file uploads.
3. Server expecting specific boundary format.
4. File path not existing when creating multipart from path.
5. Missing required form fields in multipart requests.

## How to Fix It

**Solution 1: Upload a file with MultipartRequest**

```dart
import 'package:http/http.dart' as http;

void main() async {
  var request = http.MultipartRequest(
    'POST',
    Uri.parse('https://example.com/upload'),
  );
  
  request.files.add(
    await http.MultipartFile.fromPath(
      'file',
      '/path/to/document.pdf',
      contentType: MediaType('application', 'pdf'),
    ),
  );
  
  request.fields['description'] = 'My document';
  
  var response = await request.send();
  var responseBody = await response.stream.bytesToString();
  
  print('Status: ${response.statusCode}');
  print('Response: $responseBody');
}
```

**Solution 2: Create multipart from bytes**

```dart
import 'package:http/http.dart' as http;
import 'dart:typed_data';

void main() async {
  Uint8List fileBytes = Uint8List.fromList([1, 2, 3, 4, 5]);
  
  var request = http.MultipartRequest(
    'POST',
    Uri.parse('https://example.com/upload'),
  );
  
  request.files.add(
    http.MultipartFile.fromBytes(
      'file',
      fileBytes,
      filename: 'data.bin',
      contentType: MediaType('application', 'octet-stream'),
    ),
  );
  
  var response = await request.send();
  print('Status: ${response.statusCode}');
}
```

**Solution 3: Handle multipart form fields**

```dart
import 'package:http/http.dart' as http;

void main() async {
  var request = http.MultipartRequest(
    'POST',
    Uri.parse('https://example.com/api/profile'),
  );
  
  request.fields['name'] = 'Alice';
  request.fields['email'] = 'alice@example.com';
  request.fields['age'] = '30';
  
  // Add avatar image
  request.files.add(
    await http.MultipartFile.fromPath(
      'avatar',
      '/path/to/avatar.jpg',
      contentType: MediaType('image', 'jpeg'),
    ),
  );
  
  var response = await request.send();
  print('Status: ${response.statusCode}');
}
```

**Solution 4: Stream upload progress**

```dart
import 'package:http/http.dart' as http;

void main() async {
  var request = http.MultipartRequest(
    'POST',
    Uri.parse('https://example.com/upload'),
  );
  
  request.files.add(
    await http.MultipartFile.fromPath(
      'file',
      '/path/to/large_file.zip',
      contentType: MediaType('application', 'zip'),
    ),
  );
  
  var response = await request.send();
  
  response.stream.listen(
    (data) {
      // Track upload progress
    },
    onDone: () => print('Upload complete'),
  );
}
```

**Solution 5: Validate file before upload**

```dart
import 'package:http/http.dart' as http;
import 'dart:io';

Future<void> uploadFile(String filePath) async {
  File file = File(filePath);
  
  if (!await file.exists()) {
    print('File not found: $filePath');
    return;
  }
  
  int fileSize = await file.length();
  if (fileSize == 0) {
    print('File is empty');
    return;
  }
  
  var request = http.MultipartRequest(
    'POST',
    Uri.parse('https://example.com/upload'),
  );
  
  request.files.add(
    await http.MultipartFile.fromPath(
      'file',
      filePath,
    ),
  );
  
  var response = await request.send();
  print('Uploaded: ${response.statusCode}');
}
```

## Examples

`MultipartFile.fromPath` reads the file and determines the content type from the extension. For binary data or network streams, use `fromBytes` or `fromStream`.

## Related Errors

- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart HTTP Client Error](/languages/dart/dart-http-client-error/)
- [Dart File Open Error](/languages/dart/dart-file-open-error/)
