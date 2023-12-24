#define start_value_static 10
#define counter 0
#define save_location_command 04024
#define save_location 0


initialize_code:
TAKE start_value_static
SAVE counter
INC counter
JUMP loop_dec_to_0


loop_dec_to_0:
DEC counter
SAVE save_location
INC 5   ;edit save instruction
TST counter
JUMP loop_dec_to_0
JUMP make_counter_reusable
HLT

make_counter_reusable:
TAKE save_location_command
SAVE 5 ;edit save instruction 
JUMP initialize_code

