#map() applies a function to each item in an iterable (list,tuple,etc.)

#map(func,iterable)


store=[
    ('cola',2.00),
    ('fanta',2.15),
    ('sprite',2.18)
]

to_euros=lambda data:(data[0],data[1]*0.82)

print(store_euros:=list(map(to_euros,store)))


#filter() creates a collection of elements from an iterable for which a function returns true

friends=[
    ('Elena',20),
    ('Sasha',15),
    ('Katya',18)
]

age=lambda data:data[1]>=18
print(list(filter(age,friends)))
