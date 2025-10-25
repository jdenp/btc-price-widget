# BTC Price Widget

A small, always-on-top **BTC/USD price ticker** built with Python and Tkinter.  
Displays the current Bitcoin price from Binance in a floating, draggable widget.


---

## Features

- Fetches live BTC/USD prices from Binance.
- Updates automatically every second (configurable).
- Floating, always-on-top, and semi-transparent window.
- Color-coded price changes:
  - **Green**: price increased or unchanged.
  - **Red**: price decreased.
- Draggable with the mouse.
- Right-click to close the widget.
- Runs as a `.pyw` with **no console window**.

---

## Setup

This repo uses `uv` for dependency management.

[Install here.](https://docs.astral.sh/uv/getting-started/installation/)

To start/sync dependencies, `uv sync`.
To add, `uv add`.
To remove, `uv remove`.

Entry point is `src/main.py` -> `uv run src/main.py`

---

### Options

You can configure:

- `refresh_interval` — how often the price updates (in seconds).
- `transparency` — window transparency (0 = fully transparent, 1 = opaque).

---

## Controls

- **Left-click & drag** → move the widget.
- **Right-click** → close the widget.

---

## Notes

- If running as a `.pyw` (no console), network errors will show a **popup messagebox** instead of printing to console.
- Designed for **lightweight, always-on-top monitoring** of Bitcoin price.

---
