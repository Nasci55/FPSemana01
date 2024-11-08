character1 = str(input ("What is your first creature name? "))
healtch1 = int(input ("How many health points does your first creature have? "))
lvlch1 = int (input ("What is your first creature level? "))
character2 = str(input ("What is your second creature name "))
healtch2 = int(input ("How many health points does your second creature have: "))
lvlch2 = int (input ("What is the level of your second creature? "))
character3 = str(input ("What is your third creature name "))
healtch3 = int(input ("How many health points does your third creature have: "))
lvlch3 = int (input ("What is the level of your third creature? "))

Array = [[character1, (healtch1,lvlch1)], [character2, (healtch2, lvlch2)], [character3, (healtch3, lvlch3)]]
print (Array)

if lvlch1 > lvlch2 and lvlch1 > lvlch3:
    print (character1)
    if lvlch2 > lvlch3:
        print(character2)
        print (character3)
    else:
        print (character3)
        print (character2)
elif lvlch2 > lvlch1 and lvlch2 > lvlch3:
    print (character2)
    if lvlch1 > lvlch3:
        print (character1)
        print (character3)
    else:
        print (character3)
        print (character1)
elif lvlch3 > lvlch2 and lvlch3 > lvlch1:
    print (character3)
    if lvlch1 > lvlch2:
        print (character1)
        print (character2)
    else:
        print (character2)
        print (character1)
