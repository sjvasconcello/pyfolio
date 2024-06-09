
from math import exp
from typing import Literal

class Money:
    def __init__(self,  amount: float = 0):
        # Amount (money)
        self.amount = amount
    
    def _amount(self):
        return self.amount

    def pv(self, r: float, n: int, type: Literal['c','d'] = 'd') -> float:
        match type:
            case 'd':
                return self.amount*(1 + r)**-n
            case 'c':
                return self.amount*exp(-r*n)
            case _:
                raise ValueError(f"Invalid argument: {type}")

    def fv(self, r: float, n: int, type: Literal['c','d'] = 'd') -> float:
        match type:
            case 'd':
                return self.amount*(1 + r)**n
            case 'c':
                return self.amount*exp(r*n)
            case _:
                raise ValueError(f"Invalid argument: {type}")



