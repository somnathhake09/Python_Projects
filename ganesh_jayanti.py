"""
Ganesh Jayanti Digital Greeting Card
-------------------------------------
Built with Python's built-in `turtle` module only.

Layout (top to bottom), so nothing overlaps:
    1. Title text
    2. Greeting text
    3. Om symbols + flowers (upper decoration row)
    4. Lord Ganesha illustration (center)
    5. Diyas (lower decoration row)
    6. Footer text (With Best Wishes / Somnath Hake)
"""

import turtle
import random

try:
    import tkinter.font as tkFont
except ImportError:
    tkFont = None


# ---------------------------------------------------------------------
# 1. SCREEN SETUP
# ---------------------------------------------------------------------
screen = turtle.Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Ganesh Jayanti - Somnath Hake")

# tracer(0) turns OFF automatic screen updates while drawing.
# This makes drawing much faster and lets us control exactly when
# the screen refreshes (important for smooth animation later).
screen.tracer(0)

# ---- Pick a font that can actually display Marathi (Devanagari) text ----
# turtle just asks the operating system to render the font you name.
# If that font doesn't have Devanagari letters, you'll see empty boxes.
# Here we check which fonts are installed and pick the first good one.
PREFERRED_MARATHI_FONTS = [
    "Nirmala UI",              # Windows
    "Noto Sans Devanagari",    # Linux / cross-platform (install if missing)
    "Lohit Devanagari",        # Linux
    "Kohinoor Devanagari",     # macOS
    "Mangal",                  # older Windows
]

marathi_font_name = "Arial"  # fallback if nothing better is found
if tkFont is not None:
    try:
        available_fonts = set(tkFont.families())
        for f in PREFERRED_MARATHI_FONTS:
            if f in available_fonts:
                marathi_font_name = f
                break
    except Exception:
        pass  # if anything goes wrong, we just keep the fallback font

TITLE_FONT = (marathi_font_name, 22, "bold")
GREETING_FONT = (marathi_font_name, 18, "bold")
FOOTER_FONT = ("Arial", 14, "normal")
FOOTER_NAME_FONT = ("Arial", 16, "bold")


