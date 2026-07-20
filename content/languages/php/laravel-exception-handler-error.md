---
title: "[Solution] PHP LARAVEL_EXCEPTION_HANDLER_ERROR — Laravel ExceptionHandler Error"
description: "Fix PHP Laravel ExceptionHandler errors. Check report/render methods, handle exception types, and configure error handling. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 124
---

# PHP LARAVEL_EXCEPTION_HANDLER_ERROR — Laravel ExceptionHandler Error

The Laravel exception handler failed to process or render an exception. This error occurs when the `report()` or `render()` methods throw an exception themselves, exception types are not handled, or the handler configuration is incorrect.

## Common Causes

### render() method throws exception

```php
<?php
// app/Exceptions/Handler.php
public function render($request, Throwable $e)
{
    if ($e instanceof ModelNotFoundException) {
        return response()->json([
            'error' => $e->getModel() . ' not found',
        ], 404);
    }
    // Missing return statement for other exceptions
    // Exception falls through to default handler
}
?>
```

### Wrong exception class in report()

```php
<?php
public function report(Throwable $e)
{
    if ($e instanceof SomeUndefinedException) {
        // Class does not exist
        Log::error('Handled: ' . $e->getMessage());
    }
    parent::report($e);
}
// Error: Class 'SomeUndefinedException' not found
?>
```

### Exception type mismatch in render()

```php
<?php
public function render($request, Throwable $e)
{
    if ($e instanceof HttpException) {
        return response()->json(['error' => 'HTTP error'], $e->getStatusCode());
    }
    // Missing handling for non-HTTP exceptions in API context
}
?>
```

### Circular exception in handler

```php
<?php
public function render($request, Throwable $e)
{
    if ($e instanceof ValidationException) {
        abort(500); // abort triggers new exception
        // which triggers render() again
    }
}
?>
```

### Missing parent::report() call

```php
<?php
public function report(Throwable $e)
{
    if ($e instanceof CustomException) {
        Log::error($e->getMessage());
        return; // skips parent::report()
        // exception not logged to default handler
    }
    parent::report($e);
}
?>
```

## How to Fix

### Fix 1: Handle All Exception Types in render()

```php
<?php
namespace App\Exceptions;

use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Illuminate\Auth\AuthenticationException;
use Illuminate\Validation\ValidationException;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;
use Throwable;

class Handler extends ExceptionHandler
{
    protected $dontFlash = [
        'current_password',
        'password',
        'password_confirmation',
    ];

    public function register(): void
    {
        $this->reportable(function (Throwable $e) {
            // Report to external service
        });
    }

    public function render($request, Throwable $e)
    {
        if ($request->expectsJson()) {
            return $this->handleApiException($request, $e);
        }

        return parent::render($request, $e);
    }

    private function handleApiException($request, Throwable $e)
    {
        if ($e instanceof ValidationException) {
            return response()->json([
                'message' => 'Validation failed',
                'errors' => $e->errors(),
            ], 422);
        }

        if ($e instanceof ModelNotFoundException) {
            return response()->json([
                'message' => class_basename($e->getModel()) . ' not found',
            ], 404);
        }

        if ($e instanceof AuthenticationException) {
            return response()->json(['message' => 'Unauthenticated'], 401);
        }

        $statusCode = method_exists($e, 'getStatusCode') ? $e->getStatusCode() : 500;

        return response()->json([
            'message' => $e->getMessage() ?: 'Server error',
        ], $statusCode);
    }
}
?>
```

### Fix 2: Use report() Correctly

```php
<?php
public function report(Throwable $e): void
{
    if ($this->shouldReport($e)) {
        // Log to external service
        if ($this->isNetworkException($e)) {
            // Retry logic for network errors
            Cache::increment('network_error_count');
        }

        if ($this->isCriticalException($e)) {
            // Notify admin
            Mail::to('admin@example.com')->send(new CriticalErrorAlert($e));
        }
    }

    parent::report($e);
}

private function shouldReport(Throwable $e): bool
{
    $ignored = [
        \Symfony\Component\HttpKernel\Exception\NotFoundHttpException::class,
    ];

    foreach ($ignored as $class) {
        if ($e instanceof $class) {
            return false;
        }
    }

    return true;
}
?>
```

