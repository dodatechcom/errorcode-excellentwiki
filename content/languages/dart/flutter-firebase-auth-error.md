---
title: "[Solution] Flutter Firebase Auth Error — signIn, signUp, user, idToken"
description: "Fix Flutter FirebaseAuth errors from signIn/signUp failures, user state, idToken handling, and auth state changes."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 200
---

Firebase Auth errors occur when sign-in/sign-up fails, user state is not properly handled, or token management is incorrect.

## Common Causes

1. Email/password sign-in failing due to weak password.
2. Not handling `FirebaseAuthException` properly.
3. `user` accessed when no user is signed in.
4. Not listening to auth state changes.
5. idToken not refreshed before expiry.

## How to Fix It

**Solution 1: Email/password authentication**

```dart
import 'package:firebase_auth/firebase_auth.dart';

Future<void> signUp(String email, String password) async {
  try {
    UserCredential credential = await FirebaseAuth.instance
        .createUserWithEmailAndPassword(
      email: email,
      password: password,
    );
    
    print('User created: ${credential.user?.uid}');
  } on FirebaseAuthException catch (e) {
    if (e.code == 'weak-password') {
      print('Password is too weak');
    } else if (e.code == 'email-already-in-use') {
      print('Email already registered');
    }
  }
}

Future<void> signIn(String email, String password) async {
  try {
    UserCredential credential = await FirebaseAuth.instance
        .signInWithEmailAndPassword(
      email: email,
      password: password,
    );
    
    print('Signed in: ${credential.user?.email}');
  } on FirebaseAuthException catch (e) {
    if (e.code == 'user-not-found') {
      print('No user found');
    } else if (e.code == 'wrong-password') {
      print('Wrong password');
    }
  }
}
```

**Solution 2: Listen to auth state changes**

```dart
import 'package:firebase_auth/firebase_auth.dart';

class AuthWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return StreamBuilder<User?>(
      stream: FirebaseAuth.instance.authStateChanges(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return CircularProgressIndicator();
        }
        
        if (snapshot.hasData) {
          return HomePage(user: snapshot.data!);
        }
        
        return LoginPage();
      },
    );
  }
}
```

**Solution 3: Get user token**

```dart
import 'package:firebase_auth/firebase_auth.dart';

Future<String?> getIdToken() async {
  User? user = FirebaseAuth.instance.currentUser;
  
  if (user == null) return null;
  
  String? token = await user.getIdToken();
  print('Token: ${token?.substring(0, 50)}...');
  
  return token;
}

Future<String?> getRefreshToken() async {
  User? user = FirebaseAuth.instance.currentUser;
  if (user == null) return null;
  
  // Force token refresh
  String? token = await user.getIdToken(true);
  return token;
}
```

**Solution 4: Sign out**

```dart
import 'package:firebase_auth/firebase_auth.dart';

Future<void> signOut() async {
  await FirebaseAuth.instance.signOut();
  print('User signed out');
}
```

**Solution 5: Handle phone authentication**

```dart
import 'package:firebase_auth/firebase_auth.dart';

Future<void> verifyPhoneNumber(
  String phoneNumber,
  Function(String) onCodeSent,
) async {
  await FirebaseAuth.instance.verifyPhoneNumber(
    phoneNumber: phoneNumber,
    verificationCompleted: (PhoneAuthCredential credential) async {
      await FirebaseAuth.instance.signInWithCredential(credential);
    },
    verificationFailed: (FirebaseAuthException e) {
      print('Verification failed: ${e.message}');
    },
    codeSent: (String verificationId, int? resendToken) {
      onCodeSent(verificationId);
    },
    codeAutoRetrievalTimeout: (String verificationId) {},
  );
}
```

## Examples

Add `firebase_auth: ^4.16.0` to your `pubspec.yaml`. Ensure `Firebase.initializeApp()` is called before any auth operations.

## Related Errors

- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
- [Flutter Firestore Error](/languages/dart/flutter-firestore-error/)
- [Flutter Secure Storage Error](/languages/dart/flutter-secure-storage-error/)
