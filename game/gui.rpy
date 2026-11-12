## gui.rpy — Struk Terakhir Pukul 02.14
## GUI minimal untuk Ren'Py 8.5.3. Sesuaikan warna/font di sini.

init offset = -2

init python:
    gui.init(1280, 720)

# --- Warna ---
define gui.accent_color = "#3a7d7c"      # teal SegarMart / hijab Alya
define gui.idle_color = "#888888"
define gui.idle_small_color = "#aaaaaa"
define gui.hover_color = "#c8a86a"        # amber hangat (lampu toko)
define gui.selected_color = "#ffffff"
define gui.insensitive_color = "#8888887f"
define gui.muted_color = "#512a2a"
define gui.hover_muted_color = "#7a4a4a"
define gui.text_color = "#ffffff"
define gui.interface_text_color = "#ffffff"

# --- Font ---
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size = 24
define gui.name_text_size = 26
define gui.interface_text_size = 22
define gui.label_text_size = 24
define gui.notify_text_size = 16
define gui.title_text_size = 48

# --- Kotak dialog ---
define gui.textbox_height = 185
define gui.textbox_yalign = 1.0
define gui.name_xpos = 240
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.text_xpos = 268
define gui.text_ypos = 12
define gui.text_width = 744
define gui.text_xalign = 0.0

# --- Tombol ---
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

# --- Pilihan (choice) ---
define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"

# --- Variabel yang dipakai screens.rpy ---
define gui.namebox_width = 220
define gui.namebox_height = 50
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False
define gui.choice_spacing = 10
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
define gui.slot_spacing = 10
define gui.page_spacing = 10
define gui.pref_spacing = 10
define gui.navigation_xpos = 40
define gui.navigation_spacing = 10
define gui.history_height = None
define gui.history_allow_tags = set()
define gui.about = "Visual novel misteri ringan — SegarMart Antapani, Bandung, Oktober 2020."
define gui.language = "unicode"

# --- Lainnya ---
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define gui.main_menu_background = "#1a2a2a"
define gui.game_menu_background = "#1a2a2a"
