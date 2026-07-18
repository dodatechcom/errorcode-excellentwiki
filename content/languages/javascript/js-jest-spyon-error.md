---
title: "Solved JavaScript jest.spyOn Error — How to Fix"
date: 2026-03-20T15:10:20+00:00
description: "Learn how to resolve JavaScript Jest spyOn mock function and spy configuration errors."
categories: ["javascript"]
keywords: ["jest.spyon error", "jest mock", "spy on function", "jest testing", "mock function"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

jest.spyOn errors occur when attempting to spy on non-configurable properties, methods that don't exist, or when the spy isn't properly restored. Jest requires properties to be writable and configurable.

Common causes include:
- Spying on non-configurable or non-writable properties
- Method doesn't exist on the object
- Spy not restored between tests
- Mock implementation not returning expected values
- Spying on ES6 class methods incorrectly

## Common Error Messages

```
TypeError: Cannot spy on object property because it is not configurable
```

```
ReferenceError: Cannot redefine property: methodName
```

```
TypeError: spyOn requires an object
```

## How to Fix It

### 1. Spy on Object Methods

Use spyOn correctly on objects.

```javascript
// Basic spyOn usage
const obj = {
  getValue: () => 42,
  calculate: (x, y) => x + y
};

// Spy and mock implementation
jest.spyOn(obj, "getValue").mockReturnValue(100);

expect(obj.getValue()).toBe(100);
expect(obj.getValue).toHaveBeenCalledTimes(1);

// Spy with mock implementation
jest.spyOn(obj, "calculate").mockImplementation((x, y) => x * y);

expect(obj.calculate(2, 3)).toBe(6);

// Spy and call original implementation
jest.spyOn(obj, "getValue").mockImplementation(() => {
  // Custom logic
  return 999;
});

// Restore original
afterEach(() => {
  jest.restoreAllMocks();
});
```

### 2. Spy on Module Functions

Mock entire modules or specific exports.

```javascript
// utils.js
export const fetchData = async (url) => {
  const response = await fetch(url);
  return response.json();
};

export const processData = (data) => {
  return data.map(item => item.toUpperCase());
};

// utils.test.js
import * as utils from "./utils";

// Spy on specific export
jest.spyOn(utils, "fetchData").mockResolvedValue({ id: 1 });

// Or mock entire module
jest.mock("./utils", () => ({
  fetchData: jest.fn().mockResolvedValue({ id: 1 }),
  processData: jest.fn().mockReturnValue(["PROCESSED"])
}));

test("uses mocked fetchData", async () => {
  const result = await utils.fetchData("/api/data");
  expect(result).toEqual({ id: 1 });
});
```

### 3. Spy on Class Methods

Handle class method spying.

```javascript
class UserService {
  constructor(db) {
    this.db = db;
  }
  
  async getUser(id) {
    return this.db.find(id);
  }
  
  async saveUser(user) {
    return this.db.save(user);
  }
}

// Test with spyOn
test("getUser calls db.find", async () => {
  const mockDb = { find: jest.fn(), save: jest.fn() };
  const service = new UserService(mockDb);
  
  jest.spyOn(mockDb, "find").mockResolvedValue({ id: 1, name: "Test" });
  
  const user = await service.getUser(1);
  
  expect(mockDb.find).toHaveBeenCalledWith(1);
  expect(user).toEqual({ id: 1, name: "Test" });
});

// Spy on prototype method
jest.spyOn(UserService.prototype, "getUser");

const service = new UserService(mockDb);
await service.getUser(1);

expect(UserService.prototype.getUser).toHaveBeenCalled();
```

## Common Scenarios

### Scenario 1: Mock Time-dependent Code

Use fake timers with spies:

```javascript
test("debounce works correctly", () => {
  jest.useFakeTimers();
  
  const callback = jest.fn();
  const debouncedFn = debounce(callback, 300);
  
  debouncedFn();
  debouncedFn();
  debouncedFn();
  
  expect(callback).not.toHaveBeenCalled();
  
  jest.advanceTimersByTime(300);
  
  expect(callback).toHaveBeenCalledTimes(1);
  
  jest.useRealTimers();
});
```

### Scenario 2: Mock Fetch API

Mock global fetch with spies:

```javascript
// Mock fetch globally
global.fetch = jest.fn();

// Spy on fetch
jest.spyOn(global, "fetch").mockResolvedValue({
  ok: true,
  json: async () => ({ data: "test" })
});

test("fetches data", async () => {
  const result = await fetchData("https://api.example.com");
  
  expect(global.fetch).toHaveBeenCalledWith("https://api.example.com");
  expect(result).toEqual({ data: "test" });
});

afterEach(() => {
  jest.restoreAllMocks();
});
```

## Prevent It

- Always call `jest.restoreAllMocks()` in `afterEach` to prevent test pollution
- Use `jest.fn()` for standalone mocks and `jest.spyOn()` for existing methods
- Check if property is configurable before spying
- Use `mockReturnValue()` or `mockResolvedValue()` for simple returns
- Prefer `mockImplementation()` for complex mock logic