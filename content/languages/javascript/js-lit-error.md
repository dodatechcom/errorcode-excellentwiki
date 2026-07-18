---
title: "[Solution] JavaScript Lit Web Component Error — How to Fix"
description: "Fix JavaScript Lit web component errors. Resolve rendering, property, and shadow DOM issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript Lit Web Component Error

A `LitElement` or `TypeError` occurs when Lit fails to render components, encounters property reflection issues, or when shadow DOM is not properly configured.

## Why It Happens

Lit is a web components library. Errors arise when properties are not declared, when rendering produces invalid HTML, when shadow DOM styles leak, or when the element is not registered.

## Common Error Messages

- `TypeError: Cannot read property of undefined`
- `LitElement: Properties must be declared`
- `Error: Element not registered`
- `TypeError: render is not a function`

## How to Fix It

### Fix 1: Declare properties correctly

```javascript
import { LitElement, html, css } from 'lit';
import { customElement, property } from 'lit/decorators.js';

// Wrong — no property declaration
// class MyElement extends LitElement {
//   render() { return html`<div>${this.name}</div>`; }
// }

// Correct — declare properties
@customElement('my-element')
class MyElement extends LitElement {
  @property({ type: String })
  name = 'World';

  @property({ type: Number, reflect: true })
  count = 0;

  render() {
    return html`
      <div>Hello ${this.name}!</div>
      <button @click=${this._increment}>Count: ${this.count}</button>
    `;
  }

  _increment() {
    this.count++;
  }
}
```

### Fix 2: Handle shadow DOM styles

```javascript
import { LitElement, html, css } from 'lit';

class StyledElement extends LitElement {
  static styles = css`
    :host {
      display: block;
      padding: 16px;
    }
    .container {
      border: 1px solid #ccc;
    }
  `;

  render() {
    return html`
      <div class="container">
        <slot></slot>
      </div>
    `;
  }
}

customElements.define('styled-element', StyledElement);
```

### Fix 3: Use lifecycle correctly

```javascript
import { LitElement, html } from 'lit';

class LifecycleElement extends LitElement {
  connectedCallback() {
    super.connectedCallback();
    console.log('Element connected');
  }

  disconnectedCallback() {
    super.disconnectedCallback();
    console.log('Element disconnected');
  }

  updated(changedProperties) {
    super.updated(changedProperties);
    changedProperties.forEach((oldValue, name) => {
      console.log(`${name} changed from ${oldValue}`);
    });
  }

  render() {
    return html`<div>Updated: ${Date.now()}</div>`;
  }
}
```

### Fix 4: Handle async rendering

```javascript
import { LitElement, html } from 'lit';

class AsyncElement extends LitElement {
  @property({ type: Array })
  items = [];

  async firstUpdated() {
    const response = await fetch('/api/items');
    this.items = await response.json();
  }

  render() {
    return html`
      <ul>
        ${this.items.map(item => html`
          <li>${item.name}</li>
        `)}
      </ul>
    `;
  }
}
```

## Common Scenarios

- **Property not declared** — Property used in template but not declared with @property.
- **Shadow DOM leak** — Styles from host component leak into shadow DOM.
- **Element not registered** — customElements.define not called.

## Prevent It

- Always use `@property` decorator or `static get properties()` for reactive properties.
- Call `super.connectedCallback()` and `super.disconnectedCallback()` in lifecycle methods.
- Use `static styles` for encapsulated CSS.

## Related Errors

- [TypeError](/javascript/typeerror/) — property undefined
- [LitElement](/javascript/lit-error/) — Lit operation failed
- [ShadowDOMError](/javascript/shadow-dom-error/) — shadow DOM configuration failed
