---
title: "Service Binding Error"
description: "Fix Android Service binding and unbinding lifecycle errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Service binding fails or causes memory leak because of incorrect lifecycle management

## Common Causes

- Service not bound in onStart or bound too early
- ServiceConnection not properly implemented
- Service unbind not called in matching lifecycle method
- Bound service killed when activity is destroyed

## Fixes

- Bind service in onStart/onCreate, unbind in onStop/onDestroy
- Implement ServiceConnection with onServiceConnected
- Always unbind in matching lifecycle callback
- Use bound service for activity-specific communication

## Code Example

```kotlin
private var myService: MyBoundService? = null
private var isBound = false

private val connection = object : ServiceConnection {
    override fun onServiceConnected(name: ComponentName, service: IBinder) {
        val binder = service as MyBoundService.LocalBinder
        myService = binder.getService()
        isBound = true
    }

    override fun onServiceDisconnected(name: ComponentName) {
        myService = null
        isBound = false
    }
}

override fun onStart() {
    super.onStart()
    Intent(this, MyBoundService::class.java).also { intent ->
        bindService(intent, connection, Context.BIND_AUTO_CREATE)
    }
}

override fun onStop() {
    super.onStop()
    if (isBound) {
        unbindService(connection)
        isBound = false
    }
}
```

# Bind in onStart, unbind in onStop
# Use BIND_AUTO_CREATE to auto-create service
# Bound service stops when all clients unbind
