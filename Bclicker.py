import tkinter as tk
from pynput import mouse
import pyautogui
import time
import keyboard

class MouseControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Control App")

        self.x_label = tk.Label(root, text="X: 0", font=('Arial', 12))
        self.x_label.pack(pady=5)

        self.y_label = tk.Label(root, text="Y: 0", font=('Arial', 12))
        self.y_label.pack(pady=5)

        self.saved_x_label = tk.Label(root, text="Saved X: None", font=('Arial', 12))
        self.saved_x_label.pack(pady=5)

        self.saved_y_label = tk.Label(root, text="Saved Y: None", font=('Arial', 12))
        self.saved_y_label.pack(pady=5)

        self.clicks_var = tk.IntVar(value=1)
        self.interval_var = tk.DoubleVar(value=0.1)

        self.clicks_entry = tk.Entry(root, textvariable=self.clicks_var)
        self.clicks_entry.pack(pady=5)

        self.interval_entry = tk.Entry(root, textvariable=self.interval_var)
        self.interval_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start_clicking)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_esc_button = tk.Button(root, text="Stop ESC", command=self.stop_clicking)
        self.stop_esc_button.pack(side=tk.RIGHT, padx=10)

        self.listener = mouse.Listener(on_move=self.on_mouse_move, on_click=self.on_mouse_click)
        self.listener.start()

    def on_mouse_move(self, x_coord, y_coord):
        self.x_label.config(text=f"X: {x_coord}")
        self.y_label.config(text=f"Y: {y_coord}")

    def on_mouse_click(self, x_coord, y_coord, button, pressed):
        if button == mouse.Button.right and pressed:
            self.saved_x = x_coord
            self.saved_y = y_coord
            self.saved_x_label.config(text=f"Saved X: {self.saved_x}")
            self.saved_y_label.config(text=f"Saved Y: {self.saved_y}")

    def start_clicking(self):
        if hasattr(self, 'saved_x') and hasattr(self, 'saved_y'):
            clicks = int(self.clicks_entry.get())
            interval = float(self.interval_entry.get())
            pyautogui.moveTo(self.saved_x, self.saved_y)
            for _ in range(clicks):
                if keyboard.is_pressed('esc'):
                    break
                pyautogui.click()
                time.sleep(interval)

    def stop_clicking(self):
        keyboard.unhook_all()

def main():
    root = tk.Tk()
    app = MouseControlApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()