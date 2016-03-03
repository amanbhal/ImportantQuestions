
#=> Method1
#=> for each word in words find another word that has no common char. multiply their lengths and compare to global
#   maxProduct.

#=> O(n**2*m)  n=len(words)  m=length of set of unique chars
def maxProduct1(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    if len(words)==0:
        return 0
    maxProduct = 0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            x = set(words[i])   #convert words[i] to set having only unique characters
            y = set(words[j])   #convert words[j] to set having only unique characters
            #following loop is now reduced to len(x)
            if any(a for a in x if a in y)==False:  #checking if x and y has a common char. if it does then any returns
                                                    # True
                maxProduct = max(len(words[i])*len(words[j]),maxProduct)
    return maxProduct


#=> Method2
#=> Only differece from above solution is that we try to reduce the complexity to O(n**2)
#=> to do this we convert each word into an integer using bit manipulation

from collections import defaultdict

def maxProduct2(words):
    """
    :type words: List[str]
    :rtype: int
    """
    if len(words)==0:
        return 0
    maxProduct = 0
    #convert each word in words into an integer
    stringToNumber = defaultdict(int)
    for i in range(len(words)):
        #construct a 32 bit array where 'a' represents index 31, 'b' represents index 30...so on.
        bits = ['0' for k in range(32)]
        #get all the unique chars from the word
        uniqueChars = set(words[i])
        #set the bit value to 1 for all the chars present in a word
        for j in uniqueChars:
            index = 31-(ord(j)-97)
            bits[index] = '1'
        bits = "".join(bits)
        #convert the bit array into an integer
        number = int(bits,2)
        stringToNumber[words[i]] = number
    #print sortedWordLengths
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            hasCommonCharInt = stringToNumber[words[i]]&stringToNumber[words[j]]
            #print words[i], words[j], hasCommonCharInt
            if hasCommonCharInt==0:
                #print sortedWordLengths[i],sortedWordLengths[j]
                maxProduct = max(len(words[i])*len(words[j]),maxProduct)
    return maxProduct

print maxProduct2(["fcfde","bdedfcceadeed","fdbedccaaf","babfbbabfcefef","abafaceaeb","cebebcfecbcfbc","bf","bbecdbcdf","ffddcebccecfbbacbbfbe","df","eaac","fcfdfed","ad","dbbe","edacbcf","adefbdbbeddfdf","feebbdffbeeffdceaa","cceabeacabeafebc","fdbcfefdba","afbbbfc","fcdaa","ebeadcaaabf","accdbcebddebccaffb","acaabfaeebc","caffadbcaedcebcebcecd","addddcebbaedfca","bafbdcdbebf","afd","bfaceefbcaabcf","abddaeadaebfdaffbd","eebdfbeccbdebacfb","ecbb","bdaffbedcfadefcbffb","fba","aaebeefacafddfcca","aefaacdbdda","caa","edd","fdceffaecaffac","aafceecccdabbbccde","dbacaaeaedecaeabe","aeebdfdcadeebbacffad","edbd","afbdeaceeedbecbadcf","afadddbefeabefcfbcb","aaeeceecdeaffadcdba","badebfedbcdccafaf","fefbafdecdeacbad","aeebaeddeecbcf","cacdadadddfddbdee","bedfff","fabfecbfdfda","ffebbeacfd","dacdaeecafbecfcaea","bafadeeebffccbafcedf","ecfbaef","edabfeaaabed","cccacaeeacfcfcd","faa","dafbca","ccaeedfaaedfcdfedcc","dbdcd","bfdababab","febfedfafcfbabbeafabc","dcdedbccedceb","dafabeedceafe","bffbbdaececebdb","fbbfbefda","fbbf","bfbfcefbeabeddcebdbee","eebbdfbaefebfdfebb","edbfffaddadefbfe","beacbeafecbccb","ecfeddbaee","acbeffcffebfbfeacfbb","addbcbecedcaefedebaf","dacbbaebfccdaedb","effbcfebfc","accdbdebbeeddcafaebd","ccaaafcaddbfadaadfeea","efbeebabcbfbf","febdeadebeba","da","afcbbcabbddcfeefacaf","fdfc","fcdddfbeee","baeeebbdc","dedebcffca","dfbbef","adcbdcbadcefcdceffccc","ebccaae","cffbfcc","fabbcfafed","ebefec","cdeaebaddd","bdffbccfe","fdcecbceafadcaedeafd","bffdabec","ebfcbdfb","bfabedfccacbaddf","ccbe","fcdd","dadafaebedbbcbadaaf","befbaafadeffffd","fffebdbbedfdabcaafbdf","eedfecdbfeafcbe","cdefabcbadcc","bfebcafbfebdaeb","ca","dccbebf","adfebeebbb","afaebfddadacf","ecbccaadfabacddcaa","eefbfefeffcacaff","ddaaaddaa","ade","eaaca","dfca","cafefefc","acf","bacbfbcaa","acbefbd","beaabadedfffddeeaeda","dbcaffbddaaddfcd","cbeecfbcace","edaebacdcc","fcfcabbfffcf","dbfbfbbaefdeeccca","ffabafffcada","fddecd","fbcfaffccdcdfcd","daccdbabbb","feededefdeffcabbcfccc","ecedaad","bfd","fccdadcfaeefcb","abadefbcbaadfcde","fecdbffaae","cacabbfeebcb","bbddbefded","dc","caccf","beefccefbeafebfeaddee","eaceceacbdcbef","fcbfdbfeefdcca","cadccfadad","ecfeaaacdacdabbf","ddddcbfefeecefddbd","fcaaccffbfcaabdffeb","efadbeaeadffccaaaafe","dcbbaded","ad","ffca","faabeccf","fadfecaa","beddaebeddfcab","ddddfdaaedbdfb","dfaeefbd","dddfbefebbcadcbfc","fcbeaeada","ebbedfb","fc","ababcbbdddfbebeeaf","fafccacffb","aceb","ca","daaffbdded","dccbdcebeacadbfcdd","ecfafcdbcbadfcfa","babefcefeaacbdcec","ad","bfaaa","cea","fb","daebcb","edbba","ddbcaabafffadcfed","fffabfbdbeaceecffdc","daaaacdaf","adfbccace","cdf","bcfffabddeeacdfdaad","dfdeaeae","acbbeedeeaafdbcc","edae","cdaebdffcadd","bcccfcacbcad","ddcdefdcfacdaaaaddaf","efdcfdfefcaebfedfec","fdacbddabfecdadffcbf","dfdbbdddafacefbdffef","cddbbdbbfcbb","ea","bddaabdfdcfbfaacebacc","aabeee","dfceacecdaccffea","cecafde","ceebfbdeaddefbafce","deddfdcbdbeacdb","ebfeea","afaeffecaacaddcee","cbccdeeb","cabdafedbdeaceaafcfba","bec","bfdfdbfcffaebbbadec","ebdecff","bb","eccebcffcdfcb","bfb","fccabaaacbdcdbeceb","fbbeafecfbcdbbadfac","caec","ccaefeafdbfacffd","cbbffabddaba","bcbef","eaeafcfcdf","cacbadfbed","dffaebbcafa","fd","baac","ddbaeedaceaeba","fcddfcbba","ddeefbbdf","fcf","ddaf","be","baeebccbca","cadbecfdeae","afa"])