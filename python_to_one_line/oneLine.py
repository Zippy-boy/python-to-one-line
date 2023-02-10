import argparse

def format_box(title, body, width=80):
    box_line = lambda text: "*  " + text + (" " * (width - 6 - len(text))) + "  *"

    print("*" * width)
    print(box_line(title))
    print("*" * width)
    print(box_line(""))

    for line in body.split("\n"):
        print(box_line(line.expandtabs()))

    print(box_line(""))
    print("*" * width)


parser = argparse.ArgumentParser()

parser.add_argument("first", type=str, help="Full path to file")
parser.add_argument(
    "-o", "--output", type=str, help="The outputed file", required=False
)

args = parser.parse_args()
raw_f = open(args.first, "r", encoding="utf-8")
f = str(raw_f.read())
f = (
    f.strip()
    .replace("\t", "\\t")
    .replace("\\", "\\\\")
    .replace('"', '\\"')
    .replace("'", "\\'")
    .replace("    ", "\\t")
    .split("\n")
)
a = []
for i in f:
    a.append(str(i) + "\\n")
n = ""
for i in a:
    n = n + i

input_path = args.first
output_path = args.output
output_path_none = args.first

o = output_path_none.split("\\")
o.pop()
output_path_none = ""
for i in o:
    output_path_none = output_path_none + i + "\\"

if output_path == None:
    print(output_path_none)
    with open(output_path_none + "output.py", "w") as f:
        f.write(f'exec("{n}")')
        format_box(
            "\tOne -- Line", "\tOutPut File --->\n\n" f"{output_path_none}\\output.py"
        )

else:
    with open(f"{output_path}\\output.py", "w") as f:
        f.write(f'exec("{n}")')
        format_box(
            "\tOne -- Line", "\tOutPut File --->\n\n" f"{output_path}\\output.py"
        )

