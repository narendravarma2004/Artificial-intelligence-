% Facts representing family relationships
male(john).
male(mike).
male(tom).
male(jerry).
male(harry).

female(susan).
female(lily).
female(lisa).
female(sarah).

parent(john, mike).
parent(john, lily).
parent(susan, mike).
parent(susan, lily).
parent(mike, tom).
parent(lily, jerry).
parent(lily, sarah).
parent(tom, harry).
parent(lisa, harry).

% Rules to define specific family relationships
father(Father, Child) :-
    male(Father),
    parent(Father, Child).

mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

% Rule to find all family details for a given person
family_details(Person) :-
    format('Details for ~w:~n', [Person]),
    findall(Child, parent(Person, Child), Children),
    format('Children: ~w~n', [Children]),
    findall(Parent, parent(Parent, Person), Parents),
    format('Parents: ~w~n', [Parents]),
    findall(Sibling, sibling(Person, Sibling), Siblings),
    format('Siblings: ~w~n', [Siblings]),
    findall(Grandchild, grandparent(Person, Grandchild), Grandchildren),
    format('Grandchildren: ~w~n', [Grandchildren]),
    (father(Person, X) -> format('Father: ~w~n', [X]) ; true),
    (mother(Person, Y) -> format('Mother: ~w~n', [Y]) ; true).

% Example query:
% To get all family details for John:
% ?- family_details(john).
