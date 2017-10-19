class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def print(self):
        print (self.sequence)

    def compliment(self):
        new_seq = []
        bases = {"a":"t", "t":"a", "c":"g", "g":"c"}
        for base in self.sequence:
            compbase = bases.get(base, " ")
            new_seq.append (compbase)
        seqstring = "".join(new_seq)
        print (seqstring)

    def reverse_compliment(self):
        new_seq = []
        bases = {"a": "t", "t": "a", "c": "g", "g": "c"}
        for base in self.sequence:
            compbase = bases.get(base, " ")
            new_seq[0:0] = compbase
        seqstring = "".join(new_seq)
        print(seqstring)

myseq = Sequence("aattggaagc aaatgacatc acagcaggtc agagaaaaag ggttgagcgg caggcaccca")
myseq.print()
myseq.compliment()
myseq.reverse_compliment()