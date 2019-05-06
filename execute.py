import sys, getopt

from the_race.read_file_race import ReadFileRace
from the_race.the_race import TheRace


def usage():
    help_text = """ 
    Help usage
    Parameter: 
        --file to file input. Is required
    """

    print(help_text)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hfotu", ["help", "file="])
        print("opts", opts)
    except getopt.GetoptError as e:
        print(str(e))
    file_input = "race.log"

    for o, a in opts:

        if o in ("-f", "--file"):
            file_input = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            usage()
            raise BaseException(f"Invalid parameter {o}")

    file_path = ReadFileRace(file_input)
    list_file = file_path.to_list
    race = TheRace(list_file)
    race.execute()


if __name__ == "__main__":
    main()
