male(a).
male(b).
male(d).
male(f).
female(c).
female(e).
female(g).

parent(a, b).
parent(a, c).
parent(b, d).
parent(b, e).
parent(c, f).
parent(c, g).

father(X, Y):-
    parent(X, Y),
    male(X).

mother(X, Y):-
    parent(X, Y),
    female(X).

sibling(X, Y):-
    parent(Z, X),
    parent(Z, Y),
    X\==Y.

brother(X, Y):-
    sibling(X, Y),
    male(X).

sister(X, Y):-
    sibling(X, Y),
    female(X).

grandfather(X, Y):-
    parent(Z, Y),
    father(X, Z).
