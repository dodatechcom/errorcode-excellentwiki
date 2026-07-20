---
title: "[Solution] Monolog Logging Error Fix"
description: "Fix Monolog logging errors. Check handler configuration, verify log directory permissions, handle formatter errors."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1118
---

# Monolog Logging Error

Monolog logging errors occur when log handlers cannot write to their destination, formatters fail to process records, or handler configuration is incorrect. These errors can cause application crashes if logging failures aren't handled gracefully, especially in error handlers.

## Common Causes

```php
<?php
// Cause 1: Log directory doesn't exist or isn't writable
$handler = new StreamHandler('/var/log/app/app.log');
// /var/log/app/ directory doesn't exist

// Cause 2: File permissions incorrect
// Log file exists but web server can't write to it
$handler = new StreamHandler('/var/log/app/app.log', Logger::DEBUG);

// Cause 3: Handler configuration conflict
$logger = new Logger('app');
$logger->pushHandler(new StreamHandler('/tmp/app.log'));
$logger->pushHandler(new RotatingFileHandler('/var/log/app/app.log'));
// Both handlers try to write — one may fail

// Cause 4: Formatter error
$handler = new StreamHandler('/tmp/app.log');
$handler->setFormatter(new JsonFormatter());
// JsonFormatter fails with unencodable data (circular references)

// Cause 5: Memory limit exceeded in buffer
$handler = new BufferHandler(new StreamHandler('/tmp/app.log'));
// Buffer grows too large before flushing
```

## How to Fix

### Fix 1: Ensure log directory exists and is writable

```php
<?php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;

$logDir = '/var/log/myapp';
$logFile = $logDir . '/app.log';

// Create directory if it doesn't exist
if (!is_dir($logDir)) {
    if (!mkdir($logDir, 0755, true)) {
        throw new \RuntimeException("Cannot create log directory: $logDir");
    }
}

// Check write permissions
if (!is_writable($logDir)) {
    throw new \RuntimeException("Log directory not writable: $logDir");
}

// Create logger with writable path
$logger = new Logger('app');
$logger->pushHandler(new StreamHandler($logFile, Logger::DEBUG));

$logger->info('Application started');
```

### Fix 2: Use RotatingFileHandler for log rotation

```php
<?php
use Monolog\Logger;
use Monolog\Handler\RotatingFileHandler;

$logger = new Logger('app');

// Rotates daily: app-2024-01-15.log, app-2024-01-16.log, etc.
$handler = new RotatingFileHandler(
    '/var/log/myapp/app.log',
    Logger::DEBUG,
    true // keep max 30 days by default
);

$logger->pushHandler($handler);
$logger->info('Processing request', ['url' => $_SERVER['REQUEST_URI']]);
```

### Fix 3: Handle formatter errors gracefully

```php
<?php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Formatter\JsonFormatter;

$logger = new Logger('app');
$handler = new StreamHandler('/var/log/myapp/app.log', Logger::DEBUG);

// Use JsonFormatter with error handling
$formatter = new JsonFormatter();
$handler->setFormatter($formatter);

$logger->pushHandler($handler);

// Avoid logging objects with circular references
try {
    $data = getComplexObject();
    $logger->info('Complex data', ['data' => $data]);
} catch (\Throwable $e) {
    // Fallback: log safe representation
    $logger->warning('Failed to log complex data', [
        'error' => $e->getMessage(),
        'context' => get_object_vars($data),
    ]);
}
```

### Fix 4: Use ErrorLogHandler as fallback

```php
<?php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\ErrorLogHandler;

$logger = new Logger('app');

// Primary handler
$logger->pushHandler(
    new StreamHandler('/var/log/myapp/app.log', Logger::DEBUG)
);

// Fallback handler — writes to PHP error log
$logger->pushHandler(
    new ErrorLogHandler(Logger::ERROR)
);

// If StreamHandler fails, ErrorLogHandler still captures errors
```

### Fix 5: Configure processors for safe logging

```php
<?php
use Monolog\Logger;
use Monolog\Processor\MemoryUsageProcessor;
use Monolog\Processor\PsrLogMessageProcessor;

$logger = new Logger('app');

// Add processors that don't throw
$logger->pushProcessor(new MemoryUsageProcessor());
$logger->pushProcessor(new PsrLogMessageProcessor());

// Custom safe processor
$logger->pushProcessor(function (array $record): array {
    try {
        $record['extra']['request_id'] = $_SERVER['HTTP_X_REQUEST_ID'] ?? 'unknown';
    } catch (\Throwable $e) {
        $record['extra']['request_id'] = 'error';
    }
    return $record;
});
```

## Examples

```php
<?php
// Complete Monolog setup example

use Monolog\Logger;
use Monolog\Handler\RotatingFileHandler;
use Monolog\Handler\StreamHandler;
use Monolog\Processor\WebProcessor;
use Monolog\Processor\IntrospectionProcessor;

function createLogger(string $logDir, string $level = 'debug'): Logger
{
    $logger = new Logger('app');

    // Ensure log directory exists
    if (!is_dir($logDir)) {
        mkdir($logDir, 0755, true);
    }

    // Main rotating handler
    $logger->pushHandler(
        new RotatingFileHandler(
            $logDir . '/app.log',
            constant('Monolog\Logger::' . strtoupper($level))
        )
    );

    // Add context processors
    $logger->pushProcessor(new WebProcessor());
    $logger->pushProcessor(new IntrospectionProcessor());

    return $logger;
}

// Usage
$logger = createLogger('/var/log/myapp');
$logger->info('User logged in', ['user_id' => 123]);
```

## Related Errors

- [File Permission Error]({{< relref "/languages/php/file-permission-error" >}}) — permission denied
- [File Write Error]({{< relref "/languages/php/file-write-error" >}}) — file write failures
- [Error Log Function]({{< relref "/languages/php/error-log-function" >}}) — PHP error logging
