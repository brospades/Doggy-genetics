import customtkinter as ctk
from PIL import Image, ImageTk

from genes import *

help_tab_on = False

if help_tab_on:
    from help_tab import *


##### FONTS AND COLORS #####
ctk.FontManager.load_font("vds.ttf")  # VDS bold

back_color = "#56B5AE"
frame_color = "#87C8C4"
inner_frame_color = "#C9DBDA"
button_color = "#0D5A68"
button_hover = "#177E90"
x_color = "#842613"
x_hover = "#AA3922"

light_color = "#F0F1E8"
dark_color = "#08424D"
mid_color = "#3B8492"
grey_text = "#7C8E92"


##### DOG #####
my_dogs = []


class Dog:
    "All dogs created by user"

    def __init__(
        self,
        master,
        dog_genotype,
        dog_pretty_genotype,
        dog_pretty_result,
        dog_comp,
        dog_icon,
        dog_name="My dog",
    ):
        self.genotype = dog_genotype  # Pairs of selected alleles for each locus
        self.pretty_genotype = dog_pretty_genotype  # Gene + desc

        # Name
        if master.dog_name.get():
            dog_name = master.dog_name.get()
        self.name = dog_name
        if len(self.name) > 12:
            self.name = self.name[:10] + ".."

        # Text result
        self.desc = " ".join(list(dog_pretty_result.values()))[:19] + ".."

        # Fullsize dog image
        self.comp = dog_comp
        # Dog icon
        self.icon = dog_icon


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

    def show_button(self, frame_class):
        tab_button = self.buttons[frame_class]  # find chosen button in dictionary
        tab_button.grid()  # show chosen button
        if frame_class in (CoatEditor, FamilyEditor):
            self.frames[frame_class].new_item()

    def hide_button(self, frame_class):
        self.buttons[frame_class].grid_remove()  # hide chosen button
        self.show_frame(DogLists)


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
                    self.master.show_button(fc),
                ),
                fg_color=mid_color,
                hover_color=button_hover,
            )
            list_title.grid(row=0, column=i, pady=10, padx=(x, y))
            btn.grid(row=1, column=i, padx=(x, y), sticky="n")
            list_widget = ItemList(self)
            list_widget.grid(row=2, column=i, padx=(x, y), pady=10, sticky="nsew")
            self.lists[frame_class] = list_widget


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

        # Clickable frame dictionary
        self.clickableframes = {}

    def add_clickable_frame(self, link_to, used_item, i):
        """Add new clickable frame to a list"""
        clickable_frame = ClickableFrame(
            self.master.master.master.master.frames[DogLists].lists[link_to],
            fg_color=frame_color,
            command=lambda i=i: self.frame_clicked(i),
            corner_radius=10,
        )
        clickable_frame.grid(row=i, column=0)

        # Set dog, desc, image
        clickable_frame.name.configure(text=used_item.name)
        clickable_frame.desc.configure(text=used_item.desc)
        clickable_frame.image.configure(image=used_item.icon)

        self.clickableframes[i] = clickable_frame
        print("Clickable frame added")
        print(self.clickableframes)

    def frame_clicked(self, i):
        """Event on click"""
        print(f"Clicked {i}")


