import customtkinter as ctk

# Master
WINDOW_BG = ("#EBEBEB", "#202020")
HEADER_BG = ("#F5F5F5", "#252526")
SIDEBAR_BG = ("#ECECEC", "#2D2D30")
CONTENT_BG = ("#FFFFFF", "#313131") 
BORDER = ("#D6D6D6", "#3C3C3C")
ACCENT = ("#0078D4", "#4CC2FF")
TEXT = ("#202020", "#F0F0F0")
TEXT_SECONDARY = ("#666666", "#AAAAAA")

# Sidebar
SIDEBAR_BTN_FG = "transparent"
SIDEBAR_BTN_HOVER = ("#DDDDDD", "#383838")
SIDEBAR_BTN_SELECTED = ACCENT

SIDEBAR_BTN_TEXT = TEXT
SIDEBAR_BTN_TEXT_DISABLED = TEXT_SECONDARY

# General Spacing (Legacy)
# SPACE_XL = 10
# SPACE_L = 8
# SPACE = 5
# SPACE_S = 2


# Window / Frame spacing
WINDOW_PAD = 5     # Gap from window edge
FRAME_GAP = 2   # Half of gap between adjacent frames

CARD_INSET = 5      # gap between a page's own frame and its parent frame,
# so the parent's rounded corner stays visible. Mainly for page to content frame padding

# Header
HEADER_LEFT_BTN_PADX = (WINDOW_PAD, FRAME_GAP)
HEADER_RIGHT_BTN_PADX = (FRAME_GAP, WINDOW_PAD)
HEADER_BTN_PADY = WINDOW_PAD

# Sidebar
SIDEBAR_BTN_PADX = WINDOW_PAD
SIDEBAR_BTN_PADY = FRAME_GAP

# Content
CONTENT_PAD = 10

# Padding y
PAGE_TOP = (WINDOW_PAD, FRAME_GAP)
SECTION = (0, FRAME_GAP)
PAGE_BOTTOM = (0, WINDOW_PAD)

# Padding X
PAGE_SIDES = WINDOW_PAD

# Note for future

# PAGE_PAD_X = 16
# PAGE_PAD_Y = 16
# 
# SECTION_GAP = 8

# PAGE_TOP = (PAGE_PAD_Y, SECTION_GAP)
# SECTION = (0, SECTION_GAP)
# PAGE_BOTTOM = (0, PAGE_PAD_Y)

# Fonts
TITLE_FONT = None
HEADING_FONT = None
BODY_FONT = None
SMALL_FONT = None
BUTTON_FONT = None
SMALL_HEADING_FONT = None

def init_fonts():
    global TITLE_FONT, HEADING_FONT, BODY_FONT, SMALL_FONT, BUTTON_FONT, SMALL_HEADING_FONT

    TITLE_FONT = ctk.CTkFont(
        family="League Spartan",
        size=28,
        weight="bold"
    )

    HEADING_FONT = ctk.CTkFont(
        family="League Spartan",
        size=20,
        weight="bold"
    )

    SMALL_HEADING_FONT = ctk.CTkFont(
        family="League Spartan",
        size=15,
        weight="normal"
    )

    BODY_FONT = ctk.CTkFont(
        family="League Spartan",
        size=14
    )

    SMALL_FONT = ctk.CTkFont(
        family="League Spartan",
        size=12
    )

    BUTTON_FONT = ctk.CTkFont(
        family="League Spartan",
        size=15,
        weight="normal"
    )