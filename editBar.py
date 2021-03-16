# -*- coding: utf-8 -*-
from tkinter import Frame, Button, LEFT
from tkinter import filedialog
from filterFrame import FilterFrame
from adjustFrame import AdjustFrame
import cv2


class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.open_bt = Button(self, text="Open")
        self.save_bt = Button(self, text="Save")
        self.save_as_bt = Button(self, text="Save As")
        self.draw_bt = Button(self, text="Draw")
        self.crop_bt = Button(self, text="Crop")
        self.filter_bt = Button(self, text="Filter")
        self.edit_bt = Button(self, text="Edit")
        self.revert_bt = Button(self, text="Revert")
        self.open_bt.bind("<ButtonRelease>", self.open_bt_released)
        self.save_bt.bind("<ButtonRelease>", self.save_bt_released)
        self.save_as_bt.bind("<ButtonRelease>", self.save_as_bt_released)
        self.draw_bt.bind("<ButtonRelease>", self.draw_bt_released)
        self.crop_bt.bind("<ButtonRelease>", self.crop_bt_released)
        self.filter_bt.bind("<ButtonRelease>", self.filter_bt_released)
        self.edit_bt.bind("<ButtonRelease>", self.edit_bt_released)
        self.revert_bt.bind("<ButtonRelease>", self.revert_bt_released)

        self.open_bt.pack(side=LEFT)
        self.save_bt.pack(side=LEFT)
        self.save_as_bt.pack(side=LEFT)
        self.draw_bt.pack(side=LEFT)
        self.crop_bt.pack(side=LEFT)
        self.filter_bt.pack(side=LEFT)
        self.edit_bt.pack(side=LEFT)
        self.revert_bt.pack()

    def open_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.open_bt:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)
            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True

    def save_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_bt:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_bt:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type
                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)
                self.master.filename = filename

    def draw_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_bt:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()

    def crop_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_bt:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def filter_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_bt:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def edit_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.edit_bt:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()

    def revert_bt_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.revert_bt:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()
