from address import Address
from mailing import Mailing


to_address = Address("987", "Cochi", "kvadratnau", "5", "123")
from_address = Address("123", "Москва", "Круглая", "6", "45")


mailing = Mailing(to_address, from_address, 1000, "T-567")


print(mailing)
