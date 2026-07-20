---
title: "[Solution] Flutter Local Notification Error — channel, icon, payload"
description: "Fix Flutter local notifications errors from channel configuration, icon setup, payload handling, and initialization."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 193
---

Local notification errors occur when Android notification channels are not created, icons are misconfigured, or payload handling fails.

## Common Causes

1. Android notification channel not created before showing notification.
2. Small icon resource not found or invalid.
3. Payload not being received on notification tap.
4. Notification permissions not requested on iOS 13+.
5. `initialize` not called before showing notifications.

## How to Fix It

**Solution 1: Initialize the plugin**

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
    FlutterLocalNotificationsPlugin();

Future<void> initNotifications() async {
  const AndroidInitializationSettings androidSettings =
      AndroidInitializationSettings('@mipmap/ic_launcher');
  
  const DarwinInitializationSettings iosSettings =
      DarwinInitializationSettings(
    requestAlertPermission: true,
    requestBadgePermission: true,
    requestSoundPermission: true,
  );
  
  const InitializationSettings settings = InitializationSettings(
    android: androidSettings,
    iOS: iosSettings,
  );
  
  await flutterLocalNotificationsPlugin.initialize(
    settings,
    onDidReceiveNotificationResponse: (details) {
      print('Notification tapped: ${details.payload}');
    },
  );
}
```

**Solution 2: Create Android notification channel**

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

const AndroidNotificationChannel channel = AndroidNotificationChannel(
  'high_importance_channel',
  'High Importance Notifications',
  description: 'This channel is used for important notifications',
  importance: Importance.high,
);

Future<void> createNotificationChannel() async {
  await flutterLocalNotificationsPlugin
      .resolvePlatformSpecificImplementation<
          AndroidFlutterLocalNotificationsPlugin>()
      ?.createNotificationChannel(channel);
}
```

**Solution 3: Show a notification**

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

Future<void> showNotification() async {
  const AndroidNotificationDetails androidDetails =
      AndroidNotificationDetails(
    'high_importance_channel',
    'High Importance Notifications',
    channelDescription: 'Important notifications',
    importance: Importance.high,
    priority: Priority.high,
    icon: '@mipmap/ic_launcher',
  );
  
  const NotificationDetails details = NotificationDetails(
    android: androidDetails,
  );
  
  await flutterLocalNotificationsPlugin.show(
    0,
    'Hello!',
    'This is a notification',
    details,
    payload: 'data_from_notification',
  );
}
```

**Solution 4: Handle notification tap with payload**

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

class NotificationHandler {
  static void onSelectNotification(String? payload) {
    if (payload != null) {
      print('Payload: $payload');
      // Navigate based on payload
    }
  }
}

// Modern approach with onDidReceiveNotificationResponse
flutterLocalNotificationsPlugin.initialize(
  settings,
  onDidReceiveNotificationResponse: (details) {
    String? payload = details.payload;
    if (payload != null) {
      print('Tapped with payload: $payload');
    }
  },
);
```

**Solution 5: Schedule notifications**

```dart
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

Future<void> scheduleNotification() async {
  const AndroidNotificationDetails androidDetails =
      AndroidNotificationDetails(
    'high_importance_channel',
    'Reminders',
    importance: Importance.high,
  );
  
  const NotificationDetails details = NotificationDetails(
    android: androidDetails,
  );
  
  await flutterLocalNotificationsPlugin.periodicallyShow(
    0,
    'Reminder',
    'Don\'t forget to check the app!',
    RepeatInterval.hourly,
    details,
  );
}
```

## Examples

Add `flutter_local_notifications: ^16.0.0` to your `pubspec.yaml`. On Android, create the notification channel in `main()`. On iOS, request permission in `initialize`.

## Related Errors

- [Flutter Permission Error](/languages/dart/flutter-permission-error/)
- [Flutter Firebase Messaging Error](/languages/dart/flutter-firebase-messaging-error/)
- [Flutter Shared Preferences Error](/languages/dart/flutter-shared-preferences-error/)
