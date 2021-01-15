# Keywords with the highest 'interestingness' in 2016

### Explanation:
- These tables only consider keywords in articles, which have been categorized as 'world news articles' by the
respective newspaper. 
- The table lists all keywords which fulfill the following two conditions at the same time in at least one calendar week:
	- 1. Keyword was mentioned at least 10 times in the news in a week.
	- 2. Keyword was not mentioned in the respective calendar week before (maximum/infinite changerate of news mentions).
- Additionally calendar weeks, where these keywords have a changerate of at least 5, are also given.
- **Column 1:** The row number, the table is sorted  by the first appearing calendar week of each keyword.
- **Column 2:** The name of the keyword
- **Column 3:** The changerates, which fulfill the conditions (as described above): The first value in front of the brackets represents the corresponding calendar week number. The first value within the brackets represents the total frequency of the keyword in that week. The second value represents the changerate compared to the week before.
- **Column 4:** The computed query for our advanced keyword matching approach
- **Column 5:** The name* of the resulting Wikipedia article computed from our advanced keyword matching approach. Here we use column 4 as query for the API call.

(* use the link https://en.wikipedia.org/wiki/_PLACEHOLDER_ and replace the placeholder by the name)


## Results - New York Times:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | states | 1: [17, inf] | states united u.s. | U.S._state |
| 2. | united | 1: [21, inf], 36: [20, 5.0] | united states nations | Member_states_of_the_United_Nations |
| 3. | political | 1: [10, inf], 17: [15, 5.0], 26: [15, 7.5] | political president government | President_(government_title) |
| 4. | would | 1: [11, inf], 4: [17, 17.0] | would president says | President_of_the_United_States |
| 5. | reports | 1: [10, inf] | reports news united | U.S._News_&_World_Report |
| 6. | death | 1: [10, inf], 26: [10, 10.0] | death police people | Saskatoon_freezing_deaths |
| 7. | korea | 1: [14, inf], 22: [16, 8.0] | korea north south | North_Korea–South_Korea_relations |
| 8. | attacks | 1: [11, inf], 51: [10, inf] | attacks brussels paris | 2016_Brussels_bombings |
| 9. | months | 1: [10, inf] | months government two | Month |
| 10. | u.s. | 1: [10, 5.0], 26: [10, inf] | u.s. american united | United_States |
| 11. | police | 1: [11, 11.0], 10: [13, inf], 29: [16, 5.33], 34: [19, 9.5], 40: [15, 5.0], 51: [15, 7.5] | police attack killed | 2016_shooting_of_Dallas_police_officers |
| 12. | iraq | 1: [10, inf], 8: [10, 5.0], 27: [14, inf], 42: [13, 13.0] | iraq isis syria | Islamic_State_of_Iraq_and_the_Levant |
| 13. | isis | 1: [11, inf], 26: [17, 17.0] | isis state islamic | Islamic_State_of_Iraq_and_the_Levant |
| 14. | roosevelt | 1: [10, inf], 15: [10, 10.0] | roosevelt international herald | Roosevelt_dictatorship |
| 15. | say | 1: [10, inf], 40: [18, 18.0] | say officials police | SayHerName |
| 16. | release | 2: [10, inf] | release iran u.s. | Iran–United_States_relations |
| 17. | taiwan | 2: [17, inf], 15: [15, inf] | taiwan china president | President_of_the_Republic_of_China |
| 18. | burkina | 2: [10, inf] | burkina faso ouagadougou | Ouagadougou |
| 19. | faso | 2: [10, inf] | faso burkina ouagadougou | Ouagadougou |
| 20. | week | 3: [12, 6.0], 29: [10, inf] | week last china | Last_Week_Tonight_with_John_Oliver |
| 21. | women | 4: [13, inf], 10: [12, 6.0] | women female year | List_of_female_spacefarers |
| 22. | center | 4: [10, inf] | center city detention | Baltimore_City_Detention_Center |
| 23. | seven | 5: [10, inf] | seven years officials | Seven_Years_in_Tibet_(1997_film) |
| 24. | israel | 6: [10, 10.0], 26: [15, 5.0], 35: [11, 11.0], 37: [14, inf] | israel israeli palestinian | Israeli–Palestinian_conflict |
| 25. | arab | 6: [12, inf] | arab emirates united | United_Arab_Emirates |
| 26. | nuclear | 6: [10, 10.0], 31: [10, inf] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 27. | rights | 7: [11, 5.5], 10: [10, 5.0], 23: [11, 5.5], 31: [15, inf], 34: [10, inf] | rights human china | Human_rights_in_China |
| 28. | vote | 7: [10, inf], 15: [10, 5.0] | vote britain union | Brexit |
| 29. | turkey | 7: [16, inf], 28: [27, 13.5] | turkey erdogan president | Recep_Tayyip_Erdoğan |
| 30. | border | 7: [12, 6.0], 24: [13, inf] | border killed near | Deaths_along_the_Bangladesh–India_border |
| 31. | obama | 10: [14, inf], 12: [30, 5.0], 16: [21, 5.25], 35: [12, 6.0], 46: [17, 5.67] | obama president u.s. | Barack_Obama |
| 32. | syria | 11: [14, inf] | syria russia united | Russian_military_intervention_in_the_Syrian_Civil_War |
| 33. | panama | 14: [20, inf] | panama papers minister | Panama_Papers |
| 34. | papers | 14: [19, inf] | papers panama minister | Panama_Papers |
| 35. | law | 14: [13, inf] | law international china | Chinese_law |
| 36. | leaked | 14: [10, inf] | leaked papers panama | Panama_Papers |
| 37. | offshore | 14: [10, inf] | offshore panama papers | Panama_Papers |
| 38. | official | 14: [10, 10.0], 34: [10, inf] | official says china | SAIC-GM |
| 39. | city | 15: [10, inf], 24: [14, 7.0] | city aleppo china | Ancient_City_of_Aleppo |
| 40. | britain | 16: [12, inf] | britain european union | Brexit |
| 41. | fort | 18: [12, inf] | fort mcmurray alberta | Fort_McMurray |
| 42. | mcmurray | 18: [11, inf] | mcmurray fort alberta | Fort_McMurray |
| 43. | nigeria | 19: [13, inf] | nigeria boko haram | Boko_Haram |
| 44. | bbc | 19: [10, inf] | bbc inquiry savile | Jimmy_Savile_sexual_abuse_scandal |
| 45. | moves | 20: [10, inf] | moves u.s. president | Historical_rankings_of_presidents_of_the_United_States |
| 46. | made | 20: [10, inf], 40: [10, 5.0] | made president china | President_of_the_People's_Republic_of_China |
| 47. | plane | 20: [17, inf] | plane crash flight | US_Airways_Flight_1549 |
| 48. | egyptair | 20: [13, inf] | egyptair flight plane | EgyptAir_Flight_804 |
| 49. | flight | 20: [10, inf] | flight plane egyptair | EgyptAir_Flight_804 |
| 50. | vietnam | 20: [10, inf] | vietnam international herald | Hoàng_Thùy_Linh |
| 51. | hiroshima | 21: [25, inf] | hiroshima obama visit | Barack_Obama |
| 52. | beijing | 22: [13, inf], 45: [11, 5.5] | beijing china chinese | Beijing |
| 53. | tiger | 22: [12, inf] | tiger temple officials | Tiger_Temple |
| 54. | temple | 22: [10, inf] | temple tiger officials | Tiger_Temple |
| 55. | troops | 24: [12, inf] | troops international herald | Insurgency_in_the_Maghreb_(2002–present) |
| 56. | protest | 24: [11, inf] | protest government president | Protest |
| 57. | cox | 24: [11, inf] | cox mair killing | Murder_of_Jo_Cox |
| 58. | referendum | 25: [11, inf] | referendum britain vote | 2016_United_Kingdom_European_Union_membership_referendum |
| 59. | election | 26: [12, 12.0], 31: [14, 7.0], 48: [11, inf] | election party president | 2012_United_States_presidential_election |
| 60. | two | 26: [17, 17.0], 51: [10, inf] | two killed years | Kill_Bill:_Volume_2 |
| 61. | assault | 26: [10, inf] | assault attack police | Alleged_assault_of_Jussie_Smollett |
| 62. | groups | 26: [12, inf] | groups rights say | Men's_rights_movement |
| 63. | climate | 26: [10, inf] | climate change trump | Environmental_policy_of_the_Donald_Trump_administration |
| 64. | july | 26: [11, inf] | july international archives | Archive |
| 65. | battle | 26: [16, inf], 42: [10, 10.0] | battle killed mosul | Battle_of_Mosul_(2016–17) |
| 66. | civilians | 28: [10, inf] | civilians killed syrian | Casualties_of_the_Syrian_Civil_War |
| 67. | korean | 28: [15, inf] | korean south north | North_Korea–South_Korea_relations |
| 68. | nice | 28: [21, inf] | nice attack truck | 2016_Nice_truck_attack |
| 69. | truck | 28: [16, inf], 51: [10, inf] | truck attack nice | 2016_Nice_truck_attack |
| 70. | coup | 28: [21, inf] | coup turkey erdogan | 2016_Turkish_coup_d'état_attempt |
| 71. | group | 29: [10, 5.0], 31: [11, inf] | group killed militant | Al-Shabaab_(militant_group) |
| 72. | trump | 29: [12, inf], 45: [49, 12.25] | trump donald j. | Donald_Trump |
| 73. | pope | 30: [16, inf], 44: [14, inf] | pope francis church | Pope_Francis |
| 74. | francis | 30: [10, inf] | francis pope church | Pope_Francis |
| 75. | kong | 33: [11, inf] | kong hong china | Hong_Kong |
| 76. | haiti | 33: [11, inf] | haiti cholera hurricane | 2010s_Haiti_cholera_outbreak |
| 77. | cholera | 33: [11, inf] | cholera haiti united | 2010s_Haiti_cholera_outbreak |
| 78. | italy | 34: [11, inf] | italy italian renzi | Matteo_Renzi |
| 79. | debate | 35: [10, inf] | debate china lawmakers | 2036:_Nexus_Dawn |
| 80. | west | 35: [11, inf] | west bank palestinian | Palestinian_territories |
| 81. | september | 35: [12, inf] | september archives international | Archive |
| 82. | near | 36: [14, inf] | near killed attack | List_of_fatal_cougar_attacks_in_North_America |
| 83. | become | 36: [10, inf] | become president china | President_of_the_Republic_of_China |
| 84. | opposition | 37: [10, inf] | opposition leader president | Leader_of_the_Opposition_(India) |
| 85. | myanmar | 37: [10, inf] | myanmar aung san | Aung_San_Suu_Kyi |
| 86. | policy | 38: [11, inf] | policy foreign china | Foreign_policy_of_China |
| 87. | global | 38: [10, inf] | global foreign china | China_Global_Television_Network |
| 88. | shimon | 39: [10, inf] | shimon peres israel | Shimon_Peres |
| 89. | peres | 39: [14, inf] | peres shimon israel | Shimon_Peres |
| 90. | matthew | 40: [10, inf] | matthew hurricane haiti | Effects_of_Hurricane_Matthew_in_Haiti |
| 91. | storm | 40: [10, inf] | storm least hurricane | 2020_Atlantic_hurricane_season |
| 92. | taliban | 40: [10, inf] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 93. | religious | 40: [10, inf] | religious pope president | Pope_Francis |
| 94. | toward | 40: [10, inf] | toward china leader | China |
| 95. | king | 41: [11, inf] | king international herald | The_New_York_Times_International_Edition |
| 96. | aid | 42: [10, inf] | aid syria united | Syrian_civil_war |
| 97. | known | 44: [11, inf] | known group last | List_of_languages_by_time_of_extinction |
| 98. | j. | 45: [10, inf] | j. trump donald | Donald_Trump |
| 99. | free | 46: [10, inf] | free north minister | North_American_Free_Trade_Agreement |
| 100. | language | 47: [11, inf] | language say china | China_Can_Say_No |
| 101. | castro | 47: [11, inf] | castro cuba obama | Raúl_Castro |
| 102. | paris | 50: [10, inf] | paris attacks international | November_2015_Paris_attacks |
| 103. | berlin | 51: [26, inf] | berlin attack germany | 2016_Berlin_truck_attack |
| 104. | amri | 51: [10, inf] | amri berlin anis | 2016_Berlin_truck_attack |
| 105. | north | 1: [15, 7.5], 22: [22, 22.0] | north korea south | North_Korea–South_Korea_relations |
| 106. | mexico | 6: [16, 16.0] | mexico pope mexican | Mexico |
| 107. | media | 12: [15, 15.0] | media news social | Social_media_as_a_news_source |
| 108. | officials | 1: [14, 14.0], 22: [15, 7.5] | officials u.s. say | Threatening_government_officials_of_the_United_States |
| 109. | israeli | 2: [14, 14.0] | israeli israel palestinian | Israeli–Palestinian_conflict |
| 110. | france | 10: [14, 7.0], 26: [11, 5.5], 28: [26, 13.0], 31: [11, 5.5], 47: [10, 10.0] | france international archives | Archive |
| 111. | union | 2: [10, 5.0], 7: [10, 10.0], 44: [12, 12.0] | union european britain | Brexit |
| 112. | foreign | 4: [15, 5.0], 17: [15, 7.5], 40: [12, 12.0] | foreign minister china | Foreign_Minister_of_the_People's_Republic_of_China |
| 113. | last | 5: [12, 6.0], 15: [11, 5.5], 47: [12, 12.0] | last year week | ISO_week_date |
| 114. | news | 10: [11, 11.0], 12: [12, 12.0] | news media china | Xinhua_News_Agency |
| 115. | russian | 11: [12, 12.0] | russian russia syria | Russian_military_intervention_in_the_Syrian_Civil_War |
| 116. | terrorist | 51: [12, 12.0] | terrorist attack attacks | September_11_attacks |
| 117. | international | 1: [23, 11.5] | international herald tribune | The_New_York_Times_International_Edition |
| 118. | herald | 1: [22, 11.0] | herald tribune international | The_New_York_Times_International_Edition |
| 119. | tribune | 1: [22, 11.0] | tribune herald international | The_New_York_Times_International_Edition |
| 120. | islamic | 2: [11, 11.0], 21: [10, 10.0], 26: [15, 5.0] | islamic state isis | Islamic_State_of_Iraq_and_the_Levant |
| 121. | minister | 2: [11, 11.0], 49: [35, 7.0] | minister prime britain | Prime_Minister_of_the_United_Kingdom |
| 122. | british | 3: [11, 11.0], 6: [13, 6.5] | british britain international | British_Midland_International |
| 123. | killings | 24: [11, 11.0] | killings police mass | Mass_killings_under_communist_regimes |
| 124. | recep | 28: [11, 11.0] | recep erdogan president | Recep_Tayyip_Erdoğan |
| 125. | tayyip | 28: [11, 11.0] | tayyip erdogan president | Recep_Tayyip_Erdoğan |
| 126. | hong | 33: [11, 11.0] | hong kong china | Hong_Kong |
| 127. | court | 44: [11, 11.0] | court supreme international | Supreme_Court_of_the_United_States |
| 128. | donald | 45: [22, 11.0] | donald trump j. | Donald_Trump |
| 129. | archives | 1: [21, 10.5] | archives herald international | The_New_York_Times_International_Edition |
| 130. | market | 51: [21, 10.5] | market attack killed | 2016_Berlin_truck_attack |
| 131. | leader | 1: [10, 10.0] | leader president party | Party_leaders_of_the_United_States_Senate |
| 132. | world | 2: [10, 10.0], 19: [11, 5.5] | world around president | Around_the_world_(card_game) |
| 133. | chinese | 3: [10, 10.0], 7: [13, 6.5], 19: [13, 6.5], 35: [16, 5.33] | chinese china beijing | Beijing |
| 134. | home | 5: [10, 10.0] | home president leader | List_of_presidents_of_the_Indian_National_Congress |
| 135. | spain | 9: [10, 10.0] | spain government party | Government_of_Spain |
| 136. | accused | 15: [10, 10.0] | accused president police | Interpol |
| 137. | could | 18: [10, 10.0] | could says government | 2020_United_States_federal_government_data_breach |
| 138. | nazi | 19: [10, 10.0] | nazi international herald | Neo-Nazism |
| 139. | children | 21: [10, 10.0] | children least says | List_of_people_with_the_most_children |
| 140. | russia | 24: [10, 5.0], 42: [20, 10.0] | russia syria russian | Russian_military_intervention_in_the_Syrian_Civil_War |
| 141. | town | 27: [10, 10.0] | town residents killed | Ocean_Falls |
| 142. | germany | 29: [10, 10.0], 51: [13, 6.5] | germany german merkel | Angela_Merkel |
| 143. | chief | 32: [10, 10.0] | chief police president | Chief_of_police |
| 144. | report | 37: [10, 10.0] | report says rights | Human_rights |
| 145. | trudeau | 38: [10, 10.0] | trudeau justin canada | Justin_Trudeau |
| 146. | address | 38: [10, 10.0] | address canada nations | First_Nations |
| 147. | yemen | 41: [10, 10.0] | yemen coalition saudi-led | Saudi_Arabian-led_intervention_in_Yemen |
| 148. | even | 41: [10, 10.0] | even president government | President_(government_title) |
| 149. | life | 46: [10, 10.0] | life sentence china | Life_imprisonment |
| 150. | security | 51: [10, 10.0] | security united forces | United_States_Air_Force_Security_Forces |
| 151. | brussels | 12: [69, 9.86] | brussels attacks airport | 2016_Brussels_bombings |
| 152. | mosul | 42: [18, 9.0] | mosul iraq isis | Mosul |
| 153. | party | 13: [17, 8.5] | party leader president | Party_leaders_of_the_United_States_Senate |
| 154. | european | 22: [10, 5.0], 44: [17, 8.5] | european union britain | Brexit |
| 155. | iran | 1: [15, 7.5], 16: [16, 8.0] | iran president u.s. | United_States_sanctions_against_Iran |
| 156. | government | 1: [15, 7.5], 48: [24, 8.0] | government president minister | Minister-president |
| 157. | airport | 12: [16, 8.0] | airport brussels attacks | 2016_Brussels_bombings |
| 158. | christmas | 51: [23, 7.67] | christmas berlin attack | 2016_Berlin_truck_attack |
| 159. | erdogan | 28: [15, 7.5] | erdogan turkey president | Recep_Tayyip_Erdoğan |
| 160. | attack | 26: [22, 7.33], 28: [26, 6.5] | attack killed police | 2016_shooting_of_Dallas_police_officers |
| 161. | authorities | 4: [12, 6.0], 12: [14, 7.0] | authorities killed attack | 2020_Vienna_attack |
| 162. | since | 9: [14, 7.0] | since first president | George_Washington |
| 163. | air | 44: [14, 7.0] | air base force | Dyess_Air_Force_Base |
| 164. | officers | 51: [14, 7.0] | officers police killed | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 165. | military | 5: [13, 6.5], 28: [19, 6.33], 41: [10, 5.0] | military u.s. syria | American-led_intervention_in_the_Syrian_Civil_War |
| 166. | economic | 19: [13, 6.5] | economic china president | China–Pakistan_Economic_Corridor |
| 167. | june | 22: [13, 6.5] | june archives international | Archive |
| 168. | years | 30: [13, 6.5], 48: [13, 6.5] | years two president | List_of_presidents_of_the_United_States_by_time_in_office |
| 169. | american | 2: [19, 6.33], 30: [10, 5.0] | american u.s. president | List_of_presidents_of_the_United_States |
| 170. | many | 1: [12, 6.0], 26: [12, 6.0] | many people president | President_of_the_United_States |
| 171. | president | 1: [12, 6.0] | president obama china | Barack_Obama |
| 172. | duterte | 19: [12, 6.0] | duterte rodrigo president | Rodrigo_Duterte |
| 173. | campaign | 24: [12, 6.0] | campaign president trump | Donald_Trump |
| 174. | bank | 25: [12, 6.0] | bank west palestinian | Palestinian_territories |
| 175. | hurricane | 40: [12, 6.0] | hurricane matthew haiti | Hurricane_Matthew |
| 176. | visit | 49: [12, 6.0] | visit president obama | Barack_Obama |
| 177. | renzi | 49: [12, 6.0] | renzi italy matteo | Matteo_Renzi |
| 178. | prime | 49: [28, 5.6] | prime minister britain | Prime_Minister_of_the_United_Kingdom |
| 179. | video | 5: [11, 5.5] | video footage chinese | Stock_footage |
| 180. | aleppo | 17: [11, 5.5], 49: [15, 5.0] | aleppo syria city | Aleppo |
| 181. | dilma | 19: [11, 5.5] | dilma rousseff brazil | Impeachment_of_Dilma_Rousseff |
| 182. | whether | 22: [11, 5.5] | whether european union | European_Union |
| 183. | india | 22: [11, 5.5] | india pakistan modi | 2014_India–Pakistan_floods |
| 184. | nations | 28: [11, 5.5] | nations united u.n. | Headquarters_of_the_United_Nations |
| 185. | first | 44: [11, 5.5], 51: [11, 5.5] | first leader president | Party_leaders_of_the_United_States_Senate |
| 186. | year | 44: [11, 5.5] | year last china | Chinese_New_Year |
| 187. | residents | 49: [11, 5.5] | residents city town | List_of_cities_and_towns_in_Romania |
| 188. | people | 15: [27, 5.4] | people killed least | List_of_people_killed_for_being_transgender |
| 189. | mr. | 3: [16, 5.33] | mr. trump president | Donald_Trump |
| 190. | german | 15: [16, 5.33] | german international archives | International_Council_on_Archives |
| 191. | saudi | 1: [25, 5.0] | saudi arabia iran | Iran–Saudi_Arabia_relations |
| 192. | arabia | 1: [20, 5.0] | arabia saudi iran | Iran–Saudi_Arabia_relations |
| 193. | says | 1: [10, 5.0] | says president south | President_of_South_Africa |
| 194. | pakistan | 2: [10, 5.0], 21: [10, 5.0] | pakistan india attack | India–Pakistan_relations |
| 195. | arrest | 2: [10, 5.0] | arrest arrested iran | House_arrest |
| 196. | civil | 4: [10, 5.0] | civil syria rights | Syrian_civil_war |
| 197. | time | 4: [10, 5.0] | time first president | President_of_East_Timor |
| 198. | part | 9: [15, 5.0] | part china president | President_of_the_Republic_of_China |
| 199. | south | 10: [20, 5.0] | south korea china | China–South_Korea_relations |
| 200. | palestinian | 10: [10, 5.0] | palestinian israeli israel | Israeli–Palestinian_conflict |
| 201. | victim | 12: [10, 5.0] | victim death brussels | 2016_Brussels_bombings |
| 202. | refugees | 13: [10, 5.0] | refugees syrian migrants | Refugees_of_the_Syrian_Civil_War |
| 203. | deal | 16: [10, 5.0] | deal iran president | Joint_Comprehensive_Plan_of_Action |
| 204. | day | 17: [10, 5.0], 28: [10, 5.0] | day president people | Not_My_Presidents_Day |
| 205. | impeachment | 19: [10, 5.0] | impeachment president rousseff | Impeachment_of_Dilma_Rousseff |
| 206. | jews | 19: [10, 5.0] | jews israel jewish | Israeli_Jews |
| 207. | japan | 21: [10, 5.0] | japan president abe | Shinzo_Abe |
| 208. | found | 24: [10, 5.0] | found police says | Shooting_of_Jacob_Blake |
| 209. | sentenced | 24: [10, 5.0] | sentenced years prison | List_of_longest_prison_sentences |
| 210. | convicted | 24: [10, 5.0] | convicted prison years | List_of_American_federal_politicians_convicted_of_crimes |
| 211. | human | 26: [10, 5.0] | human rights u.n. | United_Nations_Human_Rights_Council |
| 212. | seek | 26: [10, 5.0] | seek president leader | Party_leaders_of_the_United_States_House_of_Representatives |
| 213. | europe | 30: [10, 5.0] | europe migrants european | European_migrant_crisis |
| 214. | rio | 32: [10, 5.0] | rio olympics brazil | 2016_Summer_Olympics |
| 215. | philippines | 36: [10, 5.0] | philippines duterte rodrigo | Sara_Duterte |
| 216. | may | 37: [10, 5.0] | may president china | President_of_the_Republic_of_China |
| 217. | leave | 43: [10, 5.0] | leave britain european | Vote_Leave |
| 218. | dead | 44: [10, 5.0] | dead killed police | List_of_British_police_officers_killed_in_the_line_of_duty |
| 219. | detained | 46: [10, 5.0] | detained china rights | LGBT_rights_in_China |
| 220. | call | 48: [10, 5.0] | call president trump | Donald_Trump |
| 221. | tunisian | 51: [10, 5.0] | tunisian berlin attack | 2016_Berlin_truck_attack |
| 222. | suspect | 51: [10, 5.0] | suspect police brussels | 2016_Brussels_police_raids |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | test | 1: [14, inf] | test north korea | List_of_North_Korean_missile_tests |
| 2. | north | 1: [16, inf] | north korea nuclear | North_Korea_and_weapons_of_mass_destruction |
| 3. | korea | 1: [14, inf] | korea north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 4. | nuclear | 1: [14, inf] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 5. | chapo | 1: [11, inf] | chapo 's mexico | Joaquín_"El_Chapo"_Guzmán |
| 6. | easter | 12: [11, inf] | easter rising irish | Easter_Rising |
| 7. | egyptair | 20: [15, inf] | egyptair flight ms | EgyptAir_Flight_804 |
| 8. | ms | 20: [13, inf] | ms egyptair flight | EgyptAir_Flight_648 |
| 9. | truck | 28: [11, inf] | truck nice attack | 2016_Nice_truck_attack |
| 10. | nice | 28: [27, inf] | nice attack truck | 2016_Nice_truck_attack |
| 11. | turkey | 28: [20, inf] | turkey 's coup | 2016_Turkish_coup_d'état_attempt |
| 12. | munich | 29: [13, inf] | munich 's attack | Munich_massacre |
| 13. | italy | 34: [12, inf] | italy 's earthquake | List_of_earthquakes_in_Italy |
| 14. | earthquake | 34: [14, inf] | earthquake italy zealand | August_2016_Central_Italy_earthquake |
| 15. | hurricane | 40: [10, inf] | hurricane matthew haiti | Hurricane_Matthew |
| 16. | matthew | 40: [11, inf] | matthew hurricane haiti | Effects_of_Hurricane_Matthew_in_Haiti |
| 17. | trump | 45: [13, inf] | trump 's donald | Donald_Trump |
| 18. | castro | 47: [22, inf] | castro fidel 's | Fidel_Castro |
| 19. | fidel | 47: [15, inf] | fidel castro 's | Fidel_Castro |
| 20. | chapecoense | 48: [11, inf] | chapecoense plane crash | LaMia_Flight_2933 |
| 21. | plane | 48: [14, inf] | plane crash mh | Aviation_accidents_and_incidents |
| 22. | berlin | 51: [23, inf] | berlin attack suspect | 2016_Berlin_truck_attack |
| 23. | brussels | 12: [48, 24.0] | brussels attacks attack | 2016_Brussels_bombings |
| 24. | coup | 28: [18, 18.0] | coup turkey attempt | 2016_Turkish_coup_d'état_attempt |
| 25. | litvinenko | 3: [14, 14.0] | litvinenko alexander murder | Poisoning_of_Alexander_Litvinenko |
| 26. | attack | 28: [23, 5.75], 51: [22, 11.0] | attack police nice | 2016_Nice_truck_attack |
| 27. | arabia | 1: [10, 10.0] | arabia saudi iran | Iran–Saudi_Arabia_relations |
| 28. | says | 1: [10, 10.0] | says 's us | Say's_law |
| 29. | brazil | 11: [10, 10.0] | brazil 's rousseff | Impeachment_of_Dilma_Rousseff |
| 30. | burkini | 34: [10, 10.0] | burkini ban french | Burkini |
| 31. | crash | 48: [10, 10.0] | crash plane killed | Lynyrd_Skynyrd_plane_crash |
| 32. | market | 51: [10, 10.0] | market attack berlin | 2016_Berlin_truck_attack |
| 33. | mosul | 42: [14, 7.0] | mosul isis iraqi | Mosul |
| 34. | flight | 20: [13, 6.5] | flight egyptair ms | EgyptAir_Flight_648 |
| 35. | zika | 4: [12, 6.0] | zika virus 's | Zika_virus |
| 36. | china | 7: [12, 6.0] | china 's south | South_China_Sea |
| 37. | iran | 1: [10, 5.0], 8: [11, 5.5] | iran 's saudi | Iran–Saudi_Arabia_relations |
| 38. | police | 1: [11, 5.5] | police 's attack | 2016_shooting_of_Dallas_police_officers |
| 39. | isis | 10: [11, 5.5] | isis syria mosul | Mosul |
| 40. | cuba | 12: [11, 5.5] | cuba obama 's | Cuba–United_States_relations |
| 41. | zealand | 46: [11, 5.5] | zealand 's police | New_Zealand_Police |
| 42. | virus | 4: [10, 5.0] | virus zika 's | Zika_virus |
| 43. | – | 28: [10, 5.0] | – 's us | Us |
| 44. | ireland | 42: [10, 5.0] | ireland northern abortion | Abortion_in_the_United_Kingdom |
