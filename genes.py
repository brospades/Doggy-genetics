import customtkinter as ctk
from PIL import Image, ImageTk


##### IMAGES #####

save_icon = ctk.CTkImage(light_image=Image.open("images/icon-save.png"), size=(25, 25))
reload_icon = ctk.CTkImage(light_image=Image.open("images/icon-save-reload.png"), size=(25, 25))


EU = (  # eu layer images
    "none",
    "black",
    "liver",
    "blue",
    "isabella",
    "black merle",
    "liver merle",
    "blue merle",
    "isabella merle",
)
PHAEO = (
    "none none",
    "red none",
    "yellow none",
    "cream none",
    "none eu",
    "red eu",
    "yellow eu",
    "cream eu",
    "red solid",
    "yellow solid",
    "cream solid",
    "none shaded",
    "red shaded",
    "yellow shaded",
    "cream shaded",
    "none agouti",
    "red agouti",
    "yellow agouti",
    "cream agouti",
    "none saddle",
    "red saddle",
    "yellow saddle",
    "cream saddle",
    "none creeping tan",
    "red creeping tan",
    "yellow creeping tan",
    "cream creeping tan",
    "none tan",
    "red tan",
    "yellow tan",
    "cream tan",
    "domino agouti",
    "domino saddle",
    "domino shaded",
    "domino tan",
)
MASK = (
    "none",
    "none brindle",
    "black brindle",
    "liver brindle",
    "blue brindle",
    "isabella brindle",
    "black merle brindle",
    "liver merle brindle",
    "blue merle brindle",
    "isabella merle brindle",
    "mask black",
    "mask liver",
    "mask blue",
    "mask isabella",
    "mask black merle",
    "mask liver merle",
    "mask blue merle",
    "mask isabella merle",
)
WHITE = (
    "",
    "mid",
    "mid roan",
    "mid mottled roan",
    "mid ticked",
    "mid flecked",
    "high",
    "high roan",
    "high mottled roan",
    "high ticked",
    "high flecked",
    "harlequin",
    "double merle",
    "double merle harlequin",
)


outline = Image.open("images/coat_editor-outline.png").convert("RGBA")

# Dictionaries of color images
eu_pics = {}
phaeo_pics = {}
mask_pics = {}
white_pics = {}

# Tuple for generating Image objects
image_search_list = (
    ("eu", EU, eu_pics),
    ("phaeo", PHAEO, phaeo_pics),
    ("mask", MASK, mask_pics),
    ("white", WHITE, white_pics),
)
# Generate Image objects for all images in name_list constants
for layer_type, name_list, dict_name in image_search_list:
    for img_name in name_list:
        color = Image.open(f"images/coat_editor-{layer_type}-{img_name}.png").convert(
            "RGBA"
        )
        dict_name[img_name] = color


##### LOCUSES #####
# Dictionaries of results for each allele combination with a result
class Locus:
    "Locuses"

    def __init__(self, proper_name, letter, results):
        self.proper_name = proper_name
        self.letter = letter
        self.results = results


LocusB = Locus(
    "Black and liver [B locus]",
    "B",
    {
        frozenset({"_"}): ("[color of eumelanin]", "__", None),  # unknown
        frozenset({"B", "_"}): ("black eumelanin", "B_", "black"),
        frozenset({"b", "_"}): ("[color of eumelanin]", "b_", None),  # unknown
        frozenset({"B"}): ("black eumelanin", "BB", "black"),
        frozenset({"b"}): ("liver eumelanin", "bb", "liver"),
        frozenset({"B", "b"}): ("black eumelanin", "Bb", "black"),
    },
)

LocusD = Locus(
    "Eumelanin dilution [D locus]",
    "D",
    {
        frozenset({"_"}): ("[eumelanin dilution]", "__", None),  # unknown
        frozenset({"D", "_"}): ("non-diluted eumelanin", "D_", "non"),
        frozenset({"d", "_"}): ("[eumelanin dilution]", "d_", None),  # unknown
        frozenset({"D"}): ("non-diluted eumelanin", "DD", "non"),
        frozenset({"d"}): ("diluted eumelanin", "dd", "dilute"),
        frozenset({"D", "d"}): ("non-diluted eumelanin", "Dd", "non"),
    },
)

LocusI = Locus(
    "Phaeomelanin intensity [I locus]",
    "I",
    {
        frozenset({"_"}): ("[phaeomelanin intensity]*", "__", None),
        frozenset({"I", "_"}): ("[phaeomelanin intensity]*", "I_", None),
        frozenset({"i", "_"}): ("[phaeomelanin intensity]*", "i_", None),
        frozenset({"I"}): ("non-diluted phaeomelanin*", "II", "red"),
        frozenset({"i"}): ("diluted phaeomelanin*", "ii", "cream"),
        frozenset({"I", "i"}): ("diluted phaeomelanin*", "Ii", "yellow"),
    },
)

