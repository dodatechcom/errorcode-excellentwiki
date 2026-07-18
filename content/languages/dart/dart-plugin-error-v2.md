---
title: "[Solution] Dart Unable to Load Asset - Plugin Not Found Error Fix"
description: "Fix Dart unable to load asset or plugin not found error. Learn why assets fail to load, how pubspec.yaml asset paths work, and plugin resolution issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 4
---

## What This Error Means

An `Unable to load asset` error occurs when Flutter cannot locate or read an asset file declared in `pubspec.yaml`. A `plugin not found` error occurs when a Dart package or Flutter plugin cannot be resolved during build or runtime. Both errors prevent the app from building or running correctly.

## Why It Happens

For asset errors, the file path in `pubspec.yaml` does not match the actual file location. Flutter asset paths are relative to the `pubspec.yaml` file, not the project root. A path like `assets/images/logo.png` must have the file at `<project>/assets/images/logo.png`. If the directory structure does not match, the asset fails to load.

Assets must also be listed explicitly. Flutter does not automatically include all files in a directory. If you add a new image but forget to update `pubspec.yaml`, it is not bundled with the app.

Plugin errors occur when a package depends on native code (iOS, Android, web) that has not been built. Running `flutter pub get` resolves Dart dependencies but does not build native plugins. You must run `flutter build` or use platform-specific build commands.

## How to Fix It

Verify the asset path matches the file system exactly:

```yaml
# pubspec.yaml
flutter:
  assets:
    - assets/images/logo.png
    - assets/fonts/
```

Check that files exist at the specified paths relative to pubspec.yaml:

```bash
ls -la assets/images/logo.png
```

Use glob patterns to include entire directories:

```yaml
flutter:
  assets:
    - assets/images/
    - assets/data/*.json
```

For plugins, ensure native dependencies are built:

```bash
flutter clean
flutter pub get
flutter run
```

Check that the plugin supports your platform. A plugin designed for Android only will fail on iOS:

```yaml
dependencies:
  some_plugin: ^1.0.0
  # Check pub.dev for platform support
```

For web assets, ensure files are in the `web/` directory or declared as assets:

```yaml
flutter:
  assets:
    - web/icons/favicon.png
```

Verify the asset bundle identifier in build configurations:

```bash
flutter build apk --verbose 2>&1 | grep -i asset
```

## Common Mistakes

- Using absolute paths instead of paths relative to pubspec.yaml
- Adding new assets without updating pubspec.yaml
- Typo in the file path, including case sensitivity on Linux
- Not running `flutter clean` after changing asset declarations
- Assuming plugins build native code automatically without platform builds
- Using `pub get` instead of `flutter pub get` for Flutter projects
- Forgetting that asset directories require a trailing slash to include all files

## Related Pages

- [Dart Plugin Error](/languages/dart/dart-plugin-error/)
- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart Navigation Error](/languages/dart/dart-navigation-error/)
- [Dart IO Error](/languages/dart/dart-io-error/)
- [Dart Missing Override](/languages/dart/dart-missing-override/)
