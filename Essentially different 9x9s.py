Burnsides_sum = (1*18383222420692992)+(96*21233664)+(16*107495424)+(192*4204224)+(64*2508084)+(5184*323928)+(20736*162)+(20736*288)+(144*14837760)+(1728*2592)+(288*5184)+(864*2085120)+(3456*1296)+(1728*294912)+(2304*648)+(1152*6342480)+(1296*30258432)+(10368*1854)+(93312*288)+(2916*155492352)+(69984*13056)+(972*449445888)+(3888*27648)+(31104*6480)+(15552*1728)+(15552*3456)+(7776*13824)
print("Burnside sum: " + str(Burnsides_sum))

Geometry_group = 6**8 * 2
print("Order of Geometry group: " + str(Geometry_group))

essentially_different_9x9_Sudokus = Burnsides_sum / Geometry_group
print("Number of essentially different 9x9 Sudokus: " + str(essentially_different_9x9_Sudokus))

number_of_9x9_Sudokus = 6670903752021072936960
print("Ratio of essentially different 9x9 Sudokus to total number of 9x9 Sudokus: 1:" + str(number_of_9x9_Sudokus / essentially_different_9x9_Sudokus))