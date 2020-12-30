## Wikinews (CSSH Forschungspraktikum)
A survey on wikipedia indicates, that things that pop up in the news are frequently being browsed for. We would like to explore the hypothesis further by using a news webpage like nytimes and comparing topics with the viewcounts of wikipedia articles.  

[>> Data access <<](https://rwth-aachen.sciebo.de/s/dHIeP453099jjvZ)

## Statistics

|file suffix|restrictions|articles (nyt)|articles (theguardian)|
|----------------|-------------------------------|-----------------------------|-----------------------------|
|none|published in 2001 or later |2.953.454|2.096.574|
|_reduced|world news articles published in 2001 or later|213.535|168.328|
|_partition|world news articles published in January 2001|678|603|
|_ground_truth|randomly selected world news articles published in 2001 or later **manually labeled** with related wikipedia links (for measuring accuracy of matching algorithms)|200|200|

## Matching: Exemplary results
| Top-Ranking (2019) | keyword | matching result (simple) | computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
|1|says|Says|says president trump|Donald_Trump|
|2|trump|Trump|trump president u.s.|Donald_Trump|
|3|hong|Hong|hong kong protesters|2019–20_Hong_Kong_protests|
|4|kong|Kong|kong hong protesters|2019–20_Hong_Kong_protests|
|5|china|China|china hong kong|Hong_Kong|
|6|brexit|Brexit|brexit johnson prime|Boris_Johnson|
|7|iran|Iran|iran u.s. trump|Donald_Trump|
|8|u.k.|United_Kingdom|u.k. brexit britain|Brexit|
|9|leader|Leadership|leader president trump|Donald_Trump|
|10|election|Election|election minister prime|List_of_prime_ministers_of_India|
|11|protests|Protest|protests hong kong|2019–20_Hong_Kong_protests|
|12|police|Police|police hong kong|Hong_Kong_Police_Force|
|13|korea|Korea|korea north south|North_Korea–South_Korea_relations|
|14|president|President|president trump leader|Donald_Trump|
|15|say|Say|say officials police|SayHerName|
|16|north|North|north korea trump|North_Korea–United_States_relations|
|17|may|May|may brexit minister|Brexit|
|18|india|India|india modi pakistan|Narendra_Modi|
|19|johnson|Johnson|johnson boris brexit|Premiership_of_Boris_Johnson|
|20|south|South|south korea north|North_Korea–South_Korea_relations|
|21|protesters|Protest|protesters hong kong|2019–20_Hong_Kong_protests|
|22|russia|Russia|russia russian putin|Vladimir_Putin|
|23|syria|Syria|syria isis u.s.|Islamic_State_of_Iraq_and_the_Levant|
|24|attack|Attack|attack police killed|2016_shooting_of_Dallas_police_officers|
|25|isis|Islamic_State_of_Iraq_and_the_Levant|isis syria state|Islamic_State_of_Iraq_and_the_Levant|
|26|boris|Boris|boris johnson brexit|Premiership_of_Boris_Johnson|
|27|afghan|Afghan|afghan taliban peace|Afghan_peace_process|
|28|taliban|Taliban|taliban afghan talks|Afghan_peace_process|
|29|venezuela|Venezuela|venezuela maduro opposition|Nicolás_Maduro|
|30|deal|Deal|deal brexit iran|2019_Conservative_Party_leadership_election|
|31|killed|Killed_in_action|killed people least|List_of_people_killed_for_being_transgender|
|32|minister|Minister|minister prime brexit|Timeline_of_Brexit|
|33|military|Military|military u.s. president|List_of_presidents_of_the_United_States_by_military_service|
|34|talks|Talk|talks taliban peace|Afghan_peace_process|
|35|killing|Killing|killing people khashoggi|Assassination_of_Jamal_Khashoggi|
|36|france|France|france president macron|Emmanuel_Macron|
|37|government|Government|government minister president|Minister-president|
|38|israel|Israel|israel netanyahu minister|Benjamin_Netanyahu|
|39|zealand|Zealand|zealand christchurch minister|Christchurch_mosque_shootings|
|40|u.n.|United_Nations|u.n. united nations|United_Nations|
|41|parliament|Parliament|parliament brexit minister|Timeline_of_Brexit|
|42|court|Court|court supreme former|Supreme_Court_of_the_United_States|
|43|death|Death|death toll two|List_of_disasters_in_the_United_States_by_death_toll|
|44|canada|Canada|canada trudeau minister|Margaret_Trudeau|
|45|dead|Death|dead people least|List_of_rampage_killers|
|46|saudi|Saudi|saudi arabia iran|Iran–Saudi_Arabia_relations|
|47|vote|Voting|vote brexit election|Causes_of_the_vote_in_favour_of_Brexit|
|48|party|Party|party election minister|2015_Canadian_federal_election|
|49|japan|Japan|japan korea south|Japan–South_Korea_relations|
|50|first|First|first time president|President_of_East_Timor|

## Interestingness: Exemplary results
|Highest changerate (2019)|Keyword|week: [ total , changerate ]|
|---|---|---|
|1. |charges|2: [12, inf], 4: [12, 6.0]|
|2. |officials|2: [14, inf], 43: [11, 11.0]|
|3. |court|2: [10, inf], 51: [16, inf]|
|4. |venezuela|4: [20, 10.0], 18: [16, inf]|
|5. |maduro|4: [16, 8.0], 8: [19, inf], 18: [10, inf]|
|6. |help|5: [10, inf], 25: [10, 5.0]|
|7. |election|7: [12, 12.0], 11: [10, 10.0], 13: [14, 14.0], 25: [10, inf]|
|8. |report|10: [10, inf]|
|9. |black|10: [11, inf]|
|10. |border|11: [10, 10.0], 14: [12, inf], 46: [12, 12.0]|
|11. |vote|11: [11, inf], 37: [10, 5.0], 50: [10, inf]|
|12. |christchurch|11: [14, inf]|
|13. |mosques|11: [14, inf]|
|14. |massacre|11: [11, inf]|
|15. |erdogan|14: [10, inf]|
|16. |leaders|14: [11, 5.5], 49: [10, inf]|
|17. |india|15: [15, 7.5], 18: [11, inf], 20: [10, 10.0], 51: [17, 5.666666666666667]|
|18. |assange|15: [10, inf]|
|19. |north|16: [13, 6.5], 25: [26, inf], 40: [11, 11.0]|
|20. |notre-dame|16: [33, inf]|
|21. |cathedral|16: [32, inf]|
|22. |paris|16: [14, inf], 40: [10, inf]|
|23. |sri|16: [16, inf]|
|24. |lanka|16: [12, inf]|
|25. |attacks|17: [32, 8.0], 38: [10, inf]|
|26. |sunday|17: [17, inf]|
|27. |putin|17: [10, inf]|
|28. |protest|18: [11, inf], 27: [10, 5.0], 30: [10, inf]|
|29. |opposition|18: [12, inf]|
|30. |guaidó|18: [12, inf]|
|31. |crisis|18: [12, inf]|
|32. |fani|18: [10, inf]|
|33. |iraq|19: [11, inf]|
|34. |last|19: [10, inf]|
|35. |forces|21: [10, 5.0], 31: [10, inf]|
|36. |union|21: [12, 6.0], 42: [10, inf]|
|37. |political|22: [10, 5.0], 29: [14, 14.0], 42: [10, 5.0], 51: [12, inf]|
|38. |boat|22: [13, inf]|
|39. |wife|22: [10, inf]|
|40. |iran|24: [13, inf]|
|41. |shooting|25: [12, inf]|
|42. |must|25: [11, inf]|
|43. |climate|25: [10, inf]|
|44. |mexico|25: [10, 10.0], 45: [10, inf]|
|45. |around|25: [10, inf]|
|46. |g|26: [11, inf]|
|47. |japan|26: [10, inf], 41: [12, 6.0]|
|48. |kashmir|32: [13, inf]|
|49. |iranian|33: [10, inf], 39: [10, 10.0]|
|50. |prince|34: [11, inf]|
|51. |fires|34: [23, inf]|
|52. |amazon|34: [14, inf]|
|53. |residents|36: [10, inf]|
|54. |pope|36: [10, inf]|
|55. |francis|36: [11, inf]|
|56. |australia|37: [12, inf]|
|57. |netanyahu|37: [13, inf], 47: [10, inf]|
|58. |israel|37: [14, inf]|
|59. |gantz|38: [10, inf]|
|60. |trudeau|38: [15, inf]|
|61. |peru|40: [12, inf]|
|62. |kurds|41: [12, inf]|
|63. |kurdish|41: [11, inf]|
|64. |turkey|41: [15, inf]|
|65. |troops|41: [10, inf]|
|66. |syrian|41: [13, inf]|
|67. |militia|41: [11, inf]|
|68. |turkish|41: [10, inf]|
|69. |typhoon|41: [16, inf]|
|70. |amid|42: [11, inf]|
|71. |lawmakers|42: [19, inf]|
|72. |al-baghdadi|43: [10, inf]|
|73. |mining|45: [10, inf]|
|74. |macron|49: [12, inf]|
|75. |eruption|50: [11, inf]|
|76. |white|50: [10, inf]|
|77. |nobel|50: [10, inf]|
|78. |base|50: [10, inf]|
|79. |christmas|52: [18, inf]|
|80. |trump|12: [12, 6.0], 25: [44, 44.0]|
|81. |taliban|4: [23, 23.0]|
|82. |korea|12: [13, 6.5], 25: [22, 22.0]|
|83. |american|9: [19, 19.0]|
|84. |would|4: [18, 18.0]|
|85. |could|2: [10, 10.0], 9: [13, 6.5], 20: [12, 6.0], 33: [17, 17.0]|
|86. |u.s.|9: [24, 6.0], 31: [17, 8.5], 50: [16, 16.0]|
|87. |parliament|35: [16, 8.0], 42: [16, 16.0]|
|88. |people|51: [16, 16.0]|
|89. |zealand|11: [30, 15.0], 50: [11, 5.5]|
|90. |deal|33: [15, 15.0], 42: [35, 5.833333333333333]|
|91. |syria|2: [11, 11.0], 37: [11, 5.5], 41: [28, 14.0]|
|92. |family|23: [12, 6.0], 45: [14, 14.0]|
|93. |canada|9: [13, 13.0]|
|94. |visit|13: [13, 13.0], 23: [21, 5.25]|
|95. |fire|16: [26, 13.0], 46: [11, 5.5]|
|96. |many|18: [10, 10.0], 31: [13, 13.0], 37: [10, 10.0], 44: [11, 5.5]|
|97. |group|26: [13, 13.0]|
|98. |day|37: [13, 13.0]|
|99. |abuse|8: [12, 12.0]|
|100. |state|12: [12, 12.0], 29: [10, 5.0]|
|101. |protests|27: [12, 12.0], 36: [20, 1.0], 52: [11, 11.0]|
|102. |britain|21: [15, 7.5], 30: [11, 11.0]|
|103. |days|41: [11, 11.0]|
|104. |media|50: [11, 11.0]|
|105. |faces|2: [10, 5.0], 11: [10, 10.0]|
|106. |woman|2: [11, 5.5], 14: [10, 10.0]|
|107. |cyclone|12: [12, 6.0], 17: [10, 10.0]|
|108. |storm|12: [11, 5.5], 41: [10, 10.0]|
|109. |head|13: [10, 10.0]|
|110. |brunei|14: [10, 10.0]|
|111. |police|16: [10, 10.0]|
|112. |easter|17: [20, 10.0]|
|113. |came|20: [10, 10.0]|
|114. |queen|23: [10, 10.0]|
|115. |bill|24: [20, 10.0]|
|116. |top|29: [10, 10.0], 39: [10, 5.0]|
|117. |johnson|34: [10, 10.0], 39: [24, 6.0], 50: [15, 5.0]|
|118. |island|50: [10, 10.0]|
|119. |labour|50: [10, 10.0]|
|120. |ethiopian|11: [29, 9.666666666666666]|
|121. |two|19: [18, 9.0]|
|122. |first|24: [17, 8.5], 46: [10, 5.0]|
|123. |africa|36: [17, 8.5]|
|124. |victims|11: [16, 8.0]|
|125. |isis|12: [10, 5.0], 43: [16, 8.0]|
|126. |leader|11: [14, 7.0], 24: [15, 7.5]|
|127. |say|2: [14, 7.0]|
|128. |talks|9: [21, 7.0]|
|129. |time|40: [14, 7.0]|
|130. |corruption|40: [14, 7.0]|
|131. |hong|24: [40, 6.666666666666667]|
|132. |kong|24: [40, 6.666666666666667]|
|133. |law|33: [11, 5.5], 51: [20, 6.666666666666667]|
|134. |plane|11: [13, 6.5]|
|135. |flight|11: [13, 6.5]|
|136. |sudan|15: [13, 6.5]|
|137. |country|36: [13, 6.5]|
|138. |brexit|3: [22, 5.5], 42: [30, 6.0]|
|139. |military|4: [10, 5.0], 29: [12, 6.0]|
|140. |made|8: [12, 6.0]|
|141. |max|11: [12, 6.0]|
|142. |russia|13: [10, 5.0], 46: [12, 6.0]|
|143. |extradition|24: [24, 6.0]|
|144. |party|27: [18, 6.0], 50: [10, 5.0]|
|145. |russian|38: [12, 6.0], 51: [11, 5.5]|
|146. |france|49: [12, 6.0]|
|147. |crash|11: [23, 5.75]|
|148. |vatican|8: [11, 5.5]|
|149. |second|9: [11, 5.5]|
|150. |even|9: [11, 5.5]|
|151. |protesters|23: [11, 5.5]|
|152. |world|23: [16, 5.333333333333333], 47: [11, 5.5]|
|153. |former|35: [11, 5.5]|
|154. |nuclear|45: [11, 5.5]|
|155. |prime|20: [16, 5.333333333333333]|
|156. |car|3: [10, 5.0]|
|157. |europe|7: [10, 5.0]|
|158. |south|7: [10, 5.0]|
|159. |airlines|11: [20, 5.0]|
|160. |campaign|13: [10, 5.0]|
|161. |british|13: [10, 5.0]|
|162. |investigation|13: [10, 5.0]|
|163. |gay|14: [10, 5.0]|
|164. |another|15: [10, 5.0]|
|165. |al-bashir|15: [10, 5.0]|
|166. |violence|16: [10, 5.0]|
|167. |workers|20: [10, 5.0]|
|168. |chinese|22: [10, 5.0]|
|169. |accused|22: [15, 5.0]|
|170. |rights|28: [10, 5.0]|
|171. |killed|31: [10, 5.0], 45: [10, 5.0]|
|172. |tanker|33: [10, 5.0]|
|173. |boris|39: [20, 5.0]|
|174. |says|44: [10, 5.0]|
|175. |evo|46: [10, 5.0]|
|176. |mr.|46: [10, 5.0]|
|177. |government|49: [15, 5.0]|