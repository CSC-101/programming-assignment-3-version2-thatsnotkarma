import data
#Part1
# Purpose: Calculates the total population from the 2014 population data across all counties in the list.
# Input: A list of CountyDemographics objects containing population data.
# Output: The total population (sum) of all counties for the year 2014 as an integer.
def population_total(demographic_list: list[data.CountyDemographics]) -> int:
   return sum(item.population.get('2014 Population', 0) for item in demographic_list)


#Part2
# Purpose: Filters the demographic list based on the state matching the given word.
# Input: A list of CountyDemographics and a word (state) to filter by.
# Output: A list of CountyDemographics that match the state provided in 'word'.
def filter_by_stat(demographic_list: list[data.CountyDemographics], word: str) -> list[data.CountyDemographics]:
   return [item for item in demographic_list if item.state == word and word is not None]


#Part3
#function1:
# Purpose: Calculates the total population with a certain level of education
# Input: A list of CountyDemographics and the education level to filter by
# Output: A float representing the total population that has the specified education level.
def population_by_education(demographic_list: list[data.CountyDemographics], education: str) -> float:
   population_with_edu = 0.0
   for item in demographic_list:
       if education in item.education:
           high_degree_perc = item.education.get(education, 0) / 100  # Convert percentage to decimal
           county_pop = item.population.get('2014 Population', 0)
           population_with_edu += high_degree_perc * county_pop


   return population_with_edu


#function2
# Purpose: Calculates the total population of a specific ethnicity in the given demographic list.
# Input: A list of CountyDemographics and the ethnicity to filter by
# Output: A float representing the total population of the specified ethnicity.
def population_by_ethnicity(demographic_list: list[data.CountyDemographics], ethnicity: str) -> float:
   total_ethnic_pop = 0.0
   for item in demographic_list:
       if ethnicity in item.ethnicities:
           eth = item.ethnicities.get(ethnicity, 0) / 100
           county_pop = item.population.get('2014 Population', 0)
           total_ethnic_pop += eth * county_pop
   return total_ethnic_pop


#function3
# Purpose: Calculates the total population below the poverty level across the demographic list.
# Input: A list of CountyDemographics.
# Output: A float representing the total population below the poverty level.
def population_below_poverty_level(demographic_list: list[data.CountyDemographics]) -> float:
   total_below_poverty = 0.0
   for item in demographic_list:
       county_pop = item.population.get('2014 Population', 0)
       perc_below_poverty = item.income.get('Persons Below Poverty Level', 0) / 100
       total_below_poverty += county_pop * perc_below_poverty
   return total_below_poverty


#Part4
#Function1
# Purpose: Calculates the percentage of the population with a specified level of education (word) across the demographic list.
# Input: A list of CountyDemographics and a string 'word' representing the education level to calculate
# Output: A float representing the percentage of the total population with the specified education level.
def percent_by_education(demographic: list[data.CountyDemographics], word: str) -> float:
   population_for_edu = 0.0
   total_population = 0.0


   for item in demographic:
       if word in item.education:
           high_degree_perc = item.education.get(word, 0) / 100
           county_pop = item.population.get('2014 Population', 0)
           population_for_edu += high_degree_perc * county_pop


       total_population += item.population.get('2014 Population', 0)


   percentage = (population_for_edu / total_population) * 100 if total_population > 0 else 0
   return percentage
#function2
# Purpose: Calculates the percentage of the population of a specific ethnicity (word) across the demographic list.
# Input: A list of CountyDemographics and a string 'word' representing the ethnicity to calculate
# Output: A float representing the percentage of the total population for the specified ethnicity.
def percent_by_ethnicity(demographic: list[data.CountyDemographics], word: str) -> float:
   population_for_ethnicity = 0.0
   total_population = 0.0


   for item in demographic:
       if word in item.ethnicities:
           ethnic_perc = item.ethnicities.get(word, 0) / 100
           county_pop = item.population.get('2014 Population', 0)
           population_for_ethnicity += ethnic_perc * county_pop


       total_population += item.population.get('2014 Population', 0)


   percentage = (population_for_ethnicity / total_population) * 100 if total_population > 0 else 0
   return percentage
