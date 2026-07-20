---
title: "[Solution] Java SwingUtilities.invokeLater — EDT Error"
description: "Fix SwingUtilities.invokeLater errors by avoiding EDT blocking, using proper synchronization, and running UI updates on the Event Dispatch Thread."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 24
---

# SwingUtilities.invokeLater — EDT Error

Errors related to `SwingUtilities.invokeLater()` and `invokeAndWait()` occur when the Event Dispatch Thread is blocked, when UI updates happen off the EDT, or when improper synchronization causes deadlocks.

## Description

All Swing UI operations must run on the Event Dispatch Thread (EDT). `SwingUtilities.invokeLater(Runnable)` schedules code on the EDT asynchronously, while `invokeAndWait(Runnable)` blocks until the EDT completes the task. Misuse leads to UI freezes, race conditions, `InterruptedException`, or `InvocationTargetException` when exceptions propagate from the runnable.

Common message variants:

- `java.lang.InterruptedException: EDT interrupted while waiting`
- `java.lang.reflect.InvocationTargetException: exception in EDT runnable`
- `IllegalStateException: Component not visible on EDT`
- `Deadlock: invokeAndWait called from the EDT itself`
- `NullPointerException: component not initialized before invokeLater`

## Common Causes

```java
// Cause 1: Calling invokeAndWait from the EDT — deadlock
SwingUtilities.invokeLater(() -> {
    SwingUtilities.invokeAndWait(() -> {
        // DEADLOCK — waiting for EDT from the EDT
    });
});

// Cause 2: Updating Swing components from background thread
new Thread(() -> {
    jLabel.setText("Updated");  // Not on EDT — undefined behavior
}).start();

// Cause 3: Blocking the EDT with long-running task
SwingUtilities.invokeLater(() -> {
    Thread.sleep(10000);  // FREEZES entire UI for 10 seconds
});

// Cause 4: NPE from component not yet initialized
JFrame frame = new JFrame();
SwingUtilities.invokeLater(() -> {
    frame.getContentPane().add(new JLabel("Hello"));
    // May NPE if frame not yet realized
});

// Cause 5: Exception in invokeLater not caught
SwingUtilities.invokeLater(() -> {
    int result = 10 / 0;  // ArithmeticException on EDT, unhandled
});
```

## Solutions

### Fix 1: Use invokeLater for non-blocking EDT updates

```java
import javax.swing.SwingUtilities;

public class SafeUIUpdater {
    public void updateLabel(javax.swing.JLabel label, String text) {
        SwingUtilities.invokeLater(() -> {
            label.setText(text);  // Runs on EDT — safe
        });
    }

    public void updateProgress(javax.swing.JProgressBar bar, int value) {
        SwingUtilities.invokeLater(() -> {
            bar.setValue(value);
        });
    }
}
```

### Fix 2: Use invokeAndWait when result is needed synchronously

```java
import javax.swing.*;
import java.lang.reflect.InvocationTargetException;

public class SynchronousUIUpdater {
    public String getLabelText(javax.swing.JLabel label) throws
            InterruptedException, InvocationTargetException {
        final String[] result = new String[1];

        SwingUtilities.invokeAndWait(() -> {
            result[0] = label.getText();
        });

        return result[0];
    }
}
```

### Fix 3: Never call invokeAndWait from the EDT

```java
import javax.swing.SwingUtilities;

public class EDTCheck {
    public void safeInvokeAndWait(Runnable task) throws
            InterruptedException, java.lang.reflect.InvocationTargetException {
        if (SwingUtilities.isEventDispatchThread()) {
            task.run();  // Already on EDT, run directly
        } else {
            SwingUtilities.invokeAndWait(task);
        }
    }
}
```

### Fix 4: Catch exceptions in invokeLater runnables

```java
import javax.swing.SwingUtilities;
import java.util.logging.Logger;

public class SafeEDTRunner {
    private static final Logger LOG = Logger.getLogger(SafeEDTRunner.class.getName());

    public void runOnEDT(Runnable task) {
        SwingUtilities.invokeLater(() -> {
            try {
                task.run();
            } catch (Exception e) {
                LOG.severe("Exception on EDT: " + e.getMessage());
                e.printStackTrace();
            }
        });
    }
}
```

### Fix 5: Use SwingWorker instead of blocking the EDT

```java
import javax.swing.*;

public class NonBlockingTask extends SwingWorker<String, Void> {
    private final JLabel statusLabel;

    public NonBlockingTask(JLabel statusLabel) {
        this.statusLabel = statusLabel;
    }

    @Override
    protected String doInBackground() throws Exception {
        // Long-running work on background thread
        Thread.sleep(5000);
        return "Result ready";
    }

    @Override
    protected void done() {
        try {
            statusLabel.setText(get());  // On EDT — safe
        } catch (Exception e) {
            statusLabel.setText("Error: " + e.getMessage());
        }
    }
}
```

## Prevention Checklist

- Always run Swing UI updates on the EDT via `invokeLater()` or `invokeAndWait()`.
- Never call `invokeAndWait()` from the EDT itself — check with `isEventDispatchThread()`.
- Do not perform long-running tasks inside `invokeLater()` runnables.
- Wrap the body of `invokeLater()` runnables in try-catch to handle exceptions.
- Use `SwingWorker` for background tasks that update the UI.
- Ensure components are fully initialized before scheduling EDT updates.

## Related Errors

- [IllegalStateException](../illegalstateexception) — component not in correct state on EDT.
- [InvocationTargetException](../invocationtargetexception) — exception thrown in EDT runnable.
- [InterruptedException](../interruptedexception) — invokeAndWait interrupted.
- [Deadlock](../stackoverflowerror) — circular EDT waits.
