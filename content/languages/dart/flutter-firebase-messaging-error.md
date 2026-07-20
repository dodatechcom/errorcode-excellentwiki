---
title: "[Solution] Flutter Firebase Messaging Error — FCM token, onMessage, notification"
description: "Fix Flutter Firebase Cloud Messaging errors from FCM token retrieval, message handling, notification configuration, and background processing."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 203
---

Firebase Messaging errors occur when FCM tokens are not retrieved, message handlers are not configured, or notification permissions are missing.

## Common Causes

1. FCM token not being retrieved after initialization.
2. `onMessage` handler not registered.
3. Notification permission not requested on iOS.
4. Background message handler not marked as top-level function.
5. Token not being sent to the server.

## How to Fix It

**Solution 1: Get FCM token**

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

Future<void> getFCMToken() async {
  String? token = await FirebaseMessaging.instance.getToken();
  print('FCM Token: $token');
  
  // Send token to your server
  // await sendTokenToServer(token);
}

// Listen for token refresh
void listenTokenRefresh() {
  FirebaseMessaging.instance.onTokenRefresh.listen((String token) {
    print('Token refreshed: $token');
    // Update server with new token
  });
}
```

**Solution 2: Request notification permission**

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

Future<void> requestPermission() async {
  NotificationSettings settings = await FirebaseMessaging.instance
      .requestPermission(
    alert: true,
    badge: true,
    sound: true,
    provisional: false,
  );
  
  if (settings.authorizationStatus == AuthorizationStatus.authorized) {
    print('Permission granted');
  } else {
    print('Permission denied');
  }
}
```

**Solution 3: Handle foreground messages**

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

void setupMessageHandlers() {
  FirebaseMessaging.onMessage.listen((RemoteMessage message) {
    print('Foreground message: ${message.notification?.title}');
    print('Body: ${message.notification?.body}');
    print('Data: ${message.data}');
    
    // Show local notification
    showLocalNotification(message);
  });
}

void showLocalNotification(RemoteMessage message) {
  // Use flutter_local_notifications to display
}
```

**Solution 4: Handle background messages**

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

// Must be a top-level function
@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  print('Background message: ${message.messageId}');
  // Process the message
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  
  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
  
  runApp(MyApp());
}
```

**Solution 5: Handle message tap**

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

void handleMessageTap() {
  FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
    print('Message opened app: ${message.data}');
    
    // Navigate based on message data
    // Navigator.pushNamed(context, '/detail', arguments: message.data);
  });
}

// Check if app opened from notification
Future<void> checkInitialMessage() async {
  RemoteMessage? message = await FirebaseMessaging.instance.getInitialMessage();
  
  if (message != null) {
    print('App opened from notification: ${message.data}');
  }
}
```

## Examples

Add `firebase_messaging: ^14.7.0` to your `pubspec.yaml`. On iOS, ensure push notification capability is enabled in Xcode.

## Related Errors

- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
- [Flutter Local Notification Error](/languages/dart/flutter-local-notification-error/)
- [Flutter Firebase Auth Error](/languages/dart/flutter-firebase-auth-error/)
