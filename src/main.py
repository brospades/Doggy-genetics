from app.coat_editor import *
from app.family_editor import *
from app.item_lists import *

help_tab_on = False

if help_tab_on:
    from app.help_tab import *


##### CLASSES #####
### Tabs ###
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window settings
        self.title("Doggy genetics")
        self.geometry("960x540")
        self.resizable(width=False, height=False)
        self.configure(fg_color=back_color)

        # Grid settings
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=0)
        self.grid_columnconfigure((3), weight=1)

        if help_tab_on:
            self.top_window = Help(self)
            self.top_window.withdraw()
        else:
            self.top_window = None

        # Frame and button dictionaries
        self.frames = {}
        self.buttons = {}

        # List of tab names and frames
        frames_data = [
            ("Dog lists", DogLists),
            ("Coat editor", CoatEditor),
            ("Family tree editor", FamilyEditor),
        ]
        # Create tab buttons
        for i, (tab_name, frame_class) in enumerate(frames_data):
            tab = ctk.CTkFrame(self, height=35, fg_color="transparent")
            tab_button = ctk.CTkButton(
                tab,
                fg_color=button_color,
                hover_color=button_hover,
                text=tab_name,
                font=("vds", 20),
                text_color=light_color,
                command=lambda fc=frame_class: self.show_frame(fc),
                width=100,
                corner_radius=10,
            )
            x_button = ctk.CTkButton(
                tab,
                fg_color=x_color,
                hover_color=x_hover,
                text="x",
                font=("vds", 15),
                text_color=light_color,
                command=lambda fc=frame_class: self.hide_button(fc),
                width=25,
                corner_radius=10,
            )
            self.buttons[frame_class] = tab
            tab_button.grid(row=0, column=0, padx=(0, 5))
            if frame_class != DogLists:  # add x button to all tabs excet for DogLists
                x_button.grid(row=0, column=1)
            tab.grid(row=0, column=i, padx=(20, 0), pady=10, sticky="w")
            if frame_class == CoatEditor:
                frame = frame_class(self, self.top_window)
            else:
                frame = frame_class(self)
            self.frames[frame_class] = frame
            frame.grid(
                row=1, column=0, columnspan=4, padx=20, pady=(0, 20), sticky="nsew"
            )
            tab.grid_remove()

            # if not DogLists, pass function from DogLists
            if frame_class != DogLists:
                self.frames[frame_class].set_function(
                    self.frames[DogLists].lists[frame_class].add_clickable_frame
                )

        # Create Help button
        if help_tab_on:
            help = ctk.CTkButton(
                self,
                fg_color=button_color,
                hover_color=button_hover,
                text="Help",
                font=("vds", 20),
                text_color=light_color,
                command=self.top_window.show_help,
                width=100,
                corner_radius=10,
            )
            help.grid(row=0, column=3, pady=10, padx=20, sticky="e")  # show help button

        self.show_frame(DogLists)  # show first tab
        self.show_button(DogLists)  # show first tab button

    def show_frame(self, frame_class):
        for frame in self.frames.values():
            frame.grid_remove()  # hide current frame
        frame = self.frames[frame_class]  # find chosen frame in dictionary
        frame.grid()  # show chosen frame

    def show_button(self, frame_class, rule=None):
        tab_button = self.buttons[frame_class]  # find chosen button in dictionary
        tab_button.grid()  # show chosen button
        if rule == "new":
            self.frames[frame_class].new_item()

    def hide_button(self, frame_class):
        self.buttons[frame_class].grid_remove()  # hide chosen button
        self.show_frame(DogLists)


app = App()

##### PROGRAM SETTINGS #####
# Theme
ctk.set_appearance_mode("Light")  # или "Light"
ctk.set_default_color_theme("blue")  # другие: green, dark-blue


##### START #####
app.mainloop()
