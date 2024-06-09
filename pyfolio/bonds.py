
from money import Money
from typing import Literal

class Bond:
    def __init__(self, principal: float, maturity, interest_rate: float, type: Literal['c','d'] = 'd'):      
        # Principal amount
        self.principal = Money(principal)
        # Date of maturity
        self.maturity = maturity
        # Market interest rate (discounting rate)
        self.interest_rate = interest_rate
    
        self.type = type

    def _principal_amount(self):
        return self.principal._amount

class ZeroCouponBond(Bond):

    def calculate_price(self):
        return self.principal.pv(r = self.interest_rate, n = self.maturity, type = self.type)

    def __repr__(self):
        return f"ZeroCouponBond({self.principal}, {self.maturity}, {self.interest_rate})"
      
class CouponBond(Bond):
    def __init__(self, rate: float):      
        # Rate of the bond
        self.rate = rate
        # Payments
        self.payments = []

    def __repr__(self):
        return f"CouponBondBond({self.principal}, {self.maturity}, {self.interest_rate})"     
    
    def calculate_price(self):
        # Discount the coupon payments
        for t in range(1, self.maturity + 1):
            payment =  Money(self._principal_amount * self.rate)
            self.payments.append(payment.pv(r = self.interest_rate, n = t, type = self.type))

        return sum(self.payments) + self.principal.pv(r = self.interest_rate, n = self.maturity, type = self.type)
