
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 7, Python game of Pig"""



from random import randint


def roll():
    myroll = randint(1,6)
    return myroll


def turntoroll(player):
    global score
    score=0
    print "Player", player, "begin"
    raw_input( "press enter to begin")
    while True:
        myroll = randint(1,6)
        print " you got a", myroll
        if myroll == 1:
            score=0
            print " your score is", score
            break
        else:
            score += myroll
            print " your score is", score
            ans = raw_input ("do you want to continue? y=yes n=no")
            if ans == 'y':
                continue
            else:
                break

    print "next player"
    return score


def main():
    p1 = 0
    p2=0
    while p1<=100 and p2<=100:
        if turntoroll(1):
            score = p1
        elif turntoroll(2):
            score = p2
        elif p1 >=100:
            print "player 1 wins"
        elif p2 >=100:
            print "player 2 wins"


if __name__ == "__main__":
    main()

