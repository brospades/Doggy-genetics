import customtkinter as ctk

from core.constants import *

from app.coat_editor import *
from app.family_editor import *
from app.widgets import ClickableFrame


class DogLists(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=frame_color)

        # Grid settings
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # List dictionaries
        self.lists = {}

        # List of column titles and frames
        lists_data = [
            ("My dogs", CoatEditor),
            ("My family trees", FamilyEditor),
        ]

        # Create + buttons and scrollable frames
        for i, (title, frame_class) in enumerate(lists_data):
            x, y = 50, 20
            if i == 1:
                x, y = y, x
            list_title = ctk.CTkLabel(
                self,
                text=title,
                font=("vds", 25),
                text_color=dark_color,
                fg_color="transparent",
            )
            btn = ctk.CTkButton(
                self,
                width=100,
                text="+",
                font=("vds", 20),
                text_color=light_color,
                command=lambda fc=frame_class: (
                    self.master.show_frame(fc),
                    self.master.show_button(fc, "new"),
                ),
                fg_color=mid_color,
                hover_color=button_hover,
            )
            list_title.grid(row=0, column=i, pady=10, padx=(x, y))
            btn.grid(row=1, column=i, padx=(x, y), sticky="n")
            list_widget = ItemList(self)
            list_widget.grid(row=2, column=i, padx=(x, y), pady=10, sticky="nsew")
            self.lists[frame_class] = list_widget


# List for dogs or families
class ItemList(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(
            fg_color=inner_frame_color,
            scrollbar_button_color=mid_color,
            scrollbar_button_hover_color=button_hover,
            width=350,
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # Clickable frame dictionary
        self.clickableframes = {}

    def add_clickable_frame(self, link_to, used_item, i):
        """Add new clickable frame to a list"""
        if i in self.clickableframes.keys():
            self.clickableframes[i].grid_remove()
        clickable_frame = ClickableFrame(
            self.master.master.master.master.frames[DogLists].lists[link_to],
            fg_color=frame_color,
            command=lambda link=link_to: self.frame_clicked(link, i),
            corner_radius=10,
        )
        clickable_frame.grid(row=i, column=0)

        # Delete button
        self.delete_button = ctk.CTkButton(
            clickable_frame,
            text="",
            image=delete_icon,
            fg_color="transparent",
            hover_color=back_color,
            command=lambda link=link_to: self.frame_deleted(link, i),
            width=15,
            height=25,
            corner_radius=5,
        )
        self.delete_button.grid(row=0, rowspan=2, column=1, sticky="es", padx=5, pady=5)

        # Set dog, desc, image
        clickable_frame.name.configure(text=used_item.name)
        clickable_frame.desc.configure(text=used_item.desc)
        clickable_frame.image.configure(image=used_item.icon)

        self.clickableframes[i] = clickable_frame

    def frame_clicked(self, link_to, i):
        """Event on click"""
        # Show frame
        self.master.master.master.master.show_frame(link_to)
        # Show button
        self.master.master.master.master.show_button(link_to)
        # Set dog
        self.master.master.master.master.frames[link_to].open_item(i)

    def frame_deleted(self, link_to, i):
        """Delete button"""
        # Delete item from dog list and button list
        print(f"hide button {i}")
        self.clickableframes[i].grid_forget()
        print(my_dogs)
        print(self.clickableframes)
        del my_dogs[i]
        del self.clickableframes[i]
