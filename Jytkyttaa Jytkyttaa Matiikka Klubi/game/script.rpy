# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Väinö", color="#db0404")
define y = Character("Yrsa", color="#00ff00")
define l = Character("Lemitty", color="#fbff00")
define j = Character("Jalmari", color="#0000FF")




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jalmari happy

    # These display lines of dialogue.
    j "Shimi shimi ya shimi shimi e shwalalala (drank) shwalalala"

    j "Hi good to meet you!"

    j "What about you take test so we can know whats your math level"



    hide eileen happy
    
    
    
    show yrsa neutral
    
    # y "player... i remember your'e {color=#f00}{b}genocides...{/b}{/color}"
    
    # hide yrsa neutral
    # show yrsa peculiar
    
    # y "hmm........"
    
    # y "i'm feeling a bit... {color=#f0f}{b}peculiar.....{/b}{/color}"

    # This ends the game.

    return
