
#Python Script to evaluate password strength

class PasswordAnalyzer:
    def __init__  (self, password):
        self.password = password

#To check for Password complexity (out of 100, max per 25)
#• Uppercase letters (A–Z) (25 if upper)
#• Lowercase letters (a–z) (25 if lower)
#• Numbers (0–16)  (5 points if less than 8) (10 if 10) (15 if 12) (20 if 14) (25 if 16)
#• Special characters/symbols (like @, #, $, %, !, or spaces)

    def length_check(self):
        if len(self.password) in range(0,9):
            return 5
        
        if len(self.password) in range(9,11):
            return 10

        if len(self.password) in range(11,13):
            return 15

        if len(self.password) in range(13,15):
            return 20

        if len(self.password) > 14:
            return 25



    def special_char_check(self):
        special_char = {"@", "#", "$", "%", "!"}
        contains_special = any(char in self.password for char in special_char)

        if contains_special == True:
            return 25

        else:
            return 0



    def lowercase_check(self):
        lowercase_check = any(char.islower() for char in self.password)
        if lowercase_check == True:
            return 25
        else:
            return 0


    def uppercase_check(self):
        uppercase_check = any(char.isupper() for char in self.password)
        if uppercase_check == True:
            return 25
        else:
            return 0


    def score_calc(self):
        score = self.length_check() + self.special_char_check() + self.uppercase_check() + self.lowercase_check()

        if score in range (0, 26):
            print ("Weak password")

        if score in range (26, 51):
            print ("Okay password")

        if score in range (51, 76):
            print ("Good password")

        if score in range (76, 101):
            print ("Great password")
        print(score)






user_password = input("Please enter a password: ")

analyzer = PasswordAnalyzer(user_password)
analyzer.score_calc()

