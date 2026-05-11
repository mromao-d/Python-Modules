def single_function(fact_obj: CreatureFactory) -> None:
    base = fact_obj.create_base()
    evolved = fact_obj.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def another_function(fact1: FlameFactory, fact2: AquaFactory) -> None:
    flame = fact1.create_base()
    aqua = fact2.create_base()

    print(flame.describe())
    print(" vs.")
    print(aqua.describe())
    print(" fight!")
    print(flame.attack())
    print(aqua.attack())

if __name__ == '__main__':
    flame = FlameFactory()
    aqua = AquaFactory()

    single_function(flame)
    single_function(aqua)
    another_function(flame, aqua)
