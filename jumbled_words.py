# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:25:47 2018

@author: bmpatel
"""
import random
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
    
def choose():
    words=['rainbow','computer','science','programing','player','conditon','reverse','water','board']
    pick= random.choice(words)
    return pick
    
def thank(p1n,p2n,p1,p2):
    print(p1n,' Your score is : ',p1)
    print(p2n,' Your score is : ',p2)
    print('Thanks for Playing')
    print('Have nice day')
    
def play():
    p1name=input('Player 1, Please enter your name')
    p2name=input('Player 2, Please enter your name')
    pp1=0
    pp2=0
    turn=0
    while(1):
        #Computer\s task
        picked_word=choose()
        #create questions
        qn=jumble(picked_word)
        print(qn)
        #playe(r 1
        if turn%2==0:
            print(p1name,' your turn. ')
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp1=pp1+1
                print('Your score is : ',pp1)
            else:
                print('Better luck next time. I thought :',picked_word)
            c=input('Press 1 to continue and 0 to quit: ')
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        #player 2
        else:    
            print(p2name,' your turn. ')
            ans=input('What is on my mind?')
            if ans==picked_word:
                pp2=pp2+1
                print('Your score is : ',pp2)
            else:
                print('Better luck next time. I thought :',picked_word)
            c=input('Press 1 to continue and 0 to quit: ')
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
        
play()

