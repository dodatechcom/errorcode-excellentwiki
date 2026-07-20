---
title: "[Solution] JavaScript Angular Router Navigation Error — How to Fix"
description: "Fix JavaScript Angular Router route configuration, lazy loading, guard/resolver errors, and NavigationError handling."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 805
---

# JavaScript Angular Router Navigation Error

A `NavigationError`, `TypeError`, or `Error: NG04002` occurs when Angular Router encounters invalid route configurations, lazy loading modules fail to resolve, guards throw exceptions, or resolvers time out.

## Why It Happens

Angular Router errors arise from missing component imports in route definitions, incorrect `loadChildren` paths, guards that return unexpected values, resolvers that do not complete, and `forRoot`/`forChild` misuse.

## Common Error Messages

- `Error: NG04002: Cannot match any routes. URL Segment: 'xxx'`
- `TypeError: Cannot read properties of undefined (reading 'component')`
- `Error: Cannot load module: 'app/admin/admin.module'`
- `Error: NavigationError: Maximum call stack size exceeded`
- `Error: RouterModule: forRoot() called twice`

## How to Fix It

### Fix 1: Define routes with components

```typescript
import { NgModule } from '@angular/core'
import { RouterModule, Routes } from '@angular/router'
import { HomeComponent } from './home.component'

const routes: Routes = [
  // ❌ Wrong - missing component
  // { path: 'home' }

  // ✅ Correct
  { path: 'home', component: HomeComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

### Fix 2: Lazy loading with loadChildren

```typescript
const routes: Routes = [
  {
    path: 'admin',
    // ❌ Wrong - incorrect path
    // loadChildren: () => import('./admin.module').then(m => m.AdminModule)

    // ✅ Correct
    loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule)
  }
]
```

### Fix 3: Route guards must return boolean or UrlTree

```typescript
import { Injectable } from '@angular/core'
import { CanActivate, Router, UrlTree } from '@angular/router'

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private router: Router) {}

  canActivate(): boolean | UrlTree {
    // ❌ Wrong - returning void or undefined
    // ✅ Correct
    return isLoggedIn ? true : this.router.parseUrl('/login')
  }
}
```

### Fix 4: RouterModule import correctly

```typescript
@NgModule({
  // ❌ Wrong - forRoot in child module
  // imports: [RouterModule.forRoot(routes)]

  // ✅ Correct - forChild in feature modules
  imports: [RouterModule.forChild(routes)]
})
export class FeatureModule {}
```

## Examples

Route resolver that must complete:

```typescript
@Injectable({ providedIn: 'root' })
export class UserResolver implements Resolve<User> {
  constructor(private api: UserService) {}

  resolve(route: ActivatedRouteSnapshot): Observable<User> {
    // ✅ Must return Observable that completes
    return this.api.getUser(route.paramMap.get('id')!)
  }
}
```

## Related Errors

- [Angular Error](/languages/javascript/angular-error)
- [Angular HTTP Error](/languages/javascript/angular-http-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