# ---------------------------------------------------------------------
# 2. HELPER FUNCTIONS
# ---------------------------------------------------------------------
def new_pen():
    """Create a fast, invisible turtle ready for drawing."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    return pen


def filled_circle(pen, x, y, radius, fill_color, outline_color=None, outline_width=1):
    """
    Draw a filled circle centered at (x, y).
    Trick: turtle draws circles starting from the CURRENT position as the
    edge, going counter-clockwise. So we move to the bottom of the circle
    first, then call circle(radius) - this makes (x, y) the true center.
    """
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pendown()
    pen.pensize(outline_width)
    pen.pencolor(outline_color if outline_color else fill_color)
    pen.fillcolor(fill_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()
    pen.pensize(1)


def draw_flame(pen, x, y, color):
    """Draw one small flame (teardrop-ish triangle) at (x, y)."""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)
    pen.pendown()
    pen.fillcolor(color)
    pen.pencolor(color)
    pen.begin_fill()
    pen.forward(18)
    pen.right(150)
    pen.forward(13)
    pen.right(120)
    pen.forward(13)
    pen.end_fill()
    pen.penup()


def draw_text(pen, x, y, text, font, color):
    pen.penup()
    pen.goto(x, y)
    pen.pencolor(color)
    pen.write(text, align="center", font=font)


# ---------------------------------------------------------------------
# 3. GANPATI ILLUSTRATION
# ---------------------------------------------------------------------
def draw_ganpati(pen):
    """
    Draws a simple, symmetric Ganpati face using only circles, a
    triangle (crown) and one curved line (trunk). All parts are placed
    using coordinates measured from the same center point (0, 40) so
    the ears line up perfectly and stay symmetric.
    """
    cx, cy = 0, 40  # center of the face

    # --- Ears (drawn identically on both sides using a sign: -1 / +1) ---
    for side in (-1, 1):
        ex = cx + side * 125
        filled_circle(pen, ex, cy + 15, 55, "#CC6600", "#FFD700", 3)   # outer ear
        filled_circle(pen, ex, cy + 15, 28, "#FFB266", None, 1)        # inner ear

    # --- Crown (triangle + small ball on top) ---
    pen.goto(cx - 45, cy + 75)
    pen.setheading(0)
    pen.pendown()
    pen.pencolor("#FFD700")
    pen.fillcolor("#FFD700")
    pen.begin_fill()
    pen.goto(cx + 45, cy + 75)
    pen.goto(cx, cy + 130)
    pen.goto(cx - 45, cy + 75)
    pen.end_fill()
    pen.penup()
    filled_circle(pen, cx, cy + 138, 9, "#FFD700")

    # --- Face ---
    filled_circle(pen, cx, cy, 75, "#FF9933", "#FFD700", 3)

    # --- Eyes ---
    filled_circle(pen, cx - 24, cy + 15, 8, "black")
    filled_circle(pen, cx + 24, cy + 15, 8, "black")

    # --- Tilak (forehead mark) ---
    filled_circle(pen, cx, cy + 55, 5, "#CC0000")

    # --- Smile ---
    pen.goto(cx - 18, cy - 25)
    pen.setheading(-60)
    pen.pendown()
    pen.pencolor("black")
    pen.pensize(3)
    pen.circle(18, 120)
    pen.penup()
    pen.pensize(1)

    # --- Trunk (straight part + a small curled hook at the end) ---
    pen.goto(cx, cy - 35)
    pen.setheading(270)  # pointing straight down
    pen.pendown()
    pen.pensize(18)
    pen.pencolor("#FF9933")
    pen.forward(45)          # the straight part of the trunk
    pen.circle(-22, 200)     # negative radius = curls to the right (the "hook")
    pen.penup()
    pen.pensize(1)


# ---------------------------------------------------------------------
# 4. DECORATIONS
# ---------------------------------------------------------------------
def draw_diya(pen, x, y):
    """Draws a diya (oil lamp) base. Returns the flame position so the
    animation loop knows where to redraw the flickering flame."""
    pen.goto(x - 28, y)
    pen.setheading(0)
    pen.pendown()
    pen.pencolor("#8B4513")
    pen.fillcolor("#B5651D")
    pen.begin_fill()
    pen.circle(28, 180)
    pen.end_fill()
    pen.penup()
    return (x, y + 4)


def draw_flower(pen, x, y, petal_color, center_color):
    """A simple 6-petal flower made from small circles around a center."""
    for angle in range(0, 360, 60):
        pen.goto(x, y)
        pen.setheading(angle)
        pen.penup()
        px = x + 16 * _cos(angle)
        py = y + 16 * _sin(angle)
        filled_circle(pen, px, py, 11, petal_color)
    filled_circle(pen, x, y, 8, center_color)


def _cos(angle_deg):
    import math
    return math.cos(math.radians(angle_deg))


def _sin(angle_deg):
    import math
    return math.sin(math.radians(angle_deg))


def draw_om(pen, x, y):
    """Om symbol drawn as text (Devanagari 'ॐ' character)."""
    pen.penup()
    pen.goto(x, y)
    pen.pencolor("#FFD700")
    pen.write("ॐ", align="center", font=(marathi_font_name, 30, "bold"))


def draw_border_dots(pen):
    """Small decorative gold particles scattered near the side borders,
    kept away from the center so they never overlap text or Ganpati."""
    random.seed(7)  # fixed seed = same pretty pattern every run
    for _ in range(24):
        x = random.choice([-1, 1]) * random.randint(340, 390)
        y = random.randint(-330, 330)
        size = random.randint(3, 6)
        pen.goto(x, y)
        pen.dot(size, "#FFD700")


# ---------------------------------------------------------------------
# 5. STATIC LAYOUT (drawn once)
# ---------------------------------------------------------------------
art_pen = new_pen()
text_pen = new_pen()

# -- Title & Greeting (top area) --
draw_text(text_pen, 0, 295, "॥ श्री गणेशाय नमः ॥", TITLE_FONT, "#FFD700")
draw_text(text_pen, 0, 250, "गणेश जयंतीच्या हार्दिक शुभेच्छा!", GREETING_FONT, "white")

# -- Om symbols flanking the greeting --
draw_om(art_pen, -300, 262)
draw_om(art_pen, 300, 262)

# -- Flowers above the ears --
draw_flower(art_pen, -230, 165, "#FF4D4D", "#FFD700")
draw_flower(art_pen, 230, 165, "#FF4D4D", "#FFD700")

# -- Ganpati (center) --
draw_ganpati(art_pen)

# -- Diyas below Ganpati --
flame_positions = [
    draw_diya(art_pen, -290, -140),
    draw_diya(art_pen, 290, -140),
]

# -- Decorative gold particles near borders --
draw_border_dots(art_pen)

# -- Footer text --
draw_text(text_pen, 0, -300, "With Best Wishes", FOOTER_FONT, "white")
draw_text(text_pen, 0, -330, "Somnath Hake", FOOTER_NAME_FONT, "#FFD700")

# Show everything drawn so far (since tracer(0) is holding updates back)
screen.update()


# ---------------------------------------------------------------------
# 6. ANIMATION (flickering diya flames + twinkling particles)
# ---------------------------------------------------------------------
flame_pen = new_pen()
sparkle_pen = new_pen()

FLAME_COLORS = ["#FFD700", "#FFA500", "#FFEB3B"]  # cycled for a flicker effect
frame_counter = [0]  # a list so we can change it inside animate()

# A handful of small gold "sparkle" particles that slowly drift upward
# along the side margins, and loop back to the bottom when they reach top.
sparkles = []
for _ in range(15):
    sparkles.append({
        "x": random.choice([-1, 1]) * random.randint(200, 390),
        "y": random.randint(-340, 340),
        "speed": random.uniform(0.4, 1.0),
        "size": random.randint(3, 6),
    })


def animate():
    # --- Flickering diya flames ---
    flame_pen.clear()
    color = FLAME_COLORS[frame_counter[0] % len(FLAME_COLORS)]
    for (fx, fy) in flame_positions:
        draw_flame(flame_pen, fx, fy, color)

    # --- Twinkling / drifting sparkles ---
    sparkle_pen.clear()
    for s in sparkles:
        s["y"] += s["speed"]
        if s["y"] > 340:
            s["y"] = -340
            s["x"] = random.choice([-1, 1]) * random.randint(200, 390)
        sparkle_pen.goto(s["x"], s["y"])
        sparkle_pen.dot(s["size"], "#FFD700")

    frame_counter[0] += 1

    # Push all the changes to the screen in one go (smooth animation)
    screen.update()

    # Schedule this same function to run again after 150 milliseconds
    screen.ontimer(animate, 150)


# Kick off the animation loop
animate()

# Keeps the window open and responsive until the user closes it
turtle.mainloop()