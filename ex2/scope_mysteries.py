def mage_counter() -> callable:
    counter = 0

    def func():
        nonlocal counter
        counter += 1
        return counter

    return func

    # nonlocal catches counter from inside
    # is useful for variable modifications


def spell_accumulator(initial_power: int) -> callable:

    def acc():
        nonlocal initial_power
        initial_power += 1
        return initial_power

    return acc


def enchantment_factory(enchantment_type: str) -> callable:

    def ench(item: str):
        nonlocal enchantment_type
        return f"{enchantment_type} {item}"

    return ench


def memory_vault() -> dict[str, callable]:

    keys_values = {}

    def store(key, value):
        keys_values.update({key: value})

    def recall(key):
        if key in keys_values.keys():
            return keys_values[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main():

    print("Testing mage counter...")

    func = mage_counter()
    i = 1
    while i <= 3:
        print(f"Call {i}: {func()}")
        i += 1

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(0)
    for i in range(3):
        print(f"Accumulating: {acc()}")

    print("\nTesting enchantment factory...")
    ench1 = enchantment_factory("Flaming")
    ench2 = enchantment_factory("Frozen")
    print(ench1("Sword"))
    print(ench2("Shield"))

    print("\nTesting memory vault...")
    mem_process = memory_vault()
    mem_process["store"]("mastercard", "6414132")
    print(f"Recall: {mem_process["recall"]("mastercard")}")
    print(mem_process["recall"]("visa"))


if __name__ == '__main__':
    main()
