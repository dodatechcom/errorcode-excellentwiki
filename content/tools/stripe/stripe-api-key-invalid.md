---
title: "[Solution] Stripe Invalid API Key Error - Fix Invalid API Key Provided"
description: "Fix Stripe invalid API key errors. Resolve authentication failures, key rotation issues, and environment mismatches for Stripe API."
tools: ["stripe"]
error-types: ["api-key-invalid"]
severities: ["error"]
weight: 5
---

This error means the API key you provided to Stripe is invalid, revoked, or does not match the environment. Stripe rejects the request before processing any operation.

## What This Error Means

When Stripe receives a request with an invalid API key, it returns:

```
InvalidRequestError: Invalid API Key provided: sk_live_***xyz
# or
AuthenticationError: Invalid API Key
```

Stripe uses different keys for test and live modes. Using a test key against the live API (or vice versa) produces this error.

## Why It Happens

- The API key was rotated or revoked in the Stripe dashboard
- You are using a test key (`sk_test_...`) with live API endpoints
- The key has leading or trailing whitespace from copy-paste
- The key is stored as an environment variable that was not set
- A team member revoked the old key before updating the deployment
- The key does not have the required permissions for the operation

## How to Fix It

### Verify the key in the Stripe dashboard

Go to https://dashboard.stripe.com/apikeys and check the key status. Ensure it is active and not revoked.

### Check the key format

```bash
# Test keys start with sk_test_ or pk_test_
# Live keys start with sk_live_ or pk_live_
echo $STRIPE_SECRET_KEY | head -c 20
```

### Test the key directly

```bash
curl https://api.stripe.com/v1/balance \
  -u sk_test_your_key_here:
```

A successful response returns the account balance.

### Check environment variables

```bash
echo $STRIPE_SECRET_KEY
```

Ensure the environment variable is set correctly in your deployment environment.

### Regenerate the key if compromised

In the Stripe dashboard, create a new API key and update all systems using the old key before revoking it.

### Check for whitespace

```python
import os
key = os.environ.get("STRIPE_SECRET_KEY", "").strip()
```

Leading or trailing whitespace causes authentication failures.

### Verify key permissions

Some API keys have restricted permissions. Check the key's role in the dashboard:

- Full access keys can perform all operations
- Restricted keys may lack access to certain resources

### Use the correct SDK configuration

```python
import stripe
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
```

Ensure the SDK is configured with the correct key, not a hardcoded test key.

## Common Mistakes

- Committing API keys to version control and then revoking them
- Using the publishable key (`pk_...`) where the secret key (`sk_...`) is required
- Not rotating keys after a team member leaves
- Copying keys with extra spaces or newline characters
- Using test keys in production or live keys in development

## Related Pages

- [Stripe Authentication Error]({{< relref "/tools/stripe/stripe-authentication-error" >}}) -- general auth failures
- [Stripe Rate Limit]({{< relref "/tools/stripe/stripe-rate-limit" >}}) -- rate limiting
- [Stripe Webhook Error]({{< relref "/tools/stripe/stripe-webhook-error" >}}) -- webhook issues
