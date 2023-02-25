#!/usr/bin/python3
#
# A text-based adventure game, based on
# https://github.com/codinggrace/text_based_adventure_game
#
# MIT License
# Copyright (c) 2020 Coding Grace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from cmath import pi
import gamedata as game, pictures as pic

def main():
    name = input("What's your name?\n>> ")
    print("Welcome {} to the adventure of your life. Try to survive and find \
    the treasure!".format(name.upper()))
    current_state = "Start"
    while not(current_state == "End"):
        pic.print_pic(current_state)
        current_state = get_next_state(current_state)
    pic.print_pic(current_state)

def get_next_state(state):
    succ_states = game.ADVENTURE_TREE[state]
    if len(succ_states) == 1:
        print(game.DESCRIPTIONS[state])
        return succ_states[0]
    else:
        text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[state],
                                            "1", game.OPTIONS[succ_states[0]],
                                            "2", game.OPTIONS[succ_states[1]])
        print(text_box)
        inp = input(">> ")
        return succ_states[int(inp) - 1]


def main_old():
    name = input("What's your name?\n>> ")
    print("Welcome {} to the adventure of your life. Try to survive and find the \
    treasure!".format(name.upper()))
    current_state = "Start"
    while not(current_state == "End"):
        if current_state == "Start":
            pic.print_pic("print_doors")
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]

        if current_state == "Blue":
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]
        
        if current_state == "Guard":
            pic.print_pic("print_guard")
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]
        
        if current_state == "Chest":
            pic.print_pic("print_treasure")
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]
        
        if current_state == "Take":
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]

        if current_state == "Leave":
            pic.print_pic("print_guard")
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]
        
        if current_state == "Sneak":
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]
        
        if current_state == "Red":
            pic.print_pic("print_dragon")
            succ_states = game.ADVENTURE_TREE[current_state]
            text_box = "{}\n{}  {}\n{}  {}".format(game.DESCRIPTIONS[current_state],
                                                "1", game.OPTIONS[succ_states[0]],
                                                "2", game.OPTIONS[succ_states[1]])
            print(text_box)
            inp = input(">> ")
            current_state = succ_states[int(inp)-1]

        if current_state == "Sneak to the right":
            print(game.DESCRIPTIONS[current_state])
            current_state = "End"

        if current_state == "Sneak to the left":
            pic.print_pic("print_game_over")
            print(game.DESCRIPTIONS[current_state])
            current_state = "End"

        if current_state == "Talk":
            print(game.DESCRIPTIONS[current_state])
            current_state = "End"

        if current_state == "Flee":
            print(game.DESCRIPTIONS[current_state])
            current_state = "End"

        if current_state == "Attack":
            pic.print_pic("print_game_over")
            print(game.DESCRIPTIONS[current_state])
            current_state = "End"

main()