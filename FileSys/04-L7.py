# Script that asks user to encode message in Base64
# then decode message print results
import base64

# ask user to provide secret, assign to variable
secret = input("Please enter a secret: ")
# encode secret using b64encode(), convert byte data type returned by
# b64encode() to UTF-8 encoding, save to variable
encoded = base64.b64encode(secret.encode('utf-8'))
# decode secret using b64decode(), save to variable
decoded = base64.b64decode(encoded)
print("The encoded string is: ", encoded.decode("utf-8"))
print("The decoded string is: ", decoded.decode("utf-8"))
