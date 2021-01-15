# Keywords with the highest 'interestingness' in 2017

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
| 1. | trump | 1: [17, inf], 44: [36, inf] | trump president u.s. | Donald_Trump |
| 2. | mr. | 1: [11, inf], 26: [16, inf] | mr. trump president | Donald_Trump |
| 3. | would | 1: [11, inf], 13: [11, 11.0], 48: [17, 8.5] | would trump president | Donald_Trump |
| 4. | police | 1: [10, inf] | police attack officers | 2016_shooting_of_Dallas_police_officers |
| 5. | video | 1: [11, inf], 31: [12, 6.0] | video shows china | Vídeo_Show |
| 6. | minister | 1: [10, 10.0], 10: [15, inf], 16: [12, 12.0] | minister prime may | Prime_minister |
| 7. | official | 1: [10, inf] | official u.s. trump | List_of_Republicans_who_opposed_the_Donald_Trump_2020_presidential_campaign |
| 8. | year | 1: [15, 5.0], 11: [17, inf] | year last trump | Donald_Trump_(Last_Week_Tonight) |
| 9. | trial | 1: [10, inf] | trial president park | Impeachment_of_Park_Geun-hye |
| 10. | government | 1: [15, inf], 19: [12, 6.0] | government president says | Government_of_Russia |
| 11. | taiwan | 2: [10, inf] | taiwan china president | President_of_the_Republic_of_China |
| 12. | court | 3: [20, 10.0], 13: [16, 8.0], 23: [10, inf], 25: [14, 14.0] | court supreme president | Supreme_Court_of_the_United_States |
| 13. | camp | 3: [11, inf] | camp refugee people | Refugee_camp |
| 14. | order | 4: [10, inf] | order trump president | Donald_Trump |
| 15. | house | 5: [10, inf], 20: [13, 6.5] | house white trump | White_House_COVID-19_outbreak |
| 16. | iran | 5: [19, 6.33], 18: [14, inf], 37: [12, 6.0], 45: [11, 5.5] | iran trump president | Donald_Trump |
| 17. | near | 5: [11, inf], 16: [10, inf] | near attack police | Murder_of_Lee_Rigby |
| 18. | russia | 7: [20, inf], 30: [17, 5.67] | russia president trump | Donald_Trump |
| 19. | nato | 7: [11, 5.5], 21: [11, inf] | nato trump allies | Major_non-NATO_ally |
| 20. | vice | 7: [14, inf] | vice president pence | Mike_Pence |
| 21. | called | 10: [10, inf], 29: [10, 5.0] | called president trump | Donald_Trump |
| 22. | prime | 10: [13, inf] | prime minister may | Prime_minister |
| 23. | talks | 13: [10, inf] | talks north korea | North_Korea–South_Korea_relations |
| 24. | four | 14: [10, inf] | four attack killed | American_fatalities_and_injuries_of_the_2012_Benghazi_attack |
| 25. | syria | 14: [44, inf], 25: [15, 5.0], 35: [11, 11.0] | syria syrian u.s. | Syria_(region) |
| 26. | chemical | 14: [26, inf] | chemical syria attack | Ghouta_chemical_attack |
| 27. | missile | 14: [14, inf], 35: [19, 6.33], 48: [10, 10.0] | missile north korea | List_of_North_Korean_missile_tests |
| 28. | bomb | 15: [11, 11.0], 35: [18, inf] | bomb attack north | Suicide_attack |
| 29. | election | 16: [21, 10.5], 23: [25, 5.0], 31: [10, inf], 35: [11, 5.5], 37: [10, 5.0], 41: [11, 5.5] | election president party | 1828_United_States_presidential_election |
| 30. | political | 16: [11, inf] | political president minister | Minister_President_of_Prussia |
| 31. | macron | 16: [12, inf], 28: [10, 5.0] | macron france emmanuel | Emmanuel_Macron |
| 32. | land | 16: [10, inf] | land canada many | Canadian_Army |
| 33. | base | 16: [10, inf] | base military afghan | Afghan_Armed_Forces |
| 34. | system | 17: [11, inf] | system korea south | Education_in_South_Korea |
| 35. | campaign | 18: [12, 6.0], 37: [10, inf], 44: [10, 10.0] | campaign president trump | Donald_Trump |
| 36. | moon | 19: [17, inf] | moon korea south | Moon_Jae-in |
| 37. | jae-in | 19: [14, inf] | jae-in korea south | Moon_Jae-in |
| 38. | says | 20: [20, inf] | says president trump | Donald_Trump |
| 39. | saudi | 20: [14, inf], 44: [10, 5.0] | saudi arabia prince | Crown_Prince_of_Saudi_Arabia |
| 40. | manchester | 21: [38, inf] | manchester attack bomber | Manchester_Arena_bombing |
| 41. | concert | 21: [13, inf] | concert manchester bombing | Manchester_Arena_bombing |
| 42. | bombing | 21: [18, inf] | bombing attack killed | Centennial_Olympic_Park_bombing |
| 43. | bomber | 21: [14, inf] | bomber suicide manchester | Manchester_Arena_bombing |
| 44. | allies | 21: [11, inf], 23: [11, inf] | allies trump president | Donald_Trump |
| 45. | trade | 22: [10, inf] | trade trump china | China–United_States_trade_war |
| 46. | kabul | 22: [14, inf] | kabul afghan attack | Kabul |
| 47. | qatar | 23: [15, inf] | qatar gulf arab | Gulf_Cooperation_Council |
| 48. | warmbier | 24: [11, inf] | warmbier north korea | Otto_Warmbier |
| 49. | fire | 24: [10, inf] | fire london grenfell | Grenfell_Tower_fire |
| 50. | tower | 24: [10, inf] | tower london fire | Grenfell_Tower_fire |
| 51. | spyware | 25: [10, inf] | spyware government mexican | Pegasus_(spyware) |
| 52. | south | 25: [13, inf] | south korea north | North_Korea–South_Korea_relations |
| 53. | day | 26: [11, inf] | day president trump | Donald_Trump |
| 54. | hong | 26: [15, inf] | hong kong china | Hong_Kong |
| 55. | kong | 26: [15, inf] | kong hong china | Hong_Kong |
| 56. | cardinal | 26: [11, inf] | cardinal pell pope | George_Pell |
| 57. | hospital | 27: [11, inf] | hospital oxygen attack | Oxygen_therapy |
| 58. | world | 27: [15, 7.5], 38: [13, inf] | world trump president | Donald_Trump |
| 59. | woman | 29: [10, inf] | woman police american | Joan_As_Police_Woman |
| 60. | sharif | 30: [14, inf] | sharif pakistan nawaz | Maryam_Nawaz |
| 61. | pakistan | 30: [12, inf] | pakistan sharif minister | Nawaz_Sharif |
| 62. | foreign | 31: [10, inf], 49: [12, inf] | foreign trump minister | Foreign_policy_of_the_Donald_Trump_administration |
| 63. | guam | 32: [14, inf] | guam north korea | Andersen_Air_Force_Base |
| 64. | spain | 33: [12, inf] | spain catalonia independence | Catalan_declaration_of_independence |
| 65. | investigators | 33: [10, inf] | investigators say u.n. | Special_Counsel_investigation_(2017–2019) |
| 66. | people | 33: [13, inf], 51: [20, 10.0] | people killed least | List_of_people_killed_for_being_transgender |
| 67. | singapore | 34: [12, inf] | singapore navy mccain | USS_John_S._McCain_(DDG-56) |
| 68. | diana | 35: [13, inf] | diana death princess | Death_of_Diana,_Princess_of_Wales |
| 69. | hydrogen | 35: [10, inf] | hydrogen bomb north | Thermonuclear_weapon |
| 70. | next | 36: [13, inf], 50: [10, 5.0] | next president trump | Donald_Trump |
| 71. | hurricane | 36: [20, inf] | hurricane storm caribbean | Hurricane_Eta |
| 72. | irma | 36: [11, inf] | irma hurricane caribbean | Hurricane_Irma |
| 73. | national | 37: [11, inf], 40: [11, inf] | national party president | List_of_presidents_of_the_Bharatiya_Janata_Party |
| 74. | quake | 38: [14, inf] | quake mexico earthquake | 2017_Puebla_earthquake |
| 75. | deal | 40: [10, inf], 48: [10, 5.0] | deal trump iran | United_States_withdrawal_from_the_Joint_Comprehensive_Plan_of_Action |
| 76. | journalist | 40: [11, inf] | journalist wall killing | Murder_of_Kim_Wall |
| 77. | state | 42: [12, inf] | state islamic isis | Islamic_State_of_Iraq_and_the_Levant |
| 78. | isis | 42: [16, inf] | isis state islamic | Islamic_State_of_Iraq_and_the_Levant |
| 79. | mattis | 43: [10, inf] | mattis defense secretary | Jim_Mattis |
| 80. | decision | 49: [16, inf] | decision court president | Supreme_Court_of_the_United_States |
| 81. | african | 50: [10, inf] | african migrants south | Migrants'_African_routes |
| 82. | christmas | 51: [11, inf] | christmas queen day | Royal_Christmas_Message |
| 83. | fujimori | 52: [10, inf] | fujimori peru president | Alberto_Fujimori |
| 84. | star | 52: [10, inf] | star party mr. | Jeffree_Star |
| 85. | korean | 15: [10, 5.0], 46: [20, 20.0], 49: [11, 5.5] | korean north south | North_Korea–South_Korea_relations |
| 86. | president | 1: [19, 19.0] | president trump korea | Donald_Trump |
| 87. | jerusalem | 49: [34, 17.0] | jerusalem trump israel | United_States_recognition_of_Jerusalem_as_capital_of_Israel |
| 88. | power | 13: [16, 16.0] | power president china | President_of_the_Republic_of_China |
| 89. | xi | 14: [16, 16.0] | xi china jinping | Xi_Jinping_Thought |
| 90. | britain | 21: [16, 16.0] | britain brexit european | Brexit |
| 91. | european | 2: [10, 5.0], 17: [15, 15.0], 25: [11, 11.0] | european union britain | Brexit |
| 92. | say | 1: [12, 12.0], 4: [15, 7.5], 42: [14, 14.0] | say officials police | SayHerName |
| 93. | school | 12: [14, 14.0] | school children high | High_School_Musical |
| 94. | killing | 15: [10, 5.0], 42: [14, 14.0] | killing police least | Killing_of_George_Floyd |
| 95. | parliament | 23: [14, 14.0] | parliament european lawmakers | Political_groups_of_the_European_Parliament |
| 96. | visit | 27: [14, 14.0] | visit trump president | Donald_Trump |
| 97. | robert | 46: [14, 14.0] | robert mugabe zimbabwe | Robert_Mugabe |
| 98. | mexico | 4: [13, 13.0], 51: [10, 10.0] | mexico trump president | Donald_Trump |
| 99. | help | 20: [13, 13.0] | help trump president | Donald_Trump |
| 100. | islamic | 29: [13, 13.0] | islamic state isis | Islamic_State_of_Iraq_and_the_Levant |
| 101. | party | 38: [20, 10.0], 46: [13, 13.0] | party leader election | Leader_of_the_Labour_Party_(UK) |
| 102. | prince | 48: [13, 13.0] | prince saudi crown | Crown_Prince_of_Saudi_Arabia |
| 103. | nuclear | 10: [12, 12.0], 40: [16, 5.33] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 104. | independence | 11: [12, 12.0] | independence catalonia vote | Catalan_independence_movement |
| 105. | protests | 13: [12, 12.0] | protests president russia | 2011–2013_Russian_protests |
| 106. | died | 16: [12, 12.0] | died people officials | List_of_people_who_died_in_traffic_collisions |
| 107. | presidential | 16: [12, 12.0] | presidential election french | 2022_French_presidential_election |
| 108. | afghan | 20: [12, 12.0], 51: [10, 5.0] | afghan taliban afghanistan | Taliban |
| 109. | militants | 21: [11, 11.0], 35: [10, 5.0], 42: [12, 12.0] | militants killed islamic | Islamic_State_of_Iraq_and_the_Levant_–_Khorasan_Province |
| 110. | japan | 35: [12, 12.0] | japan korea north | Japan–North_Korea_relations |
| 111. | home | 4: [11, 11.0] | home president return | Vice_President_of_the_United_States |
| 112. | settlement | 5: [11, 11.0] | settlement israel trump | Trump_Heights |
| 113. | north | 7: [20, 10.0], 14: [20, 6.67], 29: [22, 5.5], 43: [11, 11.0] | north korea korean | North_Korea |
| 114. | korea | 7: [11, 11.0], 29: [15, 7.5] | korea north south | North_Korea–South_Korea_relations |
| 115. | union | 17: [11, 11.0] | union european britain | Brexit |
| 116. | vote | 23: [11, 11.0] | vote election president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 117. | india | 30: [11, 11.0] | india modi china | List_of_international_prime_ministerial_trips_made_by_Narendra_Modi |
| 118. | opposition | 31: [11, 11.0] | opposition leader president | Leader_of_the_Opposition_(India) |
| 119. | francis | 36: [10, 5.0], 48: [11, 11.0] | francis pope rohingya | Pope_Francis |
| 120. | british | 46: [11, 11.0] | british brexit may | Brexit |
| 121. | attack | 14: [43, 10.75] | attack killed police | 2016_shooting_of_Dallas_police_officers |
| 122. | city | 1: [10, 10.0] | city state isis | Islamic_State_of_Iraq_and_the_Levant |
| 123. | test | 7: [10, 10.0], 35: [15, 5.0] | test north missile | List_of_North_Korean_missile_tests |
| 124. | europe | 7: [10, 10.0] | europe trump president | Donald_Trump |
| 125. | strike | 14: [20, 10.0] | strike u.s. syria | 2018_missile_strikes_against_Syria |
| 126. | tillerson | 15: [10, 5.0], 43: [10, 10.0] | tillerson state secretary | Rex_Tillerson |
| 127. | members | 21: [10, 10.0] | members group trump | Second_impeachment_of_Donald_Trump |
| 128. | border | 29: [10, 10.0] | border north military | Military_Demarcation_Line |
| 129. | storm | 36: [10, 10.0] | storm hurricane caribbean | Hurricane_Eta |
| 130. | elections | 43: [10, 10.0] | elections president party | 2002_United_States_House_of_Representatives_elections |
| 131. | law | 50: [10, 10.0] | law rights government | Canadian_Charter_of_Rights_and_Freedoms |
| 132. | pope | 36: [14, 7.0], 48: [18, 9.0] | pope francis vatican | Pope_Francis |
| 133. | violence | 33: [16, 8.0] | violence myanmar people | Persecution_of_Muslims_in_Myanmar |
| 134. | meeting | 27: [22, 7.33] | meeting trump president | Donald_Trump |
| 135. | zimbabwe | 46: [22, 7.33] | zimbabwe mugabe president | Robert_Mugabe |
| 136. | voters | 18: [14, 7.0] | voters election party | Voter_turnout_in_United_States_presidential_elections |
| 137. | years | 19: [14, 7.0] | years president ago | Vice_President_of_the_United_States |
| 138. | first | 4: [15, 5.0], 18: [12, 6.0], 48: [13, 6.5] | first trump president | Donald_Trump |
| 139. | leaders | 5: [13, 6.5], 27: [10, 5.0] | leaders trump president | Donald_Trump |
| 140. | military | 46: [13, 6.5] | military u.s. north | United_States_Armed_Forces |
| 141. | mugabe | 46: [25, 6.25] | mugabe zimbabwe president | Robert_Mugabe |
| 142. | two | 11: [12, 6.0], 17: [18, 6.0], 23: [18, 6.0], 33: [16, 5.33] | two killed trump | Donald_Trump |
| 143. | last | 11: [12, 6.0] | last year week | ISO_week_date |
| 144. | report | 11: [12, 6.0] | report says u.n. | Woodbury_matrix_identity |
| 145. | emmanuel | 18: [24, 6.0] | emmanuel macron france | Emmanuel_Macron |
| 146. | rights | 39: [12, 6.0] | rights human u.n. | United_Nations_Human_Rights_Council |
| 147. | puigdemont | 44: [12, 6.0] | puigdemont carles catalonia | Carles_Puigdemont |
| 148. | officials | 15: [17, 5.67] | officials say u.s. | Utah_Data_Center |
| 149. | referendum | 39: [17, 5.67] | referendum independence vote | 2014_Scottish_independence_referendum |
| 150. | may | 3: [11, 5.5] | may theresa minister | Theresa_May |
| 151. | group | 6: [11, 5.5], 14: [11, 5.5] | group president militant | Lehi_(militant_group) |
| 152. | secretary | 7: [11, 5.5], 43: [10, 5.0] | secretary state tillerson | Rex_Tillerson |
| 153. | united | 43: [11, 5.5] | united states nations | Member_states_of_the_United_Nations |
| 154. | crisis | 43: [11, 5.5] | crisis president trump | Donald_Trump |
| 155. | life | 48: [11, 5.5] | life death president | President_for_life |
| 156. | news | 52: [11, 5.5] | news trump media | Donald_Trump_on_social_media |
| 157. | killed | 5: [16, 5.33] | killed people attack | Crocodile_attack |
| 158. | american | 23: [16, 5.33] | american u.s. trump | Presidency_of_Donald_Trump |
| 159. | could | 9: [10, 5.0], 28: [15, 5.0] | could president trump | Donald_Trump |
| 160. | nations | 11: [10, 5.0] | nations united u.n. | Headquarters_of_the_United_Nations |
| 161. | scandal | 12: [10, 5.0] | scandal president south | 2016_South_Korean_political_scandal |
| 162. | london | 12: [10, 5.0] | london attack police | 2017_Westminster_attack |
| 163. | security | 16: [10, 5.0] | security forces council | United_States_National_Security_Council |
| 164. | leader | 16: [10, 5.0], 36: [20, 5.0] | leader president trump | Donald_Trump |
| 165. | australia | 22: [10, 5.0] | australia australian day | Australia_Day |
| 166. | china | 41: [10, 5.0] | china president trump | Donald_Trump |
| 167. | million | 43: [10, 5.0] | million people president | Million_People_March |
| 168. | lawmakers | 43: [10, 5.0] | lawmakers parliament president | Parliament_of_Uganda |
| 169. | health | 44: [10, 5.0] | health canada people | Health_Canada |
| 170. | rebels | 51: [10, 5.0] | rebels yemen military | Saudi_Arabian-led_intervention_in_Yemen |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | terror | 33: [11, inf] | terror attack attacks | 2008_Mumbai_attacks |
| 2. | irma | 36: [27, inf] | irma hurricane caribbean | Hurricane_Irma |
| 3. | maria | 38: [12, inf] | maria hurricane puerto | Hurricane_Maria |
| 4. | zimbabwe | 46: [14, inf] | zimbabwe mugabe 's | Robert_Mugabe |
| 5. | syria | 14: [25, 25.0] | syria us 's | American-led_intervention_in_the_Syrian_Civil_War |
| 6. | barcelona | 33: [18, 18.0] | barcelona attack terror | 2017_Barcelona_attacks |
| 7. | attack | 14: [16, 16.0], 33: [18, 9.0] | attack terror syria | Brussels_ISIL_terror_cell |
| 8. | hurricane | 36: [16, 16.0] | hurricane irma maria | Hurricane_Irma |
| 9. | jerusalem | 49: [15, 15.0] | jerusalem trump 's | United_States_recognition_of_Jerusalem_as_capital_of_Israel |
| 10. | north | 15: [10, 5.0], 27: [14, 14.0], 32: [17, 5.67] | north korea trump | North_Korea–United_States_relations |
| 11. | g | 27: [13, 13.0] | g trump summit | 46th_G7_summit |
| 12. | korea | 27: [12, 12.0], 32: [15, 5.0], 35: [12, 12.0] | korea north trump | 2018_North_Korea–United_States_Singapore_Summit |
| 13. | qatar | 23: [11, 11.0] | qatar crisis gulf | Qatar_diplomatic_crisis |
| 14. | spain | 33: [11, 11.0] | spain catalonia catalan | Catalonia_national_football_team |
| 15. | mugabe | 46: [15, 7.5] | mugabe zimbabwe robert | Robert_Mugabe |
| 16. | women | 3: [14, 7.0], 10: [19, 6.33] | women 's march | 2017_Women's_March |
| 17. | hong | 26: [13, 6.5] | hong kong china | Hong_Kong |
| 18. | kong | 26: [13, 6.5] | kong hong china | Hong_Kong |
| 19. | trump | 27: [19, 6.33], 45: [15, 5.0] | trump 's donald | Donald_Trump |
| 20. | 's | 1: [24, 6.0] | 's trump president | Donald_Trump |
| 21. | sexual | 44: [18, 6.0] | sexual harassment assault | Sexual_harassment |
| 22. | harassment | 44: [10, 5.0] | harassment sexual women | Sexual_Harassment_of_Women_at_Workplace_(Prevention,_Prohibition_and_Redressal)_Act,_2013 |
