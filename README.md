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
|2|trump|Trump||*topic already covered (see 'says')*|
|3|hong|Hong|hong kong protesters|2019–20_Hong_Kong_protests|
|4|kong|Kong||*topic already covered (see 'hong')*|
|5|china|China|china hong kong|Hong_Kong|
|6|brexit|Brexit|brexit johnson prime|Boris_Johnson|
|7|iran|Iran|iran u.s. trump|United_States_sanctions_against_Iran|
|8|u.k.|United_Kingdom|u.k. brexit britain|Brexit|
|9|leader|Leadership|leader president trump|Donald_Trump|
|10|election|Election|election minister prime|Prime_Minister_of_the_United_Kingdom|
|11|protests|Protest|protests hong kong|2019–20_Hong_Kong_protests|
|12|police|Police|police hong kong|Hong_Kong_Police_Force|
|13|korea|Korea|korea north south|North_Korea–South_Korea_relations|
|14|president|President||*topic already covered (see 'says')*|
|15|say|Say||*topic already covered (see 'says')*|
|16|north|North||*topic already covered (see 'korea')*|
|17|may|May|may brexit minister|Brexit|
|18|india|India|india modi pakistan|Narendra_Modi|
|19|johnson|Johnson||*topic already covered (see 'brexit')*|
|20|south|South||*topic already covered (see 'korea')*|
|21|protesters|Protest||*topic already covered (see 'hong')*|
|22|russia|Russia|russia russian putin|Opposition_to_Vladimir_Putin_in_Russia|
|23|syria|Syria|syria isis u.s.|Islamic_State_of_Iraq_and_the_Levant|
|24|attack|Attack|attack police killed|2016_shooting_of_Dallas_police_officers|
|25|isis|Isis||*topic already covered (see 'syria')*|
|26|boris|Boris|boris johnson brexit|Premiership_of_Boris_Johnson|
|27|afghan|Afghan|afghan taliban peace|Afghan_peace_process|
|28|taliban|Taliban||*topic already covered (see 'afghan')*|
|29|venezuela|Venezuela|venezuela maduro opposition|Nicolás_Maduro|
|30|deal|Deal|deal brexit iran|Dominic_Raab|
|31|killed|Killed_in_action||*topic already covered (see 'attack')*|
|32|minister|Minister||*topic already covered (see 'brexit')*|
|33|military|Military|military u.s. president|List_of_presidents_of_the_United_States_by_military_service|
|34|talks|Talk|talks taliban peace|Afghan_peace_process|
|35|killing|Killing|killing people khashoggi|Assassination_of_Jamal_Khashoggi|
|36|france|France|france president macron|Emmanuel_Macron|
|37|government|Government|government minister president|Minister-president|
|38|israel|Israel|israel netanyahu minister|Benjamin_Netanyahu|
|39|zealand|Zealand|zealand christchurch minister|Christchurch_mosque_shootings|
|40|u.n.|United_Nations|u.n. united nations|Headquarters_of_the_United_Nations|
|41|parliament|Parliament|parliament brexit minister|Timeline_of_Brexit|
|42|court|Court|court supreme former|Supreme_Court_of_the_United_States|
|43|death|Death|death toll two|List_of_wars_by_death_toll|
|44|canada|Canada|canada trudeau minister|Margaret_Trudeau|
|45|dead|Death|dead people least|Dead_cat_strategy|
|46|saudi|Saudi|saudi arabia iran|Iran–Saudi_Arabia_relations|
|47|vote|Voting|vote brexit election|Causes_of_the_vote_in_favour_of_Brexit|
|48|party|Party|party election minister|Prime_Minister_of_Malaysia|
|49|japan|Japan|japan korea south|Japan–South_Korea_relations|
|50|first|First|first time president|List_of_presidents_of_the_United_States_by_age|
