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

def get_next_line_number_starting_with_space_or_tab(lines,i):
    assert len(lines) > 0, "Lines cannot be empty"
    for j in range(i+1,len(lines)):
        if lines[j].startswith("\t") or lines[j].startswith(" "):
            return j

if __name__ == "__main__":
    for i in range(len(lines)):
        line = lines[i].strip().strip("\t")
        if line.startswith("#"):
            continue
        
        if line.startswith("def"):
            if not line.endswith(":"):
                raise Exception(f"Syntax Error near line {i+1}")

            fn_name_with_params = line.lstrip("def").strip().strip("\t")
            before_and_return_type = fn_name_with_params.split("->")

            ret_type = None

            if len(before_and_return_type) == 2:
                ret_type = before_and_return_type[1].strip().strip("\t").rstrip(":").strip().strip("\t")

            start_index = fn_name_with_params.find("(")
            if start_index == -1:
                raise Exception(f"Syntax Error near line {i+1}")
            
            last_index = fn_name_with_params.rfind(")")
            if last_index == -1:
                raise Exception(f"Syntax Error near line {i+1}")
            
            fn_name = fn_name_with_params[0:start_index]
            fn_name = fn_name.strip().strip("\t")

            if fn_name in unparsed_functions:
                raise Exception(f"Duplicate function `{fn_name}`")

            unparsed_functions[fn_name] = {}
            unparsed_functions[fn_name]["ret_type"]    = ret_type
            unparsed_functions[fn_name]["signature"]   = fn_name_with_params[start_index+1:last_index]
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
            params_ = []
            for param in params:
                params_.append(param.strip(" ").strip("\t"))
            print(f"Params: {params_}")
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
                        
        summary = summary + "\n\n" + "Returns:\n"
        print()
        if unparsed_functions[fn_name]["ret_type"] is None:
            print(f"\nNo explicit return type found for function `{fn_name}`")
        else:
            print(f"Return type of function `{fn_name}` is `{unparsed_functions[fn_name]['ret_type']}`")
            summary = summary + unparsed_functions[fn_name]["ret_type"] + ": "
        
        consent = False
        while consent == False:
            return_summary = input("Enter return summary:  ")
            inp = input("Are you sure? (y/n)  ")
            if inp.strip().lower() == "" or inp.strip().lower() in ("y", "yes"):
                summary = summary + return_summary
                unparsed_functions[fn_name]["desc"] = summary
                consent = True

    new_content = ""

    for i in range(len(lines)):
        new_content = new_content + lines[i] + "\n"
        if i in line_number_fn_name:
            next_index_to_count = get_next_line_number_starting_with_space_or_tab(lines,i)
            space_or_tab , num = space_or_tab_counter(lines[next_index_to_count])
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
