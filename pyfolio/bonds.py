
from .money import Money
from .utils import validate_inputs

class Bond:
    def __init__(self, principal: float, maturity, interest_rate: float):      
        # Principal amount
        self.principal = Money(principal)
        # Date of maturity
        self.maturity = maturity
        # Market interest rate (discounting rate)
        self.interest_rate = interest_rate

    def _principal_amount(self):
        value = self.principal.amount
        return value

class ZeroCouponBond(Bond):
    def __init__(self, principal: float, maturity: float, interest_rate: float, discret: bool = True):
        super().__init__(principal, maturity, interest_rate)

        #if not isinstance(discret, bool):
        #    raise ValueError("discret must be Boolean")
        
        self.discret = discret

        params = {'principal': principal, 'maturity': maturity, 'interest_rate': interest_rate,'discret': discret}
        expected_types = {
            'principal': (int, float), 
            'maturity': (int, float), 
            'interest_rate': float,
            'discret': bool
        }
        validate_inputs(params, expected_types)

    def calculate_price(self):
        return self.principal.pv(r = self.interest_rate, n = self.maturity, discret = self.discret)

    def __repr__(self):
        return f"ZeroCouponBond({self.principal.amount}, {self.maturity}, {self.interest_rate})"
      
class CouponBond(Bond):
    def __init__(self, principal, maturity, interest_rate, rate: float, discret: bool  = True):
        super().__init__(principal, maturity, interest_rate) 
        # Rate of the bond
        self.rate = rate

        params = {'principal': principal, 'maturity': maturity, 'interest_rate': interest_rate, 'rate':rate, 'discret': discret}

        expected_types = {
            'principal': (int, float), 
            'maturity': (int, float), 
            'interest_rate': float,
            'rate': float,
            'discret': bool
        }
        validate_inputs(params, expected_types)

        self.discret = discret

        # Payments
        self.payments = []

    def __repr__(self):
        return f"CouponBond({self.principal.amount}, {self.maturity}, {self.interest_rate}, {self.rate})"     
    
    def calculate_price(self):
        # Discount the coupon payments
        amount_payment_t = float(self.principal.amount) * self.rate
        payment = Money(amount_payment_t)
        for t in range(1, self.maturity + 1):
            self.payments.append(payment.pv(r = self.interest_rate, n = t, discret = self.discret))

        return sum(self.payments) + self.principal.pv(r = self.interest_rate, n = self.maturity, discret = self.discret)

