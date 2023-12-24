#define start_value 10
#define save_location 0
INC start_value
loop_dec_to_0:
DEC start_value
SAVE save_location
INC 2;edit save instruction
TST start_value
JUMP loop_dec_to_0
