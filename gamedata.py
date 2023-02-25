DESCRIPTIONS = {
    "Start": """You enter a room, and you see a blue door to your left and a \
red door to your right.
Which door do you pick?""",
    "Blue": """You see a room with a wooden treasure chest on the left, and a \
sleeping guard on the right in front of the door.
What do you do?""",
    "Chest": """Let's see what's in here... /grins
The chest creaks open, and the guard is still sleeping. That's one heavy \
sleeper! You find some diamonds, a shiny sword, and lots of gold coins.
Do you take the treasure or leave it?""",
    "Take": """Woohoo! Bounty and a shiney new sword. /drops your crappy \
sword in the empty treasure chest.
Ooops! The noise has woken up the guard.
What do you do now?""",
    "Leave":
    """Leaving all the shinies behind hurts, but it feels safer for now.
Hopefully, it will still be here, right after you gets past this guard.
What do you do next?""",
    "Guard": """The guard seems to be deep in sleep, but he has a mean \
looking axe right beside him.
What do you do?""",
    "Sneak": """You try to sneak past him. Do you want to go left or right?""",
    "Sneak to the right": """The guard jumps up and looks the other way, missing you \
entirely.
You just slipped through the door before the guard realised it.
You are now outside, home free! Huzzah!""",
    "Sneak to the left": """The guard catches you loser!!! Should have gone to the right:(""",
    "Talk": """What do you want to say?""",
    "RUN!! THE DRAGON IS COMMING!!": """Terrefied, he runs of out of the castle together with you""",
    "Hello!": """The guard is unfortunately not as happy to see you and clubs you with his axe""",
    "Red": """There you see the great evil Slathborg.
He, it, whatever stares at you and you go insane.
Do you flee for your life or attack it with your bare hands?""",
    "Flee": """You made it out alive, alas empty handed.""",
    "Attack": """You died. Well, at least the dragon thought you were tasty"""
}

OPTIONS = {
    "Blue": "Blue",
    "Red": "Red",
    "Chest": "Explore the chest",
    "Guard": "Advance toward the guard",
    "Take": "Grab all of the treasures",
    "Leave": "Leave them for another day",
    "Sneak": "Try to sneak past the guard",
    "Sneak to the right": "Try to sneak to the right of the guard",
    "Sneak to the left": "Try to sneak to the left of the guard",
    "Talk": "Talk to the guard",
    "RUN!! THE DRAGON IS COMMING!!": "RUN!! THE DRAGON IS COMMING!!",
    "Hello!": "Hello!",
    "Flee": "Flee",
    "Attack": "Attack"
}

ADVENTURE_TREE = {
    "Start": ["Blue", "Red"],
    "Blue": ["Chest", "Guard"],
    "Guard": ["Sneak", "Talk"],
    "Chest": ["Take", "Leave"],
    "Take": ["Sneak", "Talk"],
    "Leave": ["Sneak", "Talk"],
    "Sneak": ["Sneak to the right", "Sneak to the left"],
    "Sneak to the right": ["End"],
    "Sneak to the left": ["End"],
    "Talk": ["RUN!! THE DRAGON IS COMMING!!", "Hello!"],
    "RUN!! THE DRAGON IS COMMING!!": ["End"],
    "Hello!": ["End"],
    "Red": ["Flee", "Attack"],
    "Flee": ["End"],
    "Attack": ["End"]
}