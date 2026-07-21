---
title: "Connectivity Check Error"
description: "Fix Android network connectivity check and state monitoring errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App does not detect network changes or makes requests when offline

## Common Causes

- NetworkInfo deprecated and not used
- ConnectivityManager.getNetworkCapabilities not checked
- Network callback not properly registered
- Connectivity check not performed before request

## Fixes

- Use ConnectivityManager.getNetworkCapabilities()
- Register NetworkCallback for real-time changes
- Check connectivity before making requests
- Use TrafficStats for bandwidth monitoring

## Code Example

```kotlin
// Check connectivity
val connectivityManager = getSystemService(ConnectivityManager::class.java)
val network = connectivityManager.activeNetwork
val capabilities = connectivityManager.getNetworkCapabilities(network)

val isConnected = capabilities?.let {
    it.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET) &&
    it.hasCapability(NetworkCapabilities.NET_CAPABILITY_VALIDATED)
} ?: false

// Real-time monitoring:
val callback = object : ConnectivityManager.NetworkCallback() {
    override fun onAvailable(network: Network) { /* online */ }
    override fun onLost(network: Network) { /* offline */ }
}

val request = NetworkRequest.Builder()
    .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    .build()
connectivityManager.registerNetworkCallback(request, callback)
```

# Use NetworkCapabilities, not deprecated NetworkInfo
# registerNetworkCallback for real-time updates
# Check NET_CAPABILITY_VALIDATED for actual internet access
