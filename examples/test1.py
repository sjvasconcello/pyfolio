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
        if not bool(discret):
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
        if not bool(discret):
            raise ValueError("discret must be Boolean")

        if discret:
            # Calculate future value with discrete interest
            return self.amount * (1 + r)**n
        else:
            # Calculate future value with continuous interest
            return self.amount * exp(r * n)
        
# %% 
class Bond:
    def __init__(self, principal: float, maturity, interest_rate: float):      
        # Principal amount
        self.principal = Money(principal)
        # Date of maturity
        self.maturity = maturity
        # Market interest rate (discounting rate)
        self.interest_rate = interest_rate

        self._principal_amount = float(self.principal.amount)

class ZeroCouponBond(Bond):
    def __init__(self, principal, maturity, interest_rate, discret: bool = True):
        super().__init__(principal, maturity, interest_rate)

        if not bool(discret):
            raise ValueError("discret must be Boolean")
        self.discret = discret

    def calculate_price(self):
        return self.principal.pv(r = self.interest_rate, n = self.maturity, discret = self.discret)

    def __repr__(self):
        return f"ZeroCouponBond({self._principal_amount}, {self.maturity}, {self.interest_rate})"
      
class CouponBond(Bond):
    def __init__(self, principal, maturity, interest_rate, rate: float, discret: bool  = True):
        super().__init__(principal, maturity, interest_rate) 
        # Rate of the bond
        self.rate = rate
       
        if not bool(discret):
            raise ValueError("discret must be Boolean")
        self.discret = discret

        # Payments
        self.payments = []

    def __repr__(self):
        return f"CouponBondBond({self._principal_amount}, {self.maturity}, {self.interest_rate})"     
    
    def calculate_price(self):
        # Discount the coupon payments
        for t in range(1, self.maturity + 1):
            amount_payment_t = float(self._principal_amount) * self.rate
            payment =  Money(amount_payment_t)
            self.payments.append(payment.pv(r = self.interest_rate, n = t, discret = self.discre))

        return sum(self.payments) + self.principal.pv(r = self.interest_rate, n = self.maturity, discret = self.discre)


# %%
