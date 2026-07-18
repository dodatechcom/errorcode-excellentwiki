---
title: "[Solution] Stripe Payout Failed or Delayed Error — How to Fix"
description: "Fix Stripe payout failures by verifying bank details, checking balance availability, resolving payout declines, and configuring payout schedules"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Payout Failed or Delayed Error

This error means a payout from your Stripe balance to your connected bank account or debit card failed or was delayed. Payouts can fail due to invalid bank information, bank declines, or insufficient available balance.

## Why It Happens

- The bank account or debit card on file is invalid or has been closed
- The available balance is less than the payout amount
- The bank returned the payout (ACH return code)
- The payout was sent to a restricted or closed bank account
- The payout schedule has not yet reached the payout date
- Stripe's risk system flagged the payout for manual review
- Cross-border payout currency mismatches
- The bank account has not been verified

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "payout_failed",
    "message": "The bank account has been closed."
  }
}
```

```
{
  "object": "payout",
  "status": "failed",
  "failure_code": "bank_declined",
  "failure_message": "The bank account on file is no longer valid."
}
```

```
{
  "object": "payout",
  "status": "in_transit",
  "arrival_date": 1706217600
}
```

## How to Fix It

### 1. Check Payout Status and Failure Details

```javascript
const payout = await stripe.payouts.retrieve('po_abc123');

console.log('Status:', payout.status);
console.log('Failure code:', payout.failure_code);
console.log('Failure message:', payout.failure_message);
console.log('Expected arrival:', new Date(payout.arrival_date * 1000));
```

### 2. Verify Bank Account Details

```javascript
// Check the connected bank account
const bankAccount = await stripe.accounts.retrieveExternalAccount(
  'acct_abc123',
  'ba_xyz789'
);

console.log('Bank:', bankAccount.bank_name);
console.log('Last 4:', bankAccount.last4);
console.log('Status:', bankAccount.status);
console.log('Default for payout:', bankAccount.default_for_currency);
```

### 3. Update Bank Account Information

```javascript
// Delete the old bank account
await stripe.accounts.deleteExternalAccount(
  'acct_abc123',
  'ba_xyz789'
);

// Add new bank account
const bankAccount = await stripe.accounts.createExternalAccount(
  'acct_abc123',
  {
    external_account: {
      object: 'bank_account',
      country: 'US',
      currency: 'usd',
      account_number: '000123456789',
      routing_number: '110000000'
    },
    default_for_currency: true
  }
);
```

### 4. Create a Manual Payout

```javascript
// Instead of waiting for automatic payout, create one manually
const payout = await stripe.payouts.create({
  amount: 50000,  // $500.00 in cents
  currency: 'usd'
});

console.log('Payout created:', payout.id);
```

### 5. Check Balance Before Payout

```javascript
const balance = await stripe.balance.retrieve();
const available = balance.available.find(b => b.currency === 'usd');

if (!available || available.amount < payoutAmount) {
  console.log('Insufficient balance for payout');
  console.log('Available:', available?.amount / 100 || 0);
  return;
}

// Proceed with payout
await stripe.payouts.create({
  amount: payoutAmount,
  currency: 'usd'
});
```

## Common Scenarios

- **Bank account closed**: Customer changed banks. Update the bank account via the Stripe Dashboard or API and retry the payout.
- **ACH return code R01**: Insufficient funds in the Stripe account. Wait for pending charges to settle or reduce the payout amount.
- **Weekend payout delay**: Payouts initiated on Friday arrive on Monday. Configure the payout schedule to account for banking days.

## Prevent It

- Monitor payout webhooks (`payout.paid`, `payout.failed`) to react quickly to failures
- Verify bank accounts before setting them as the default payout destination
- Keep a small reserve in the Stripe account to cover payout amounts during settlement periods

## Related Pages

- [Stripe Balance Error](/tools/stripe/stripe-balance-error)
- [Stripe Account Restricted](/tools/stripe/stripe-account-restricted)
- [Stripe Payout Error](/tools/stripe/stripe-payout-error)
