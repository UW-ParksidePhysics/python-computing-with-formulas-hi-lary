# densities

V = 1000  # Volume in milliliters
Di = 7.87  # density of iron
Da = 0.0001225  # density of air
Dg = 0.7489  # density of gasoline
Dh = 0.985  # density of human
Ds = 10.49  # density of silver
Dp = 21.45  # density of platinum


def masses():
    mass_iron = Di * V
    mass_air = Da * V
    mass_gas = Dg * V
    mass_human = Dh * V
    mass_silver = Ds * V
    mass_plat = Dp * V
    return mass_iron, mass_air, mass_gas, mass_human, mass_silver, mass_plat


print(f' 1 Liter of iron is {masses()[0]} grams')
print(f' 1 Liter of air is {masses()[1]} grams')
print(f' 1 Liter of gasoline is {masses()[2]} grams')
print(f' 1 Liter of "human" is {masses()[3]} grams')
print(f' 1 Liter of silver is {masses()[4]} grams')
print(f' 1 Liter of platinum is {masses()[5]} grams')
