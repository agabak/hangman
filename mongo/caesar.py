alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']

direction = input("Type 'ecode' to encrypt, tyep 'decode' to decrypt:\n ")
text = input("Type a message:\n").lower()
shift = int(input("Type the shift number:\n"))

def crypt(plan_text,shift_amount):
    my_text = ""
    for letter in plan_text:
        indx_latter = alphabet.index(letter)
        new_indz_letter = indx_latter + shift_amount
        new_letter = alphabet[new_indz_letter]
        my_text += new_letter
    print(my_text)


crypt(text,shift) 
        


#instead of building all new string , just append a letter an empty stringeed