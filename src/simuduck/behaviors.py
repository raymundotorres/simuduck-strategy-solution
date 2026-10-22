from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> str:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> str:
        return "flying with wings"


class FlyNoWay(FlyBehavior):
    def fly(self) -> str:
        return "cannot fly"


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> str:
        return "flying with a rocket"


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> str:
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self) -> str:
        return "quack"


class Squeak(QuackBehavior):
    def quack(self) -> str:
        return "squeak"


class MuteQuack(QuackBehavior):
    def quack(self) -> str:
        return "(silence)"
