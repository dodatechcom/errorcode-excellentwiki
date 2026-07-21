---
title: "[Solution] Laravel View Data Undefined Variable"
description: "Fix Laravel view variable not defined or undefined array key. Resolve undefined data passed to Blade templates."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when a Blade template references a variable that was not passed from the controller or is misspelled.

## Common Causes

- Controller does not pass the variable to the view
- Variable name is misspelled in the Blade template
- Variable is conditionally set but template assumes it exists
- Partial or component receives undefined variable
- `compact()` references a variable that does not exist in scope

## How to Fix

1. Always pass required variables from the controller:

```php
public function show(int $id)
{
    $order = Order::findOrFail($id);
    return view('orders.show', compact('order'));
}
```

2. Use the null coalescing operator in Blade:

```php
{{ $order->notes ?? 'No notes available' }}
```

3. Provide default values with `@isset`:

```php
@isset($discount)
    <p>Discount: {{ $discount }}%</p>
@endisset
```

4. Use `View::share` for global data:

```php
View::share('appName', config('app.name'));
```

## Examples

```php
// Blade template uses $user but controller does not pass it
return view('dashboard.index');
// ErrorException: Undefined variable $user

// Fix: pass the user explicitly
return view('dashboard.index', ['user' => auth()->user()]);
```
