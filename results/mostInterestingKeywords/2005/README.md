# Keywords with the highest 'interestingness' in 2005

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
| 1. | north | 1: [10, 5.0], 17: [15, 5.0], 27: [15, 15.0], 37: [49, inf] | north korea 's | North_Korea |
| 2. | including | 1: [10, inf], 38: [11, 5.5] | including 's world | The_World's_Billionaires |
| 3. | region | 1: [15, 7.5], 4: [12, 12.0], 22: [10, inf], 50: [15, inf] | region 's world | Region |
| 4. | families | 1: [11, inf] | families 's two | Two_Is_a_Family |
| 5. | family | 1: [15, inf], 36: [12, 6.0] | family 's police | United_States_Capitol_Police |
| 6. | photos | 1: [26, 13.0], 27: [11, 5.5], 44: [12, inf] | photos 's map | Google_Maps |
| 7. | abbas | 1: [28, 7.0], 13: [16, inf], 21: [19, inf] | abbas palestinian israel | Mahmoud_Abbas |
| 8. | fire | 1: [12, 6.0], 7: [12, inf], 10: [10, 5.0], 43: [11, 5.5] | fire gaza israeli | 2014_Gaza_War |
| 9. | tsunami | 1: [70, 8.75], 13: [10, inf] | tsunami 's aid | 2004_Indian_Ocean_earthquake_and_tsunami |
| 10. | south | 1: [24, inf] | south 's africa | South_Africa |
| 11. | two | 1: [16, inf] | two 's world | Two_Worlds_II |
| 12. | make | 1: [11, inf], 35: [16, 5.33] | make 's would | Would? |
| 13. | economy | 1: [10, inf] | economy 's china | Economy_of_China |
| 14. | sri | 1: [13, 6.5], 34: [10, 10.0], 46: [16, inf] | sri lanka 's | Sri_Lanka |
| 15. | aceh | 1: [13, inf], 28: [13, 6.5] | aceh indonesia tsunami | Aceh |
| 16. | around | 1: [10, 10.0], 16: [10, 5.0], 18: [10, inf], 26: [12, 6.0] | around 's world | Around_the_World_in_Eighty_Days |
| 17. | struggle | 1: [11, inf] | struggle 's political | Struggle_session |
| 18. | basque | 1: [12, inf], 5: [13, inf] | basque spain eta | ETA_(separatist_group) |
| 19. | spain | 1: [11, 11.0], 5: [11, inf], 10: [14, 7.0], 39: [11, 5.5], 44: [20, 20.0] | spain 's europe | Spain |
| 20. | province | 1: [10, inf], 26: [10, 10.0], 31: [18, 6.0], 33: [10, 5.0], 35: [20, inf] | province 's killed | Islamic_State_of_Iraq_and_the_Levant_–_Khorasan_Province |
| 21. | try | 1: [11, inf], 28: [10, 10.0] | try 's israel | Israel |
| 22. | bush | 1: [10, inf], 34: [11, 11.0] | bush 's president | George_H._W._Bush |
| 23. | official | 1: [12, inf], 30: [19, 6.33] | official 's police | Colt_Official_Police |
| 24. | million | 1: [16, inf], 11: [18, 6.0], 17: [18, 9.0], 37: [11, 5.5] | million 's world | Mega_Millions |
| 25. | state | 1: [10, inf], 30: [19, 6.33], 33: [20, 5.0], 35: [21, 5.25] | state 's government | State_governments_of_the_United_States |
| 26. | cuba | 1: [13, inf] | cuba 's guantánamo | Guantánamo_Bay |
| 27. | jewish | 1: [14, inf], 16: [12, 6.0], 26: [18, 6.0], 29: [10, 10.0], 31: [19, inf] | jewish gaza israeli | 2014_Gaza_War |
| 28. | french | 1: [11, inf], 7: [11, 5.5], 15: [12, 12.0], 24: [30, 5.0], 35: [11, 5.5], 38: [10, 10.0], 45: [48, 12.0] | french france 's | France |
| 29. | children | 1: [22, inf], 22: [17, 5.67], 30: [12, 6.0], 38: [14, 7.0] | children 's world | Children_of_the_World |
| 30. | report | 1: [10, 10.0], 9: [17, inf], 38: [21, 7.0] | report 's united | U.S._News_&_World_Report |
| 31. | relations | 1: [11, inf] | relations 's china | China–United_States_relations |
| 32. | solidarity | 1: [10, inf] | solidarity 's would | Solidarity |
| 33. | aids | 1: [10, inf], 18: [12, 6.0], 47: [12, inf] | aids 's africa | HIV/AIDS_in_Africa |
| 34. | arafat | 1: [18, inf], 8: [14, inf], 36: [19, inf] | arafat palestinian abbas | Mahmoud_Abbas |
| 35. | lost | 1: [11, inf] | lost 's people | The_Lost_People |
| 36. | mandela | 1: [13, inf] | mandela south africa | Zindzi_Mandela |
| 37. | prison | 2: [17, inf], 18: [10, 10.0] | prison years 's | Prison |
| 38. | flight | 2: [10, inf], 31: [10, inf] | flight 's world | TWA_Flight_800 |
| 39. | corruption | 2: [13, inf], 12: [11, inf], 36: [17, 17.0] | corruption 's president | President_of_the_United_States |
| 40. | members | 2: [13, inf], 45: [10, 5.0] | members 's government | Federal_government_of_the_United_States |
| 41. | talks | 2: [13, inf], 4: [17, 8.5], 19: [15, 5.0], 30: [33, 6.6], 37: [40, 5.0], 49: [25, 8.33] | talks 's nuclear | Six-party_talks |
| 42. | nazi | 2: [10, inf], 4: [12, inf] | nazi 's world | Nazi_Germany |
| 43. | visit | 2: [12, 6.0], 13: [17, inf], 35: [11, 5.5], 52: [10, 5.0] | visit 's china | Richard_Nixon's_1972_visit_to_China |
| 44. | cow | 2: [10, inf] | cow mad disease | Bovine_spongiform_encephalopathy |
| 45. | congressional | 2: [10, inf] | congressional 's president | President_pro_tempore_of_the_United_States_Senate |
| 46. | prince | 2: [10, inf], 14: [29, 14.5] | prince 's monaco | Albert_II,_Prince_of_Monaco |
| 47. | titan | 2: [15, inf] | titan 's moon | Titan_(moon) |
| 48. | zhao | 3: [18, 9.0], 35: [10, inf] | zhao chinese times | Zhao_Ziyang |
| 49. | funeral | 3: [11, inf], 14: [66, inf] | funeral 's pope | Funeral_of_Pope_John_Paul_II |
| 50. | car | 3: [11, inf], 17: [11, 5.5], 28: [16, 16.0] | car bomb 's | Car_bomb |
| 51. | abuse | 3: [13, 13.0], 16: [14, inf], 39: [11, 5.5] | abuse 's report | Abuse_Reporting_Format |
| 52. | autonomy | 4: [13, inf] | autonomy 's government | Autonomy |
| 53. | georgia | 4: [15, inf] | georgia 's europe | Georgia_(U.S._state) |
| 54. | pentagon | 4: [10, inf], 31: [13, inf] | pentagon iraq american | The_Pentagon |
| 55. | general | 4: [15, inf] | general 's united | United_States_Attorney_General |
| 56. | auschwitz | 4: [13, inf] | auschwitz camp death | Auschwitz_concentration_camp |
| 57. | davos | 4: [11, inf] | davos atomic world | DNA_digital_data_storage |
| 58. | church | 5: [14, inf], 45: [20, 6.67] | church pope 's | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 59. | parliament | 5: [13, inf], 22: [12, 6.0] | parliament 's government | Government_of_the_United_Kingdom |
| 60. | ireland | 5: [15, inf] | ireland northern irish | Northern_Ireland |
| 61. | king | 5: [10, 5.0], 27: [14, inf], 31: [31, inf], 35: [12, 6.0] | king 's nepal | King_of_Nepal |
| 62. | emergency | 5: [10, 10.0], 45: [14, inf] | emergency 's state | State_of_emergency |
| 63. | greets | 6: [10, inf] | greets pope 's | Pope_Francis |
| 64. | togo | 6: [12, 12.0], 17: [16, inf] | togo 's gnassingbe | Faure_Gnassingbé |
| 65. | investigation | 6: [10, 5.0], 32: [10, inf] | investigation 's police | Police_Bureau_of_Investigation |
| 66. | suspects | 6: [11, 5.5], 28: [22, inf], 44: [10, 5.0] | suspects 's police | The_Usual_Suspects |
| 67. | sudan | 6: [11, 11.0], 31: [39, 19.5], 45: [11, inf] | sudan darfur 's | War_in_Darfur |
| 68. | kurds | 6: [11, inf] | kurds kurdish iraqi | Kurdish_population |
| 69. | darfur | 6: [13, 6.5], 45: [14, inf] | darfur sudan 's | War_in_Darfur |
| 70. | quebec | 6: [14, inf], 31: [11, inf] | quebec party canada | Quebec_Liberal_Party |
| 71. | wednesday | 6: [13, inf], 21: [15, 5.0] | wednesday 's president | President_of_the_United_States |
| 72. | rape | 6: [14, inf], 26: [13, 13.0] | rape 's court | Mahmudiyah_rape_and_killings |
| 73. | charles | 6: [11, inf], 14: [19, inf] | charles police 's | Charles_Ramsey |
| 74. | japan | 6: [10, 5.0], 31: [14, inf] | japan 's china | China–Japan_relations |
| 75. | saudi | 6: [12, 12.0], 9: [10, inf], 31: [23, inf] | saudi arabia 's | Saudi_Arabia |
| 76. | claim | 7: [10, inf], 45: [11, 5.5] | claim 's police | Police |
| 77. | policy | 7: [13, inf], 18: [10, 10.0] | policy 's government | Public_policy |
| 78. | administration | 7: [10, inf], 21: [16, 5.33], 23: [11, 5.5] | administration 's bush | Presidency_of_George_W._Bush |
| 79. | mosque | 7: [10, inf] | mosque 's attacks | Christchurch_mosque_shootings |
| 80. | monday | 7: [20, inf], 17: [11, inf], 23: [17, 5.67], 34: [19, 9.5], 36: [10, 5.0], 44: [13, 13.0], 46: [10, 5.0] | monday 's mr. | Plough_Monday |
| 81. | oil | 7: [16, 8.0], 19: [10, 5.0], 35: [18, inf], 40: [15, 15.0], 47: [20, 6.67] | oil 's iraq | Oil_reserves_in_Iraq |
| 82. | iran | 7: [11, 11.0], 19: [13, 6.5], 43: [15, inf] | iran nuclear 's | Nuclear_program_of_Iran |
| 83. | terrorist | 7: [11, inf], 27: [11, 5.5], 39: [17, 8.5] | terrorist 's attacks | September_11_attacks |
| 84. | hariri | 7: [16, inf], 22: [13, inf], 25: [13, inf], 35: [12, 12.0] | hariri 's lebanon | Rafic_Hariri |
| 85. | lebanon | 7: [30, inf], 9: [26, 5.2], 50: [11, inf] | lebanon 's syria | Mandate_for_Syria_and_the_Lebanon |
| 86. | hezbollah | 7: [12, inf], 10: [21, 10.5] | hezbollah lebanese lebanon | 2006_Lebanon_War |
| 87. | raids | 7: [10, inf] | raids police 's | Police_raid |
| 88. | canada | 8: [11, inf], 26: [15, inf], 31: [11, 11.0], 35: [11, 5.5], 43: [11, 5.5] | canada 's canadian | Canadians |
| 89. | gaymard | 8: [11, inf] | gaymard apartment finance | Hervé_Gaymard |
| 90. | apartment | 8: [12, inf] | apartment 's french | Penthouse_apartment |
| 91. | pledges | 8: [10, inf] | pledges 's aid | Aid |
| 92. | palestinians | 8: [18, 6.0], 11: [12, inf], 21: [18, 9.0] | palestinians israel palestinian | Israeli–Palestinian_conflict |
| 93. | barrier | 8: [10, inf] | barrier 's israel | Israeli_West_Bank_barrier |
| 94. | home | 8: [11, inf] | home 's britain | British_Home_Championship |
| 95. | document | 9: [12, inf] | document 's constitution | Constitution |
| 96. | syria | 9: [25, 6.25], 17: [16, inf], 21: [11, 5.5], 29: [10, inf], 49: [10, 5.0] | syria 's lebanon | Mandate_for_Syria_and_the_Lebanon |
| 97. | hussein | 9: [15, 7.5], 15: [14, inf], 19: [12, 6.0], 24: [13, 13.0], 42: [19, 9.5] | hussein 's iraq | Human_rights_in_Saddam_Hussein's_Iraq |
| 98. | hong | 9: [14, inf], 14: [10, inf], 22: [12, 12.0], 38: [17, inf], 45: [10, inf] | hong kong 's | Hong_Kong |
| 99. | kong | 9: [14, inf], 14: [10, inf], 22: [12, 12.0], 38: [17, inf], 45: [10, inf] | kong hong 's | Hong_Kong |
| 100. | abortion | 9: [10, inf] | abortion 's women | Abortion_in_India |
| 101. | journalist | 9: [13, 13.0], 22: [14, inf], 24: [12, 12.0], 31: [13, 6.5], 40: [10, 10.0] | journalist 's killed | List_of_journalists_killed_in_Europe |
| 102. | shooting | 10: [12, inf] | shooting police israeli | Stoneman_Douglas_High_School_shooting |
| 103. | system | 10: [11, inf], 19: [14, 7.0] | system 's government | List_of_countries_by_system_of_government |
| 104. | moldova | 10: [11, inf] | moldova russia communist | Party_of_Communists_of_the_Republic_of_Moldova |
| 105. | russian | 10: [12, inf], 46: [11, inf] | russian russia 's | Russia |
| 106. | dominican | 10: [10, inf] | dominican prison home | Dominican_Republic |
| 107. | sony | 10: [16, inf] | sony 's company | Sony |
| 108. | next | 10: [10, inf] | next 's party | PartyNextDoor |
| 109. | company | 10: [11, 5.5], 49: [10, inf] | company 's oil | Shell_Oil_Company |
| 110. | kosovo | 10: [10, inf] | kosovo 's united | United_Nations_Interim_Administration_Mission_in_Kosovo |
| 111. | mesa | 10: [10, inf] | mesa bolivia president | Carlos_Mesa |
| 112. | ira | 10: [11, inf], 14: [11, inf], 30: [11, inf] | ira irish ireland | Irish_Republican_Army |
| 113. | chechen | 10: [15, inf] | chechen russia russian | Chechen–Russian_conflict |
| 114. | airport | 11: [10, inf], 31: [14, 14.0], 36: [12, 12.0] | airport 's plane | Gordon_Ramsay_Plane_Food |
| 115. | korea | 11: [19, inf], 30: [35, 8.75], 37: [42, 10.5], 49: [15, 15.0] | korea north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 116. | rice | 11: [15, inf], 16: [10, inf], 19: [10, 5.0], 24: [11, 11.0], 41: [20, inf], 45: [10, 5.0], 49: [21, 10.5] | rice state secretary | Condoleezza_Rice |
| 117. | canadian | 11: [10, 10.0], 37: [13, inf] | canadian canada 's | Canadians |
| 118. | budget | 12: [10, inf], 48: [12, 6.0] | budget 's sharon | Sharon_Pratt |
| 119. | pakistani | 12: [11, inf], 44: [16, inf] | pakistani pakistan 's | Pakistanis |
| 120. | khan | 12: [10, inf], 28: [11, 5.5] | khan london 's | Sadiq_Khan |
| 121. | week | 12: [16, inf] | week 's last | Last_Week_Tonight_with_John_Oliver |
| 122. | program | 12: [14, inf], 35: [11, inf], 41: [15, 5.0] | program 's nuclear | Nuclear_program_of_Iran |
| 123. | chechnya | 12: [11, 11.0], 50: [12, inf] | chechnya russia 's | Chechnya |
| 124. | commission | 12: [10, 5.0], 25: [12, inf] | commission 's government | City_commission_government |
| 125. | oil-for-food | 12: [10, inf], 36: [11, inf] | oil-for-food program united | Oil-for-Food_Programme |
| 126. | trade | 12: [10, inf], 23: [10, 5.0], 40: [14, inf] | trade 's china | China–United_States_trade_war |
| 127. | whether | 12: [10, inf], 25: [11, 11.0], 30: [17, 17.0] | whether 's government | Federal_government_of_the_United_States |
| 128. | rebels | 13: [10, inf], 15: [12, 6.0] | rebels 's government | List_of_Star_Wars_Rebels_characters |
| 129. | parties | 13: [10, inf], 38: [10, 10.0], 43: [19, 19.0] | parties 's government | Federal_government_of_the_United_States |
| 130. | known | 13: [11, inf], 45: [11, 5.5] | known 's years | There_are_known_knowns |
| 131. | death | 13: [45, 6.43], 16: [10, 10.0], 33: [19, 9.5], 40: [12, inf], 48: [10, 10.0] | death 's world | Death_to_the_World |
| 132. | festival | 13: [10, inf] | festival film 's | Film_festival |
| 133. | journalists | 13: [12, inf] | journalists 's government | List_of_journalists_killed_in_Europe |
| 134. | near | 13: [10, 5.0], 22: [18, inf], 35: [18, 18.0], 44: [20, 5.0] | near 's two | Near-Earth_object |
| 135. | described | 13: [10, inf] | described 's two | Two-hybrid_screening |
| 136. | nias | 13: [10, inf] | nias quake earthquake | Nias |
| 137. | signs | 13: [11, inf] | signs 's israel | Israel |
| 138. | great | 13: [10, inf] | great 's pope | Pope_Leo_I |
| 139. | vatican | 13: [17, 5.67], 30: [14, inf] | vatican pope 's | Pope_John_Paul_I_conspiracy_theories |
| 140. | resignation | 13: [12, inf], 23: [11, 5.5] | resignation 's president | Letter_of_resignation |
| 141. | mr. | 13: [10, 10.0], 15: [16, inf], 30: [34, 8.5] | mr. 's president | Mr._President_(title) |
| 142. | heart | 13: [10, inf] | heart 's pope | Sacred_Heart |
| 143. | rwanda | 13: [10, inf] | rwanda genocide rwandan | Rwandan_genocide |
| 144. | pray | 13: [10, inf] | pray 's pope | Rosary |
| 145. | krakow | 13: [22, inf] | krakow 's pope | Kraków_John_Paul_II_International_Airport |
| 146. | beyond | 13: [20, inf] | beyond 's pope | Pope |
| 147. | prayers | 13: [23, inf] | prayers 's pope | Prayer_to_Saint_Michael |
| 148. | tributes | 13: [20, inf] | tributes 's pope | Smoking_Popes_Tribute |
| 149. | awe | 13: [20, inf] | awe 's pope | Pope_Benedict_XVI |
| 150. | poland | 13: [11, inf], 30: [13, inf] | poland 's pope | Pope_John_Paul_II |
| 151. | cardinal | 13: [10, inf] | cardinal pope 's | Pope_Francis |
| 152. | kashmir | 14: [11, inf] | kashmir pakistan india | 2014_India–Pakistan_floods |
| 153. | bus | 14: [13, inf], 27: [21, inf], 49: [11, inf] | bus london police | List_of_bus_routes_in_London |
| 154. | divided | 14: [12, inf] | divided 's kashmir | List_of_districts_of_Jammu_and_Kashmir |
| 155. | legal | 14: [10, inf], 17: [10, 10.0], 35: [10, 5.0] | legal 's court | Court_dress |
| 156. | wedding | 14: [16, inf] | wedding charles 's | Wedding_of_Prince_Charles_and_Lady_Diana_Spencer |
| 157. | blair | 14: [11, inf], 22: [16, 16.0], 48: [11, 5.5] | blair 's prime | Tony_Blair |
| 158. | camilla | 14: [13, inf] | camilla charles wedding | Wedding_of_Prince_Charles_and_Camilla_Parker_Bowles |
| 159. | parker | 14: [11, inf] | parker charles camilla | Wedding_of_Prince_Charles_and_Camilla_Parker_Bowles |
| 160. | bowles | 14: [11, inf] | bowles charles camilla | Wedding_of_Prince_Charles_and_Camilla_Parker_Bowles |
| 161. | bolton | 15: [18, 6.0], 30: [10, inf] | bolton 's senate | John_Bolton |
| 162. | soldiers | 15: [10, 10.0], 38: [16, inf], 48: [13, 6.5] | soldiers military 's | Women_in_the_military |
| 163. | constitution | 15: [12, inf], 21: [21, 7.0], 27: [15, inf] | constitution 's iraq | Constitution_of_Iraq |
| 164. | rumsfeld | 15: [11, inf], 41: [11, 11.0] | rumsfeld defense secretary | Donald_Rumsfeld |
| 165. | `` | 15: [12, inf] | `` 's mr. | Toyota_MR2 |
| 166. | pledge | 15: [10, inf] | pledge 's world | The_Giving_Pledge |
| 167. | support | 16: [11, 5.5], 47: [10, inf], 51: [13, 13.0] | support 's government | Federal_government_of_the_United_States |
| 168. | congress | 16: [15, 7.5], 22: [17, inf], 25: [10, 10.0], 32: [15, 5.0] | congress 's president | List_of_presidents_of_the_Indian_National_Congress |
| 169. | gutierrez | 16: [13, inf] | gutierrez ecuador 's | Lucio_Gutiérrez |
| 170. | gen | 16: [12, inf] | gen 's annan | Kofi_Annan |
| 171. | federal | 16: [12, 12.0], 30: [11, inf] | federal 's mexico | Mexico_City |
| 172. | delay | 16: [24, inf], 19: [13, inf] | delay 's gaza | Gaza_Strip |
| 173. | film | 16: [12, inf] | film 's police | Police_Academy_(film) |
| 174. | might | 16: [13, inf], 30: [11, 11.0] | might 's government | They_Might_Be_Giants |
| 175. | roman | 16: [12, 6.0], 45: [10, inf] | roman pope 's | Pope |
| 176. | obrador | 16: [14, inf] | obrador mexico mayor | Andrés_Manuel_López_Obrador |
| 177. | presidential | 16: [10, inf], 34: [11, 5.5] | presidential 's election | United_States_presidential_election |
| 178. | benedict | 16: [32, inf] | benedict pope xvi | Resignation_of_Pope_Benedict_XVI |
| 179. | xvi | 16: [29, inf] | xvi pope benedict | Resignation_of_Pope_Benedict_XVI |
| 180. | wartime | 16: [12, inf] | wartime 's japan | Economic_history_of_Japan |
| 181. | social | 17: [17, inf] | social 's party | Social_Liberal_Party_(Brazil) |
| 182. | syrian | 17: [10, inf], 22: [20, inf], 41: [16, inf] | syrian lebanon 's | Syrian_occupation_of_Lebanon |
| 183. | tuesday | 17: [18, 18.0], 26: [28, 7.0], 31: [25, inf], 33: [17, 5.67] | tuesday 's mr. | Tuesday_Weld |
| 184. | wounded | 17: [12, inf], 35: [10, inf], 46: [11, 11.0] | wounded killed least | List_of_mass_shootings_in_the_United_States_in_2020 |
| 185. | driver | 17: [20, inf] | driver killed 's | Baby_Driver |
| 186. | croatia | 17: [10, inf] | croatia crimes union | 2013_enlargement_of_the_European_Union |
| 187. | anthem | 17: [10, inf] | anthem `` teachers | Kimigayo |
| 188. | member | 17: [10, 10.0], 35: [10, inf] | member 's union | Member_state_of_the_European_Union |
| 189. | gen. | 17: [14, inf] | gen. 's military | Military_coups_in_Pakistan |
| 190. | chisale | 17: [10, inf] | chisale lions mr. | EMPTY MATCHING |
| 191. | northern | 18: [16, 5.33], 33: [16, inf] | northern 's police | Police_Service_of_Northern_Ireland |
| 192. | kills | 18: [12, inf], 33: [16, 8.0] | kills bomb suicide | Suicide_attack |
| 193. | old | 18: [12, inf], 39: [10, 10.0] | old 's years | 38_Years_Old |
| 194. | child | 18: [11, inf] | child 's children | Child_labour |
| 195. | labor | 18: [17, inf] | labor 's party | Minnesota_Democratic–Farmer–Labor_Party |
| 196. | fatah | 18: [10, inf], 50: [18, inf] | fatah palestinian elections | Next_Palestinian_general_election |
| 197. | without | 19: [14, inf] | without 's government | Federal_government_of_the_United_States |
| 198. | trial | 19: [16, inf], 35: [10, 10.0], 38: [13, 13.0], 42: [26, 13.0] | trial 's court | Trial_court |
| 199. | union | 19: [16, 5.33], 35: [10, inf], 37: [24, inf], 46: [17, 17.0] | union european 's | European_Union |
| 200. | permanent | 19: [10, inf] | permanent 's united | Green_card |
| 201. | crimes | 19: [15, inf], 23: [11, 11.0] | crimes 's tribunal | International_Military_Tribunal_for_the_Far_East |
| 202. | run | 19: [10, inf], 30: [13, 6.5] | run 's president | President_of_the_United_States |
| 203. | council | 19: [22, 7.33], 36: [11, 5.5], 38: [20, inf] | council 's security | United_Nations_Security_Council |
| 204. | lower | 19: [10, 10.0], 51: [13, inf] | lower 's house | Lower_house |
| 205. | uzbek | 19: [10, inf], 46: [10, inf] | uzbek uzbekistan crackdown | Education_in_Uzbekistan |
| 206. | treaty | 19: [14, inf] | treaty 's nuclear | Treaty_on_the_Non-Proliferation_of_Nuclear_Weapons |
| 207. | raise | 20: [13, inf] | raise 's government | Federal_government_of_the_United_States |
| 208. | verdict | 20: [11, inf] | verdict 's mr. | After_the_Verdict |
| 209. | companies | 20: [10, inf], 22: [12, 6.0], 43: [15, inf] | companies 's oil | Seven_Sisters_(oil_companies) |
| 210. | truce | 20: [10, inf] | truce palestinian israel | Gaza_War_(2008–2009) |
| 211. | bring | 21: [10, inf] | bring 's party | Democratic_Party_(United_States) |
| 212. | shrine | 21: [21, 10.5], 39: [10, inf], 42: [12, inf] | shrine 's japan | Yasukuni_Shrine |
| 213. | sectarian | 21: [10, inf] | sectarian iraq 's | Iraqi_Civil_War_(2006–2008) |
| 214. | nearly | 21: [10, inf] | nearly 's government | Government_of_India |
| 215. | chirac | 21: [18, 9.0], 35: [10, inf] | chirac france french | Jacques_Chirac |
| 216. | site | 21: [15, inf] | site 's web | Website |
| 217. | short | 21: [10, inf] | short 's vote | Voting |
| 218. | i.r.a | 21: [11, inf], 30: [12, inf] | i.r.a irish ireland | Ireland |
| 219. | paramilitary | 21: [10, inf] | paramilitary 's colombia | Right-wing_paramilitarism_in_Colombia |
| 220. | right | 21: [10, inf] | right 's nuclear | Nuclear_program_of_Iran |
| 221. | fertility | 22: [10, inf] | fertility law pope | 2005_Italian_fertility_laws_referendum |
| 222. | newspaper | 22: [14, inf], 48: [10, 10.0] | newspaper 's world | List_of_newspapers_by_circulation |
| 223. | hamas | 22: [11, 5.5], 50: [10, inf] | hamas palestinian gaza | Hamas |
| 224. | bomber | 22: [10, 5.0], 24: [14, inf], 28: [23, inf], 49: [14, 7.0] | bomber suicide police | Female_suicide_bomber |
| 225. | food | 22: [12, inf], 38: [18, 6.0] | food 's aid | Aid |
| 226. | charter | 22: [10, inf] | charter 's constitution | Canadian_Charter_of_Rights_and_Freedoms |
| 227. | missile | 22: [11, inf] | missile israel 's | Arrow_(Israeli_missile) |
| 228. | zimbabwe | 22: [11, 5.5], 29: [16, inf], 35: [15, inf] | zimbabwe 's mugabe | Robert_Mugabe |
| 229. | missiles | 22: [12, inf] | missiles 's gaza | 2014_Gaza_War |
| 230. | video | 22: [10, inf] | video 's iraq | July_12,_2007,_Baghdad_airstrike |
| 231. | scud | 22: [12, inf] | scud syria missiles | Scud_missile |
| 232. | kassir | 22: [10, inf] | kassir lebanese syrian | Samir_Kassir |
| 233. | hindu | 23: [18, inf] | hindu india party | Hindu_Mahasabha |
| 234. | mortar | 23: [13, inf] | mortar israeli gaza | 2014_Gaza_War |
| 235. | senate | 23: [14, inf], 38: [10, 10.0] | senate bolton 's | John_Bolton |
| 236. | advani | 23: [10, inf] | advani hindu party | L._K._Advani |
| 237. | debt | 23: [10, inf] | debt world 's | History_of_the_United_States_public_debt |
| 238. | questioned | 24: [10, inf] | questioned bombings 's | Atomic_bombings_of_Hiroshima_and_Nagasaki |
| 239. | wine | 24: [10, inf] | wine france europe | French_wine |
| 240. | memo | 24: [15, inf] | memo 's iraq | Bush–Blair_2003_Iraq_memo |
| 241. | executive | 24: [11, inf] | executive 's hong | Chief_Executive_of_Hong_Kong |
| 242. | prosecutor | 24: [12, inf], 38: [12, 6.0] | prosecutor 's mr. | My_Lawyer,_Mr._Jo |
| 243. | strike | 25: [11, inf], 28: [11, 5.5], 47: [10, inf] | strike 's government | UK_miners'_strike_(1984–85) |
| 244. | bombs | 25: [12, inf], 27: [24, 8.0] | bombs police london | List_of_terrorist_incidents_in_London |
| 245. | fraud | 25: [14, inf] | fraud 's election | Republican_reactions_to_Donald_Trump's_claims_of_2020_election_fraud |
| 246. | wines | 25: [11, inf], 35: [12, inf] | wines africa 's | South_African_wine |
| 247. | arab | 25: [11, 11.0], 43: [10, 5.0], 50: [10, inf] | arab 's sunni | Arab_states–Israeli_alliance_against_Iran |
| 248. | muslim | 25: [10, inf], 34: [12, 6.0] | muslim 's police | National_Association_of_Muslim_Police |
| 249. | use | 25: [16, inf], 40: [10, 10.0] | use 's china | Land_use_in_China |
| 250. | six | 25: [11, inf] | six 's police | Six_Pack_(The_Police_box_set) |
| 251. | turkey | 25: [10, 10.0], 28: [14, inf], 35: [16, inf] | turkey 's european | Accession_of_Turkey_to_the_European_Union |
| 252. | crash | 25: [12, inf], 31: [17, inf], 36: [11, inf] | crash plane 's | Lynyrd_Skynyrd_plane_crash |
| 253. | plane | 25: [10, inf], 31: [16, inf], 33: [28, 14.0] | plane crash people | Germanwings_Flight_9525 |
| 254. | berlusconi | 25: [10, inf] | berlusconi 's italy | Silvio_Berlusconi |
| 255. | bosnian | 25: [11, inf] | bosnian serb crimes | Bosnian_War |
| 256. | supporters | 26: [10, 5.0], 45: [10, inf] | supporters 's president | Vice_President_of_the_United_States |
| 257. | fusion | 26: [10, inf] | fusion reactor france | Fusion_power |
| 258. | helicopter | 26: [17, inf] | helicopter crash 's | 2020_Calabasas_helicopter_crash |
| 259. | forgery | 26: [11, inf] | forgery mubarak nour | Ayman_Nour |
| 260. | nour | 26: [11, inf] | nour mubarak 's | Ayman_Nour |
| 261. | held | 26: [17, 5.67], 30: [14, inf], 43: [10, 10.0] | held 's world | Held |
| 262. | sovereignty | 26: [14, inf] | sovereignty 's government | Popular_sovereignty |
| 263. | gay | 26: [17, inf] | gay marriage bill | Same-sex_marriage |
| 264. | shiite | 26: [15, inf], 34: [16, 8.0], 43: [10, 5.0] | shiite 's iraq | Faisal_I_of_Iraq |
| 265. | reactor | 26: [10, inf], 37: [13, 13.0] | reactor nuclear north | List_of_nuclear_reactors |
| 266. | operations | 26: [12, inf] | operations military 's | Military_operation_plan |
| 267. | team | 26: [14, inf] | team 's united | United_States_women's_national_soccer_team |
| 268. | protesters | 26: [13, inf], 38: [12, inf] | protesters 's police | George_Floyd_protests |
| 269. | missing | 26: [12, inf] | missing 's people | Missing_People |
| 270. | sunni | 27: [21, inf], 50: [17, inf] | sunni iraq 's | Sons_of_Iraq |
| 271. | diplomat | 27: [22, inf] | diplomat 's iraq | Abduction_of_Russian_diplomats_in_Iraq |
| 272. | threat | 27: [10, inf], 42: [10, 5.0] | threat 's would | Minor_Threat |
| 273. | flu | 27: [11, 5.5], 38: [14, inf] | flu bird china | Avian_influenza |
| 274. | details | 27: [10, inf] | details 's would | The_Detail |
| 275. | republic | 27: [11, inf] | republic 's chechnya | Chechnya |
| 276. | show | 27: [11, 11.0], 51: [11, inf] | show 's would | Would_I_Lie_to_You?_(game_show) |
| 277. | warming | 27: [13, inf] | warming global 's | Climate_change |
| 278. | global | 27: [13, inf] | global 's world | Global_city |
| 279. | london | 27: [59, inf], 38: [19, 19.0] | london police 's | Metropolitan_Police |
| 280. | pinochet | 27: [10, inf], 32: [11, inf] | pinochet chile 's | Augusto_Pinochet |
| 281. | immunity | 27: [10, inf] | immunity pinochet court | Indictment_and_arrest_of_Augusto_Pinochet |
| 282. | subway | 27: [20, inf], 33: [11, 5.5] | subway police london | 1984_New_York_City_Subway_shooting |
| 283. | trains | 27: [13, inf] | trains london police | Metropolitan_Police |
| 284. | sunday | 28: [30, 6.0], 36: [23, 5.75], 45: [11, inf] | sunday 's president | President_of_the_United_States |
| 285. | armed | 28: [12, 12.0], 48: [10, inf] | armed 's palestinian | Palestinian_Security_Services |
| 286. | body | 28: [11, inf] | body 's police | Police_body_camera |
| 287. | number | 28: [13, inf] | number 's iraq | Multi-National_Force_–_Iraq |
| 288. | reserve | 28: [10, inf] | reserve iraq 's | Oil_reserves_in_Iraq |
| 289. | brought | 28: [10, inf] | brought 's president | President_of_the_United_States |
| 290. | silence | 28: [13, inf] | silence 's party | "S"_Is_for_Silence |
| 291. | leeds | 28: [17, inf] | leeds police london | Little_London,_Leeds |
| 292. | tanweer | 28: [10, inf] | tanweer bombers khan | Shehzad_Tanweer |
| 293. | panel | 29: [11, inf], 52: [12, 12.0] | panel 's annan | Kofi_Annan |
| 294. | already | 29: [14, inf], 31: [10, 5.0] | already 's government | Federal_government_of_the_United_States |
| 295. | sheik | 29: [11, inf] | sheik 's sharm | Sharm_El_Sheikh |
| 296. | committee | 29: [10, inf] | committee 's bolton | John_Bolton |
| 297. | korean | 30: [11, inf] | korean north korea | North_Korea–South_Korea_relations |
| 298. | raid | 30: [13, 13.0], 38: [11, inf], 48: [10, inf] | raid police 's | RAID_(French_police_unit) |
| 299. | ambassador | 30: [13, inf] | ambassador bolton 's | John_Bolton |
| 300. | mubarak | 30: [16, inf] | mubarak 's egypt | Hosni_Mubarak |
| 301. | belarus | 30: [13, inf] | belarus 's lukashenko | Alexander_Lukashenko |
| 302. | rome | 30: [12, inf] | rome 's pope | List_of_popes |
| 303. | sudanese | 31: [10, inf] | sudanese sudan darfur | Sudanese_nomadic_conflicts |
| 304. | arabia | 31: [13, inf] | arabia saudi 's | Saudi_Arabia |
| 305. | fahd | 31: [16, inf] | fahd king saudi | Fahd_of_Saudi_Arabia |
| 306. | italian | 31: [11, 5.5], 36: [10, inf] | italian italy 's | Demographics_of_Italy |
| 307. | brother | 31: [10, inf] | brother 's former | Big_Brother_(American_TV_series) |
| 308. | garang | 31: [21, inf] | garang sudan leader | John_Garang |
| 309. | passengers | 31: [10, inf] | passengers police 's | Passenger_57 |
| 310. | marines | 31: [19, inf], 40: [13, inf], 48: [17, inf] | marines iraq american | United_States_Marine_Corps |
| 311. | david | 31: [12, inf] | david 's british | David_Soul |
| 312. | arabs | 31: [16, inf] | arabs sunni 's | Arab_states–Israeli_alliance_against_Iran |
| 313. | jet | 31: [10, inf] | jet 's air | Jet_engine |
| 314. | vehicle | 31: [10, inf] | vehicle bomb 's | Car_bomb |
| 315. | health | 31: [15, 7.5], 43: [16, 8.0], 45: [10, inf] | health 's world | World_Health_Organization |
| 316. | crew | 31: [14, inf] | crew 's crash | Crash_Crew |
| 317. | submarine | 31: [12, inf] | submarine russian 's | List_of_Soviet_and_Russian_submarine_classes |
| 318. | river | 31: [11, inf] | river 's iraq | Iraq |
| 319. | information | 31: [14, inf] | information 's intelligence | Intelligence_assessment |
| 320. | niger | 31: [12, inf] | niger 's world | Niger |
| 321. | soldier | 31: [10, inf] | soldier israeli killed | Timeline_of_the_Israeli–Palestinian_conflict |
| 322. | u.n. | 32: [11, inf] | u.n. united nations | Headquarters_of_the_United_Nations |
| 323. | koizumi | 32: [13, 6.5], 42: [11, 11.0], 44: [10, inf] | koizumi 's japan | Junichiro_Koizumi |
| 324. | sikhs | 32: [10, inf] | sikhs sikh party | Sikhs |
| 325. | cleric | 32: [14, inf], 38: [11, 5.5] | cleric shiite 's | Shia_clergy |
| 326. | indulgences | 32: [14, inf] | indulgences pope young | Pope_Leo_X |
| 327. | militants | 32: [12, 6.0], 48: [11, inf] | militants palestinian gaza | Gaza–Israel_conflict |
| 328. | heathrow | 32: [10, inf] | heathrow british strike | British_Airways |
| 329. | athens | 33: [12, inf] | athens plane crash | List_of_accidents_and_incidents_involving_airliners_by_location |
| 330. | spanish | 33: [10, inf], 51: [11, inf] | spanish spain 's | Spain |
| 331. | sentences | 33: [11, inf] | sentences court years | Suspended_sentence |
| 332. | port | 33: [10, inf] | port 's world | World's_busiest_ports |
| 333. | synagogue | 33: [13, inf] | synagogue gaza israeli | Israeli_disengagement_from_Gaza |
| 334. | synagogues | 33: [10, inf] | synagogues gaza israeli | Israeli_disengagement_from_Gaza |
| 335. | resume | 34: [10, inf] | resume nuclear iran | Joint_Comprehensive_Plan_of_Action |
| 336. | france | 34: [10, inf] | france 's french | France |
| 337. | hunger | 34: [10, inf] | hunger 's world | Global_Hunger_Index |
| 338. | immigrants | 34: [11, inf], 45: [12, 6.0] | immigrants 's french | Immigration_to_France |
| 339. | knives | 35: [10, inf] | knives africa chisale | EMPTY MATCHING |
| 340. | senators | 35: [10, inf] | senators bolton 's | John_Bolton |
| 341. | public | 35: [18, inf] | public 's government | State_school |
| 342. | ethnic | 35: [11, inf] | ethnic 's government | List_of_ethnic_slurs_by_ethnicity |
| 343. | netanyahu | 35: [17, inf] | netanyahu sharon 's | Benjamin_Netanyahu |
| 344. | michael | 35: [14, inf] | michael 's africa | Out_of_Africa_(film) |
| 345. | stampede | 35: [16, inf] | stampede iraq baghdad | 2005_Al-Aaimmah_bridge_stampede |
| 346. | minibus | 35: [10, inf] | minibus police cliff | Get_Duked! |
| 347. | linked | 36: [15, inf] | linked 's police | United_States_Capitol_Police |
| 348. | indonesian | 36: [12, inf] | indonesian indonesia 's | Indonesia |
| 349. | outside | 36: [13, inf] | outside 's world | World_Outside |
| 350. | weapon | 36: [12, inf] | weapon nuclear `` | Nuclear_weapon |
| 351. | cyprus | 37: [17, inf] | cyprus turkey union | Turkish_invasion_of_Cyprus |
| 352. | britain | 37: [19, inf], 48: [16, 8.0] | britain 's british | Britishness |
| 353. | compromise | 37: [11, inf] | compromise 's mr. | Compromise_of_1790 |
| 354. | hopes | 37: [10, inf], 42: [10, 10.0] | hopes 's political | New_Hope_(Israel) |
| 355. | demand | 37: [11, inf] | demand 's nuclear | Nuclear_program_of_Iran |
| 356. | shiites | 37: [10, inf] | shiites iraq 's | Islamic_State_of_Iraq_and_the_Levant |
| 357. | camp | 38: [10, inf], 41: [11, inf] | camp 's refugee | Refugee_camp |
| 358. | massacre | 38: [10, inf] | massacre srebrenica bosnian | Srebrenica_massacre |
| 359. | british | 38: [32, 10.67], 40: [12, 6.0], 51: [15, inf] | british 's britain | Britishness |
| 360. | bombers | 38: [10, inf] | bombers london police | 7_July_2005_London_bombings |
| 361. | tensions | 38: [10, inf] | tensions 's china | 2020_China–India_skirmishes |
| 362. | khodorkovsky | 38: [17, inf] | khodorkovsky 's oil | Mikhail_Khodorkovsky |
| 363. | protest | 38: [10, inf], 51: [12, 6.0] | protest 's government | Protest |
| 364. | echeverría | 38: [10, inf] | echeverría mr. president | President_of_Mexico |
| 365. | charge | 38: [10, inf] | charge 's mr. | Mr._Mayor |
| 366. | ayatollah | 38: [12, inf] | ayatollah 's iran | Ayatollah |
| 367. | draft | 38: [13, inf], 43: [10, inf] | draft constitution 's | Constitution_of_the_United_States |
| 368. | governing | 38: [12, inf] | governing party 's | Ruling_party |
| 369. | visits | 39: [17, inf] | visits 's japan | Japan |
| 370. | justice | 39: [10, inf] | justice 's government | United_States_Department_of_Justice |
| 371. | hughes | 39: [11, inf] | hughes american 's | Glenn_Hughes_(American_singer) |
| 372. | laws | 39: [10, inf] | laws 's `` | Murphy's_law |
| 373. | algerians | 39: [11, inf] | algerians vote 's | Algerian_War |
| 374. | iranian | 39: [10, 10.0], 43: [14, inf] | iranian iran 's | Demographics_of_Iran |
| 375. | possible | 39: [10, inf] | possible 's government | Kim_Possible |
| 376. | ice | 39: [10, inf] | ice arctic gases | Climate_change_in_the_Arctic |
| 377. | venezuelan | 40: [10, inf] | venezuelan venezuela 's | Crisis_in_Venezuela_during_the_Bolivarian_Revolution |
| 378. | chancellor | 40: [18, 18.0], 47: [13, inf] | chancellor 's germany | Chancellor_of_Germany |
| 379. | nobel | 40: [13, inf] | nobel prize nuclear | 2017_Nobel_Peace_Prize |
| 380. | sanctions | 40: [13, inf] | sanctions 's united | United_States_sanctions |
| 381. | rescue | 41: [10, inf] | rescue 's train | Search_and_rescue |
| 382. | rescuers | 41: [11, inf] | rescuers survivors quake | 2008_Sichuan_earthquake |
| 383. | strain | 41: [10, inf] | strain 's flu | Hong_Kong_flu |
| 384. | virus | 41: [10, inf] | virus birds flu | Avian_influenza |
| 385. | poverty | 41: [12, inf] | poverty africa 's | Poverty_in_Africa |
| 386. | travel | 42: [10, inf] | travel 's palestinian | Palestinian_Authority_passport |
| 387. | coast | 42: [10, inf] | coast 's people | Indigenous_peoples_of_the_Pacific_Northwest_Coast |
| 388. | authority | 42: [10, inf] | authority palestinian 's | Palestinian_National_Authority |
| 389. | results | 42: [11, inf] | results 's election | Attempts_to_overturn_the_2020_United_States_presidential_election |
| 390. | criticism | 42: [10, inf] | criticism 's government | Criticism_of_the_Israeli_government |
| 391. | lawyer | 42: [10, inf] | lawyer 's hussein | Execution_of_Saddam_Hussein |
| 392. | work | 43: [12, inf] | work 's government | Copyright_status_of_works_by_the_federal_government_of_the_United_States |
| 393. | study | 43: [12, inf] | study 's world | Globalization_and_World_Cities_Research_Network |
| 394. | determine | 43: [13, inf] | determine 's world | Darts_world_rankings |
| 395. | leaders | 43: [13, inf] | leaders 's government | List_of_current_heads_of_state_and_government |
| 396. | center | 43: [10, inf] | center 's city | CityCenter |
| 397. | girl | 43: [16, inf] | girl 's -year-old | Destiny's_Child |
| 398. | spread | 44: [11, inf] | spread 's two | Spread_betting |
| 399. | rioting | 44: [14, inf] | rioting france violence | 2005_French_riots |
| 400. | clashes | 44: [10, inf] | clashes 's killed | 2020–21_Ayn_Issa_clashes |
| 401. | unrest | 44: [12, inf] | unrest 's police | Ferguson_unrest |
| 402. | spreads | 44: [13, inf] | spreads 's violence | Violence |
| 403. | suburbs | 44: [15, inf] | suburbs violence paris | Paris |
| 404. | summit | 44: [10, inf] | summit meeting 's | Summit_(meeting) |
| 405. | equatorial | 44: [10, inf] | equatorial guinea coup | 2004_Equatorial_Guinea_coup_d'état_attempt |
| 406. | guinea | 44: [10, inf] | guinea equatorial coup | 2004_Equatorial_Guinea_coup_d'état_attempt |
| 407. | catholic | 45: [15, inf] | catholic pope 's | List_of_popes |
| 408. | chile | 45: [14, inf] | chile pinochet 's | Augusto_Pinochet |
| 409. | curfews | 45: [11, inf] | curfews emergency violence | Violence_and_controversies_during_the_George_Floyd_protests |
| 410. | discrimination | 45: [10, inf] | discrimination french 's | Discrimination |
| 411. | mandate | 45: [12, inf] | mandate 's government | Mandate_for_Palestine |
| 412. | lawyers | 45: [13, inf] | lawyers 's court | Lawyer |
| 413. | jordan | 45: [16, inf] | jordan jordanian attack | Jordan |
| 414. | like | 45: [11, 11.0], 47: [13, inf] | like 's world | In_a_World_Like_This |
| 415. | amman | 45: [12, inf] | amman jordan attacks | 2005_Amman_bombings |
| 416. | priests | 45: [14, inf] | priests church pope | Catholic_Church_sexual_abuse_cases |
| 417. | sexual | 45: [12, inf] | sexual report church | Catholic_Church_sexual_abuse_cases |
| 418. | contract | 46: [10, inf] | contract annan iraq | Kofi_Annan |
| 419. | defeat | 47: [10, inf] | defeat 's party | Democratic_Party_(United_States) |
| 420. | water | 47: [18, inf] | water 's city | New_York_City_water_supply_system |
| 421. | spill | 47: [15, inf] | spill china water | Xingang_Port_oil_spill |
| 422. | alamieyeseigha | 48: [10, inf] | alamieyeseigha nigeria 's | Diepreye_Alamieyeseigha |
| 423. | see | 48: [10, inf] | see 's many | How_Many_Clouds_Can_You_See? |
| 424. | mall | 49: [12, inf] | mall shopping suicide | Westroads_Mall_shooting |
| 425. | lead | 49: [11, inf] | lead 's party | Republican_Party_(United_States) |
| 426. | planned | 50: [11, inf] | planned 's gaza | Israeli_disengagement_from_Gaza |
| 427. | tueni | 50: [10, inf] | tueni car syria | Gebran_Tueni |
| 428. | missionaries | 51: [12, inf] | missionaries north 's | Missionary |
| 429. | uzbekistan | 51: [11, inf] | uzbekistan uzbek crackdown | Education_in_Uzbekistan |
| 430. | karzai | 51: [11, inf] | karzai afghanistan afghan | Politics_of_Afghanistan |
| 431. | tax | 51: [12, inf] | tax 's charges | Poll_tax_(Great_Britain) |
| 432. | navy | 51: [13, inf] | navy 's u.s. | United_States_Navy |
| 433. | h.i.v | 51: [10, inf] | h.i.v 's children | V/H/S |
| 434. | libya | 51: [11, inf] | libya 's nuclear | Libya_and_weapons_of_mass_destruction |
| 435. | schwarzenegger | 52: [10, inf] | schwarzenegger 's stadium | Liebenauer_Stadium |
| 436. | ghana | 52: [12, inf] | ghana 's africans | Ghana |
| 437. | kidnapped | 52: [10, inf] | kidnapped 's baghdad | Foreign_hostages_in_Iraq |
| 438. | hwang | 52: [10, inf] | hwang stem cells | Hwang_Woo-suk |
| 439. | rebel | 10: [12, 6.0], 31: [28, 28.0] | rebel 's leader | Carlota_(rebel_leader) |
| 440. | suicide | 18: [10, 5.0], 24: [14, 14.0], 28: [56, 28.0], 30: [35, 5.0] | suicide bomber killed | Female_suicide_bomber |
| 441. | failed | 30: [26, 26.0] | failed 's police | Failed_state |
| 442. | paris | 44: [26, 26.0] | paris france 's | Paris |
| 443. | women | 32: [25, 25.0], 51: [10, 5.0] | women 's rights | Women's_rights |
| 444. | africa | 10: [19, 6.33], 14: [16, 5.33], 22: [24, 24.0] | africa world 's | South_Africa |
| 445. | italy | 16: [23, 23.0], 46: [19, 9.5] | italy 's italian | Demographics_of_Italy |
| 446. | speech | 26: [22, 22.0] | speech 's bush | Mission_Accomplished_speech |
| 447. | forces | 17: [21, 21.0], 48: [18, 9.0] | forces 's security | Rhodesian_Security_Forces |
| 448. | air | 31: [21, 21.0] | air 's world | United_States_Air_Force |
| 449. | group | 3: [19, 19.0], 29: [20, 5.0] | group 's world | World_Group |
| 450. | rights | 9: [19, 19.0] | rights 's human | Human_rights |
| 451. | girls | 22: [19, 19.0] | girls 's children | Children's_literature |
| 452. | says | 1: [37, 18.5] | says 's government | Say's_law |
| 453. | photo | 1: [39, 6.5], 25: [18, 18.0], 35: [20, 5.0] | photo 's government | Google_Photos |
| 454. | last | 6: [18, 18.0] | last 's world | The_Last_World |
| 455. | thailand | 1: [17, 17.0] | thailand 's tsunami | 2004_Indian_Ocean_earthquake_and_tsunami |
| 456. | troops | 2: [17, 17.0], 17: [17, 17.0], 33: [22, 7.33] | troops 's iraq | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 457. | iraqis | 3: [17, 17.0], 15: [10, 10.0], 21: [12, 6.0], 41: [11, 11.0] | iraqis iraq iraqi | Islamic_State_of_Iraq |
| 458. | mexico | 16: [12, 6.0], 22: [12, 12.0], 26: [12, 12.0], 37: [20, 5.0], 46: [17, 17.0] | mexico 's fox | Vicente_Fox |
| 459. | guilty | 26: [17, 17.0] | guilty 's court | Alford_plea |
| 460. | foreign | 34: [17, 17.0] | foreign 's minister | Foreign_minister |
| 461. | prize | 40: [17, 17.0] | prize nobel nuclear | 2017_Nobel_Peace_Prize |
| 462. | pakistan | 12: [16, 16.0], 19: [20, 6.67], 34: [10, 5.0], 40: [33, 16.5] | pakistan 's pakistani | Pakistanis |
| 463. | palestinian | 1: [35, 7.0], 33: [25, 5.0], 42: [16, 16.0] | palestinian israeli israel | Israeli–Palestinian_conflict |
| 464. | long | 13: [16, 16.0], 26: [16, 16.0] | long 's government | Government |
| 465. | across | 17: [15, 7.5], 21: [16, 16.0] | across 's iraq | Iraq_War |
| 466. | issue | 19: [11, 11.0], 38: [16, 16.0] | issue 's government | Government_Issue |
| 467. | religious | 27: [12, 6.0], 45: [16, 16.0], 51: [11, 11.0] | religious 's government | Separation_of_church_and_state_in_the_United_States |
| 468. | search | 28: [16, 16.0] | search police 's | Search_warrant |
| 469. | forced | 33: [16, 16.0] | forced 's government | Forced_conversion |
| 470. | basra | 38: [16, 16.0] | basra iraq 's | Basra |
| 471. | vote | 1: [15, 15.0], 36: [20, 6.67], 45: [21, 7.0] | vote 's election | Electoral_fraud |
| 472. | killing | 7: [15, 15.0] | killing 's police | Encounter_killings_by_police |
| 473. | intelligence | 13: [19, 9.5], 22: [12, 12.0], 28: [15, 15.0] | intelligence 's officials | William_Binney_(intelligence_official) |
| 474. | villagers | 15: [15, 15.0] | villagers 's police | Wukan_protests |
| 475. | must | 19: [15, 15.0], 28: [10, 10.0] | must 's says | Say's_law |
| 476. | terrorism | 27: [12, 6.0], 37: [15, 15.0] | terrorism 's suspects | Terrorism_in_the_United_States |
| 477. | pullout | 32: [30, 15.0] | pullout gaza 's | Israeli_disengagement_from_Gaza |
| 478. | relief | 41: [30, 15.0] | relief 's aid | CARES_Act |
| 479. | israel | 1: [42, 14.0] | israel gaza palestinian | Gaza_War_(2008–2009) |
| 480. | still | 1: [14, 14.0], 45: [11, 5.5] | still 's world | The_World_Is_Still_Beautiful |
| 481. | fox | 6: [14, 14.0] | fox mexico 's | Vicente_Fox |
| 482. | gaza | 7: [13, 6.5], 13: [20, 10.0], 16: [28, 14.0], 22: [17, 8.5] | gaza israeli israel | Gaza–Israel_conflict |
| 483. | chinese | 9: [10, 10.0], 13: [14, 14.0] | chinese china 's | China |
| 484. | civil | 10: [14, 14.0], 51: [10, 5.0] | civil 's government | Civil_Disobedience_(Thoreau) |
| 485. | india | 14: [14, 14.0], 41: [12, 6.0] | india 's pakistan | India–Pakistan_relations |
| 486. | german | 15: [14, 14.0] | german 's germany | Germany |
| 487. | taiwan | 17: [28, 14.0] | taiwan china 's | Taiwan,_China |
| 488. | bolivian | 23: [14, 14.0] | bolivian president protests | 2019_Bolivian_protests |
| 489. | polls | 36: [14, 14.0] | polls 's party | Democratic_Party_(United_States) |
| 490. | candidates | 37: [14, 14.0], 43: [10, 10.0] | candidates 's elections | List_of_United_States_presidential_candidates |
| 491. | would | 4: [12, 6.0], 13: [27, 13.5] | would 's world | The_World's_Billionaires |
| 492. | year | 1: [12, 12.0], 8: [13, 13.0], 44: [18, 6.0] | year 's last | Last_Year_at_Marienbad |
| 493. | president | 1: [13, 13.0] | president 's mr. | Mr._President_(title) |
| 494. | died | 1: [13, 13.0], 43: [12, 6.0] | died 's world | Dior |
| 495. | earthquake | 13: [13, 13.0] | earthquake pakistan quake | 2005_Kashmir_earthquake |
| 496. | percent | 16: [13, 13.0], 28: [10, 10.0], 42: [19, 6.33], 51: [10, 5.0] | percent 's government | Federal_government_of_the_United_States |
| 497. | colombia | 18: [13, 13.0] | colombia 's world | Colombia |
| 498. | join | 19: [13, 13.0] | join 's european | 2022_European_Men's_Handball_Championship_qualification |
| 499. | dutch | 19: [14, 7.0], 39: [13, 13.0] | dutch netherlands 's | Netherlands_national_football_team |
| 500. | found | 24: [13, 13.0] | found 's police | Death_of_JonBenét_Ramsey |
| 501. | g- | 27: [13, 13.0] | g- africa protesters | George_Floyd_protests |
| 502. | cross | 27: [13, 13.0] | cross 's north | Knight's_Cross_of_the_Iron_Cross |
| 503. | central | 27: [13, 13.0] | central 's government | Central_government |
| 504. | malaysia | 32: [13, 13.0] | malaysia indonesia 's | Indonesia–Malaysia_confrontation |
| 505. | force | 33: [26, 13.0] | force 's police | United_States_Air_Force_Security_Forces |
| 506. | ban | 35: [13, 13.0] | ban 's world | Ban_Ki-moon |
| 507. | meeting | 35: [25, 8.33], 44: [13, 13.0] | meeting 's leaders | Asia-Pacific_Economic_Cooperation |
| 508. | helicopters | 41: [13, 13.0] | helicopters military american | Military_helicopter |
| 509. | conservatives | 42: [13, 13.0] | conservatives 's party | Conservative_Party_(UK) |
| 510. | appears | 49: [13, 13.0] | appears 's gaza | 2014_Gaza_War |
| 511. | -- | 1: [16, 8.0], 14: [17, 5.67], 27: [17, 8.5], 30: [13, 6.5], 45: [25, 12.5], 50: [25, 5.0] | -- 's government | Federal_government_of_the_United_States |
| 512. | election | 1: [24, 12.0], 13: [21, 10.5], 45: [28, 7.0] | election 's party | 2024_United_States_presidential_election |
| 513. | israeli | 1: [22, 7.33], 10: [12, 12.0], 22: [38, 6.33], 49: [20, 5.0] | israeli gaza palestinian | 2012_Israeli_operation_in_the_Gaza_Strip |
| 514. | effort | 1: [16, 5.33], 5: [15, 7.5], 30: [12, 12.0] | effort 's government | War_effort |
| 515. | years | 1: [12, 12.0] | years 's world | Years_&_Years |
| 516. | bombing | 3: [10, 10.0], 35: [12, 12.0], 38: [14, 7.0] | bombing 's suicide | Suicide_attack |
| 517. | pope | 5: [12, 12.0], 12: [17, 5.67], 13: [95, 5.59] | pope 's john | Pope_John_Paul_II |
| 518. | irish | 7: [12, 12.0] | irish ireland 's | Great_Famine_(Ireland) |
| 519. | accused | 9: [10, 5.0], 30: [11, 11.0], 43: [12, 12.0] | accused 's world | The_Accüsed |
| 520. | violence | 13: [12, 12.0], 44: [30, 6.0] | violence 's police | List_of_police_violence_incidents_during_George_Floyd_protests |
| 521. | mourning | 14: [24, 12.0] | mourning 's pope | National_day_of_mourning |
| 522. | money | 20: [12, 6.0], 32: [12, 12.0] | money 's world | All_the_Money_in_the_World |
| 523. | post | 20: [12, 12.0] | post 's minister | Minister_for_Posts_and_Telegraphs |
| 524. | department | 21: [12, 12.0] | department 's state | United_States_Department_of_State |
| 525. | insurgent | 22: [12, 12.0] | insurgent iraq american | Iraqi_insurgency_(2003–2011) |
| 526. | democracy | 23: [15, 5.0], 45: [12, 12.0], 49: [11, 11.0] | democracy 's bush | Bush_Doctrine |
| 527. | marriage | 23: [10, 10.0], 26: [12, 12.0] | marriage gay 's | Same-sex_marriage_in_the_United_States |
| 528. | ahmadinejad | 25: [12, 12.0] | ahmadinejad iran 's | Mahmoud_Ahmadinejad |
| 529. | schröder | 26: [12, 12.0], 36: [15, 5.0] | schröder 's chancellor | Gerhard_Schröder |
| 530. | interview | 30: [12, 12.0] | interview 's united | The_Interview |
| 531. | afghan | 32: [10, 5.0], 36: [12, 12.0], 51: [19, 6.33] | afghan afghanistan taliban | War_in_Afghanistan_(2001–present) |
| 532. | law | 35: [12, 12.0], 39: [11, 11.0] | law 's government | Constitutional_law |
| 533. | aid | 35: [12, 12.0], 51: [11, 5.5] | aid 's united | United_States_foreign_aid |
| 534. | institute | 36: [12, 12.0] | institute 's international | Graduate_Institute_of_International_and_Development_Studies |
| 535. | detonated | 39: [12, 12.0] | detonated suicide least | 2019_Jalalabad_suicide_bombing |
| 536. | made | 40: [12, 12.0] | made 's united | How_It's_Made |
| 537. | counterterrorism | 40: [12, 12.0] | counterterrorism 's bombings | National_Counterterrorism_Center |
| 538. | shootings | 42: [12, 12.0] | shootings killed least | Mass_shootings_in_the_United_States |
| 539. | left | 1: [11, 11.0], 21: [17, 5.67] | left 's world | Left_Behind |
| 540. | among | 1: [11, 11.0] | among 's government | Federal_government_of_the_United_States |
| 541. | toward | 1: [11, 11.0] | toward 's step | Neil_Armstrong |
| 542. | campaign | 1: [11, 11.0], 7: [11, 5.5] | campaign 's party | WalkAway_campaign |
| 543. | united | 1: [11, 11.0] | united 's nations | United_Nations |
| 544. | european | 1: [17, 8.5], 13: [11, 11.0], 35: [14, 7.0], 37: [15, 5.0] | european 's union | European_Union |
| 545. | leader | 2: [27, 6.75], 16: [33, 11.0] | leader 's party | Party_leader |
| 546. | east | 4: [11, 11.0] | east middle world | Middle_East |
| 547. | camps | 4: [11, 11.0] | camps 's china | Xinjiang_re-education_camps |
| 548. | time | 5: [11, 11.0] | time 's first | First_Time |
| 549. | office | 6: [10, 5.0], 30: [11, 11.0] | office 's mr. | Mr._Box_Office |
| 550. | countries | 9: [10, 5.0], 48: [11, 11.0] | countries 's world | List_of_sovereign_states |
| 551. | plan | 13: [16, 5.33], 34: [11, 11.0] | plan 's would | Plan_S |
| 552. | baghdad | 15: [11, 11.0], 37: [16, 8.0] | baghdad iraq iraqi | Baghdad |
| 553. | become | 15: [11, 11.0] | become 's government | Federal_government_of_the_United_States |
| 554. | poor | 15: [11, 11.0] | poor 's world | S&P_Global_Ratings |
| 555. | afghanistan | 17: [11, 11.0], 35: [12, 6.0], 37: [22, 5.5] | afghanistan afghan 's | Flag_of_Afghanistan |
| 556. | fired | 20: [11, 11.0] | fired gaza israeli | 2014_Gaza_War |
| 557. | -year-old | 22: [11, 11.0] | -year-old 's world | The_World's_Billionaires |
| 558. | annan | 24: [22, 11.0] | annan united nations | Kofi_Annan |
| 559. | bombings | 24: [15, 7.5], 27: [22, 11.0], 45: [21, 5.25] | bombings london attacks | 7_July_2005_London_bombings |
| 560. | tehran | 24: [11, 11.0] | tehran iran 's | Tehran |
| 561. | amid | 26: [11, 11.0] | amid 's government | Government_shutdowns_in_the_United_States |
| 562. | month | 27: [10, 5.0], 46: [11, 11.0] | month 's last | Month |
| 563. | question | 30: [11, 11.0] | question 's police | United_States_Capitol_Police |
| 564. | orleans | 38: [11, 11.0] | orleans mayor reopening | LaToya_Cantrell |
| 565. | service | 41: [11, 11.0] | service 's officials | List_of_U.S._statewide_elected_officials |
| 566. | violent | 44: [11, 11.0] | violent 's city | Violent_City |
| 567. | call | 45: [11, 11.0] | call 's government | Federal_government_of_the_United_States |
| 568. | dispute | 46: [11, 11.0] | dispute 's world | Dispute_settlement_in_the_World_Trade_Organization |
| 569. | reports | 48: [11, 11.0] | reports 's world | U.S._News_&_World_Report |
| 570. | victims | 1: [11, 5.5], 24: [10, 10.0], 28: [21, 10.5], 41: [11, 5.5] | victims 's government | Victims'_rights |
| 571. | insurgents | 12: [21, 10.5] | insurgents iraq iraqi | Iraqi_insurgency_(2003–2011) |
| 572. | attacks | 1: [10, 10.0], 12: [11, 5.5], 35: [25, 5.0] | attacks 's police | 2016_shooting_of_Dallas_police_officers |
| 573. | lanka | 1: [10, 5.0], 34: [10, 10.0] | lanka sri 's | Sri_Lanka |
| 574. | kill | 2: [10, 10.0], 32: [15, 5.0], 36: [15, 5.0] | kill 's least | Disposition_Matrix |
| 575. | bill | 5: [15, 5.0], 44: [10, 10.0] | bill 's would | Bill_&_Ted |
| 576. | minister | 5: [15, 5.0], 10: [10, 10.0], 38: [47, 5.22] | minister 's prime | List_of_prime_ministers_of_the_United_Kingdom |
| 577. | back | 8: [10, 10.0], 51: [17, 5.67] | back 's world | Back_in_the_U.S.S.R. |
| 578. | defense | 8: [10, 10.0], 31: [11, 5.5] | defense 's minister | Defence_minister |
| 579. | anniversary | 10: [10, 10.0] | anniversary 's th | Wedding_anniversary |
| 580. | thousands | 10: [10, 10.0], 31: [17, 5.67] | thousands 's people | Decimal_separator |
| 581. | march | 10: [10, 10.0], 17: [13, 6.5], 26: [12, 6.0], 47: [10, 5.0] | march 's party | Political_party_strength_in_U.S._states |
| 582. | match | 10: [10, 10.0] | match 's rights | Children's_rights |
| 583. | statement | 13: [10, 10.0] | statement 's world | Mission_statement |
| 584. | day | 13: [10, 10.0], 17: [20, 5.0] | day 's police | Police_Day |
| 585. | several | 13: [10, 10.0], 24: [10, 5.0], 38: [10, 10.0] | several 's police | United_States_Capitol_Police |
| 586. | action | 13: [10, 10.0] | action 's world | World_in_Action |
| 587. | japanese | 15: [14, 7.0], 21: [10, 10.0], 44: [14, 7.0] | japanese japan 's | Japan |
| 588. | rally | 15: [10, 10.0] | rally 's gaza | Reactions_to_the_2014_Israel–Gaza_conflict |
| 589. | charged | 15: [12, 6.0], 22: [10, 10.0] | charged 's world | Fully_Charged |
| 590. | continue | 16: [10, 10.0], 28: [10, 10.0] | continue 's world | U.S._News_&_World_Report |
| 591. | night | 17: [10, 10.0] | night 's president | President_of_the_United_States |
| 592. | win | 18: [12, 6.0], 38: [10, 10.0] | win 's party | WIN_Party |
| 593. | arrested | 18: [17, 5.67], 40: [10, 10.0] | arrested 's police | Arrest |
| 594. | tower | 19: [10, 10.0] | tower 's police | Grenfell_Tower_fire |
| 595. | taliban | 22: [11, 5.5], 26: [10, 10.0], 39: [16, 8.0] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 596. | reporter | 22: [10, 10.0] | reporter 's iraq | 2003_invasion_of_Iraq |
| 597. | affairs | 22: [10, 10.0] | affairs 's united | United_States_Department_of_Veterans_Affairs |
| 598. | israelis | 22: [10, 10.0] | israelis israeli gaza | Gaza–Israel_conflict |
| 599. | houses | 24: [10, 10.0] | houses 's police | White_House_Police_Force |
| 600. | anti-syrian | 25: [10, 10.0] | anti-syrian 's lebanon | Syrian_Civil_War_spillover_in_Lebanon |
| 601. | denies | 26: [10, 10.0] | denies 's government | Copyright_status_of_works_by_the_federal_government_of_the_United_States |
| 602. | britons | 28: [10, 10.0] | britons british britain | Celtic_Britons |
| 603. | menezes | 30: [10, 10.0] | menezes police london | Shooting_of_Jean_Charles_de_Menezes |
| 604. | qaeda | 31: [12, 6.0], 35: [10, 10.0] | qaeda 's iraq | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 605. | buried | 31: [10, 10.0] | buried 's pope | List_of_popes |
| 606. | close | 31: [11, 5.5], 33: [10, 10.0] | close 's government | Federal_voting_rights_in_Puerto_Rico |
| 607. | board | 33: [13, 6.5], 38: [10, 10.0] | board 's iran | Nuclear_program_of_Iran |
| 608. | accident | 33: [10, 10.0] | accident 's crash | Aviation_accidents_and_incidents |
| 609. | start | 34: [10, 10.0] | start 's government | Government |
| 610. | fires | 34: [10, 10.0] | fires 's government | Federal_government_of_the_United_States |
| 611. | white | 35: [10, 10.0] | white house 's | White_House |
| 612. | weeks | 35: [12, 6.0], 50: [10, 10.0] | weeks 's two | Two_Weeks_Notice |
| 613. | development | 35: [10, 10.0] | development 's united | United_States_Secretary_of_Housing_and_Urban_Development |
| 614. | army | 38: [11, 5.5], 46: [10, 10.0] | army 's israeli | Israel_Defense_Forces |
| 615. | n't | 42: [10, 10.0] | n't 's says | T.N.T._(album) |
| 616. | numbers | 42: [10, 10.0] | numbers 's world | Numbers_Gang |
| 617. | ally | 44: [10, 10.0] | ally 's minister | Allies_of_World_War_II |
| 618. | riots | 44: [10, 10.0] | riots party minister | Samajwadi_Party |
| 619. | voters | 45: [10, 10.0] | voters 's election | Electoral_fraud |
| 620. | address | 45: [10, 10.0] | address 's president | United_States_presidential_inauguration |
| 621. | getting | 48: [10, 10.0] | getting 's american | United_States |
| 622. | democrats | 49: [10, 10.0] | democrats 's bolton | John_Bolton |
| 623. | asian | 50: [10, 10.0] | asian 's japan | Economy_of_Asia |
| 624. | birds | 50: [20, 10.0] | birds flu 's | Avian_influenza |
| 625. | stroke | 51: [10, 10.0] | stroke sharon hospital | Ariel_Sharon |
| 626. | us | 51: [10, 10.0] | us 's united | United_States_Senate |
| 627. | assembly | 17: [19, 9.5] | assembly 's elections | 2019_Andhra_Pradesh_Legislative_Assembly_election |
| 628. | border | 19: [19, 9.5], 35: [17, 8.5] | border 's gaza | Gaza–Egypt_border |
| 629. | announced | 38: [19, 9.5] | announced 's world | A_Murder_Is_Announced |
| 630. | charges | 4: [13, 6.5], 18: [15, 5.0], 35: [18, 9.0] | charges 's mr. | Mr._Mayor |
| 631. | nuclear | 12: [32, 5.33], 34: [18, 9.0] | nuclear iran 's | Nuclear_program_of_Iran |
| 632. | least | 15: [18, 9.0] | least 's people | Least_squares |
| 633. | torture | 18: [11, 5.5], 48: [18, 9.0] | torture 's rights | Torture |
| 634. | survivors | 41: [18, 9.0] | survivors people 's | Survivor_guilt |
| 635. | bomb | 46: [18, 9.0] | bomb 's killed | Car_bomb |
| 636. | ratzinger | 16: [35, 8.75] | ratzinger pope 's | Pope_Benedict_XVI |
| 637. | disaster | 1: [26, 8.67] | disaster 's tsunami | 2011_Tōhoku_earthquake_and_tsunami |
| 638. | former | 35: [26, 8.67] | former 's minister | List_of_prime_ministers_of_India |
| 639. | many | 1: [32, 8.0], 8: [10, 5.0] | many 's people | Too_Many_People |
| 640. | may | 1: [16, 5.33], 38: [16, 8.0] | may 's world | The_World's_Billionaires |
| 641. | sharon | 7: [15, 7.5], 16: [16, 8.0], 51: [15, 7.5] | sharon israel gaza | Israeli_disengagement_from_Gaza |
| 642. | blast | 7: [10, 5.0], 46: [16, 8.0] | blast bomb killed | Blast_bomb |
| 643. | pres | 16: [33, 6.6], 25: [10, 5.0], 29: [15, 7.5], 51: [16, 8.0] | pres 's government | Federal_government_of_the_United_States |
| 644. | house | 16: [16, 8.0] | house 's white | White_House |
| 645. | embassy | 21: [16, 8.0] | embassy american 's | 1998_United_States_embassy_bombings |
| 646. | took | 30: [16, 8.0] | took 's world | Jasmine_Tookes |
| 647. | yushchenko | 36: [15, 7.5], 38: [16, 8.0] | yushchenko ukraine 's | Viktor_Yushchenko |
| 648. | gas | 52: [16, 8.0] | gas 's china | Natural_gas_in_China |
| 649. | u.s. | 1: [15, 7.5] | u.s. 's american | U.S._state |
| 650. | security | 11: [15, 7.5] | security 's forces | Rhodesian_Security_Forces |
| 651. | lebanese | 14: [15, 7.5], 22: [17, 5.67] | lebanese 's syrian | Syrian_Civil_War_spillover_in_Lebanon |
| 652. | expected | 22: [21, 5.25], 47: [15, 7.5] | expected 's world | Expected_value |
| 653. | shot | 26: [11, 5.5], 29: [15, 7.5] | shot police killed | List_of_British_police_officers_killed_in_the_line_of_duty |
| 654. | calls | 27: [12, 6.0], 32: [15, 7.5] | calls 's government | Federal_government_of_the_United_States |
| 655. | peres | 48: [15, 7.5] | peres sharon party | Shimon_Peres |
| 656. | settlers | 26: [22, 7.33] | settlers gaza israeli | Israeli_disengagement_from_Gaza |
| 657. | political | 3: [14, 7.0], 16: [31, 6.2] | political 's party | Political_parties_in_the_United_States |
| 658. | term | 10: [14, 7.0], 30: [12, 6.0] | term 's president | List_of_presidents_of_the_United_States_by_time_in_office |
| 659. | quake | 13: [21, 7.0] | quake pakistan earthquake | 2005_Kashmir_earthquake |
| 660. | watch | 14: [14, 7.0] | watch 's rights | Human_Rights_Watch |
| 661. | saturday | 15: [14, 7.0], 22: [14, 7.0] | saturday 's police | A_Night_at_the_Roxbury |
| 662. | joseph | 16: [28, 7.0] | joseph 's pope | Pope_Benedict_XVI |
| 663. | authorities | 21: [10, 5.0], 35: [14, 7.0] | authorities 's world | World_Service_Authority |
| 664. | referendum | 21: [14, 7.0] | referendum 's constitution | 2005_French_European_Constitution_referendum |
| 665. | beirut | 22: [14, 7.0], 50: [10, 5.0] | beirut syrian lebanon | Beirut |
| 666. | despite | 22: [14, 7.0], 27: [10, 5.0] | despite 's would | Covfefe |
| 667. | channel | 23: [14, 7.0] | channel 's news | Channel_4_News |
| 668. | decision | 23: [14, 7.0] | decision 's court | Dred_Scott_v._Sandford |
| 669. | african | 24: [12, 6.0], 44: [14, 7.0] | african 's africa | Africa |
| 670. | arrest | 25: [14, 7.0] | arrest 's police | Arrest |
| 671. | times | 35: [14, 7.0] | times 's police | United_States_Capitol_Police |
| 672. | candidate | 37: [14, 7.0] | candidate 's election | Write-in_candidate |
| 673. | indian | 41: [14, 7.0] | indian india 's | Economy_of_India |
| 674. | suspected | 49: [14, 7.0] | suspected 's police | Prime_Suspect |
| 675. | fuel | 49: [14, 7.0], 52: [11, 5.5] | fuel nuclear iran | Nuclear_program_of_Iran |
| 676. | convicted | 51: [14, 7.0] | convicted 's court | List_of_American_federal_politicians_convicted_of_crimes |
| 677. | cabinet | 8: [27, 6.75], 36: [10, 5.0], 44: [25, 6.25] | cabinet 's minister | Union_Council_of_Ministers |
| 678. | country | 1: [10, 5.0], 13: [26, 6.5] | country 's government | List_of_countries_by_government_budget |
| 679. | prime | 1: [13, 6.5] | prime 's minister | List_of_prime_ministers_of_the_United_Kingdom |
| 680. | major | 13: [13, 6.5], 31: [12, 6.0] | major 's government | Federal_government_of_the_United_States |
| 681. | mugabe | 13: [26, 6.5] | mugabe zimbabwe 's | Robert_Mugabe |
| 682. | apr | 14: [13, 6.5] | apr 's pope | Antipope |
| 683. | trip | 18: [13, 6.5] | trip 's mr. | Mr._Mouse_Takes_a_Trip |
| 684. | agency | 21: [11, 5.5], 32: [13, 6.5] | agency 's iran | Iranian_Space_Agency |
| 685. | thursday | 21: [12, 6.0], 38: [13, 6.5] | thursday 's mr. | Mr_Inbetween |
| 686. | early | 23: [13, 6.5] | early 's government | Federal_government_of_the_United_States |
| 687. | envoy | 25: [10, 5.0], 39: [13, 6.5] | envoy 's united | United_States_Special_Envoy_for_Northern_Ireland |
| 688. | even | 25: [13, 6.5] | even 's government | Federal_government_of_the_United_States |
| 689. | failure | 25: [13, 6.5] | failure 's european | European_Potato_Failure |
| 690. | town | 27: [13, 6.5] | town 's killed | S-Town |
| 691. | part | 30: [12, 6.0], 50: [13, 6.5] | part 's government | Federal_government_of_the_United_States |
| 692. | rocket | 33: [13, 6.5] | rocket gaza israeli | 2012_Israeli_operation_in_the_Gaza_Strip |
| 693. | led | 36: [11, 5.5], 45: [13, 6.5] | led 's government | LED_lamp |
| 694. | much | 41: [13, 6.5] | much 's world | The_World_Is_Too_Much_with_Us |
| 695. | guatemala | 41: [13, 6.5] | guatemala 's relief | Guatemala_City |
| 696. | australia | 41: [13, 6.5] | australia australian 's | Australia |
| 697. | officers | 44: [13, 6.5] | officers police 's | Police_officer |
| 698. | likud | 47: [13, 6.5] | likud sharon party | Likud |
| 699. | brotherhood | 47: [13, 6.5] | brotherhood muslim egypt | Muslim_Brotherhood_in_Egypt |
| 700. | reported | 48: [13, 6.5] | reported 's world | U.S._News_&_World_Report |
| 701. | figure | 51: [13, 6.5] | figure 's opposition | Leader_of_the_Opposition_(United_Kingdom) |
| 702. | peace | 51: [13, 6.5] | peace 's israel | Egypt–Israel_peace_treaty |
| 703. | map | 1: [19, 6.33], 33: [15, 5.0] | map 's photos | Google_Maps |
| 704. | asia | 1: [19, 6.33] | asia world briefing | BBC_World_News |
| 705. | indonesia | 1: [19, 6.33], 18: [12, 6.0] | indonesia 's aceh | Aceh |
| 706. | catholics | 14: [19, 6.33] | catholics pope 's | List_of_popes |
| 707. | city | 38: [43, 6.14] | city 's police | Baltimore_Police_Department |
| 708. | protests | 9: [12, 6.0] | protests 's government | Protest |
| 709. | basilica | 14: [12, 6.0] | basilica 's pope | St._Peter's_Basilica |
| 710. | called | 16: [12, 6.0] | called 's `` | The_Wolf's_Call |
| 711. | judge | 21: [12, 6.0], 25: [10, 5.0] | judge 's charges | Jared_Lee_Loughner |
| 712. | planes | 22: [12, 6.0] | planes 's world | Plane_(esotericism) |
| 713. | help | 22: [12, 6.0], 34: [12, 6.0] | help 's world | Help! |
| 714. | ministers | 23: [12, 6.0] | ministers 's world | Historical_rankings_of_prime_ministers_of_the_United_Kingdom |
| 715. | control | 24: [12, 6.0] | control 's government | Divided_government_in_the_United_States |
| 716. | case | 26: [24, 6.0] | case 's court | Supreme_Court_of_the_United_States |
| 717. | judges | 28: [12, 6.0] | judges 's court | List_of_sitting_judges_of_the_Supreme_Court_of_India |
| 718. | agreement | 30: [12, 6.0] | agreement 's talks | Paris_Peace_Accords |
| 719. | began | 31: [18, 6.0] | began 's world | Ever_Since_the_World_Began |
| 720. | toronto | 31: [12, 6.0] | toronto air canada | Air_Canada |
| 721. | earlier | 31: [12, 6.0] | earlier 's world | Early_world_maps |
| 722. | roadside | 31: [12, 6.0] | roadside bomb 's | Improvised_explosive_device |
| 723. | venezuela | 33: [12, 6.0] | venezuela 's chávez | Hugo_Chávez |
| 724. | buildings | 35: [18, 6.0] | buildings 's city | List_of_tallest_buildings_in_New_York_City |
| 725. | dozens | 38: [12, 6.0] | dozens 's people | Dozen |
| 726. | bird | 41: [12, 6.0] | bird flu china | Avian_influenza |
| 727. | finds | 41: [12, 6.0] | finds 's report | U.S._News_&_World_Report |
| 728. | saddam | 42: [24, 6.0], 45: [12, 6.0] | saddam hussein 's | Execution_of_Saddam_Hussein |
| 729. | plot | 43: [12, 6.0] | plot 's bomb | Bojinka_plot |
| 730. | brazil | 44: [12, 6.0] | brazil 's silva | Thiago_Silva |
| 731. | court | 48: [42, 6.0] | court 's world | International_Court_of_Justice |
| 732. | went | 51: [12, 6.0] | went 's world | The_Day_the_World_Went_Away |
| 733. | york | 51: [12, 6.0] | york 's united | List_of_United_States_Representatives_from_New_York |
| 734. | months | 24: [23, 5.75] | months 's government | Month |
| 735. | murder | 9: [17, 5.67] | murder 's world | World's_End_Murders |
| 736. | tony | 18: [17, 5.67] | tony blair 's | Tony_Blair |
| 737. | germany | 31: [17, 5.67] | germany 's world | Nazi_Germany |
| 738. | weapons | 37: [17, 5.67] | weapons 's nuclear | List_of_states_with_nuclear_weapons |
| 739. | putin | 17: [28, 5.6] | putin 's russia | Russia_under_Vladimir_Putin |
| 740. | bank | 34: [28, 5.6] | bank west israel | Israeli_West_Bank_barrier |
| 741. | mahmoud | 1: [11, 5.5] | mahmoud palestinian abbas | Mahmoud_Abbas |
| 742. | beijing | 9: [11, 5.5] | beijing 's china | Beijing |
| 743. | conference | 9: [11, 5.5] | conference 's world | World_Hindi_Conference |
| 744. | square | 13: [11, 5.5] | square 's pope | Attempted_assassination_of_Pope_John_Paul_II |
| 745. | st | 14: [22, 5.5] | st 's pope | Pope_Pius_X |
| 746. | killed | 15: [22, 5.5] | killed 's people | Mary_Kills_People |
| 747. | southern | 15: [11, 5.5] | southern 's police | Southern_United_States |
| 748. | seek | 15: [11, 5.5] | seek 's `` | Hide-and-seek |
| 749. | elected | 16: [10, 5.0], 51: [11, 5.5] | elected 's president | President-elect_of_the_United_States |
| 750. | staff | 17: [11, 5.5] | staff 's united | Chief_of_Staff_of_the_United_States_Army |
| 751. | lawmakers | 19: [11, 5.5] | lawmakers 's world | Mary_Miller_(politician) |
| 752. | energy | 20: [11, 5.5], 37: [11, 5.5] | energy 's nuclear | Nuclear_binding_energy |
| 753. | problems | 21: [11, 5.5] | problems 's say | Hilbert's_problems |
| 754. | nomination | 21: [11, 5.5] | nomination bolton 's | John_Bolton |
| 755. | inquiry | 22: [11, 5.5] | inquiry 's investigation | Committee_for_Skeptical_Inquiry |
| 756. | th | 22: [11, 5.5] | th 's anniversary | Wedding_anniversary |
| 757. | constitutional | 23: [11, 5.5] | constitutional 's elections | Elections_in_Germany |
| 758. | woman | 24: [11, 5.5] | woman 's world | Woman_Is_the_Nigger_of_the_World |
| 759. | hostage | 24: [11, 5.5] | hostage iraq united | Foreign_hostages_in_Iraq |
| 760. | second | 25: [11, 5.5] | second 's two | Two-round_system |
| 761. | network | 25: [11, 5.5] | network 's nuclear | Nuclear_weapons_of_the_United_States |
| 762. | chief | 28: [11, 5.5] | chief 's world | White_House_Chief_of_Staff |
| 763. | brazilian | 30: [11, 5.5] | brazilian police 's | Federal_Police_of_Brazil |
| 764. | vice | 31: [11, 5.5] | vice 's president | Vice_President_of_the_United_States |
| 765. | challenge | 32: [11, 5.5] | challenge 's party | Primary_challenge |
| 766. | settlement | 33: [22, 5.5] | settlement gaza 's | Population_statistics_for_Israeli_settlements_in_the_Gaza_Strip |
| 767. | crashed | 33: [11, 5.5] | crashed plane crash | Lynyrd_Skynyrd_plane_crash |
| 768. | gunmen | 38: [11, 5.5] | gunmen palestinian 's | Timeline_of_the_Israeli–Palestinian_conflict,_2002 |
| 769. | victory | 39: [11, 5.5] | victory 's party | Victory_Party |
| 770. | villages | 41: [11, 5.5] | villages 's people | Village_People |
| 771. | al-assad | 44: [11, 5.5] | al-assad syria 's | Asma_al-Assad |
| 772. | sentenced | 51: [11, 5.5] | sentenced years prison | List_of_longest_prison_sentences |
| 773. | agents | 52: [11, 5.5] | agents 's federal | Federal_Bureau_of_Investigation |
| 774. | 's | 1: [113, 5.38] | 's world government | World_government |
| 775. | china | 1: [16, 5.33] | china 's chinese | China |
| 776. | third | 18: [16, 5.33] | third 's world | Third_World |
| 777. | ministry | 22: [16, 5.33] | ministry 's interior | Ministry_of_Interior_(Pakistan) |
| 778. | national | 13: [21, 5.25] | national 's party | People's_National_Party |
| 779. | three | 45: [31, 5.17] | three 's two | One,_Two,_Three |
| 780. | mexican | 3: [10, 5.0] | mexican mexico 's | History_of_Mexico |
| 781. | opposition | 5: [10, 5.0] | opposition 's party | Opposition_Party_(Southern_U.S.) |
| 782. | vietnam | 5: [10, 5.0] | vietnam flu 's | Hong_Kong_flu |
| 783. | west | 8: [10, 5.0], 37: [10, 5.0] | west bank 's | West_Bank |
| 784. | coalition | 8: [10, 5.0] | coalition 's party | National_Coalition_Party |
| 785. | head | 13: [10, 5.0], 17: [10, 5.0] | head 's world | Beavis_and_Butt-Head |
| 786. | far | 13: [10, 5.0] | far 's people | Far-right_politics |
| 787. | robert | 13: [10, 5.0] | robert 's mugabe | Robert_Mugabe |
| 788. | behind | 14: [10, 5.0] | behind 's world | Leave_the_World_Behind_(novel) |
| 789. | homes | 14: [10, 5.0] | homes gaza 's | 2014_Gaza_War |
| 790. | papal | 14: [15, 5.0] | papal pope 's | Papal_conclave |
| 791. | plans | 14: [10, 5.0] | plans 's world | Plan_S |
| 792. | rainier | 14: [10, 5.0] | rainier prince monaco | Rainier_III,_Prince_of_Monaco |
| 793. | crisis | 16: [10, 5.0] | crisis 's government | 2020_Thuringian_government_crisis |
| 794. | sought | 16: [10, 5.0] | sought 's united | United_States |
| 795. | chiefs | 17: [10, 5.0] | chiefs 's security | Joint_Chiefs_of_Staff |
| 796. | way | 17: [10, 5.0] | way 's world | That's_the_Way_of_the_World |
| 797. | seven | 17: [10, 5.0] | seven 's police | Police_Academy:_Mission_to_Moscow |
| 798. | soviet | 19: [15, 5.0] | soviet 's russia | Russian_Soviet_Federative_Socialist_Republic |
| 799. | cases | 22: [10, 5.0] | cases 's world | U.S._News_&_World_Report |
| 800. | airline | 22: [10, 5.0] | airline 's plane | ValuJet_Airlines |
| 801. | spokesman | 22: [15, 5.0] | spokesman 's world | Fabio_Lanzoni |
| 802. | western | 23: [15, 5.0] | western 's iraq | 2017_Western_Iraq_campaign |
| 803. | kofi | 24: [10, 5.0] | kofi annan united | Kofi_Annan |
| 804. | almost | 24: [10, 5.0] | almost 's police | The_Police |
| 805. | moderate | 24: [10, 5.0] | moderate 's party | Moderate_Party |
| 806. | egypt | 25: [10, 5.0] | egypt 's egyptian | Egyptians |
| 807. | strip | 26: [10, 5.0], 52: [10, 5.0] | strip gaza palestinian | Gaza_Strip |
| 808. | facing | 26: [10, 5.0] | facing 's president | Harry_S._Truman |
| 809. | attackers | 28: [10, 5.0] | attackers police london | 2017_London_Bridge_attack |
| 810. | filmmaker | 28: [10, 5.0] | filmmaker dutch killing | Agnieszka_Holland |
| 811. | real | 28: [10, 5.0] | real 's world | The_Real_World:_Austin |
| 812. | arms | 28: [10, 5.0] | arms 's nuclear | Nuclear_arms_race |
| 813. | kenya | 28: [10, 5.0] | kenya 's africa | Kenya |
| 814. | suspect | 29: [25, 5.0] | suspect police 's | Prime_Suspect |
| 815. | peacekeepers | 29: [10, 5.0] | peacekeepers 's united | United_Nations_peacekeeping |
| 816. | joint | 30: [10, 5.0] | joint 's would | Sacroiliac_joint |
| 817. | another | 30: [15, 5.0] | another 's world | Another_World_(TV_series) |
| 818. | politics | 30: [10, 5.0] | politics 's political | Politics |
| 819. | response | 31: [10, 5.0] | response 's israel | Israel |
| 820. | corn | 32: [10, 5.0] | corn mexico 's | Corn_smut |
| 821. | gazans | 33: [10, 5.0] | gazans palestinian israeli | 2014_Gaza_War |
| 822. | resistance | 33: [10, 5.0] | resistance 's gaza | Hamas |
| 823. | later | 33: [10, 5.0] | later 's mr. | Toyota_MR2 |
| 824. | ships | 33: [10, 5.0] | ships 's china | List_of_Republic_of_China_Navy_ships |
| 825. | move | 35: [10, 5.0] | move 's government | MOVE |
| 826. | jerusalem | 35: [10, 5.0] | jerusalem israel israeli | United_States_recognition_of_Jerusalem_as_capital_of_Israel |
| 827. | killings | 38: [10, 5.0] | killings 's police | Encounter_killings_by_police |
| 828. | rejected | 38: [15, 5.0] | rejected 's mr. | List_of_Mr._Men |
| 829. | used | 40: [10, 5.0] | used 's police | Police_firearm_use_by_country |
| 830. | future | 40: [10, 5.0] | future 's talks | Future_(rapper) |
| 831. | russia | 41: [20, 5.0] | russia 's russian | Russia |
| 832. | received | 41: [10, 5.0] | received 's world | The_World's_Billionaires |
| 833. | storm | 42: [10, 5.0] | storm 's palestinian | Palestinian_Legislative_Council |
| 834. | documents | 43: [10, 5.0] | documents 's program | United_States_Federal_Witness_Protection_Program |
| 835. | toll | 43: [10, 5.0] | toll death people | List_of_wars_and_anthropogenic_disasters_by_death_toll |
| 836. | groups | 43: [10, 5.0] | groups 's government | Federal_government_of_the_United_States |
| 837. | projects | 45: [10, 5.0] | projects 's world | List_of_German_aircraft_projects,_1939–45 |
| 838. | uganda | 47: [10, 5.0] | uganda 's africa | Uganda |
| 839. | rare | 48: [10, 5.0] | rare 's government | Rare-earth_element |
| 840. | today | 49: [20, 5.0] | today 's iraq | Iraq_Today |
| 841. | organization | 49: [10, 5.0] | organization world 's | World_Health_Organization |
| 842. | spending | 50: [10, 5.0] | spending 's government | Government_spending |
| 843. | malawi | 50: [10, 5.0] | malawi 's africa | Malawi |
| 844. | obituary | 51: [10, 5.0] | obituary u.s. chirac | Jacques_Chirac |
| 845. | domestic | 51: [10, 5.0] | domestic 's say | Domestic_terrorism |
| 846. | changes | 51: [10, 5.0] | changes 's united | United_States |
| 847. | rule | 51: [10, 5.0] | rule 's court | Merrick_Garland_Supreme_Court_nomination |
| 848. | ukraine | 52: [10, 5.0] | ukraine 's yushchenko | Viktor_Yushchenko |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | press | 1: [13, inf] | press review ... | Press_review |
| 2. | review | 1: [14, inf] | review press ... | Chicago_Review_Press |
| 3. | thailand | 4: [11, inf] | thailand g tsunami | 2004_Indian_Ocean_earthquake_and_tsunami |
| 4. | lebanon | 9: [10, inf] | lebanon syria press | Mandate_for_Syria_and_the_Lebanon |
| 5. | people | 14: [12, inf] | people 's say | What_Will_People_Say |
| 6. | brief | 1: [12, 12.0] | brief news international | Sky_News |
| 7. | france | 45: [12, 12.0] | france 's may | May_68 |
| 8. | g | 27: [11, 11.0] | g tsunami summit | 2011_Tōhoku_earthquake_and_tsunami |
| 9. | us | 9: [15, 5.0], 44: [10, 10.0] | us iraq 's | 2003_invasion_of_Iraq |
| 10. | boycott | 21: [10, 10.0] | boycott israeli vote | Boycotts_of_Israel |
| 11. | pope | 13: [24, 8.0], 16: [25, 5.0] | pope 's vatican | Pope_John_Paul_I_conspiracy_theories |
| 12. | 's | 1: [17, 5.67] | 's letters iraq | Iraq–United_States_relations |
