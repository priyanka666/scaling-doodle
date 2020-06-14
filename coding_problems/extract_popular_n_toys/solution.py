def popularNToys(topToys, toys, quotes):
    """
    :param topToys: maximum number of topToys which we would be interested in
    :param toys: list of toy names in which we are interested
    :param quotes: feedback or quotes given customers about the product
    :return: list of toy names sorted in the order of count and then alphabetical order
    """
    count_of_toy_names = {}
    toys = [toy.lower() for toy in toys]
    for quote in quotes:
        words = quote.split()
        already_in_quote = []
        for word in words:
            word = word.lower()
            if word in toys:
                if word not in count_of_toy_names:
                    count_of_toy_names[word] = 0
                if word not in already_in_quote:
                    count_of_toy_names[word] += 1
                    already_in_quote.append(word)

    count_of_toys_interested = len(count_of_toy_names.keys())
    sorted_dict = [v[0] for v in sorted(count_of_toy_names.iteritems(), key = lambda (k,v):(-v,k))]
    return sorted_dict[:topToys] if count_of_toys_interested>topToys else sorted_dict