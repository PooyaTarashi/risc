import re

instruction_patterns = {
    'ADD_unsigned': re.compile(r'r(\d+) <= r(\d+) \+u r(\d+)'),
    'ADD_signed': re.compile(r'r(\d+) <= r(\d+) \+ r(\d+)'),
    'SUB_unsigned': re.compile(r'r(\d+) <= r(\d+) \-u r(\d+)'),
    'SUB_signed': re.compile(r'r(\d+) <= r(\d+) \- r(\d+)'),
    'NOT': re.compile(r'r(\d+) <= NOT r(\d+)'),
    'AND': re.compile(r'r(\d+) <= r(\d+) AND r(\d+)'),
    'OR': re.compile(r'r(\d+) <= r(\d+) OR r(\d+)'),
    'XOR': re.compile(r'r(\d+) <= r(\d+) XOR r(\d+)'),
    'LSL': re.compile(r'r(\d+) <= r(\d+) << r(\d+)'),
    'LSR': re.compile(r'r(\d+) <= r(\d+) >> r(\d+)'),
    'CMP_unsigned': re.compile(r'r(\d+) <= r(\d+) >u r(\d+)'),
    'CMP_signed': re.compile(r'r(\d+) <= r(\d+) > r(\d+)'),
    'B_rM': re.compile(r'PC <= r(\d+)'),
    'B_imm': re.compile(r'PC <= (\d+)'),
    'BEQ': re.compile(r'PC <= r(\d+) \|: r(\d+)'),
    'IMMEDIATE_Save_To_Lower': re.compile(r'lower r(\d+) <= (\d+)'),
    'IMMEDIATE_Save_To_Upper': re.compile(r'upper r(\d+) <= (\d+)'),
    'LD': re.compile(r'r(\d+) <= memory[r(\d+)]'),
    'ST': re.compile(r'memory[r(\d+)] <= r(\d+)')
}

def convert_to_machine_code(instruction, line):
    for instr, pattern in instruction_patterns.items():
        matched = pattern.match(instruction)
        if matched:
            match instr:
                case 'ADD_unsigned':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'00000{rD_address}{rM_address}{rN_address}00'
                case 'ADD_signed':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'10000{rD_address}{rM_address}{rN_address}00'
                case 'SUB_unsigned':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'00001{rD_address}{rM_address}{rN_address}00'
                case 'SUB_signed':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'10001{rD_address}{rM_address}{rN_address}00'
                case 'NOT':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    return f'00010{rD_address}{rM_address}00000'
                case 'AND':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'00011{rD_address}{rM_address}{rN_address}00'
                case 'OR':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'01000{rD_address}{rM_address}{rN_address}00'
                case 'XOR':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'00101{rD_address}{rM_address}{rN_address}00'
                case 'LSL':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'00110{rD_address}{rM_address}{rN_address}00'
                case 'LSR':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'00111{rD_address}{rM_address}{rN_address}00'
                case 'CMP_unsigned':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'01000{rD_address}{rM_address}{rN_address}00'
                case 'CMP_signed':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    rN_address = format(int(matched.group(3)), '03b')  
                    return f'01001{rD_address}{rM_address}{rN_address}00'
                case 'B_rM':
                    rM_address = format(int(matched.group(1)), '03b')
                    return f'11001{rD_address}{rM_address}{rN_address}00'
                case 'B_imm':
                    imm = format(int(matched.group(1)), '08b')
                    return f'01001000{imm}'
                case 'BEQ':
                    rM_address = format(int(matched.group(1)), '03b')
                    rN_address = format(int(matched.group(2)), '03b')  
                    return f'01010000{rM_address}{rN_address}00'
                case 'IMMEDIATE_Save_To_Lower':
                    rD_address = format(int(matched.group(1)), '03b')
                    imm = format(int(matched.group(1)), '08b')
                    return f'01011{rD_address}{imm}'
                case 'IMMEDIATE_Save_To_Upper':
                    rD_address = format(int(matched.group(1)), '03b')
                    imm = format(int(matched.group(1)), '08b')
                    return f'11011{rD_address}{imm}'
                case 'LD':
                    rD_address = format(int(matched.group(1)), '03b')
                    rM_address = format(int(matched.group(2)), '03b')
                    return f'01100{rD_address}{rM_address}00000'
                case 'ST':
                    rM_address = format(int(matched.group(1)), '03b')
                    rN_address = format(int(matched.group(2)), '03b')
                    return f'01101000{rM_address}{rN_address}00'
        if instruction[0] == '#':
            continue
    raise ValueError(f"Invalid instruction in line {line}: \"{instruction}\"")


def convert_kkt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    machine_code = []
    cnt = 0
    for line in lines:
        cnt += 1
        line = line.strip()
        if line:
            machine_code.append(convert_to_machine_code(line, cnt))
    
    return machine_code


def write_machine_code(file_path, machine_code, target=26):
    code_string = '\t\t\"'
    for code in machine_code:
        code_string += (code + '\",\n\t\t\"')
    code_string = code_string[:-1]

    with open('ramTmplt.vhd', 'r') as template_file:
        template_lines = template_file.readlines()

    template_lines.insert(target, code_string + '\n')

    with open(file_path, 'w') as file:
        file.writelines(template_lines)


def main(input_file, output_file):
    machine_code = convert_kkt_file(input_file)
    write_machine_code(output_file, machine_code)
    print(f"Done! Machine code written to {output_file}")

if __name__ == "__main__":
    input_file = 'program.kkt'
    output_file = 'ram.vhd'
    main(input_file, output_file)