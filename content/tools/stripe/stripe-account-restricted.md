---
title: "[Solution] Stripe Account Has Been Restricted Error — How to Fix"
description: "Fix Stripe account restricted errors by completing verification, resolving outstanding issues, submitting required documents, and maintaining compliance"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Account Has Been Restricted Error

This error means your Stripe account has been restricted and can no longer process payments, create payouts, or accept new charges. Stripe restricts accounts when verification is incomplete or compliance requirements are not met.

## Why It Happens

- Identity or business verification was not completed
- Required documents (business license, tax ID) were not submitted
- The account exceeded Stripe's dispute rate threshold
- Suspicious or prohibited activity was detected
- Bank account verification for payouts failed
- Terms of service violations
- Missing or outdated business information
- High-risk business category without proper documentation

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "account_invalid",
    "message": "Your account has been restricted. Please update your account information."
  }
}
```

```
{
  "object": "account",
  "capabilities": {
    "card_payments": "inactive",
    "transfers": "inactive"
  },
  "requirements": {
    "currently_due": ["business_profile.mcc", "individual.verification.document"]
  }
}
```

## How to Fix It

### 1. Check Account Status and Requirements

```javascript
const account = await stripe.accounts.retrieve('acct_abc123');

console.log('Status:', account.status);
console.log('Charges enabled:', account.charges_enabled);
console.log('Payouts enabled:', account.payouts_enabled);
console.log('Currently due:', account.requirements.currently_due);
console.log('Eventually due:', account.requirements.eventually_due);
console.log('Past due:', account.requirements.past_due);
```

### 2. Submit Required Documents

```javascript
// Upload identity verification document
const account = await stripe.accounts.update('acct_abc123', {
  individual: {
    verification: {
      document: {
        front: 'file_abc123',  // File uploaded via File uploads API
        back: 'file_def456'
      }
    }
  }
});

// Submit business profile
await stripe.accounts.update('acct_abc123', {
  business_profile: {
    mcc: '5734',  // Merchant Category Code
    url: 'https://example.com',
    name: 'My Business Inc'
  }
});
```

### 3. Upload Verification Files

```javascript
// Step 1: Create a file upload
const file = await stripe.files.create({
  purpose: 'identity_document',
  file: {
    data: fs.readFileSync('./business_license.pdf'),
    name: 'business_license.pdf',
    type: 'application/pdf'
  }
});

// Step 2: Attach to account
await stripe.accounts.update('acct_abc123', {
  business_profile: {
    support_address: {
      line1: '123 Main St',
      city: 'San Francisco',
      state: 'CA',
      postal_code: '94105',
      country: 'US'
    }
  }
});
```

### 4. Handle Restricted Connected Accounts (Platforms)

```javascript
// For Connect platforms: check all connected accounts
const accounts = await stripe.accounts.list({
  limit: 100
});

for (const acct of accounts.data) {
  if (acct.requirements.currently_due.length > 0) {
    console.log(`Account ${acct.id} needs attention:`, acct.requirements.currently_due);
  }
}
```

## Common Scenarios

- **New account missing business info**: Stripe requires a business URL, MCC code, and description within 30 days. Provide these in the Dashboard or via the API.
- **Identity document rejected**: The uploaded document was blurry or expired. Retake the photo with good lighting and ensure the document is current.
- **High dispute rate**: The account dispute rate exceeded 1%. Work with Stripe support and implement fraud prevention to reduce disputes.

## Prevent It

- Complete Stripe onboarding within the first few days of creating the account
- Monitor `account.requirements.currently_due` via webhooks and respond immediately
- Keep business documents (license, tax filings) updated in your records

## Related Pages

- [Stripe Charge Disputed](/tools/stripe/stripe-charge-disputed)
- [Stripe Payout Error](/tools/stripe/stripe-payout-error)
- [Stripe Account Restricted](/tools/stripe/stripe-account-restricted)
