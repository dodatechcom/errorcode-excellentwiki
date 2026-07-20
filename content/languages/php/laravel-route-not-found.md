---
title: "[Solution] PHP LARAVEL_ROUTE_NOT_FOUND — Route Not Defined"
description: "Fix PHP LARAVEL_ROUTE_NOT_FOUND by checking route definitions, clearing route cache, and verifying controller method. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 123
---

# PHP LARAVEL_ROUTE_NOT_FOUND — Route Not Defined

A route was not found or is invalid in Laravel. This error occurs when the route is not defined, the route name is incorrect, or the route cache is stale.

## Common Causes

```php
// Route not defined in routes/web.php
Route::get('/about', [PageController::class, 'about']);
// But URL is /about-us (typo)
```

```php
// Wrong route name
route('user.show', $id); // route is actually 'users.show'
```

```php
// Route cache is stale
// Route was added but cache wasn't cleared
// php artisan route:cache was run before adding new routes
```

```php
// Controller method doesn't exist
Route::get('/dashboard', [DashboardController::class, 'index']);
// But DashboardController has no index() method
```

```php
// Route defined in wrong file or group
Route::get('/api/users', [UserController::class, 'index']);
// But UserController is only loaded in api.php, not web.php
```

## How to Fix

### Fix 1: Check Route Definitions

```php
// routes/web.php
use App\Http\Controllers\UserController;
use App\Http\Controllers\PostController;
use App\Http\Controllers\DashboardController;

// Simple routes
Route::get('/', [DashboardController::class, 'index'])->name('home');
Route::get('/about', [PageController::class, 'about'])->name('about');
Route::get('/contact', [PageController::class, 'contact'])->name('contact');

// Resource routes
Route::resource('users', UserController::class);
Route::resource('posts', PostController::class);

// Route groups
Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('/dashboard', [AdminController::class, 'dashboard'])->name('dashboard');
    Route::resource('users', AdminUserController::class);
});

// API routes
Route::prefix('api')->group(function () {
    Route::get('/users', [ApiUserController::class, 'index']);
});
```

### Fix 2: Clear Route Cache

```bash
# Clear route cache
php artisan route:clear

# List all routes
php artisan route:list

# List specific routes
php artisan route:list --name=user

# List routes with controller
php artisan route:list --controller=UserController

# Generate fresh route cache
php artisan route:cache

# Debug route
php artisan route:list --path=dashboard
```

### Fix 3: Verify Route Names and URLs

```php
// Check route name exists
if (Route::has('users.index')) {
    $url = route('users.index');
}

// Generate URL safely
$url = route('users.show', ['user' => $user->id]);
$url = route('posts.index', ['category' => 'tech']);

// Redirect to named route
return redirect()->route('users.show', $user);
return to_route('users.show', $user);

// In Blade templates
<a href="{{ route('users.show', $user) }}">View User</a>
<a href="{{ route('posts.index') }}">All Posts</a>
```

### Fix 4: Handle Route Not Found

```php
// In App/Exceptions/Handler.php (Laravel 10.x)
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;

class Handler extends ExceptionHandler
{
    protected $dontFlash = [
        'current_password',
        'password',
        'password_confirmation',
    ];

    public function register(): void
    {
        $this->reportable(function (NotFoundHttpException $e) {
            if (request()->expectsJson()) {
                return response()->json([
                    'error' => 'Route not found',
                ], 404);
            }
        });
    }
}

// In App/Exceptions/Handler.php (Laravel 11+)
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;

public function register(): void
{
    $this->renderable(function (NotFoundHttpException $e, $request) {
        if ($request->is('api/*')) {
            return response()->json([
                'error' => 'API endpoint not found',
            ], 404);
        }
    });
}
```

## Examples

```php
// Complete route setup example
// routes/web.php
use App\Http\Controllers\{
    Auth\LoginController,
    Auth\RegisterController,
    DashboardController,
    ProfileController,
    PostController
};

// Public routes
Route::get('/', [DashboardController::class, 'index'])->name('home');
Route::get('/about', function () {
    return view('pages.about');
})->name('about');

// Authentication routes
Route::middleware('guest')->group(function () {
    Route::get('/login', [LoginController::class, 'showLoginForm'])->name('login');
    Route::post('/login', [LoginController::class, 'login']);
    Route::get('/register', [RegisterController::class, 'showRegistrationForm'])->name('register');
    Route::post('/register', [RegisterController::class, 'register']);
});

// Authenticated routes
Route::middleware('auth')->group(function () {
    Route::post('/logout', [LoginController::class, 'logout'])->name('logout');
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::put('/profile', [ProfileController::class, 'update'])->name('profile.update');

    Route::resource('posts', PostController::class);
});
```

## Related Errors

- [Symfony Route Error](/languages/php/symfony-route-error)
- [CodeIgniter Routing Error](/languages/php/codeigniter-routing-error)
- [Laravel Model Not Found](/languages/php/laravel-model-not-found)
- [Laravel Token Mismatch](/languages/php/laravel-token-mismatch)
