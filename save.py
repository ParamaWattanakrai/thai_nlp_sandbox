from dict import *

BLENDS = th_chars['consonants']['blends']
BLEND_INITIALS = th_utils['blend_initials']
POLY_INITIALS = th_utils['poly_initials']
POLY_FOLLOWS = th_utils['poly_follows']

text = ('กร้ะเพราห์อกะเพราะท์โต๊ะพิ์เนี้ยะก์เกลื่อง์เละซ์')
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
    potential_poly_follow = no_tones[poly_initial_index+2+add_true_blend_vowel_initial(poly_initial_index)]
    if potential_poly_follow[0] not in POLY_FOLLOWS[poly_initial[0]]:
        return False
    return True

def check_poly_sara_ee(poly_initial_index):
    print(no_tones[poly_initial_index])
    add_current_sara_a = 0
    poly_follow_first = no_tones[poly_initial_index+2+add_true_blend_vowel_initial(poly_initial_index)]
    poly_follow_second = no_tones[poly_initial_index+3+add_true_blend_vowel_initial(poly_initial_index)]
    potential_sara_a = no_tones[poly_initial_index+2+add_current_sara_a+add_true_blend_vowel_initial(poly_initial_index)]
    if poly_follow_first[0] == 'า':
        add_current_sara_a = 1
    if (poly_follow_first[0] == 'ี' and poly_follow_second[0] == 'ย') \
    or (poly_follow_first[0] == 'ื' and poly_follow_second[0] == 'อ'):
        add_current_sara_a = 2
    if potential_sara_a[0] == 'ะ':
        add_current_sara_a += 1
    return add_current_sara_a

def check_karan(current):
    add_current_karan = 0
    if no_tones[current+3+check_poly_sara_ee(current)+add_true_blend_vowel_initial(current)][0] in th_chars['vowels']: #ป้องกันคำจำพวก "พันธุ์"
        add_current_karan = 1
    if no_tones[current+3+check_poly_sara_ee(current)+add_true_blend_vowel_initial(current)+add_current_karan][0] == '์':
        split_indexes.append(no_tones[current+3+check_poly_sara_ee(current)+add_true_blend_vowel_initial(current)+add_current_karan][1])
    return

def poly_initial(vowels):
    if vowels[0] in POLY_INITIALS:
        poly_initial_index = find_index(vowels, no_tones)
        if check_poly_follow(poly_initial_index) == True:
            if check_poly_sara_ee(poly_initial_index) > 0:
                check_karan(poly_initial_index)
                print('yes')

for vowels in text_vowels:
    poly_initial(vowels)

print(no_tones)
print(split_indexes)