---
title: "[Solution] Java PartialResultException — JNDI Result Is Incomplete"
description: "Fix Java PartialResultException by following referrals, increasing referral limits, handling partial results, and properly configuring referral handling."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1510
---

# PartialResultException — JNDI Result Is Incomplete

A `javax.naming.PartialResultException` is thrown when a JNDI operation returns only a partial result, typically because referrals were not followed or a search limit was reached.

## Description

`PartialResultException` is a subclass of `NamingException` indicating that the naming service returned an incomplete result set. This commonly occurs in distributed directory services (e.g., multi-server LDAP) where referrals point to other servers, and the client is not configured to follow them.

**Message variants:**
- `javax.naming.PartialResultException`
- `Partial result`
- `Not all referrals were followed`
- `Result is incomplete`

## Common Causes

```java
// Cause 1: Referrals not configured to be followed
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://server1:389");
// Default: referrals are NOT followed
Context ctx = new InitialContext(env);
NamingEnumeration<?> results = ctx.search("dc=example,dc=com", "(objectClass=*)");
while (results.hasMore()) {
    Object result = results.next(); // PartialResultException
}

// Cause 2: Referral limit exceeded
env.put(Context.REFERRAL, "follow");
env.put("java.naming.ldap.referral.limit", "2"); // Low limit
Context ctx = new InitialContext(env); // PartialResultException after 2 referrals

// Cause 3: Search size limit reached mid-result
env.put("com.sun.jndi.ldap.search.limit", "10");
// 100 matching entries exist — only 10 returned

// Cause 4: Distributed naming with cross-server referrals
// LDAP server A refers to server B, which refers to server C

// Cause 5: Partial results from a federated directory
// Some naming contexts are unavailable
```

## Solutions

### Fix 1: Enable Referral Following

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
env.put(Context.REFERRAL, "follow"); // Enable referral following

Context ctx = new InitialContext(env);
SearchControls controls = new SearchControls();
controls.setSearchScope(SearchControls.SUBTREE_SCOPE);

NamingEnumeration<SearchResult> results =
        ctx.search("dc=example,dc=com", "(objectClass=*)", controls);
while (results.hasMore()) {
    SearchResult result = results.next();
    System.out.println(result.getName());
}
```

### Fix 2: Set Referral Limit

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import java.util.Hashtable;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");
env.put(Context.REFERRAL, "follow");
env.put("java.naming.ldap.referral.limit", "10"); // Max 10 referrals

try {
    Context ctx = new InitialContext(env);
    Object obj = ctx.lookup("cn=users,dc=remote,dc=com");
} catch (javax.naming.PartialResultException e) {
    System.err.println("Partial result — referral limit reached: " + e.getMessage());
} catch (javax.naming.ReferralException e) {
    System.err.println("Referral could not be followed: " + e.getMessage());
}
```

### Fix 3: Handle Partial Results Gracefully

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.PartialResultException;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import java.util.ArrayList;
import java.util.List;
import java.util.Hashtable;

public static List<SearchResult> searchWithPartialHandling(Context ctx,
        String base, String filter) throws javax.naming.NamingException {
    List<SearchResult> results = new ArrayList<>();
    SearchControls controls = new SearchControls();
    controls.setSearchScope(SearchControls.SUBTREE_SCOPE);

    try {
        NamingEnumeration<SearchResult> enumeration =
                ctx.search(base, filter, controls);
        while (enumeration.hasMore()) {
            results.add(enumeration.nextElement());
        }
    } catch (PartialResultException e) {
        System.err.println("Partial results received: " + e.getMessage());
        System.err.println("Collected " + results.size() + " results so far.");
        // Process whatever results were returned
    }
    return results;
}
```

### Fix 4: Use LdapReferralException for Manual Referral Handling

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import com.sun.jndi.ldap.ReferralException;
import java.util.Hashtable;

public static void searchWithManualReferrals(Context ctx,
        String base, String filter) throws javax.naming.NamingException {
    SearchControls controls = new SearchControls();
    controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
    controls.setReferralHandling(
            com.sun.jndi.ldap.AnonymousAuthenticator.create());

    NamingEnumeration<SearchResult> results =
            ctx.search(base, filter, controls);
    while (results.hasMore()) {
        SearchResult result = results.next();
        System.out.println("Found: " + result.getName());
    }
}
```

## Prevention Checklist

- Set `Context.REFERRAL` to `"follow"` when referrals should be traversed
- Configure `java.naming.ldap.referral.limit` to prevent infinite referral chains
- Handle `PartialResultException` to gracefully process incomplete results
- Test with referral-heavy directory configurations before deployment
- Use manual referral handling for complex multi-server directory topologies
- Log partial results for auditing and debugging

## Related Errors

- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [ReferralException](/languages/java/referralException) — Referral encountered during operation
- [SizeLimitExceededException](/languages/java/sizeLimitExceededException) — Result set too large
- [CommunicationException](/languages/java/communicationexception) — Cannot reach referral server
