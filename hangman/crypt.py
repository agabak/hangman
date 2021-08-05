from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

still_playing  = True

while still_playing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plan_text, shift_amount):
        encrypt_text = ""
        if type(plan_text) == str and type(shift_amount) == int:
            for letter in plan_text:
                indx_text = alphabet.index(letter)
                new_indx_text = indx_text + shift_amount
                new_letter = alphabet[new_indx_text]
                encrypt_text += new_letter
            
        print(encrypt_text)
          
    def decrypt(plan_text, shift_amount):
        decrypt_text = ""
        if type(plan_text) == str and type(shift_amount) == int:
            for letter in plan_text:
                indx_text = alphabet.index(letter)
                new_indx_text = indx_text - shift_amount
                new_letter = alphabet[new_indx_text]
                decrypt_text += new_letter
        print(decrypt_text)
         
    def  encrypt_decrypt_message(par_direction, text, shift): 
        if type(par_direction) == str:
            if par_direction == "encode":
                encrypt(text,shift)
            if  par_direction == "decode":
                decrypt(text, shift)
                
    encrypt_decrypt_message(direction,text, shift)

    still_want_crypt = input("If you want to quite crypt type No or Yes \n")

    if still_want_crypt.lower() == "no":
       still_playing = False
       print("Bye thank for using my sys")