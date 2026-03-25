from aoc.utilities.register import puzzles
from datetime import date
import aoc.solutions, argparse, os, platform


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", metavar="", type=int, help="specify the year to select")
    parser.add_argument("-d", "--day", metavar="", type=str, help="specify the day to select")
    parser.add_argument("-p", "--part", metavar="", type=str, help="specify the part to select")
    parser.add_argument("-l", "--latest", help="execute latest solution", action="store_true")
    args = parser.parse_args()

    # Get latest puzzle if "-l"
    if args.latest:
        latest_year = next(reversed(puzzles))
        latest_day = next(reversed(puzzles[latest_year]))
        latest_part = next(reversed(puzzles[latest_year][latest_day]))
        selected_puzzle = puzzles[latest_year][latest_day].get(latest_part)

    else:
        # Get year
        selected_year = args.year
        valid_year_from = 2015
        valid_year_to = date.today().year - 1 if date.today().month < 12 else date.today().year
        
        while True:
            if selected_year != None:
                try:
                    selected_year = int(selected_year)

                    if selected_year < valid_year_from or selected_year > valid_year_to:
                        raise ValueError

                except:
                    print("\033[F\033[K", end='')
                    print(f"Year must be a number in range {valid_year_from}-{valid_year_to}")

                else:
                    if selected_year in puzzles:
                        break

                    print("\033[F\033[K", end='')
                    print(f"Year \"{selected_year}\" does not exist in puzzle solutions")

            selected_year = input("Select a year: ")

        # Get day
        selected_day = args.day
        valid_day_from = 1
        valid_day_to = 25

        while True:
            if selected_day != None:
                try:
                    selected_day = int(selected_day)

                    if selected_day < valid_day_from or selected_day > valid_day_to:
                        raise ValueError

                except:
                    print("\033[F\033[K", end='')
                    print(f"Day must be a number in range {valid_day_from}-{valid_day_to}")

                else:
                    if selected_day in puzzles[selected_year]:
                        break

                    print("\033[F\033[K", end='')
                    print(f"Day \"{selected_day}\" in year \"{selected_year}\" does not exist in puzzle solutions")
        
            selected_day = input("Select a day: ")

        # Get part 
        selected_part = args.part
        valid_part_from = 0
        valid_part_to = 2

        while True:
            if selected_part != None:
                try:
                    selected_part = int(selected_part)

                    if selected_part < valid_part_from or selected_part > valid_part_to:
                        raise ValueError

                except:
                    print("\033[F\033[K", end='')
                    print(f"Part must be a number in range {valid_part_from}-{valid_part_to}")

                else:
                    if selected_part in puzzles[selected_year][selected_day]:
                        break

                    print("\033[F\033[K", end='')
                    print(f"Part \"{selected_part}\" at day \"{selected_day}\" in year \"{selected_year}\" does not exist in puzzle solutions")

            selected_part = input("Select part: ")
        
        selected_puzzle = puzzles[selected_year][selected_day].get(selected_part)
    
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(f"{'#'*70}\n#{f'Holmgrens Advent of Code'.center(68, ' ')}#\n#{f''.center(68, ' ')}#\n#{f'Solving puzzle part {selected_part} at {selected_day:02}/12/{selected_year}'.center(68, ' ')}#\n{'#'*70}")
    selected_puzzle()


    # insert into loop
    """
    user_input = input("Enter command: ").strip().lower()
    func = puzzles.get(user_input)
    if func:
        func()  # runs the registered function
    else:
        # Could not find day
        # or
        # not a real day
        # q exits the program (directly?)
        print(f"Unknown command: {user_input}")
    """
if __name__ == "__main__":
    main()