def get_multiples_between(start, stop, factor):
   if start < 0 or stop < 0 or factor < 0:
    raise ValueError("Negative numbers are not allowed")
   elif factor == 0 : raise ValueError("Factor cannot be zero")
   elif start > stop : raise ValueError("Start number cannot be greater than stop number")
   elif start == stop : raise ValueError("Invalid range! Start number cannot be equal to stop number")
   else :
    return [multiples for multiples in range(start, stop + 1) if multiples % factor == 0 ]

