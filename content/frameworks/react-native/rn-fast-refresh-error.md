---
title: "Fast Refresh - module update error"
description: "React Native Fast Refresh fails to apply module updates during development, requiring a full reload"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

Fast Refresh module update errors occur when the React Native development server cannot apply code changes to the running app. Fast Refresh works by replacing module implementations in place, but certain code patterns prevent it from working.

## Common Causes

- Changes to non-component modules with side effects
- File exports only default export as a React component
- Class components renamed or restructured significantly
- Changes to root-level module initialization code
- Syntax errors preventing the module from compiling

## How to Fix

1. Use named exports alongside default exports for better refresh:

```javascript
// Good for Fast Refresh
export const UserProfile = ({ name }) => <Text>{name}</Text>;
export default UserProfile;
```

2. Separate side effects from component definitions:

```javascript
// components/Tracker.js
import { initTracker } from './tracking';

initTracker(); // side effect - run separately

export const TrackerComponent = () => {
  // component logic
};
```

3. Force a full reload when Fast Refresh fails:

```bash
# Press 'r' in Metro terminal to reload
# Or shake device and select "Reload"
```

4. Check Metro logs for the specific failure:

```bash
npx react-native start --verbose
```

5. Disable Fast Refresh temporarily if needed:

```bash
npx react-native start --no-fast-refresh
```

## Examples

```javascript
// This can break Fast Refresh
const styles = StyleSheet.create({});
// ... only default export follows

// Better: named export first
export const MyComponent = () => <View />;
export default MyComponent;
```

```bash
# Metro output
warn Fast Refresh is unable to apply the update.
An error occurred during the update. Falling back to full reload.
```

## Related Errors

- [Bundler error]({{< relref "/frameworks/react-native/rn-bundler-error-v2" >}})
- [Reanimated error]({{< relref "/frameworks/react-native/rn-reanimated-error" >}})
