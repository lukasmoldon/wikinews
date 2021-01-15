# Keywords with the highest 'interestingness' in 2008

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
| 1. | israel | 2: [15, 5.0], 14: [18, inf] | israel gaza israeli | Gaza–Israel_conflict |
| 2. | official | 2: [12, inf] | official u.s. president | List_of_presidents_of_the_United_States |
| 3. | suharto | 2: [11, inf] | suharto former president | Suharto |
| 4. | former | 2: [16, inf], 35: [12, 6.0] | former president minister | List_of_presidents_of_India |
| 5. | bush | 2: [25, 5.0], 7: [10, inf], 14: [15, 5.0], 20: [10, inf] | bush president iraq | George_W._Bush |
| 6. | pakistani | 3: [11, inf] | pakistani pakistan taliban | Tehrik-i-Taliban_Pakistan |
| 7. | shiite | 3: [10, inf] | shiite iraq iraqi | Sons_of_Iraq |
| 8. | israeli | 5: [11, inf] | israeli gaza israel | Gaza–Israel_conflict |
| 9. | rocket | 6: [12, inf] | rocket gaza israeli | Gaza_War_(2008–2009) |
| 10. | party | 6: [11, 11.0], 37: [11, inf], 43: [11, 11.0], 47: [18, 18.0] | party leader opposition | Leader_of_the_Opposition_(India) |
| 11. | bhutto | 6: [15, inf] | bhutto pakistan benazir | Nusrat_Bhutto |
| 12. | east | 7: [17, inf] | east middle timor | Middle_East |
| 13. | timor | 7: [14, inf] | timor east president | President_of_East_Timor |
| 14. | australia | 7: [12, inf] | australia australian pope | Lloyd_Pope |
| 15. | hezbollah | 7: [10, inf], 19: [11, inf] | hezbollah israel lebanon | 2006_Lebanon_War |
| 16. | fidel | 8: [12, inf] | fidel castro cuba | Cuba_under_Fidel_Castro |
| 17. | castro | 8: [19, inf] | castro cuba raúl | Raúl_Castro |
| 18. | serbia | 8: [10, inf] | serbia kosovo serbian | Kosovo–Serbia_relations |
| 19. | would | 8: [11, inf], 42: [27, 5.4] | would president u.s. | President_of_the_United_States |
| 20. | militants | 8: [11, inf] | militants pakistan pakistani | Pakistan |
| 21. | bureau | 9: [11, inf] | bureau baghdad iraq | Iraq_War |
| 22. | london | 9: [11, inf] | london britain north | London |
| 23. | ecuador | 10: [10, inf] | ecuador colombia american | 1906_Ecuador–Colombia_earthquake |
| 24. | soldiers | 11: [13, inf], 34: [10, 5.0] | soldiers u.s. killed | June_2006_abduction_of_United_States_soldiers_in_Iraq |
| 25. | story | 12: [11, inf] | story f – | The_Short_Stories_of_F._Scott_Fitzgerald |
| 26. | opposition | 14: [16, 5.33], 23: [10, 5.0], 33: [12, inf] | opposition zimbabwe president | President_of_Zimbabwe |
| 27. | bahrain | 14: [11, inf] | bahrain race tomorrow | 2008_Bahrain_Grand_Prix |
| 28. | gaza | 14: [10, inf], 23: [10, 10.0] | gaza israel israeli | Gaza–Israel_conflict |
| 29. | – | 17: [12, inf], 31: [10, 5.0] | – f race | F1_Race |
| 30. | children | 18: [13, inf] | children killed parents | Goebbels_children |
| 31. | hong | 18: [14, inf] | hong kong china | Hong_Kong |
| 32. | kong | 18: [14, inf] | kong hong china | Hong_Kong |
| 33. | myanmar | 19: [18, inf] | myanmar aid cyclone | Cyclone_Nargis |
| 34. | earthquake | 20: [30, inf] | earthquake china quake | 2008_Sichuan_earthquake |
| 35. | monaco | 21: [15, inf] | monaco race track | Race_track |
| 36. | top | 21: [10, inf], 24: [10, 10.0] | top official iraq | Iraq |
| 37. | embassy | 23: [10, inf] | embassy u.s. attack | Attack_on_the_United_States_embassy_in_Baghdad |
| 38. | arrested | 23: [10, inf] | arrested police attack | 2008_Mumbai_attacks |
| 39. | track | 23: [12, inf] | track – race | Race_track |
| 40. | beef | 24: [10, inf] | beef south korea | 2008_US_beef_protest_in_South_Korea |
| 41. | deal | 24: [10, inf] | deal u.s. iraq | Assassination_of_Qasem_Soleimani |
| 42. | mans | 24: [14, inf] | mans – race | 24_Hours_of_Le_Mans |
| 43. | lebanon | 25: [10, inf] | lebanon hezbollah israel | 2006_Lebanon_War |
| 44. | oil | 25: [13, inf], 44: [12, 6.0] | oil iraq deal | Iraq_War |
| 45. | ferry | 26: [10, inf] | ferry capsized philippine | MV_Princess_of_the_Stars |
| 46. | diplomatic | 29: [11, inf] | diplomatic u.s. president | President_of_the_United_States |
| 47. | paddock | 29: [12, inf] | paddock poker media | Stephen_Paddock |
| 48. | pope | 29: [12, inf] | pope benedict xvi | Pope_Benedict_XVI |
| 49. | karadzic | 30: [18, inf] | karadzic radovan arrest | Radovan_Karadžić |
| 50. | radovan | 30: [13, inf] | radovan karadzic crimes | Radovan_Karadžić |
| 51. | cambodia | 30: [10, inf] | cambodia thailand dispute | Cambodian–Thai_border_dispute |
| 52. | months | 31: [11, inf] | months two three | 3_Years,_5_Months_and_2_Days_in_the_Life_Of... |
| 53. | heikki | 31: [10, inf] | heikki kovalainen hamilton | Heikki_Kovalainen |
| 54. | solzhenitsyn | 32: [12, inf] | solzhenitsyn aleksandr russia | Aleksandr_Solzhenitsyn |
| 55. | kirkuk | 34: [18, inf] | kirkuk iraq city | Kirkuk |
| 56. | parliament | 35: [10, inf], 41: [13, inf], 47: [11, inf] | parliament president minister | Minister-president |
| 57. | say | 35: [10, 5.0], 42: [10, inf] | say officials u.s. | Threatening_government_officials_of_the_United_States |
| 58. | european | 36: [10, inf] | european union europe | European_Union |
| 59. | court | 37: [10, inf] | court ruling case | Lists_of_United_States_Supreme_Court_cases |
| 60. | troops | 37: [16, inf] | troops iraq iraqi | Iraq_War |
| 61. | leave | 37: [10, inf] | leave iraq u.s. | Iraq_War |
| 62. | sent | 37: [11, inf] | sent letter u.s. | Bixby_letter |
| 63. | engine | 38: [14, inf] | engine rules freeze | Honda_Indy_V8_engine |
| 64. | food | 38: [10, inf] | food china prices | Food_prices |
| 65. | women | 38: [10, inf] | women iraqi iraq | Women_in_Iraq |
| 66. | second | 41: [14, inf], 44: [11, inf] | second time – | Not_a_Second_Time |
| 67. | policy | 42: [10, inf] | policy u.s. president | Historical_rankings_of_presidents_of_the_United_States |
| 68. | plan | 42: [10, inf] | plan u.s. would | Operation_Northwoods |
| 69. | reform | 42: [10, inf] | reform rural president | Land_reform_in_the_Philippines |
| 70. | somalia | 44: [10, inf] | somalia government islamist | Somali_Civil_War_(2009–present) |
| 71. | missile | 45: [14, inf] | missile u.s. russia | Russia–United_States_relations |
| 72. | victory | 45: [11, inf] | victory president election | 2008_United_States_presidential_election |
| 73. | obama | 45: [10, inf] | obama barack president | Barack_Obama |
| 74. | mumbai | 48: [15, inf] | mumbai attacks india | 2008_Mumbai_attacks |
| 75. | meeting | 50: [12, inf] | meeting leaders president | Asia-Pacific_Economic_Cooperation |
| 76. | climate | 50: [10, inf] | climate treaty change | Climate_change |
| 77. | university | 51: [10, inf] | university baghdad bureau | Baghdad_Pact |
| 78. | family | 51: [10, inf] | family iraqi house | List_of_kings_of_Iraq |
| 79. | iran | 2: [22, 22.0], 15: [13, 13.0], 17: [14, 7.0] | iran nuclear president | Nuclear_program_of_Iran |
| 80. | attacks | 15: [12, 6.0], 44: [12, 12.0], 48: [20, 20.0] | attacks killed mumbai | 2008_Mumbai_attacks |
| 81. | north | 9: [18, 18.0], 26: [13, 6.5], 36: [11, 11.0], 40: [14, 7.0] | north korea nuclear | North_Korea_and_weapons_of_mass_destruction |
| 82. | killed | 18: [17, 17.0] | killed people attack | Crocodile_attack |
| 83. | christmas | 52: [17, 17.0] | christmas pope peace | Let_There_Be_Peace_on_Earth_(song) |
| 84. | aid | 19: [16, 16.0], 36: [20, 5.0] | aid myanmar u.s. | Myanmar |
| 85. | debate | 37: [16, 16.0] | debate iraq troop | Iraq_War_troop_surge_of_2007 |
| 86. | security | 2: [11, 11.0], 24: [11, 5.5], 31: [15, 15.0], 47: [21, 5.25] | security iraq iraqi | Iraqi_Kurdistan |
| 87. | rice | 10: [10, 5.0], 17: [14, 14.0] | rice state condoleezza | Condoleezza_Rice |
| 88. | troop | 37: [14, 14.0] | troop iraq would | Iraq_War_troop_surge_of_2007 |
| 89. | bombings | 38: [14, 14.0] | bombings killed baghdad | October_2009_Baghdad_bombings |
| 90. | plot | 7: [12, 12.0] | plot police coup | List_of_coups_and_coup_attempts |
| 91. | thursday | 7: [12, 12.0] | thursday iraq president | Iraq_War |
| 92. | f | 10: [11, 11.0], 31: [12, 12.0] | f – formula | Formula_One |
| 93. | sunday | 10: [12, 12.0] | sunday officials killed | Bloody_Sunday_(1972) |
| 94. | hussein | 12: [12, 12.0] | hussein iraq saddam | Saddam's_family |
| 95. | results | 16: [12, 12.0] | results election opposition | Results_of_the_2019_Indian_general_election |
| 96. | taliban | 25: [15, 5.0], 29: [12, 12.0] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 97. | case | 29: [12, 12.0] | case court years | Supreme_Court_of_the_United_States |
| 98. | car | 39: [12, 12.0] | car bomb killed | Car_bomb |
| 99. | thai | 48: [12, 12.0] | thai protesters prime | 2020_Thai_protests |
| 100. | two | 16: [23, 11.5] | two killed police | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 101. | coalition | 10: [11, 11.0] | coalition government minister | Coalition_government |
| 102. | time | 12: [11, 11.0] | time first two | Time_zone |
| 103. | zimbabwe | 14: [17, 8.5], 33: [11, 11.0] | zimbabwe mugabe opposition | Robert_Mugabe |
| 104. | made | 20: [11, 11.0] | made president iraq | Rationale_for_the_Iraq_War |
| 105. | south | 24: [11, 11.0], 37: [10, 5.0], 44: [10, 5.0] | south korea korean | South_Korea |
| 106. | europe | 24: [11, 11.0] | europe european union | European_Union |
| 107. | afghanistan | 34: [11, 11.0] | afghanistan taliban afghan | War_in_Afghanistan_(2001–present) |
| 108. | live | 44: [11, 11.0] | live blogging embed | Liveblogging |
| 109. | city | 44: [11, 11.0] | city sadr iraqi | Siege_of_Sadr_City |
| 110. | china | 5: [21, 10.5], 30: [10, 5.0] | china chinese dalai | 14th_Dalai_Lama |
| 111. | nato | 14: [21, 10.5], 38: [10, 5.0] | nato afghanistan russia | Russia–NATO_relations |
| 112. | peace | 2: [10, 10.0] | peace talks israel | 2013–2014_Israeli–Palestinian_peace_talks |
| 113. | palestinians | 2: [10, 10.0] | palestinians israel gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 114. | move | 6: [10, 10.0] | move president talks | Josh_Talks |
| 115. | colombia | 10: [16, 5.33], 27: [10, 10.0] | colombia colombian forces | Military_Forces_of_Colombia |
| 116. | dalai | 12: [20, 10.0] | dalai china tibet | Dalai_Lama |
| 117. | saddam | 12: [10, 10.0] | saddam hussein iraq | Saddam's_family |
| 118. | marine | 12: [10, 10.0] | marine iraqis rape | Greg_Kelly |
| 119. | bank | 14: [10, 10.0] | bank west israel | Israeli_West_Bank_barrier |
| 120. | palestinian | 14: [10, 10.0] | palestinian israeli israel | Israeli–Palestinian_conflict |
| 121. | last | 14: [10, 10.0], 25: [11, 5.5] | last week year | ISO_week_date |
| 122. | could | 19: [10, 10.0], 29: [10, 10.0] | could china government | Government_of_the_Republic_of_China |
| 123. | survivors | 20: [10, 10.0] | survivors earthquake still | 1908_Messina_earthquake |
| 124. | ruling | 21: [10, 10.0] | ruling party president | Ruling_party |
| 125. | three | 23: [10, 10.0] | three killed police | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 126. | video | 26: [10, 10.0] | video iraqi answers | Most-wanted_Iraqi_playing_cards |
| 127. | embed | 44: [10, 10.0] | embed live blogging | Liveblogging |
| 128. | many | 44: [10, 10.0] | many iraq people | Iraqis |
| 129. | french | 47: [10, 10.0] | french france president | President_of_France |
| 130. | human | 50: [10, 10.0] | human rights china | Human_rights_in_China |
| 131. | india | 48: [19, 9.5] | india pakistan attacks | 2008_Mumbai_attacks |
| 132. | gates | 38: [18, 9.0] | gates defense secretary | Robert_Gates |
| 133. | protesters | 48: [18, 9.0] | protesters thai police | 2020_Thai_protests |
| 134. | officials | 19: [16, 8.0] | officials u.s. killed | Disposition_Matrix |
| 135. | attack | 28: [16, 8.0] | attack killed police | 2016_shooting_of_Dallas_police_officers |
| 136. | military | 9: [12, 6.0], 43: [15, 7.5] | military u.s. iraq | Occupation_of_Iraq_(2003–2011) |
| 137. | leader | 9: [13, 6.5], 12: [11, 5.5], 47: [16, 5.33], 50: [15, 7.5] | leader president party | Party_leaders_of_the_United_States_Senate |
| 138. | kosovo | 8: [21, 7.0] | kosovo serbia independence | Kosovo–Serbia_relations |
| 139. | baghdad | 9: [19, 6.33], 24: [22, 5.5], 45: [14, 7.0] | baghdad iraq iraqi | Baghdad |
| 140. | korea | 38: [10, 5.0], 40: [14, 7.0] | korea north south | North_Korea–South_Korea_relations |
| 141. | election | 45: [14, 7.0] | election zimbabwe opposition | 2018_Zimbabwean_general_election |
| 142. | team | 2: [13, 6.5] | team race members | World's_Toughest_Race:_Eco-Challenge_Fiji |
| 143. | iraq | 2: [13, 6.5] | iraq iraqi u.s. | Occupation_of_Iraq_(2003–2011) |
| 144. | first | 17: [12, 6.0], 41: [13, 6.5] | first time since | First-person_shooter |
| 145. | united | 2: [12, 6.0] | united states nations | Member_states_of_the_United_Nations |
| 146. | russia | 3: [10, 5.0], 32: [17, 5.67], 45: [12, 6.0] | russia georgia russian | Georgia–Russia_relations |
| 147. | taiwan | 12: [12, 6.0] | taiwan china president | President_of_the_Republic_of_China |
| 148. | putin | 16: [12, 6.0] | putin russia vladimir | Russia_under_Vladimir_Putin |
| 149. | kills | 24: [12, 6.0] | kills suicide bomb | Suicide_attack |
| 150. | talks | 25: [24, 6.0] | talks president peace | 2013–2014_Israeli–Palestinian_peace_talks |
| 151. | korean | 28: [12, 6.0] | korean north south | North_Korea–South_Korea_relations |
| 152. | u.s. | 43: [18, 6.0] | u.s. iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 153. | president | 2: [53, 5.3], 50: [17, 5.67] | president bush leader | George_H._W._Bush |
| 154. | chad | 6: [17, 5.67] | chad capital rebels | Chadian_Civil_War_(2005–2010) |
| 155. | mugabe | 14: [17, 5.67] | mugabe zimbabwe robert | Robert_Mugabe |
| 156. | leaders | 50: [17, 5.67] | leaders president political | Party_leaders_of_the_United_States_Senate |
| 157. | nuclear | 4: [10, 5.0], 39: [11, 5.5] | nuclear korea north | North_Korea_and_weapons_of_mass_destruction |
| 158. | police | 7: [11, 5.5] | police attack arrested | 2008_Mumbai_attacks |
| 159. | forces | 13: [11, 5.5] | forces iraqi u.s. | Iraqi_Armed_Forces |
| 160. | questions | 24: [11, 5.5] | questions baghdad iraq | Baghdad |
| 161. | arrest | 29: [11, 5.5] | arrest police leader | Police |
| 162. | russian | 33: [33, 5.5] | russian russia georgia | Georgia–Russia_relations |
| 163. | iraqis | 35: [11, 5.5] | iraqis iraqi u.s. | Iraqis |
| 164. | robert | 38: [11, 5.5] | robert mugabe zimbabwe | Robert_Mugabe |
| 165. | world | 39: [11, 5.5] | world president around | Around_the_world_(card_game) |
| 166. | recent | 40: [11, 5.5] | recent iraq attacks | Iran–Iraq_War |
| 167. | political | 3: [10, 5.0] | political president minister | Minister_President_of_Prussia |
| 168. | tuesday | 7: [10, 5.0] | tuesday north china | Super_Tuesday |
| 169. | crisis | 10: [10, 5.0] | crisis political country | Political_midlife_crisis |
| 170. | vote | 15: [10, 5.0] | vote president election | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 171. | calls | 15: [10, 5.0] | calls president security | Presidency_of_the_United_Nations_Security_Council |
| 172. | arms | 17: [10, 5.0] | arms u.s. nuclear | Nuclear_arms_race |
| 173. | chinese | 30: [10, 5.0] | chinese china officials | China |
| 174. | cheney | 36: [10, 5.0] | cheney dick georgia | Mary_Cheney |
| 175. | rural | 42: [10, 5.0] | rural china reform | China's_Rural_Reform |
| 176. | report | 47: [10, 5.0] | report says rights | Human_rights |
| 177. | elections | 48: [10, 5.0] | elections party government | One-party_state |
| 178. | airport | 48: [10, 5.0] | airport protesters heathrow | Heathrow_Airport |
| 179. | violence | 49: [10, 5.0] | violence kenya iraq | Communal_violence |
| 180. | support | 50: [10, 5.0] | support president u.s. | President_of_the_United_States |
| 181. | journalist | 51: [15, 5.0] | journalist iraqi trial | Trial_of_Saddam_Hussein |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | bush | 2: [10, inf] | bush george 's | George_H._W._Bush |
| 2. | basra | 13: [11, inf] | basra british battle | Battle_of_Basra_(2003) |
| 3. | quake | 20: [10, inf] | quake china shakes | 2008_Sichuan_earthquake |
| 4. | betancourt | 27: [13, inf] | betancourt ingrid hostage | Íngrid_Betancourt |
| 5. | radovan | 30: [13, inf] | radovan karadzic crimes | Trial_of_Radovan_Karadžić |
| 6. | karadzic | 30: [26, inf] | karadzic radovan crimes | Radovan_Karadžić |
| 7. | georgia | 32: [10, inf] | georgia russia russian | Georgia–Russia_relations |
| 8. | crash | 34: [10, inf] | crash plane madrid | Spanair_Flight_5022 |
| 9. | plane | 34: [11, inf] | plane crash madrid | Spanair_Flight_5022 |
| 10. | madrid | 34: [13, inf] | madrid crash plane | Spanair_Flight_5022 |
| 11. | congo | 44: [15, inf] | congo rebels 's | Simba_rebellion |
| 12. | reports | 45: [11, inf] | reports first world | First_World |
| 13. | mumbai | 48: [51, inf] | mumbai attacks terror | 2008_Mumbai_attacks |
| 14. | eyewitness | 52: [17, inf] | eyewitness burma account | Burmese_invasions_of_Assam |
| 15. | first | 45: [24, 24.0] | first world 's | First_World |
| 16. | thai | 48: [14, 14.0] | thai pm protesters | 2020_Thai_protests |
| 17. | nevada | 3: [13, 13.0] | nevada clinton south | 2016_Nevada_Democratic_presidential_caucuses_and_convention |
| 18. | aid | 19: [13, 13.0] | aid burma agencies | Cyclone_Nargis |
| 19. | burma | 19: [23, 11.5] | burma aid cyclone | Cyclone_Nargis |
| 20. | tibet | 11: [10, 10.0] | tibet china protest | 2008_Tibetan_unrest |
| 21. | zimbabwe | 23: [12, 6.0], 25: [12, 6.0], 37: [10, 10.0] | zimbabwe mugabe tsvangirai | Morgan_Tsvangirai |
| 22. | afghanistan | 34: [10, 10.0] | afghanistan killed british | British_Forces_casualties_in_Afghanistan_since_2001 |
| 23. | terror | 48: [20, 10.0] | terror mumbai attacks | 2008_Mumbai_attacks |
| 24. | death | 52: [10, 10.0] | death toll 's | List_of_wars_and_anthropogenic_disasters_by_death_toll |
| 25. | south | 32: [13, 6.5] | south africa ossetia | International_recognition_of_Abkhazia_and_South_Ossetia |
| 26. | treaty | 24: [12, 6.0] | treaty lisbon irish | Treaty_of_Lisbon |
| 27. | georgian | 33: [11, 5.5] | georgian russia russian | Russo-Georgian_War |
| 28. | gaza | 52: [16, 5.33] | gaza israel israeli | Gaza–Israel_conflict |
| 29. | israel | 10: [10, 5.0] | israel gaza 's | 2014_Gaza_War |
| 30. | mbeki | 38: [10, 5.0] | mbeki anc zimbabwe | Thabo_Mbeki |
