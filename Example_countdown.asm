#define save_location 0
loop_dec_to_0:
TAKE 006
DEC 006
SAVE save_location
INC 2
TST 6
JUMP 0
;this code needs a manual change ad the start value in cell 06! always store n+1 there
