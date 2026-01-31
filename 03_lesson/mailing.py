from address import Address


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.address = Address
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        mail_str = ", ".join([str(maili) for maili in self.mail])
        return f"{self.address} учится вместе с: {mail_str}"
