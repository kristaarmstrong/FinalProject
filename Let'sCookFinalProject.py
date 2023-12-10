import random

breakingBadQuotes = [
#Walter White quotes
    {"quote": "I am the the one who knocks", "character":"Walter White"},
    {"quote": "Say my name.", "character": "Walter White"},
    {"quote": "You're an insane, degenerate piece of filth, and you deserve to die", "chracter":"Walter White"},
    {"quote": "Stay out of my territory.", "character": "Walter White"},
    {"quote": "I'm in the empire business", "character": "Walter White"},
    {"quote": "If you believe that there's a hell, I don't know if youre into that, but we're pretty much going there, right?", "character": "Walter White"},
    {"quote": "Tread lightly", "character": "Walter White"},
    {"quote": "I did it for me.", "character": "Walter White"},
    {"quote": "It can be done exactly as I want it. The only question is, are you the man to do it.", "character":"Walter White"},
    {"quote": "I spent my whole life scared, frightened, of things that could happen, might happen, might not happen.","character":"Walter White"},
#Jesse Pinkman Quotes
    {"quote": "Well, um, he did try to kill us both yesterday. So, there's that.", "character":"Jesse Pinkman"},
    {"quote": "Then do it yourself.", "character":"Jesse Pinkman"},
    {"quote": "Yeah, science!", "character": "Jesse Pinkman"},
    {"quote":"I'm not turning down the money.I'm turning down you." ,"character":"Jesse Pinkman"},
    {"quote":"We make poison for people who don't care","character":"Jesse Pinkman"},
    {"quote":"Would you just, for once, stop working me","character":"Jesse Pinkman"},
    {"quote":"Are we in the meth business or the money business","character":"Jesse Pinkman"},
    {"quote":"When I was comin' up it was just possum. Opossum makes it sounds like he's irish or something","character":"Jesse Pinkman"},
    {"quote":"I'm a blowfish! Blowfish! Yeah! Blowfishin' this up!","character":"Jesse Pinkman"},
    {"quote":"What ever happened to truth in advertising?","character":"Jesse Pinkman"},
#Gus Quotes
    {"quote":"You are a wealthy man now. One must learn to be rich. To be poor, anyone can manage", "character":"Gustavo Fring"},
    {"quote":"Don Eladio is dead. His Capos are dead. You have no one left to fight for.", "character":"Gustavo Fring"},
    {"quote":"I investigate everone with whom I do business.", "character":"Gustavo Fring"},
    {"quote":"I hide in plain sight, same as you.", "character":"Gustavo Fring"},
    {"quote":"Never make the same mistake twice.", "character":"Gustavo Fring"},
    {"quote":"A bullet to the head would have been far too humane", "character":"Gustavo Fring"},
    {"quote":"I will kill your wife. I will kill your son. I will kill your infant daughter", "character":"Gustavo Fring"},
    {"quote":"What does a man do? A man provides", "character":"Gustavo Fring"},
    {"quote":"My friends, I promise you that together, we will prosper.", "character":"Gustavo Fring"},
    {"quote":"You can never trust a junkie.", "character":"Gustavo Fring"},
#Saul Goodman Quotes
    {"quote":"What did you expect? Haji's quick vanish?", "character":"Saul Goodman"},
    {"quote":"Congratulations! You're now officially the cute one of the group", "character":"Saul Goodman"},
    {"quote":"Look, let's start with some tough love, all right? Ready for this? Here goes: you suck at peddling meth. Period.", "character":"Saul Goodman"},
    {"quote":"He gave me the dead mackerel eyes.", "character":"Saul Goodman"},
    {"quote":"If you're committed enough, you can make any story work.", "character":"Saul Goodman"},
    {"quote":"That's what the kids call 'epic fail'", "character":"Saul Goodman"},
    {"quote":"You worked for him? The guy with the eyebrows that won't quit?", "character":"Saul Goodman"},
    {"quote":"Alaska? That's a different vibe. I never figured you for a big moose lover, but whatever floats your boat", "character":"Saul Goodman"},
    {"quote":"As for your dead guy... occupational hazard. Drug dealer getting shot? I'm gonna go out on a limb here and say it's been known to happen.", "character":"Saul Goodman"},
    {"quote":"Believe me, money laundering ain't what it used to be. God, do I miss the 80s.", "character":"Saul Goodman"},
#Hank Quotes
    {"quote":"Tagging trees is alot better than chasing monsters", "character":"Hank Schrader"},
    {"quote":"A guy that clean has to be dirty", "character":"Hank Schrader"},
    {"quote":"Sometimes the forbidden fruit tastes the sweetest", "character":"Hank Schrader"},
    {"quote":"When I go there, I'm bringing proof, not suspicion.", "character":"Hank Schrader"},
    {"quote":"You're the smartest guy I ever met. But you're too stupid to see...", "character":"Hank Schrader"},
    {"quote":"Heh-heh. S'all good, man! Come on. That's your name?", "character":"Hank Schrader"},
    {"quote":"I swear to Christ- I will put you under the jail.", "character":"Hank Schrader"},
    {"quote":"You had my cell phone number! You had my wife's name! How'd you do it? Talk! Who you working with?", "character":"Hank Schrader"},
    {"quote":"THEY ARE MINERALS!", "character":"Hank Schrader"},
    {"quote":"Free food always tastes good. Free drinks even better.", "character":"Hank Schrader"}
]


