def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    sorted_artifacts = sorted(artifacts, key=lambda x: x["power_lvl"],
                              reverse=True)

    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    powerful_mages = list(filter(lambda x: x["power"] >= min_power, mages))

    return powerful_mages


def spell_transformer(spells: list[str]) -> list[str]:

    new_spells = list(map(lambda x: "* " + x + " *", spells))
    return new_spells


def mage_stats(mages: list[dict]) -> dict:

    best_mage = max(mages, key=lambda x: x["power"])
    worst_mage = min(mages, key=lambda x: x["power"])
    avg = sum(map(lambda x: x["power"], mages)) / len(mages)

    return {"strongest": best_mage,
            "weakest": worst_mage,
            "avg": avg}


def main():

    a1 = {"name": "cursed_dagger",
          "type": "attack_boost",
          "power_lvl": 69}

    a2 = {"name": "Fire Staff",
          "type": "fire_damage_amp",
          "power_lvl": 92}
    a3 = {"name": "Crystal Orb",
          "type": "heal",
          "power_lvl": 85}

    m1 = {"name": "Ice Wizard", "power": 120, "element": "Ice"}
    m2 = {"name": "Fire Wizard", "power": 150, "element": "Fire"}
    m3 = {"name": "Dark Wizard", "power": 150, "element": "Darkness"}

    artifacts = [a1, a2, a3]
    mages = [m1, m2, m3]
    spells = ["Fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power_lvl']} power) comes before"
          f" {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power_lvl']} power)")

    print("\nTesting spell transformer...")
    new_spells = " ".join(spell_transformer(spells))
    print(new_spells)

    print("\nTesting power filter...")
    print(f"Powerful mages: {power_filter(mages, 150)}")

    print("\nTesting mage stats...")
    print(f"Mage stats: {mage_stats(mages)}")


if __name__ == '__main__':
    main()

# lamda function format example: output = lambda x: expression
# x is the input, the expression can be a function/loop/calculation
