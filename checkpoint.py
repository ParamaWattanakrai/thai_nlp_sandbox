from dict import *

BLENDS = th_chars['consonants']['blends']
BLEND_INITIALS = th_utils['blend_initials']
POLY_INITIALS = th_utils['poly_initials']
POLY_FOLLOWS = th_utils['poly_follows']

#text = ('กร้ะเพราห์อกะเพราะท์โต๊ะพิ์เนี้ยะก์เกลื่อง์เละซ์')
text = ('กร้ะเพราห์อกะเพราะท์โต๊ะเนี้ยะก์เกลื่อง์เละซ์')
text_lists = [[char, true_index] for true_index, char in enumerate(text)]
no_tones = [[char, true_index] for char, true_index in text_lists if not char in th_chars['diacritics']['tones']]
text_vowels = [[char, true_index] for char, true_index in text_lists if char in th_chars['vowels']]
split_indexes = []
syllables = []

for index in range(len(no_tones),len(no_tones)+6):
    unbugger = 0
    no_tones.append(['X',len(no_tones)+unbugger])
    unbugger += 1

def find_index(vowels, target_list):
    for index, sublists in enumerate(target_list):
        if sublists[1] == vowels[1]:
            return index

def add_true_blend_vowel_initial(current):
    potential_initial_blend = no_tones[current+1]
    potential_blend = no_tones[current+2]
    if potential_blend[0] not in BLENDS:
        return 0
    if potential_initial_blend[0] not in BLEND_INITIALS[potential_blend[0]]:
        return 0
    return 1

def check_poly_follow(poly_initial_index):
    poly_initial = no_tones[poly_initial_index]
    add_blend = add_true_blend_vowel_initial(poly_initial_index)
    potential_poly_follow = no_tones[poly_initial_index+2+add_blend]
    if potential_poly_follow[0] not in POLY_FOLLOWS[poly_initial[0]]:
        return False
    return True

def check_karan(current):
    add_index = 0
    if no_tones[current+2][0] in th_chars['vowels']:
        add_index = 1
    if no_tones[current+add_index+2][0] == '์':
        add_index += 2
    end_syllable_index = current + add_index
    return end_syllable_index

def check_poly_sara_ee(poly_initial_index):
    add_blend = add_true_blend_vowel_initial(poly_initial_index)
    add_index = 0
    poly_follow_first = no_tones[poly_initial_index+add_blend+2]
    potential_poly_follow_second = no_tones[poly_initial_index+add_blend+3]

    if poly_follow_first[0] == 'ะ':
        add_index = 2
        potential_final_consonant = False
    if poly_follow_first[0] == 'า':
        add_index = 2
        potential_final_consonant = False
    if (poly_follow_first[0] == 'ี' and potential_poly_follow_second[0] == 'ย') \
    or (poly_follow_first[0] == 'ื' and potential_poly_follow_second[0] == 'อ'):
        add_index = 3
        potential_final_consonant = True

    potential_sara_a = no_tones[poly_initial_index+add_blend+add_index+1]
    if potential_sara_a[0] == 'ะ':
        add_index += 1
        potential_final_consonant = False
    
    poly_final_index = check_karan(poly_initial_index + add_blend + add_index)
    return [poly_final_index, potential_final_consonant]

def poly_initial(vowels):
    if vowels[0] in POLY_INITIALS:
        poly_initial_index = find_index(vowels, no_tones)
        if check_poly_follow(poly_initial_index) == True:
            poly_final_index = check_poly_sara_ee(poly_initial_index)[0]
            print(no_tones[poly_initial_index])
            print(no_tones[poly_final_index])
            print('yes')

for vowels in text_vowels:
    poly_initial(vowels)

print(no_tones)
print(split_indexes)