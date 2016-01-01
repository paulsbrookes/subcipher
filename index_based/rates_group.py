class Rates_Group(object):
    def __init__(self, rates_list, natural_rates):
        self.rates_list = rates_list
        self.natural_rates = natural_rates

    def proliferate(self, maps, number_carried=1):
        new_rates = []
        for rates in self.rates_list[0:number_carried]:
            new_rates += [rates.map(map) for map in maps]
        self.rates_list = new_rates

    def rank(self, metric_function, retain=1):
        metric_results = np.zeros(len(self.rates_list))
        for i, rates in enumerate(self.rates_list):
            metric = metric_function(rates, self.natural_rates)
            metric_results[i] = metric
        ranking = np.argsort(metric_results)
        ranked_rates = [self.rates_list[x] for x in ranking]
        filtered_ranked_rates = rm_duplicate_records(ranked_rates, retain)
        self.rates_list = filtered_ranked_rates
