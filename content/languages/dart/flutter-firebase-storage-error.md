---
title: "[Solution] Flutter Firebase Storage Error — put/get/delete, download URL"
description: "Fix Flutter Firebase Storage errors from file upload, download URL retrieval, delete operations, and metadata configuration."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 202
---

Firebase Storage errors occur when file uploads fail, download URLs are not retrieved correctly, or storage rules deny access.

## Common Causes

1. File path not found during upload.
2. Storage rules not allowing write access.
3. Download URL not available immediately after upload.
4. File size exceeding storage limits.
5. Metadata not set correctly.

## How to Fix It

**Solution 1: Upload a file**

```dart
import 'dart:io';
import 'package:firebase_storage/firebase_storage.dart';

Future<String> uploadFile(File file, String path) async {
  Reference ref = FirebaseStorage.instance.ref().child(path);
  
  UploadTask task = ref.putFile(file);
  
  TaskSnapshot snapshot = await task;
  
  String downloadUrl = await snapshot.ref.getDownloadURL();
  print('Download URL: $downloadUrl');
  
  return downloadUrl;
}
```

**Solution 2: Upload with metadata**

```dart
import 'dart:io';
import 'package:firebase_storage/firebase_storage.dart';

Future<String> uploadWithMetadata(File file, String path) async {
  Reference ref = FirebaseStorage.instance.ref().child(path);
  
  SettableMetadata metadata = SettableMetadata(
    contentType: 'image/jpeg',
    customMetadata: {
      'uploadedBy': 'user123',
      'description': 'Profile picture',
    },
  );
  
  UploadTask task = ref.putFile(file, metadata);
  TaskSnapshot snapshot = await task;
  
  return await snapshot.ref.getDownloadURL();
}
```

**Solution 3: Download file**

```dart
import 'dart:io';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:path_provider/path_provider.dart';

Future<void> downloadFile(String url, String fileName) async {
  Directory tempDir = await getTemporaryDirectory();
  File file = File('${tempDir.path}/$fileName');
  
  await FirebaseStorage.instance.refFromURL(url).writeToFile(file);
  print('Downloaded to: ${file.path}');
}
```

**Solution 4: List files in a directory**

```dart
import 'package:firebase_storage/firebase_storage.dart';

Future<void> listFiles() async {
  ListResult result = await FirebaseStorage.instance.ref('uploads/').listAll();
  
  for (Reference ref in result.items) {
    String url = await ref.getDownloadURL();
    print('${ref.name}: $url');
  }
}
```

**Solution 5: Delete files**

```dart
import 'package:firebase_storage/firebase_storage.dart';

Future<void> deleteFile(String path) async {
  await FirebaseStorage.instance.ref(path).delete();
  print('Deleted: $path');
}

Future<void> deleteAll() async {
  ListResult result = await FirebaseStorage.instance.ref('uploads/').listAll();
  
  for (Reference ref in result.items) {
    await ref.delete();
  }
}
```

## Examples

Add `firebase_storage: ^11.6.0` to your `pubspec.yaml`. Storage rules must allow `write` access for authenticated users.

## Related Errors

- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
- [Flutter Firebase Auth Error](/languages/dart/flutter-firebase-auth-error/)
- [Flutter File Open Error](/languages/dart/dart-file-open-error/)
