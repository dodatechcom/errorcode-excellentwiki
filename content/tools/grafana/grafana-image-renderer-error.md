---
title: "[Solution] Grafana Image Renderer Error"
description: "Fix Grafana image renderer errors. Learn why this happens and how to resolve it quickly."
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Grafana Image Renderer Error

Grafana image renderer errors occur when the rendering service fails to generate images for reports or panels.

## Why This Happens

- Renderer not running
- Timeout exceeded
- Font missing
- Memory limit

## Common Error Messages

- `renderer_not_found`
- `renderer_timeout`
- `renderer_font_error`
- `renderer_memory_error`

## How to Fix It

### Solution 1: Start renderer service

Install and start the renderer:

```bash
npm install -g @grafana/renderer
grafana-image-renderer
```

### Solution 2: Increase timeout

Adjust rendering timeout:

```ini
[rendering]
timeout = 60
```

### Solution 3: Install fonts

Install required fonts for the renderer.


## Common Scenarios

- **Renderer not responding:** Restart the renderer service.
- **Timeout exceeded:** Increase timeout or optimize the panel.

## Prevent It

- Start renderer service
- Install fonts
- Monitor renderer health
