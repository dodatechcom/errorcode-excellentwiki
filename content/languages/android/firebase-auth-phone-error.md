---
title: "Firebase Phone Auth Error"
description: "Fix Firebase phone number authentication and verification code errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase phone authentication fails to send or verify code

## Common Causes

- Phone number format incorrect with country code
- Verification ID not received
- Verification code expired or incorrect
- Phone number not registered in Firebase console

## Fixes

- Format phone number with +[country code]
- Wait for verification callback before proceeding
- Handle verification timeout
- Add phone number provider in Firebase console

## Code Example

```kotlin
val auth = FirebaseAuth.getInstance()

// Start verification
val options = PhoneAuthOptions.newBuilder(auth)
    .setPhoneNumber("+1234567890")
    .setTimeout(60L, TimeUnit.SECONDS)
    .setActivity(this)
    .setCallbacks(object : PhoneAuthProvider.OnVerificationStateChangedCallbacks() {
        override fun onVerificationCompleted(credential: PhoneAuthCredential) {
            // Auto-retrieval on some devices
            signInWithCredential(credential)
        }

        override fun onVerificationFailed(e: FirebaseException) {
            Log.e("Auth", "Phone verification failed", e)
        }

        override fun onCodeSent(verificationId: String, token: PhoneAuthProvider.ForceResendingToken) {
            // Store verificationId, send code to user
            this@Activity.verificationId = verificationId
        }
    })
    .build()

PhoneAuthProvider.verifyPhoneNumber(options)
```

# Enable Phone auth in Firebase console
# Handle both auto-retrieval and manual code entry
# Store verificationId for code verification step
