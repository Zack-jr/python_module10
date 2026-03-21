from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:

    if operation == 'multiply':
        res = reduce(mul, spells)
        return res

    elif operation == 'add':
        res = reduce(add, spells)
        return res

    elif operation == 'max':
        res = max(spells)
        return res

    elif operation == 'min':
        res = min(spells)
        return res


def base_enchantment(power: int, element: str, target: str):

    return f"{element} enchant hits {target} with power {power}."


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    firefunction = partial(base_enchantment, 50, "Fire")
    icefunction = partial(base_enchantment, 50, "Ice")
    lightningfunction = partial(base_enchantment, 50, "Lightning")
    return {'fire_enchant': firefunction,
            'ice_enchant': icefunction,
            'lightning_enchant': lightningfunction}


@lru_cache
def memorized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def dispatcher(value: any):
        return "Unknown spell type"

    @dispatcher.register
    def _(value: int):
        return f"Damage spell with power {value}"

    @dispatcher.register
    def _(value: str):
        return f"{value} enchantment"

    @dispatcher.register
    def _(value: list):
        return f"{', '.join(v.capitalize() for v in value)}"

    return dispatcher


def main():

    print("\nTesting spell reducer...")
    numbers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(numbers, "add")}")
    print(f"Product: {spell_reducer(numbers, "multiply")}")
    print(f"Max: {spell_reducer(numbers, "max")}")
    print(f"Min: {spell_reducer(numbers, "min")}")

    print("\nTesting partial enchanter...")
    spellbook = partial_enchanter(base_enchantment)
    print(spellbook['fire_enchant']("Goblin"))
    print(spellbook['ice_enchant']("Dragon"))
    print(spellbook['lightning_enchant']("Elf"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memorized_fibonacci(10)}")
    print(f"Fib(15): {memorized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    words = ["apple", "samsung", "google"]
    spell = spell_dispatcher()
    print(f"Integer: {spell(50)}")
    print(f"String: {spell("Fire")}")
    print(f"Multi-cast: {spell(words)}")


if __name__ == '__main__':
    main()
