---
title: "[Solution] Java TimeLimitExceededException — JNDI Operation Timed Out"
description: "Fix Java TimeLimitExceededException by increasing timeout values, optimizing queries, handling timeouts gracefully, and configuring connection timeouts."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1513
---

# TimeLimitExceededException — JNDI Operation Timed Out

A `javax.naming.TimeLimitExceededException` is thrown when a JNDI operation exceeds the configured time limit.

## Description

`TimeLimitExceededException` is a subclass of `LimitExceededException` indicating that a search or other JNDI operation took longer than the allowed time limit. This can be caused by server-side timeout policies, slow network connections, or inefficient queries.

**Message variants:**
- `javax.naming.TimeLimitExceededException`
- `Time limit exceeded`
- `Operation timed out`
- `Search timed out`

## Common Causes

```java
// Cause 1: Default time limit too short
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
Context ctx = new InitialContext(env);

SearchControls controls = new SearchControls();
controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
controls.setTimeLimit(100); // 100ms — too short
ctx.search("dc=example,dc=com", "(objectClass=person)", controls);
// TimeLimitExceededException

// Cause 2: Inefficient search filter causing slow query
ctx.search("dc=example,dc=com", "(|(cn=*a*)(sn=*a*))", controls);
// Wildcard search on large directory is slow

// Cause 3: Large result set with complex attribute retrieval
controls.setReturningAttributes(new String[]{"*"});
controls.setTimeLimit(500); // 500ms for 10,000 entries

// Cause 4: Network latency causing slow responses
// LDAP server on remote data center with high latency

// Cause 5: Server overloaded and slow to respond
// High CPU load on LDAP server
```

## Solutions

### Fix 1: Increase Time Limit on SearchControls

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import java.util.Hashtable;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
Context ctx = new InitialContext(env);

SearchControls controls = new SearchControls();
controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
controls.setTimeLimit(30000); // 30 seconds

NamingEnumeration<SearchResult> results =
        ctx.search("dc=example,dc=com", "(objectClass=person)", controls);
while (results.hasMore()) {
    SearchResult result = results.next();
    System.out.println(result.getName());
}
```

### Fix 2: Set Connection and Read Timeouts on Environment

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import java.util.Hashtable;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");

// Connection timeout (how long to wait for connection)
env.put("com.sun.jndi.ldap.connect.timeout", "10000"); // 10 seconds

// Read timeout (how long to wait for response)
env.put("com.sun.jndi.ldap.read.timeout", "30000"); // 30 seconds

Context ctx = new InitialContext(env);
```

### Fix 3: Optimize Search Queries

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import java.util.Hashtable;

Context ctx = new InitialContext(env);
SearchControls controls = new SearchControls();
controls.setSearchScope(SearchControls.ONELEVEL_SCOPE); // Limit scope
controls.setTimeLimit(30000);
controls.setSizeLimit(5000);
controls.setReturningAttributes(new String[]{"cn", "mail", "uid"}); // Only needed attrs

// Use indexed attributes in filter
NamingEnumeration<SearchResult> results =
        ctx.search("ou=users,dc=example,dc=com",
                "(&(objectClass=person)(uid=*))",
                controls);
while (results.hasMore()) {
    SearchResult result = results.next();
    System.out.println(result.getAttributes().get("cn").get());
}
```

### Fix 4: Handle Timeout Gracefully with Fallback

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.TimeLimitExceededException;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import javax.naming.NamingEnumeration;
import java.util.Hashtable;
import java.util.ArrayList;
import java.util.List;

public static List<SearchResult> searchWithTimeout(
        Context ctx, String base, String filter,
        int timeLimitMs) throws javax.naming.NamingException {
    List<SearchResult> results = new ArrayList<>();
    SearchControls controls = new SearchControls();
    controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
    controls.setTimeLimit(timeLimitMs);

    try {
        NamingEnumeration<SearchResult> enumeration =
                ctx.search(base, filter, controls);
        while (enumeration.hasMore()) {
            results.add(enumeration.nextElement());
        }
    } catch (TimeLimitExceededException e) {
        System.err.println("Search timed out after " + timeLimitMs
                + "ms. Returning " + results.size() + " partial results.");
    }
    return results;
}
```

### Fix 5: Async Search with Time Limit

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import javax.naming.NamingEnumeration;
import java.util.Hashtable;
import java.util.concurrent.*;

public static CompletableFuture<List<SearchResult>> searchAsync(
        Context ctx, String base, String filter, int timeLimitMs) {
    return CompletableFuture.supplyAsync(() -> {
        try {
            SearchControls controls = new SearchControls();
            controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
            controls.setTimeLimit(timeLimitMs);
            List<SearchResult> results = new ArrayList<>();
            NamingEnumeration<SearchResult> enumeration =
                    ctx.search(base, filter, controls);
            while (enumeration.hasMore()) {
                results.add(enumeration.nextElement());
            }
            return results;
        } catch (Exception e) {
            throw new CompletionException(e);
        }
    });
}

// Usage with overall timeout
Context ctx = new InitialContext(env);
CompletableFuture<List<SearchResult>> future =
        searchAsync(ctx, "dc=example,dc=com", "(objectClass=person)", 30000);
try {
    List<SearchResult> results = future.get(60, TimeUnit.SECONDS);
} catch (TimeoutException e) {
    System.err.println("Overall operation timed out.");
} catch (Exception e) {
    System.err.println("Search failed: " + e.getMessage());
}
```

## Prevention Checklist

- Set appropriate `timeLimit` on `SearchControls` for expected query complexity
- Configure `com.sun.jndi.ldap.connect.timeout` and `read.timeout` on the environment
- Use indexed attributes in search filters to improve query performance
- Limit search scope (`ONELEVEL_SCOPE` or `BASE_SCOPE`) when possible
- Request only needed attributes with `setReturningAttributes()`
- Handle `TimeLimitExceededException` to return partial results gracefully

## Related Errors

- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [SizeLimitExceededException](/languages/java/sizeLimitExceededException) — Result set too large
- [CommunicationException](/languages/java/communicationexception) — Network communication failure
- [ServiceUnavailableException](/languages/java/serviceunavailableexception) — Service unavailable
