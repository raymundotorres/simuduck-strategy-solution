from simuduck.behaviors import (
    FlyNoWay,
    FlyRocketPowered,
    FlyWithWings,
    MuteQuack,
    Quack,
    Squeak,
)


def test_fly_with_wings():
    assert FlyWithWings().fly() == "flying with wings"


def test_fly_no_way():
    assert FlyNoWay().fly() == "cannot fly"


def test_fly_rocket_powered():
    assert FlyRocketPowered().fly() == "flying with a rocket"


def test_quack():
    assert Quack().quack() == "quack"


def test_squeak():
    assert Squeak().quack() == "squeak"


def test_mute_quack():
    assert MuteQuack().quack() == "(silence)"
