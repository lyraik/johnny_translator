#define N 10
#define F1 1
#define F2 1
#define output 0
DEC N
loop_fib_rechner:
TAKE F1
ADD F2
SAVE output
INC 01              ;replace with code line for TAKE F1
INC 02              ;replace with code line for ADD F2
INC 03
DEC N               ;dec counter
TST N               ;test if counter 0
JUMP loop_fib_rechner
