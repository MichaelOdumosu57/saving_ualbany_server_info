import random
import time
import os
import sys

class Flashcards:

        
    def __init__(self):

        self.flashcards = dict()

    def play_a_game(self):
        
        print("\n")
        print("Lets play Flashcards and Your Mind!!!\n")
        answer_i = "skip"

        while answer_i != "q":
            print("If you want to quit at any time press q")
            self.flashcards = self.flashcards

            
            
            for i in self.flashcards.keys():

                randomizer = 0
                attempts = 0

                if type(self.flashcards[i]) == list:
                    bullet_points = 1

                while True:

    

                        #answer_i = input("What is  " + i + " ? ")
                            
                        if answer_i == "q":
                            return
                        if answer_i == "skip":
                            print('alright')
                            time.sleep(.5)
                            print(i)


                            break
                          
                        if randomizer == 0:
                            print("Alright lets check\n")
                            print("...")
                            time.sleep(5)
                            if answer_i == self.flashcards[i][j]:
                                print("Alright you got it in" + attempts + "tries!,")
                                break
                            else:
                                if attempts % 2 == 0:
                                    print("No you didn't get it try again")
                                else:
                                    print("Are you sure? try again")
                                attempts += 1
                            
    def studY(self):
        while True:
                          
            query = input("Please type in term  ")
            a=0
            
            for i in self.flashcards.keys():

                if i == query:
                    print(self.flashcards[i])
                    a=1
                    break
            if a==0:
                print("Could not find search term, would you like to try another?")

    def add(self,term = None):
        try:
            while True:
                answer = input("Do you want to add again?")
                if answer == "no":
                    print(str(self.flashcards))
                    return
                terms = str(input("Please input terms  "))
                definition = str(input("Please input definition   "))             
                if  definition.find(',') != -1:
                    definition = definition.split(",")

                self.flashcards[terms] =definition 
        except:
            print("Place quotes")
            self.add()

    def save(self,ginit):

        final = open(ginit,"w")
        for i,j in self.flashcards.items():
            i += "$"
            final.write(i)
            final.flush()
            if type(j) == list:
                for defs in j:
                    final.write(str(defs)+ ",")
                    final.flush()
            else:
                final.write(j)
                final.flush()
            final.write("\n")
            final.flush()
        final.close()

    def load(self,ok):
        
        final = open(ok,"r")
        flash = final.read().splitlines()
        for i in flash:
            i  = i.split("$")
            print(i)
            if i[1].find(",") != -1:
                i[1] = i[1].split(',')
                print(type(i[1]))
                print("\n")
            self.flashcards[i[0]]= i[1]
        final.close()
        return 


def main():
        Archaelogy = Flashcards()
        Archaelogy.load('exmpr_try.txt')
        gisher = ""

        
        while True:
                        
            then= input("What would you like to do next?")
            if then.find("play") != -1:
                Archaelogy.play_a_game()

            if then.find("study") != -1:
                Archaelogy.reg_studY()

            if then.find("add") != -1:
                Archaelogy.add()

            if then.find("save") != -1:
                gisher = input("save as")
                Archaelogy.save(gisher)
                                        
            if then.find("load") != -1:
                gisher = input("which file")
                Archaelogy.load(gisher)




main()


        
    
    
                  
    
    

        
        
    
    

        


        
