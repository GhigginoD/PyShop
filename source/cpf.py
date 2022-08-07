import re
class Cpf(): 
    QUANTITY_CARACTERES_CPF = 11
    DIGIT_1_FACTOR = 10
    DIGIT_2_FACTOR = 11

    def __init__(self,cpf:str):
        self.cpf = re.sub(r'\D+','', cpf.strip())
        self.validate()
    
    def validate(self):
        if self.is_empty_string(): raise ValueError("cpf empty")
        if self.is_wrong_size():  raise ValueError("wrong cpf size")
        if self.is_digits_invalids(): raise ValueError("cpf invalid")

    def is_empty_string(self) -> bool:
        return True if not self.cpf else False
        
    def is_wrong_size(self) -> bool:
        return True if len(self.cpf) != self.QUANTITY_CARACTERES_CPF else False

    def is_digits_invalids(self)-> bool:
        digit_1 = self.calculate_digit(self.DIGIT_1_FACTOR)
        digit_2 = self.calculate_digit(self.DIGIT_2_FACTOR)
        print(f"{digit_1}{digit_2}")
        return True if self.cpf[-2:] != f"{digit_1}{digit_2}" else False

    def calculate_digit(self, factor:int)->int :
        total = 0
        for digit in self.cpf[:factor]:
            if (factor > 1):
                total += int(digit) * (factor)
                factor -= 1
        rest = total % 11
        return  0 if (rest < 2)  else  11 - rest
    