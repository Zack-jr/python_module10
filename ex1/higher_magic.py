def spell_combiner(spell1: callable, spell2: callable) -> callable:

    return lambda target: (spell1(target), spell2(target))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    def multiply():
        res = base_spell()
        res *= multiplier

        return res

    return multiply


def conditional_caster(condition: callable, spell: callable) -> callable:

    def trigger(target):
        if condition(target) is True:
            res = spell(target)
            return res
        else:
            return "Spell fizzled"

    return trigger


def spell_sequence(spells: list[callable]) -> callable:

    def cast(target):
        res = []
        for spell in spells:
            res.append(spell(target))
        return res

    return cast


# example functions
def fireball(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def base_spell():
    return 10


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    tup = combined("Dragon")

    res = ", ".join(e for e in tup)
    print(f"Combined spell result: {res}")

    print("\nTesting power amplifier...")
    combined = power_amplifier(base_spell, 3)
    before = base_spell()
    res = combined()
    print(f"Original: {before}, Amplified: {res}")

    print("Testing conditional caster...")
    combined = conditional_caster(str.isalpha, heal)
    res = combined("Dragon")
    print(f"\nConditional caster result: {res}")

    print("\nTesting spell sequence...")
    spell_list = [fireball, heal]
    combined = spell_sequence(spell_list)
    res = combined("Dragon")
    print(f"Spell sequence result: {res}")


if __name__ == '__main__':
    main()
