SUM_LENGTHS = {
	0: (0,),
	1: (),
	2: (1,),
	3: (1,),
	4: (1,),
	5: (1, 2),
	6: (1, 2),
	7: (1, 2),
	8: (1, 2),
	9: (2, 3),
	10: (2, 3),
	11: (2, 3),
	12: (2, 3),
	13: (2, 3),
	14: (2, 3, 4),
	15: (2, 3, 4),
	16: (3, 4),
	17: (3, 4),
	18: (3, 4),
	19: (3, 4),
	20: (3, 4, 5),
	21: (3, 4, 5),
	22: (4, 5),
	23: (4, 5),
	24: (4, 5),
	25: (4, 5),
	26: (4, 5),
	27: (5, 6),
	28: (5, 6),
	29: (5, 6),
	30: (5, 6),
	31: (6,),
	32: (6,),
	33: (6,),
	34: (),
	35: (7,),
}

SUM_SETS = {
	0: ((),),
	1: (),
	2: ((1,),),
	3: ((2,),),
	4: ((3,),),
	5: ((4,), (1, 2)),
	6: ((1, 3), (5,)),
	7: ((6,), (1, 4), (2, 3)),
	8: ((7,), (1, 5), (2, 4)),
	9: ((1, 6), (3, 4), (1, 2, 3), (2, 5)),
	10: ((1, 2, 4), (2, 6), (3, 5), (1, 7)),
	11: ((1, 2, 5), (2, 7), (3, 6), (1, 3, 4), (4, 5)),
	12: ((3, 7), (2, 3, 4), (1, 3, 5), (4, 6), (1, 2, 6)),
	13: ((2, 3, 5), (5, 6), (1, 2, 7), (1, 4, 5), (1, 3, 6), (4, 7)),
	14: ((5, 7), (2, 3, 6), (1, 3, 7), (2, 4, 5), (1, 2, 3, 4), (1, 4, 6)),
	15: ((1, 2, 3, 5), (1, 5, 6), (2, 3, 7), (6, 7), (2, 4, 6), (1, 4, 7), (3, 4, 5)),
	16: ((3, 4, 6), (1, 2, 3, 6), (1, 5, 7), (2, 5, 6), (1, 2, 4, 5), (2, 4, 7)),
	17: ((1, 6, 7), (1, 2, 3, 7), (3, 4, 7), (2, 5, 7), (1, 2, 4, 6), (3, 5, 6), (1, 3, 4, 5)),
	18: ((1, 2, 5, 6), (1, 3, 4, 6), (2, 6, 7), (3, 5, 7), (4, 5, 6), (2, 3, 4, 5), (1, 2, 4, 7)),
	19: ((1, 3, 4, 7), (2, 3, 4, 6), (4, 5, 7), (1, 2, 5, 7), (1, 3, 5, 6), (3, 6, 7)),
	20: ((1, 2, 6, 7), (2, 3, 4, 7), (1, 3, 5, 7), (1, 4, 5, 6), (1, 2, 3, 4, 5), (2, 3, 5, 6), (4, 6, 7)),
	21: ((1, 4, 5, 7), (2, 4, 5, 6), (1, 2, 3, 4, 6), (1, 3, 6, 7), (5, 6, 7), (2, 3, 5, 7)),
	22: ((1, 2, 3, 4, 7), (1, 4, 6, 7), (2, 3, 6, 7), (1, 2, 3, 5, 6), (2, 4, 5, 7), (3, 4, 5, 6)),
	23: ((1, 2, 4, 5, 6), (1, 5, 6, 7), (1, 2, 3, 5, 7), (2, 4, 6, 7), (3, 4, 5, 7)),
	24: ((2, 5, 6, 7), (1, 2, 4, 5, 7), (3, 4, 6, 7), (1, 3, 4, 5, 6), (1, 2, 3, 6, 7)),
	25: ((2, 3, 4, 5, 6), (1, 2, 4, 6, 7), (3, 5, 6, 7), (1, 3, 4, 5, 7)),
	26: ((4, 5, 6, 7), (2, 3, 4, 5, 7), (1, 2, 5, 6, 7), (1, 3, 4, 6, 7)),
	27: ((1, 3, 5, 6, 7), (2, 3, 4, 6, 7), (1, 2, 3, 4, 5, 6)),
	28: ((1, 2, 3, 4, 5, 7), (1, 4, 5, 6, 7), (2, 3, 5, 6, 7)),
	29: ((1, 2, 3, 4, 6, 7), (2, 4, 5, 6, 7)),
	30: ((1, 2, 3, 5, 6, 7), (3, 4, 5, 6, 7)),
	31: ((1, 2, 4, 5, 6, 7),),
	32: ((1, 3, 4, 5, 6, 7),),
	33: ((2, 3, 4, 5, 6, 7),),
	34: (),
	35: ((1, 2, 3, 4, 5, 6, 7),)
}