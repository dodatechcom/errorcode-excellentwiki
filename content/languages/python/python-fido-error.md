---
title: "[Solution] Python WebAuthn Error — How to Fix"
description: "Fix Python WebAuthn errors. Resolve registration, authentication, and attestation issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python WebAuthn Error

A `webauthn.exceptions.WebAuthnException` or `InvalidSignatureError` occurs when WebAuthn fails to verify credentials, encounters attestation errors, or when the challenge is invalid.

## Why It Happens

WebAuthn provides passwordless authentication. Errors arise when the origin does not match, when the challenge has expired, when attestation is invalid, or when the credential is not found.

## Common Error Messages

- `WebAuthnException: Origin mismatch`
- `InvalidSignatureError: Invalid signature`
- `WebAuthnException: Challenge expired`
- `CredentialNotFoundError: Credential not found`

## How to Fix It

### Fix 1: Configure relying party

```python
from webauthn import generate_registration_options, verify_registration_response

# Wrong — no relying party configuration
# options = generate_registration_options(user_id=b"user")

# Correct — configure relying party
options = generate_registration_options(
    rp_name="My App",
    rp_id="example.com",
    user_id=b"user123",
    user_name="user@example.com",
)
```

### Fix 2: Handle registration

```python
from webauthn import generate_registration_options, verify_registration_response

# Generate options
options = generate_registration_options(
    rp_name="My App",
    rp_id="example.com",
    user_id=b"user123",
    user_name="user@example.com",
)

# Verify response
try:
    verification = verify_registration_response(
        credential=credential_data,
        expected_challenge=challenge,
        expected_origin="https://example.com",
        expected_rp_id="example.com",
    )
    # Store credential
    save_credential(verification)
except Exception as e:
    print(f"Registration failed: {e}")
```

### Fix 3: Handle authentication

```python
from webauthn import generate_authentication_options, verify_authentication_response

# Generate options
options = generate_authentication_options(
    rp_id="example.com",
    allow_credentials=[credential_id],
)

# Verify response
try:
    verification = verify_authentication_response(
        credential=credential_data,
        expected_challenge=challenge,
        expected_origin="https://example.com",
        expected_rp_id="example.com",
        credential_public_key=public_key,
        credential_current_sign_count=sign_count,
    )
    # Update sign count
    update_sign_count(verification.new_sign_count)
except Exception as e:
    print(f"Authentication failed: {e}")
```

## Common Scenarios

- **Origin mismatch** — Request origin does not match registered relying party.
- **Challenge expired** — Challenge has exceeded the allowed time window.
- **Invalid attestation** — Attestation statement cannot be verified.

## Prevent It

- Always verify the origin matches your domain exactly.
- Set appropriate challenge timeout (recommended: 60 seconds).
- Store the credential public key and sign count securely.

## Related Errors

- [WebAuthnException](/languages/python/webauthn-error/) — WebAuthn operation failed
- [InvalidSignatureError](/languages/python/invalid-signature/) — signature verification failed
- [ChallengeExpired](/languages/python/challenge-expired/) — challenge timeout
