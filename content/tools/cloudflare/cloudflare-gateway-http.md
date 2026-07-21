---
title: "[Solution] Cloudflare Gateway HTTP Error"
description: "Fix Cloudflare Gateway HTTP errors. Resolve HTTP traffic filtering issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Gateway HTTP Error can prevent your application from working correctly.

## Common Causes

- Certificate not installed
- HTTPS inspection blocked
- Content categories blocked
- Application filtering too aggressive

## How to Fix

### Install Certificate

Download certificate from Zero Trust dashboard and install in system trust store.

### Configure Policy

1. Go to Zero Trust > Gateway > HTTP policies
2. Create inspection rules

