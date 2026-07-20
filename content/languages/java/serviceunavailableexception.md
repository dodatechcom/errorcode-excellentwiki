---
title: "[Solution] Java ServiceUnavailableException — JNDI Naming Service Unavailable"
description: "Fix Java ServiceUnavailableException by checking service status, implementing connection pooling, handling service outages, and adding retry with backoff."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1507
---

# ServiceUnavailableException — JNDI Naming Service Unavailable

A `javax.naming.ServiceUnavailableException` is thrown when the naming or directory service is unavailable to perform the requested operation.

## Description

`ServiceUnavailableException` is a subclass of `CommunicationException` indicating that the naming service is running but currently unable to handle requests. This differs from `CommunicationException` which typically indicates a network connectivity failure.

**Message variants:**
- `javax.naming.ServiceUnavailableException`
- `Service is not available`
- `Server is shutting down`
- `Naming service is not running`
- `Too many connections`

## Common Causes

```java
// Cause 1: Naming service is restarting or shutting down
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
Context ctx = new InitialContext(env); // ServiceUnavailableException

// Cause 2: Server has reached connection limit
// Too many concurrent clients connected
Context ctx = new InitialContext(env); // ServiceUnavailableException

// Cause 3: RMI registry is not running
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.rmi.registry.RegistryContextFactory");
env.put(Context.PROVIDER_URL, "rmi://localhost:1099");
Context ctx = new InitialContext(env); // ServiceUnavailableException

// Cause 4: Service is being maintained
// LDAP server in maintenance mode

// Cause 5: Server overloaded with requests
// High load causing temporary unavailability
```

## Solutions

### Fix 1: Check Service Status Before Operations

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import java.net.InetSocketAddress;
import java.net.Socket;

public static boolean isServiceReady(String host, int port) {
    try (Socket socket = new Socket()) {
        socket.connect(new InetSocketAddress(host, port), 3000);
        return true;
    } catch (IOException e) {
        return false;
    }
}

// Usage
String host = "ldap.example.com";
int port = 389;
if (isServiceReady(host, port)) {
    Hashtable<String, String> env = new Hashtable<>();
    env.put(Context.INITIAL_CONTEXT_FACTORY,
            "com.sun.jndi.ldap.LdapCtxFactory");
    env.put(Context.PROVIDER_URL, "ldap://" + host + ":" + port);
    Context ctx = new InitialContext(env);
} else {
    System.err.println("Naming service is currently unavailable.");
}
```

### Fix 2: Implement Retry with Exponential Backoff

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.ServiceUnavailableException;
import java.util.Hashtable;

public static Context connectWithBackoff(Hashtable<String, String> env,
        int maxRetries) throws javax.naming.NamingException {
    for (int attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            return new InitialContext(env);
        } catch (ServiceUnavailableException e) {
            System.err.println("Service unavailable, attempt " + (attempt + 1)
                    + " of " + (maxRetries + 1));
            if (attempt == maxRetries) throw e;
            try {
                long delay = Math.min(30000L, 1000L * (1L << attempt));
                Thread.sleep(delay);
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
                throw e;
            }
        }
    }
    throw new ServiceUnavailableException("All retry attempts exhausted");
}

// Usage
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
Context ctx = connectWithBackoff(env, 5);
```

### Fix 3: Use Connection Pooling

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.ServiceUnavailableException;
import java.util.Hashtable;
import java.util.concurrent.ConcurrentLinkedQueue;

public class JndiContextPool {
    private final Hashtable<String, String> env;
    private final ConcurrentLinkedQueue<Context> pool = new ConcurrentLinkedQueue<>();

    public JndiContextPool(Hashtable<String, String> env) {
        this.env = env;
    }

    public synchronized Context acquire() throws javax.naming.NamingException {
        Context ctx;
        while ((ctx = pool.poll()) != null) {
            try {
                // Verify the context is still usable
                ctx.lookup("");
                return ctx;
            } catch (Exception e) {
                try { ctx.close(); } catch (Exception ignored) {}
            }
        }
        return new InitialContext(env);
    }

    public synchronized void release(Context ctx) {
        if (ctx != null) {
            pool.offer(ctx);
        }
    }

    public synchronized void closeAll() {
        Context ctx;
        while ((ctx = pool.poll()) != null) {
            try { ctx.close(); } catch (Exception ignored) {}
        }
    }
}

// Usage
JndiContextPool pool = new JndiContextPool(env);
Context ctx = pool.acquire();
try {
    Object obj = ctx.lookup("cn=users,dc=example,dc=com");
} finally {
    pool.release(ctx);
}
```

### Fix 4: Handle Outage with Circuit Breaker Pattern

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.ServiceUnavailableException;
import java.util.concurrent.atomic.AtomicInteger;
import java.time.Instant;

public class JndiCircuitBreaker {
    private final Hashtable<String, String> env;
    private final AtomicInteger failureCount = new AtomicInteger(0);
    private volatile Instant lastFailure = Instant.MIN;
    private volatile boolean circuitOpen = false;
    private static final int FAILURE_THRESHOLD = 5;
    private static final long RESET_TIMEOUT_MS = 60000;

    public JndiCircuitBreaker(Hashtable<String, String> env) {
        this.env = env;
    }

    public Context getContext() throws javax.naming.NamingException {
        if (circuitOpen) {
            if (Instant.now().isAfter(lastFailure.plusMillis(RESET_TIMEOUT_MS))) {
                circuitOpen = false; // Half-open: allow one attempt
            } else {
                throw new ServiceUnavailableException(
                        "Circuit breaker is open — service marked as unavailable");
            }
        }
        try {
            Context ctx = new InitialContext(env);
            failureCount.set(0);
            return ctx;
        } catch (ServiceUnavailableException e) {
            lastFailure = Instant.now();
            if (failureCount.incrementAndGet() >= FAILURE_THRESHOLD) {
                circuitOpen = true;
            }
            throw e;
        }
    }
}
```

## Prevention Checklist

- Monitor naming service health with health checks and alerts
- Implement retry logic with exponential backoff for transient unavailability
- Use connection pooling to manage context lifecycle efficiently
- Implement a circuit breaker pattern to fail fast during prolonged outages
- Configure multiple naming service replicas for high availability
- Set appropriate timeouts to prevent hanging operations

## Related Errors

- [CommunicationException](/languages/java/communicationexception) — Network communication failure
- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [TimeLimitExceededException](/languages/java/timeLimitExceededException) — Operation timed out
- [NoInitialContextException](/languages/java/noinitialcontextexception) — Missing JNDI configuration
