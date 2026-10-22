from simuduck.behaviors import FlyRocketPowered
from simuduck.ducks import DecoyDuck, MallardDuck, ModelDuck, RedheadDuck, RubberDuck


def test_mallard_composition():
    duck = MallardDuck()
    assert duck.perform_fly() == "flying with wings"
    assert duck.perform_quack() == "quack"


def test_redhead_composition():
    duck = RedheadDuck()
    assert duck.perform_fly() == "flying with wings"
    assert duck.perform_quack() == "quack"


def test_rubber_duck_composition():
    duck = RubberDuck()
    assert duck.perform_fly() == "cannot fly"
    assert duck.perform_quack() == "squeak"


def test_decoy_duck_composition():
    duck = DecoyDuck()
    assert duck.perform_fly() == "cannot fly"
    assert duck.perform_quack() == "(silence)"


def test_model_duck_starts_unable_to_fly():
    duck = ModelDuck()
    assert duck.perform_fly() == "cannot fly"
    assert duck.perform_quack() == "quack"


def test_same_model_duck_can_change_to_rocket_powered_flight():
    duck = ModelDuck()
    before = duck.perform_fly()
    duck.set_fly_behavior(FlyRocketPowered())
    after = duck.perform_fly()
    assert before == "cannot fly"
    assert after == "flying with a rocket"
