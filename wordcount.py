def findWordCount(userInput):
    userInput = input("Enter a string to check its word count: ")
    wordCount = len(re.split(';|.|,|\*|\n|\t', userInput))
    print ("Your sentence has " +  str(wordCount) + " words.")
    return(wordCount)
