import customtkinter as ctk
from PIL import Image, ImageTk
from genes import *

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


##### IMAGES #####

# Dictionaries of illustrations
illus_pics = {}

name_list = {
    "B": ("liver 1", "liver 2"),
    "D": ("grey 1", "grey 2", "isabella 1", "isabella 2"),
    "I": ("irish red"),
    "K": ("seal", "ghost tan"),
    "E": ("masked"),
    "S": ("irish"),
    "M": (
        "double",
        "patch size 1",
        "patch size 2",
        "patch size 4",
        "intensity 1",
        "intensity 3",
    ),
    "H": ("harlequin"),
}

# Generate Image objects for all images in name_list
for key in name_list.keys():
    if type(name_list[key]) == str:
        img_name = name_list[key]
        color = ctk.CTkImage(
            light_image=Image.open(
                f"images/illustrations/illus-{key}-{img_name}.png"
            ).convert("RGBA"),
            size=(300, 256),
        )
        illus_pics[img_name] = color
    else:
        for img_name in name_list[key]:
            color = ctk.CTkImage(
                light_image=Image.open(
                    f"images/illustrations/illus-{key}-{img_name}.png"
                ).convert("RGBA"),
                size=(300, 256),
            )
            illus_pics[img_name] = color


##### HELP TEXTS #####
# Texts from the Help window

# Main window
main_first = """I do not guarantee the accuracy of the information
presented here. I am not a geneticist, just a dog liker.
If you spot a mistake, feel free to contact me."""
main_second = "Feel free to use for any of your silly OC business!"

