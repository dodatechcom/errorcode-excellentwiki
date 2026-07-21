---
title: "[Solution] Vercel Wildcard Domain Error"
description: "Fix Vercel wildcard domain errors. Resolve wildcard domain configuration issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Wildcard Domain Error can prevent your application from working correctly.

## Common Causes

- Wildcard not configured
- SSL certificate not issued
- DNS record missing

## How to Fix

### Add Wildcard Domain

1. Go to Project Settings > Domains
2. Add `*.example.com`

### Configure DNS

Add CNAME record: `*.example.com` -> `cname.vercel-dns.com`

