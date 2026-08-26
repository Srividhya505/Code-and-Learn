class Attendance:
    def __init__(self,st):
        self.students=st
        self.roll_no=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.roll_no < len(self.students):
            name=self.students[self.roll_no]
            self.roll_no+=1
            return name
        else:
            raise StopIteration
st1=Attendance(["vidhya","prathyu","nandu","cherry"])
st2=Attendance(["valli","poli","guna","sidd"])



class Even:
    def __init__(self,l):
        self.l = l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            n=self.l[self.index]
            self.index+=1
            if n%2==0:
                return n
            else:
                return next(self)


# create a custom iterator that takes a whole sentence and returns the non-vowels only.
class NonVowelIterator:
    def __init__(self, sen):
        self.sen= sen
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.sen):
            char = self.sen[self.index]
            self.index += 1
            if char.lower() not in "aeiou":
                return char
        raise StopIteration
sentence = input("Enter a sentence: ")
obj = NonVowelIterator(sentence)
for char in obj:
    print(char, end="")



class Sen:
    def __init__(self,s):
        self.s=0
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i<len(self.s):
            self.i+=1
            if self.s[self.i-1] not in "AEIOUaeiou" :
                return self.s[self.i-1]
        raise StopIteration


# create a custom iterator that takes the string and returns Ascii values of the character.
class Asciivalues:
    def __init__(self,s):
        self.s=0
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<len(self.s):
            self.i+=1
            return ord(self.s[self.i-1])
        else:
            raise StopIteration