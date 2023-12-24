#define MAX_N 12 ;MAX value for N
#define ERROR 0; error register set to !=0 if error
#define N 1
#define F1 1
#define F2 1
#define output 0


TST N; test if N=0
JUMP test_n_to_high
INC ERROR; increase error register
HLT;halt the programm otherwise



test_n_to_high:
INC MAX_N ;increase max n by one to not fail for N=Max-N
TAKE MAX_N ;Input validation N<MaxN
SUB N
SAVE MAX_N ; Saves the result to MAX-N
TST MAX_N
JUMP loop_fib_rechner
INC ERROR; increase error register
HLT;Halt program if n out of range   



loop_fib_rechner:
TAKE F1
ADD F2
SAVE output 
INC 12              ;replace with code line for TAKE F1
INC 13              ;replace with code line for ADD F2
INC 14              ;replace with code line for save output
DEC N               ;dec counter
TST N               ;test if counter 0
JUMP loop_fib_rechner
