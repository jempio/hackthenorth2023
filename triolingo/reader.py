def readQuote():
    with open('quote.txt') as f:
        return f.readlines()[0] 
    
def readDiff():
    with open('quote.txt') as f:
        return f.readlines()[1] 
    
def readScore():
    with open('score.txt') as f:
        return f.readlines()[0] 
    
