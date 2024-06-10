#%%
from math import exp

class Money:
    def __init__(self, amount: float = 0):
        """
        Initializes an instance of the Money class.

        :param amount: Initial amount of money, defaults to 0.
        """
        # Amount of money
        self.amount = amount
    
    def amount(self):
        """
        Returns the amount of money.

        :return: The amount of money.
        """
        return self.amount

    def pv(self, r: float, n: int, discret: bool = True) -> float:
        """
        Calculates the present value (PV) of money.

        :param r: Interest rate.
        :param n: Number of periods.
        :param discret: Indicates whether to use discrete (True) or continuous (False) interest.
        :return: The present value of the money.
        """
        if not isinstance(discret, bool):
            raise ValueError("discret must be Boolean")
          
        if discret:
            # Calculate present value with discrete interest
            return self.amount * (1 + r)**-n
        else:
            # Calculate present value with continuous interest
            return self.amount * exp(-r * n)


    def fv(self, r: float, n: int, discret: bool = True) -> float:
        """
        Calculates the future value (FV) of money.

        :param r: Interest rate.
        :param n: Number of periods.
        :param discret: Indicates whether to use discrete (True) or continuous (False) interest.
        :return: The future value of the money.
        """
        if not isinstance(discret, bool):
            raise ValueError("discret must be Boolean")

        if discret:
            # Calculate future value with discrete interest
            return self.amount * (1 + r)**n
        else:
            # Calculate future value with continuous interest
            return self.amount * exp(r * n)