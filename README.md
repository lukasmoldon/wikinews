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
|1.|says|Says|says president trump|Donald_Trump|
|2.|trump|Trump|trump president u.s.|Donald_Trump|
|3.|hong|Hong|hong kong protesters|2019–20_Hong_Kong_protests|
|4.|kong|Kong|kong hong protesters|2019–20_Hong_Kong_protests|
|5.|china|China|china hong kong|Hong_Kong|
|6.|brexit|Brexit|brexit johnson prime|Boris_Johnson|
|7.|iran|Iran|iran u.s. trump|Donald_Trump|
|8.|u.k.|United_Kingdom|u.k. brexit britain|Brexit|
|9.|leader|Leadership|leader president trump|Donald_Trump|
|10.|election|Election|election minister prime|List_of_prime_ministers_of_India|
|11.|protests|Protest|protests hong kong|2019–20_Hong_Kong_protests|
|12.|police|Police|police hong kong|Hong_Kong_Police_Force|
|13.|korea|Korea|korea north south|North_Korea–South_Korea_relations|
|14.|president|President|president trump leader|Donald_Trump|
|15.|say|Say|say officials police|SayHerName|
|16.|north|North|north korea trump|North_Korea–United_States_relations|
|17.|may|May|may brexit minister|Brexit|
|18.|india|India|india modi pakistan|Narendra_Modi|
|19.|johnson|Johnson|johnson boris brexit|Premiership_of_Boris_Johnson|
|20.|south|South|south korea north|North_Korea–South_Korea_relations|
|21.|protesters|Protest|protesters hong kong|2019–20_Hong_Kong_protests|
|22.|russia|Russia|russia russian putin|Vladimir_Putin|
|23.|syria|Syria|syria isis u.s.|Islamic_State_of_Iraq_and_the_Levant|
|24.|attack|Attack|attack police killed|2016_shooting_of_Dallas_police_officers|
|25.|isis|Islamic_State_of_Iraq_and_the_Levant|isis syria state|Islamic_State_of_Iraq_and_the_Levant|
|26.|boris|Boris|boris johnson brexit|Premiership_of_Boris_Johnson|
|27.|afghan|Afghan|afghan taliban peace|Afghan_peace_process|
|28.|taliban|Taliban|taliban afghan talks|Afghan_peace_process|
|29.|venezuela|Venezuela|venezuela maduro opposition|Nicolás_Maduro|
|30.|deal|Deal|deal brexit iran|2019_Conservative_Party_leadership_election|
|31.|killed|Killed_in_action|killed people least|List_of_people_killed_for_being_transgender|
|32.|minister|Minister|minister prime brexit|Timeline_of_Brexit|
|33.|military|Military|military u.s. president|List_of_presidents_of_the_United_States_by_military_service|
|34.|talks|Talk|talks taliban peace|Afghan_peace_process|
|35.|killing|Killing|killing people khashoggi|Assassination_of_Jamal_Khashoggi|
|36.|france|France|france president macron|Emmanuel_Macron|
|37.|government|Government|government minister president|Minister-president|
|38.|israel|Israel|israel netanyahu minister|Benjamin_Netanyahu|
|39.|zealand|Zealand|zealand christchurch minister|Christchurch_mosque_shootings|
|40.|u.n.|United_Nations|u.n. united nations|United_Nations|
|41.|parliament|Parliament|parliament brexit minister|Timeline_of_Brexit|
|42.|court|Court|court supreme former|Supreme_Court_of_the_United_States|
|43.|death|Death|death toll two|List_of_disasters_in_the_United_States_by_death_toll|
|44.|canada|Canada|canada trudeau minister|Margaret_Trudeau|
|45.|dead|Death|dead people least|List_of_rampage_killers|
|46.|saudi|Saudi|saudi arabia iran|Iran–Saudi_Arabia_relations|
|47.|vote|Voting|vote brexit election|Causes_of_the_vote_in_favour_of_Brexit|
|48.|party|Party|party election minister|2015_Canadian_federal_election|
|49.|japan|Japan|japan korea south|Japan–South_Korea_relations|
|50.|first|First|first time president|President_of_East_Timor|

