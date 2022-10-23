from env_setup import setup_postgre, setup_grafana
import logging

logging.basicConfig(level=logging.INFO)


def main():
    # Initialize local db
    setup_postgre()
    # Initialize local Grafana
    setup_grafana()
    # Initialize data loaders


if __name__ == '__main__':
    main()
