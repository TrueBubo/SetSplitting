import os
import subprocess
import sys
import tempfile

def load_input(filename: str) -> list[list[int]]:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} does not exist.")
    with open(filename) as file:
        return [[int(literal) for literal in line.split()] for line in file]


def create_clauses(subsets: list[list[int]]) -> list[list[int]]:
    return [[elem for elem in subset] + [0] for subset in subsets] + [[-elem for elem in subset] + [0] for subset in subsets]


def main():
    args: list[str] = sys.argv
    if len(args) == 1: raise ValueError("The SAT Solver needs at least a filename")

    filename: str = args[-1]

    subsets: list[list[int]] = load_input(filename)


    clauses: list[list[int]] = create_clauses(subsets)
    if "--only-conversion" in args:
        print("\n".join([" ".join(map(str, clause)) for clause in clauses]))
        return
    if "--verbose" in args:
        print(f"Clauses: {clauses}")

    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
        print("\n".join([" ".join(tuple(map(str, clause))) for clause in clauses]), file=temp_file)
        temp_file.flush()
        command: list[str] = ["glucose", "-model", temp_file.name]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 10:
            print("Satisfiable")
            print(" ".join(result.stdout.split("\n")[-2].split()[1:-1]))
        elif result.returncode == 20:
            print("Unsatisfiable")
        else:
            print("Error occurred, make sure glucose is included in you path")


if __name__ == "__main__":
    main()