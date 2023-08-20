#define start_value 10
#define save_location 0
INC start_value
loop_dec_to_0:
TAKE start_value
DEC start_value
SAVE save_location
INC 3
TST start_value
JUMP loop_dec_to_0
