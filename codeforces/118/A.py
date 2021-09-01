input = input()
input = input.lower()


word = list(input)

vowels = {'a',  'i', 'o', 'u', 'e', 'y'}

for i in range(len(word)):
    if word[i] in vowels:
        word[i] = ''
    else:
        word[i] = '.'+word[i]

print("".join(word))
