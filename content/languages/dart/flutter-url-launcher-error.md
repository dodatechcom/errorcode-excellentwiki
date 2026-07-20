---
title: "[Solution] Flutter URL Launcher Error — canLaunch, mode, scheme validation"
description: "Fix Flutter url_launcher errors from canLaunch checks, launch mode configuration, and URI scheme validation."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 198
---

URL launcher errors occur when `canLaunch` returns false, launch mode is not configured for the platform, or URI schemes are invalid.

## Common Causes

1. `canLaunch` returning false for valid URLs.
2. Not configuring `LaunchMode` for external apps.
3. Missing platform declarations for custom URL schemes.
4. Launching URLs without checking availability first.
5. `launch` called with an invalid URI.

## How to Fix It

**Solution 1: Launch a URL safely**

```dart
import 'package:url_launcher/url_launcher.dart';

Future<void> launchUrl(String urlString) async {
  final Uri url = Uri.parse(urlString);
  
  if (await canLaunchUrl(url)) {
    await launchUrl(url);
  } else {
    print('Cannot launch: $urlString');
  }
}
```

**Solution 2: Launch email and phone**

```dart
import 'package:url_launcher/url_launcher.dart';

Future<void> sendEmail() async {
  final Uri emailUri = Uri(
    scheme: 'mailto',
    path: 'user@example.com',
    queryParameters: {
      'subject': 'Hello',
      'body': 'Message content',
    },
  );
  
  if (await canLaunchUrl(emailUri)) {
    await launchUrl(emailUri);
  }
}

Future<void> makePhoneCall() async {
  final Uri phoneUri = Uri(scheme: 'tel', path: '+1234567890');
  
  if (await canLaunchUrl(phoneUri)) {
    await launchUrl(phoneUri);
  }
}
```

**Solution 3: Launch with specific mode**

```dart
import 'package:url_launcher/url_launcher.dart';

Future<void> launchExternal(String urlString) async {
  final Uri url = Uri.parse(urlString);
  
  await launchUrl(
    url,
    mode: LaunchMode.externalApplication,
  );
}

Future<void> launchInApp(String urlString) async {
  final Uri url = Uri.parse(urlString);
  
  await launchUrl(
    url,
    mode: LaunchMode.inAppWebView,
  );
}
```

**Solution 4: Handle launch errors**

```dart
import 'package:url_launcher/url_launcher.dart';

Future<void> safeLaunch(String urlString) async {
  try {
    final Uri url = Uri.parse(urlString);
    
    if (await canLaunchUrl(url)) {
      bool launched = await launchUrl(url);
      if (!launched) {
        print('Launch returned false');
      }
    } else {
      print('Cannot launch URL');
    }
  } catch (e) {
    print('Error launching URL: $e');
  }
}
```

**Solution 5: Configure scheme in Info.plist (iOS)**

```dart
// In Info.plist:
// <key>CFBundleURLTypes</key>
// <array>
//   <dict>
//     <key>CFBundleURLSchemes</key>
//     <array>
//       <string>myapp</string>
//     </array>
//   </dict>
// </array>

import 'package:url_launcher/url_launcher.dart';

Future<void> launchCustomScheme() async {
  final Uri url = Uri.parse('myapp://deeplink');
  
  if (await canLaunchUrl(url)) {
    await launchUrl(url);
  }
}
```

## Examples

Add `url_launcher: ^6.2.0` to your `pubspec.yaml`. On iOS, configure `LSApplicationQueriesSchemes` in `Info.plist` for custom URL schemes.

## Related Errors

- [Flutter HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Flutter URI Encode Error](/languages/dart/dart-uri-encode-error/)
- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
