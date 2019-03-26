import numpy
import GA
import random
"""
Имеем определенное кол-во класоов(тут 3) и уроков в неделю по 
предмету (без учета кол-ва классов). 
Нужно найти наименьшее кол-во учителей (общее), у которых
будет нормальная занятость по предмету (от 20 до 25 часов -+ 2 часа)
Варьироваться в алгоритме (весами уравнения) будут часы на 
учителя по предмету. 
Уравнение в целом простое 
number_of_teachers = lessons / number_of_hours.
lessons - кол-во уроков в неделю * кол-во классов (параллелей)
number_of_hours = список часов по предмету (варьируется)
number_of_teachers - искомое значение (ищем минимум)
"""

# Inputs of the equation.
classes_num = 3
number_of_lessons = [33.82, 16.85, 14.91, 7.94, 24.91, 8.86, 11.88, 7, 7]
classes = [classes_num] * len(number_of_lessons)
lessons = numpy.multiply(classes, number_of_lessons)
# Number of the weights we are looking to optimize.
num_weights = len(number_of_lessons)

"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 8
num_parents_mating = 4

# Defining the population size.
pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.randint(low=20, high=25, size=pop_size)
print(new_population)

num_generations = 10
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measing the fitness of each chromosome in the population.
    fitness = GA.cal_pop_fitness(lessons, new_population)

    # Selecting the best parents in the population for mating.
    parents = GA.select_mating_pool(new_population, fitness,
                                      num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = GA.crossover(parents,
                                       offspring_size=(pop_size[0]-parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = GA.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # The best result in the current iteration.
    print("Best result : ", numpy.min(numpy.sum(
        numpy.ceil(numpy.divide(
            lessons,new_population)), axis=1)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = GA.cal_pop_fitness(lessons, new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.min(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])