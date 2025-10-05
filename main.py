import customtkinter as ctk
from PIL import Image, ImageTk

from genes import *

help_tab_on = True

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
class Dog:
    "All dogs created by user"

    def __init__(self, dog_id, dog_name):
        self.dog_id = dog_id
        self.dog_name = dog_name


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

    def hide_button(self, frame_class):
        self.buttons[frame_class].grid_remove()  # hide chosen button
        self.show_frame(DogLists)

    # def create_dog(self): make new dog object


class DogLists(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=frame_color)

        # Grid settings
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # List of column titles and frames
        lists_data = [
            ("My dogs", CoatEditor),
            ("My family trees", FamilyEditor),
        ]
        # Create + buttons
        for i, (title, frame_class) in enumerate(lists_data):
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
                command=lambda fc=frame_class: (
                    self.master.show_frame(fc),
                    self.master.show_button(fc),
                ),
            )
            list_title.grid(row=0, column=i, pady=10)
            btn.grid(row=1, column=i, sticky="n")
        user_dogs = DogList(self)
        user_families = FamilyList(self)
        user_dogs.grid(row=2, column=0, padx=20, pady=10, sticky="snew")
        user_families.grid(row=2, column=1, padx=20, pady=10, sticky="snew")


class DogList(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=inner_frame_color)

        self.label = ctk.CTkLabel(self, text="list1")
        self.label.grid(row=0, column=0, padx=20)


class FamilyList(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=inner_frame_color)

        self.label = ctk.CTkLabel(self, text="list2")
        self.label.grid(row=0, column=0, padx=20)


class CoatEditor(ctk.CTkFrame):
    def __init__(self, master, instance):
        super().__init__(master)
        self.configure(fg_color=inner_frame_color)
        self.dogmodel_link = DogModel
        self.help_link = instance

        # Grid settings
        self.grid_columnconfigure(0, weight=2)  # Two halves - dog and genes
        self.grid_columnconfigure(
            1, weight=1, minsize=440
        )  # Two halves - dog and genes
        self.grid_rowconfigure(0, weight=1)

        dog_half = ctk.CTkFrame(self, fg_color="transparent")
        dog_half.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")
        dog_half.grid_rowconfigure(0, weight=0)  # Top row
        dog_half.grid_rowconfigure(1, weight=1)  # Dog image area
        dog_half.grid_columnconfigure(0, weight=1)

        dog_top = ctk.CTkFrame(dog_half, height=60, fg_color="transparent")
        dog_top.grid(row=0, column=0, sticky="nsew")
        dog_top.grid_columnconfigure((0, 1), weight=1)
        dog_top.grid_rowconfigure(0)
        dog_name = ctk.CTkEntry(
            dog_half,
            height=50,
            font=("vds", 25),
            text_color=dark_color,
            border_color=grey_text,
            placeholder_text="Name",
            placeholder_text_color=grey_text,
            fg_color=inner_frame_color,
        )
        dog_name.grid(row=0, column=0, padx=10, sticky="w")
        # Dog base
        self.dog_model = DogModel(dog_half)
        self.dog_model.grid(row=1, column=0, sticky="w")

        gene_half = ctk.CTkFrame(self, fg_color="transparent")
        gene_half.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        gene_half.grid_rowconfigure(0, weight=0)  # Top row
        gene_half.grid_rowconfigure(1, weight=1)  # Gene list
        gene_half.grid_columnconfigure(0, weight=1)

        gene_top = ctk.CTkFrame(gene_half, height=25, fg_color="transparent")
        gene_top.grid(row=0, column=0, pady=(0, 10), sticky="nse")
        gene_top.grid_columnconfigure((0, 1), weight=0)
        save_button = ctk.CTkButton(
            gene_top,
            width=40,
            text="",
            image=save_icon,
            fg_color="transparent",
            hover_color=mid_color,
        )
        save_button.grid(row=0, column=1)

        gene_list = ctk.CTkScrollableFrame(
            gene_half,
            fg_color=frame_color,
            scrollbar_button_color=mid_color,
            scrollbar_button_hover_color=button_hover,
        )
        gene_list.grid(row=1, column=0, sticky="nsew")
        gene_list.grid_columnconfigure(0, weight=1)

        # Dictionaries
        self.genotype = {}  # Pairs of selected alleles for each locus
        self.pretty_genotype = {}
        self.genotype_desc = {}  # List of used descriptions

        # Contents of the scrollable frame
        for i, (section, genes_in_section) in enumerate(genes_list):
            section_frame = ctk.CTkFrame(gene_list, fg_color="transparent")
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
                    # Set different starter choices
                    if locus_name in replacement_list:
                        gene_menu.set(replacement_list[locus_name])
                    gene_menu.grid(row=1 + j, column=m, pady=(0, 3), sticky="n")
                    # Fill dictionary with "_'s" for each locus
                    self.genotype[(locus_name, m)] = "_"
                    self.pretty_genotype[(locus_name.letter)] = None

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
        for y in range(2):
            for locus_key in replacement_list:
                self.allele_callback(replacement_list[locus_key], locus_key, y)

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
        self.dogmodel_link.dog_configure(self.dog_model, self.pretty_genotype)

    # def save_dog():


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
        # work out WHITE
        # work out RED

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
        # WHAT IF ee AND aa (samoyed?)

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
        display = ctk.CTkLabel(self, image=self.comp, text="")
        display.grid(row=0, column=0)


class FamilyEditor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=frame_color)

        # Widgets
        self.test = ctk.CTkLabel(self, text="fam editor", fg_color="transparent")
        self.new_dog = ctk.CTkButton(self, text="++")
        self.test.grid(row=0, column=0, padx=20)


app = App()

##### PROGRAM SETTINGS #####
# Theme
ctk.set_appearance_mode("Light")  # или "Light"
ctk.set_default_color_theme("blue")  # другие: green, dark-blue


##### START #####
app.mainloop()
