---
title: "[Solution] JavaScript Angular Runtime Error — How to Fix"
description: "Fix JavaScript Angular dependency injection, component creation, template parsing, module imports, and ChangeDetection errors."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 803
---

# JavaScript Angular Runtime Error

An `Error: NGxxx`, `TypeError`, or `CompileError` occurs when Angular's DI system cannot resolve providers, component selectors conflict, template parser detects invalid syntax, modules are incorrectly imported, or change detection cycles exceed limits.

## Why It Happens

Angular errors stem from unprovided dependencies, missing `@NgModule` declarations, template binding syntax mistakes, circular module imports, and improper `ChangeDetectionStrategy` usage that breaks UI updates.

## Common Error Messages

- `NullInjectorError: No provider for HttpClient`
- `Error: NG0304: 'component' is not a known element`
- `Error: NG0500: Infinite change detection detected`
- `TypeError: Cannot read properties of undefined (reading 'xxx')`
- `Error: Template parse errors: Unexpected closing tag`

## How to Fix It

### Fix 1: Register providers in modules

```typescript
import { NgModule } from '@angular/core'
import { HttpClientModule } from '@angular/common/http'

@NgModule({
  imports: [HttpClientModule], // ✅ Correct - provides HttpClient
  providers: []
})
export class AppModule {}
```

### Fix 2: Declare components properly

```typescript
import { NgModule } from '@angular/core'
import { UserComponent } from './user.component'

@NgModule({
  // ❌ Wrong - component not declared
  // bootstrap: [UserComponent]

  // ✅ Correct
  declarations: [UserComponent],
  exports: [UserComponent]
})
export class SharedModule {}
```

### Fix 3: Use ChangeDetectionStrategy correctly

```typescript
import { Component, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core'

@Component({
  selector: 'app-user',
  template: `{{ user.name }}`,
  // ❌ Wrong - OnPush without manual trigger
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserComponent {
  constructor(private cdr: ChangeDetectorRef) {}

  updateUser(data: any) {
    this.user = data
    this.cdr.markForCheck() // ✅ Required with OnPush
  }
}
```

### Fix 4: Template syntax

```html
<!-- ❌ Wrong - property binding without brackets -->
<!-- user name="{{ user.name }}" -->

<!-- ✅ Correct -->
<div>{{ user.name }}</div>
<input [value]="user.name">
<button (click)="save()">Save</button>
```

## Examples

Circular dependency in module imports:

```typescript
// ❌ Wrong - circular import between modules
// @NgModule({ imports: [ModuleB] }) class ModuleA {}
// @NgModule({ imports: [ModuleA] }) class ModuleB {}

// ✅ Correct - extract shared module
@NgModule({
  imports: [CommonModule],
  declarations: [SharedComponent],
  exports: [SharedComponent]
})
class SharedModule {}
```

## Related Errors

- [Angular HTTP Error](/languages/javascript/angular-http-error)
- [Angular Router Error](/languages/javascript/angular-router-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
