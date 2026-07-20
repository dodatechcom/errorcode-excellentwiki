---
title: "[Solution] JavaScript Electron Runtime Error — How to Fix"
description: "Fix JavaScript Electron main/renderer process errors, contextBridge, IPC communication, and security warning issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 806
---

# JavaScript Electron Runtime Error

An `Error`, `TypeError`, or `SecurityError` occurs when Electron's main and renderer processes communicate incorrectly, `contextBridge` APIs are not exposed, IPC channels mismatch, or security best practices are violated.

## Why It Happens

Electron errors arise from using Node.js APIs directly in the renderer without `contextIsolation`, `ipcMain`/`ipcRenderer` channel name mismatches, `contextBridge` not exposing methods correctly, and missing `preload` script configuration.

## Common Error Messages

- `TypeError: Cannot read properties of undefined (reading 'send')`
- `Error: require() is not defined in the renderer process`
- `Uncaught Error: IPC channel 'xxx' is not registered`
- `SecurityError: Blocked a frame with origin from accessing a cross-origin frame`
- `Error: contextBridge API is not a function`

## How to Fix It

### Fix 1: Configure preload script with contextBridge

```javascript
// preload.js
const { contextBridge, ipcRenderer } = require('electron')

// ❌ Wrong - exposing entire ipcRenderer
// contextBridge.exposeInMainWorld('electron', require('electron'))

// ✅ Correct - expose specific channels
contextBridge.exposeInMainWorld('api', {
  sendMessage: (msg) => ipcRenderer.invoke('send-message', msg),
  onMessage: (callback) => ipcRenderer.on('message', callback)
})
```

### Fix 2: Enable contextIsolation in main process

```javascript
// main.js
const { BrowserWindow } = require('electron')

const win = new BrowserWindow({
  webPreferences: {
    // ❌ Wrong - disabling security
    // nodeIntegration: true,
    // contextIsolation: false

    // ✅ Correct
    nodeIntegration: false,
    contextIsolation: true,
    preload: path.join(__dirname, 'preload.js')
  }
})
```

### Fix 3: Match IPC channel names

```javascript
// main.js
const { ipcMain } = require('electron')

// ❌ Wrong - channel name 'save-file' in main
// ipcMain.handle('save-file', async (event, data) => {})

// ✅ Correct
ipcMain.handle('save-file', async (event, data) => {
  await fs.writeFile(data.path, data.content)
  return { success: true }
})
```

```javascript
// preload.js
contextBridge.exposeInMainWorld('api', {
  // ❌ Wrong - channel 'save' doesn't match
  // saveFile: (data) => ipcRenderer.invoke('save', data)

  // ✅ Correct - channel must match
  saveFile: (data) => ipcRenderer.invoke('save-file', data)
})
```

### Fix 4: Handle IPC errors

```javascript
// preload.js
contextBridge.exposeInMainWorld('api', {
  getData: async () => {
    try {
      return await ipcRenderer.invoke('get-data')
    } catch (error) {
      console.error('IPC failed:', error)
      return null
    }
  }
})
```

## Examples

Two-way IPC communication with progress:

```javascript
// main.js
ipcMain.handle('process-file', async (event, filePath) => {
  // ✅ Send progress updates to renderer
  event.sender.send('progress', { percent: 50 })
  const result = await processFile(filePath)
  return result
})
```

## Related Errors

- [Electron Build Error](/languages/javascript/electron-build-error)
- [JavaScript TypeError](/languages/javascript/typeerror)
- [JavaScript SecurityError](/languages/javascript/securityerror-dom-exception)
