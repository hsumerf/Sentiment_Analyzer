import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # TODO
        self.positives=positives
        self.negatives=negatives


    def analyze(self, str):
        """Analyze text for sentiment, returning its score."""
        # TODO
        positive_words=set()
        negative_words=set()
        file1 = open(self.positives, "r")
        for line in file1:
            positive_words.add(line.rstrip("\n"))
        file1.close()
        file2 = open(self.negatives,"r")
        for line in file2:
            negative_words.add(line.rstrip("\n"))
        file2.close()
        #str=str.lower()
        if str in positive_words:
             return 1.0
        if str in negative_words:
            return -1.0
        else:
            return 0.0
