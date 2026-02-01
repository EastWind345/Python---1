from address import Address


class Mailing:
    def __init__(self, to_address: Address,
                 from_address: Address, cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f" OTPRAVLENIE {self.track} "
                f"iz {self.from_address.index}, "
                f" {self.from_address.city}, {self.from_address.street}, "
                f" {self.from_address.house} - {self.from_address.apartment} "
                f"v {self.to_address.index}, "
                f" {self.to_address.city}, {self.to_address.street}, "
                f"{self.to_address.house} - {self.to_address.apartment}. "
                f"STOIMOST {self.cost} rublei.")
