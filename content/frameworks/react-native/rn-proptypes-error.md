---
title: "[Solution] React Native PropTypes Validation Warning"
description: "react-native PropTypes validation warnings or errors when mismatched prop types cause silent rendering failures in React Native components"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The PropTypes validation error occurs when a component receives a prop with an unexpected type. React Native only validates PropTypes in development mode. In production these mismatches silently break the layout or cause undefined method calls.

## Common Causes

- PropTypes.string expected but a number is passed
- Required prop completely omitted from the parent component
- PropTypes.shape does not match the nested object structure
- Boolean prop passed as a string ("true" instead of true)
- PropTypes.arrayOf expects an array but null or undefined is passed
- React Native specific prop types like EdgeInsetsPropType not matched

## How to Fix

1. Define PropTypes explicitly:

```javascript
import PropTypes from 'prop-types';

function Avatar({ name, size }) {
  return <Text style={{ fontSize: size }}>{name}</Text>;
}

Avatar.propTypes = {
  name: PropTypes.string.isRequired,
  size: PropTypes.number,
};

Avatar.defaultProps = {
  size: 16,
};
```

2. For TypeScript users, replace PropTypes with interfaces:

```typescript
interface AvatarProps {
  name: string;
  size?: number;
}
const Avatar: React.FC<AvatarProps> = ({ name, size = 16 }) => { ... };
```

3. Convert booleans correctly:

```javascript
// Bad: passes "true" as string
<Button disabled="true" />
// Good: passes boolean
<Button disabled={true} />
```

## Examples

```javascript
// Error: Warning: Failed prop type: Invalid prop `width` of type `string` supplied to `Image`, expected `number`
// Fix:
<Image source={img} width={200} /> // not width="200"
```

## Related Errors

- [TypeScript Error]({{< relref "/frameworks/react-native/rn-typescript-error" >}})