class ClickableFrame(ctk.CTkFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command

        # Settings
        self.normal_color = self.cget("fg_color")
        self.hover_color = back_color

        # Make grid and place all elements
        self.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.grid_columnconfigure(0, weight=0)
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
        self.name.grid(row=0, column=1, pady=(30, 10), sticky="nw")

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


class CoatEditor(ctk.CTkFrame):
    def __init__(self, master, help_instance):
        super().__init__(master)
        self.configure(fg_color=inner_frame_color)
        self.dogmodel_link = DogModel
        self.help_link = help_instance

        # Grid settings
        self.grid_columnconfigure(0, weight=2)  # Two halves - dog and genes
        self.grid_columnconfigure(
            1, weight=1, minsize=440
        )  # Two halves - dog and genes
        self.grid_rowconfigure(0, weight=1)

        self.dog_half = ctk.CTkFrame(self, fg_color="transparent")
        self.dog_half.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")
        self.dog_half.grid_rowconfigure(0, weight=0)  # Top row
        self.dog_half.grid_rowconfigure(1, weight=1)  # Dog image area
        self.dog_half.grid_columnconfigure(0, weight=1)

        self.dog_top = ctk.CTkFrame(self.dog_half, height=60, fg_color="transparent")
        self.dog_top.grid(row=0, column=0, sticky="nsew")
        self.dog_top.grid_columnconfigure((0, 1), weight=1)
        self.dog_top.grid_rowconfigure(0)
        self.dog_name = ctk.CTkEntry(
            self.dog_half,
            height=50,
            font=("vds", 25),
            text_color=dark_color,
            border_color=grey_text,
            placeholder_text="Name",
            placeholder_text_color=grey_text,
            fg_color=inner_frame_color,
        )
        self.dog_name.grid(row=0, column=0, padx=10, sticky="w")
        # Dog base
        self.dog_model = DogModel(self.dog_half)
        self.dog_model.grid(row=1, column=0, sticky="w")

        self.gene_half = ctk.CTkFrame(self, fg_color="transparent")
        self.gene_half.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.gene_half.grid_rowconfigure(0, weight=0)  # Top row
        self.gene_half.grid_rowconfigure(1, weight=1)  # Gene list
        self.gene_half.grid_columnconfigure(0, weight=1)

        self.gene_top = ctk.CTkFrame(self.gene_half, height=25, fg_color="transparent")
        self.gene_top.grid(row=0, column=0, pady=(0, 10), sticky="nse")
        self.gene_top.grid_columnconfigure((0, 1), weight=0)
        self.save_button = ctk.CTkButton(
            self.gene_top,
            width=40,
            text="",
            image=save_icon,
            fg_color="transparent",
            hover_color=mid_color,
            command=lambda: self.save_item(),
        )
        self.save_button.grid(row=0, column=1)

        self.gene_list = ctk.CTkScrollableFrame(
            self.gene_half,
            fg_color=frame_color,
            scrollbar_button_color=mid_color,
            scrollbar_button_hover_color=button_hover,
        )
        self.gene_list.grid(row=1, column=0, sticky="nsew")
        self.gene_list.grid_columnconfigure(0, weight=1)

        # Dictionaries
        self.section_frames = {}  # Section frames
        self.gene_menus = {}  # Menus by locus+number
        self.genotype_desc = {}  # Description lines

        # Contents of the scrollable frame
        for i, (section, genes_in_section) in enumerate(genes_list):
            section_frame = ctk.CTkFrame(self.gene_list, fg_color="transparent")
            section_frame.grid(row=i, column=0, pady=(0, 15), sticky="ew")
            section_frame.grid_columnconfigure((0, 1, 2), weight=1)
            section_title = ctk.CTkLabel(  # Section name
                section_frame,
                text=section,
                font=("vds", 20),
                text_color=dark_color,
                fg_color=back_color,
                corner_radius=10,
            )
            section_title.grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="ew")
            self.section_frames[section] = section_frame

            for j, (locus_name, allele_options) in enumerate(genes_in_section):
                for m in range(2):
                    gene_menu = ctk.CTkOptionMenu(  # Two option menus
                        section_frame,
                        width=60,
                        font=("vds", 17),
                        text_color=light_color,
                        values=allele_options,
                        command=lambda choice, lc=locus_name, n=m: self.allele_callback(
                            choice, lc, n
                        ),
                        fg_color=back_color,
                        button_color=mid_color,
                        button_hover_color=button_hover,
                        dropdown_fg_color=inner_frame_color,
                        dropdown_hover_color=frame_color,
                        dropdown_font=("vds", 17),
                        dropdown_text_color=dark_color,
                    )
                    gene_menu.grid(row=1 + j, column=m, pady=(0, 3), sticky="n")
                    self.gene_menus[(locus_name, m)] = gene_menu

                gene_desc = ctk.CTkButton(  # Gene descripton
                    section_frame,
                    width=150,
                    text=locus_name.results[frozenset({"_"})][0],
                    font=("vds", 15),
                    text_color=mid_color,
                    hover_color=back_color,
                    fg_color="transparent",
                    command=lambda ll=locus_name.letter: (
                        self.help_link.show_help(),
                        self.help_link.show_frame(ll),
                    ),
                )
                gene_desc.grid(row=1 + j, column=2, sticky="n")
                self.genotype_desc[locus_name] = gene_desc  # save gene descriprion

        # Set different starter alleles

    def allele_callback(self, choice, locus, num):
        # add change to genotype
        self.genotype[(locus, num)] = choice
        # combine alleles of the locus into set
        allele_set = frozenset((self.genotype[(locus, 0)], self.genotype[(locus, 1)]))
        # pull results from dictionary using set of alleles
        text_result, pretty_genes, show_res = locus.results[allele_set]
        # update pretty genotype with allele set
        self.pretty_genotype[(locus.letter)] = show_res
        self.genotype_desc[locus].grid_remove()  # hide chosen desc
        desc = self.genotype_desc[locus]
        desc.configure(text=text_result)  # change desc based on dict data
        desc.grid()  # add new desc-
        self.pretty_result[locus] = pretty_genes
        self.dogmodel_link.dog_configure(self.dog_model, self.pretty_genotype)

    def set_function(self, func):
        """Set link to function from ItemList"""
        self.itemlist_function = func

    def new_item(self):
        print("dog added")

        # Clear name and deselect
        self.dog_name.delete(0, len(self.dog_name.get()))
        self.master.focus_set()

        # Dictionaries
        self.genotype = {}  # Pairs of selected alleles for each locus
        self.pretty_genotype = {}  # Gene + desc
        self.pretty_result = {}  # Text result

        # Go through buttons
        for (locus_name, num), menu in self.gene_menus.items():
            # Set default options
            if locus_name in replacement_list:
                default_value = replacement_list[locus_name]
            else:
                default_value = "_"
            menu.set(default_value)
            # Save them to genotype
            self.genotype[(locus_name, num)] = default_value
            # Set pretties to None
            self.pretty_genotype[locus_name.letter] = None
        # Go through descriptions
        for locus_name, desc_button in self.genotype_desc.items():
            # Set them to default options
            desc_button.configure(text=locus_name.results[frozenset({"_"})][0])
        # For both menus, set them to replacement options
        for locus_key in replacement_list:
            for y in range(2):
                self.allele_callback(replacement_list[locus_key], locus_key, y)

    def save_item(self):
        """Save NEW dog item"""
        print("dog saved")
        # Create dog object and save it to my_dogs
        saved_dog = Dog(
            self,
            self.genotype,
            self.pretty_genotype,
            self.pretty_result,
            self.dog_model.comp,
            self.dog_model.icon,
        )
        my_dogs.append(saved_dog)
        # Add new button to DogLists
        self.itemlist_function(CoatEditor, saved_dog, len(my_dogs) - 1)


