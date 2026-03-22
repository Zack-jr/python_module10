from time import perf_counter, sleep
from functools import wraps


def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        t1 = perf_counter()
        res = func()
        t2 = perf_counter()
        print(f"Spell completed in {t2-t1:.3f} seconds")
        return res

    return wrapper


def power_validator(min_power: int) -> callable:

    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):

            power = kwargs.get('power') if 'power' in kwargs else args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:

    def decorator(func: callable):

        @wraps(func)
        def wrapper():

            failed_attempts = 0
            while failed_attempts < max_attempts:
                try:
                    return func()
                except Exception:
                    print("Spell failed, retrying")
                    failed_attempts += 1

            if failed_attempts is max_attempts:
                return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


# start of example functions ---
def fireball():

    sleep(0.101)
    return "Fireball cast!"


@power_validator(50)
def cast_meteor(power: int):
    return "Meteor Cast!"


@retry_spell(5)
def provoke_error():
    return 1 / 0

# end of example functions ---


class MagicGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:

        if len(name) > 3 and any(c.isalpha() and c.isspace() for c in name):
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():

    print("\nTesting spell timer...")
    timer = spell_timer(fireball)
    print(f"Result: {timer()}")

    print("\nTesting power validator...")
    print(cast_meteor(51))
    print(cast_meteor(10))

    print("\nTesting retry spell...")
    print(provoke_error())

    print("\nTesting MageGuild...")
    magicguild = MagicGuild()
    print(magicguild.validate_mage_name("Merlin"))
    print(magicguild.validate_mage_name(""))
    print(magicguild.cast_spell("Lightning", power=15))
    print(magicguild.cast_spell("Explosion", power=9))


if __name__ == '__main__':
    main()
