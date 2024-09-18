from nada_dsl import *

def nada_main():

    party = Party(name="user")

    num = SecretInteger(Input(name="num", party=party))

    rem = num % Intger(2)

    is_even = rem == Intger(0)
  

    return [Output(is_even, "is_even", party=party)]
