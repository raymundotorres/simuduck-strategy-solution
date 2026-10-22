# SimUDuck Strategy Pattern — Possible Solution

This repository contains **one possible reference implementation** of the SimUDuck Strategy exercise.

Keep it unavailable to students until the submission deadline has passed.

## Design

`Duck` remains the abstract base class for Duck identity / display behavior.

Flying and quacking are moved into two independent Strategy families.

### Fly Strategy

- `FlyBehavior`
- `FlyWithWings`
- `FlyNoWay`
- `FlyRocketPowered`

### Quack Strategy

- `QuackBehavior`
- `Quack`
- `Squeak`
- `MuteQuack`

`Duck` composes one object from each family and delegates through:

- `perform_fly()`
- `perform_quack()`

## Initial combinations

| Duck | Fly behavior | Quack behavior |
| --- | --- | --- |
| `MallardDuck` | `FlyWithWings` | `Quack` |
| `RedheadDuck` | `FlyWithWings` | `Quack` |
| `RubberDuck` | `FlyNoWay` | `Squeak` |
| `DecoyDuck` | `FlyNoWay` | `MuteQuack` |
| `ModelDuck` | `FlyNoWay` | `Quack` |

`ModelDuck` can later replace only its flying Strategy with `FlyRocketPowered`.

## What varies?

- how a Duck flies,
- how a Duck quacks.

These behaviors vary independently from Duck identity.

## What stays stable?

- Duck identity,
- `display()`,
- `swim()`,
- the delegation mechanism in `Duck`.

## Why inheritance alone became awkward

Inheritance was mixing different dimensions of variation. Duck identity belongs in the Duck hierarchy, but flying and quacking do not align cleanly with that hierarchy.

## Complexity cost

Strategy introduces:

- additional classes,
- more objects,
- dependency wiring,
- another level of indirection.

That cost is justified when the behavior families actually vary and are reused independently.

## OOP constraint

This implementation intentionally uses:

- abstract base classes,
- concrete Strategy classes,
- inheritance for Strategy contracts,
- composition,
- constructor injection,
- setter injection for the runtime behavior change.

It does not use standalone functions, lambdas, callbacks, or other functional-programming alternatives.

## Run tests

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```
