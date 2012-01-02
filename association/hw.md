## Association Rules Homework

*Alireza Nourian*
<br />

1.a)

	s({E}) = 0.8
	s({B,D}) = 0.2
	s({B,D,E}) = 0.2

b) confidence is not symmetric

	c(BD => E) = 1.0
	c(E => BD) = 0.25
	
c)

	s({E}) = 1.0
	s({B,D}) = 1.0
	s({B,D,E}) = 0.8

d)

	c(BD => E) = 0.8
	c(E => BD) = 1.0

f)

	PS(BD => E) = PS(E => BD) = 1.25
	phi-coefficient(BD => E) = phi-coefficient(E => BD) = 0.25
	Lift(BD => E) = Lift(E => BD) = 0.04

2.a) This measure is anti-monontone. Minimum confidence of all characteristic rules generated from two itemsets:

	['A', 'B', 'C']
	0.29, 0.33, 0.40
	min: 0.29
	
	['A', 'B']
	0.57, 0.67
	min: 0.57	

b) Also this measure is anti-monontone. Minimum confidence of all discriminant rules generated from three itemsets:

	['A', 'B', 'C', 'E']
	0.50, 0.50, 0.33, 0.50
	min: 0.33

	['A', 'B', 'C']
	0.67, 0.67, 0.50
	min: 0.50

	['A', 'B']
	0.67, 0.57
	min: 0.57

c) Results doesn't change

3.a)

	'C (50) :F', 'A (50) :F', 'E (60) :F', 'B (70) :F', 'D (90) :F'
	'C A (20) :I', 'C E (20) :I', 'C B (30) :F', 'C D (40) :F', 'A E (40) :F', 'A B (30) :F', 'A D (40) :F', 'E D (60) :F', 'E B (40) :F', 'B D (60) :F'
	'C A E :N', 'C A B :N', 'C A D :N', 'C E D :N', 'C E B :N', 'C B D (20) :I', 'A E D (40) :F', 'A E B (20) :I', 'A B D (20) :I', 'E B D (40) :F'
	'C A E D :N', 'C E B D :N', 'A E B D :N', 'A B C E :N', 'A B C D :N'
	'C A E D B :N'

b)

	frequent items = 15 / 28 = 0.54

c) 

	pruning ratio = 8 / 28 = 0.29

d)

	false alarm rate = 5 / 28 = 0.18

6.a)
	
	s({Exercise=Yes, Cholesterol=Low}) = 0.16
	c(Exercise=Yes => Cholesterol=Low) = 0.36

b)

	s({Exercise=No, Cholesterol=Low}) = 0.2
	c(Exercise=No => Cholesterol=Low) = 0.36

c) there isn't any clear relationship between them

d) doing daily exercises doesn't impact Cholesterol rate of the non-retired patients

	s({Exercise=Yes, Cholesterol=Low}) = 0.24
	c(Exercise=Yes => Cholesterol=Low) = 0.3

	s({Exercise=No, Cholesterol=Low}) = 0.04
	c(Exercise=No => Cholesterol=Low) = 0.2

e) retired patients that use to do daily exercises have low Cholesterol rate

	s({Exercise=Yes, Cholesterol=Low}) = 0.08
	c(Exercise=Yes => Cholesterol=Low) = 0.8

	s({Exercise=No, Cholesterol=Low}) = 0.36
	c(Exercise=No => Cholesterol=Low) = 0.4

f) the results of part (e) is inconsistent with part (c). in part (e) we are analysing the impact of Exercise on Cholesterol rate only for part of data and in part (c) we are doing that for whole of them. So we've got local relationship between these two attribute.
