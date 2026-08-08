# Chhatrapati Shivaji Maharaj Tribute - Star Art in Orange (Saffron)
# Python program using ANSI escape codes for orange color

ORANGE = "\033[38;5;208m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_orange(text):
    print(f"{ORANGE}{BOLD}{text}{RESET}")

def crown_design():
    # Simple crown shape made of stars
    crown = [
        "                *                ",
        "               ***               ",
        "        *     *****     *        ",
        "       ***   *******   ***       ",
        "      ***** ********* *****      ",
        "     ******************** *****  ",
        "   ****************************  ",
        "  ******************************* ",
        " ********************************* ",
        "***************************************",
    ]
    for line in crown:
        print_orange(line.center(45))

def sword_design():
    # Simple sword/talwar shape
    sword = [
        "                *                ",
        "               ***               ",
        "              *****              ",
        "             *******             ",
        "            *********            ",
        "               ***               ",
        "               ***               ",
        "               ***               ",
        "               ***               ",
        "              *****              ",
        "             *******             ",
        "            *********            ",
    ]
    for line in sword:
        print_orange(line.center(45))

def print_banner():
    border = "*" * 45
    print_orange(border)
    print_orange("★  जय भवानी | जय शिवाजी  ★".center(45))
    print_orange(border)
    print()
    crown_design()
    print()
    print_orange("छत्रपती शिवाजी महाराज".center(45))
    print_orange("हिंदवी स्वराज्याचे संस्थापक".center(45))
    print()
    sword_design()
    print()
    print_orange(border)

if __name__ == "__main__":
    print_banner()