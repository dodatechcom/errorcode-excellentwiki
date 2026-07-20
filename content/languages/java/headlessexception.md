---
title: "[Solution] Java HeadlessException — Display Required but Unavailable"
description: "Fix Java HeadlessException by setting java.awt.headless=true, using headless-compatible APIs, or avoiding GUI components in headless environments."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# HeadlessException — Display Required but Unavailable

A `HeadlessException` is thrown when code that requires a display, keyboard, or mouse is invoked in an environment that does not support them (headless mode). This commonly occurs in server-side Java applications, containers, or CI/CD pipelines where no graphical display is available.

## Description

Java AWT/Swing components normally require a graphical display environment. When running in headless mode (e.g., a Docker container, remote server, or system without X11), attempting to create or manipulate GUI components throws `HeadlessException`.

Common message variants:

- `java.awt.HeadlessException`
- `java.awt.HeadlessException: No X11 DISPLAY variable was set`
- `java.awt.HeadlessException: Can't connect to X11 display`
- `java.awt.HeadlessException: no platform monitor found`

## Common Causes

```java
// Cause 1: Creating a Frame in headless mode
Frame frame = new Frame("My App");  // HeadlessException

// Cause 2: Opening a FileDialog in headless mode
FileDialog fd = new FileDialog(frame, "Open");  // HeadlessException

// Cause 3: Getting screen dimensions in headless mode
Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();  // HeadlessException

// Cause 4: Printing via AWT in headless mode
PrinterJob job = PrinterJob.getPrinterJob();
job.printDialog();  // HeadlessException

// Cause 5: Creating Robot in headless mode
Robot robot = new Robot();  // HeadlessException
```

## Solutions

### Fix 1: Set the `java.awt.headless` property

```java
// Set before any AWT/Swing calls
System.setProperty("java.awt.headless", "true");

// Or pass as JVM argument
// java -Djava.awt.headless=true -jar myapp.jar
```

### Fix 2: Use headless-compatible APIs

```java
// Instead of Toolkit.getDefaultToolkit().getScreenSize(), use:
GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
Rectangle bounds = ge.getDefaultScreenDevice().getDefaultConfiguration().getBounds();

// For image generation, use BufferedImage directly
BufferedImage image = new BufferedImage(800, 600, BufferedImage.TYPE_INT_ARGB);
Graphics2D g2d = image.createGraphics();
g2d.drawString("Hello", 10, 50);
g2d.dispose();
```

### Fix 3: Conditionally create GUI components

```java
import java.awt.*;

public class SafeGUI {
    public static void main(String[] args) {
        if (GraphicsEnvironment.isHeadless()) {
            System.out.println("Running in headless mode — GUI unavailable");
            return;
        }

        // Safe to create GUI components
        Frame frame = new Frame("My App");
        frame.setSize(400, 300);
        frame.setVisible(true);
    }
}
```

### Fix 4: Use headless mode for server-side image processing

```java
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;

public class HeadlessImageProcessor {
    public static void main(String[] args) throws Exception {
        System.setProperty("java.awt.headless", "true");

        BufferedImage image = new BufferedImage(200, 200, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = image.createGraphics();
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, 200, 200);
        g.setColor(Color.BLACK);
        g.drawString("Generated in headless mode", 10, 100);
        g.dispose();

        ImageIO.write(image, "png", new File("output.png"));
    }
}
```

### Fix 5: Install X11 virtual framebuffer for display-dependent code

```bash
# Install Xvfb
sudo apt-get install xvfb

# Run with virtual display
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99
java -jar myapp.jar
```

## Prevention Checklist

- Set `java.awt.headless=true` for server-side or containerized applications.
- Use `GraphicsEnvironment.isHeadless()` before creating GUI components.
- Prefer headless-compatible APIs (`BufferedImage`, `Graphics2D`) over `Frame`, `Dialog`, etc.
- Use Xvfb for testing GUI-dependent code in headless environments.
- Document headless requirements in deployment documentation.

## Related Errors

- [AWTException](../awtexception) — generic AWT error signaling configuration problems.
- [UnsupportedOperationException](../unsupportedoperationexception) — operation not supported in current context.
- [NullPointerException](../nullpointerexception) — NPE when GraphicsEnvironment returns null.
