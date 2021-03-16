# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from editBar import EditBar
from imageViewer import ImageViewer

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.filter_frame = None
        self.adjust_frame = None
        self.is_image_selected = False
        self.is_draw_state = False
        self.is_crop_state = False
        self.title("IMAGE EDITOR")
        self.editbar = EditBar(master=self)
        self.image_viewer = ImageViewer(master=self)
        self.editbar.pack(padx=10,pady=5, expand=1)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=5, expand=1)
