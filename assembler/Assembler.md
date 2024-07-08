# Project Contribution

I have added an assembler written in Python to this VHDL project. The assembler translates assembly language code into machine code, enhancing the functionality of the project. This addition streamlines the development process by automating the conversion of assembly instructions. 


## The way to use assembler
Write your program in program.kkt file, run main.py, and copy the content of ram.vhdl file to the ram.vhdl file of your CPU.


## Instruction Set

The following table outlines the instruction set with examples using `D`, `N`, and `M` to represent register numbers:

| Instruction          | Example                               |
|----------------------|---------------------------------------|
| ADD_unsigned         | rD <= rN +u rM                        |
| ADD_signed           | rD <= rN + rM                         |
| SUB_unsigned         | rD <= rN -u rM                        |
| SUB_signed           | rD <= rN - rM                         |
| NOT                  | rD <= NOT rN                          |
| AND                  | rD <= rN AND rM                       |
| OR                   | rD <= rN OR rM                        |
| XOR                  | rD <= rN XOR rM                       |
| LSL                  | rD <= rN << rM                        |
| LSR                  | rD <= rN >> rM                        |
| CMP_unsigned         | rD <= rN >u rM                        |
| CMP_signed           | rD <= rN > rM                         |
| B_rM                 | PC <= rM                              |
| B_imm                | PC <= imm                             |
| BEQ                  | PC <= rN |: rM                       |
| IMMEDIATE_Save_To_Lower | lower rD <= imm                     |
| IMMEDIATE_Save_To_Upper | upper rD <= imm                     |
| LD                   | rD <= memory[rN]                      |
| ST                   | memory[rN] <= rD                      |
