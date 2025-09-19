import argparse
import json
from pathlib import Path


def main():

    # use argparse to get in Arguments
    msg = "Script to filter for need-types and generate proxy elements"

    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("-i", "--input", help="Path to the JSON-Input File", required=True, type=Path,)
    parser.add_argument("-o", "--output", help="Path to the JSON-Output File", required=True, type=Path,)
    parser.add_argument("-p", "--pretty", help="Enable pretty output json. needs more disc space", action="store_true",)
    parser.add_argument("-t", "--filter_types", help="Types to be filtered.", nargs="+", required=True,)

    args = parser.parse_args()

    json_input_path = Path(args.input).absolute()
    json_output_path = Path(args.output).absolute()
    pretty_output: bool = args.pretty
    filter_types = args.filter_types

    print(filter_types)

    # check if input file exists
    if not json_input_path.is_file():
        print(f"Error: The File '{json_input_path}' does not existed.")
        return

    #read json file
    try:
        with json_input_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"✅ JSON '{json_input_path}' loaded.")
    except json.JSONDecodeError as e:
        print(f"❌ Error during parsing the JSON-File: {e}")

    # filter data for current version
    for v in data["versions"]:
        if v != data["current_version"]:
            del data["versions"][v]

    # Get the needs dictionary from the current version
    needs = data["versions"][data["current_version"]]["needs"]

    # Filter needs dictionary by type
    filtered_needs = {
        need_id: need_data
        for need_id, need_data in needs.items()
        if need_data.get("type") in filter_types
    }

    new_needs = data.copy()
    new_needs["versions"][data["current_version"]]["needs"] = filtered_needs
    new_needs["versions"][data["current_version"]]["needs_amount"] = len(filtered_needs)

    print("✅ Data filtered.")

    # Convert the new needs dictionary back to a JSON string
    indent=None
    if pretty_output:
        indent=4

    str_new_needs = json.dumps(new_needs, indent=indent, ensure_ascii=False)
    print("✅ Json string created.")

    # Write the JSON string to a new file
    try:
        with json_output_path.open("w", encoding="utf-8") as f:
            f.write(str_new_needs)
            print(f"✅ Output file '{json_output_path}' written.")
    except json.JSONDecodeError as e:
        print(f"❌ Error during parsing the JSON-File: {e}")

if __name__ == "__main__":
    main()

