import tkinter as tk
import time

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("Canvas")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.objects = {}
        self.last_click_x = 0
        self.last_click_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<Motion>", self._on_motion)
        
    def _on_click(self, event):
        self.last_click_x = event.x
        self.last_click_y = event.y
        
    def _on_motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        
    def create_rectangle(self, x1, y1, x2, y2, color):
        obj = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.objects[obj] = {'type': 'rectangle', 'color': color}
        return obj
        
    def moveto(self, obj, x, y):
        coords = self.canvas.coords(obj)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(obj, x, y, x + width, y + height)
        
    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)
        self.objects[obj]['color'] = color
        
    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)
        
    def get_mouse_x(self):
        return self.mouse_x
        
    def get_mouse_y(self):
        return self.mouse_y
        
    def get_last_click(self):
        return self.last_click_x, self.last_click_y
        
    def wait_for_click(self):
        self.root.update()
        while True:
            if self.last_click_x != 0 or self.last_click_y != 0:
                break
            self.root.update()
            time.sleep(0.05)
        return self.last_click_x, self.last_click_y 