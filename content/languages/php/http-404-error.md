---
title: "[Solution] PHP HTTP 404 Not Found — Script or Page Not Found"
description: "Fix PHP HTTP 404 Not Found: script/page not found. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1102
---

# PHP HTTP 404 Not Found — Script or Page Not Found

An HTTP 404 Not Found error means the server cannot find the requested resource. In PHP applications, this typically results from incorrect file paths, broken routing, missing `.htaccess` rules, or disabled URL rewriting modules.

## Common Causes

```php
<?php
// Incorrect include path
include '/wrong/path/to/file.php'; // Warning + 404

// Broken header redirect
header('Location: /nonexistent-page.php'); // 404

// Using $_SERVER['REQUEST_URI'] without validation
$file = $_SERVER['REQUEST_URI'];
readfile($file); // 404 if file doesn't exist
```

## How to Fix

### Fix 1: Verify File Paths

```php
<?php
// Check if a file exists before including it
function safeInclude(string $path, array $allowedDirs = []): bool
{
    $realPath = realpath($path);

    if ($realPath === false || !file_exists($realPath)) {
        http_response_code(404);
        echo "Page not found: " . htmlspecialchars($path);
        return false;
    }

    if (!empty($allowedDirs)) {
        $allowed = false;
        foreach ($allowedDirs as $dir) {
            if (strpos($realPath, realpath($dir)) === 0) {
                $allowed = true;
                break;
            }
        }

        if (!$allowed) {
            http_response_code(403);
            echo "Access denied";
            return false;
        }
    }

    include $realPath;
    return true;
}

// Usage
$pages = __DIR__ . '/pages';
safeInclude($pages . '/about.php', [$pages]);
```

### Fix 2: Implement Proper Routing

```php
<?php
// Simple router with 404 handling
function route(string $uri): void
{
    $routes = [
        '/'          => 'pages/home.php',
        '/about'     => 'pages/about.php',
        '/contact'   => 'pages/contact.php',
        '/api/users' => 'api/users.php',
    ];

    // Remove query string and trailing slash
    $path = parse_url($uri, PHP_URL_PATH);
    $path = rtrim($path, '/') ?: '/';

    if (isset($routes[$path])) {
        $file = __DIR__ . $routes[$path];
        if (file_exists($file)) {
            require $file;
            return;
        }
    }

    // 404 — no matching route
    http_response_code(404);
    require __DIR__ . '/pages/404.php';
}

route($_SERVER['REQUEST_URI']);
```

### Fix 3: Configure Apache .htaccess

```apache
# .htaccess — enable URL rewriting
RewriteEngine On

# If the requested file or directory doesn't exist, route to index.php
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php?route=$1 [QSA,L]

# Custom 404 error document
ErrorDocument 404 /404.php
```

### Fix 4: Configure Nginx for PHP Applications

```nginx
# nginx.conf
server {
    listen 80;
    server_name example.com;
    root /var/www/html;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    # Custom 404 page
    error_page 404 /404.php;
    location = /404.php {
        internal;
    }
}
```

### Fix 5: Check mod_rewrite Status

```bash
# Check if mod_rewrite is enabled (Apache)
apachectl -M | grep rewrite

# Enable mod_rewrite on Ubuntu/Debian
sudo a2enmod rewrite
sudo systemctl restart apache2

# Enable mod_rewrite on CentOS/RHEL
sudo yum install mod_rewrite
sudo systemctl restart httpd

# Verify .htaccess is allowed
# In Apache config, ensure AllowOverride is not set to None
# <Directory /var/www/html>
#     AllowOverride All
# </Directory>
```

## Examples

```php
<?php
// Example 1: SPA-style routing with fallback
$requestedPath = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$requestedPath = rtrim($requestedPath, '/') ?: '/';

$validRoutes = ['/', '/about', '/products', '/contact', '/blog'];

if (in_array($requestedPath, $validRoutes)) {
    $page = __DIR__ . '/pages' . $requestedPath . '.php';
    if (file_exists($page)) {
        require $page;
    } else {
        http_response_code(404);
        require __DIR__ . '/pages/404.php';
    }
} else {
    // Check for dynamic routes
    if (preg_match('#^/blog/(\d+)$#', $requestedPath, $matches)) {
        require __DIR__ . '/pages/blog-post.php?id=' . $matches[1];
    } else {
        http_response_code(404);
        require __DIR__ . '/pages/404.php';
    }
}

// Example 2: API 404 response
function apiRoute(string $method, string $uri): void
{
    $path = parse_url($uri, PHP_URL_PATH);

    if ($path === '/api/users' && $method === 'GET') {
        echo json_encode(['users' => []]);
        return;
    }

    http_response_code(404);
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'Endpoint not found',
        'path'  => $path,
    ]);
}
```

## Related Errors

- [PHP File Not Found Error]({{< relref "/languages/php/file-not-found-error" >}})
- [PHP cURL Connection Error]({{< relref "/languages/php/curl-connection-error" >}})
- [PHP HTTP 403 Forbidden]({{< relref "/languages/php/http-403-error" >}})
