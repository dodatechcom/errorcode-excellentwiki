---
title: "[Solution] Flutter Firestore Error — get/set/update/delete, transaction"
description: "Fix Flutter Cloud Firestore errors from document operations, query failures, transaction conflicts, and permission rules."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 201
---

Firestore errors occur when document operations fail, queries are misconfigured, transactions conflict, or security rules deny access.

## Common Causes

1. Document path not matching Firestore structure.
2. Missing security rules allowing read/write.
3. Transaction conflicting due to concurrent modifications.
4. Query cursor or ordering errors.
5. Not handling `FirebaseFirestoreException` properly.

## How to Fix It

**Solution 1: Read and write documents**

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

Future<void> writeData() async {
  await FirebaseFirestore.instance.collection('users').doc('user1').set({
    'name': 'Alice',
    'email': 'alice@example.com',
    'age': 30,
    'createdAt': FieldValue.serverTimestamp(),
  });
}

Future<Map<String, dynamic>?> readData() async {
  DocumentSnapshot doc = await FirebaseFirestore.instance
      .collection('users')
      .doc('user1')
      .get();
  
  if (doc.exists) {
    return doc.data() as Map<String, dynamic>?;
  }
  return null;
}
```

**Solution 2: Update documents**

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

Future<void> updateData() async {
  await FirebaseFirestore.instance.collection('users').doc('user1').update({
    'age': FieldValue.increment(1),
  });
}

Future<void> deleteData() async {
  await FirebaseFirestore.instance.collection('users').doc('user1').delete();
}
```

**Solution 3: Query data**

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

Future<void> queryData() async {
  QuerySnapshot snapshot = await FirebaseFirestore.instance
      .collection('users')
      .where('age', isGreaterThan: 25)
      .orderBy('age', descending: true)
      .limit(10)
      .get();
  
  for (DocumentSnapshot doc in snapshot.docs) {
    Map<String, dynamic> data = doc.data() as Map<String, dynamic>;
    print('${doc.id}: ${data['name']}');
  }
}
```

**Solution 4: Use transactions**

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

Future<void> transferPoints(String fromId, String toId, int points) async {
  await FirebaseFirestore.instance.runTransaction((transaction) async {
    DocumentSnapshot fromDoc = await transaction.get(
      FirebaseFirestore.instance.collection('users').doc(fromId),
    );
    DocumentSnapshot toDoc = await transaction.get(
      FirebaseFirestore.instance.collection('users').doc(toId),
    );
    
    int fromPoints = (fromDoc.data() as Map<String, dynamic>)['points'] ?? 0;
    int toPoints = (toDoc.data() as Map<String, dynamic>)['points'] ?? 0;
    
    transaction.update(
      FirebaseFirestore.instance.collection('users').doc(fromId),
      {'points': fromPoints - points},
    );
    transaction.update(
      FirebaseFirestore.instance.collection('users').doc(toId),
      {'points': toPoints + points},
    );
  });
}
```

**Solution 5: Real-time listener**

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

Stream<QuerySnapshot> listenToUsers() {
  return FirebaseFirestore.instance
      .collection('users')
      .orderBy('name')
      .snapshots();
}

// Usage in a widget
Widget build(BuildContext context) {
  return StreamBuilder<QuerySnapshot>(
    stream: listenToUsers(),
    builder: (context, snapshot) {
      if (!snapshot.hasData) return CircularProgressIndicator();
      
      return ListView(
        children: snapshot.data!.docs.map((doc) {
          Map<String, dynamic> data = doc.data() as Map<String, dynamic>;
          return ListTile(title: Text(data['name']));
        }).toList(),
      );
    },
  );
}
```

## Examples

Add `cloud_firestore: ^4.14.0` to your `pubspec.yaml`. Ensure Firestore security rules allow the operations you're performing.

## Related Errors

- [Flutter Firebase Core Error](/languages/dart/flutter-firebase-core-error/)
- [Flutter Firebase Auth Error](/languages/dart/flutter-firebase-auth-error/)
- [Flutter Firebase Storage Error](/languages/dart/flutter-firebase-storage-error/)
