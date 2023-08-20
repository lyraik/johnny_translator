#define Z 10 ;variable for 
#define N 3
#define Q 0
#define R 0
#define TEMP 0

loop_reduction:;this is an anoying comment
TAKE Z  ;Z gets loaded into the accumulator
SUB N   ;N gets substracted
SAVE Z
INC Q
TST Z
JUMP loop_test_for_rest
HLT




loop_test_for_rest:         ;this loop tests if there is a Rest or if there isnt
INC Z ;Ibcrease Z
TAKE Z ; Load Z to the ACCumulator
SUB N
SAVE TEMP
DEC Z
TST TEMP
JUMP loop_reduction
TAKE Z
SAVE R
HLT
