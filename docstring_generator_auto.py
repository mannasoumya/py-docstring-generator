#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print(f"Usage: python3 {sys.argv[0]} <file-path>")
    sys.exit(1)

file_name    = sys.argv[1]
file_content = None
no_counter   = 0
    

with open(file_name) as f:
    file_content = f.read()

lines = file_content.split("\n")

unparsed_functions  = {}
line_number_fn_name = {}

def space_or_tab_counter(line):
    space_or_tab = " "
    count = 0
    if line.startswith("\t"):
        space_or_tab = "\t"
    
    for c in line:
        if c == space_or_tab:
            count = count + 1
        else:
            break
    
    return (space_or_tab,count)

if __name__ == "__main__":
    for i in range(len(lines)):
        line = lines[i].strip().strip("\t")
        if line.startswith("#"):
            continue
        
        if line.startswith("def"):
            if not line.endswith(":"):
                raise Exception(f"Syntax Error near line {i+1}")

            fn_name_with_params = line.lstrip("def").strip().strip("\t")

            start_index = fn_name_with_params.find("(")
            if start_index == -1:
                raise Exception(f"Syntax Error near line {i+1}")
            
            last_index = fn_name_with_params.rfind(")")
            if last_index == -1:
                raise Exception(f"Syntax Error near line {i+1}")
            
            fn_name = fn_name_with_params[0:start_index]

            if fn_name in unparsed_functions:
                raise Exception(f"Duplicate function `{fn_name}`")

            unparsed_functions[fn_name] = {}
            unparsed_functions[fn_name]["signature"] = fn_name_with_params[start_index+1:last_index]
            unparsed_functions[fn_name]["line_number"] = i
            line_number_fn_name[i] = fn_name

    for fn_name in unparsed_functions:
        print()
        fn_signature = unparsed_functions[fn_name]["signature"]
        if fn_signature == "":
            print(f"Function `{fn_name}` has no parameters")
            ans = input(f"Do you want to write docstring for `{fn_name}` ? (y/n)  ")
            if ans.strip().lower() == "n" or ans.strip().lower() == "no":
                no_counter = no_counter + 1
                continue
            consent = False
            while consent == False:
                summary = input("Enter function summary:  ")
                inp = input("Are you sure? (y/n)  ")
                if inp.strip().lower() == "" or inp.strip().lower() in ("y", "yes"):
                    unparsed_functions[fn_name]["desc"] = summary
                    consent = True
        else:

            print(f"Function `{fn_name}`")
            params = fn_signature.split(",")
            print(f"Params {params}")
            ans = input(f"Do you want to write docstring for `{fn_name}` ? (y/n)  ")
            if ans.strip().lower() == "n" or ans.strip().lower() == "no":
                no_counter = no_counter + 1
                continue

            consent = False
            while consent == False:
                summary = input("Enter function summary:  ")
                inp = input("Are you sure? (y/n)  ")
                if inp.strip().lower() == "" or inp.strip().lower() in ("y", "yes"):
                    unparsed_functions[fn_name]["desc"] = summary
                    consent = True

            summary = summary + "\n\nArgs:"
            for param in params:
                print()
                param_and_type = param.split(":")
                if len(param_and_type) > 1:
                    param_name = param_and_type[0].strip()
                    param_type = param_and_type[1].strip()
                    print(f"{param_name} : {param_type}")
                    summary = summary + "\n" + param_name + " " + "(" + param_type + ") :"
                
                if len(param_and_type) == 1:
                    param_name = param_and_type[0].strip()
                    print(f"{param_name} : ")
                    summary = summary + "\n" + param_name + " " + "( _obj_ ) :"
                
                consent = False
                while consent == False:
                    param_summary = input("Enter parameter summary:  ")
                    inp = input("Are you sure? (y/n)  ")
                    if inp.strip().lower() == "" or inp.strip().lower() in ("y", "yes"):
                        unparsed_functions[fn_name]["desc"] = summary
                        consent = True
                
                summary = summary + " " + param_summary
                
            unparsed_functions[fn_name]["desc"] = summary

    new_content = ""

    for i in range(len(lines)):
        new_content = new_content + lines[i] + "\n"
        if i in line_number_fn_name:
            space_or_tab , num = space_or_tab_counter(lines[i+1])
            if "desc" in unparsed_functions[line_number_fn_name[i]]:
                new_content = new_content + num * space_or_tab + '"""\n'
                desc_lines = unparsed_functions[line_number_fn_name[i]]["desc"].split("\n")
                for desc_line in desc_lines:
                    new_content = new_content + num * space_or_tab + desc_line + "\n"
                new_content = new_content + num * space_or_tab + '"""\n'

    if no_counter == len(unparsed_functions):
        print()
        print("No docstrings to save... Exiting")
        sys.exit(0)
    
    new_file_name = f"{file_name[:file_name.rfind('.py')]}_docstrings.py"
    
    with open(new_file_name,"w") as f:
        f.write(new_content)
        print(f"\nNew file with docstings saved at : `{new_file_name}`")
