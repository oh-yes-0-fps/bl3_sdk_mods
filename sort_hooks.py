import sys
from pathlib import Path

def main():
    parent_dir = Path(__file__).resolve().parent

    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python sort_hooks.py <log_file>")
        sys.exit(1)

    log_file = parent_dir / sys.argv[1]

    fn_counter = {}

    with open(log_file, 'r') as f:
        lines = f.readlines()

        #step every 3 lines
        for i in range(0, len(lines), 3):
            fn = lines[i+1].split("Function: ")[1].strip()
            if fn not in fn_counter:
                fn_counter[fn] = 0
            fn_counter[fn] += 1

    sorted_fns = sorted(fn_counter.items(), key=lambda x: x[1], reverse=True)

    for fn, count in sorted_fns:
        print(f"{count}: {fn}")

if __name__ == "__main__":
    main()