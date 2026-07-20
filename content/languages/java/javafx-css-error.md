---
title: "[Solution] JavaFX CSS — Parsing Error"
description: "Fix JavaFX CSS parsing errors by checking CSS syntax, verifying selectors, and using correct JavaFX CSS property names."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 33
---

# JavaFX CSS — Parsing Error

Errors related to JavaFX CSS occur when stylesheets have invalid syntax, use incorrect property names, or reference selectors that do not match any node in the scene graph.

## Description

JavaFX uses a CSS-like styling system similar to web CSS but with different property names and syntax. Errors arise from using web CSS properties instead of JavaFX equivalents, invalid selector syntax, unclosed braces, or referencing non-existent pseudo-classes.

Common message variants:

- `CSSException: Unknown property: background-color`
- `ParseException: Invalid selector syntax`
- `Pseudo-class not found: -fx-hover`
- `CSS parse error at line N: unexpected token`
- `NullPointerException: stylesheet not loaded`

## Common Causes

```java
// Cause 1: Using web CSS properties instead of JavaFX
// WRONG: .button { background-color: red; }
// CORRECT: .button { -fx-background-color: red; }

// Cause 2: Invalid selector syntax
// WRONG: .button:hover > .label { }
// CORRECT: .button:hover .label { }

// Cause 3: Unclosed braces in CSS
// .root {
//     -fx-background-color: white;
//     -fx-font-size: 14px;
//     // Missing closing brace — parse error

// Cause 4: Missing -fx- prefix on properties
// { color: red; }  // Should be -fx-text-fill: red;

// Cause 5: Referencing non-existent pseudo-class
// .button:active { }  // Not supported — use .button:pressed { }
```

## Solutions

### Fix 1: Use correct JavaFX CSS property names

```java
import javafx.scene.control.Button;
import javafx.scene.Scene;

public class CorrectCSS {
    // Use -fx- prefixed properties
    String css = """
        .root {
            -fx-background-color: #f0f0f0;
            -fx-font-size: 14px;
        }
        .button {
            -fx-background-color: #4CAF50;
            -fx-text-fill: white;
            -fx-font-size: 16px;
            -fx-padding: 10 20;
            -fx-background-radius: 5;
        }
        .label {
            -fx-text-fill: #333333;
            -fx-font-weight: bold;
        }
    """;

    public void applyStyles(Scene scene) {
        scene.getRoot().setStyle(css);
    }
}
```

### Fix 2: Load external stylesheet correctly

```java
import javafx.scene.Scene;
import javafx.scene.Parent;

public class StylesheetLoader {
    public static void loadStylesheet(Scene scene) {
        String css = scene.getClass().getResource("/css/styles.css").toExternalForm();

        if (css == null) {
            System.err.println("Stylesheet not found: /css/styles.css");
            return;
        }

        scene.getStylesheets().add(css);
    }
}
```

### Fix 3: Use inline styles for quick fixes

```java
import javafx.scene.control.Label;

public class InlineStyling {
    public static void styleLabel(Label label) {
        label.setStyle(
            "-fx-text-fill: blue;" +
            "-fx-font-size: 20px;" +
            "-fx-font-weight: bold;" +
            "-fx-background-color: yellow;" +
            "-fx-padding: 10px;"
        );
    }
}
```

### Fix 4: Validate CSS properties with known JavaFX properties

```java
import java.util.Set;

public class JavaFXCSSValidator {
    private static final Set<String> COMMON_PROPERTIES = Set.of(
        "-fx-background-color",
        "-fx-text-fill",
        "-fx-font-size",
        "-fx-font-weight",
        "-fx-padding",
        "-fx-background-radius",
        "-fx-border-color",
        "-fx-border-width",
        "-fx-alignment",
        "-fx-opacity",
        "-fx-cursor",
        "-fx-effect",
        "-fx-background-image"
    );

    public static boolean isValidProperty(String property) {
        return COMMON_PROPERTIES.contains(property.trim());
    }
}
```

### Fix 5: Use correct pseudo-classes

```java
// JavaFX valid pseudo-classes:
// :hover        — mouse over
// :pressed      — mouse pressed
// :focused      — has focus
// :disabled     — disabled
// :checked      — CheckBox selected
// :selected     — TableView row selected

// CSS example:
// .button:hover {
//     -fx-background-color: lightblue;
// }
//
// .button:pressed {
//     -fx-background-color: darkblue;
// }
//
// .button:focused {
//     -fx-background-color: lightgreen;
// }

// WRONG — web-only pseudo-classes:
// :active  → use :pressed
// :first-child → not supported in JavaFX
// :nth-child → not supported in JavaFX
```

## Prevention Checklist

- Always prefix JavaFX CSS properties with `-fx-`.
- Use `-fx-text-fill` instead of `color` for text color.
- Use `-fx-background-color` instead of `background-color`.
- Use `-fx-padding` instead of `padding`.
- Verify pseudo-classes are JavaFX-compatible (`:hover`, `:pressed`, `:focused`, `:disabled`).
- Load stylesheets with `scene.getStylesheets().add()`.
- Validate CSS syntax before loading to catch parse errors early.

## Related Errors

- [NullPointerException](../nullpointerexception) — stylesheet URL is null.
- [IOException](../ioexception) — CSS file not found on classpath.
- [IllegalArgumentException](../illegalargumentexception) — invalid CSS property value.
