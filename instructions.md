### Instruction set
<br>

<p align="center" width="100%">
    <img width="442" height="154" alt="programmer" src="https://github.com/user-attachments/assets/fe744e02-c4cb-464b-b15a-53f843daa596" />
</p>

<br>
The programmer uses 8 bits with 4 most significant bits being the opcode (instruction code) below:
<br>

|Instruction code|Mnemonic|Action|Notes|
|----------------|--------|------|-----|
|0000 | NOPO | No change in registers | R --> R|
|0001 | LD | Load result reg | Data --> RR|
|0010| LDC | Load compliment of data | |
|0011| AND | Logical AND | RR . D --> RR|
|0100| ANDC| Logical AND compliment ||
|0101| OR | Logical OR | RR + D --> RR|
|0110| ORC | Logical OR compliment ||
|0111| XNOR | Exclusive NOR | If RR = D, RR <-- 1|
|1000| STO | Store | RR --> Data Pin, Write <-- 1|
|1001| STOC| Store compliment | |
|1010| IEN | Input enable | D --> IEN Reg|
|1011| OEN | Output enable | D --> OEN Reg|
|1100| JMP | Jump ||
|1101| RTN | Return | Skip next instruction|
|1110| SKZ | Skip next instruction if RR = 0|
|1111| NOPF | No change in registers||




