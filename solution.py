first_shuffle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
# after first shuffle
second_shuffle = [1, 27, 2, 28, 3, 29, 4, 30, 5, 31, 6, 32, 7, 33, 8, 34, 9, 35, 10, 36, 11, 37, 12, 38, 13, 39, 14, 40, 15, 41, 16, 42, 17, 43, 18, 44, 19, 45, 20, 46, 21, 47, 22, 48, 23, 49, 24, 50, 25, 51, 26, 52]
# after second shuffle 
third_shuffle = [1, 14, 27, 40, 2, 15, 28, 41, 3, 16, 29, 42, 4, 17, 30, 43, 5, 18, 31, 44, 6, 19, 32, 45, 7, 20, 33, 46, 8, 21, 34, 47, 9, 22, 35, 48, 10, 23, 36, 49, 11, 24, 37, 50, 12, 25, 38, 51, 13, 26, 39, 52]
# after third shuffle 
forth_shuffle = [1, 33, 14, 46, 27, 8, 40, 21, 2, 34, 15, 47, 28, 9, 41, 22, 3, 35, 16, 48, 29, 10, 42, 23, 4, 36, 17, 49, 30, 11, 43, 24, 5, 37, 18, 50, 31, 12, 44, 25, 6, 38, 19, 51, 32, 13, 45, 26, 7, 39, 20, 52]
# after forth shuffle 
fifth_shuffle = [1, 17, 33, 49, 14, 30, 46, 11, 27, 43, 8, 24, 40, 5, 21, 37, 2, 18, 34, 50, 15, 31, 47, 12, 28, 44, 9, 25, 41, 6, 22, 38, 3, 19, 35, 51, 16, 32, 48, 13, 29, 45, 10, 26, 42, 7, 23, 39, 4, 20, 36, 52]
# after fifth shuffle
sixth_shuffle = [1, 9, 17, 25, 33, 41, 49, 6, 14, 22, 30, 38, 46, 3, 11, 19, 27, 35, 43, 51, 8, 16, 24, 32, 40, 48, 5, 13, 21, 29, 37, 45, 2, 10, 18, 26, 34, 42, 50, 7, 15, 23, 31, 39, 47, 4, 12, 20, 28, 36, 44, 52]
# after sixth shuffle
seventh_shuffle = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52]
# after seventh shuffle 
eighth_shuffle = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52]

# create a list of of 52 cards 
# divide them in half 
# store both halves in a variable
# loop over over the list to shuffle the deck 
# return the shuffled deck 
# store the shuffled list in a new variable 

def riffle_shuffle(deck):
    cutDeckInHalf = len(deck) // 2
    firstHalf = deck[:cutDeckInHalf]
    secondHalf = deck[cutDeckInHalf:]
    for i, item in enumerate(secondHalf):
        index = i * 2 + 1
        firstHalf.insert(index, item)
    return firstHalf

print(riffle_shuffle(eighth_shuffle))