

BINARY = lambda X: f"{X:032b}"
MASK = lambda X: X ^ 0B11111111111111111111111111111111

FLAG_EMPTY =     0B00000000000000000000000000000000
FLAG_STK0UP =    0B00000000000000000000000000000001
FLAG_STK0RIGHT = 0B00000000000000000000000000000010
FLAG_STK0DOWN =  0B00000000000000000000000000000100
FLAG_STK0LEFT =  0B00000000000000000000000000001000
FLAG_STK1UP =    0B00000000000000000000000000010000


FLAG_STK0UPMASK = MASK(FLAG_STK0UP)


FLAG_EMPTYSET = lambda X: FLAG_EMPTY
FLAG_STK0UPSET = lambda X: X | FLAG_STK0UP
FLAG_STK0UPCLEAR = lambda X: X & FLAG_STK0UPMASK
FLAG_STK0UPTEST = lambda X: X & FLAG_STK0UP

