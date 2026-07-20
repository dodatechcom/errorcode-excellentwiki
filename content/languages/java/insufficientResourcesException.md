---
title: "[Solution] Java InsufficientResourcesException — JNDI Server Resources Exhausted"
description: "Fix Java InsufficientResourcesException by implementing backoff, reducing request rate, checking server capacity, and using connection pooling."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1515
---

# InsufficientResourcesException — JNDI Server Resources Exhausted

A `javax.naming.InsufficientResourcesException` is thrown when the naming or directory server cannot handle the request due to insufficient resources.

## Description

`InsufficientResourcesException` is a subclass of `ServiceUnavailableException` indicating that the server has run out of resources such as memory, connections, or processing capacity. The client should retry after a delay.

**Message variants:**
- `javax.naming.InsufficientResourcesException`
- `Insufficient resources`
- `Server is out of resources`
- `Connection pool exhausted`
- `Too many connections`

## Common Causes

```java
// Cause 1: Too many concurrent connections to LDAP server
// Server has a max connection limit (e.g., 200)
// Application opens 250 connections
for (int i = 0; i < 250; i++) {
    Context ctx = new InitialContext(env); // InsufficientResourcesException
}

// Cause 2: Server memory exhausted
// LDAP server unable to allocate memory for search

// Cause 3: Connection pool depleted
// Application request rate exceeds pool capacity

// Cause 4: Server CPU overloaded
// Complex queries consuming all server resources

// Cause 5: Disk space full on server
// LDAP database cannot write new entries
```

## Solutions

### Fix 1: Implement Retry with Exponential Backoff

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.InsufficientResourcesException;
import javax.naming.NamingException;
import java.util.Hashtable;

public static Context connectWithBackoff(Hashtable<String, String> env,
        int maxRetries) throws NamingException {
    NamingException lastException = null;

    for (int attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            return new InitialContext(env);
        } catch (InsufficientResourcesException e) {
            lastException = e;
            System.err.println("Server resources exhausted, attempt "
                    + (attempt + 1) + "/" + (maxRetries + 1));
            if (attempt < maxRetries) {
                long delay = Math.min(60000L, 2000L * (1L << attempt));
                System.err.println("Retrying in " + delay + "ms...");
                try {
                    Thread.sleep(delay);
                } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                    throw e;
                }
            }
        }
    }
    throw lastException;
}
```

### Fix 2: Reduce Request Rate with Throttling

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.util.Hashtable;
import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicInteger;

public class ThrottledJndiClient {
    private final Hashtable<String, String> env;
    private final Semaphore semaphore;
    private final AtomicInteger activeRequests = new AtomicInteger(0);
    private final int maxConcurrent;

    public ThrottledJndiClient(Hashtable<String, String> env,
            int maxConcurrent) {
        this.env = env;
        this.semaphore = new Semaphore(maxConcurrent);
        this.maxConcurrent = maxConcurrent;
    }

    public Context acquireContext() throws NamingException {
        try {
            semaphore.acquire();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new NamingException("Interrupted while waiting for connection");
        }
        activeRequests.incrementAndGet();
        try {
            return new InitialContext(env);
        } catch (NamingException e) {
            activeRequests.decrementAndGet();
            semaphore.release();
            throw e;
        }
    }

    public void releaseContext(Context ctx) {
        if (ctx != null) {
            try { ctx.close(); } catch (Exception ignored) {}
        }
        activeRequests.decrementAndGet();
        semaphore.release();
    }

    public int getActiveRequests() {
        return activeRequests.get();
    }
}
```

### Fix 3: Implement Connection Pooling

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.InsufficientResourcesException;
import javax.naming.NamingException;
import java.util.Hashtable;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.TimeUnit;

public class JndiConnectionPool {
    private final Hashtable<String, String> env;
    private final BlockingQueue<Context> pool;
    private final int maxSize;

    public JndiConnectionPool(Hashtable<String, String> env, int maxSize) {
        this.env = env;
        this.pool = new ArrayBlockingQueue<>(maxSize);
        this.maxSize = maxSize;
    }

    public Context borrowContext(long timeoutMs) throws NamingException {
        Context ctx = pool.poll(timeoutMs, TimeUnit.MILLISECONDS);
        if (ctx != null) {
            try {
                ctx.lookup(""); // Verify context is still valid
                return ctx;
            } catch (Exception e) {
                try { ctx.close(); } catch (Exception ignored) {}
            }
        }
        return new InitialContext(env);
    }

    public void returnContext(Context ctx) {
        if (ctx != null && pool.size() < maxSize) {
            try {
                pool.offer(ctx);
            } catch (Exception e) {
                try { ctx.close(); } catch (Exception ignored) {}
            }
        } else {
            try { ctx.close(); } catch (Exception ignored) {}
        }
    }

    public void shutdown() {
        Context ctx;
        while ((ctx = pool.poll()) != null) {
            try { ctx.close(); } catch (Exception ignored) {}
        }
    }
}

// Usage
JndiConnectionPool pool = new JndiConnectionPool(env, 20);
Context ctx = pool.borrowContext(5000);
try {
    Object obj = ctx.lookup("cn=users,dc=example,dc=com");
} finally {
    pool.returnContext(ctx);
}
```

### Fix 4: Monitor and Log Server Resource Status

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.InsufficientResourcesException;
import javax.naming.NamingException;
import java.util.Hashtable;
import java.util.logging.Logger;

public class ResilientJndiClient {
    private static final Logger logger = Logger.getLogger(ResilientJndiClient.class.getName());
    private final Hashtable<String, String> env;
    private volatile long lastFailure = 0;
    private volatile int consecutiveFailures = 0;

    public ResilientJndiClient(Hashtable<String, String> env) {
        this.env = env;
    }

    public Context getContext() throws NamingException {
        long now = System.currentTimeMillis();
        long backoffMs = Math.min(30000L, 1000L * (1L << consecutiveFailures));

        if (consecutiveFailures > 0 && (now - lastFailure) < backoffMs) {
            throw new InsufficientResourcesException(
                    "Backing off after " + consecutiveFailures + " failures");
        }

        try {
            Context ctx = new InitialContext(env);
            consecutiveFailures = 0;
            return ctx;
        } catch (InsufficientResourcesException e) {
            consecutiveFailures++;
            lastFailure = now;
            logger.warning("Server resources exhausted. Failure count: "
                    + consecutiveFailures);
            throw e;
        }
    }
}
```

## Prevention Checklist

- Implement connection pooling to limit concurrent connections
- Use throttling (semaphores) to control request rate
- Implement exponential backoff retry for `InsufficientResourcesException`
- Monitor server resource metrics (connections, memory, CPU)
- Set reasonable connection pool sizes based on server capacity
- Log failures and track consecutive errors for adaptive backoff

## Related Errors

- [ServiceUnavailableException](/languages/java/serviceunavailableexception) — Service unavailable
- [CommunicationException](/languages/java/communicationexception) — Network communication failure
- [SizeLimitExceededException](/languages/java/sizeLimitExceededException) — Result set too large
- [TimeLimitExceededException](/languages/java/timeLimitExceededException) — Operation timed out
