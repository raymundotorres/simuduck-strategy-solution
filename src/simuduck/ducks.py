from abc import ABC, abstractmethod

from .behaviors import (
    FlyBehavior,
    FlyNoWay,
    FlyWithWings,
    MuteQuack,
    Quack,
    QuackBehavior,
    Squeak,
)


class Duck(ABC):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self) -> str:
        return "swimming"

    def perform_fly(self) -> str:
        return self.fly_behavior.fly()

    def perform_quack(self) -> str:
        return self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> str:
        raise NotImplementedError


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> str:
        return "mallard duck"


class RedheadDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> str:
        return "redhead duck"


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self) -> str:
        return "rubber duck"


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), MuteQuack())

    def display(self) -> str:
        return "decoy duck"


class ModelDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())

    def display(self) -> str:
        return "model duck"
