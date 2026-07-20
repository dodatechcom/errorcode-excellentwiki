---
title: "[Solution] JavaFX FXMLLoader — FXML Load Error"
description: "Fix JavaFX FXMLLoader errors by checking FXML syntax, verifying controller, and ensuring fx:controller attribute is correct."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 32
---

# JavaFX FXMLLoader — FXML Load Error

Errors related to `FXMLLoader` occur when FXML files have invalid syntax, the controller class is misconfigured, or `fx:id` references do not match the controller's `@FXML` fields.

## Description

`FXMLLoader` parses FXML files and wires them to controller classes. Errors arise when the FXML references non-existent controller classes, `fx:id` attributes do not match `@FXML`-annotated fields, the FXML file is not on the classpath, or the controller violates the MVC contract.

Common message variants:

- `IOException: Cannot load FXML file`
- `NullPointerException: controller field not injected — fx:id mismatch`
- `ClassNotFoundException: controller class not found`
- `IllegalArgumentException: fx:id not found in controller`
- `InvalidException: FXML syntax error — mismatched tags`

## Common Causes

```java
// Cause 1: fx:id does not match controller field name
// FXML: <Button fx:id="submitBtn"/>
// Controller: @FXML private Button submitButton;  // Different name!
// Result: submitButton is null at runtime

// Cause 2: Controller class not found
// FXML: fx:controller="com.app.MyController"
// But MyController.class does not exist or wrong package

// Cause 3: FXML file not on classpath
FXMLLoader loader = new FXMLLoader();
loader.setLocation(getClass().getResource("/fxml/missing.fxml"));
Parent root = loader.load();  // IOException — resource not found

// Cause 4: Missing fx:id for programmatic access
// FXML: <Label text="Hello"/>  (no fx:id)
// Controller tries: @FXML private Label myLabel;  // Will be null

// Cause 5: Controller class is not public or has no default constructor
// private class MyController { }  // Cannot be instantiated by FXMLLoader
```

## Solutions

### Fix 1: Match fx:id exactly with controller field names

```java
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class MyController {
    @FXML private Button submitButton;   // fx:id="submitButton" in FXML
    @FXML private Label statusLabel;     // fx:id="statusLabel" in FXML
    @FXML private TextField nameField;   // fx:id="nameField" in FXML

    @FXML
    private void initialize() {
        // Fields are injected after FXMLLoader loads the FXML
        submitButton.setOnAction(e -> {
            String name = nameField.getText();
            statusLabel.setText("Hello, " + name);
        });
    }
}
```

### Fix 2: Load FXML with correct resource path

```java
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;

public class FXMLLoaderHelper {
    public static Parent loadFXML(String fxmlPath) throws java.io.IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(
            FXMLLoaderHelper.class.getResource(fxmlPath));

        if (loader.getLocation() == null) {
            throw new java.io.IOException(
                "FXML not found on classpath: " + fxmlPath);
        }

        return loader.load();
    }
}

// Usage
Parent root = FXMLLoaderHelper.loadFXML("/fxml/my_scene.fxml");
```

### Fix 3: Set controller explicitly if not in FXML

```java
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;

public class ManualControllerSetup {
    public static Parent loadWithController(
            String fxmlPath, Object controller) throws java.io.IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(
            ManualControllerSetup.class.getResource(fxmlPath));
        loader.setController(controller);  // Set controller programmatically
        return loader.load();
    }
}

// Usage
MyController controller = new MyController();
Parent root = loadWithController("/fxml/my_scene.fxml", controller);
```

### Fix 4: Validate fx:id at runtime

```java
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class ValidatedController {
    @FXML private Button actionButton;

    @FXML
    private void initialize() {
        if (actionButton == null) {
            throw new IllegalStateException(
                "fx:id='actionButton' not found in FXML — check fx:id spelling");
        }
    }
}
```

### Fix 5: Controller class must be public with default constructor

```java
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class ProperController {
    @FXML private Label messageLabel;

    public ProperController() {
        // Default constructor — required by FXMLLoader
    }

    @FXML
    private void initialize() {
        messageLabel.setText("Controller initialized");
    }
}

// WRONG — private class
// private class BadController { }  // Cannot be instantiated

// WRONG — no default constructor
// public class BadController {
//     public BadController(String arg) { }  // No no-arg constructor
// }
```

## Prevention Checklist

- Ensure every `fx:id` in FXML has a matching `@FXML` field in the controller.
- Use the same spelling and case for `fx:id` and field names.
- Place FXML files on the classpath (typically in `resources/fxml/`).
- Controller classes must be public, have a default constructor, and be in the correct package.
- Use `FXMLLoader.setLocation()` with the correct resource path.
- Validate that injected fields are not null in `initialize()`.

## Related Errors

- [NullPointerException](../nullpointerexception) — fx:id field not injected.
- [IOException](../ioexception) — FXML file not found.
- [ClassNotFoundException](../classnotfoundexception) — controller class missing.
- [InstantiationException](../instantiationexception) — controller has no default constructor.
