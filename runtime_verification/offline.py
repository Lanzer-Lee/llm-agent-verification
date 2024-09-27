from system.scenarios import Scenarios
from monitor import properties


def main():
    properties.weave()
    Scenarios().run_all_scenarios()


if __name__ == '__main__':
    main()