LocusK = Locus(
    "Brindle [K locus]",
    "K",
    {
        frozenset({"_"}): ("[brindle]", "__", None),  # unknown
        frozenset({"KB", "_"}): ("solid eumelanin", "KB_", "solid"),
        frozenset({"kbr", "_"}): ("[brindle]", "kbr_", None),  # unknown
        frozenset({"ky", "_"}): ("[brindle]", "ky_", None),  # unknown
        frozenset({"KB"}): ("solid eumelanin", "KBKB", "solid"),
        frozenset({"kbr"}): ("brindle over pattern", "kbrkbr", "brindle"),
        frozenset({"ky"}): ("pattern visible", "kyky", "clear"),
        frozenset({"KB", "kbr"}): ("solid eumelanin", "KBkbr", "solid"),
        frozenset({"KB", "ky"}): ("solid eumelanin*", "KBky", "solid"),
        frozenset({"kbr", "ky"}): ("brindle over pattern", "kbrky", "brindle"),
    },
)

LocusA = Locus(
    "Sable, agouti, tan point [A locus]",
    "A",
    {
        frozenset({"_"}): ("[sable, agouti or tan]", "__", None),  # unknown
        frozenset({"Ay", "_"}): ("clear sable", "Ay_", "solid"),
        frozenset({"Ays", "_"}): ("[sable, agouti or tan]", "Ays_", None),
        frozenset({"aw", "_"}): ("[sable, agouti or tan]", "aw_", None),
        frozenset({"asa", "_"}): ("[sable, agouti or tan]", "asa_", None),
        frozenset({"at", "_"}): ("[sable, agouti or tan]", "at_", None),
        frozenset({"a", "_"}): ("[sable, agouti or tan]", "a_", None),
        frozenset({"Ay"}): ("clear sable", "AyAy", "solid"),
        frozenset({"Ays"}): ("shaded sable", "AysAys", "shaded"),
        frozenset({"aw"}): ("agouti", "awaw", "agouti"),
        frozenset({"asa"}): ("saddle", "asaasa", "saddle"),
        frozenset({"at"}): ("tan point", "atat", "tan"),
        frozenset({"a"}): ("solid eumelanin", "aa", "eu"),
        frozenset({"Ay", "Ays"}): ("clear sable", "AyAys", "solid"),
        frozenset({"Ay", "aw"}): ("clear sable", "Ayaw", "solid"),
        frozenset({"Ay", "asa"}): ("clear sable", "Ayasa", "solid"),
        frozenset({"Ay", "at"}): ("clear sable", "Ayat", "solid"),
        frozenset({"Ay", "a"}): ("clear sable", "Aya", "solid"),
        frozenset({"Ays", "aw"}): ("shaded sable", "Aysaw", "shaded"),
        frozenset({"Ays", "asa"}): ("shaded sable", "Aysasa", "shaded"),
        frozenset({"Ays", "at"}): ("shaded sable", "Aysat", "shaded"),
        frozenset({"Ays", "a"}): ("shaded sable", "Aysa", "shaded"),
        frozenset({"aw", "asa"}): ("agouti", "awasa", "agouti"),
        frozenset({"aw", "at"}): ("agouti", "awat", "agouti"),
        frozenset({"aw", "a"}): ("agouti", "awa", "agouti"),
        frozenset({"asa", "at"}): ("creeping tan", "asaat", "creeping tan"),
        frozenset({"asa", "a"}): ("creeping tan", "asaa", "creeping tan"),
        frozenset({"at", "a"}): ("tan point", "ata", "tan"),
    },
)

LocusE = Locus(
    "Masking, recessive red [E locus]",
    "E",
    {
        frozenset({"_"}): ("[masking, recessive red]", "__", None),
        frozenset({"Em", "_"}): ("masked", "Em_", "mask"),
        frozenset({"E", "_"}): ("[masking, recessive red]", "E_", None),
        frozenset({"e", "_"}): ("[masking, recessive red]", "e_", None),
        frozenset({"Em"}): ("masked", "EmEm", "mask"),
        frozenset({"E"}): ("no effect", "EE", None),
        frozenset({"e"}): ("recessive red", "ee", "rec red"),
        frozenset({"Em", "E"}): ("masked", "EmE", "mask"),
        frozenset({"Em", "e"}): ("masked", "Eme", "mask"),
        frozenset({"E", "e"}): ("no effect", "Ee", None),
    },
)


