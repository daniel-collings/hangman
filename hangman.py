#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


words = ['python','army reserve','great britain','machine learning','coding','middlesbrough']


# In[3]:


def getRandomWord():
    return random.choice(words)


# In[4]:


def nextRound(game):
    print('Letters used: ', game['guessed'])

    temp = ''
    for i in game['wordIs']:
        if(i == ' '):
            temp += i
            continue
        if(i not in game['guessed']):
            temp += '*'
        else:
            temp += i
    print('\nWord state is currently: ',temp)
    letterCheck = input("\n\t\tPlease Enter your next letter guess...\n\n")
    while(letterCheck not in 'qwertyuiopasdfghjklzxcvbnm' or letterCheck in game['guessed']):
          letterCheck = input("\n\t\tPlease enter ONLY letters you've not used before...\n\n")
    game['guessed'] += letterCheck
    temp2 = wordState(game)
    if('*' in temp2 and temp2.count('*') < temp.count('*')):
        print('Correct! Keep it up.')
        game['flag'] = True
        drawHangman(game)
    elif('*' not in temp2):
        print('CONGRATULATIONS! YOU SAVED THE STICKMAN!')
        cont = input('\n\tDO YOU WANT TO PLAY AGAIN? PRESS 1 TO PLAY  AGAIN... PRESS ANYOTHER KEY TO EXIT.')
        if(cont == '1'):
            startGame()
    else:
        game['attempts'] += 1
        game['flag'] = False
        drawHangman(game)
    
        


# In[5]:


def startGame():
    game = {'wordIs' : '','attempts': 0,'guessed': '', 'flag':True}
    game['wordIs'] = getRandomWord()
    nextRound(game)


# In[6]:


def wordState(game):
    mask = ''
    for i in game['wordIs']:
        if(i == ' '):
            mask += i
        elif(i in game['guessed']):
            mask += i
        else:
            mask += '*'
    return mask


# In[7]:


def drawHangman(game):
    HANGMANPICS = ["""
      +---+
      |   |
          |
          |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========="""]

    if(game['attempts'] == 7):
        print('Uh-oh! Game Over')
        print('The word was:',game['wordIs'])
        cont = input('DO YOU WANT TO PLAY AGAIN? PRESS 1 TO PLAY  AGAIN... PRESS ANYOTHER KEY TO EXIT.')
        if(cont == '1'):
            startGame()
    elif(game['attempts'] == 0):
        print(HANGMANPICS[game['attempts']])
        nextRound(game)
    elif(game['flag'] == False):
        unluckyList = ['Ouch! not quiet, ','Oh so close! ','Seriously!? ','Unlucky, ']
        encouragementList = ['keep trying','you can do it!','you know what to guess next']
        print(random.choice(unluckyList), random.choice(encouragementList))
        print(game['guessed'])
        game['flag'] = True
        if(game['attempts'] < 7):
            print(HANGMANPICS[game['attempts']])
        nextRound(game)        
    else:
        print(HANGMANPICS[game['attempts']])
        print(game['guessed'])
        nextRound(game)      


# In[ ]:


startGame()


# In[ ]:





# In[ ]:




