import numpy as np

def evidential_reasoning_aggregation(input_evidence, weights=[]):
    num_columns = input_evidence.shape[1] - 1
    num_rows = input_evidence.shape[0]

    if weights == []:
        weights = np.ones(num_rows) / num_rows

    weights2 = np.repeat([weights], num_columns + 1, axis=0).transpose()
    input2 = np.multiply(input_evidence, weights2)

    for evidence_row in input2:
        evidence_row[num_columns] = 1 - sum(evidence_row[0:num_columns])

    mnI = input2[0]

    for i in range(1, num_rows):
        mnI_tmp = input2[i]
        K = 0

        for j in range(num_columns):
            for j2 in range(num_columns):
                if j != j2:
                    K += mnI[j] * mnI_tmp[j2]

        K = 1 / (1 - K)

        for j in range(num_columns):
            tmp = (
                mnI[j] * mnI_tmp[j]
                + mnI[num_columns] * mnI_tmp[j]
                + mnI[j] * mnI_tmp[num_columns]
            )
            mnI[j] = K * tmp

    mnI[num_columns] = 1 - sum(mnI[0:num_columns])

    return mnI

# Example Input
# in this example we are comparing 4 criteria, and the strengh of evidence
input_evidence = np.array([
    [0, 0, 0.2, 0.2, 0.6, 0],
    [0, 0, 0.2, 0.4, 0.4, 0],
    [0, 0, 0.2, 0.8, 0, 0],
    [0, 0, 0.4, 0.2, 0.4, 0]
])

weights = np.array([
    0.25,#regulatory
    0.25,#ressearch and development
    0.25,#display quality
    0.25 #performance
])

# Calculate the aggregation
result = evidential_reasoning_aggregation(input_evidence, weights)
print(result)
