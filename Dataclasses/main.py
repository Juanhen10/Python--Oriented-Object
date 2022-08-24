from dataclasses import dataclass, field


class Person:
    def __init__(self, name,lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        class_str = f'{self.__class__.__name__}'\
                    f'({self.name } {self.lastname})'
        return class_str

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.lastname == other.lastname

@dataclass(frozen=True, kw_only=False)
class Person:
    name: str
    lastname: str
    active: bool = False
    addresses: list = field(default_factory=list, repr= False, compare=True, kw_only=True)
    full_name: str = field(default='Missing', init=False, repr= False)

    def __post_init__(self):
        full_name = f'{self.name} '  \
            f'{self.lastname}'
        object.__setattr__(
            self,
            'full_name', full_name
        )
if __name__ == '__main__':
    john1 = Person('John', 'Doe',True, addresses=['R1'])
    john2 = Person('John', 'Doe', True, addresses=['R2'])
    print(john1)
    print(john2.full_name)
    print(john1 == john2)