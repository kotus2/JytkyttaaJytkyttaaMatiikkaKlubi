# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#cf88c8")
define y = Character("Yrsa", color="#00ff00")

define z = Character("")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Welcome to the bloody death battle™."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Слоны превосоходны!"

    hide eileen happy
    
    z "11"
    
    show yrsa neutral
    
    y "player... i remember your'e {color=#f00}{b}genocides...{/b}{/color}"
    
    hide yrsa neutral
    show yrsa peculiar
    
    y "hmm........"
    
    y "i'm feeling a bit... {color=#f0f}{b}peculiar.....{/b}{/color}"

    # This ends the game.

    return
