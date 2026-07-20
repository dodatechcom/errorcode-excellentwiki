---
title: "[Solution] Flutter Secure Storage Error — keychain, keyStore, options"
description: "Fix Flutter secure storage errors from keychain/keyStore configuration, encryption options, and platform-specific setup."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 195
---

Secure storage errors occur when keychain/keyStore access fails, encryption options are misconfigured, or platform setup is incomplete.

## Common Causes

1. Keychain access not configured for iOS.
2. `AndroidOptions` not specifying correct keyStore config.
3. Reading a value that does not exist.
4. Storage cleared on app uninstall by default.
5. Biometric authentication not configured.

## How to Fix It

**Solution 1: Basic read and write**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureStorageService {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();
  
  Future<void> writeToken(String token) async {
    await _storage.write(key: 'auth_token', value: token);
  }
  
  Future<String?> readToken() async {
    return await _storage.read(key: 'auth_token');
  }
  
  Future<void> deleteToken() async {
    await _storage.delete(key: 'auth_token');
  }
  
  Future<void> deleteAll() async {
    await _storage.deleteAll();
  }
}
```

**Solution 2: Configure Android options**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

void configureSecureStorage() {
  const storage = FlutterSecureStorage(
    aOptions: AndroidOptions(
      encryptedSharedPreferences: true,
    ),
  );
}
```

**Solution 3: Configure iOS options**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

void configureIOs() {
  const storage = FlutterSecureStorage(
    iOptions: IOSOptions(
      accessibility: KeychainAccessibility.first_unlock_this_device,
    ),
  );
}
```

**Solution 4: Read all stored values**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

Future<void> readAll() async {
  const storage = FlutterSecureStorage();
  
  Map<String, String> allValues = await storage.readAll();
  
  allValues.forEach((key, value) {
    print('$key: $value');
  });
}
```

**Solution 5: Check if key exists**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

Future<void> checkKeyExists() async {
  const storage = FlutterSecureStorage();
  
  bool exists = await storage.containsKey(key: 'auth_token');
  print('Token exists: $exists');
  
  if (!exists) {
    await storage.write(key: 'auth_token', value: 'new_token');
  }
}
```

## Examples

Add `flutter_secure_storage: ^9.0.0` to your `pubspec.yaml`. On iOS, configure Keychain Sharing and Accessibility in your Xcode project.

## Related Errors

- [Flutter Shared Preferences Error](/languages/dart/flutter-shared-preferences-error/)
- [Flutter Firebase Auth Error](/languages/dart/flutter-firebase-auth-error/)
- [Flutter Path Provider Error](/languages/dart/flutter-path-provider-error/)
