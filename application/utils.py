def convert_register_format(register, register_format):
    if register_format == "subreg":
        return convert_to_subreg_format(register)

def convert_to_subreg_format(register):
    a_reg = {"entries":[]}
    b_reg = {"entries":[]}
    c_reg = {"entries":[]}
    for group in register["groups"]:
        for entry in group["entries"]:
            if entry["sub_register"] == "A":
                add_entry_to_sub_register(a_reg, entry)
            elif entry["sub_register"] == "B":
                add_entry_to_sub_register(b_reg, entry)
            elif entry["sub_register"] == "C":
                add_entry_to_sub_register(c_reg, entry)

    formatted_register = {"a_register" : a_reg, "b_register" : b_reg, "c_register" : c_reg}

    return formatted_register

def add_entry_to_sub_register(sub_register, entry_to_add):
    if len(sub_register["entries"]) == 0:
        sub_register["entries"].append(entry_to_add)
    else:
        entry_added = False
        for idx, entry in enumerate(sub_register["entries"]):
            if entry_to_add["sequence_number"] < entry["sequence_number"]:
                sub_register["entries"].insert(idx, entry_to_add)
                entry_added = True
                break
        if not entry_added:
            sub_register["entries"].append(entry_to_add)
