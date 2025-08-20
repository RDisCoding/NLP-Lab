import collections

with open('brown_nouns.txt', 'r') as f:
    words = [line.strip().lower() for line in f if line.strip()]

freq = collections.Counter(words)

print('Common words ending in -s:')
s_words = [w for w in freq.most_common(200) if w[0].endswith('s') and len(w[0]) > 3]
for w, f in s_words[:10]:
    print(f'{w}: {f}')

print('\nCommon words ending in -ing:')
ing_words = [w for w in freq.most_common(500) if w[0].endswith('ing') and len(w[0]) > 4]
for w, f in ing_words[:10]:
    print(f'{w}: {f}')

print('\nCommon words ending in -ed:')
ed_words = [w for w in freq.most_common(500) if w[0].endswith('ed') and len(w[0]) > 3]
for w, f in ed_words[:10]:
    print(f'{w}: {f}')

print('\nCommon words ending in -er:')
er_words = [w for w in freq.most_common(500) if w[0].endswith('er') and len(w[0]) > 3]
for w, f in er_words[:10]:
    print(f'{w}: {f}')
