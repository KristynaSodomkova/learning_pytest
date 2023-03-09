from dataclasses import dataclass, field
@dataclass
class Player:
    first_name: str
    last_name: str
    guardians: list = field(default_factory=list)

    def add_guardian(self, guardian):
        self.guardians.append(guardian)