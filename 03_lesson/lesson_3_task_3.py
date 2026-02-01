from address import Address
from mailing import Mailing


mail = Address("123", "Москва", "Круглая", "6", "45")
maili = Mailing("Москва", "Круглая", "900", "Lhy")
maili1 = Mailing("Москва", "Малиновая", "600", "kiuh")
cost = Mailing("Москва", "Малиновая", "600", "kiuh")
track = Mailing("Москва", "Малиновая", "600", "kiuh")

mailing = Mailing(Address, [mail, maili, maili1, cost, track])


print(mailing)
