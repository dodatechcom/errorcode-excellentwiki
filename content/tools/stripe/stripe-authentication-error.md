---
title: "[Solution] Stripe API Authentication Error — No API Key Provided or Invalid Key"
description: "Fix Stripe API authentication errors. Resolve invalid or missing API key issues in your Stripe integration."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
---

A Stripe authentication error occurs when your request lacks a valid API key or the key you provided is invalid, revoked, or incorrectly formatted. Stripe requires every API call to include a valid secret key in the Authorization header.

## What This Error Means

Stripe returns an authentication error (HTTP 401) when it cannot verify your identity. The error message typically reads:

```
Invalid API Key provided: sk_test_...INVALID
```

or

```
No API key provided.
```

This means Stripe rejected your request before processing any business logic. Authentication always happens first.

## Why It Happens

- The API key is missing from the request headers
- The API key is malformed or contains extra whitespace
- You are using a test key in production or vice versa
- The API key was revoked in the Stripe Dashboard
- You are using the wrong key type (secret vs publishable)
- Environment variables are not loaded correctly
- The key was rotated and the old key is still in use

## How to Fix It

### Verify Your API Key

```bash
curl https://api.stripe.com/v1/balance \
  -u sk_test_YOUR_SECRET_KEY:
```

### Check Environment Variables

```bash
# Ensure STRIPE_SECRET_KEY is set
echo $STRIPE_SECRET_KEY

# Set it if missing
export STRIPE_SECRET_KEY=sk_test_your_key_here
```

### Node.js Example

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

// Verify the key works
const balance = await stripe.balance.retrieve();
console.log('Available:', balance.available[0].amount);
```

### Python Example

```python
import stripe
import os

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

# Verify the key works
balance = stripe.Balance.retrieve()
print(f"Available: {balance.available[0].amount}")
```

### Check Key in Dashboard

1. Go to https://dashboard.stripe.com/apikeys
2. Verify the key is active (not revoked)
3. Copy the correct key for your environment (test or live)

## Common Mistakes

- Copying the publishable key (pk_) instead of the secret key (sk_)
- Including newline characters when copying the key
- Using test keys in production mode
- Hardcoding keys instead of using environment variables
- Forgetting to set the key in serverless function environments
- Using the restricted key without the required permissions

## Related Pages

- [Stripe Rate Limit Error]({{< relref "/tools/stripe/stripe-rate-limit" >}}) — Too Many Requests (429)
- [Stripe Webhook Error]({{< relref "/tools/stripe/stripe-webhook-error" >}}) — Webhook signature verification failed
