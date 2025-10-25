import tkinter as tk
import requests
import threading
import time
from typing import Optional


class BTCPriceFetcher:
    """Fetches the current BTC/USD price from Binance."""

    API_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    def __init__(self, timeout: float = 3.0):
        self.timeout = timeout

    def fetch(self) -> Optional[float]:
        """Fetch the latest BTC/USD price."""
        try:
            resp = requests.get(self.API_URL, timeout=self.timeout)
            data = resp.json()
            return float(data["price"])
        except Exception as e:
            # Error messagebox - widget is console-absent
            mbox.showerror("BTC Price Widget", f"Error fetching price:\n{e}")
            return None


class BTCPriceWidget:
    """Tkinter widget that displays the current BTC/USD price."""

    def __init__(self, refresh_interval: float = 1.0, transparency: float = 0.85):
        self.refresh_interval = refresh_interval
        self.fetcher = BTCPriceFetcher()
        self.running = True
        self.prev_price: Optional[float] = None

        # --- UI Setup ---
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", transparency)
        self.root.geometry("200x40+100+100")
        self.root.configure(bg="#111")

        self.price_label = tk.Label(
            self.root, text="...", font=("Arial", 21, "bold"), fg="#00FF66", bg="#111"
        )
        self.price_label.pack(pady=(0, 0))

        # --- Event bindings ---
        self.root.bind("<Button-1>", self._start_move)
        self.root.bind("<B1-Motion>", self._do_move)
        self.root.bind("<Button-3>", self._close_widget)

        # --- Start background thread ---
        self.thread = threading.Thread(target=self._price_loop, daemon=True)
        self.thread.start()

    def _start_move(self, event: tk.Event) -> None:
        self._offset_x = event.x
        self._offset_y = event.y

    def _do_move(self, event: tk.Event) -> None:
        x = event.x_root - self._offset_x
        y = event.y_root - self._offset_y
        self.root.geometry(f"+{x}+{y}")

    def _close_widget(self, event: Optional[tk.Event] = None) -> None:
        """Stop background thread and close the widget."""
        self.running = False
        self.root.destroy()

    def _price_loop(self) -> None:
        """Fetch and update the BTC price periodically."""
        while self.running:
            btc_usd = self.fetcher.fetch()
            if btc_usd is not None:
                color = "#00FF66" if self.prev_price is None or btc_usd >= self.prev_price else "#FF5555"
                self.prev_price = btc_usd
                self.root.after(
                    0,
                    lambda c=color, p=btc_usd: self.price_label.config(
                        text=f"1₿ = ${p:,.0f}", fg=c
                    ),
                )
            time.sleep(self.refresh_interval)

    def run(self) -> None:
        """Public method - run the widget main loop."""
        try:
            self.root.mainloop()
        finally:
            self.running = False


if __name__ == "__main__":
    widget = BTCPriceWidget(refresh_interval=1.0, transparency=0.85)
    widget.run()
