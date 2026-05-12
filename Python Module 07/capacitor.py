import ex1


def healing():
    print("Testing Creature with healing capability")
    print(" base:")
    creature = ex1.HealingCreatureFactory()
    base = creature.create_base()
    evolved = creature.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def transform():
    print("Testing Creature with transform capability")
    print(" base:")
    creature = ex1.TransformCreatureFactory()
    base = creature.create_base()
    evolved = creature.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main():
    # healing()
    # print()
    transform()


if __name__ == '__main__':
    main()
