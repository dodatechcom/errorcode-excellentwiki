---
title: "[Solution] Go Wails Error — How to Fix"
description: "Fix Go Wails errors. Handle application setup, frontend integration, and runtime communication."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Wails Error

Fix Go Wails errors. Handle application setup, frontend integration, and runtime communication.

## Why It Happens

- Wails application does not start because of wrong configuration
- Frontend does not load because of wrong build directory
- Runtime calls from frontend fail because Go methods are not bound

## Common Error Messages

```
wails: application not started
```
```
wails: frontend not found
```
```
wails: method not bound
```
```
wails: build failed
```

## How to Fix It

### Solution 1: Initialize Wails app

```go
import "github.com/wailsapp/wails/v2"
func main() {
    app := wails.Create(&options.App{
        Title:  "My App",
        Width:  1024,
        Height: 768,
        AssetServer: &options.AssetServer{
            Assets: assets,
        },
        Bind: []interface{}{
            &MyStruct{},
        },
    })
    app.Run()
}
```

### Solution 2: Bind Go methods to frontend

```go
type MyStruct struct{}
func (s *MyStruct) Greet(name string) string {
    return fmt.Sprintf("Hello %s!", name)
}
```

### Solution 3: Use runtime from frontend

```javascript
import {Greet} from '../wailsjs/go/main/MyStruct'
const result = await Greet('World')
```

### Solution 4: Configure build

```json
// wails.json
{
  "name": "myapp",
  "outputfilename": "myapp",
  "frontend:dir": "frontend",
  "frontend:install": "npm install",
  "frontend:build": "npm run build"
}
```

## Common Scenarios

- Wails application fails to start because of missing frontend build
- Go methods are not callable from JavaScript because they are not bound
- Wails build fails because of frontend build errors

## Prevent It

- Run wails dev for development
- Ensure all Go methods are added to the Bind array
- Test frontend build separately before running Wails
