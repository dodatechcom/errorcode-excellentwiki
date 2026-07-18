---
title: "[Solution] Flutter Asset Loading Error — How to Fix"
description: "Fix Flutter asset loading errors. Resolve asset not found, bundle, and image loading issues in Flutter."
frameworks: ["flutter"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flutter asset loading error occurs when the app cannot find or load assets like images, fonts, or JSON files. Assets must be declared in `pubspec.yaml` and placed in the correct directory.

## Why It Happens

Flutter bundles assets during build time. Errors occur when assets are not declared in `pubspec.yaml`, when the file path is incorrect, when the asset directory structure doesn't match the declaration, when font families are not properly configured, or when assets are case-sensitive on different platforms.

## Common Error Messages

```
Exception: Unable to load asset: assets/images/logo.png
```

```
Unable to load asset: assets/fonts/Roboto-Regular.ttf
```

```
Error: No Material Icons font found
```

```
Exception: asset "assets/data.json" does not exist
```

## How to Fix It

### 1. Declare Assets in pubspec.yaml

Configure assets correctly:

```yaml
# pubspec.yaml
flutter:
  assets:
    - assets/images/
    - assets/data/
    - assets/fonts/

  fonts:
    - family: CustomFont
      fonts:
        - asset: assets/fonts/CustomFont-Regular.ttf
        - asset: assets/fonts/CustomFont-Bold.ttf
          weight: 700
```

### 2. Load Assets in Code

Use the correct API for each asset type:

```dart
// Load an image
Image.asset('assets/images/logo.png');

// Load an image with error handling
Image.asset(
    'assets/images/logo.png',
    errorBuilder: (context, error, stackTrace) {
        return Icon(Icons.broken_image);
    },
    // Or use a placeholder
    frameBuilder: (context, child, frame, wasSynchronouslyLoaded) {
        return child;
    },
);

// Load a JSON file
Future<Map<String, dynamic>> loadAssetData() async {
    final jsonString = await rootBundle.loadString('assets/data/config.json');
    return jsonDecode(jsonString);
}

// Load a font
Text(
    'Hello',
    style: TextStyle(fontFamily: 'CustomFont'),
)
```

### 3. Handle Asset Path Issues

Verify asset paths exist:

```dart
class AssetChecker {
    static Future<bool> assetExists(String path) async {
        try {
            await rootBundle.load(path);
            return true;
        } catch (e) {
            return false;
        }
    }
}

// Usage in code
if (await AssetChecker.assetExists('assets/images/logo.png')) {
    return Image.asset('assets/images/logo.png');
} else {
    return Icon(Icons.image);
}
```

### 4. Handle Font Loading

Configure and load custom fonts:

```yaml
# pubspec.yaml
flutter:
  fonts:
    - family: Roboto
      fonts:
        - asset: assets/fonts/Roboto-Regular.ttf
        - asset: assets/fonts/Roboto-Bold.ttf
          weight: 700
        - asset: assets/fonts/Roboto-Italic.ttf
          style: italic
```

```dart
// Use in app
MaterialApp(
    theme: ThemeData(
        fontFamily: 'Roboto',
    ),
)

// Or for specific text
Text(
    'Hello World',
    style: TextStyle(
        fontFamily: 'Roboto',
        fontWeight: FontWeight.w700,
    ),
)
```

## Common Scenarios

**Scenario 1: Asset works in debug but not in release.**
Ensure the asset path is correct and the file exists in the build output. Use `flutter build` to test.

**Scenario 2: Font not rendering correctly.**
Check that the font family name in `pubspec.yaml` matches what you use in `TextStyle`. The family name must be exactly the same.

**Scenario 3: Asset loaded from wrong directory.**
Relative paths in `pubspec.yaml` are relative to the project root, not the lib/ directory.

## Prevent It

1. **Use `flutter pub get` after changing `pubspec.yaml`** to ensure assets are registered.

2. **Keep asset names lowercase** to avoid case-sensitivity issues across platforms.

3. **Test asset loading on both debug and release builds** to catch build-specific issues.
