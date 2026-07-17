---
title: "Octane worker error"
description: "Laravel Octane throws worker errors when the application running in Swoole or RoadRunner encounters issues"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["octane", "swoole", "roadrunner", "worker", "persistent"]
weight: 5
---

This error occurs when Laravel Octane workers encounter issues related to long-lived application state, memory leaks, or incompatibility with singleton services that retain state between requests.

## Common Causes

- Singleton services retaining state between requests
- Memory leak from unclosed resources or growing collections
- Static variables not being reset between requests
- Octane incompatible with certain Laravel packages
- Worker timeout due to long-running operations

## How to Fix

1. Flush state between requests using the `Terminating` interface:

```php
class ClearState implements ShouldFlushState
{
    public function handle(): void
    {
        // Reset singleton state here
    }
}
```

2. Register flush handlers in `AppServiceProvider`:

```php
use Illuminate\Support\ServiceProvider;
use Laravel\Octane\Events\OperationTerminated;

class AppServiceProvider extends ServiceProvider
{
    public function boot(): void
    {
        if ($this->app->has('octane')) {
            $this->app['events']->listen(OperationTerminated::class, function () {
                // Reset state
                app()->forgetInstance('some-singleton');
            });
        }
    }
}
```

3. Configure Octane settings in `config/octane.php`:

```php
'swoole' => [
    'options' => [
        'worker_num' => 4,
        'max_request' => 1000,
        'max_coroutine' => 10000,
    ],
],
```

## Examples

```php
// Static variable persists between requests under Octane
class RequestCounter
{
    public static int $count = 0; // Never resets!
}

// Fix: Use instance state with flush
class RequestCounter implements ShouldFlushState
{
    public int $count = 0;
}
```

## Related Errors

- [Vapor error]({{< relref "/frameworks/laravel/vapor-error" >}})
- [Sail error]({{< relref "/frameworks/laravel/sail-error" >}})
