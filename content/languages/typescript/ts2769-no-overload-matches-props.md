---
title: "[Solution] TypeScript TS2769 — No overload matches this call (props)"
description: "TS2769 occurs when React component props don't match any overload."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the component's prop types."
---

The error "[Solution] TypeScript TS2769 — No overload matches this call (props)" occurs when ts2769 occurs when react component props don't match any overload.

## Solution

Check the component's prop types.

## Code Example

```typescript
interface Props { name: string; }
const Component = (props: Props) => {};
<Component name={42} /> // TS2769
```
