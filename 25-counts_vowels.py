phrase = "la rana esta perdida en el bosque pero tiene sueño"

def count_vowels(myphrase):
    vowels = "aeiouAEIOU"
    counter = 0 
    
    for letter in myphrase:
        if letter in vowels: 
            counter = counter + 1
    return counter 

total_vowels = count_vowels(phrase)



print(f"la frase:{phrase} tiene {total_vowels} vocales ")
