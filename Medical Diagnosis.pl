% Define symptoms
symptom(john, fever).
symptom(john, cough).
symptom(john, headache).
symptom(mary, fever).
symptom(mary, sore_throat).
symptom(mary, runny_nose).

% Define diseases and their symptoms
disease(cold, [fever, cough, headache, runny_nose]).
disease(flu, [fever, cough, headache, sore_throat]).
disease(allergy, [runny_nose]).

% Define rules for diagnosis based on symptoms
diagnose(Person, Disease) :-
    symptom(Person, Symptom),
    disease(Disease, Symptoms),
    member(Symptom, Symptoms).

% Querying for diagnosis
% Example query: diagnose(john, Disease).
