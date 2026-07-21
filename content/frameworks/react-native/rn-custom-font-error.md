---
title: "[Solution] React Native Custom Font Not Displayed"
description: "react-native custom font family not rendering on iOS or Android due to file path issues or misconfigured plist/asset exports in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The custom font error occurs when a TTF or OTF font file bundled in the project does not appear in the running application. Android loads fonts from the assets/fonts/ directory, whereas iOS requires an Info.plist entry naming all custom fonts.

## Common Causes

- Font files not placed in android/app/src/main/assets/fonts
- Info.plist missing the UIAppFonts key for the custom font
- Font file name does not match the actual PostScript name of the font
- Font license restricts embedding resulting in a corrupt or empty glyph table
- Running android:mergeDex as true without specifying the font path
- metro.config.cjs does not include .ttf or .otf in assetExts

## How to Fix

1. Place font files correctly for both platforms:

```bash
# Android
mkdir -p android/app/src/main/assets/fonts
cp fonts/Inter-Regular.ttf android/app/src/main/assets/fonts/

# iOS
mkdir -p ios/YourApp/
cp fonts/Inter-Regular.ttf ios/YourApp/
```

2. Add fonts to iOS Info.plist:

```xml
<key>UIAppFonts</key>
<array>
  <string>Inter-Regular.ttf</string>
  <string>Inter-Bold.ttf</string>
</array>
```

3. Rebuild and verify font availability:

```javascript
import { Platform } from 'react';
const fontFamily = Platform.select({
  ios: 'Inter',
  android: 'Inter',
});
```

## Examples

```javascript
// Error: Text renders as a placeholder box or invisible
<Text style={{ fontFamily: 'Inter' }}>Hello</Text>

// Fix: use exact PostScript name
<Text style={{ fontFamily: 'Inter-Regular' }}>Hello</Text>
```

## Related Errors

- [Build Error]({{< relref "/frameworks/react-native/rn-build-error" >}})
