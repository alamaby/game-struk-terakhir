## screens.rpy — Struk Terakhir Pukul 02.14
## Layar minimal untuk Ren'Py 8.5.3 (say, choice, menu, save/load, preferensi).
## Kalau Ren'Py Launcher membuat proyek baru, file ini boleh diganti
## dengan screens.rpy bawaan Launcher — script.rpy tetap jalan.

init offset = -1

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")

## --- Layar dialog (say) ---
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Solid("#000000cc")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Solid("#3a7d7c")
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.text_xpos
    xsize gui.text_width
    ypos gui.text_ypos
    adjust_spacing False

## --- Layar pilihan ---
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action

define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "audio/click.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## --- Menu utama ---
screen main_menu():
    tag menu
    add gui.main_menu_background
    frame:
        pass
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        text "Struk Terakhir Pukul 02.14" size 48 xalign 0.5
        text "SegarMart Antapani tutup pukul 22.00. Selalu." size 20 xalign 0.5
        textbutton _("Mulai") action Start()
        textbutton _("Muat") action ShowMenu("load")
        textbutton _("Pengaturan") action ShowMenu("preferences")
        textbutton _("Keluar") action Quit(confirm=False)

## --- Menu dalam game ---
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            spacing spacing
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude
                else:
                    transclude
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        if main_menu:
            textbutton _("Mulai") action Start()
        else:
            textbutton _("Riwayat") action ShowMenu("history")
            textbutton _("Simpan") action ShowMenu("save")
        textbutton _("Muat") action ShowMenu("load")
        textbutton _("Pengaturan") action ShowMenu("preferences")
        if _in_replay:
            textbutton _("Akhiri Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Menu Utama") action MainMenu()
        textbutton _("Tentang") action ShowMenu("about")
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Bantuan") action ShowMenu("help")
        if renpy.variant("pc"):
            textbutton _("Keluar") action Quit(confirm=not main_menu)

screen save():
    tag menu
    use file_slots(_("Simpan"))

screen load():
    tag menu
    use file_slots(_("Muat"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Simpan Otomatis"), quick=_("Simpan Cepat"))
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("slot kosong")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

screen preferences():
    tag menu
    use game_menu(_("Pengaturan"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Tampilan")
                        textbutton _("Jendela") action Preference("display", "window")
                        textbutton _("Layar Penuh") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("Rollback")
                    textbutton _("Nonaktif") action Preference("rollback side", "disable")
                    textbutton _("Kiri") action Preference("rollback side", "left")
                    textbutton _("Kanan") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("Lewati")
                    textbutton _("Teks Belum Dibaca") action Preference("skip", "toggle")
                    textbutton _("Setelah Pilihan") action Preference("after choices", "toggle")
                    textbutton _("Transisi") action InvertSelected(Preference("transitions", "toggle"))
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Kecepatan Teks")
                    bar value Preference("text speed")
                    label _("Auto-Forward")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Volume Musik")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Volume Suara")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Tes") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Volume Suara Karakter")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Tes") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Bisukan Semua"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

screen history():
    tag menu
    predict False
    use game_menu(_("Riwayat"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("Bantuan"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 15
            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Memajukan dialog dan mengaktifkan antarmuka.")
    hbox:
        label _("Spasi")
        text _("Memajukan dialog tanpa memilih pilihan.")
    hbox:
        label _("Tombol Panah")
        text _("Menavigasi antarmuka.")
    hbox:
        label _("Esc")
        text _("Mengakses menu game.")
    hbox:
        label _("Ctrl")
        text _("Menahan untuk melewati dialog.")
    hbox:
        label _("Tab")
        text _("Mengaktifkan/menonaktifkan skip.")
    hbox:
        label _("Page Up")
        text _("Rollback ke dialog sebelumnya.")
    hbox:
        label _("Page Down")
        text _("Roll forward ke dialog berikutnya.")
    hbox:
        label _("H")
        text _("Menyembunyikan antarmuka pengguna.")
    hbox:
        label _("S")
        text _("Mengambil screenshot.")
    hbox:
        label _("V")
        text _("Mengaktifkan/menonaktifkan voice.")
    hbox:
        label _("Shift+A")
        text _("Membuka menu aksesibilitas.")

screen mouse_help():
    hbox:
        label _("Klik Kiri")
        text _("Memajukan dialog dan mengaktifkan antarmuka.")
    hbox:
        label _("Klik Tengah")
        text _("Menyembunyikan antarmuka pengguna.")
    hbox:
        label _("Klik Kanan")
        text _("Mengakses menu game.")
    hbox:
        label _("Roda Mouse Ke Atas")
        text _("Rollback ke dialog sebelumnya.")
    hbox:
        label _("Roda Mouse Ke Bawah")
        text _("Roll forward ke dialog berikutnya.")

screen gamepad_help():
    hbox:
        label _("Right Trigger\nA / Tombol Bawah")
        text _("Memajukan dialog dan mengaktifkan antarmuka.")
    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rollback ke dialog sebelumnya.")
    hbox:
        label _("Right Shoulder")
        text _("Roll forward ke dialog berikutnya.")
    hbox:
        label _("D-Pad, Stik")
        text _("Menavigasi antarmuka.")
    hbox:
        label _("Start, Guide, B / Tombol Kanan")
        text _("Mengakses menu game.")
    hbox:
        label _("Y / Tombol Atas")
        text _("Menyembunyikan antarmuka pengguna.")

screen about():
    tag menu
    use game_menu(_("Tentang"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Versi [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Dibuat dengan {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Ya") action yes_action
                textbutton _("Tidak") action no_action
    key "game_menu" action no_action

screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!t]"
    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
