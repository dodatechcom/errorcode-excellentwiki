---
title: "[Solution] Service Worker Cache API Error — CacheStorage Fix"
description: "Fix errors with Cache API in Service Workers. Handle CacheStorage.open() failures and quota issues."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Service Worker Cache Error

```javascript
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) return response;
      return fetch(event.request).catch(() => {
        return new Response('Offline', { status: 503 });
      });
    })
  );
});
```

Handle cache errors:

```javascript
try {
  const cache = await caches.open('v1');
  await cache.addAll(urlsToCache);
} catch (err) {
  console.error('Cache failed:', err);
}
```
