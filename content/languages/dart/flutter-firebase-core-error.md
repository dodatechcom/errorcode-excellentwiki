---
title: "[Solution] Flutter Firebase Core Error — initializeApp, options, google-services.json"
description: "Fix Flutter Firebase Core errors from Firebase.initializeApp, missing options, google-services.json configuration, and platform setup."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 199
---

Firebase Core errors occur when `Firebase.initializeApp` fails, configuration files are missing, or platform-specific setup is incomplete.

## Common Causes

1. `Firebase.initializeApp` not called before using Firebase services.
2. `google-services.json` (Android) or `GoogleService-Info.plist` (iOS) missing.
3. `FirebaseOptions` not provided for web or desktop.
4. Firebase SDK version mismatch.
5. Firebase not initialized in `main()`.

## How to Fix It

**Solution 1: Initialize Firebase in main**

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Firebase.initializeApp();
  
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(child: Text('Firebase Ready')),
      ),
    );
  }
}
```

**Solution 2: Handle initialization errors**

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

class FirebaseInitApp extends StatefulWidget {
  @override
  State<FirebaseInitApp> createState() => _FirebaseInitAppState();
}

class _FirebaseInitAppState extends State<FirebaseInitApp> {
  bool _initialized = false;
  String? _error;
  
  @override
  void initState() {
    super.initState();
    _initializeFirebase();
  }
  
  Future<void> _initializeFirebase() async {
    try {
      await Firebase.initializeApp();
      setState(() => _initialized = true);
    } catch (e) {
      setState(() => _error = e.toString());
    }
  }
  
  @override
  Widget build(BuildContext context) {
    if (_error != null) {
      return MaterialApp(
        home: Scaffold(
          body: Center(child: Text('Error: $_error')),
        ),
      );
    }
    
    if (!_initialized) {
      return MaterialApp(
        home: Scaffold(
          body: Center(child: CircularProgressIndicator()),
        ),
      );
    }
    
    return MaterialApp(home: HomePage());
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(body: Center(child: Text('Home')));
  }
}
```

**Solution 3: Firebase options for web/desktop**

```dart
import 'package:firebase_core/firebase_core.dart';

// In main.dart
await Firebase.initializeApp(
  options: FirebaseOptions(
    apiKey: 'your-api-key',
    authDomain: 'your-project.firebaseapp.com',
    projectId: 'your-project-id',
    storageBucket: 'your-project.appspot.com',
    messagingSenderId: '123456789',
    appId: '1:123456789:web:abcdef',
  ),
);
```

**Solution 4: Check Firebase status**

```dart
import 'package:firebase_core/firebase_core.dart';

void checkFirebaseStatus() {
  FirebaseApp app = Firebase.app();
  print('App name: ${app.name}');
  print('Project ID: ${app.options.projectID}');
  print('Is default: ${app.name == '[DEFAULT]'}');
}
```

**Solution 5: Multiple Firebase projects**

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> setupMultipleFirebase() async {
  // Default project
  await Firebase.initializeApp();
  
  // Secondary project
  await Firebase.initializeApp(
    name: 'secondary',
    options: FirebaseOptions(
      apiKey: 'second-api-key',
      projectId: 'second-project',
      appId: 'second-app-id',
    ),
  );
  
  FirebaseApp secondary = Firebase.app('secondary');
  print('Secondary: ${secondary.options.projectID}');
}
```

## Examples

Add `firebase_core: ^2.24.0` to your `pubspec.yaml`. For Android, place `google-services.json` in `android/app/`. For iOS, place `GoogleService-Info.plist` in `ios/Runner/`.

## Related Errors

- [Flutter Firebase Auth Error](/languages/dart/flutter-firebase-auth-error/)
- [Flutter Firestore Error](/languages/dart/flutter-firestore-error/)
- [Flutter Firebase Storage Error](/languages/dart/flutter-firebase-storage-error/)
