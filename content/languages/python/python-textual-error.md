---
title: "[Solution] Python Textual TUI Error — How to Fix"
description: "Fix Python Textual TUI errors. Resolve widget mounting failures, CSS issues, and async event handling problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Textual TUI Error

A `textual.errors.MountError` or `textual.css.parse.CssError` occurs when Textual fails to mount widgets, encounters invalid CSS syntax, or when async event handlers conflict with the application's event loop.

## Why It Happens

Textual is a TUI framework built on Rich. Errors arise when widgets are mounted in invalid containers, CSS selectors reference non-existent widget IDs, async handlers are not properly decorated, or the event loop receives conflicting operations.

## Common Error Messages

- `MountError: Widget 'Button' has already been mounted`
- `CssError: Unknown pseudo-class ':invalid'`
- `NoWidget: No widget matches selector '#nonexistent'`
- `asyncio ERROR: Task was destroyed but it is pending`

## How to Fix It

### Fix 1: Fix widget mounting

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MyApp(App):
    CSS = """
    Screen { layout: vertical; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello World", id="greeting")
        yield Footer()

    def on_mount(self) -> None:
        # Wrong — mounting same widget twice
        # self.mount(Static("Duplicate"))

        # Correct — check before mounting
        if not self.query_one("#status", default=None):
            self.mount(Static("Status: OK", id="status"))

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### Fix 2: Fix CSS syntax

```python
from textual.app import App, ComposeResult
from textual.widgets import Static, Button

class MyApp(App):
    # Wrong — invalid CSS pseudo-class
    # CSS = "Static:invalid { color: red; }"

    # Correct — use valid Textual CSS
    CSS = """
    Screen { background: $surface; }
    Static { width: 100%; height: auto; }
    #title { text-style: bold; color: $text; }
    Button { margin: 1; }
    Button:hover { background: $primary; }
    """

    def compose(self) -> ComposeResult:
        yield Static("Title", id="title")
        yield Button("Click Me", id="action")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one("#title").update("Button clicked!")

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### Fix 3: Handle async event handlers correctly

```python
from textual.app import App, ComposeResult
from textual.widgets import Static, Input
import asyncio

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Type here...")
        yield Static("Waiting...", id="output")

    # Wrong — async handler without proper handling
    # async def on_input_changed(self, event):
    #     await asyncio.sleep(1)  # blocks event loop

    # Correct — use proper async patterns
    async def on_input_changed(self, event: Input.Changed) -> None:
        output = self.query_one("#output")
        output.update(f"You typed: {event.value}")

    # Use worker for background tasks
    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.run_worker(self.process_input, event.value)

    async def process_input(self, value: str) -> None:
        output = self.query_one("#output")
        output.update(f"Processing: {value}")
        await asyncio.sleep(0.1)
        output.update(f"Done: {value}")

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### Fix 4: Manage widget state correctly

```python
from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.reactive import reactive

class Counter(App):
    count = reactive(0)

    CSS = """
    #count { text-align: center; text-style: bold; width: 100%; }
    """

    def compose(self) -> ComposeResult:
        yield Static("0", id="count")
        yield Button("Increment", id="inc")
        yield Button("Decrement", id="dec")

    def watch_count(self, new_value: int) -> None:
        self.query_one("#count").update(str(new_value))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "inc":
            self.count += 1
        elif event.button.id == "dec":
            self.count -= 1

if __name__ == "__main__":
    app = Counter()
    app.run()
```

## Common Scenarios

- **Double mounting** — Mounting the same widget instance twice causes MountError.
- **Invalid CSS selector** — Using CSS pseudo-classes not supported by Textual raises CssError.
- **Blocking async handlers** — Long-running async handlers block the event loop and freeze the UI.

## Prevent It

- Always use `yield` in `compose()` instead of calling `mount()` for initial widget creation.
- Reference only IDs and classes defined in your CSS in selectors.
- Use `self.run_worker()` for background tasks instead of `await` in event handlers.

## Related Errors

- [CssError](/languages/python/css-error/) — invalid CSS syntax
- [MountError](/languages/python/mount-error/) — widget already mounted
- [asyncio error](/languages/python/asyncio-error/) — event loop conflict
