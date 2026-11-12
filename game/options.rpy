## options.rpy — Struk Terakhir Pukul 02.14
## Ren'Py 8.5.3

define config.name = _("Struk Terakhir Pukul 02.14")
define config.version = "0.1.0-scaffold"
define gui.show_name = True

# 16:9, sesuai outline.
define config.screen_width = 1280
define config.screen_height = 720

define config.window_title = _("Struk Terakhir Pukul 02.14")

# Build: nama file distribusi.
define build.name = "struk-terakhir-0214"

# Bahasa Indonesia.
define config.language = "indonesian"

## Build distributions — aktifkan di Ren'Py Launcher > Build Distributions.
## Web masih beta di Ren'Py 8, tes dulu sebelum dirilis.
init python:
    build.classify_0("**/*.png", "archive")
    build.classify_0("**/*.jpg", "archive")
    build.classify_0("**/*.webp", "archive")
    build.classify_0("**/*.ogg", "archive")
    build.classify_0("**/*.mp3", "archive")
    build.classify_0("**/*.rpy", "archive")
    build.classify_0("**/*.rpyc", "archive")
    build.documentation("*.html")
    build.documentation("*.txt")
