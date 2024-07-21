#Given A List Of Animals Perform All The Operations On The Same List

animals = ['cat','dog','parrot','tiger','zebra']
#1. Add New Aniumal "Lion"
animals.append('lion')

#2. Add 'Bear' In Between 'Dog' & 'Parrot'
animals.insert(animals.index('dog')+1,'bear')

#3. Add Some More Animals Like: 'tiger', 'rabbit', 'horse'
animals.extend(['tiger','rabbit','horse'])

#4. Delete The 2nd Tiger From The List
first_tiger = animals.index('tiger')
second_tiger = animals.index('tiger',first_tiger+1)
del animals[second_tiger]

#5. print the final list of animal
print("Final list of animals: ",animals)

#6. print the total number of animals in the list 
print('Total number of animals in the list: ',len(animals))