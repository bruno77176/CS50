import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        self.positives = []
        
        file = open(positives,"r")
        for line in file:
            if line.startswith(";") == False:
                self.positives.append(line.strip("\n"))
        file.close()
        
        self.negatives = []
        
        file = open(negatives,"r")
        for line in file:
            if line.startswith(";") == False:
                self.negatives.append(line.strip("\n"))
        file.close()    

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokens = nltk.tokenize.word_tokenize(text)
        score = 0
        for word in tokens:
            if word.lower() in self.positives:
                score += 1
            if word.lower() in self.negatives:
                score -= 1
     
        return score

