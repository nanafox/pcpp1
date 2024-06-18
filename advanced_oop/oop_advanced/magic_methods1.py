from pydantic import BaseModel


class SlotSchema(BaseModel):
    a: int
    b: int


class SlotBasedClass:
    """A slot-based class"""

    __slots__ = ["a", "b"]

    def __init__(self, *, a: int, b: int):
        SlotSchema(a=a, b=b)
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

    def __delattr__(self, name: str) -> None:
        raise AttributeError("Cannot delete attributes")

    def __contains__(self, item: int) -> bool:
        return item in [self.a, self.b]

    def __iter__(self):
        for attr in self.__slots__:
            yield getattr(self, attr)

    def __len__(self):
        return len(self.__slots__)


sbc = SlotBasedClass(a=1, b=2)
print(sbc)
