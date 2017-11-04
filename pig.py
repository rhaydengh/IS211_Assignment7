
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 7, Python game of Pig"""

from random import randint

class Player(object):

    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self):
        print "----------------------------------------------------------"
        print "Player", self.name, "begin"
        print "Current score is {}".format(self.score)
        while True:
            myroll = randint(1, 6)
            print " you got a", myroll
            if myroll == 1:
                self.score = 0
                print " your score is", self.score
                break
            else:
                self.score += myroll
                print " your score is", self.score
                if self.score >= 100:
                    return
                ans = raw_input("do you want to continue (y=yes n=no)?")
                if ans == 'n':
                    break

        print "next player"


def turntoroll(player, score):
    print "----------------------------------------------------------"
    print "Player", player, "begin"
    print "Your current score is {}".format(score)
    while True:
        myroll = randint(1, 6)
        print " you got a", myroll
        if myroll == 1:
            score = 0
            print " your score is", score
            break
        else:
            score += myroll
            print " your score is", score
            if score >= 100:
                return score
            ans = raw_input ("do you want to continue (y=yes n=no)?")
            if ans == 'n':
                break

    print "next player"
    return score


def main():
    p1 = 0
    p2 = 0
    while p1 < 100 and p2 < 100:
        p1 = turntoroll(1, p1)
        if p1 >= 100:
            print "player 1 wins"
            break
        p2 = turntoroll(2, p2)
        if p2 >= 100:
            print "player 2 wins"
            break

if __name__ == "__main__":
    main()

