def wordMatching(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == "__main__":

    sentences=["Python language",'Java langauge','C++ essentials','Flask framework in python','Django in python']
     
    query=input("Please Enter what you want to search \n")

    #finding scores in two sentenses, the query sentsense and the sentce from list

    scores=[wordMatching(query,sentence) for sentence in sentences]
    # print(scores)
    #cretaing a list comphrension, to find sentscore in scores and sentnces and it shud print in descending
    #order, so reverse=True and should give results only if sentscore is not zero
    sortedlist = [sentscore for sentscore in sorted(zip(scores,sentences), reverse=True) if sentscore[0] != 0]
    
    # print(sortedlist)
    print(f"{len(sortedlist)} results found")
    for score, item in sortedlist:
        print(f" \'{item}\'  ")

