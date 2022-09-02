import re

all_serach_term_data_dict = [{'Search term' : 'best deodorant', 'Clicks': 4}, {'Search term' : 'extra strength deodorant', 'Clicks' : 1}]

gram_vecs = ['deodorant', 'best', 'extra', 'strength']
stringOfGramVecs = "|".join(gram_vecs)

gram_dict_with_values = {}

for search_term_row in all_serach_term_data_dict:
    #for gram in gram_vecs:
        #if search_term_row['Search term'] == gram or gram + " " in search_term_row['Search term'] or " " + gram in search_term_row['Search term']:
        listOfMatches = re.findall(stringOfGramVecs, 
        search_term_row['Search term'])
        for gram in listOfMatches:
            if gram not in gram_dict_with_values.keys():
                gram_dict_with_values[gram] = {
                    'count' : 1,
                    'Clicks' : search_term_row['Clicks']
                }
            else:
                gram_dict_with_values[gram]['count'] += 1
                gram_dict_with_values[gram]['Clicks'] += search_term_row['Clicks']

print(gram_dict_with_values)
