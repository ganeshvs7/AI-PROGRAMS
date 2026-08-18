import math

print("GANESH V S  24BECS157 ")
print("Naive Bayes Classification")

class NaiveBayes:

    def __init__(self):
        self.prior = {}
        self.conditional = {}
        self.classes = []
        self.feature_value_sets = {}
        self.class_feature_counts = {}

    def fit(self, data):
        total_records = len(data)
        labels = [row[-1] for row in data]

        self.classes = list(set(labels))

        # Collect value sets for each feature across the whole dataset
        num_features = len(data[0]) - 1
        for f_idx in range(num_features):
            self.feature_value_sets[f_idx] = set(row[f_idx] for row in data)

        # Calculate Priors
        for c in self.classes:
            self.prior[c] = labels.count(c) / total_records
            self.conditional[c] = {}

        # Calculate Conditionals
        num_features = len(data[0]) - 1

        for c in self.classes:
            sub_data = [
                row[:-1]
                for row in data
                if row[-1] == c
            ]

            sub_total = len(sub_data)
            # record sub_total per class and feature for fallback smoothing
            self.class_feature_counts.setdefault(c, {})

            for f_idx in range(num_features):
                self.conditional[c][f_idx] = {}
                self.class_feature_counts[c][f_idx] = sub_total

                feature_vals = [
                    row[f_idx]
                    for row in data
                ]

                for val in set(feature_vals):
                    count = sum(
                        1
                        for row in sub_data
                        if row[f_idx] == val
                    )

                    # Using Laplace smoothing
                    V = len(self.feature_value_sets[f_idx])
                    self.conditional[c][f_idx][val] = (
                        (count + 1)
                        / (sub_total + V)
                    )

    def predict(self, sample):
        best_class = None
        best_log_prob = float('-inf')

        for c in self.classes:
            # start with log prior
            prior = self.prior.get(c, 0)
            if prior <= 0:
                continue
            log_prob = math.log(prior)

            for f_idx, val in enumerate(sample):
                # if we've seen this value for this class/feature use stored probability
                if val in self.conditional[c].get(f_idx, {}):
                    p = self.conditional[c][f_idx][val]
                else:
                    # fallback Laplace-smoothed probability for unseen value
                    sub_total = self.class_feature_counts[c].get(f_idx, 0)
                    V = len(self.feature_value_sets.get(f_idx, []))
                    # add-one smoothing: count = 0 so (0+1)/(sub_total+V)
                    p = 1 / (sub_total + V) if (sub_total + V) > 0 else 0

                # avoid log(0)
                if p <= 0:
                    log_prob = float('-inf')
                    break

                log_prob += math.log(p)

            # choose the class with highest log-probability; tie-break by higher prior
            if log_prob > best_log_prob:
                best_log_prob = log_prob
                best_class = c
            elif log_prob == best_log_prob:
                # tie-break: choose class with larger prior
                if self.prior.get(c, 0) > self.prior.get(best_class, 0):
                    best_class = c

        return best_class


# Example Usage
if __name__ == "__main__":
    dataset = [
        ['Sunny', 'High', 'No'],
        ['Sunny', 'High', 'No'],
        ['Overcast', 'High', 'Yes'],
        ['Rainy', 'Normal', 'Yes'],
        ['Rainy', 'Normal', 'Yes']
    ]

    nb = NaiveBayes()

    nb.fit(dataset)

    test_instance = ['Sunny', 'Normal']

    print(
        f"Predicted class for {test_instance}:",
        nb.predict(test_instance)
    )