person(a; b; c; d; e).
position(1..5).

% Każda osoba ma tylko jedną pozycję
1 { order(P, Pos) : position(Pos) } 1 :- person(P).

% Każda pozycja jest zajęta przez tylko jedną osobę
1 { order(P, Pos) : person(P) } 1 :- position(Pos).

% Ograniczenia:
:- order(a, PA), order(b, PB), not PA < PB.
:- order(c, PC), order(a, PA), not PC < PA.
:- order(b, PB), order(d, PD), not PB < PD.
:- order(d, PD), order(e, PE), not PD < PE.

#show order/2.
