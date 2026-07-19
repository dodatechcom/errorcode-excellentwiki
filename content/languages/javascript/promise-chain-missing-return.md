---
title: "[Solution] Promise Chain Missing Return — Undefined Value Fix"
description: "Fix promise chains that lose return values, resulting in undefined. Always return in .then() callbacks."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Promise Chain Missing Return

```javascript
// BUG — missing return
fetchUser().then(user => {
  fetchPosts(user.id);  // posts lost!
}).then(posts => {
  console.log(posts); // undefined
});

// Fix
fetchUser().then(user => {
  return fetchPosts(user.id); // return the promise
}).then(posts => {
  console.log(posts); // works
});
```
