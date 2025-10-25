# BTC Price Widget

A small, always-on-top **BTC/USD price ticker** built with Python and Tkinter.  
Displays the current Bitcoin price from Binance in a floating, draggable widget.

<img width="366" height="45" alt="image" src="https://github.com/user-attachments/assets/40c56cc2-025d-4ee6-a250-4501443a2b43" />


## Features

- Fetches live BTC/USD prices from Binance.
- Updates automatically every second (configurable).
- Floating, always-on-top, semi-transparent window.
- Color-coded price changes:
  - **Green**: price increased or unchanged.
  - **Red**: price decreased.
- Draggable with the mouse.
- Right-click to close the widget.
- Runs as a `.pyw` with **no console window**.


## Setup

This repo uses `uv` for dependency management.

[Install here.](https://docs.astral.sh/uv/getting-started/installation/)

To start/sync dependencies, `uv sync`.
To add, `uv add`.
To remove, `uv remove`.

Entry point is `src/main.py` -> `uv run src/main.py`


### Options

You can configure:

- `refresh_interval` — how often the price updates (in seconds).
- `transparency` — window transparency (0 = fully transparent, 1 = opaque).


## Controls

- **Left-click & drag** → move the widget.
- **Right-click** → close the widget.


---
