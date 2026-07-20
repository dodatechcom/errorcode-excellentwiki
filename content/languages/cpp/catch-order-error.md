---
title: "[Solution] C++ Catch Block Order Error — Fix"
description: "Fix catch block order errors by placing derived type catches before base type catches, and handling exception hierarchies correctly."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 926
---

# C++ Catch Block Order Error — Fix

In C++, catch blocks are matched in order — the first matching handler is selected. If a base class catch appears before a derived class catch, the derived exception is caught by the base handler, and the derived-specific handler is never reached. This is a logic error that silently ignores derived exception handling.

## Common Causes

```cpp
// Cause 1: Base class catch before derived class catch
#include <stdexcept>
#include <iostream>

class NetworkError : public std::runtime_error {
    using std::runtime_error::runtime_error;
};

class TimeoutError : public NetworkError {
    using NetworkError::NetworkError;
};

int main() {
    try {
        throw TimeoutError("connection timed out");
    } catch (const std::runtime_error& e) {  // catches everything
        std::cout << "Runtime error: " << e.what() << std::endl;
    } catch (const NetworkError& e) {  // NEVER REACHED
        std::cout << "Network error: " << e.what() << std::endl;
    } catch (const TimeoutError& e) {  // NEVER REACHED
        std::cout << "Timeout: " << e.what() << std::endl;
    }
    return 0;
}
```

```cpp
// Cause 2: Catching std::exception before custom exceptions
#include <exception>
#include <iostream>

class ValidationError : public std::exception {
    std::string msg_;
public:
    ValidationError(std::string msg) : msg_(std::move(msg)) {}
    const char* what() const noexcept override { return msg_.c_str(); }
};

int main() {
    try {
        throw ValidationError("invalid input");
    } catch (const std::exception& e) {  // catches ValidationError too
        std::cout << "Error: " << e.what() << std::endl;
    } catch (const ValidationError& e) {  // NEVER REACHED
        std::cout << "Validation: " << e.what() << std::endl;
    }
    return 0;
}
```

```cpp
// Cause 3: Catch-all (...) before specific catches
int main() {
    try {
        throw std::runtime_error("error");
    } catch (...) {  // catches everything — specific handlers never reached
        std::cout << "Something went wrong" << std::endl;
    } catch (const std::runtime_error& e) {  // NEVER REACHED
        std::cout << e.what() << std::endl;
    }
    return 0;
}
```

```cpp
// Cause 4: Template catch ambiguity
#include <typeinfo>
#include <iostream>

int main() {
    try {
        throw 42;
    } catch (const int& e) {  // might catch before more specific handlers
        std::cout << "int: " << e << std::endl;
    } catch (...) {
        std::cout << "other" << std::endl;
    }
    return 0;
}
```

```cpp
// Cause 5: Exception hierarchy with multiple inheritance
#include <stdexcept>
#include <iostream>

class IOError : public std::runtime_error {
    using std::runtime_error::runtime_error;
};

class FormatError : public std::runtime_error {
    using std::runtime_error::runtime_error;
};

class FileFormatError : public IOError, public FormatError {
public:
    FileFormatError() : IOError("file format"), FormatError("file format") {}
    const char* what() const noexcept override { return "file format error"; }
};
```

## How to Fix

### Fix 1: Order Catches from Most Derived to Least Derived

```cpp
#include <stdexcept>
#include <iostream>

class NetworkError : public std::runtime_error {
    using std::runtime_error::runtime_error;
};

class TimeoutError : public NetworkError {
    using NetworkError::NetworkError;
};

int main() {
    try {
        throw TimeoutError("timed out");
    } catch (const TimeoutError& e) {       // most derived first
        std::cout << "Timeout: " << e.what() << std::endl;
    } catch (const NetworkError& e) {       // then base
        std::cout << "Network: " << e.what() << std::endl;
    } catch (const std::runtime_error& e) { // then more base
        std::cout << "Runtime: " << e.what() << std::endl;
    } catch (const std::exception& e) {     // then std::exception
        std::cout << "Exception: " << e.what() << std::endl;
    }
    return 0;
}
```

### Fix 2: Handle Custom Exceptions Before std::exception

