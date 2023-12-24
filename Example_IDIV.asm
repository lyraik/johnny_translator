#define Z 3 ; numerator
#define N 0 ; denominator
#define Q 0 ; quotient
#define R 0 ; rest
#define ERROR 0 ;Variable to show if error 
#define TEMP 0 ; Temp variable

TST Z ;if Z == 0 programm can end as result = 0
JUMP loop_input_validation_N ;z != 0 tests if N= 0
HLT

loop_input_validation_N:
TST N ;if N==0 end Programm here
JUMP loop_test_for_rest ;if N != 0 continue to programm 
INC ERROR ;show division error
HLT ;halt programm

loop_reduction: ;this is an anoying comment
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
