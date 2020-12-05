class IOString():
    
    def get_String(self):
        self.str1 = input()
        self.str2 = input()
        self.str3 = input()

    def print_String(self):
        print(self.str1.upper())
        print(self.str2.upper())
        print(self.str3.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
