import customtkinter as ctk

from core.constants import *


# Clickable frame for lists
class ClickableFrame(ctk.CTkFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command

        # Settings
        self.normal_color = self.cget("fg_color")
        self.hover_color = back_color

        # Make grid and place all elements
        self.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.grid_columnconfigure((0), weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1), weight=0)

        # Name
        self.name = ctk.CTkLabel(
            self,
            font=("vds", 25),
            text="Name",
            text_color=dark_color,
            fg_color="transparent",
            bg_color="transparent",
        )
        self.name.grid(row=0, column=1, pady=(30, 5), sticky="nw")

        # Description
        self.desc = ctk.CTkLabel(
            self,
            font=("vds", 20),
            text="Description",
            text_color=mid_color,
        )
        self.desc.grid(row=1, column=1, pady=(0, 30), sticky="nw")

        # Image (for dog list only)
        self.image = ctk.CTkLabel(
            self,
            fg_color=light_color,
            text="",
            height=100,
            width=100,
            corner_radius=7,
        )
        self.image.grid(row=0, rowspan=2, column=0, pady=10, padx=(10, 20), sticky="w")

        # Set events for the frame
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.configure(cursor="hand2")

        # Set events for child widgets of the frame
        for child in self.winfo_children():
            child.bind("<Enter>", self._on_enter)
            child.bind("<Leave>", self._on_leave)
            child.bind("<Button-1>", self._on_click)
            child.configure(cursor="hand2")

    def _on_enter(self, event):
        """Change background color when hovering"""
        self.configure(fg_color=self.hover_color)

    def _on_leave(self, event):
        """Change background color back after hovering"""
        self.configure(fg_color=self.normal_color)

    def _on_click(self, event):
        """Button command"""
        if self.command:
            self.command()
