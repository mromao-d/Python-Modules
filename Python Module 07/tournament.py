from ex2 import FlameFactory, AquaFactory, HealingCreatureFactory, TransformCreatureFactory, NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(
        data: list[tuple[FlameFactory | AquaFactory | HealingCreatureFactory | TransformCreatureFactory, NormalStrategy | AggressiveStrategy | DefensiveStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(data)} opponents involved")
    for i in range(len(data) - 1):
        creature1, stategy1 = data[i]
        creature_type1 = creature1().create_base()
        for j in range(i + 1, len(data)):
            try:
                print() 
                print("* Battle *")
                print(creature_type1.describe())

                creature2, stategy2 = data[j]
                creature_type2 = creature2().create_base()

                print(" vs.")
                print(creature_type2.describe())

                print(" now fight")
                for action in stategy1().act(creature_type1):
                    print(action)
                for action in stategy2().act(creature_type2):
                    print(action)
            except Exception as e:
                print(e)
    return None


def main():
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print()
    battle([(FlameFactory, NormalStrategy), (HealingCreatureFactory, DefensiveStrategy)])

    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print()
    battle([(FlameFactory, AggressiveStrategy), (HealingCreatureFactory, DefensiveStrategy)])

    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print()
    battle([(AquaFactory, NormalStrategy), (HealingCreatureFactory, DefensiveStrategy), (TransformCreatureFactory, AggressiveStrategy)])



if __name__ == '__main__':
    main()