LocusM = Locus(
    "Merle [M locus]",
    "M",
    {
        frozenset({"_"}): ("[merle]", "__", None),
        frozenset({"M", "_"}): ("[merle]", "M_", None),
        frozenset({"m", "_"}): ("[merle]", "m_", None),
        frozenset({"M"}): ("double merle (!)", "MM", "double merle"),
        frozenset({"m"}): ("non-merle", "mm", None),
        frozenset({"M", "m"}): ("merle", "Mm", "merle"),
    },
)

LocusH = Locus(
    "Harlequin merle [H locus]",
    "H",
    {
        frozenset({"_"}): ("[harlequin merle]", "__", None),
        frozenset({"H", "_"}): ("[harlequin merle]", "H_", None),
        frozenset({"h", "_"}): ("[harlequin merle]", "h_", None),
        frozenset({"H"}): ("embryonic lethal (!)", "HH", "dead"),
        frozenset({"h"}): ("non-harlequin", "hh", None),
        frozenset({"H", "h"}): ("harlequin merle", "Hh", "harlequin"),
    },
)

LocusS = Locus(
    "White spotting [S locus]",
    "S",
    {
        frozenset({"_"}): ("[white spotting]", "__", None),
        frozenset({"S", "_"}): ("[white spotting]", "S_", None),
        frozenset({"sp", "_"}): ("[white spotting]", "sp_", None),
        frozenset({"S"}): ("solid coat", "SS", None),
        frozenset({"sp"}): ("piebald", "spsp", "high"),
        frozenset({"S", "sp"}): ("white spotted", "Ssp", "mid"),
    },
)

LocusT = Locus(
    "Ticking and roan [T locus]",
    "T",
    {
        frozenset({"_"}): ("[ticking and roan]", "__", None),
        frozenset({"TR", "_"}): ("[ticking and roan]", "TR_", None),
        frozenset({"T", "_"}): ("[ticking and roan]", "T_", None),
        frozenset({"t", "_"}): ("[ticking and roan]", "t_", None),
        frozenset({"TR"}): ("roan", "TRTR", "roan"),
        frozenset({"T"}): ("ticked", "TT", "ticked"),
        frozenset({"t"}): ("clear white", "tt", None),
        frozenset({"TR", "T"}): ("mottled roan", "TRT", "mottled roan"),
        frozenset({"TR", "t"}): ("roan", "TRt", "roan"),
        frozenset({"T", "t"}): ("ticked", "Tt", "ticked"),
    },
)

LocusF = Locus(
    "Dalmatian flecking [F locus]",
    "F",
    {
        frozenset({"_"}): ("[dalmatian flecking]", "__", None),
        frozenset({"F", "_"}): ("no flecking", "F_", None),
        frozenset({"f", "_"}): ("[dalmatian flecking]", "f_", None),
        frozenset({"F"}): ("no flecking", "FF", None),
        frozenset({"f"}): ("flecked", "ff", "flecked"),
        frozenset({"F", "f"}): ("no flecking", "Ff", None),
    },
)


# Locus names
locus_names = (
    LocusB,
    LocusD,
    LocusI,
    LocusK,
    LocusA,
    LocusE,
    LocusM,
    LocusH,
    LocusS,
    LocusT,
    LocusF,
)

##### COAT EDITOR #####
# Genes list
genes_list = [
    (
        "Pigment shade",
        (
            (LocusB, ["_", "B", "b"]),
            (LocusD, ["_", "D", "d"]),
            (LocusI, ["_", "I", "i"]),
        ),
    ),
    (
        "Pattern",
        (
            (LocusK, ["_", "KB", "kbr", "ky"]),
            (LocusA, ["_", "Ay", "Ays", "aw", "asa", "at", "a"]),
            (LocusE, ["_", "Em", "E", "e"]),
        ),
    ),
    (
        "Merle and white spotting",
        (
            (LocusM, ["_", "M", "m"]),
            (LocusH, ["_", "H", "h"]),
            (LocusS, ["_", "S", "sp"]),
        ),
    ),
    (
        "Theoretical",
        (
            (LocusT, ["_", "TR", "T", "t"]),
            (LocusF, ["_", "F", "f"]),
        ),
    ),
]

# List of genes that need to be reset in coat editor
replacement_list = {
    LocusB: "B",
    LocusD: "D",
    LocusI: "I",
    LocusK: "ky",
    LocusA: "Ays",
}

##### ALLELE COMBINATIONS #####
# Visual presentation of all combinations of alelles

eumelanin_shade = {
    "blacknon": "black",
    "livernon": "liver",
    "blackdilute": "blue",
    "liverdilute": "isabella",
}
