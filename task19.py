letters = ["h", "e", "l", "l", "o", "w", "O", "r", "l", "d"]

unlilar = ['a', 'e', 'i', 'o', 'u']

unli_soni = sum(1 for harf in letters if harf.lower() in unlilar)

print(unli_soni)  
