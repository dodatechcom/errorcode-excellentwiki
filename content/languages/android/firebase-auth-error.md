---
title: "Firebase Authentication Error"
description: "Fix Firebase Authentication errors for email, Google, and phone sign-in"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase Authentication fails with credential or configuration errors

## Common Causes

- Email/password sign-in requires email verification first
- Google Sign-In SHA-1 fingerprint not registered
- Phone auth quota exceeded or invalid verification code
- Auth state listener not properly registered

## Fixes

- Verify email before sign-in or disable verification
- Add SHA-1 fingerprint to Firebase project
- Check phone number format with country code
- Use addAuthStateListener to track sign-in state

## Code Example

```kotlin
// Email sign-in
firebaseAuth.signInWithEmailAndPassword(email, password)
    .addOnCompleteListener { task ->
        if (task.isSuccessful) {
            val user = firebaseAuth.currentUser
        } else {
            Log.e("Auth", "Failed: ${task.exception?.message}")
        }
    }

// Get SHA-1 for Google Sign-In:
// ./gradlew signingReport
```

# Firebase Console > Project Settings > Add SHA-1
# SHA-1: keytool -list -v -keystore my-key.jks
