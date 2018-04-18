#For building the encrypted string:
#Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
#Do this n times!

#Examples:

#"This is a test!", 1 -> "hsi  etTi sats!"
#"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

#Write two methods:

#def encrypt(text, n)
#def decrypt(encrypted_text, n)

#For both methods:
#If the input-string is null or empty return exactly this value!
#If n is <= 0 then return the input text.

def encrypt(text, n):
    if n <= 0:
        return text
    else:
        j = 1
        while j <= n:
            text_list = [x for x in text]
            new = ""
            i = 1
            while i < len(text):
                new = new + text[i]
                text_list[i] = ""
                i+= 2
            j += 1
            text_remain = "".join(text_list)
            text = new + text_remain
    return new + text_remain

def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    else:
        j = 1
        while j <= n:
            new = ""
            i = 0
            leng = len(encrypted_text)
            if leng % 2 == 0:
                while i < int(leng/2):
                    new = new + encrypted_text[i+int(leng/2)] + encrypted_text[i]
                    i += 1
            elif leng % 2 == 1:
                while i < int((leng-1)/2):
                    new = new + encrypted_text[i+int((leng-1)/2)] + encrypted_text[i]
                    i += 1
                new = new + encrypted_text[leng-1]
            encrypted_text = new
            j += 1
    return new
