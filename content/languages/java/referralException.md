---
title: "[Solution] Java ReferralException — JNDI Referral Encountered"
description: "Fix Java ReferralException by following referrals programmatically, setting referral limits, handling referral chains, and configuring proper referral handling."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1511
---

# ReferralException — JNDI Referral Encountered

A `javax.naming.ReferralException` is thrown when a JNDI operation encounters a referral that cannot be followed automatically.

## Description

`ReferralException` is a subclass of `NamingException` indicating that the naming or directory service returned a referral to another server or naming context. The exception is thrown when referral following is disabled or when the referral cannot be resolved. It provides methods to access the referral information and follow it programmatically.

**Message variants:**
- `javax.naming.ReferralException`
- `Referral`
- `Referral detected`
- `Cannot follow referral`

## Common Causes

```java
// Cause 1: Referral following is disabled (default)
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://server1:389");
// Context.REFERRAL defaults to "ignore"
Context ctx = new InitialContext(env);
ctx.lookup("cn=users,dc=remote,dc=com"); // ReferralException

// Cause 2: Referral points to unreachable server
env.put(Context.REFERRAL, "follow");
Context ctx = new InitialContext(env);
ctx.lookup("cn=users,dc=remote,dc=com"); // ReferralException (server2 down)

// Cause 3: Circular referrals
// server1 -> server2 -> server1

// Cause 4: Referral limit exceeded
env.put("java.naming.ldap.referral.limit", "2");
ctx.lookup("cn=deep,dc=remote,dc=com"); // ReferralException

// Cause 5: Referral with incompatible context factory
// Referral URL uses a different protocol than the client supports
```

## Solutions

### Fix 1: Enable Automatic Referral Following

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import java.util.Hashtable;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://server1:389");
env.put(Context.REFERRAL, "follow"); // Automatically follow referrals

Context ctx = new InitialContext(env);
Object obj = ctx.lookup("cn=users,dc=remote,dc=com");
```

### Fix 2: Follow Referrals Programmatically

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.ReferralException;
import javax.naming.directory.DirContext;
import javax.naming.directory.InitialDirContext;
import java.util.Hashtable;

public static Object followReferrals(String initialUrl, String name,
        Hashtable<String, String> baseEnv) throws javax.naming.NamingException {
    Hashtable<String, String> env = new Hashtable<>(baseEnv);
    env.put(Context.PROVIDER_URL, initialUrl);
    env.put(Context.REFERRAL, "throw"); // Throw instead of auto-follow

    Context ctx = new InitialContext(env);
    try {
        return ctx.lookup(name);
    } catch (ReferralException e) {
        System.out.println("Referral at: " + e.getReferralInfo());
        // Follow the referral by creating a new context with the referral URL
        String referralUrl = e.getReferralInfo().toString();
        return followReferrals(referralUrl, name, baseEnv);
    } finally {
        ctx.close();
    }
}

// Usage
Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, "cn=admin,dc=example,dc=com");
env.put(Context.SECURITY_CREDENTIALS, "password");

Object result = followReferrals("ldap://server1:389",
        "cn=users,dc=remote,dc=com", env);
```

### Fix 3: Set Referral Limit to Prevent Infinite Chains

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.ReferralException;
import java.util.Hashtable;

public static void lookupWithReferralLimit(Hashtable<String, String> env,
        String name, int maxReferrals) throws javax.naming.NamingException {
    env.put(Context.REFERRAL, "follow");
    env.put("java.naming.ldap.referral.limit", String.valueOf(maxReferrals));

    Context ctx = new InitialContext(env);
    try {
        Object obj = ctx.lookup(name);
        System.out.println("Found: " + obj.getClass().getName());
    } catch (ReferralException e) {
        System.err.println("Referral limit reached after " + maxReferrals
                + " hops. Last referral: " + e.getReferralInfo());
    } finally {
        ctx.close();
    }
}
```

### Fix 4: Handle ReferralException in Search Operations

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingEnumeration;
import javax.naming.ReferralException;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;
import java.util.Hashtable;
import java.util.ArrayList;
import java.util.List;

public static List<SearchResult> searchWithReferralHandling(
        Hashtable<String, String> env, String base, String filter)
        throws javax.naming.NamingException {
    env.put(Context.REFERRAL, "follow");
    List<SearchResult> allResults = new ArrayList<>();

    Context ctx = new InitialContext(env);
    SearchControls controls = new SearchControls();
    controls.setSearchScope(SearchControls.SUBTREE_SCOPE);

    NamingEnumeration<SearchResult> results =
            ctx.search(base, filter, controls);
    while (results.hasMore()) {
        try {
            allResults.add(results.nextElement());
        } catch (ReferralException e) {
            System.err.println("Referral encountered: " + e.getReferralInfo());
            // Auto-following should handle this, but log for debugging
        }
    }
    ctx.close();
    return allResults;
}
```

## Prevention Checklist

- Set `Context.REFERRAL` to `"follow"` for automatic referral traversal
- Configure `java.naming.ldap.referral.limit` to prevent infinite referral loops
- Handle `ReferralException` explicitly when using `"throw"` mode
- Test referral chains in a staging environment before production deployment
- Monitor and log referral paths for debugging distributed directory issues
- Verify that referral URLs use protocols supported by the JNDI provider

## Related Errors

- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [PartialResultException](/languages/java/partialresultexception) — Incomplete results from referrals
- [LinkException](/languages/java/linkexception) — Link resolution failure
- [CommunicationException](/languages/java/communicationexception) — Cannot reach referral server
