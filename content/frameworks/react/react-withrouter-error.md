---
title: "[Solution] React withRouter Error"
description: "withRouter not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

withRouter not working.

## Common Causes

Wrong import.

## How to Fix

Import correctly.

## Example

```javascript
import { withRouter } from 'next/router';
function Page({ router }) { return <div>{router.pathname}</div>;
}
export default withRouter(Page);
```