class DogModel(ctk.CTkFrame):
    def __init__(self, master, width=550, height=386):
        super().__init__(master)
        self.canvas = ctk.CTkCanvas(
            self, width=width, height=height, highlightthickness=0
        )
        self.canvas.grid(row=0, column=0)
        self.configure(fg_color="transparent")

    # Make dog image, based off the whole genotype at the moment
    def dog_configure(self, genotype):
        self.eumelanin_color = "none"  # Eumelanin color - not set
        self.phaeomelanin_color = "none"  # Phaeomelanin color - not set
        self.brindle_color = "none"  # Mask color - not set
        self.mask_color = "none"  # Mask color - not set
        self.merle_color = ""  # Merle color - not set
        self.white_color = ""  # White color - not set
        self.phaeo_shade = "none"

        # Eumelanin-related and merle (B/D, M, H)
        # Layers: eumelanin, white
        if genotype["B"] and genotype["D"]:
            # Set base color
            self.eumelanin_color = eumelanin_shade[genotype["B"] + genotype["D"]]
            if genotype["M"] == "double merle":
                # Double merle white covers up phaeomelanin too
                self.eumelanin_color += " " + "merle"
                self.merle_color = genotype["M"]
                if genotype["H"]:
                    # Harlequin white covers up phaeomelanin too
                    self.merle_color += " " + genotype["H"]
            elif genotype["M"]:
                self.eumelanin_color += " " + genotype["M"]
                # Harlequin white covers up phaeomelanin too
                if genotype["H"] == "harlequin":
                    self.merle_color = genotype["H"]

        # Primary pheomelanin color (I)
        # Layers: phaeomelanin
        if genotype["I"]:
            if genotype["I"] == "red":
                self.phaeo_shade = "red"
            elif genotype["I"] == "yellow":
                self.phaeo_shade = "yellow"
            else:
                self.phaeo_shade = "cream"

        # Fur pattern phaeomelanin (K, A)
        # Layers: phaeomelanin, mask
        if genotype["K"] == "solid":
            # Presence of K doesn't allow A to show
            self.phaeomelanin_color = self.phaeo_shade + " eu"
        elif genotype["K"] == "brindle" or "clear":
            # Add brindling of the right color if needed
            if genotype["K"] == "brindle":
                self.brindle_color = self.eumelanin_color + " brindle"
            if genotype["A"]:
                # Add pattern
                self.phaeomelanin_color = self.phaeo_shade + " " + genotype["A"]
            else:
                # A unknown therefore pattern unknown
                self.phaeomelanin_color += " none"
        else:
            # K unknown therefore pattern visibility unknown
            self.phaeomelanin_color = self.phaeo_shade + " none"

        # Masking, recessive red (E)
        # Layers: phaeomelanin, mask
        if genotype["E"] == "mask":
            self.mask_color = "mask " + self.eumelanin_color
        elif genotype["E"] == "rec red":
            self.phaeomelanin_color = self.phaeomelanin_color = (
                self.phaeo_shade + " solid"
            )
            self.brindle_color = "none"

        # Fixes mistake
        if self.phaeomelanin_color == "none solid":
            self.phaeomelanin_color = "none none"

        # White pattern (S, T, F)
        # Layers: white
        if genotype["S"]:  # Assign white spotting
            self.white_color = genotype["S"]
            if genotype["T"]:  # Roan or ticked
                if genotype["T"] == "roan" and genotype["F"]:
                    # Add flecking to roan
                    self.white_color += " " + genotype["F"]
                else:
                    self.white_color += " " + genotype["T"]

        # Overrule: one or several genes covers up the rest
        if genotype["H"] == "dead":
            self.eumelanin_color = "none"
            self.phaeomelanin_color = "none none"
            self.mask_color = "none"
            self.white_color = ""

        # Assign layer variables correct images
        self.white_color = white_pics[self.white_color]
        self.merle_color = white_pics[self.merle_color]
        self.mask_color = mask_pics[self.mask_color]
        self.brindle_color = mask_pics[self.brindle_color]
        self.phaeo_color = phaeo_pics[self.phaeomelanin_color]
        self.eu_color = eu_pics[self.eumelanin_color]

        # Compile layered image from selected images
        self.comp = Image.alpha_composite(self.eu_color, self.phaeo_color)
        self.comp = Image.alpha_composite(self.comp, self.brindle_color)
        self.comp = Image.alpha_composite(self.comp, self.mask_color)
        self.comp = Image.alpha_composite(self.comp, self.white_color)
        self.comp = Image.alpha_composite(self.comp, self.merle_color)
        self.comp = Image.alpha_composite(self.comp, outline)
        self.comp = ctk.CTkImage(
            light_image=self.comp,
            size=(550, 386),
        )
        self.display = ctk.CTkLabel(self, image=self.comp, text="")
        self.display.grid(row=0, column=0)

        self.icon = self.image_clone(self.comp, (100, 70))

    def image_clone(self, image, new_size):
        pil_image = image._light_image
        return ctk.CTkImage(light_image=pil_image, size=new_size)


class FamilyEditor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=frame_color)

        # Widgets
        self.test = ctk.CTkButton(
            self, text="fam editor", fg_color="transparent", command=self.save_item
        )
        self.test.grid(row=0, column=0, padx=20)

    def set_function(self, func):
        """Set link to function from ItemList"""
        self.itemlist_function = func

    def new_item(self):
        print("family added")

    def save_item(self):
        print("family saved")
        self.itemlist_function(FamilyEditor, 1)


app = App()

##### PROGRAM SETTINGS #####
# Theme
ctk.set_appearance_mode("Light")  # или "Light"
ctk.set_default_color_theme("blue")  # другие: green, dark-blue


##### START #####
app.mainloop()
