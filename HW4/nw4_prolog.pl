max_sum(L, M) :-
    max_sum(L, 0, 0, M).

max_sum([], _, M, M).
max_sum([X | L], H, F, M) :-
    Temp_H is max(0, H + X),
    (F < H + X -> Temp_F is Temp_H; Temp_F is F),
    max_sum(L, Temp_H, Temp_F, M).
	
#L:list
#M:Max value
#F:Max so far
#H:max ending position
#X:head of list
#Temp_H, Temp_F:temporatory value