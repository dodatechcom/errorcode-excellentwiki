---
title: "[Solution] Fiber Internationalization Error -- How to Fix"
description: "Fix Fiber i18n errors. Resolve language detection, translation loading, and locale issues."
frameworks: ["fiber"]
error-types: ["i18n-error"]
severities: ["warning"]
weight: 5
comments: true
---

A Fiber internationalization error occurs when the application cannot properly detect or apply the correct language.

## Why It Happens

i18n errors happen due to missing translation files, incorrect locale detection, or missing language headers.

## Common Error Messages

```
translation not found
```

```
locale not supported
```

```
language file missing
```

```
invalid locale
```

## How to Fix It

### 1. Load Translations

Set up i18n with translation files.

```go
import "github.com/gofiber/fiber/v2/middleware/i18n"

app.Use(i18n.New(i18n.Config{
    Default: "en",
    RootDirectory: "locales",
    AcceptLanguages: map[string]string{"en": "en-US", "zh": "zh-CN"},
}))
```

### 2. Detect Language

Use Accept-Language header.

```go
app.Use(i18n.New(i18n.Config{
    DetectFromHeader: true,
}))
```

### 3. Use Translation Function

Get translated strings.

```go
app.Get("/hello", func(c *fiber.Ctx) error {
    return c.SendString(i18n.Message(c, "hello"))
})
```

### 4. Set Default Language

Provide fallback translations.

```go
app.Use(i18n.New(i18n.Config{
    Default: "en",
}))
```

## Common Scenarios

**Scenario 1: Translation not found.**
Check translation file exists.

**Scenario 2: Wrong language shown.**
Check Accept-Language header.

## Prevent It

1. **Always provide default translations.**


2. **Use proper locale files.**


3. **Test with different languages.**


