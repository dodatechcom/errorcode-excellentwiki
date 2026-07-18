---
title: "[Solution] Stripe Transfer Error - Fix Transfer Failed Account Not Linked"
description: "Fix Stripe transfer failures when moving funds to connected accounts. Resolve account onboarding, payout, and transfer destination issues."
tools: ["stripe"]
error-types: ["transfer-error"]
severities: ["error"]
weight: 5
---

This error means a Stripe transfer to a connected account failed. The destination account may not be fully onboarded, the transfer amount may exceed available balance, or the account may be restricted.

## What This Error Means

When you attempt to transfer funds and it fails, Stripe returns:

```
InvalidRequestError: No such destination: acct_xxx
# or
InvalidRequestError: Transfer amount must be less than or equal to the available
balance
# or
InvalidRequestError: The connected account is not currently capable of accepting transfers
```

Transfers move funds from your Stripe account to a connected account. Multiple conditions can prevent successful transfers.

## Why It Happens

- The connected account has not completed onboarding
- The connected account's payout capability is not enabled
- Your available balance is less than the transfer amount
- The transfer destination account is restricted or closed
- The currency of the transfer does not match the account's currency
- The connected account has a negative balance from refunds or disputes
- Platform charges were not properly configured

## How to Fix It

### Check connected account status

```python
account = stripe.Account.retrieve('acct_xxx')
print(account.charges_enabled)
print(account.payouts_enabled)
```

Both `charges_enabled` and `payouts_enabled` must be True for transfers.

### Verify available balance

```python
balance = stripe.Balance.retrieve()
for available in balance.available:
    print(available.currency, available.amount)
```

Ensure you have sufficient funds in the correct currency.

### Complete account onboarding

```python
account_link = stripe.AccountLink.create(
    account='acct_xxx',
    refresh_url='https://example.com/reauth',
    return_url='https://example.com/return',
    type='account_onboarding',
)
```

### Check transfer capability

```python
account = stripe.Account.retrieve('acct_xxx')
print(account.capabilities)
```

The `transfers` capability must be `active`.

### Use correct transfer destination

```python
stripe.Transfer.create(
    amount=1000,
    currency='usd',
    destination='acct_xxx',
    transfer_group='ORDER_95',
)
```

### Handle insufficient balance with top-ups

```python
stripe.TopUp.create(
    amount=5000,
    currency='usd',
    source={'type': 'bank_account', ...},
    description='Top-up for transfers',
)
```

### Set up destination charges

```python
stripe.PaymentIntent.create(
    amount=2000,
    currency='usd',
    application_fee_amount=200,
    transfer_data={
        'destination': 'acct_xxx',
    },
)
```

Destination charges handle transfers automatically during payment.

## Common Mistakes

- Not verifying connected account onboarding status before transfers
- Assuming transfers work for accounts that have not completed identity verification
- Not checking available balance before initiating transfers
- Using the wrong currency for the destination account
- Not setting up proper webhook handlers for transfer failures

## Related Pages

- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) -- payment processing
- [Stripe Customer Error]({{< relref "/tools/stripe/stripe-customer-error" >}}) -- customer management
- [Stripe Balance Insufficient]({{< relref "/tools/stripe/stripe-balance-insufficient" >}}) -- balance issues
