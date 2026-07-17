---
title: "RedBox error - undefined is not an object"
description: "React Native RedBox error when accessing undefined as an object, typically caused by null data in component props or state"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The RedBox error "undefined is not an object (evaluating 'X.Y')" occurs when your code tries to access a property or method on an undefined value. This is one of the most common React Native runtime errors.

## Common Causes

- Props not passed to a component or passed as undefined
- API response returning null/undefined instead of expected data
- Navigating to a screen before params are available
- Forgetting to initialize state with proper default values
- Destructuring properties from an undefined object

## How to Fix

1. Add optional chaining and nullish coalescing for safe access:

```javascript
const UserProfile = ({ user }) => {
  const name = user?.profile?.name ?? 'Guest';
  return <Text>{name}</Text>;
};
```

2. Initialize state with safe defaults:

```javascript
const [data, setData] = useState({ items: [], total: 0 });
```

3. Guard against undefined params in navigation:

```javascript
const ProductScreen = ({ route }) => {
  const productId = route?.params?.productId;
  if (!productId) return <LoadingSpinner />;
  // ...
};
```

4. Use PropTypes or TypeScript to catch missing props at development time:

```typescript
interface Props {
  title: string;
  count: number;
}

const Counter: React.FC<Props> = ({ title, count }) => (
  <Text>{title}: {count}</Text>
);
```

## Examples

```javascript
// RedBox: undefined is not an object (evaluating 'user.name')
const ProfileCard = ({ user }) => (
  <Text>{user.name}</Text> // user could be undefined
);

// Fix: safe access
const ProfileCard = ({ user }) => (
  <Text>{user?.name ?? 'Anonymous'}</Text>
);
```

## Related Errors

- [Native module error]({{< relref "/frameworks/react-native/native-module-error" >}})
- [Network error]({{< relref "/frameworks/react-native/rn-network-error" >}})
