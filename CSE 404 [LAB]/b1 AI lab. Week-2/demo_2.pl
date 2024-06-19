father(john, jim).
mother(jane, jim).
father(jack, john).   % fact

parent(Person1, Person2):-    %rule
    father(Person1, Person2);
    mother(Person1, Person2).

grandparent(Person1, Person2):-
    parent(Person3, Person2),
    parent(Person1, Person3).
