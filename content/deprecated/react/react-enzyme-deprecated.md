---
title: "[Solution] Deprecated Function Migration: Enzyme to React Testing Library"
description: "Migrate from deprecated Enzyme to React Testing Library."
deprecated_function: "Enzyme's shallow/mount"
replacement_function: "React Testing Library render"
languages: ["react"]
deprecated_since: "React 16+"
---

# [Solution] Deprecated Function Migration: Enzyme to React Testing Library

The `Enzyme's shallow/mount` has been deprecated in favor of `React Testing Library render`.

## Migration Guide

React Testing Library tests behavior.

## Before (Deprecated)

```react
import { shallow } from 'enzyme';
const wrapper = shallow(<MyComponent />);
expect(wrapper.find('.btn')).toHaveLength(1);
```

## After (Modern)

```react
import { render, screen } from '@testing-library/react';
render(<MyComponent />);
expect(screen.getByRole('button')).toBeInTheDocument();
```

## Key Differences

- React Testing Library tests behavior
