# 154 Olympics. You're given list of lists where each list is the countries that won the gold, silver and bronze for that activity. Return the countries and their medal counts, prioritizing first gold, silver then bronze. If its a full tie in all 3 categories, alphabetize. 


from operator import itemgetter
""" 
sample input: [["ITA", "JPN", "AUS"], ["KOR", "TPE", "UKR"], ["KOR", "KOR", "GBR"], ["KOR", "CHN", "TPE"]]

sample output:
KOR 3 1 0
ITA 1 0 0
TPE 0 1 1
CHN 0 1 0
JPN 0 1 0
AUS 0 0 1
GBR 0 0 1
UKR 0 0 1
"""

l = [["ITA", "JPN", "AUS"], ["KOR", "TPE", "UKR"], ["KOR", "KOR", "GBR"], ["KOR", "CHN", "TPE"]]

# naive solution with set

def country_list(l):
    global countries
    countries = set()
    for i in l:
        for country in i:
            countries.add(country)
    return countries

def set_matrix(countries):
    global matrix
    matrix = []
    for country in countries:
        matrix.append(country.split())
    matrix.sort()
    return matrix

def medal_count(l, matrix):
    gold_count = 0
    silver_count = 0
    bronze_count = 0

    for country in matrix:
        for medal in l:
            if country == (medal[0]).split():
                gold_count += 1
            if country == (medal[1]).split():
                silver_count += 1
            if country == (medal[2]).split():
                bronze_count += 1
        country.append(gold_count)
        country.append(silver_count)
        country.append(bronze_count)
        gold_count = 0
        silver_count = 0
        bronze_count = 0
    return matrix

def medal_sort(matrix):
    global sorted_mat
    sorted_mat = sorted(matrix, key=itemgetter(1,2,3), reverse = True)
    print sorted_mat

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print col,
        print

# set_matrix(country_list(l))
# medal_count(l, matrix)
# medal_sort(matrix)
# print_matrix(sorted_mat)


# with dictionary aka the elli method

def generate_ranks(l):
    results = {}
    for score_set in l:
        for country in score_set:
            results.setdefault(country, {"name": country, "gold": 0, "silver": 0, "bronze":0})
        results[score_set[0]]["gold"]+= 1
        results[score_set[1]]["silver"] += 1
        results[score_set[2]]["bronze"] += 1

    list_of_results = []
    for key, value in results.iteritems():
        list_of_results.append(value)

    sorted_list = sorted(list_of_results, key=itemgetter("name"))
    sorted_list = sorted(sorted_list, key=itemgetter("gold", "silver", "bronze"), reverse=True)

    for item in sorted_list:
        print "%s %d %d %d" %(item["name"], item["gold"], item["silver"], item["bronze"])

print generate_ranks(l)



# in class, the katherine way
class Country:
  def __init__(self, name, gold = 0, silver = 0, bronze = 0):
    self.name = name
    self.golds = gold
    self.silvers = silver
    self.bronzes = bronze

def sort_and_print_results(results):
  medal_record = group_results_by_country(results)

  alphabetical_results = sorted(medal_record.values(), key=attrgetter('name'))
  sorted_results_by_medal_count = sorted(alphabetical_results, key=attrgetter('golds', 'silvers', 'bronzes'), reverse = True)

  for country in sorted_results_by_medal_count:
    print country.name, country.golds, country.silvers, country.bronzes

def group_results_by_country(results):
  results_by_country = {}

  for activity in results:
    gold_country = activity[0]
    silver_country = activity[1]
    bronze_country = activity[2]

    results_by_country.setdefault(gold_country, Country(name = gold_country)).golds += 1
    results_by_country.setdefault(silver_country, Country(name = silver_country)).silvers += 1
    results_by_country.setdefault(bronze_country, Country(name = bronze_country)).bronzes += 1

  print results_by_country(l)

