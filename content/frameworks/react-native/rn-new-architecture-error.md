---
title: "New Architecture - Turbo Module error"
description: "React Native New Architecture fails when Turbo Module specification is invalid or native code is not properly configured"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
tags: ["new-architecture", "turbo-module", "fabric", "codegen", "c++", "jni"]
weight: 5
---

The Turbo Module error in React Native's New Architecture occurs when native modules are not properly defined for the new bridgeless architecture. This includes missing Codegen specifications, incompatible native code, or build configuration issues.

## Common Causes

- Missing or invalid Turbo Module spec file
- Native code not updated for New Architecture
- Codegen not configured correctly in `build.gradle`
- Legacy native modules used without compatibility layer
- Fabric renderer conflicts with existing native components

## How to Fix

1. Define a proper Turbo Module spec:

```typescript
// specs/NativeStorage.ts
import type { TurboModule } from 'react-native';
import { TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  getItem(key: string): Promise<string | null>;
  setItem(key: string, value: string): Promise<void>;
}

export default TurboModuleRegistry.getEnforcing<Spec>('Storage');
```

2. Enable New Architecture in `android/gradle.properties`:

```properties
newArchEnabled=true
hermesEnabled=true
```

3. For iOS, enable in `ios/Podfile`:

```ruby
:hermes_enabled => true
:fabric_enabled => true
```

4. Regenerate Codegen after changes:

```bash
cd ios && pod install
cd ../android && ./gradlew generateCodegenSchemaFromJavaScript
```

5. Check compatibility with existing libraries:

```bash
npx react-native config | grep -i "turbo"
```

## Examples

```bash
# Build error with Turbo Module
> Task :app:generateCodegenSchemaFromJavaScript FAILED
Error: TurboModule 'Storage' was not found.
Make sure the native module is properly registered.
```

## Related Errors

- [Hermes error]({{< relref "/frameworks/react-native/rn-hermes-error" >}})
- [Linking error]({{< relref "/frameworks/react-native/rn-linking-error" >}})
