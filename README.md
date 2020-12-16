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