def FunFact(character):
    fun_facts = {
        "Walter White": "The iconic shot of Walter White tossing the pizza on the roof of his hour was shot in one take and was possible due to the pizza being unsliced.",
        "Jesse Pinkman": "Jesse Pinkman was only supposed to appear in nine episodes of Breaking Bad",
        "Saul Goodman": "The name 'Saul Goodman' comes from the the phrase 'It's all good, man'",
        "Gustavo Fring":"Gus Fring spent is childhood living in extreme poverty with his siblings.",
        "Hank Schrader": "DEA special agent Hank Schroder was supervisor of all investigations handled by his Albequerque office."

    }
    return fun_facts.get(character, "Fun fact not available for this character.")

def pressToContinue():
    try:
        input("\n" + "Press any key to continue!")
    except KeyboardInterrupt:
        pass

def pressForDirections():
    try:
        input("\n" + "Press any key for directions.")
    except KeyboardInterrupt:
        pass

def randomQuote():
    return random.choice(breakingBadQuotes)

def playAgain():
    quote1 = randomQuote()
    print( "\n" + "Your next quote is:" + "\n" + quote1["quote"])
    character = quote1["character"]
    guess = input("Who said this?")
    if guess.lower() == quote1["character"].lower():
        print("Correct!Nice job!")
        fact = FunFact(character)
        print(f"Fun Fact: {fact}")
        again = input("Would you like to play again?(yes or no)")
        if again == "yes":
            letsCook()
        else:
            print("Thank you for playing, hope to see you again soon!")
    else:
        redo = input(f"No, sorry! The quote was said by {quote1['character']}. Would you like to try a different quote? (yes or no)")
        if redo == "yes":
            letsCook()
        else:
            print("Thank you for playing, hope to see you again soon!")

def letsCook():
    print("Welcome to Let's Cook! A game to guess which character said this line!")
    
    pressForDirections()
    
    print("A quote from the show Breaking Bad will appear, and it is your job to guess to said it. You're options are Walter White, Jesse Pinkman, Gustavo Fring, Hank Schrader, and Saul Goodman.")
    
    pressToContinue()
    
    quote1 = randomQuote()
    print( "\n" + quote1["quote"])
    character = quote1["character"]

    guess = input("Who said this?")
    if guess.lower() == quote1["character"].lower():
        print("Correct!Nice job!")
        fact = FunFact(character)
        print(f"Fun Fact: {fact}")
        again = input("Would you like to play again?(yes or no)")
        if again == "yes":
            playAgain()
        else:
            print("Thank you for playing, hope to see you again soon!")
    else:
        redo = input(f"No, sorry! The quote was said by {quote1['character']}. Would you like to try a different quote? (yes or no)")
        if redo == "yes":
            playAgain()
        else:
            print("Thank you for playing, hope to see you again soon!")
                        

letsCook()

    
 
