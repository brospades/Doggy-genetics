import customtkinter as ctk

from core.constants import *
from genetics.help import *


##### MODULES #####


class Help(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Help")
        self.geometry("400x540")
        self.resizable(width=False, height=False)
        self.configure(fg_color=back_color)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.withdraw()

        # Frame dictionary
        self.frames = {}

        # Add main frame
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=0, sticky="news")
        self.frame.grid_rowconfigure(0, weight=0)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.page_name_label = ctk.CTkLabel(
            self.frame,
            text="Help",
            font=("vds", 25),
            text_color=dark_color,
        )
        self.page_name_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.frame = HelpMain(self.frame, self)
        self.frames["Main"] = self.frame
        self.frame.grid(
            row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="snew"
        )

        # Fill dictionary
        for locus in locus_names:
            # Make big frame
            self.frame = ctk.CTkFrame(self, fg_color="transparent")
            self.frame.grid(row=0, column=0, sticky="news")
            self.frame.grid_rowconfigure(0, weight=0)
            self.frame.grid_rowconfigure(1, weight=1)
            self.frame.grid_columnconfigure((0, 1), weight=1)

            # Page name
            page_name = locus.proper_name
            self.page_name_label = ctk.CTkLabel(
                self.frame,
                text=page_name,
                font=("vds", 25),
                text_color=dark_color,
            )
            # Resize page names to fit them in
            if locus.letter in ("D", "F"):
                self.page_name_label.configure(font=("vds", 23))
            elif locus.letter in ("G"):
                self.page_name_label.configure(font=("vds", 22))
            elif locus.letter in ("I", "A"):
                self.page_name_label.configure(font=("vds", 21))
            elif locus.letter in ("E"):
                self.page_name_label.configure(font=("vds", 20))
            self.page_name_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

            # Back button
            self.page_back_btn = ctk.CTkButton(
                self.frame,
                text="Back",
                font=("vds", 20),
                text_color=light_color,
                fg_color=button_color,
                hover_color=button_hover,
                width=80,
                corner_radius=10,
                command=lambda: self.show_frame("Main"),
            )
            self.page_back_btn.grid(row=0, column=1, pady=10, padx=10, sticky="e")

            # Put little frame into big frame
            self.scframe = HelpFrame(self.frame, locus.letter)
            self.scframe.grid(
                row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="snew"
            )
            self.frames[locus.letter] = self.frame

        self.show_frame("Main")

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_remove()  # hide current frame
        frame = self.frames[frame_name]  # find chosen frame in dictionary
        frame.grid()  # show chosen frame

    def show_help(self):
        if not self.winfo_exists():  # if wondow was destroyed, show another
            self.__init__(self.master)
        self.deiconify()
        self.lift()
        self.focus()


class HelpMain(ctk.CTkScrollableFrame):  # Main help frame (with buttons)
    def __init__(self, master, instance):
        super().__init__(master)
        self.configure(
            fg_color=frame_color,
            scrollbar_button_color=mid_color,
            scrollbar_button_hover_color=button_hover,
        )
        self.help_instance = instance

        self.grid_columnconfigure(0, weight=1)

        self.text = ctk.CTkLabel(
            self,
            text=main_first,
            font=("vds", 15),
            text_color=mid_color,
            fg_color="transparent",
        )
        self.text.grid(row=0, column=0, pady=5, sticky="new")

        self.text = ctk.CTkLabel(
            self,
            text=main_second,
            font=("vds", 15),
            text_color=dark_color,
            fg_color="transparent",
        )
        self.text.grid(row=1, column=0, sticky="new")

        for i, (section, genes_in_section) in enumerate(genes_list):
            self.block = ctk.CTkFrame(self, fg_color="transparent")
            self.block.grid(row=2 + i, column=0, sticky="new")
            self.block.grid_columnconfigure(0, weight=1)
            self.label = ctk.CTkLabel(
                self.block,
                height=30,
                text=section,
                font=("vds", 20),
                text_color=dark_color,
                fg_color=back_color,
                corner_radius=10,
            )
            self.label.grid(row=0, column=0, pady=10, sticky="new")
            for j, (locus_name, genes) in enumerate(genes_in_section):
                self.btn = ctk.CTkButton(
                    self.block,
                    height=30,
                    text=locus_name.proper_name,
                    font=("vds", 20),
                    text_color=light_color,
                    fg_color=button_color,
                    hover_color=button_hover,
                    corner_radius=8,
                    command=lambda ll=locus_name.letter: self.help_instance.show_frame(
                        ll
                    ),
                )
                self.btn.grid(row=1 + j, column=0, padx=25, pady=(0, 10), sticky="new")


class HelpFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, letter):
        super().__init__(master)
        self.configure(
            fg_color=frame_color,
            scrollbar_button_color=mid_color,
            scrollbar_button_hover_color=button_hover,
        )
        self.letter = letter
        self.grid_columnconfigure(0, weight=1)

        # Get page intro and page sections
        (intro, texts) = texts_dict[self.letter]
        # Set intro
        self.intro = ctk.CTkLabel(
            self,
            text=intro,
            font=("vds", 15),
            text_color=dark_color,
        )
        self.intro.grid(row=0, column=0, sticky="news")

        for i, (title, image_name, text) in enumerate(texts):
            self.section = ctk.CTkFrame(self, fg_color="transparent")
            self.section.grid(row=1 + i, column=0, sticky="news")
            self.section.grid_columnconfigure(0, weight=1)
            # Make title
            self.txt = ctk.CTkLabel(
                self.section,
                height=30,
                text=title,
                font=("vds", 20),
                text_color=dark_color,
                fg_color=back_color,
                corner_radius=10,
            )
            self.txt.grid(row=0, column=0, pady=10, sticky="ew")
            # Make text block
            self.txt = ctk.CTkLabel(
                self.section,
                text=text,
                font=("vds", 15),
                text_color=dark_color,
            )
            self.txt.grid(row=1, column=0)
            if type(image_name) == str and len(image_name) > 0:  # Make image
                self.img = ctk.CTkLabel(
                    self.section,
                    text="",
                    image=illus_pics[image_name],
                    fg_color="white",
                    corner_radius=10,
                )
                self.img.grid(row=2, column=0, pady=10, sticky="ew")
            elif type(image_name) == tuple:  # Make images
                self.image_block = ctk.CTkFrame(self.section, fg_color="transparent")
                self.image_block.grid(row=2, column=0, pady=(10, 0), sticky="ew")
                self.image_block.grid_columnconfigure(0, weight=1)
                for j, img in enumerate(image_name):
                    self.img = ctk.CTkLabel(
                        self.image_block,
                        text="",
                        image=illus_pics[img],
                        fg_color="white",
                        corner_radius=10,
                    )
                    self.img.grid(row=j, column=0, pady=(0, 10), sticky="ew")
