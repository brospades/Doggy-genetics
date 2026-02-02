from core.constants import *
from genetics.genes import *


class FamilyEditor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=frame_color)

        # Widgets
        # self.test = ctk.CTkButton(
        #    self, text="fam editor", fg_color="transparent", command=self.save_item
        # )
        self.test = ctk.CTkLabel(self, text="To be added", font=("vds", 20))
        self.test.grid(row=0, column=0, padx=20)

    def set_function(self, func):
        """Set link to function from ItemList"""
        self.itemlist_function = func

    def new_item(self):
        print("family added")

    def save_item(self):
        print("family saved")
        self.itemlist_function(FamilyEditor, 1)
