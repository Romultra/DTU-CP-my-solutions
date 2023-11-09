"""This file contains all the exercises relating to string exercise (10.1)."""

class ExtendedString(str):
    """Your expanded version of the python str class.""" 
    
    def to_snake_case(self):
        for char in self:
            if char == ' ':
                self = self.replace(' ', '_')
        return self.lower()
    
    def word_count(self):
        if self != "":
            count = 1
        else:
            count = 0

        for i, char in enumerate(self):
            if i != len(self)-1:
                if char == " " and self[i+1] != ' ':
                    count += 1
        
        return count