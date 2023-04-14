from dict import *

text = ('เคราะห์')
no_tones = []
text_lists = []
text_vowels = []
split_indexes = []
syllables = []

# FIRST LAST CHECKER
# ะ  ์ function
# index out of range fix

for true_index, char in enumerate(text):
    text_lists.append([char, true_index])
    no_tones.append([char, true_index])
    if char in th_chars['vowels']:
        text_vowels.append([char, true_index])
    if char in th_chars['diacritics']['tones']:
        no_tones.pop()

for vowels in text_vowels:
    current = None
    #Find poly_initial
    if vowels[0] in th_utils['poly_initials']:
        #Find no_tones index
        for index, sublists in enumerate(no_tones):
            if sublists[1] == vowels[1]:
                current = index
        #Checks if true blend
        print(no_tones[current+2][0])
        if no_tones[current+2][0] in th_chars['consonants']['blends']:
            if no_tones[current+1][0] in th_utils['blend_initials'][no_tones[current+2][0]]:
                if no_tones[current+3][0] in th_utils['poly_follows'][no_tones[current][0]]:
                    if no_tones[current+3][0] == 'ะ':
                        if no_tones[current+5][0] == '์':
                            #INFRONT WIP
                            split_indexes.append(no_tones[current+5][1])
                        else:
                            #INFRONT WIP
                            split_indexes.append(no_tones[current+3][1])
                    elif no_tones[current+3][0] == 'า':
                        if no_tones[current+4][0] == 'ะ':
                            if no_tones[current+6][0] == '์':
                                #INFRONT WIP
                                split_indexes.append(no_tones[current+6][1])
                            else:
                                #INFRONT WIP
                                split_indexes.append(no_tones[current+4][1])
                        else:
                            if no_tones[current+5][0] == '์':
                                #INFRONT WIP
                                split_indexes.append(no_tones[current+5][1])
                            else:
                                #INFRONT WIP
                                split_indexes.append(no_tones[current+3][1])
                                print('yes')



print(split_indexes)