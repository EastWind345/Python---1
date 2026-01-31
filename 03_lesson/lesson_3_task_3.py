from address import Address
from mailing import Mailing


maili = Address("123", "Москва", "Круглая", "6", "45")


mailing = Mailing(Address, [Mailing])


print(mailing)
