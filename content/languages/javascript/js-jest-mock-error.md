---
title: "Solved JavaScript jest.mock Error — How to Fix"
date: 2026-03-20T16:50:10+00:00
description: "Learn how to resolve JavaScript Jest module mocking and jest.mock configuration errors."
categories: ["javascript"]
keywords: ["jest.mock error", "jest mock", "module mock", "jest testing", "mock module"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

jest.mock errors occur when module mocks are misconfigured, mock factories return incorrect shapes, or hoisting causes unexpected behavior. Jest mocks must match the original module structure.

Common causes include:
- Mock factory function doesn't match exports
- Mock not hoisted correctly
- Partial mock missing required exports
- Mock implementation throwing errors
- Module path incorrect

## Common Error Messages

```
Error: Cannot find module './api'
```

```
TypeError: api.getUser is not a function
```

```
Warning: Using fake timers with real timers
```

## How to Fix It

### 1. Mock Entire Modules

Mock complete modules.

```javascript
// api.js
export const getUser = async (id) => {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
};

export const createUser = async (data) => {
  const response = await fetch("/api/users", {
    method: "POST",
    body: JSON.stringify(data)
  });
  return response.json();
};

// api.test.js
import * as api from "./api";

// Mock entire module
jest.mock("./api");

// Mock before import
const mockedApi = api;

describe("API Tests", () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });
  
  test("getUser returns data", async () => {
    mockedApi.getUser.mockResolvedValue({ id: 1, name: "John" });
    
    const user = await api.getUser(1);
    
    expect(user).toEqual({ id: 1, name: "John" });
    expect(mockedApi.getUser).toHaveBeenCalledWith(1);
  });
});
```

### 2. Partial Mocking

Mock specific functions.

```javascript
import * as api from "./api";

// Partial mock - keep other implementations
jest.mock("./api", () => ({
  ...jest.requireActual("./api"),
  getUser: jest.fn()
}));

test("getUser is mocked", async () => {
  api.getUser.mockResolvedValue({ id: 1 });
  
  const user = await api.getUser(1);
  expect(user).toEqual({ id: 1 });
});

test("createUser uses real implementation", async () => {
  // createUser is not mocked
  global.fetch = jest.fn().mockResolvedValue({
    ok: true,
    json: () => Promise.resolve({ id: 1 })
  });
  
  const user = await api.createUser({ name: "Test" });
  expect(user).toEqual({ id: 1 });
});
```

### 3. Mock with Factory Functions

Use factory functions for complex mocks.

```javascript
// database.js
export class Database {
  constructor(config) {
    this.config = config;
  }
  
  async connect() {
    // Connection logic
  }
  
  async query(sql, params) {
    // Query logic
  }
  
  async disconnect() {
    // Disconnect logic
  }
}

// database.test.js
jest.mock("./database", () => {
  return {
    Database: jest.fn().mockImplementation(() => ({
      connect: jest.fn().mockResolvedValue(true),
      query: jest.fn().mockResolvedValue([{ id: 1 }]),
      disconnect: jest.fn().mockResolvedValue(true)
    }))
  };
});

import { Database } from "./database";

test("Database methods work", async () => {
  const db = new Database({});
  
  await db.connect();
  const result = await db.query("SELECT * FROM users");
  
  expect(result).toEqual([{ id: 1 }]);
  expect(db.query).toHaveBeenCalledWith("SELECT * FROM users");
});
```

## Common Scenarios

### Scenario 1: Mock Async Modules

Mock async imports:

```javascript
// Lazy import
const getApi = async () => {
  const api = await import("./api");
  return api;
};

// Mock dynamic import
jest.mock("./api", () => ({
  getData: jest.fn()
}));

test("lazy loaded API is mocked", async () => {
  const api = await getApi();
  api.getData.mockResolvedValue("mocked data");
  
  const result = await api.getData();
  expect(result).toBe("mocked data");
});
```

### Scenario 2: Mock Third-Party Libraries

Mock external dependencies:

```javascript
// Mock axios
jest.mock("axios");
import axios from "axios";

test("axios request is mocked", async () => {
  axios.get.mockResolvedValue({ data: { id: 1 } });
  
  const response = await axios.get("/api/user/1");
  
  expect(response.data).toEqual({ id: 1 });
  expect(axios.get).toHaveBeenCalledWith("/api/user/1");
});

// Mock with implementation
jest.mock("axios", () => ({
  get: jest.fn().mockImplementation((url) => {
    if (url.includes("/users")) {
      return Promise.resolve({ data: [{ id: 1 }] });
    }
    return Promise.resolve({ data: {} });
  })
}));
```

## Prevent It

- Use `jest.mock()` before imports for proper hoisting
- Match mock shape to original module exports
- Use `jest.requireActual()` for partial mocks
- Clear mocks in `beforeEach` to avoid test pollution
- Use `mockImplementation()` for complex return values