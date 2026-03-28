import argparse, sys
from datetime import date

from aoc import puzzles
from aoc.config import config
from aoc.puzzles.solve import *

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", metavar="", type=str, help="specify the year to select")
    parser.add_argument("-d", "--day", metavar="", type=str, help="specify the day to select")
    parser.add_argument("-p", "--part", metavar="", type=str, help="specify the part to select")
    parser.add_argument("-l", "--latest", help="execute latest solution", action="store_true")
    args = parser.parse_args()


    if args.latest:
        year, day, part = get_latest()
        display_header(year, day, part)
        check, solution, error = solve(year, day, part)

    else:
        # Get year
        year = args.year
        valid_year_from = config.get("aoc", "start_year")
        valid_year_to = date.today().year - 1 if date.today().month < 12 else date.today().year
        
        while True:
            try:
                year = int(year)
                if year < valid_year_from or year > valid_year_to:
                    raise ValueError

            except:
                year = input(f"Select a valid year ({valid_year_from}-{valid_year_to}): ")
                print("\033[F\033[K", end='')
            
            else:
                break

        # Get day
        day = args.day
        valid_day_from = 1
        valid_day_to = config.get("aoc", "end_day")
        
        while True:
            try:
                day = int(day)
                if day < valid_day_from or day > valid_day_to:
                    raise ValueError

            except:
                day = input(f"Select a valid day ({valid_day_from}-{valid_day_to}): ")
                print("\033[F\033[K", end='')
            
            else:
                break

        # Get part
        part = args.part
        valid_part_from =  config.get("aoc", "start_part")
        valid_part_to =  config.get("aoc", "end_part")
        
        while True:
            try:
                part = int(part)
                if part < valid_part_from or part > valid_part_to:
                    raise ValueError

            except:
                part = input(f"Select a valid part ({valid_part_from}-{valid_part_to}): ")
                print("\033[F\033[K", end='')
            
            else:
                break
        
        display_header(year, day, part)
        check, solution, error = solve(year, day, part)
    
    if not check:
        display_error(error)
        sys.exit(1)

    display_solution(year, day, part, solution)



def display_header(year, day, part):
    print(f"{'#'*70}\n#{f'Holmgrens Advent of Code'.center(68, ' ')}#\n#{f''.center(68, ' ')}#\n#{f'Solving puzzle part {part} at {day:02}/12/{year}'.center(68, ' ')}#\n{'#'*70}")

def display_solution(year, day, part, solution):
    print(f"\n{f'Solution for puzzle part {part} at {day:02}/12/{year}:'.center(70, ' ')}\n\n{f'{'-'*50}'.center(70, ' ')}\n\n{f'{solution}'}\n\n{'#'*70}")

def display_error(error):
    print(f"\n{f'Something went wrong trying to solve the puzzle:'.center(70, ' ')}\n\n{f'{'-'*50}'.center(70, ' ')}\n\n{f'{error}'}\n\n{'#'*70}")

if __name__ == "__main__":
    main()