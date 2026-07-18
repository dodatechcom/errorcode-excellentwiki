---
title: "[Solution] C Vulkan Error — How to Fix"
description: "Fix C Vulkan errors including instance creation, device selection, and swapchain issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Vulkan Error — How to Fix

Vulkan errors include out-of-memory, validation layer failures, and wrong queue family selection.

## Common Error Messages

- `VK_ERROR_OUT_OF_HOST_MEMORY`
- `VK_ERROR_INCOMPATIBLE_DRIVER`
- `VK_ERROR_LAYER_NOT_PRESENT`
- `VK_ERROR_EXTENSION_NOT_PRESENT`

## How to Fix It

### Check VkResult

```c
#include <vulkan/vulkan.h>
VkResult create_inst(VkInstance *i) {
    VkApplicationInfo app = {VK_STRUCTURE_TYPE_APPLICATION_INFO, NULL,
        "App", VK_MAKE_VERSION(1,0,0), "E", VK_MAKE_VERSION(1,0,0), VK_API_VERSION_1_0};
    VkInstanceCreateInfo ci = {VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO, NULL, 0, &app, 0, NULL, 0, NULL};
    return vkCreateInstance(&ci, NULL, i);
}
```

### Validation layers

```c
const char *layers[] = {"VK_LAYER_KHRONOS_validation"};
VkInstanceCreateInfo ci = {VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO, NULL, 0, NULL, 1, layers, 0, NULL};
```

### Find queue family

```c
uint32_t find_qf(VkPhysicalDevice d) {
    uint32_t c; vkGetPhysicalDeviceQueueFamilyProperties(d, &c, NULL);
    VkQueueFamilyProperties f[64]; vkGetPhysicalDeviceQueueFamilyProperties(d, &c, f);
    for (uint32_t i = 0; i < c; i++) if (f[i].queueFlags & VK_QUEUE_GRAPHICS_BIT) return i;
    return UINT32_MAX;
}
```

### Logical device

```c
float pri = 1.0f;
VkDeviceQueueCreateInfo qci = {VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO, NULL, 0, 0, 1, &pri};
VkDeviceCreateInfo dci = {VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO, NULL, 0, 0, 1, &qci, 0, NULL, 0, NULL};
```

## Common Scenarios

### Scenario 1: Instance fails with INCOMPATIBLE_DRIVER

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 2: Validation layer not found

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values.

### Scenario 3: No graphics queue family

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values.

## Prevent It

- **Tip 1:** Check VkResult from every call
- **Tip 2:** Enable validation layers in dev
- **Tip 3:** Query device properties first
