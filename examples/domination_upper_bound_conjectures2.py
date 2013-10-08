'''
This file assumes that the conjecturing spkg is installed and that 'conjecturing.py' and
'graphtheory.py' are loaded.
'''

objects = [graphs.CompleteGraph(3), 
           Graph('WxEW?CB?I?_R????_?W?@?OC?AW???O?C??B???G?A?_??R'),
           Graph('PKKOGCO?G?gH?@_?_?_?@C?C'),
           Graph('T{aAA@?G@?C?C?A??_??_?A??C?@??A??A??'),
           Graph('~?BH{aCCA?_C?O?_?_?O?C??_?A??C??C??A???_??C???O???_???_???O???C????_???A????C????C????A?????_????C?????O?????_?????_?????O?????C??????_?????A??????C??????C??????A???????_??????C???????O???????_???????_???????O???????C????????_???????A????????C????????C????????A?????????_????????C?????????O?????????_?????????_?????????O?????????C??????????_?????????A??????????C??????????C??????????A???????????_??????????C???????????O???????????_???????????_???????????O???????????C????????????_???????????A????????????C????????????C????????????A?????????????_????????????C?????????????O?????????????_?????????????_?????????????O?????????????C??????????????_?????????????A??????????????C??????????????C??????????????A???????????????_??????????????C???????????????O???????????????_???????????????_???????????????O???????????????C????????????????_???????????????@????????????????@?????????????????_????????????????G????????????????@?????????????????C?????????????????G?????????????????G?????????????????C?????????????????@??????????????????G??????????????????_?????????????????@??????????????????@???????????????????_??????????????????G??????????????????@???????????????????C???????????????????G???????????????????G???????????????????C???????????????????@????????????????????G????????????????????_???????????????????@????????????????????@?????????????????????_????????????????????G????????????????????@?????????????????????C?????????????????????G?????????????????????G?????????????????????C?????????????????????@??????????????????????G??????????????????????_?????????????????????@??????????????????????@???????????????????????_??????????????????????G??????????????????????@???????????????????????C???????????????????????G???????????????????????G???????????????????????C???????????????????????@????????????????????????G????????????????????????_???????????????????????@????????????????????????@?????????????????????????_????????????????????????G????????????????????????@?????????????????????????C?????????????????????????G?????????????????????????G?????????????????????????C?????????????????????????@??????????????????????????G??????????????????????????_?????????????????????????@??????????????????????????@???????????????????????????_??????????????????????????G??????????????????????????@???????????????????????????C???????????????????????????G???????????????????????????G???????????????????????????C???????????????????????????@????????????????????????????G????????????????????????????_???????????????????????????@????????????????????????????@?????????????????????????????_????????????????????????????G????????????????????????????@?????????????????????????????C?????????????????????????????G?????????????????????????????G?????????????????????????????C?????????????????????????????@??????????????????????????????G??????????????????????????????_?????????????????????????????@??????????????????????????????@???????????????????????????????_??????????????????????????????G??????????????????????????????@???????????????????????????????C???????????????????????????????G???????????????????????????????G???????????????????????????????C???????????????????????????????@????????????????????????????????G????????????????????????????????_???????????????????????????????@????????????????????????????????@?????????????????????????????????_????????????????????????????????G????????????????'),
           Graph('BW'),
           Graph('CU'),
           Graph('E]~o'),
           Graph('G?o~f_'),
           Graph('G?`FE_'),
           Graph('H?BFEbJ'),
           Graph('I?AAFBOqO')]

knownUpperBounds = [matching_number, annihilation_number, fractional_alpha, lovasz_theta, cvetkovic]
for bound in knownUpperBounds:
    invariants.remove(bound)
mainInvariant = invariants.index(dominationNumber) + 1

#switch min and maximum degree
minPos, maxPos = invariants.index(min_degree), invariants.index(max_degree)
invariants[minPos], invariants[maxPos] = invariants[maxPos], invariants[minPos]

conjectures = conjecture(objects, invariants, mainInvariant, upperBound=True)

print("The conjectures are stored in the variable conjectures.")