def patterns(rows, columns):
    sequences = []
    seq = []
    for i in range(rows):
        for j in range(columns):
            for k in range(columns):
                if k == j:
                    seq.append(1)
                else:
                    seq.append(0)
            seq.extend(seq)
            sequences.append(seq)
            seq = []
    print(sequences)
