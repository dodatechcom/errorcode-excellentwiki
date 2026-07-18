---
title: "[Solution] JavaScript Stencil Compiler Error — How to Fix"
description: "Fix JavaScript Stencil compiler errors. Resolve build, component, and configuration issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript Stencil Compiler Error

A `CompilerError` or `BuildError` occurs when Stencil fails to compile components, encounters invalid decorators, or when the configuration is incompatible.

## Why It Happens

Stencil is a web components compiler. Errors arise when decorators are not properly used, when the build configuration is wrong, when components are not registered, or when the output targets are misconfigured.

## Common Error Messages

- `CompilerError: Invalid decorator`
- `BuildError: Component not found`
- `Error: @Component not found`
- `TypeError: render is not a function`

## How to Fix It

### Fix 1: Configure Stencil properly

```typescript
// stencil.config.ts
import { Config } from '@stencil/core';

export const config: Config = {
  namespace: 'my-app',
  outputTargets: [
    { type: 'dist' },
    { type: 'docs-readme' },
    { type: 'www', serviceWorker: null },
  ],
};
```

### Fix 2: Use decorators correctly

```typescript
import { Component, Prop, h } from '@stencil/core';

// Wrong — no decorators
// class MyComponent { render() { return <div>Hello</div>; } }

// Correct — use decorators
@Component({
  tag: 'my-component',
  shadow: true,
})
export class MyComponent {
  @Prop() name: string;
  @Prop({ reflect: true }) count: number = 0;

  render() {
    return (
      <div>
        Hello {this.name}!
        <button onClick={() => this.count++}>
          Count: {this.count}
        </button>
      </div>
    );
  }
}
```

### Fix 3: Handle lifecycle

```typescript
import { Component, Prop, State, Watch, h } from '@stencil/core';

@Component({
  tag: 'lifecycle-component',
  shadow: true,
})
export class LifecycleComponent {
  @Prop() userId: string;
  @State() user: any;

  @Watch('userId')
  async userIdChanged() {
    this.user = await fetchUser(this.userId);
  }

  connectedCallback() {
    this.userIdChanged();
  }

  render() {
    return <div>{this.user?.name}</div>;
  }
}
```

### Fix 4: Build and test

```bash
# Build components
npm run build

# Start dev server
npm run start

# Run tests
npm test
```

## Common Scenarios

- **Decorator missing** — Component class not decorated with @Component.
- **Prop not declared** — Property used but not decorated with @Prop.
- **Build failure** — Invalid TypeScript or JSX syntax.

## Prevent It

- Always use `@Component` decorator on component classes.
- Declare all props with `@Prop()` decorator.
- Use `npm run build` before `npm run start` for production builds.

## Related Errors

- [CompilerError](/javascript/compile-error/) — compilation failed
- [BuildError](/javascript/build-error/) — build failed
- [DecoratorError](/javascript/decorator-error/) — decorator invalid
