---
title: "React Native Testing Library - render error"
description: "React Native Testing Library fails to render a component during tests due to missing providers or configuration issues"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The React Native Testing Library render error occurs when a component cannot be properly rendered in the test environment. This is typically caused by missing context providers, improper mocking, or test configuration issues.

## Common Causes

- Missing NavigationContainer or other required providers
- Native module not mocked for the test environment
- Jest configuration missing React Native setup file
- Component depends on context that is not provided in tests
- Async rendering not properly awaited

## How to Fix

1. Wrap tested components with required providers:

```javascript
import { render } from '@testing-library/react-native';
import { NavigationContainer } from '@react-navigation/native';

const renderWithProviders = (component) => {
  return render(
    <NavigationContainer>
      {component}
    </NavigationContainer>
  );
};

test('renders profile', () => {
  const { getByText } = renderWithProviders(
    <ProfileScreen userId="123" />
  );
  expect(getByText('Profile')).toBeTruthy();
});
```

2. Mock native modules in `jest/setup.js`:

```javascript
jest.mock('react-native-reanimated', () =>
  require('react-native-reanimated/mock')
);

jest.mock('@react-native-async-storage/async-storage', () =>
  require('@react-native-async-storage/async-storage/jest/async-storage-mock')
);
```

3. Configure Jest for React Native:

```javascript
// jest.config.js
module.exports = {
  preset: 'react-native',
  setupFilesAfterSetup: ['./jest/setup.js'],
  transformIgnorePatterns: [
    'node_modules/(?!(react-native|@react-native|@react-navigation)/)',
  ],
};
```

4. Handle async rendering:

```javascript
import { render, waitFor } from '@testing-library/react-native';

test('loads user data', async () => {
  const { getByText } = render(<UserProfile userId="123" />);
  await waitFor(() => {
    expect(getByText('John')).toBeTruthy();
  });
});
```

## Examples

```javascript
// Error: Invariant Violation: Element type is invalid
// Missing navigation provider
const { getByText } = render(<ScreenWithNav />);
// Fix: wrap with NavigationContainer
```

```javascript
// Error: Cannot find module 'react-native-reanimated'
// Fix: add mock
jest.mock('react-native-reanimated', () =>
  require('react-native-reanimated/mock')
);
```

## Related Errors

- [RedBox error]({{< relref "/frameworks/react-native/rn-redbox-error-v2" >}})
- [Fast Refresh error]({{< relref "/frameworks/react-native/rn-fast-refresh-error" >}})
