---
title: "[Solution] Flutter SharedPreferences Error — read, write, commit, reload"
description: "Fix Flutter SharedPreferences errors from async initialization, commit vs set, type mismatch, and cache issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 194
---

SharedPreferences errors occur when the instance is not initialized, values are read before write completes, or wrong types are accessed.

## Common Causes

1. `SharedPreferences.getInstance()` called without awaiting.
2. Reading a value that was never written.
3. `commit()` vs `setBool` confusion (commit returns Future).
4. Cache not being reloaded after external changes.
5. Storing complex objects instead of primitives.

## How to Fix It

**Solution 1: Initialize and use SharedPreferences**

```dart
import 'package:shared_preferences/shared_preferences.dart';

class StorageService {
  late SharedPreferences _prefs;
  
  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
  }
  
  Future<void> saveName(String name) async {
    await _prefs.setString('name', name);
  }
  
  String? getName() {
    return _prefs.getString('name');
  }
  
  Future<void> saveCount(int count) async {
    await _prefs.setInt('count', count);
  }
  
  int? getCount() {
    return _prefs.getInt('count');
  }
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  final storage = StorageService();
  await storage.init();
  
  await storage.saveName('Alice');
  print(storage.getName()); // Alice
  
  runApp(MyApp());
}
```

**Solution 2: Handle defaults when values don't exist**

```dart
import 'package:shared_preferences/shared_preferences.dart';

Future<void> demonstrateDefaults() async {
  final prefs = await SharedPreferences.getInstance();
  
  // getString returns null if not set
  String name = prefs.getString('name') ?? 'Guest';
  print('Name: $name');
  
  // getInt returns null if not set
  int count = prefs.getInt('count') ?? 0;
  print('Count: $count');
  
  // getBool returns null if not set
  bool isDark = prefs.getBool('darkMode') ?? false;
  print('Dark mode: $isDark');
}
```

**Solution 3: Store and retrieve lists**

```dart
import 'package:shared_preferences/shared_preferences.dart';

Future<void> demonstrateLists() async {
  final prefs = await SharedPreferences.getInstance();
  
  // Save list
  List<String> fruits = ['apple', 'banana', 'cherry'];
  await prefs.setStringList('fruits', fruits);
  
  // Read list
  List<String>? savedFruits = prefs.getStringList('fruits');
  print(savedFruits); // [apple, banana, cherry]
}
```

**Solution 4: Remove and clear data**

```dart
import 'package:shared_preferences/shared_preferences.dart';

Future<void> demonstrateCleanup() async {
  final prefs = await SharedPreferences.getInstance();
  
  // Remove specific key
  await prefs.remove('name');
  
  // Clear all data
  await prefs.clear();
  
  // Check if key exists
  bool hasName = prefs.containsKey('name');
  print('Has name: $hasName'); // false
}
```

**Solution 5: Test with SharedPreferences.setMockInitialValues**

```dart
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  test('reads name correctly', () async {
    // Set up mock values
    SharedPreferences.setMockInitialValues({
      'name': 'Test User',
      'count': 42,
    });
    
    final prefs = await SharedPreferences.getInstance();
    
    expect(prefs.getString('name'), 'Test User');
    expect(prefs.getInt('count'), 42);
  });
}
```

## Examples

Add `shared_preferences: ^2.2.0` to your `pubspec.yaml`. SharedPreferences stores data as key-value pairs of primitives (String, int, double, bool, List<String>).

## Related Errors

- [Flutter Secure Storage Error](/languages/dart/flutter-secure-storage-error/)
- [Flutter Path Provider Error](/languages/dart/flutter-path-provider-error/)
- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
