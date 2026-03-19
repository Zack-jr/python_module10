def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    print("Testing artifact sorter...")
    sorted_artifacts = sorted(artifacts, key=lambda x: x["power_lvl"])
    
    return sorted_artifacts

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    

def spell_transformer(spells: list[str]) -> list[str]:
    pass

def mage_stats(mages: list[dict]) -> dict:
    pass


def main():

    a1 = {"name": "cursed_dagger", "type":"attack_boost", "power_lvl": 111}
    a2 = {"name": "fire staff", "type": "fire_damage_amp", "power_lvl": 22}
    a3 = {"name": "Crystal Orb", "type": "heal", "power_lvl": 56}

    m1 = {"name": "Ice Wizard", "power": 120, "element": "Ice"}
    m2 = {"name": "Fire Wizard", "power": 120, "element": "Fire"}
    m3 = {"name": "Dark Wizard", "power": 150, "element": "Darkness"}

    artifacts = [a1, a2, a3]
    mages = [m1, m2, m3]
    spells = ["Fireball", "Electric shock", "Mind Control"]

    

    print(artifact_sorter(artifacts))


if __name__ == '__main__':
    main()