# Texts in format "title - the rest"
texts_dict = {
    "B": (
        """Gene TYRP1 at the B locus is responsible for the color
of eumelanin pigment in the entire dog.
That doesn't only affect the fur color: it also changes 
the colors of the eyes, nose, paw pads, claws, lips 
and eye rims.""",
        (
            (
                "Black eumelanin (BB, Bb)",
                "",
                """All eumelanin in the fur (if any is present) is black.
The nose and paw pads are black.
The eye color is typically a darker brown, but it can 
also be a lighter brown.""",
            ),
            (
                "Liver eumelanin (bb)",
                ("liver 2", "liver 1"),
                """All eumelanin in the fur (if any is present) is brown,
ranging from chocolate to liver.
The nose and paw pads are liver.
The eye color is amber, ranging from lighter 
brown to yellow.""",
            ),
        ),
    ),
    "D": (
        """Gene MLPH at the D locus is responsible for dilution of 
eumelanin pigment in the entire dog.
That doesn't only affect the fur color: it also changes 
the colors of the eyes, nose, paw pads, claws, lips 
and eye rims.""",
        (
            (
                "Non-diluted eumelanin (DD, Dd)",
                "",
                """The color of the dog's eumelanin is unaffected: black 
or liver, depending on the alleles at the B locus.""",
            ),
            (
                "Diluted eumelanin (dd)",
                "",
                """The color of the dog's eumelanin is diluted: blue
(grey) instead of black and isabella instead of liver.""",
            ),
            (
                "Blue (diluted black) eumelanin",
                ("grey 1", "grey 2"),
                """All eumelanin in the fur (if any is present) is grey,
ranging from silver to slate or almost black.
The nose and paw pads are blue.
The eye color is light amber, ranging from yellow and 
light yellow to greenish or grey.""",
            ),
            (
                "Isabella (diluted liver) eumelanin",
                ("isabella 1", "isabella 2"),
                """All eumelanin in the fur (if any is present) is pale
greyish brown, also called "lilac" or "isabella".
The nose and paw pads are isabella. Though, it isn't 
uncommon for isabella dog noses to be as dark as 
noses of liver dogs.
The eye color is light amber, ranging from yellow and 
light yellow to greenish or grey.""",
            ),
        ),
    ),
    "I": (
        """Phaeomelanin intensity is controlled by a number of
different genes. There is at least 5 known loci that
affect the color of a dog's phaeomelanin, and they
are not yet fully studied.
Phaeomelanin comes in a wide range of colors, from
dark red to orange, yellow, cream and pure white.
Here I will talk about MFSD12 gene, responsible for the
colors of Golden Retrievers and Labradors.""",
        (
            (
                "Non-diluted phaeomelanin (II)",
                "",
                """The color of the dog's phaeomelanin is not diluted.
It is orange.""",
            ),
            (
                "Diluted phaeomelanin (Ii, ii)",
                "",
                """The color of the dog's phaeomelanin is diluted.
It ranges from yellow to white: ii are more diluted 
than Ii.""",
            ),
            (
                "Irish setter red",
                "irish red",
                """KITLG gene is responsible for the dark red color of
phaeomelanin, such as the one found in irish setters.""",
            ),
        ),
    ),
    "K": (
        """The alleles at the K locus affect the dog's pattern,
determining whether the pattern coded the by A locus
alleles will be expressed on the coat or not.""",
        (
            (
                "Dominant black (KBKB, KBkbr, KBby)",
                "",
                """KB, also referred to as "dominant black", creates a 
solid eumelanin coat which "covers up" the A locus
alleles, not allowing them to express on the fur.
Despite the name, the coat doesn't have to be black;
it has the color of the dog's eumelanin, whichever
it might be.""",
            ),
            (
                "Brindle (kbrkbr, kbrky)",
                "",
                """Brindle adds eumelanin stripes over the pattern coded
by the A locus.
The width of the stripes ranges, but it's unknown
what modifiers (if any) affect it.""",
            ),
            (
                "Phaeomelanin expression (kyky)",
                "",
                """ky allows phaeomelanin expression in the coat,
letting the coat show the pattern coded by the
A locus.""",
            ),
            (
                "Seal and ghost tan (KBky)*",
                ("seal", "ghost tan"),
                """There are two more patterns connected to this locus:
"seal" and "ghost tan".
They appear to happen only in KBky dogs, possibly
with an additional modifier gene involved. It seems
like the dominant black doesn't fully cover up the 
A locus, allowing it to shine through.
Seal dogs are sables at the A locus. They often have
dark faces, ears and tails, and a dark stripe along
the back.
Ghost tan dogs are tan points at the A locus.""",
            ),
        ),
    ),
    "A": (
        """The alleles at the A locus affect the dog's pattern.
They deterime the distribution of phaeomelanin and 
eumelanin-colored hairs in the coat.
Each hair may have one or both colors at a time, and 
together they create the pattern.""",
        (
            (
                "Clear sable (Ay)",
                "",
                """"Clear sable" is a coat pattern made up of
phaeomelanin, with little to no eumelanin-tipped 
hairs.
Sometimes clear sable puppies may be born with
some shading, like shaded sables, but it fades 
when the adult coat grows in.
Clear sables may appear really similar to recessive
red dogs (see E locus page), the difference being the 
color of the whiskers: dark for clear sables and pale 
for recessive reds.""",
            ),
            (
                "Shaded sable (Ays)",
                "",
                """"Shaded sable" is a coat pattern of 
eumelanin-tipped hairs on phaeomelanin base. 
The shading usually covers the top of the dog's head, 
the back of the neck and the tail, leaving out the legs.
On the forehead, many sable dogs have a "widow's 
peak".
Intensity of the shading may vary from low (the hairs 
with more phaeomelanin) where black over orange 
appears brown, to high (the hairs with more 
eumelanin) where the shaded area has the color of 
eumelanin. 
The intensity can vary within the pattern, giving the 
shaded area a blurred edge.
If the dog looks similar to a shaded sable but has
tipped hairs on the front legs, markings under the 
eyes, or a nose bar instead of the widow's peak, 
it might be an agouti (see below).
Shaded sable puppies may be born with dark-ish
coats, but the color fades when the adult coat 
grows in.""",
            ),
            (
                "Agouti (aw)",
                "",
                """"Agouti" or "wolf sable" is a coat pattern of 
eumelanin-tipped hairs on phaeomelanin base.
Most of the hairs hairs have both phaeomelanin and 
eumelanin on them, as well as dark tips. 
It is found it wild animals, including wolves.
Agouti creates a dark pattern over the top of the 
dog's body, leaving out phaeomelanin markings on 
the eyebrows, cheeks, chroat, chest, belly and legs, 
creating a dark nose bar and markings under the 
eyes.
The intensity of the hair banding varies within one 
pattern, making it appear unevenly colored.""",
            ),
            (
                "Saddle and creeping tan (asa)",
                "",
                """"Saddle tan" and "creeping tan" are coat patterns 
of eumelanin-tipped hairs on phaeomelanin base.
Puppies with these patterns are born with tan points 
(see below), but as they grow older some eumelanin 
hairs are replaced with phaeomelanin.
Saddle tan has eumelanin left on the neck and the 
back, leaving out the legs.
Creeping tan is anything between a tan point and a 
saddle.
In general, the eumelanin areas on dogs with saddles
and creeping tan are more solid than they are on
shaded sables.""",
            ),
            (
                "Tan point (at)",
                "",
                """Tan point is a coat pattern made up of eumelanin
with symmetrical phaeomelanin markings.
The markings include pips above the eyes, sides of 
the muzzle, pips on the cheeks, below the head, two
triangular patches on the chest, bottom of the legs
and sometimes the bottom side of the tail.
There may be small eumelanin marks on the toes, 
called "pencilling".
Unlike with other patterns, on tan pointed dogs the 
color of eumelanin is pretty even.
The markings on a tan pointed dog can be covered up 
with intense masking (see E locus page).""",
            ),
            (
                "Recessive black (aa)",
                "",
                """aa, also referred to as "recessive black", creates a 
solid eumelanin coat.
Despite the name, the coat doesn't have to be black;
it has the color of the dog's eumelanin, whichever
it might be.""",
            ),
        ),
    ),
    "E": (
        """The alleles at the E locus affect the dog's pattern,
specifically the phaeomelanin. They modify patterns
from the A locus, adding some eumelanin (masks) or
removing it (recessive red).""",
        (
            (
                "Masking (Em)",
                "",
                """Em adds a eumelanin mask over any A locus pattern.
The mask typically covers the muzzle (ranging from 
only the tip to reaching the eyes) and sometimes the
ears.
There is also "extreme" masking, which adds shading
to the chest, the legs and the tail. In these dogs,
the mask can cover the entire face.""",
            ),
            (
                "Extreme masking",
                "masked",
                """"Extreme" masking is modified masking, which adds
shading to the chest, the legs and the tail. 
In these dogs, the mask can cover up the entire face.""",
            ),
            (
                "Normal expression (EE, Ee)",
                "",
                "The dog is unaffected.",
            ),
            (
                "Recessive red (ee)",
                "",
                """ee, also referred to as "recessive red", creates a 
solid phaeomelanin coat by making the dog unable to
produce eumelanin in the fur. Unlike clear sables 
(see A locus page), these dogs have pale whiskers.
Despite the name, the coat doesn't have to be red;
it has the color of the dog's phaeomelanin, whichever
it might be.
Since these is no eumelanin in these dogs, recessive
red can easily cover up the merle alleles and lead to 
accidental breeding of two merles. The only signs
could be merling on the eyes and the nose, but they
are not always present in merles.
Sometimes a recessive red cell mutates and starts to
produce eumelanin. It may appear like a small patch
or a large area (depending on how early in
development the mutation happened) of eumelanin.""",
            ),
            (
                "Domino, grizzle, cocker sable",
                "",
                """These alleles are also at the E locus, but are not 
mentioned in the coat editor, because they're not yet
fully studied and it is impossible to accurately 
predict the results of combining them.
Ancient domino ("northern domino") (eA or eD) is
common in northern and breeds like huskies, laikas 
or malamutes. It lightens the color of phaeomelanin
and makes the phaeomelanin areas created by the 
A locus larger. It also often adds a light stripe 
down the middle of the nose.
Grizzle ("sighthound domino") is found in sighthound 
breeds. It acts similarly to northern domino, 
lightening the phaeomelann and making the 
phaeomelanin areas larger.
"Cocker sable" appears in cocker spaniels. It gives
them a sable-like pattern, even though their A locus
is fixed for tan points.""",
            ),
        ),
    ),
    "M": (
        """Merle is caused by SINE insertion in the PMEL gene at
the M locus.
Merle dilutes random patches of eumelanin in the
entire dog to a paler color or white, keeping the rest
of it intact. Often there are also patches of a third
color, darker than the dilute and ligher than the 
non-dilute shades.
That doesn't only affect the fur color: it also changes 
the colors of the eyes, nose and paw pads.
Placement of the patches is unique to each dog.""",
        (
            (
                "Non-merle (mm)",
                "",
                """The dog is unaffected.""",
            ),
            (
                "Merle (Mm)",
                "patch size 2",
                """All eumelanin in the fur (if any is present) is merled.
The nose and paw pads may be merled, leaving
patches of dark color and diluting the rest to pink.
The eyes may be merled too, diluting some parts of
the eyes to light blue. It can be sections of an eye,
a whole eye, or even both eyes.
Because merle patching is random, the nose, paw pad
and eye dilution may not be present at all.""",
            ),
            (
                "Double merle (MM) (!)",
                "double",
                """All eumelanin in the fur (if any is present) is merled.
Both eumelanin and phaeomelanin in the most of
the body is diluted to white, with non-white merled
areas remaining on the top of the head, the back, and
the base of the tail. Some double merles are fully
white.
The nose and paw pads are merled, and are mostly
or fully pink.
The eyes are merled, and are often mostly or fully
blue.
(!) Double merle patterns are connected with eye
defects (such as blindness, jagged or dropped pupils,
small eyes) of deafness. They are also more 
sensitive to sun and have higher risks of skin
cancer.
Because of this, breeding two merle (Mm) dogs, which
might result in a double merle situation, is
discouraged. The safe way is to breed a merle (Mm)
with a non-merle (mm).""",
            ),
            (
                "Patching variation",
                ("patch size 1", "patch size 2", "patch size 4"),
                """Amount of patching can vary from a few small
patches to almost fully covering up the dilution.
The pattern preferred in breed standards has the
amount of dark color and dilution split evenly, 
about 50/50.
High patching is discouraged, because it can fully hide 
the merle.""",
            ),
            (
                "Base color variation",
                ("intensity 1", "patch size 2", "intensity 3"),
                """Base color (the color of dilution) can vary
from very pale to almost as dark as the patch color.""",
            ),
            (
                "Advanced merle genetics",
                "",
                """For simplicity's sake, I am only talking about M and m
alleles here. In reality though, genetic testing shows
there are 7 alleles with different SINE insertion
lengths, along with the mentioned two including
cryptic, atypical and harlequin merle alleles.
The discovery is fairly recent, and the results of 
combining these are harder to predict.
Combinations with atypical merle can create patterns
like "maltese merle", "muddy merle" and "tweed".
Combinations with harlequin merle can dilute both
eumelanin and phaeomelanin to full white. It can also
partially dilute phaeomelanin, allowing the dark merle
patches to be visible "through" it.""",
            ),
            (
                "Mosaicism",
                "",
                """The merle gene is unstable, and sometimes it can
mutate during development, causing the shortening
of SINE insertion (the longer the insertion, the more
merle) in one of the cells.
As the cells split to make more cells, the dog
develops having an area with a different genotype.
This is called mosaicism.
If this happens in the fur, the dog might have a 
differently colored patch of fur. If this happens in the 
reproductive cells, the dog might pass the new
mutant allele to its puppies.""",
            ),
        ),
    ),
    "H": (
        """Great Dane Harlequin is a modifier of merle, turning 
all the dilute areas of the dog to white, instead of 
the dilute color. These white areas also cover up the
phaeomelanin in the coat.
If the dog is not a merle, harlequin will not affect it 
in any way.
This mutation specific to Great Danes, and is 
different from the M locus "harlequin" allele.""",
        (
            (
                "Non-harlequin (hh)",
                "",
                "The dog is unaffected.",
            ),
            (
                "Harlequin merle (Hh)",
                "harlequin",
                """All pigment outside the dark color merle patches, 
including phaeomelanin, is diluted to white.""",
            ),
            (
                "Embryonic lethal (HH)",
                "",
                """There are no known HH harlequin dogs. Supposedly, 
it is embryonic lethal — any HH puppy is reabsorbed
in the womb and never born.""",
            ),
        ),
    ),
    "S": (
        """The S locus creates white areas on the coat. 
In these areas, neither eumelanin nor phaeomelanin 
is produced.
The two known alleles (S and si) don't cover the 
entire range of white spotting patterns. There are two 
more theoretical alleles: si (irish spotting) and 
sw (extreme piebald), but theis existence hasn't 
been proven yet.
It's possible that the amount and pattern of white is
controlled by some not yet known modifiers.""",
        (
            (
                "Solid coat (SS)",
                "",
                "The dog is uneffected.",
            ),
            (
                "White spotted (Ssp)",
                "",
                """The coat has some white spotting.
The white spotting starts with the muzzle, the tip of
the tail and the paws, and spreads to the chest area, 
belly and forehead in dog with more white.""",
            ),
            (
                "Piebald (spsp) (!)",
                "",
                """The coat is predominantly or completely white.
As the white spotting spreads, the color tends to
remain around the ears and at the base of the tail.
It can disappear from there as well, if there is more 
white.
High white spotting can make the dog's eyes blue,
and the nose partly or fully pink due to the lack of 
pigment.
When a large amount of white is removed from the 
face and ears, it can lead to deafness.""",
            ),
            (
                "Irish spotting",
                "irish",
                """Irish spotting ("boston" or "mantle") is a pattern of
white on the legs, tip of the tail, chest, neck and
muzzle.
Ssp dogs can look like that, too, but the results of 
breeding true irish spotted dogs show that this is a
separate allele.
It is not yet known whether it is on the same locus
as sp or not.""",
            ),
            (
                "Whitehead",
                "",
                """There appears to be a different mutation responsible 
for white patching that starts with the head (unlike 
piebald which starts with the lower body).""",
            ),
        ),
    ),
    "T": (
        """Ticking and roan cause pigmented hairs to grow on 
the areas of the coat that are spotted white 
(see S locus).
It's basically "holes" in the white pattern, showing
what the coat would look like if there was no white 
there.
Puppies with ticking and roan are born with clear
white, and the color appears as the adult coat grows 
in.""",
        (
            (
                "Roan (TRTR, TRT, TRt)",
                "",
                """Roan adds pigmented hairs to the entire body 
without forming any clear spots.
Roan ranges from moderate (clearer white) to heavy 
(clearer pigment, can even appear like it isn't spotted 
white at all).""",
            ),
            (
                "Ticking (TT, Tt)",
                "",
                """Ticking adds small pigmented spots, like freckles.
Ticking ranges from moderate (spots on the legs and 
the muzzle) to heavy (spots on the entire body).
If the fur is long, the spots will be blurred.""",
            ),
            ("No effect (tt)", "", "The dog is uneffected."),
        ),
    ),
    "F": (
        """Flecking is a modifier of roan found in dalmatians.
Compared to ticking, the dalmatian spots are larger, 
rounder and more evenly distributed. Also, they have
solid pigment, unlike ticking which may have some 
white hairs in the spots.
Like roan and ticking, it creates a pattern of spots 
over the white spotting which appears when the dog's
adult coat grows in.""",
        (
            ("No flecking (FF, Ff)", "", "The dog is uneffected."),
            (
                "Dalmatian flecking (ff)",
                "",
                """The dog is flecked.
All dalmatians are TR, so it is assumed that it
modifies speficically roan and not ticking.
In reality, maybe it does both.""",
            ),
        ),
    ),
}

##### IMAGES #####


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
