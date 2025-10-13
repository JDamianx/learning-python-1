IS_ALIVE        = 1 << 0   # bit 0 → 00000001 → 1
IS_VISIBLE      = 1 << 1   # bit 1 → 00000010 → 2
IS_FLYING       = 1 << 2   # bit 2 → 00000100 → 4
IS_POISONED     = 1 << 3   # bit 3 → 00001000 → 8
HAS_LOOT        = 1 << 4   # bit 4 → 00010000 → 16
IS_INVINCIBLE   = 1 << 5   # bit 5 → 00100000 → 32
npc_flags = IS_ALIVE | IS_VISIBLE | HAS_LOOT
# czyli: 1 + 2 + 16 = 19 → 0b00010011
npc_flags = npc_flags & ~HAS_LOOT #turning off
npc_flags = npc_flags ^ IS_FLYING #toggle
if npc_flags & IS_POISONED:
    print("NPC is poisoned!")#checking bool
def print_flags(flags):
    print("ALIVE:",      bool(flags & IS_ALIVE))
    print("VISIBLE:",    bool(flags & IS_VISIBLE))
    print("FLYING:",     bool(flags & IS_FLYING))
    print("POISONED:",   bool(flags & IS_POISONED))
    print("HAS LOOT:",   bool(flags & HAS_LOOT))
    print("INVINCIBLE:", bool(flags & IS_INVINCIBLE))
npc_flags = IS_ALIVE | IS_VISIBLE | IS_POISONED
print_flags(npc_flags)
npc=0b00000000
npc=npc^((1<<0)|(1<<4))
npc=npc&~((1<<1)|(1<<2))
npc=npc&~HAS_LOOT
npc=npc^IS_FLYING
if npc & IS_POISONED:
    print("npc is poisoned!")
else:
    print("czysty jak łza")
if npc & (IS_ALIVE|IS_FLYING):
    print("npc zyje i lata")
else:
    print("albo nie żyje albo nie lata")
