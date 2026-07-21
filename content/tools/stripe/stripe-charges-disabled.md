---
title: "[Solution] Stripe Charges Disabled"
description: "Fix Stripe charges disabled errors. Enable charges on your Stripe account and resolve restrictions."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

## Error Description

The Stripe API returned a `charges_disabled` error. This error occurs when your account cannot process charges due to verification or configuration issues.

A typical error:

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "charges_disabled",
    "message": "Charges are disabled for this account."
  }
}
```

## Common Causes

- **Account not verified**: Stripe requires identity verification before enabling charges.
- **Restricted account**: Account restrictions prevent charge processing.
- **Missing business profile**: Business information is incomplete.
- **Compliance review**: Account is under review for compliance issues.
- **Country restrictions**: Charges are restricted in your country.

## How to Fix It

**Step 1: Check account status**

```python
import stripe
stripe.api_key = "sk_test_..."

account = stripe.Account.retrieve()
print(f"Charges enabled: {account.charges_enabled}")
print(f"Payouts enabled: {account.payouts_enabled}")
print(f"Requirements: {account.requirements}")
```

**Step 2: Complete account verification**

```python
# Update business profile
stripe.Account.modify(
    "acct_...",
    business_profile={
        "mcc": "5734",
        "name": "Your Business Name",
        "url": "https://yourbusiness.com",
    },
)
```

**Step 3: Submit verification documents**

```python
# Upload identity document
stripe.Account.create_login_link("acct_...")
```

**Step 4: Check dashboard for requirements**

Visit [Stripe Dashboard](https://dashboard.stripe.com) to see pending requirements.

## Common Scenarios

**New account.**
New Stripe accounts require business verification before charges are enabled. Complete the onboarding process in the Dashboard.

**Test mode.**
Ensure you are using the correct API keys. Use `sk_test_...` for test mode and `sk_live_...` for live mode.

## Prevention

1. Complete Stripe onboarding immediately after account creation
2. Keep business information up to date in the Dashboard
3. Monitor account status regularly
4. Respond to Stripe verification requests promptly
