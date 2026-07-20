---
title: "[Solution] PHP HTTP 403 Forbidden — Permission Denied"
description: "Fix PHP HTTP 403 Forbidden: permission denied. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1103
---

# PHP HTTP 403 Forbidden — Permission Denied

An HTTP 403 Forbidden error means the server understood the request but refuses to authorize it. In PHP applications, this is commonly caused by incorrect file/directory permissions, misconfigured `.htaccess` rules, disabled directory indexing, or missing access control logic.

## Common Causes

```php
<?php
// Attempting to read a file without proper permissions
$data = file_get_contents('/etc/shadow'); // Warning + 403

// Serving a file from a protected directory
readfile('/var/www/private/secret.pdf'); // 403

// Missing authentication check
$user = $_SESSION['user'] ?? null;
// No check — page served without auth → 403 from middleware

// Upload directory listing disabled
// Accessing /uploads/ directly → 403 if directory indexing is off
```

## How to Fix

### Fix 1: Check and Set Correct File Permissions

```bash
# Check current permissions
ls -la /var/www/html/

# Set correct permissions for web files
sudo find /var/www/html -type f -exec chmod 644 {} \;
sudo find /var/www/html -type d -exec chmod 755 {} \;

# Ensure the web server user owns the files
sudo chown -R www-data:www-data /var/www/html/

# For writable directories (uploads, cache)
sudo chmod 775 /var/www/html/uploads
sudo chown -R www-data:www-data /var/www/html/uploads

# Check if SELinux is blocking access (CentOS/RHEL)
ls -Z /var/www/html/
# Fix SELinux context if needed
sudo restorecon -Rv /var/www/html/
```

### Fix 2: Configure .htaccess Access Control

```apache
# .htaccess — allow access to all files
# Remove any Deny directives that block access
<IfModule mod_authz_core.c>
    Require all granted
</IfModule>

# If you need to restrict specific directories:
<Directory "/var/www/html/private">
    Require all denied
</Directory>

# For password-protected directories:
<Directory "/var/www/html/admin">
    AuthType Basic
    AuthName "Admin Area"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>

# Re-enable directory listing if needed
Options +Indexes
IndexIgnore *.log *.tmp
```

### Fix 3: Handle Access Control in PHP

```php
<?php
// Simple role-based access control
function checkAccess(array $requiredRole = []): bool
{
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }

    $currentUser = $_SESSION['user'] ?? null;

    if ($currentUser === null) {
        http_response_code(403);
        echo json_encode(['error' => 'Authentication required']);
        return false;
    }

    if (!empty($requiredRole) && !in_array($currentUser['role'], $requiredRole)) {
        http_response_code(403);
        echo json_encode(['error' => 'Insufficient permissions']);
        return false;
    }

    return true;
}

// Usage
if (!checkAccess(['admin', 'editor'])) {
    exit;
}

// Serve admin page
echo "Welcome, admin!";
```

### Fix 4: Serve Files with Permission Checks

```php
<?php
function secureFileServe(string $filePath, string $allowedDir): void
{
    $fullPath = realpath($filePath);

    // Prevent directory traversal
    if ($fullPath === false || strpos($fullPath, realpath($allowedDir)) !== 0) {
        http_response_code(403);
        echo 'Access denied';
        return;
    }

    if (!file_exists($fullPath)) {
        http_response_code(404);
        echo 'File not found';
        return;
    }

    // Check file permissions
    if (!is_readable($fullPath)) {
        http_response_code(403);
        echo 'File not readable';
        return;
    }

    // Serve the file
    $mimeTypes = [
        'pdf'  => 'application/pdf',
        'jpg'  => 'image/jpeg',
        'png'  => 'image/png',
        'txt'  => 'text/plain',
    ];

    $ext = strtolower(pathinfo($fullPath, PATHINFO_EXTENSION));
    $mime = $mimeTypes[$ext] ?? 'application/octet-stream';

    http_response_code(200);
    header('Content-Type: ' . $mime);
    header('Content-Length: ' . filesize($fullPath));
    header('Content-Disposition: inline; filename="' . basename($fullPath) . '"');
    readfile($fullPath);
}

// Usage
secureFileServe($_GET['file'] ?? '', '/var/www/html/uploads');
```

### Fix 5: Configure Nginx Access Control

```nginx
# nginx.conf — deny access to hidden files
location ~ /\. {
    deny all;
    access_log off;
    log_not_found off;
}

# Protect specific directories
location /private/ {
    deny all;
    return 403;
}

# Restrict by IP
location /admin/ {
    allow 192.168.1.0/24;
    allow 10.0.0.0/8;
    deny all;
}

# Custom 403 error page
error_page 403 /403.php;
location = /403.php {
    internal;
}
```

## Examples

```php
<?php
// Example 1: Middleware-style access control
class AccessControl
{
    private array $protectedRoutes;
    private string $loginUrl;

    public function __construct(array $protectedRoutes, string $loginUrl = '/login')
    {
        $this->protectedRoutes = $protectedRoutes;
        $this->loginUrl = $loginUrl;
    }

    public function check(string $uri): bool
    {
        foreach ($this->protectedRoutes as $pattern => $roles) {
            if (preg_match($pattern, $uri)) {
                if (session_status() === PHP_SESSION_NONE) {
                    session_start();
                }

                $userRole = $_SESSION['role'] ?? null;

                if ($userRole === null) {
                    header('Location: ' . $this->loginUrl);
                    return false;
                }

                if (!in_array($userRole, (array) $roles)) {
                    http_response_code(403);
                    echo '403 Forbidden — You do not have access to this page.';
                    return false;
                }
            }
        }
        return true;
    }
}

// Usage
$access = new AccessControl([
    '#^/admin/#'  => ['admin'],
    '#^/api/#'    => ['admin', 'api_user'],
    '#^/edit/#'   => ['admin', 'editor'],
]);

if (!$access->check($_SERVER['REQUEST_URI'])) {
    exit;
}

// Example 2: IP-based restriction
function restrictToIPs(array $allowedIPs): void
{
    $clientIP = $_SERVER['REMOTE_ADDR'];

    if (!in_array($clientIP, $allowedIPs)) {
        http_response_code(403);
        error_log("403 Forbidden: IP $clientIP attempted access");
        echo 'Access denied from your IP address.';
        exit;
    }
}

restrictToIPs(['192.168.1.0/24', '10.0.0.1']);
```

## Related Errors

- [PHP File Permission Error]({{< relref "/languages/php/file-permission-error" >}})
- [PHP HTTP 404 Not Found]({{< relref "/languages/php/http-404-error" >}})
- [PHP HTTP 500 Internal Server Error]({{< relref "/languages/php/http-500-error" >}})
