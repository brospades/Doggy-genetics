import customtkinter as ctk
from PIL import Image

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

# For editors
save_icon = ctk.CTkImage(light_image=Image.open("images/icon-save.png"), size=(25, 25))
reload_icon = ctk.CTkImage(
    light_image=Image.open("images/icon-save-reload.png"), size=(25, 25)
)

# For lists
delete_icon = ctk.CTkImage(
    light_image=Image.open("images/icon-delete.png"), size=(20, 20)
)
