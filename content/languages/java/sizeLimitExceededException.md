---
title: "[Solution] Java SizeLimitExceededException — JNDI Search Result Too Large"
description: "Fix Java SizeLimitExceededException by increasing size limit, using pagination, refining search criteria, and implementing result set streaming."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1512
---

# SizeLimitExceededException — JNDI Search Result Too Large

A `javax.naming.SizeLimitExceededException` is thrown when a JNDI search or list operation exceeds the size limit imposed by the naming or directory service.

## Description

`SizeLimitExceededException` is a subclass of `LimitExceededException` indicating that the number of entries returned by a search operation exceeded the server-configured or client-configured size limit. This is common in LDAP directories with large datasets.

**Message variants:**
- `javax.naming.SizeLimitExceededException`
- `Size limit exceeded`
- `Too many results`
- `Search size limit exceeded`

## Common Causes

```java
// Cause 1: Default search limit too low
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
Context ctx = new InitialContext(env);

SearchControls controls = new SearchControls();
controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
// No size limit set — server default applies (often 1000)
NamingEnumeration<SearchResult> results =
        ctx.search("dc=example,dc=com", "(objectClass=person)", controls);
// SizeLimitExceededException if more than 1000 results

// Cause 2: Overly broad search filter
ctx.search("dc=example,dc=com", "(objectClass=*)", controls);
// Matches everything in the directory

// Cause 3: Server-side size limit configured conservatively
// Server admin set sizeLimit: 500 in slapd.conf

// Cause 4: Client-side size limit explicitly set too low
controls.setSizeLimit(10); // Only 10 results allowed

// Cause 5: Listing all bindings in a large context
NamingEnumeration<Binding> bindings = ctx.listBindings("dc=example,dc=com");
// May exceed server limit
```

## Solutions

### Fix 1: Increase Client-Side Size Limit

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
controls.setSizeLimit(10000); // Increase size limit

NamingEnumeration<SearchResult> results =
        ctx.search("dc=example,dc=com", "(objectClass=person)", controls);
while (results.hasMore()) {
    SearchResult result = results.next();
    System.out.println(result.getName());
}
```

### Fix 2: Use Paged Results Control

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import com.sun.jndi.ldap.Control;
import com.sun.jndi.ldap.ctl.PagedResultsControl;
import com.sun.jndi.ldap.ctl.PagedResultsResponseControl;
import java.util.Hashtable;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");

int pageSize = 500;
byte[] cookie = null;
Context ctx = new InitialContext(env);

do {
    SearchControls controls = new SearchControls();
    controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
    controls.setReturningAttributes(new String[]{"cn", "mail"});

    // Set paged results control
    ctx.addToEnvironment("java.naming.ldap.control",
            new PagedResultsControl(pageSize, Control.CRITICAL));

    NamingEnumeration<SearchResult> results =
            ctx.search("dc=example,dc=com", "(objectClass=person)", controls);

    while (results.hasMore()) {
        SearchResult result = results.next();
        System.out.println(result.getName());
    }

    // Extract cookie for next page
    Control[] responseControls = (Control[]) ctx.getEnvironment()
            .get("java.naming.ldap.control");
    cookie = null;
    if (responseControls != null) {
        for (Control control : responseControls) {
            if (control instanceof PagedResultsResponseControl) {
                cookie = ((PagedResultsResponseControl) control).getCookie();
            }
        }
    }
} while (cookie != null && cookie.length > 0);
```

### Fix 3: Refine Search Criteria

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import javax.naming.NamingEnumeration;
import java.util.Hashtable;

Context ctx = new InitialContext(env);
SearchControls controls = new SearchControls();
controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
controls.setSizeLimit(1000);

// Instead of broad search:
// ctx.search("dc=example,dc=com", "(objectClass=person)", controls);

// Use more specific filters:
NamingEnumeration<SearchResult> results =
        ctx.search("ou=engineering,dc=example,dc=com",
                "(&(objectClass=person)(department=Engineering))",
                controls);
while (results.hasMore()) {
    SearchResult result = results.next();
    System.out.println(result.getName());
}
```

### Fix 4: Handle SizeLimitExceededException Gracefully

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.SizeLimitExceededException;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import java.util.ArrayList;
import java.util.List;
import java.util.Hashtable;

public static List<SearchResult> searchWithSizeLimitHandling(
        Context ctx, String base, String filter, int sizeLimit)
        throws javax.naming.NamingException {
    List<SearchResult> results = new ArrayList<>();
    SearchControls controls = new SearchControls();
    controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
    controls.setSizeLimit(sizeLimit);

    try {
        NamingEnumeration<SearchResult> enumeration =
                ctx.search(base, filter, controls);
        while (enumeration.hasMore()) {
            results.add(enumeration.nextElement());
        }
    } catch (SizeLimitExceededException e) {
        System.err.println("Size limit exceeded. Collected "
                + results.size() + " results. Refine search criteria.");
    }
    return results;
}
```

## Prevention Checklist

- Set appropriate `setSizeLimit()` on `SearchControls` for expected result sizes
- Use paged results control for large result sets
- Refine search filters to return only necessary entries
- Set `setReturningAttributes()` to limit returned attributes
- Handle `SizeLimitExceededException` to gracefully process partial results
- Coordinate with directory administrators on server-side size limits

## Related Errors

- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [TimeLimitExceededException](/languages/java/timeLimitExceededException) — Search timed out
- [PartialResultException](/languages/java/partialresultexception) — Incomplete results
- [CommunicationException](/languages/java/communicationexception) — Connection lost during search
