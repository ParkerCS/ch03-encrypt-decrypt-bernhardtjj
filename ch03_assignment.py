# MODULES AND LIBRARIES

# For this assignment, we will practice the use of imports to encrypt and decrypt messages.
# The functions are already contained in the files.  Your job is to use them to encrypt and decrypt strings.  Good luck.
from decode import *
from encode import *
from encryption_key import *

# 1 Decrypt this message using imports from the decode.py and encryption_key.py.
# Make the result print in a friendly format that is easy for the user to understand. (10pt)
encrypted_message = "¿®ªªÈÙ®ÏT¤ÕEÓ¹âeCíÉÁÏº¢¡i¸ºÇ¿"
print(decode(key, encrypted_message))
# 2 Encrypt your name and print the encrypted result.
# Make the result print in a friendly format that is easy for the user to understand. (5pt)
yum = encode(key, "JJ Bernhardt")
print(yum)
# 3 Decrypt the encrypted code from part 2 to ensure that it worked properly and print the result.
# Make the result print in a friendly format that is easy for the user to understand. (5pt)
print(decode(key, yum))
