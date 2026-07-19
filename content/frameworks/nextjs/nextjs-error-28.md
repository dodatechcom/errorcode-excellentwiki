---
title: "Next.js App Router intercepting routes errors"
description: "Next.js errors related to intercepting routes using the (..) syntax. Common issues include incorrect route interception patterns, missing modals, or intercepted routes not rendering correctly."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "intercepting-routes", "modals", "routing"]
severity: "error"
solution: "Understand the (..) syntax for route interception. Use (.) for same-level interception, (..) for one level up, and (..)(..) for two levels up. Combine with parallel routes for modals."
---

Next.js errors related to intercepting routes using the (..) syntax. Common issues include incorrect route interception patterns, missing modals, or intercepted routes not rendering correctly.

## Solution

Understand the (..) syntax for route interception. Use (.) for same-level interception, (..) for one level up, and (..)(..) for two levels up. Combine with parallel routes for modals.

## Code Example

```javascript
  // BAD: Incorrect interception syntax
  // app/(.)photo/[id]/page.tsx - Wrong path
  export default function PhotoModal() {
    return <div>Modal</div>;
  }
  
  // GOOD: Proper intercepting routes
  // app/@modal/(.)photo/[id]/page.tsx
  export default function PhotoModal({ params }) {
    return (
      <div className="modal">
        <h2>Photo {params.id}</h2>
        <CloseButton />
      </div>
    );
  }
  
  // app/layout.tsx
  export default function Layout({ children, modal }) {
    return (
      <html>
        <body>
          {children}
          {modal}
        </body>
      </html>
    );
  }
  
  // app/@modal/default.tsx
  export default function Default() {
    return null;
  }
  
  // GOOD: Same-level interception
  // app/feed/(.)photo/[id]/page.tsx
  export default function PhotoModal() {
    return (
      <Modal>
        <PhotoDetails />
      </Modal>
    );
  }
  
  // app/feed/photo/[id]/page.tsx (Normal page for direct access)
  export default function PhotoPage() {
    return (
      <div>
        <PhotoDetails />
        <Comments />
      </div>
    );
  }
  
  // GOOD: Multiple interception levels
  // Parent level: app/(.)shop/page.tsx
  export default function ShopModal() {
    return <Modal><ShopContent /></Modal>;
  }
  
  // Two levels up: app/(..)(..)dashboard/page.tsx  
  export default function DashboardIntercept() {
    return <Modal><DashboardContent /></Modal>;
  }
```
