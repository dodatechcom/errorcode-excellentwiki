---
title: "[Solution] Laravel Broadcast Driver Not Configured"
description: "Fix Laravel broadcast driver not set or configured. Resolve Connection could not be established error in broadcasting."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error appears when the application attempts to broadcast an event but the configured broadcast driver is unavailable or missing.

## Common Causes

- `BROADCAST_DRIVER` in `.env` is set to a driver not installed
- Pusher credentials are wrong or account is inactive
- Laravel Reverb server is not running
- Socket.IO or WebSocket server is not reachable
- `broadcaster.php` config references undefined connections

## How to Fix

1. Set the broadcast driver in `.env`:

```text
BROADCAST_DRIVER=reverb
```

2. For Pusher, verify credentials:

```text
PUSHER_APP_ID=your-app-id
PUSHER_APP_KEY=your-key
PUSHER_APP_SECRET=your-secret
```

3. For Reverb, ensure the server is running:

```bash
php artisan reverb:start
```

4. Register broadcast routes in `routes/channels.php`:

```php
Broadcast::channel('orders.{id}', function ($user, $id) {
    return $user->id === Order::find($id)->user_id;
});
```

## Examples

```php
// Broadcasting fails when driver is not configured
event(new OrderShipped($order));
// RuntimeException: Broadcasting driver [reverb] is not supported.

// Fallback to log driver in testing
// .env.testing
BROADCAST_DRIVER=log
```
