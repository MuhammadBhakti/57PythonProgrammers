#caunting words
words = input("Masukkan :") #input new words
num_words = words.split()   #split words to the list
numberwords = len(num_words) #Caunt the words

#Caunting word without space
numberalphabet = 0
for i in words:
    if(i.isalpha()):
        numberalphabet=numberalphabet+1

numbers = 0
for i in words:
    if(i.isnumeric()):
        numbers=numbers+1

print("{} memiliki {} kata, {} huruf dan {} angka".format(words,numberwords,numberalphabet,numbers))