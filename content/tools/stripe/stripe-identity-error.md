---
title: "[Solution] Stripe Identity Verification Failed Error — How to Fix"
description: "Fix Stripe identity verification errors by resubmitting documents, resolving mismatched information, handling expired IDs, and using the VerificationSessions API"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Identity Verification Failed Error

This error means Stripe Identity could not verify the user's identity document or selfie. Verification can fail due to unclear images, mismatched data between the ID and provided information, or unsupported document types.

## Why It Happens

- The uploaded ID photo is blurry, cropped, or has glare
- The name or date of birth on the ID does not match the provided information
- The ID is expired
- The selfie does not match the ID photo
- The ID is from a country not supported by Stripe Identity
- The document type is not accepted (e.g., a student ID)
- The user is under the minimum age requirement
- The verification session expired before completion

## Common Error Messages

```
{
  "verification": {
    "status": "unverified",
    "last_error": {
      "code": "document_unverified",
      "reason": "document_not_supported",
      "message": "The document type is not supported."
    }
  }
}
```

```
{
  "last_error": {
    "code": "selfie_failed",
    "reason": "selfie_mismatch",
    "message": "The selfie does not match the photo on the document."
  }
}
```

```
{
  "last_error": {
    "code": "document_expired",
    "reason": "document_expired",
    "message": "The document has expired."
  }
}
```

## How to Fix It

### 1. Check Verification Status

```python
import stripe

session = stripe.identity.VerificationSession.retrieve('vs_abc123')

print('Status:', session.status)
print('Last error:', session.last_error)
```

### 2. Allow the User to Resubmit

```javascript
// Create a new verification session after failure
const session = await stripe.identity.verificationSessions.create({
  type: 'document',
  metadata: {
    user_id: 'user_123'
  },
  options: {
    document: {
      require_id_number: true,
      require_live_selfie: true
    }
  }
});

// Redirect the user to the session URL
console.log('Redirect to:', session.url);
```

### 3. Validate Data Before Submission

```javascript
// Ensure submitted data matches the ID before verification
function validateIdentityData(formData, idData) {
  const errors = [];

  if (formData.fullName.toLowerCase() !== idData.fullName.toLowerCase()) {
    errors.push('Name does not match ID');
  }

  if (formData.dateOfBirth !== idData.dateOfBirth) {
    errors.push('Date of birth does not match ID');
  }

  if (new Date(idData.expiryDate) < new Date()) {
    errors.push('ID is expired');
  }

  return errors;
}
```

### 4. Handle Verification via API Reports

```javascript
// Check the detailed verification report
const report = await stripe.identity.VerificationReport.retrieve('vr_abc123');

console.log('Document result:', report.document);
console.log('Selfie result:', report.selfie);

// Use the report to make business decisions
if (report.document.status === 'unverified') {
  console.log('Reason:', report.document.last_error.reason);
}
```

### 5. Support Multiple Document Types

```javascript
const session = await stripe.identity.verificationSessions.create({
  type: 'document',
  options: {
    document: {
      // Accept multiple document types
      allowed_types: ['driving_license', 'passport', 'id_card']
    }
  }
});
```

## Common Scenarios

- **International customer**: A customer submits an ID from a country Stripe Identity does not support. Advise them to use a passport or check Stripe's supported countries list.
- **Name mismatch**: The customer legally changed their name but the ID still shows the old name. Ask them to provide an additional supporting document or use manual review.
- **Expired driver's license**: Customer's license expired 6 months ago. Ask for a passport or national ID card instead.

## Prevent It

- Provide clear instructions to users about photo quality requirements before they submit
- Validate form data against the ID data before creating the verification session
- Offer multiple verification methods (document + selfie) for higher pass rates

## Related Pages

- [Stripe Account Restricted](/tools/stripe/stripe-account-restricted)
- [Stripe Tax Error](/tools/stripe/stripe-tax-error)
- [Stripe Identity Error](/tools/stripe/stripe-identity-error)
