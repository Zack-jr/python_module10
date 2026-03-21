from time import time
from functools import wraps

class MagicGuild:

    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if name == self.name:
            return True
        else:
            return False
    
    def cast_spell(self, spell_name: str, power: int) -> str:
        pass
    

@timing_val
def spell_timer(func: callable) -> callable:

    def wrapper(func):
        print(f"Casting {func}...")
        t1 = time()
        func()
        t2 = time()
        print(f"Spell completed in {t1-t2} seconds")

def power_validator(min_power: int) -> callable:
    pass

def retry_spell(max_attempts: int) -> callable:
    pass

def main():
    pass


if __name__ == '__main__':
    pass

