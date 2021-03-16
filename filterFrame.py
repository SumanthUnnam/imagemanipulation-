# -*- coding: utf-8 -*-
from tkinter import Toplevel, Button, RIGHT
import numpy as np
import cv2


class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.filtered_image = None

        self.negative_bt = Button(master=self, text="Negative")
        self.bnw_bt = Button(master=self, text="Black White")
        self.gaussian_blur_bt = Button(master=self, text="Gaussian Blur")
        self.cancel_bt = Button(master=self, text="Cancel")
        self.apply_bt = Button(master=self, text="Apply")
        self.negative_bt.bind("<ButtonRelease>", self.negative_bt_released)
        self.bnw_bt.bind("<ButtonRelease>", self.bnw_bt_released)
        self.gaussian_blur_bt.bind("<ButtonRelease>", self.gaussian_blur_bt_released)
        self.apply_bt.bind("<ButtonRelease>", self.apply_bt_released)
        self.cancel_bt.bind("<ButtonRelease>", self.cancel_bt_released)

        self.negative_bt.pack()
        self.bnw_bt.pack()
        self.gaussian_blur_bt.pack()
        self.cancel_bt.pack(side=RIGHT)
        self.apply_bt.pack()

    def negative_bt_released(self, event):
        self.negative()
        self.show_image()

    def bnw_bt_released(self, event):
        self.black_white()
        self.show_image()

    def gaussian_blur_bt_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def apply_bt_released(self, event):
        self.master.processed_image = self.filtered_image
        self.show_image()
        self.close()

    def cancel_bt_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def negative(self):
        self.filtered_image = cv2.bitwise_not(self.original_image)

    def black_white(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)

    def gaussian_blur(self):
        self.filtered_image = cv2.GaussianBlur(self.original_image, (41, 41), 0)

    def close(self):
        self.destroy()
