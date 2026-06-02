
import argparse

def load(filepath):
    """Loads datas from filepath to database"""
    try:
        with open(filepath)as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")




def main():
    print("Executing Dundie from entry point")

    parser = argparse.ArgumentParser(
    description = "Dunder Mifflin Rewards CLI",
    epilog = "Enjoy and use with cautions"
)
    parser.add_argument(
        "subcommand",
        type = str,
        help = "The subcomand to run",
        choices = ("load", "show", "send"),
    )

    parser.add_argument(
        "filepath",
        type = str,
        help = "Filepath to load",
    )

    args = parser.parse_args()
    
    globals()[args.subcommand](args.filepath)
    
    

if __name__ == "__main__":
    main()
