---
title: "[Solution] Java SwingWorker — Execution Error"
description: "Fix Java SwingWorker errors by running on the EDT correctly, handling exceptions in doInBackground, and using publish/process properly."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 22
---

# SwingWorker — Execution Error

Errors in `SwingWorker` occur when background tasks are not executed correctly, exceptions in `doInBackground` are unhandled, or EDT updates violate Swing's single-thread rule.

## Description

`SwingWorker<T, V>` is designed for long-running tasks that need to update Swing UI components. It runs background logic in `doInBackground()` on a worker thread and publishes intermediate results via `publish/process` to the EDT. Errors occur when Swing components are updated from worker threads, when exceptions go unhandled, or when `publish/process` is misused.

Common message variants:

- `IllegalStateException: This function should be called from the EDT`
- `java.util.concurrent.ExecutionException: Exception in doInBackground()`
- `NullPointerException in process(List<V>) — published values are null`
- `CancellationException: task was cancelled before completion`
- `RejectedExecutionException: executor shut down`

## Common Causes

```java
// Cause 1: Updating Swing components from doInBackground
new SwingWorker<Void, Void>() {
    @Override
    protected Void doInBackground() {
        jLabel.setText("Updated");  // WRONG — not on EDT
        return null;
    }
}.execute();

// Cause 2: Unhandled exception in doInBackground
new SwingWorker<String, Void>() {
    @Override
    protected String doInBackground() {
        throw new RuntimeException("Task failed");  // ExecutionException
    }
}.execute();

// Cause 3: NPE in process() when no values published
new SwingWorker<Void, Integer>() {
    @Override
    protected Void doInBackground() {
        // No publish() calls
        return null;
    }

    @Override
    protected void process(List<Integer> chunks) {
        progressBar.setValue(chunks.get(chunks.size() - 1));
        // NullPointerException if chunks is empty
    }
}.execute();

// Cause 4: Accessing SwingWorker after completion
SwingWorker<String, Void> worker = new SwingWorker<>() {
    @Override
    protected String doInBackground() {
        return "done";
    }
};
worker.execute();
worker.get();  // Blocks calling thread — deadlock if on EDT
```

## Solutions

### Fix 1: Update UI only in done() or process()

```java
import javax.swing.*;

public class SafeSwingWorker extends SwingWorker<String, Integer> {
    private final JProgressBar progressBar;
    private final JLabel resultLabel;

    public SafeSwingWorker(JProgressBar bar, JLabel label) {
        this.progressBar = bar;
        this.resultLabel = label;
    }

    @Override
    protected String doInBackground() throws Exception {
        for (int i = 0; i <= 100; i += 10) {
            Thread.sleep(200);
            publish(i);  // Safe — goes to process() on EDT
        }
        return "Complete";
    }

    @Override
    protected void process(java.util.List<Integer> chunks) {
        int latest = chunks.get(chunks.size() - 1);
        progressBar.setValue(latest);  // On EDT — safe
    }

    @Override
    protected void done() {
        try {
            resultLabel.setText(get());  // On EDT — safe
        } catch (Exception e) {
            resultLabel.setText("Error: " + e.getMessage());
        }
    }
}
```

### Fix 2: Handle exceptions in doInBackground

```java
import javax.swing.*;
import java.util.concurrent.ExecutionException;

public class RobustWorker extends SwingWorker<String, Void> {
    @Override
    protected String doInBackground() throws Exception {
        try {
            return fetchDataFromServer();
        } catch (Exception e) {
            throw new Exception("Data fetch failed: " + e.getMessage(), e);
        }
    }

    @Override
    protected void done() {
        try {
            String result = get();
            JOptionPane.showMessageDialog(null, "Data: " + result);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            JOptionPane.showMessageDialog(null, "Task interrupted");
        } catch (ExecutionException e) {
            Throwable cause = e.getCause();
            JOptionPane.showMessageDialog(null,
                "Error: " + cause.getMessage());
        }
    }
}
```

### Fix 3: Use publish/process for progress updates safely

```java
import javax.swing.*;
import java.util.List;

public class ProgressWorker extends SwingWorker<Void, Integer> {
    private final JProgressBar progressBar;

    public ProgressWorker(JProgressBar bar) {
        this.progressBar = bar;
    }

    @Override
    protected Void doInBackground() throws Exception {
        String[] files = getFilesToProcess();
        for (int i = 0; i < files.length; i++) {
            processFile(files[i]);
            int progress = (int) ((i + 1.0) / files.length * 100);
            publish(progress);
        }
        return null;
    }

    @Override
    protected void process(List<Integer> chunks) {
        if (chunks != null && !chunks.isEmpty()) {
            int latest = chunks.get(chunks.size() - 1);
            progressBar.setValue(latest);
        }
    }
}
```

### Fix 4: Do not call get() on the EDT

```java
import javax.swing.*;
import java.util.concurrent.ExecutionException;

public class NonBlockingWorker extends SwingWorker<String, Void> {
    @Override
    protected String doInBackground() throws Exception {
        return fetchData();
    }

    @Override
    protected void done() {
        try {
            String result = get();  // Safe in done() — called on EDT
            updateUI(result);
        } catch (ExecutionException | InterruptedException e) {
            handleError(e);
        }
    }
}

// WRONG — calling get() on EDT blocks the UI
// SwingUtilities.invokeLater(() -> {
//     String result = worker.get();  // DEADLOCK
// });
```

### Fix 5: Cancel workers properly

```java
import javax.swing.*;

public class CancellableWorker extends SwingWorker<String, Void> {
    @Override
    protected String doInBackground() throws Exception {
        for (int i = 0; i < 1000; i++) {
            if (isCancelled()) {
                throw new InterruptedException("Task cancelled");
            }
            processChunk(i);
            Thread.sleep(10);
        }
        return "Done";
    }

    // Cancel on button press
    public void onCancel JButton button, CancellableWorker worker) {
        button.addActionListener(e -> {
            if (!worker.isDone()) {
                worker.cancel(true);
            }
        });
    }
}
```

## Prevention Checklist

- Only update Swing components in `process()` and `done()`, never in `doInBackground()`.
- Always call `get()` inside `done()`, not from event dispatch code.
- Handle `ExecutionException` and `InterruptedException` in `done()`.
- Check `isCancelled()` periodically in long `doInBackground` loops.
- Validate that `chunks` is non-empty in `process()` before accessing elements.
- Use `cancel(true)` to request interruption of worker threads.

## Related Errors

- [IllegalStateException](../illegalstateexception) — Swing component access off the EDT.
- [ExecutionException](../executionexception) — exception thrown inside doInBackground.
- [InterruptedException](../interruptedexception) — worker thread interrupted.
- [CancellationException](../cancellationexception) — task cancelled before get().
