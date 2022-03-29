
def rotationalCipher(input, rotation_factor):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_letters = list(input)
    ciphered = []
    for letter in all_letters:
        if letter.upper() in alphabet: # letter
            ix = (alphabet.index(letter.upper()) + rotation_factor)
            transform = alphabet[ix % len(alphabet)]
            transform = transform if letter.isupper() else transform.lower()
        elif letter.isnumeric(): # number
            transform = str((int(letter) + rotation_factor) % 10)
        else: # character
            transform = letter
        ciphered.append(transform)
    return "".join(ciphered)

if __name__ == '__main__':
    R = []
    R.append(["Zebra-493?",3]) #Cheud-726?
    R.append(["abcdefghijklmNOPQRSTUVWXYZ0123456789",39]) #nopqrstuvwxyzABCDEFGHIJKLM9012345678
    R.append(["All-convoYs-9-be:Alert1.",4]) #"Epp-gsrzsCw-3-fi:Epivx5."
    R.append(["abcdZXYzxy-999.@",200]) #stuvRPQrpq-999.@
    R.append(["agoda",5]) # eafcobok
    for r in R:
        print(rotationalCipher(r[0], r[1]))
        

    