#function3
# Purpose: Calculates the percentage of the population below the poverty level across the demographic list.
# Input: A list of CountyDemographics.
# Output: A float representing the percentage of the total population that is below the poverty level.
def percent_by_poverty(demographic: list[data.CountyDemographics]) -> float:
   total_population_below_poverty = 0.0
   total_population = 0.0


   for item in demographic:
       county_population = item.population.get('2014 Population', 0)
       poverty_percentage = item.income.get('Persons Below Poverty Level', 0) / 100
       total_population_below_poverty += county_population * poverty_percentage
       total_population += county_population
   if total_population > 0:
       poverty_percentage = (total_population_below_poverty / total_population) * 100
   else:
       poverty_percentage = 0.0


   return poverty_percentage


#Part5
#function1:
# Purpose: Filters a list of CountyDemographics to return those with an education level greater than the given number.
# Input: A list of CountyDemographics objects, a string representing the education level, and a float as the threshold value.
# Output: A list of CountyDemographics where the specified education level exceeds the given threshold.
def education_greater_than(demographic: list[data.CountyDemographics], education: str, num: float) -> list[data.CountyDemographics]:
   return [
       item for item in demographic
       if education in item.education and item.education.get(education, 0) > num
   ]
#function2
# Purpose: Filters a list of CountyDemographics to return those with an education level less than the given number.
# Input: A list of CountyDemographics objects, a string representing the education level, and a float as the threshold value.
# Output: A list of CountyDemographics where the specified education level is below the given threshold.
def education_less_than(demographic: list[data.CountyDemographics], education: str, num: float) -> list[data.CountyDemographics]:
   return [
       item for item in demographic
       if education in item.education and item.education.get(education, 0) < num
   ]
#Function3
# Purpose: Filters a list of CountyDemographics to return those with an ethnicity count greater than the given number.
# Input: A list of CountyDemographics objects, a string representing the ethnicity, and a float as the threshold value.
# Output: A list of CountyDemographics where the specified ethnicity count exceeds the given threshold.
def ethnicity_greater_than(demographic: list[data.CountyDemographics], ethnicity: str, num: float) -> list[data.CountyDemographics]:
   return [
       item for item in demographic
       if ethnicity in item.ethnicities and item.ethnicities.get(ethnicity, 0) > num
   ]
#function4
# Purpose: Filters a list of CountyDemographics to return those with an ethnicity count less than the given number.
# Input: A list of CountyDemographics objects, a string representing the ethnicity, and a float as the threshold value.
# Output: A list of CountyDemographics where the specified ethnicity count is below the given threshold.
def ethnicity_less_than(demographic: list[data.CountyDemographics], ethnicity: str, num: float) -> list[data.CountyDemographics]:
   return [
       item for item in demographic
       if ethnicity in item.ethnicities and item.ethnicities.get(ethnicity, 0) < num
   ]
#function5
# Purpose: Filters a list of CountyDemographics to return those with a poverty level greater than the given number.
# Input: A list of CountyDemographics objects and a float representing the poverty level threshold.
# Output: A list of CountyDemographics where the number of persons below the poverty level exceeds the given threshold.
def def_poverty_level_greater_than(demographic: list[data.CountyDemographics], num: float) -> list[data.CountyDemographics]:
   return [
       item for item in demographic
       if item.income.get('Persons Below Poverty Level', 0) > num
   ]
#function6
# Purpose: Filters a list of CountyDemographics to return those with a poverty level less than the given number.
# Input: A list of CountyDemographics objects and a float representing the poverty level threshold.
# Output: A list of CountyDemographics where the number of persons below the poverty level is less than the given threshold.
def def_poverty_level_less_than(demographic: list[data.CountyDemographics], num: float) -> list[data.CountyDemographics]:
   return [
       item for item in demographic
       if item.income.get('Persons Below Poverty Level', 0) < num
   ]
