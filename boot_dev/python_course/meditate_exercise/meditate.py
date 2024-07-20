
def meditate(mana, max_mana, energy, energy_potions):
    """
    while mana < max_mana or (energy == 0 and energy_potions == 0 and mana < max_mana):
          if (energy == 0 and energy_potions):
              energy_potions -= 1
              energy += 50
          while energy > 0:
              energy -= 1
              mana += 3
         return mana, energy, energy_potions
    """
    while mana < max_mana:
        if (energy > 0):
            energy -= 1
            mana += 3
        elif (energy == 0):
            if (energy_potions):
                energy_potions -= 1
                energy += 50
    return mana, energy, energy_potions

