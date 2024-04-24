import random

# Define the objective function (fitness function) to be optimized
def objective_function(x):
    return sum(x)  # Example objective function: sum of all elements

# Generate initial population of antibodies
def initialize_population(pop_size, num_genes, min_value, max_value):
    population = []
    for _ in range(pop_size):
        antibody = [random.uniform(min_value, max_value) for _ in range(num_genes)]
        population.append(antibody)
    return population

# Calculate affinity (fitness) of antibodies
def calculate_affinity(population):
    return [objective_function(antibody) for antibody in population]

# Clone antibodies based on affinity
def clone_antibodies(population, affinity, clone_factor):
    clones = []
    for i, antibody in enumerate(population):
        num_clones = int(clone_factor * affinity[i])
        clones.extend([antibody] * num_clones)
    return clones

# Mutate cloned antibodies to introduce diversity
def mutate_clones(clones, mutation_rate, min_value, max_value):
    mutated_clones = []
    for clone in clones:
        mutated_clone = [gene + random.uniform(-mutation_rate, mutation_rate) for gene in clone]
        mutated_clone = [min(max(gene, min_value), max_value) for gene in mutated_clone]  # Clip values to within range
        mutated_clones.append(mutated_clone)
    return mutated_clones

# Select top antibodies from the combined population of parents and clones
def select_antibodies(population, clone_population, affinity, clone_affinity, pop_size):
    combined_population = population + clone_population
    combined_affinity = affinity + clone_affinity
    sorted_indices = sorted(range(len(combined_affinity)), key=lambda i: combined_affinity[i], reverse=True)
    return [combined_population[i] for i in sorted_indices[:pop_size]]

# Clonal Selection Algorithm
def clonal_selection_algorithm(pop_size, num_genes, min_value, max_value, generations, clone_factor, mutation_rate):
    population = initialize_population(pop_size, num_genes, min_value, max_value)
    for _ in range(generations):
        affinity = calculate_affinity(population)
        clones = clone_antibodies(population, affinity, clone_factor)
        mutated_clones = mutate_clones(clones, mutation_rate, min_value, max_value)
        clone_affinity = calculate_affinity(mutated_clones)
        population = select_antibodies(population, mutated_clones, affinity, clone_affinity, pop_size)
    return population

# Example usage
if __name__ == "__main__":
    pop_size = 50
    num_genes = 5
    min_value = -10
    max_value = 10
    generations = 100
    clone_factor = 2
    mutation_rate = 0.1

    best_solution = clonal_selection_algorithm(pop_size, num_genes, min_value, max_value, generations, clone_factor, mutation_rate)
    print("Best solution:", best_solution)
    print("Objective value:", objective_function(best_solution[0]))