```cpp
#include <stdexcept>
#include <iostream>

class ValidationError : public std::exception {
    std::string msg_;
public:
    ValidationError(std::string msg) : msg_(std::move(msg)) {}
    const char* what() const noexcept override { return msg_.c_str(); }
};

class DatabaseError : public std::exception {
    std::string msg_;
public:
    DatabaseError(std::string msg) : msg_(std::move(msg)) {}
    const char* what() const noexcept override { return msg_.c_str(); }
};

int main() {
    try {
        throw ValidationError("bad input");
    } catch (const ValidationError& e) {    // custom first
        std::cout << "Validation: " << e.what() << std::endl;
    } catch (const DatabaseError& e) {      // custom first
        std::cout << "Database: " << e.what() << std::endl;
    } catch (const std::exception& e) {     // std::exception last
        std::cout << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

### Fix 3: Put catch(...) Last

```cpp
#include <exception>
#include <iostream>

int main() {
    try {
        throw std::runtime_error("error");
    } catch (const std::exception& e) {  // specific first
        std::cout << e.what() << std::endl;
    } catch (...) {                       // catch-all last
        std::cout << "Unknown error" << std::endl;
    }
    return 0;
}
```

### Fix 4: Use Function Try Block for Constructors

```cpp
#include <stdexcept>
#include <string>

class SafeResource {
    int* data_;
public:
    // Function try block — catches exceptions from member init
    SafeResource(int size)
    try : data_(new int[size]) {
        // constructor body
    } catch (const std::bad_alloc&) {
        throw std::runtime_error("failed to allocate resource");
    } catch (...) {
        throw;  // re-throw unknown exceptions
    }

    ~SafeResource() { delete[] data_; }
};
```

### Fix 5: Separate Exception Hierarchy Handling

```cpp
#include <stdexcept>
#include <iostream>
#include <string>

class AppException : public std::runtime_error {
    using std::runtime_error::runtime_error;
};

class NetworkException : public AppException {
    using AppException::AppException;
};

class ConfigException : public AppException {
    using AppException::AppException;
};

void handle_exception(const std::exception& e) {
    // Use dynamic type for proper dispatch
    try {
        throw e;
    } catch (const NetworkException& e) {
        std::cerr << "Network: " << e.what() << std::endl;
    } catch (const ConfigException& e) {
        std::cerr << "Config: " << e.what() << std::endl;
    } catch (const AppException& e) {
        std::cerr << "App: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}
```

## Examples

```cpp
// Real-world: proper exception hierarchy handling
#include <stdexcept>
#include <iostream>
#include <string>
#include <vector>

// Exception hierarchy
class BaseError : public std::runtime_error {
    using std::runtime_error::runtime_error;
};

class ConnectionError : public BaseError {
    using BaseError::BaseError;
};

class TimeoutError : public ConnectionError {
    using ConnectionError::ConnectionError;
};

class AuthError : public BaseError {
    int code_;
public:
    AuthError(std::string msg, int code)
        : BaseError(std::move(msg)), code_(code) {}
    int code() const { return code_; }
};

// Properly ordered catch blocks
void execute_operation() {
    try {
        // ... operation that may throw ...
        throw TimeoutError("connection timeout after 30s");
    } catch (const TimeoutError& e) {          // most derived
        std::cerr << "Timeout: " << e.what() << std::endl;
    } catch (const ConnectionError& e) {       // derived before base
        std::cerr << "Connection: " << e.what() << std::endl;
    } catch (const AuthError& e) {             // specific derived
        std::cerr << "Auth [" << e.code() << "]: " << e.what() << std::endl;
    } catch (const BaseError& e) {             // base last
        std::cerr << "Error: " << e.what() << std::endl;
    } catch (const std::exception& e) {        // std::exception last
        std::cerr << "Unexpected: " << e.what() << std::endl;
    }
}
```

## Related Errors

- [noexcept violation]({{< relref "/languages/cpp/noexcept-violation" >}}) — exception from noexcept function.
- [Exception in destructor]({{< relref "/languages/cpp/exception-destructor" >}}) — exceptions during cleanup.
- [Exception safety guarantees]({{< relref "/languages/cpp/exception-safety-guarantees" >}}) — guarantee violations.
