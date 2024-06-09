
from .money import Money
from typing import Literal

class Bond:
    def __init__(self, principal: float, maturity, interest_rate: float, type_m: Literal['c','d'] = 'd'):      
        # Principal amount
        self.principal = Money(principal)
        # Date of maturity
        self.maturity = maturity
        # Market interest rate (discounting rate)
        self.interest_rate = interest_rate
    
        self.type_m = type_m

    def _principal_amount(self):
        return self.principal._amount

class ZeroCouponBond(Bond):
    def __init__(self, principal, maturity, interest_rate, type_m: Literal['c','d'] = 'd'):
        super().__init__(principal, maturity, interest_rate, type_m)

    def calculate_price(self):
        return self.principal.pv(r = self.interest_rate, n = self.maturity, type = self.type_m)

    def __repr__(self):
        return f"ZeroCouponBond({self._principal_amount}, {self.maturity}, {self.interest_rate})"
      
class CouponBond(Bond):
    def __init__(self, principal, maturity, interest_rate, rate: float, type_m: Literal['c','d'] = 'd'):
        super().__init__(principal, maturity, interest_rate, type_m) 
        # Rate of the bond
        self.rate = rate
        # Payments
        self.payments = []

    def __repr__(self):
        return f"CouponBondBond({self._principal_amount}, {self.maturity}, {self.interest_rate})"     
    
    def calculate_price(self):
        # Discount the coupon payments
        for t in range(1, self.maturity + 1):
            payment =  Money(self._principal_amount * self.rate)
            self.payments.append(payment.pv(r = self.interest_rate, n = t, type = self.type_m))

        return sum(self.payments) + self.principal.pv(r = self.interest_rate, n = self.maturity, type = self.type_m)
