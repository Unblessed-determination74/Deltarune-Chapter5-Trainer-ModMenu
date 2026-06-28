from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B51F
    hp_current: int = 0x2F7
    hp_max: int = 0x2FB
    atk: int = 0x2FF
    def_: int = 0x303
    magic: int = 0x307
    gold: int = 0x31F
    inventory_ptr: int = 0x33F
    battle_flag: int = 0x377
    timer: int = 0x38F
    items_base: int = 0x2A4B60F

CURRENT_OFFSETS = Offsets()
