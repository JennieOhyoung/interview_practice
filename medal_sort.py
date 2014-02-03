""" 

Olympics. You're given list of lists where each list is the countries that won the gold, silver and bronze for that activity. Return the countries and their medal counts, prioritizing first gold, silver then bronze. If its a full tie in all 3 categories, alphabetize. 

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

from operator import itemgetter

def default_list(l):
    results = {}
    for medal in l:
        # for each country as a key in dictionary, add name, and start gold silver and bronze count at 0
        for country in medal:
            results.setdefault(country, {"name":country, "gold":0, "silver":0, "bronze":0})
        # the first country in every sublist won gold, 2nd silver, 3rd bronze. use country name as key, increase gold count for that country. 
        results[medal[0]]["gold"]+=1
        results[medal[1]]["silver"]+=1
        results[medal[2]]["bronze"]+=1
    # print results

    # now that i have a tally of total count, I need to sort the result. Since I cant sort a dictionary I need to put everything in a list.
    sorted_result = []
    for k, v in results.iteritems():
        sorted_result.append(v)

    # print sorted_result

    # Now I need to perform the actual sorting
    sorted_list = sorted(sorted_result, key=itemgetter("name"))
    sorted_list = sorted(sorted_result, key=itemgetter("gold","silver","bronze"), reverse=True)
    # print sorted_list

    # The list is in the order I want, now I just need to make sure I print them out in the order I want
    for i in sorted_list:
        print i["name"], i["gold"], i["silver"], i["bronze"]


default_list(l)













