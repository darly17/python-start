# students=['mary','bob','patrick','sandy','fizz','carl']


# students.sort(reverse=True)

# for i in students:
#     print(i)


# students1=('mary','bob','patrick','sandy','fizz','carl')
# sorted_students= sorted(students1)

# for i in sorted_students:
#     print(i)



students=[ ('bob','F',60),
('sandy','A',32),
('cap','B',31),
('bill','C',51),
('borys','D',27) ]

grade=lambda grades:grades[1]

students.sort(key=grade,reverse=True)
for i in students:
    print(i)



age=lambda grades:grades[2]

students.sort(key=age,reverse=True)
for i in students:
    print(i)



