import tkinter as tk


class Screen:
    @staticmethod
    def get_screen_resolution():
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
        return screen_width, screen_height
