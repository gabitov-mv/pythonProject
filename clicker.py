# def base64_to_base10(str):
#     x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#     y = 0
#     for i, j in enumerate(str[::-1]):
#         for k, n in enumerate(x):
#             if j == n:
#                 y += k * 64 ** i
#                 break
#
#     return y
#
# base64_to_base10("WIN")

class VigenereCipher(object):
    def __init__(self, password, alphabet):
        self.password = password
        self.alphabet = alphabet
        self.password_index = []
        self.text_index = []

    def text_to_index(self, text):
        for i in text:
            if i in self.alphabet:
                self.text_index.append(self.alphabet.find(i))
            if i not in self.alphabet:
                self.text_index.append(i)

    def password_to_index(self, text):
        while len(self.password_index) < len(text):
            for i in self.password:
                if i in self.alphabet:
                    self.password_index.append(self.alphabet.find(i))
                if i not in self.alphabet:
                    self.password_index.append(i)

    def encode(self, text):
        self.text_index.clear()
        self.password_index.clear()
        result = ""

        self.text_to_index(text)
        self.password_to_index(text)

        for i in range(len(self.text_index)):
            if isinstance(self.text_index[i], int) and isinstance(self.password_index[i], int):
                x = self.text_index[i] + self.password_index[i]
                result += self.alphabet[x if x < len(self.alphabet) else x - len(self.alphabet)]
            else:
                result += self.text_index[i]

        return result

    def decode(self, text):
        self.text_index.clear()
        self.password_index.clear()
        result = ""

        self.text_to_index(text)
        self.password_to_index(text)

        for i in range(len(self.text_index)):
            if isinstance(self.text_index[i], int) and isinstance(self.password_index[i], int):
                x = self.text_index[i] - self.password_index[i]
                result += self.alphabet[x if x > -1 else x + len(self.alphabet)]
            else:
                result += self.text_index[i]

        return result


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

for i in 'codewars', 'waffles', 'CODEWARS':
    c.encode(i)
    c.decode(i)
