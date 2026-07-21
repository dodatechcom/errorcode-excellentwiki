---
title: "Firestore Database Error"
description: "Fix Firebase Firestore database errors and security rule issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firestore reads or writes fail because of security rules or configuration

## Common Causes

- Security rules deny read/write access
- Firestore not initialized before use
- Document reference path incorrect
- Offline persistence not enabled properly

## Fixes

- Test security rules with Firebase emulator
- Initialize Firestore before any database operation
- Verify document path matches expected structure
- Enable offline persistence for offline support

## Code Example

```kotlin
// Initialize Firestore
val db = Firebase.firestore

// Read data
db.collection("users")
    .document(userId)
    .get()
    .addOnSuccessListener { document ->
        val user = document.toObject(User::class.java)
    }

// Write data
db.collection("users")
    .document(userId)
    .set(user)
    .addOnSuccessListener { /* success */ }
    .addOnFailureListener { e -> /* handle error */ }
```

# Test rules with emulator:
# firebase emulators:start
# Or deploy rules: firebase deploy --only firestore:rules
