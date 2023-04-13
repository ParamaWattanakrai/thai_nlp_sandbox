import pythainlp

text = 'ประวัติศาสตร์ราษฎร์'
syllables = pythainlp.tokenize.subword_tokenize(text)

for syllable in syllables:
    print(syllable)

print('ประวัติศาสตร์')