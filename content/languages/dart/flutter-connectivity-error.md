---
title: "[Solution] Flutter Connectivity Error — connectivity_plus, wifi/cellular, checkInterval"
description: "Fix Flutter connectivity_plus errors from connection checking, wifi/cellular detection, and event stream issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 196
---

Connectivity errors occur when connection status is not properly detected, the plugin is not initialized, or real-time monitoring is misconfigured.

## Common Causes

1. `Connectivity` not initialized before checking.
2. Confusing `ConnectivityResult` values.
3. Not listening to real-time connectivity changes.
4. Checking connectivity before the first frame.
5. Missing platform permissions.

## How to Fix It

**Solution 1: Check current connectivity**

```dart
import 'package:connectivity_plus/connectivity_plus.dart';

Future<void> checkConnectivity() async {
  final ConnectivityResult result = await Connectivity().checkConnectivity();
  
  if (result == ConnectivityResult.mobile) {
    print('Connected via mobile data');
  } else if (result == ConnectivityResult.wifi) {
    print('Connected via WiFi');
  } else if (result == ConnectivityResult.ethernet) {
    print('Connected via ethernet');
  } else if (result == ConnectivityResult.bluetooth) {
    print('Connected via bluetooth');
  } else if (result == ConnectivityResult.vpn) {
    print('Connected via VPN');
  } else {
    print('No internet connection');
  }
}
```

**Solution 2: Listen to connectivity changes**

```dart
import 'package:connectivity_plus/connectivity_plus.dart';

class ConnectivityService {
  StreamSubscription<ConnectivityResult>? _subscription;
  
  void startListening() {
    _subscription = Connectivity().onConnectivityChanged.listen((result) {
      if (result == ConnectivityResult.none) {
        print('Lost connection');
      } else {
        print('Connected: $result');
      }
    });
  }
  
  void stopListening() {
    _subscription?.cancel();
    _subscription = null;
  }
}
```

**Solution 3: Check actual internet access**

```dart
import 'package:connectivity_plus/connectivity_plus.dart';
import 'package:http/http.dart' as http;

Future<bool> hasInternetAccess() async {
  final ConnectivityResult result = await Connectivity().checkConnectivity();
  
  if (result == ConnectivityResult.none) {
    return false;
  }
  
  try {
    final response = await http.get(
      Uri.parse('https://www.google.com'),
    ).timeout(Duration(seconds: 5));
    
    return response.statusCode == 200;
  } catch (_) {
    return false;
  }
}
```

**Solution 4: Use in a widget**

```dart
import 'package:flutter/material.dart';
import 'package:connectivity_plus/connectivity_plus.dart';

class ConnectivityWidget extends StatefulWidget {
  @override
  State<ConnectivityWidget> createState() => _ConnectivityWidgetState();
}

class _ConnectivityWidgetState extends State<ConnectivityWidget> {
  String _status = 'Checking...';
  
  @override
  void initState() {
    super.initState();
    _checkConnectivity();
    
    Connectivity().onConnectivityChanged.listen((result) {
      setState(() {
        _status = result == ConnectivityResult.none
            ? 'Offline'
            : 'Online ($result)';
      });
    });
  }
  
  Future<void> _checkConnectivity() async {
    final result = await Connectivity().checkConnectivity();
    setState(() {
      _status = result == ConnectivityResult.none ? 'Offline' : 'Online';
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Text('Status: $_status');
  }
}
```

**Solution 5: Handle multiple connectivity results**

```dart
import 'package:connectivity_plus/connectivity_plus.dart';

Future<void> handleMultipleResults() async {
  List<ConnectivityResult> results = await Connectivity().checkConnectivity();
  
  print('Active connections: ${results.length}');
  for (ConnectivityResult result in results) {
    print('  - $result');
  }
}
```

## Examples

Add `connectivity_plus: ^5.0.0` to your `pubspec.yaml`. `ConnectivityResult` indicates the type of connection, not whether internet access is actually available.

## Related Errors

- [Flutter HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Flutter Location Error](/languages/dart/flutter-location-error/)
- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
