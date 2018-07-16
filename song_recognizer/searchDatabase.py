
# coding: utf-8

import numpy as np
from collections import Counter

def search_database(dic, fingerpairs,min_matches = 500):
    
    '''
    INPUTS

        dic:   dictionary with (f_n+1, f_n, f_n+1-t_n): [(song_name, t_n)...]

        fingerpairs:     [(f_n+1, f_n, f_n+1-t_n), t_n] x N
        
        min_matches:     minimum number of matches for the top song to be confirmed as the match

    OUTPUTS
    
        name of the song with the most matches
        OR -1 if no single song fulfills the number of min_match
    '''
    
    cnt = Counter()
    for fpair in fingerpairs:
        if fpair[0] in dic:
            for songname, t in dic[fpair[0]]:
              #  print(fpair[1])
              #  print(obj1)
                #print(obj[1].type)
                offset = fpair[1]-t
                cnt[(songname, offset)]+=1
        else: continue
    #song = cnt.most_common(1)
    if len(cnt) > 0 and cnt.most_common(1)[0][1] > min_matches:
        return cnt.most_common(1)[0][0][0] 
    else: return -1