### Fix 3: Prevent Circular Exceptions

```php
<?php
public function render($request, Throwable $e)
{
    // Prevent recursive rendering
    if ($request->has('exception_rendered')) {
        return response('Internal Server Error', 500);
    }

    $request->merge(['exception_rendered' => true]);

    if ($e instanceof ValidationException) {
        return redirect()->back()->withErrors($e->errors())->withInput();
    }

    if ($e instanceof ModelNotFoundException) {
        return response()->json(['error' => 'Not found'], 404);
    }

    return parent::render($request, $e);
}
?>
```

### Fix 4: Handle Specific HTTP Status Codes

```php
<?php
public function render($request, Throwable $e)
{
    if ($request->expectsJson()) {
        $response = [
            'message' => $e->getMessage(),
        ];

        if (config('app.debug')) {
            $response['exception'] = get_class($e);
            $response['trace'] = $e->getTrace();
        }

        $statusCode = 500;
        if (method_exists($e, 'getStatusCode')) {
            $statusCode = $e->getStatusCode();
        } elseif ($e instanceof \Illuminate\Auth\AuthenticationException) {
            $statusCode = 401;
        } elseif ($e instanceof \Illuminate\Validation\ValidationException) {
            $statusCode = 422;
            $response['errors'] = $e->errors();
        }

        return response()->json($response, $statusCode);
    }

    return parent::render($request, $e);
}
?>
```

### Fix 5: Register Exception Callbacks

```php
<?php
// app/Providers/AppServiceProvider.php
use Illuminate\Support\Facades\Log;

public function boot(): void
{
    // Register callbacks in the handler instead
}

// app/Exceptions/Handler.php
public function register(): void
{
    $this->reportable(function (Throwable $e) {
        if ($e instanceof \Symfony\Component\Mailer\Exception\TransportExceptionInterface) {
            Log::error('Mailer transport failed: ' . $e->getMessage());
        }
    });

    $this->renderable(function (NotFoundHttpException $e, $request) {
        if ($request->is('api/*')) {
            return response()->json(['error' => 'Resource not found'], 404);
        }
    });
}
?>
```

## Examples

### Complete Exception Handler

```php
<?php
namespace App\Exceptions;

use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Illuminate\Auth\AuthenticationException;
use Illuminate\Validation\ValidationException;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Symfony\Component\HttpKernel\Exception\TooManyRequestsHttpException;
use Throwable;

class Handler extends ExceptionHandler
{
    public function register(): void
    {
        $this->reportable(function (Throwable $e) {
            if ($e instanceof TooManyRequestsHttpException) {
                Log::warning('Rate limited: ' . request()->ip());
            }
        });

        $this->renderable(function (Throwable $e, $request) {
            if ($request->expectsJson() && !app()->hasBeenBooted()) {
                return response()->json(['error' => 'Application not ready'], 503);
            }
        });
    }

    public function render($request, Throwable $e)
    {
        if ($request->expectsJson()) {
            return $this->handleJsonException($e);
        }
        return parent::render($request, $e);
    }

    private function handleJsonException(Throwable $e)
    {
        $statusCode = method_exists($e, 'getStatusCode') ? $e->getStatusCode() : 500;
        $message = $e->getMessage() ?: 'Server error';

        $data = ['message' => $message];
        if ($e instanceof ValidationException) {
            $data['errors'] = $e->errors();
            $statusCode = 422;
        }

        return response()->json($data, $statusCode);
    }
}
?>
```

## Related Errors

- [Laravel Model Not Found]({{< relref "/languages/php/laravel-model-not-found" >}})
- [Laravel Validation Error]({{< relref "/languages/php/laravel-validation-error" >}})
- [Symfony HttpKernel Error]({{< relref "/languages/php/symfony-http-kernel-error" >}})
