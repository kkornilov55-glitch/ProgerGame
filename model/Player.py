from dataclasses import dataclass


@dataclass()
class Player:
    _name: str
    _satiety: int
    _mental: int
    _productivity: int

    @property
    def name(self):
        return self._name

    @property
    def satiety(self):
        return self._satiety

    @property
    def mental(self):
        return self._mental

    @property
    def productivity(self):
        return self._productivity


