import ijson
from fuzzywuzzy import fuzz
from bisect import bisect

# Test cards
# Atraxa, Praetors' Voice
# Demonic Tutor


def SearchCard(search):
    with open('AllCards.json', 'rb') as f:
        events = ijson.parse(f)

        names = []
        ratios = []
        for prefix, event, value in events:
            # Ignore foreignData please, don't need the spanish cards "Atraiçoar"
            if prefix.endswith('.name') and not prefix.endswith('.foreignData.item.name'):
                processedValue = value.strip().lower()
                processedSearch = search.strip().lower()
                nameNext = False
                # is the name equals or not
                ratio = fuzz.ratio(processedValue, processedSearch)
                partialRatio = fuzz.partial_ratio(
                    processedValue, processedSearch)

                if (ratio > 60 or partialRatio > 90) and len(names) < 20:
                    higher = max(ratio, partialRatio)
                    insertIndex = bisect(ratios, higher)
                    names.insert(insertIndex, value)
                    ratios.insert(insertIndex, higher)
                elif (ratio > 90):
                    names.pop(0)
                    insertIndex = bisect(ratios, ratio)
                    names.insert(insertIndex, value)
                    ratios.insert(insertIndex, ratio)

        # Reset file pointer can crash
        f.close()
        # print the ratios of the search
        # for index, ratio in enumerate(ratios):
        #     print("R:%d name:%s" % (ratio, names[index]))
        return names[::-1]


def GetCardByName(name):
    file = open('AllCards.json', 'rb')
    objects = ijson.items(file, name)
    columns = list(objects)

    # print(columns[0])

    if len(columns) > 0:
        file.close()

        return getFields(columns[0])
    else:
        raise Exception('No card with name %s ?' % name)

approved = [
    "name",
    "manaCost",
    "subTypes",
    "type",
    "text",
    "legal"
]
def getFields(fields):
    container = {}
    for key in fields:
        if key in approved:
            container[key] = fields[key]
    return container
