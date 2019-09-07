"""
Created on Wed Sep  4 12:20:27 2019
Lab 1
CS2302 Data Structures
MW 10:30
@author: Laurence Justin Labayen
"""
wordSet = list(open("words_alpha.txt").read().splitlines())
import time

def prefix():
    set2=set()
    for j in range(len(wordSet)):
        w=wordSet[j]
        for i in range(len(w)):
            set2.add(w.strip(w[i:]))
    return sorted(set2)

def anagram_search(r_letters, s_letters, wordSet, s, s1):

    if len(r_letters) == 0:
        if s_letters in wordSet:
            s.add(s_letters)      
    else:
        for i in range(len(r_letters)):
            scramble_letter = r_letters[i]
            remaining_letters = r_letters[:i] + r_letters[i+1:]  
            anagram_search(remaining_letters, s_letters + scramble_letter, wordSet, s, s1)
    return s

def optimized_anagram_search(r_letters, s_letters, wordSet, s, s1):

    if len(r_letters) == 0 and s_letters in wordSet:
            s.add(s_letters)      
    else:
        for i in range(len(r_letters)):
            scramble_letter = r_letters[i]
            remaining_letters = r_letters[:i] + r_letters[i+1:]  
            if scramble_letter not in remaining_letters and remaining_letters in s1:
                optimized_anagram_search(remaining_letters, s_letters + scramble_letter, wordSet, s, s1)
    return s

def search(anagram_finder):
    
    set1 = set()
    word = input('Enter anagram: ')
    start = time.perf_counter()
        
    if len(word) > 0 and word.startswith(' ') == False: 
        anagram_list = sorted(list(anagram_finder(word, '', wordSet, set1, set2)))
    
        if len(anagram_list) >= 2:
            anagram_list.remove(word)
            for i in range(len(anagram_list)):
                print(anagram_list[i])
        else:
            print('No anagrams for ' + word)
        end = time.perf_counter()
        print('It took ' + str(round((end - start), 6)) + ' seconds to find the anagram(s)')
    else:
        print("Bye! Thanks for using the program!")
set2=prefix()
search(anagram_search)
search(optimized_anagram_search)