## Interestingness: Exemplary results (min_weektotal=10, min_changerate=5)
|Highest changerate (2019)|Keyword|week: [ total , changerate ]|
|---|---|---|
|1. |charges|2: [12, inf], 4: [12, 6.0]|
|1. |officials|2: [14, inf], 43: [11, 11.0]|
|1. |court|2: [10, inf], 51: [16, inf]|
|1. |venezuela|4: [20, 10.0], 18: [16, inf]|
|1. |maduro|4: [16, 8.0], 8: [19, inf], 18: [10, inf]|
|1. |help|5: [10, inf], 25: [10, 5.0]|
|1. |election|7: [12, 12.0], 11: [10, 10.0], 13: [14, 14.0], 25: [10, inf]|
|1. |report|10: [10, inf]|
|1. |black|10: [11, inf]|
|1. |border|11: [10, 10.0], 14: [12, inf], 46: [12, 12.0]|
|1. |vote|11: [11, inf], 37: [10, 5.0], 50: [10, inf]|
|1. |christchurch|11: [14, inf]|
|1. |mosques|11: [14, inf]|
|1. |massacre|11: [11, inf]|
|1. |erdogan|14: [10, inf]|
|1. |leaders|14: [11, 5.5], 49: [10, inf]|
|1. |india|15: [15, 7.5], 18: [11, inf], 20: [10, 10.0], 51: [17, 5.666666666666667]|
|1. |assange|15: [10, inf]|
|1. |north|16: [13, 6.5], 25: [26, inf], 40: [11, 11.0]|
|1. |notre-dame|16: [33, inf]|
|1. |cathedral|16: [32, inf]|
|1. |paris|16: [14, inf], 40: [10, inf]|
|1. |sri|16: [16, inf]|
|1. |lanka|16: [12, inf]|
|1. |attacks|17: [32, 8.0], 38: [10, inf]|
|1. |sunday|17: [17, inf]|
|1. |putin|17: [10, inf]|
|1. |protest|18: [11, inf], 27: [10, 5.0], 30: [10, inf]|
|1. |opposition|18: [12, inf]|
|1. |guaidó|18: [12, inf]|
|1. |crisis|18: [12, inf]|
|1. |fani|18: [10, inf]|
|1. |iraq|19: [11, inf]|
|1. |last|19: [10, inf]|
|1. |forces|21: [10, 5.0], 31: [10, inf]|
|1. |union|21: [12, 6.0], 42: [10, inf]|
|1. |political|22: [10, 5.0], 29: [14, 14.0], 42: [10, 5.0], 51: [12, inf]|
|1. |boat|22: [13, inf]|
|1. |wife|22: [10, inf]|
|1. |iran|24: [13, inf]|
|1. |shooting|25: [12, inf]|
|1. |must|25: [11, inf]|
|1. |climate|25: [10, inf]|
|1. |mexico|25: [10, 10.0], 45: [10, inf]|
|1. |around|25: [10, inf]|
|1. |g|26: [11, inf]|
|1. |japan|26: [10, inf], 41: [12, 6.0]|
|1. |kashmir|32: [13, inf]|
|1. |iranian|33: [10, inf], 39: [10, 10.0]|
|1. |prince|34: [11, inf]|
|1. |fires|34: [23, inf]|
|1. |amazon|34: [14, inf]|
|1. |residents|36: [10, inf]|
|1. |pope|36: [10, inf]|
|1. |francis|36: [11, inf]|
|1. |australia|37: [12, inf]|
|1. |netanyahu|37: [13, inf], 47: [10, inf]|
|1. |israel|37: [14, inf]|
|1. |gantz|38: [10, inf]|
|1. |trudeau|38: [15, inf]|
|1. |peru|40: [12, inf]|
|1. |kurds|41: [12, inf]|
|1. |kurdish|41: [11, inf]|
|1. |turkey|41: [15, inf]|
|1. |troops|41: [10, inf]|
|1. |syrian|41: [13, inf]|
|1. |militia|41: [11, inf]|
|1. |turkish|41: [10, inf]|
|1. |typhoon|41: [16, inf]|
|1. |amid|42: [11, inf]|
|1. |lawmakers|42: [19, inf]|
|1. |al-baghdadi|43: [10, inf]|
|1. |mining|45: [10, inf]|
|1. |macron|49: [12, inf]|
|1. |eruption|50: [11, inf]|
|1. |white|50: [10, inf]|
|1. |nobel|50: [10, inf]|
|1. |base|50: [10, inf]|
|1. |christmas|52: [18, inf]|
|80. |trump|12: [12, 6.0], 25: [44, 44.0]|
|81. |taliban|4: [23, 23.0]|
|82. |korea|12: [13, 6.5], 25: [22, 22.0]|
|83. |american|9: [19, 19.0]|
|84. |would|4: [18, 18.0]|
|85. |could|2: [10, 10.0], 9: [13, 6.5], 20: [12, 6.0], 33: [17, 17.0]|
|86. |u.s.|9: [24, 6.0], 31: [17, 8.5], 50: [16, 16.0]|
|86. |parliament|35: [16, 8.0], 42: [16, 16.0]|
|86. |people|51: [16, 16.0]|
|89. |zealand|11: [30, 15.0], 50: [11, 5.5]|
|89. |deal|33: [15, 15.0], 42: [35, 5.833333333333333]|
|91. |syria|2: [11, 11.0], 37: [11, 5.5], 41: [28, 14.0]|
|91. |family|23: [12, 6.0], 45: [14, 14.0]|
|93. |canada|9: [13, 13.0]|
|93. |visit|13: [13, 13.0], 23: [21, 5.25]|
|93. |fire|16: [26, 13.0], 46: [11, 5.5]|
|93. |many|18: [10, 10.0], 31: [13, 13.0], 37: [10, 10.0], 44: [11, 5.5]|
|93. |group|26: [13, 13.0]|
|93. |day|37: [13, 13.0]|
|99. |abuse|8: [12, 12.0]|
|99. |state|12: [12, 12.0], 29: [10, 5.0]|
|99. |protests|27: [12, 12.0], 36: [20, 1.0], 52: [11, 11.0]|
|102. |britain|21: [15, 7.5], 30: [11, 11.0]|
|102. |days|41: [11, 11.0]|
|102. |media|50: [11, 11.0]|
|105. |faces|2: [10, 5.0], 11: [10, 10.0]|
|105. |woman|2: [11, 5.5], 14: [10, 10.0]|
|105. |cyclone|12: [12, 6.0], 17: [10, 10.0]|
|105. |storm|12: [11, 5.5], 41: [10, 10.0]|
|105. |head|13: [10, 10.0]|
|105. |brunei|14: [10, 10.0]|
|105. |police|16: [10, 10.0]|
|105. |easter|17: [20, 10.0]|
|105. |came|20: [10, 10.0]|
|105. |queen|23: [10, 10.0]|
|105. |bill|24: [20, 10.0]|
|105. |top|29: [10, 10.0], 39: [10, 5.0]|
|105. |johnson|34: [10, 10.0], 39: [24, 6.0], 50: [15, 5.0]|
|105. |island|50: [10, 10.0]|
|105. |labour|50: [10, 10.0]|
|120. |ethiopian|11: [29, 9.666666666666666]|
|121. |two|19: [18, 9.0]|
|122. |first|24: [17, 8.5], 46: [10, 5.0]|
|122. |africa|36: [17, 8.5]|
|124. |victims|11: [16, 8.0]|
|124. |isis|12: [10, 5.0], 43: [16, 8.0]|
|126. |leader|11: [14, 7.0], 24: [15, 7.5]|
|127. |say|2: [14, 7.0]|
|127. |talks|9: [21, 7.0]|
|127. |time|40: [14, 7.0]|
|127. |corruption|40: [14, 7.0]|
|131. |hong|24: [40, 6.666666666666667]|
|131. |kong|24: [40, 6.666666666666667]|
|131. |law|33: [11, 5.5], 51: [20, 6.666666666666667]|
|134. |plane|11: [13, 6.5]|
|134. |flight|11: [13, 6.5]|
|134. |sudan|15: [13, 6.5]|
|134. |country|36: [13, 6.5]|
|138. |brexit|3: [22, 5.5], 42: [30, 6.0]|
|138. |military|4: [10, 5.0], 29: [12, 6.0]|
|138. |made|8: [12, 6.0]|
|138. |max|11: [12, 6.0]|
|138. |russia|13: [10, 5.0], 46: [12, 6.0]|
|138. |extradition|24: [24, 6.0]|
|138. |party|27: [18, 6.0], 50: [10, 5.0]|
|138. |russian|38: [12, 6.0], 51: [11, 5.5]|
|138. |france|49: [12, 6.0]|
|147. |crash|11: [23, 5.75]|
|148. |vatican|8: [11, 5.5]|
|148. |second|9: [11, 5.5]|
|148. |even|9: [11, 5.5]|
|148. |protesters|23: [11, 5.5]|
|148. |world|23: [16, 5.333333333333333], 47: [11, 5.5]|
|148. |former|35: [11, 5.5]|
|148. |nuclear|45: [11, 5.5]|
|155. |prime|20: [16, 5.333333333333333]|
|156. |car|3: [10, 5.0]|
|156. |europe|7: [10, 5.0]|
|156. |south|7: [10, 5.0]|
|156. |airlines|11: [20, 5.0]|
|156. |campaign|13: [10, 5.0]|
|156. |british|13: [10, 5.0]|
|156. |investigation|13: [10, 5.0]|
|156. |gay|14: [10, 5.0]|
|156. |another|15: [10, 5.0]|
|156. |al-bashir|15: [10, 5.0]|
|156. |violence|16: [10, 5.0]|
|156. |workers|20: [10, 5.0]|
|156. |chinese|22: [10, 5.0]|
|156. |accused|22: [15, 5.0]|
|156. |rights|28: [10, 5.0]|
|156. |killed|31: [10, 5.0], 45: [10, 5.0]|
|156. |tanker|33: [10, 5.0]|
|156. |boris|39: [20, 5.0]|
|156. |says|44: [10, 5.0]|
|156. |evo|46: [10, 5.0]|
|156. |mr.|46: [10, 5.0]|
|156. |government|49: [15, 5.0]|