userInput = input("Enter a string to check its word count: ")

def findWordCount(userInput):
    wordCount = len(re.split(';|.|,|\*|\n|\t', userInput))
    print ("Your sentence has " +  str(wordCount) + " words.")
    return(wordCount)
