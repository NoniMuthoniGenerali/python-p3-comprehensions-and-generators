#!/usr/bin/env python3

def return_evens(num_list):
     evens = [num for num in range(num_list) if  num%2 == 0]
     print(evens)
return_evens(19)

def make_exclamation(sentence_list):
    exclaim = [word + "!" for word in sentence_list]
    print(exclaim)
make_exclamation(["VivaPalestina", "untiil" "everyone" "is" "free"]) 