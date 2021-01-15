# Keywords with the highest 'interestingness' in 2002

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
| 1. | singapore | 2: [16, inf], 4: [14, 7.0] | singapore qaeda indonesia | Jemaah_Islamiyah |
| 2. | speech | 2: [23, inf], 14: [22, 22.0], 26: [33, 6.6], 32: [17, inf] | speech 's bush | Mission_Accomplished_speech |
| 3. | nation | 2: [16, inf], 35: [11, 11.0] | nation 's function | List_of_specialized_agencies_of_the_United_Nations |
| 4. | day | 2: [10, inf], 45: [12, 6.0] | day 's israeli | Independence_Day_(Israel) |
| 5. | saint | 2: [10, inf] | saint 's pope | Pope_Pius_X |
| 6. | laurent | 2: [10, inf] | laurent saint french | Yves_Saint_Laurent_(designer) |
| 7. | mr. | 2: [19, inf], 24: [18, inf], 29: [10, inf], 40: [10, inf], 46: [17, 17.0], 49: [12, inf] | mr. 's world | Toyota_MR2 |
| 8. | gaza | 2: [19, 9.5], 16: [11, inf], 19: [36, inf], 30: [16, 8.0], 39: [23, 23.0], 41: [19, 19.0] | gaza israeli palestinian | Gaza_War_(2008–2009) |
| 9. | turkey | 2: [16, 8.0], 18: [11, inf], 40: [15, 7.5], 44: [15, 5.0] | turkey 's iraq | Iraq–Turkey_relations |
| 10. | building | 2: [12, inf] | building 's palestinian | Palestinian_Legislative_Council |
| 11. | terror | 2: [12, inf], 19: [15, inf] | terror 's bush | War_on_terror |
| 12. | issued | 2: [12, inf], 46: [14, 14.0] | issued 's says | Say_Say_Say |
| 13. | general | 2: [10, 10.0], 36: [11, inf], 43: [15, inf] | general 's iraq | Iraq_War |
| 14. | saying | 2: [14, 7.0], 42: [11, inf] | saying 's bush | George_W._Bush |
| 15. | nuclear | 2: [37, inf], 31: [21, 5.25], 34: [10, 5.0], 42: [38, 5.43] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 16. | protest | 2: [10, 10.0], 28: [12, inf], 35: [10, 5.0] | protest 's world | Protest |
| 17. | airport | 2: [17, 8.5], 49: [11, inf] | airport american 's | List_of_busiest_airports_by_passenger_traffic |
| 18. | plane | 2: [18, inf], 16: [14, inf], 48: [17, 5.67] | plane 's crash | Lynyrd_Skynyrd_plane_crash |
| 19. | visit | 2: [10, inf], 30: [12, 6.0], 42: [13, 6.5], 49: [15, 5.0] | visit 's bush | George_W._Bush |
| 20. | aboard | 2: [10, inf] | aboard plane crash | Germanwings_Flight_9525 |
| 21. | vatican | 2: [11, inf], 42: [11, inf] | vatican pope church | Second_Vatican_Council |
| 22. | power | 2: [10, inf] | power 's government | Federal_government_of_the_United_States |
| 23. | cuba | 2: [10, inf], 19: [15, 7.5], 38: [12, inf] | cuba 's prisoners | Cuban_Five |
| 24. | sec | 2: [10, inf], 11: [11, 5.5] | sec 's says | U.S._Securities_and_Exchange_Commission |
| 25. | catholic | 2: [10, inf], 46: [10, 5.0] | catholic church 's | Catholic_Church |
| 26. | colombia | 2: [12, inf], 5: [13, 6.5] | colombia rebels 's | Revolutionary_Armed_Forces_of_Colombia |
| 27. | pastrana | 2: [15, inf], 8: [11, inf] | pastrana rebels colombia | Revolutionary_Armed_Forces_of_Colombia |
| 28. | zone | 2: [12, inf], 48: [11, 11.0] | zone 's north | Eastern_Time_Zone |
| 29. | colin | 2: [10, inf], 14: [21, 7.0], 36: [17, 17.0], 51: [10, 10.0] | colin powell 's | Colin_Powell |
| 30. | powell | 2: [12, inf], 14: [27, 9.0], 36: [26, 26.0], 51: [18, 18.0] | powell 's bush | Colin_Powell |
| 31. | home | 2: [10, inf] | home 's photo | Photo_Booth |
| 32. | fashion | 3: [12, inf], 11: [11, 5.5], 41: [16, 8.0] | fashion 's luxury | Italian_fashion |
| 33. | schools | 3: [18, 9.0], 44: [12, inf], 47: [13, 6.5] | schools 's government | Federal_government_of_the_United_States |
| 34. | jerusalem | 3: [11, inf], 25: [21, 10.5], 31: [25, 12.5] | jerusalem israeli palestinian | East_Jerusalem |
| 35. | town | 3: [13, inf] | town 's israeli | List_of_cities_in_Israel |
| 36. | jewish | 3: [10, inf], 14: [11, 5.5], 22: [10, 10.0], 43: [20, 10.0] | jewish israeli palestinian | Israeli–Palestinian_conflict |
| 37. | book | 3: [12, inf] | book 's photo | Photo-book |
| 38. | haiti | 3: [10, inf], 36: [10, 10.0] | haiti 's aristide | Jean-Bertrand_Aristide |
| 39. | opium | 3: [10, inf] | opium 's afghanistan | Opium_production_in_Afghanistan |
| 40. | return | 4: [10, 5.0], 9: [12, inf], 12: [18, 6.0] | return 's iraq | Iraq_War |
| 41. | raid | 4: [16, 5.33], 39: [13, inf] | raid israeli 's | Raid_on_Entebbe_(film) |
| 42. | arabia | 4: [12, 6.0], 25: [10, inf], 38: [11, inf] | arabia saudi 's | Saudi_Arabia |
| 43. | congress | 4: [10, 5.0], 6: [10, inf], 9: [10, inf], 35: [15, 15.0] | congress 's bush | Cori_Bush |
| 44. | muslims | 4: [11, 5.5], 9: [17, 8.5], 18: [12, inf] | muslims 's muslim | Muslims |
| 45. | bomber | 4: [11, inf] | bomber suicide israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 46. | arms | 4: [15, 7.5], 9: [14, 14.0], 23: [11, inf] | arms iraq 's | Coat_of_arms_of_Iraq |
| 47. | ago | 4: [10, inf], 30: [10, 5.0] | ago 's years | All_Those_Years_Ago |
| 48. | district | 4: [10, inf] | district 's killed | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 49. | main | 5: [10, inf] | main 's government | Federal_government_of_the_United_States |
| 50. | captives | 5: [16, inf] | captives prisoners 's | List_of_Guantanamo_Bay_detainees |
| 51. | message | 5: [22, inf] | message 's bush | Marvin_Bush |
| 52. | pearl | 5: [33, 16.5], 17: [27, inf] | pearl pakistan reporter | Mariane_Pearl |
| 53. | militant | 5: [10, 5.0], 9: [10, 5.0], 17: [13, inf] | militant 's pakistan | Insurgency_in_Khyber_Pakhtunkhwa |
| 54. | york | 5: [21, 10.5], 16: [28, inf] | york function 's | Riemann_zeta_function |
| 55. | policy | 5: [21, 5.25], 14: [14, 7.0], 49: [11, inf] | policy 's bush | Foreign_policy_of_the_George_W._Bush_administration |
| 56. | office | 5: [10, 5.0], 8: [20, 5.0], 43: [10, inf] | office 's government | Government_Accountability_Office |
| 57. | outside | 5: [11, 5.5], 12: [12, 6.0], 24: [11, 11.0], 38: [12, inf], 43: [11, 5.5], 49: [13, inf] | outside 's government | Federal_government_of_the_United_States |
| 58. | school | 5: [11, inf], 9: [15, 5.0], 17: [18, inf], 42: [18, 9.0], 49: [11, inf] | school 's children | Professional_Children's_School |
| 59. | journalists | 5: [11, 11.0], 13: [13, inf] | journalists 's government | List_of_journalists_killed_in_Europe |
| 60. | mugabe | 5: [11, inf], 33: [12, inf] | mugabe zimbabwe 's | Robert_Mugabe |
| 61. | 'axis | 5: [14, inf] | 'axis bush 's | Axis_of_evil |
| 62. | swiss | 5: [10, 10.0], 27: [23, inf] | swiss switzerland 's | Demographics_of_Switzerland |
| 63. | politicians | 5: [10, inf] | politicians 's government | List_of_foreign-born_United_States_politicians |
| 64. | koizumi | 5: [10, inf] | koizumi japan 's | Junichiro_Koizumi |
| 65. | abuse | 5: [10, inf], 43: [18, inf] | abuse 's priests | Catholic_Church_sexual_abuse_cases |
| 66. | dept | 5: [10, inf] | dept 's state | United_States_Department_of_State |
| 67. | intelligence | 6: [24, 6.0], 18: [11, inf] | intelligence 's officials | William_Binney_(intelligence_official) |
| 68. | ends | 6: [13, 6.5], 16: [10, inf], 36: [10, inf] | ends 's world | It's_the_End_of_the_World |
| 69. | musharraf | 6: [13, inf], 17: [11, inf], 22: [19, 9.5], 33: [13, 13.0] | musharraf pakistan 's | Pervez_Musharraf |
| 70. | kashmir | 6: [12, 6.0], 20: [15, inf], 29: [19, 6.33], 37: [12, 6.0], 51: [14, 14.0] | kashmir india pakistan | Kashmir |
| 71. | missing | 6: [14, inf], 49: [12, 6.0] | missing 's dead | The_Missing_and_the_Dead |
| 72. | heisenberg | 6: [12, inf] | heisenberg bohr 's | Niels_Bohr |
| 73. | bohr | 6: [12, inf] | bohr heisenberg 's | Niels_Bohr |
| 74. | sheikh | 6: [16, inf], 11: [16, 8.0], 17: [11, inf] | sheikh pearl pakistan | Daniel_Pearl |
| 75. | vaccine | 7: [10, 5.0], 13: [10, inf] | vaccine smallpox health | Smallpox_vaccine |
| 76. | saudi | 7: [14, 7.0], 9: [33, 8.25], 13: [29, 5.8], 25: [14, 7.0], 33: [17, inf], 38: [13, 13.0], 47: [31, 15.5] | saudi 's arabia | Saudi_Arabia |
| 77. | trial | 7: [28, inf], 17: [35, 5.83], 24: [28, 28.0], 40: [22, 7.33] | trial 's milosevic | Trial_of_Slobodan_Milošević |
| 78. | milosevic | 7: [40, inf], 18: [11, 5.5], 24: [10, inf], 30: [11, inf], 34: [10, inf], 39: [19, inf] | milosevic crimes trial | Trial_of_Slobodan_Milošević |
| 79. | slobodan | 7: [12, inf] | slobodan milosevic crimes | Trial_of_Slobodan_Milošević |
| 80. | yugoslavia | 7: [11, inf] | yugoslavia milosevic europe | Slobodan_Milošević |
| 81. | feb | 7: [12, inf] | feb 's government | Government_of_the_United_Kingdom |
| 82. | crimes | 7: [25, inf], 40: [10, 5.0], 49: [10, 10.0] | crimes milosevic trial | Trial_of_Slobodan_Milošević |
| 83. | kosovo | 7: [12, inf], 52: [11, inf] | kosovo milosevic crimes | Slobodan_Milošević |
| 84. | rockets | 7: [12, inf] | rockets israeli palestinian | Palestinian_rocket_attacks_on_Israel |
| 85. | border | 7: [10, 10.0], 21: [12, 12.0], 31: [13, inf] | border pakistan 's | India–Pakistan_border |
| 86. | budget | 7: [11, 5.5], 11: [11, 5.5], 44: [13, inf] | budget 's government | Government_budget |
| 87. | protests | 7: [10, inf] | protests 's government | Protest |
| 88. | genocide | 7: [14, inf] | genocide crimes trial | Genocide |
| 89. | serb | 7: [10, inf], 40: [11, 11.0] | serb crimes bosnian | Bosnian_War |
| 90. | falun | 7: [12, inf], 14: [12, inf] | falun gong china | Persecution_of_Falun_Gong |
| 91. | gong | 7: [12, inf], 14: [12, inf] | gong falun china | Persecution_of_Falun_Gong |
| 92. | nato | 7: [10, inf], 9: [21, 21.0], 17: [14, inf], 20: [18, 6.0], 35: [11, 5.5], 47: [57, 6.33] | nato 's bush | Major_non-NATO_ally |
| 93. | italy | 7: [12, 12.0], 16: [12, inf], 19: [15, inf], 38: [16, 5.33] | italy 's europe | Italy |
| 94. | kenya | 7: [10, inf], 48: [32, 8.0], 52: [12, inf] | kenya 's africa | Kenya |
| 95. | marxist | 8: [10, inf] | marxist rebels 's | Marxism–Leninism |
| 96. | rebel | 8: [21, inf], 15: [12, 6.0], 25: [12, inf] | rebel 's government | Rebellion |
| 97. | seven | 8: [10, inf], 10: [10, inf], 31: [10, 10.0] | seven 's israeli | Israel–United_States_relations |
| 98. | armed | 8: [10, inf], 15: [11, inf] | armed 's military | United_States_Armed_Forces |
| 99. | board | 8: [10, inf] | board 's plane | Plane_(tool) |
| 100. | overseas | 8: [11, inf] | overseas 's us | Territories_of_the_United_States |
| 101. | mexican | 8: [10, inf], 33: [12, 6.0], 43: [11, 11.0] | mexican mexico 's | History_of_Mexico |
| 102. | rumsfeld | 8: [11, 5.5], 13: [13, inf] | rumsfeld defense donald | Donald_Rumsfeld |
| 103. | train | 8: [12, inf] | train 's military | Military_marine_mammal |
| 104. | guerrilla | 8: [10, inf], 30: [14, 7.0] | guerrilla 's group | People's_Guerrilla_Group |
| 105. | colombian | 8: [12, inf] | colombian colombia rebels | Revolutionary_Armed_Forces_of_Colombia |
| 106. | hope | 9: [10, inf] | hope 's bush | Bush_family |
| 107. | case | 9: [17, 5.67], 16: [10, inf], 25: [19, 9.5], 35: [12, inf], 43: [17, 8.5], 45: [23, 11.5] | case 's say | Say_Say_Say |
| 108. | muslim | 9: [12, 12.0], 17: [10, inf] | muslim 's american | Islam_in_the_United_States |
| 109. | region | 9: [13, 6.5], 19: [14, inf] | region 's function | Riemann_zeta_function |
| 110. | hindu | 9: [17, inf], 18: [10, inf], 20: [11, 5.5], 39: [13, inf] | hindu india 's | Hindu_Mahasabha |
| 111. | demand | 9: [10, 5.0], 26: [13, inf], 38: [10, inf] | demand 's bush | George_W._Bush |
| 112. | soviet | 9: [15, 7.5], 22: [10, inf] | soviet 's russia | Russian_Soviet_Federative_Socialist_Republic |
| 113. | lake | 9: [11, inf] | lake 's city | Salt_Lake_City |
| 114. | calls | 9: [16, inf], 50: [11, 5.5] | calls 's bush | Bush_family |
| 115. | groups | 9: [22, inf], 15: [11, 5.5] | groups 's government | Federal_government_of_the_United_States |
| 116. | abdullah | 9: [13, 6.5], 17: [20, inf] | abdullah saudi 's | Abdullah_of_Saudi_Arabia |
| 117. | future | 9: [16, inf], 29: [11, 11.0], 47: [12, 6.0] | future 's says | Say's_law |
| 118. | quebec | 9: [10, inf] | quebec province 's | Quebec |
| 119. | arab | 9: [21, inf], 13: [61, 6.1], 46: [14, inf] | arab 's israeli | Arab–Israeli_conflict |
| 120. | idea | 9: [10, inf] | idea 's bush | George_H._W._Bush |
| 121. | opposition | 9: [17, 5.67], 36: [13, inf] | opposition 's government | Parliamentary_opposition |
| 122. | witnesses | 9: [10, inf] | witnesses 's israeli | Criticism_of_Jehovah's_Witnesses |
| 123. | georgia | 9: [26, inf], 33: [20, 10.0] | georgia russia 's | Russo-Georgian_War |
| 124. | dozens | 9: [10, inf] | dozens 's israeli | Israel |
| 125. | mosque | 9: [12, inf] | mosque 's people | Sheikh_Zayed_Mosque |
| 126. | dna | 9: [18, inf] | dna 's say | The_DNA_Will_Have_Its_Say |
| 127. | kong | 9: [10, 5.0], 12: [11, inf], 25: [15, inf] | kong hong 's | Hong_Kong |
| 128. | total | 10: [10, inf] | total 's military | Total_SE |
| 129. | strategy | 10: [10, inf], 38: [10, 5.0], 43: [11, 5.5] | strategy 's bush | Bush_Doctrine |
| 130. | egypt | 10: [11, inf] | egypt 's israel | Egypt–Israel_peace_treaty |
| 131. | voters | 10: [11, inf] | voters 's party | Political_party_strength_in_U.S._states |
| 132. | helicopter | 10: [11, inf], 34: [19, inf] | helicopter military crash | 2011_Afghanistan_Boeing_Chinook_shootdown |
| 133. | another | 10: [10, 10.0], 44: [14, 14.0], 46: [14, inf] | another 's says | Say's_law |
| 134. | vienna | 10: [10, inf] | vienna 's united | Vienna |
| 135. | uterus | 10: [12, inf] | uterus transplant say | Organ_transplantation |
| 136. | design | 11: [10, inf] | design fashion 's | Fashion_design |
| 137. | march | 11: [11, 5.5], 14: [12, inf] | march 's israeli | Nuclear_weapons_and_Israel |
| 138. | press | 11: [10, inf], 13: [12, inf], 37: [15, 7.5] | press 's bush | George_W._Bush |
| 139. | korean | 11: [11, 5.5], 26: [22, 22.0], 47: [20, inf] | korean north korea | North_Korea–South_Korea_relations |
| 140. | camp | 11: [16, 5.33], 15: [20, inf], 22: [16, 8.0], 39: [22, 22.0], 48: [20, 5.0] | camp israeli palestinian | 2000_Camp_David_Summit |
| 141. | civilians | 11: [12, inf], 29: [14, 14.0], 33: [10, inf] | civilians israeli palestinian | 2006_Israeli_operation_in_Beit_Hanoun |
| 142. | yemen | 11: [14, inf], 41: [10, inf], 45: [14, inf] | yemen qaeda american | Al-Qaeda_insurgency_in_Yemen |
| 143. | begin | 11: [10, inf], 20: [10, 5.0], 34: [12, 6.0] | begin 's bush | George_W._Bush |
| 144. | montenegro | 11: [10, inf] | montenegro serbia yugoslavia | Serbia_and_Montenegro |
| 145. | monterrey | 12: [24, inf] | monterrey mexico aid | Mexico |
| 146. | labor | 12: [22, inf], 15: [11, inf], 28: [11, 5.5], 40: [11, 5.5], 44: [18, 9.0] | labor 's party | Minnesota_Democratic–Farmer–Labor_Party |
| 147. | list | 12: [10, inf] | list 's says | Say's_law |
| 148. | summit | 12: [10, 5.0], 35: [26, inf] | summit 's meeting | Summit_(meeting) |
| 149. | peru | 12: [15, inf] | peru 's pres | Pre-Columbian_Peru |
| 150. | seen | 12: [11, inf] | seen 's iraq | Iraq_War |
| 151. | tax | 12: [10, inf] | tax 's government | List_of_countries_by_tax_rates |
| 152. | arabs | 13: [22, inf] | arabs israeli israel | Arab_citizens_of_Israel |
| 153. | quake | 13: [10, inf] | quake earthquake people | 1994_Northridge_earthquake |
| 154. | polish | 13: [12, inf] | polish poland paetz | Juliusz_Paetz |
| 155. | paetz | 13: [10, inf] | paetz polish pope | Pope_John_Paul_II |
| 156. | young | 13: [10, inf], 27: [10, 5.0] | young 's people | Young_People_Fucking |
| 157. | turmoil | 13: [11, inf] | turmoil 's government | S._Venkitaramanan |
| 158. | iraq | 13: [27, 5.4], 27: [10, inf], 31: [50, 5.0] | iraq 's bush | George_W._Bush |
| 159. | challenged | 13: [16, inf], 16: [21, inf] | challenged function purl | Permalink |
| 160. | smallpox | 13: [10, inf] | smallpox health vaccine | Smallpox_vaccine |
| 161. | jews | 14: [17, 5.67], 22: [12, inf] | jews 's jewish | American_Jews |
| 162. | bethlehem | 14: [21, inf], 34: [13, 13.0] | bethlehem israeli palestinian | Bethlehem |
| 163. | abu | 14: [15, 7.5], 34: [12, inf], 38: [10, 10.0] | abu american philippines | Abu_Sayyaf |
| 164. | opponents | 14: [10, inf] | opponents 's government | Divided_government_in_the_United_States |
| 165. | church | 14: [34, 6.8], 28: [11, inf], 30: [10, inf], 43: [12, 6.0], 46: [17, inf] | church 's israeli | Church_of_Israel |
| 166. | streets | 14: [12, inf] | streets 's government | Federal_government_of_the_United_States |
| 167. | job | 14: [15, inf] | job 's photo | Steve_Jobs |
| 168. | statement | 14: [14, inf], 49: [12, inf] | statement 's says | Mission_statement |
| 169. | vehicles | 14: [12, inf] | vehicles israeli 's | Vehicle_registration_plates_of_Israel |
| 170. | crisis | 14: [21, 10.5], 20: [13, 13.0], 32: [10, inf] | crisis 's bush | Savings_and_loan_crisis |
| 171. | synagogue | 14: [10, inf] | synagogue tunisia attack | Ghriba_synagogue_bombing |
| 172. | gunmen | 14: [14, inf] | gunmen israeli palestinian | 2010_Palestinian_militancy_campaign |
| 173. | defendants | 14: [10, inf] | defendants trial court | Chicago_Seven |
| 174. | sweep | 14: [15, inf] | sweep israeli 's | Israel |
| 175. | northern | 14: [16, inf] | northern 's ireland | Northern_Ireland |
| 176. | union | 14: [14, inf], 33: [12, 12.0], 35: [24, 8.0], 40: [18, 9.0], 50: [50, 6.25] | union european 's | European_Union |
| 177. | put | 14: [13, inf] | put 's bush | George_H._W._Bush |
| 178. | parts | 14: [10, inf] | parts 's israeli | Israel |
| 179. | venezuela | 15: [35, inf] | venezuela chavez 's | Hugo_Chávez |
| 180. | company | 15: [12, 6.0], 38: [11, inf] | company 's oil | Shell_Oil_Company |
| 181. | hugo | 15: [15, inf] | hugo chavez venezuela | Hugo_Chávez |
| 182. | chavez | 15: [26, inf], 33: [12, inf] | chavez venezuela 's | Hugo_Chávez |
| 183. | business | 15: [17, inf], 37: [10, 10.0] | business 's function | Business_process |
| 184. | battle | 15: [14, inf], 21: [14, 14.0] | battle 's american | List_of_American_Civil_War_battles |
| 185. | sri | 15: [10, inf], 38: [10, inf] | sri lanka tamil | Sri_Lankan_Tamils |
| 186. | refugees | 15: [12, inf], 39: [14, 7.0], 50: [14, 7.0] | refugees 's north | North_Korean_defectors |
| 187. | bus | 15: [14, inf], 23: [10, inf], 25: [14, inf], 29: [17, inf], 41: [10, inf], 43: [20, inf] | bus israeli suicide | Dizengoff_Street_bus_bombing |
| 188. | dutch | 15: [10, inf], 19: [19, inf] | dutch netherlands fortuyn | Pim_Fortuyn |
| 189. | barakaat | 15: [10, inf] | barakaat 's somalia | Al-Barakat |
| 190. | coup | 16: [22, inf] | coup 's chavez | 1992_Venezuelan_coup_d'état_attempts |
| 191. | surrender | 16: [11, inf] | surrender 's says | Battle_of_Appomattox_Court_House |
| 192. | clear | 16: [11, 11.0], 21: [11, inf] | clear 's bush | George_H._W._Bush |
| 193. | died | 16: [17, 5.67], 44: [14, inf] | died 's say | Never_Say_Die! |
| 194. | votes | 16: [10, inf] | votes 's party | Party-line_vote |
| 195. | weather | 16: [26, inf] | weather function purl | Clear_Lake_(California) |
| 196. | greece | 16: [10, inf], 30: [12, 6.0] | greece europe world | Greece |
| 197. | settlement | 16: [12, inf], 29: [12, 6.0] | settlement israeli palestinian | 2010–11_Israeli–Palestinian_peace_talks |
| 198. | science | 16: [22, inf] | science function purl | Persistent_uniform_resource_locator |
| 199. | titl | 16: [21, inf], 36: [21, 7.0] | titl | G-Eazy |
| 200. | function | 16: [63, inf] | function purl features | Permalink |
| 201. | pop_me_up | 16: [21, inf] | pop_me_up function purl | Happy_Days |
| 202. | purl | 16: [42, inf] | purl function features | Permalink |
| 203. | new_window | 16: [21, inf] | new_window function purl | Happy_Days |
| 204. | window.open | 16: [21, inf] | window.open function purl | Office_Open_XML_file_formats |
| 205. | popup_window | 16: [21, inf] | popup_window function purl | EMPTY MATCHING |
| 206. | new_window.focus | 16: [21, inf] | new_window.focus function purl | Happy_Days |
| 207. | changeimage | 16: [21, inf] | changeimage function purl | EMPTY MATCHING |
| 208. | image_name | 16: [42, inf] | image_name function purl | Permalink |
| 209. | image_src | 16: [42, inf] | image_src function purl | EPUB |
| 210. | document.images | 16: [21, inf] | document.images function purl | Office_Open_XML_file_formats |
| 211. | .src | 16: [21, inf] | .src function purl | EPUB |
| 212. | mm_jumpmenu | 16: [21, inf] | mm_jumpmenu function purl | EMPTY MATCHING |
| 213. | targ | 16: [21, inf] | targ function purl | EMPTY MATCHING |
| 214. | selobj | 16: [21, inf] | selobj function purl | EMPTY MATCHING |
| 215. | restore | 16: [42, inf] | restore function purl | Persistent_uniform_resource_locator |
| 216. | //v.eval | 16: [21, inf] | //v.eval function purl | Bosnia_and_Herzegovina |
| 217. | targ+ | 16: [21, inf] | targ+ function purl | EMPTY MATCHING |
| 218. | .location= | 16: [21, inf] | .location= function purl | Persistent_uniform_resource_locator |
| 219. | +selobj.options | 16: [21, inf] | +selobj.options function purl | EMPTY MATCHING |
| 220. | selobj.selectedindex | 16: [21, inf] | selobj.selectedindex function purl | EMPTY MATCHING |
| 221. | .value+ | 16: [21, inf] | .value+ function purl | Persistent_uniform_resource_locator |
| 222. | selobj.selectedindex= | 16: [21, inf] | selobj.selectedindex= function purl | EMPTY MATCHING |
| 223. | // | 16: [21, inf] | // function purl | Permalink |
| 224. | technology | 16: [21, inf] | technology function purl | Persistent_uniform_resource_locator |
| 225. | education | 16: [21, inf] | education function purl | Charlotte_of_Mecklenburg-Strelitz |
| 226. | obituaries | 16: [21, inf] | obituaries function purl | Stanford_University |
| 227. | page | 16: [21, inf] | page function purl | Permalink |
| 228. | corrections | 16: [21, inf] | corrections function purl | Portugal |
| 229. | editorials/op-ed | 16: [21, inf] | editorials/op-ed function purl | EMPTY MATCHING |
| 230. | readers | 16: [21, inf] | readers function purl | EPUB |
| 231. | opinions | 16: [21, inf] | opinions function purl | Paolo_Sarpi |
| 232. | pen | 17: [52, 10.4], 23: [15, inf] | pen french chirac | 2002_French_presidential_election |
| 233. | local | 17: [18, inf], 20: [11, inf] | local 's officials | Official |
| 234. | pakistan | 17: [22, inf] | pakistan 's india | India–Pakistan_relations |
| 235. | argentine | 17: [15, inf] | argentine 's argentina | Argentina |
| 236. | argentina | 17: [12, inf] | argentina 's duhalde | Eduardo_Duhalde |
| 237. | eduardo | 17: [11, inf] | eduardo argentina duhalde | Eduardo_Duhalde |
| 238. | duhalde | 17: [16, inf] | duhalde argentina 's | Eduardo_Duhalde |
| 239. | immigration | 17: [15, 5.0], 25: [23, inf] | immigration 's immigrants | Illegal_immigration_to_the_United_States |
| 240. | success | 17: [11, inf] | success 's says | NXIVM |
| 241. | rightist | 17: [18, 9.0], 32: [14, inf] | rightist 's pen | Anti-Rightist_Campaign |
| 242. | chirac | 17: [22, 5.5], 29: [11, inf] | chirac france jacques | Jacques_Chirac |
| 243. | guilty | 17: [17, inf], 40: [10, inf] | guilty world briefing | Stephanie_Grisham |
| 244. | reporter | 17: [18, inf], 29: [11, 5.5] | reporter pearl 's | Daniel_Pearl |
| 245. | daniel | 17: [12, inf] | daniel pearl 's | Daniel_Pearl |
| 246. | viagra | 17: [10, inf] | viagra china shenzhen | 2013_Summer_Universiade |
| 247. | member | 17: [15, inf], 22: [10, 5.0] | member 's say | Say_Say_Say |
| 248. | free | 17: [13, 6.5], 38: [12, inf] | free 's says | Say's_law |
| 249. | suspended | 17: [10, inf] | suspended world briefing | Stephanie_Grisham |
| 250. | castro | 17: [14, inf] | castro cuba 's | Cuban_Revolution |
| 251. | fox | 17: [13, inf] | fox mexico 's | Vicente_Fox |
| 252. | crown | 17: [16, inf] | crown saudi bush | Abdullah_of_Saudi_Arabia |
| 253. | good | 17: [12, inf] | good 's photo | Google_Photos |
| 254. | evicted | 17: [12, inf] | evicted palestinians says | Palestinians |
| 255. | nepal | 17: [14, inf], 40: [15, inf] | nepal rebels asia | Nepalese_Civil_War |
| 256. | pakistani | 17: [11, 5.5], 31: [12, 6.0], 37: [10, 5.0], 44: [10, inf], 47: [10, 5.0] | pakistani pakistan 's | Pakistanis |
| 257. | shooting | 17: [10, inf] | shooting israeli 's | Stoneman_Douglas_High_School_shooting |
| 258. | n't | 18: [10, inf] | n't 's says | T.N.T._(album) |
| 259. | journalist | 18: [11, inf] | journalist 's pearl | Daniel_Pearl |
| 260. | research | 18: [10, inf] | research 's says | Say's_law |
| 261. | wins | 18: [10, inf] | wins 's party | WIN_Party |
| 262. | raffarin | 19: [10, inf] | raffarin chirac jean-pierre | Jean-Pierre_Raffarin |
| 263. | fortuyn | 19: [11, inf] | fortuyn dutch pim | Pim_Fortuyn |
| 264. | burma | 19: [10, inf] | burma government envoy | Saffron_Revolution |
| 265. | hamas | 19: [11, inf], 41: [13, inf] | hamas palestinian israeli | Hamas |
| 266. | asylum | 19: [10, inf], 36: [12, inf] | asylum north seekers | Asylum_seeker |
| 267. | session | 19: [14, inf] | session 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 268. | assembly | 19: [13, inf] | assembly 's government | Victoria_State_Government |
| 269. | carter | 20: [36, 6.0], 41: [15, inf], 50: [14, inf] | carter 's pres | Jay-Z |
| 270. | terrorist | 20: [16, inf], 25: [12, 12.0], 29: [12, 12.0], 41: [24, 12.0] | terrorist 's attacks | September_11_attacks |
| 271. | putin | 20: [12, 6.0], 34: [29, inf], 40: [22, 11.0], 43: [14, inf] | putin russia pres | Russian_interference_in_the_2016_United_States_elections |
| 272. | independent | 20: [11, inf] | independent 's says | Say's_law |
| 273. | prison | 20: [10, inf] | prison 's years | Prison |
| 274. | every | 20: [12, inf] | every 's government | Federal_government_of_the_United_States |
| 275. | basra | 20: [12, inf] | basra 's pakistan | Riaz_Basra |
| 276. | reform | 20: [13, inf] | reform 's palestinian | 2006_Palestinian_legislative_election |
| 277. | rape | 20: [10, inf] | rape 's charges | Mahmudiyah_rape_and_killings |
| 278. | medicine | 20: [10, inf] | medicine 's israeli | Healthcare_in_Israel |
| 279. | brazil | 20: [10, inf], 27: [10, 5.0], 48: [10, 10.0] | brazil 's world | Brazil_v_Germany_(2014_FIFA_World_Cup) |
| 280. | hair | 20: [13, inf] | hair 's schroder | Ricky_Schroder |
| 281. | weisfeiler | 20: [12, inf] | weisfeiler state 's | Boris_Weisfeiler |
| 282. | israelis | 21: [11, inf] | israelis israeli palestinian | Israeli–Palestinian_conflict |
| 283. | whaling | 21: [19, inf] | whaling japan commission | International_Whaling_Commission |
| 284. | offshore | 21: [10, inf] | offshore 's oil | Oil_platform |
| 285. | funds | 21: [16, 16.0], 38: [14, inf], 51: [15, 7.5] | funds 's government | Federal_government_of_the_United_States |
| 286. | percent | 22: [11, 5.5], 28: [13, inf], 32: [13, 13.0], 35: [10, 5.0] | percent 's government | Federal_government_of_the_United_States |
| 287. | full | 22: [11, inf] | full 's iraq | Occupation_of_Iraq_(2003–2011) |
| 288. | aimed | 22: [10, inf] | aimed 's government | Top_100_Contractors_of_the_U.S._federal_government |
| 289. | anti-semitism | 22: [10, inf] | anti-semitism jewish 's | Antisemitism |
| 290. | raids | 22: [10, inf] | raids israeli 's | 1968_Israeli_raid_on_Lebanon |
| 291. | official | 22: [13, inf], 33: [14, 7.0] | official 's says | Say_Say_Say |
| 292. | nablus | 22: [17, inf], 31: [14, inf] | nablus israeli palestinian | Nablus |
| 293. | week | 22: [13, inf], 27: [10, 5.0], 46: [11, 11.0] | week 's bush | George_H._W._Bush |
| 294. | point | 22: [13, inf] | point 's american | United_States |
| 295. | problem | 22: [10, inf] | problem 's says | Scunthorpe_problem |
| 296. | zimbabwe | 22: [12, inf], 37: [10, 5.0] | zimbabwe mugabe 's | Robert_Mugabe |
| 297. | efforts | 23: [11, 11.0], 25: [11, inf], 29: [11, 5.5] | efforts 's bush | Efforts_to_impeach_George_W._Bush |
| 298. | french | 23: [12, inf], 37: [10, 5.0], 41: [22, 7.33] | french france 's | France |
| 299. | guerrillas | 23: [12, 12.0], 43: [19, inf] | guerrillas 's rebels | Guerrilla_warfare |
| 300. | farm | 24: [10, inf] | farm 's subsidies | Agricultural_subsidy |
| 301. | bomb | 24: [16, 8.0], 36: [14, inf] | bomb 's israeli | Nuclear_weapons_and_Israel |
| 302. | suspect | 24: [13, inf], 27: [16, 5.33] | suspect 's police | Prime_Suspect |
| 303. | mandela | 24: [10, inf] | mandela africa south | Nelson_Mandela |
| 304. | ban | 24: [12, inf], 51: [12, inf] | ban 's world | Ban_Ki-moon |
| 305. | karzai | 24: [10, inf], 30: [10, 10.0] | karzai afghanistan afghan | Politics_of_Afghanistan |
| 306. | threats | 24: [11, inf] | threats 's iraq | Iraq_War |
| 307. | threat | 24: [11, 5.5], 32: [14, inf] | threat 's iraq | Iraq_War |
| 308. | plant | 24: [12, inf], 48: [14, inf], 52: [14, 7.0] | plant nuclear 's | Chernobyl_Nuclear_Power_Plant |
| 309. | mexico | 25: [11, inf], 31: [19, inf], 33: [13, 6.5], 41: [10, 5.0], 48: [23, inf] | mexico 's mexican | Crime_in_Mexico |
| 310. | prosecution | 25: [11, inf] | prosecution court 's | Prosecutor |
| 311. | legal | 25: [10, inf] | legal 's court | Court_dress |
| 312. | land | 25: [13, 6.5], 27: [15, inf] | land 's israeli | Land_of_Israel |
| 313. | ouster | 26: [14, inf] | ouster 's bush | Cori_Bush |
| 314. | violence | 26: [11, inf] | violence 's israeli | Israeli_settler_violence |
| 315. | chile | 26: [10, inf] | chile 's trade | Economy_of_Chile |
| 316. | suit | 26: [10, inf] | suit 's american | Suit |
| 317. | starts | 26: [10, inf] | starts 's world | The_World_Starts_Tonight |
| 318. | removal | 26: [11, inf] | removal 's bush | George_W._Bush |
| 319. | secret | 27: [12, inf] | secret 's nuclear | Nuclear_Secrets |
| 320. | peacekeeping | 27: [12, inf] | peacekeeping force 's | United_Nations_peacekeeping |
| 321. | code | 27: [10, inf] | code 's legal | Philippine_legal_codes |
| 322. | czech | 27: [10, inf], 33: [10, inf], 43: [17, 17.0] | czech republic europe | Czech_Republic |
| 323. | republic | 27: [12, inf], 43: [10, 10.0] | republic 's czech | Czech_Republic |
| 324. | settlements | 27: [10, inf] | settlements israeli says | Israeli_settlement |
| 325. | flight | 27: [11, inf], 35: [11, inf] | flight say air | Lion_Air_Flight_610 |
| 326. | paid | 27: [11, inf] | paid 's says | Say's_law |
| 327. | collision | 27: [19, inf] | collision crash air | Mid-air_collision |
| 328. | aids | 27: [20, 20.0], 46: [11, inf] | aids 's africa | HIV/AIDS_in_Africa |
| 329. | africa | 27: [12, inf], 46: [29, 5.8] | africa world 's | South_Africa |
| 330. | conviction | 28: [12, inf] | conviction 's court | Conviction |
| 331. | soon | 28: [16, inf] | soon 's says | Say_This_Sooner |
| 332. | marijuana | 28: [10, inf] | marijuana 's use | Cannabis_use_disorder |
| 333. | factory | 29: [11, inf] | factory 's workers | Workers'_self-management |
| 334. | month | 29: [11, inf] | month 's last | The_Last_Month_of_the_Year |
| 335. | call | 29: [11, inf], 43: [11, inf] | call 's bush | George_H._W._Bush |
| 336. | kill | 29: [10, inf] | kill israeli palestinian | Timeline_of_the_Israeli–Palestinian_conflict |
| 337. | different | 29: [10, inf] | different 's bush | Bush_family |
| 338. | growing | 29: [12, inf], 34: [11, 5.5], 39: [10, 10.0] | growing 's bush | George_H._W._Bush |
| 339. | suspects | 29: [12, inf] | suspects 's qaeda | Al-Qaeda |
| 340. | ambush | 29: [11, inf] | ambush israeli killed | Ansariya_ambush |
| 341. | agreement | 30: [13, inf] | agreement 's north | North_American_Free_Trade_Agreement |
| 342. | shehada | 30: [11, inf] | shehada hamas israeli | Hamas |
| 343. | menem | 30: [21, inf] | menem argentina pres | Argentina |
| 344. | taliban | 30: [10, inf], 41: [11, inf], 44: [16, 8.0] | taliban afghanistan qaeda | Taliban_insurgency |
| 345. | cease-fire | 30: [11, inf] | cease-fire israeli israel | Yom_Kippur_War |
| 346. | cafeteria | 31: [12, inf] | cafeteria bomb jerusalem | Propane_bomb |
| 347. | university | 31: [24, inf] | university 's students | Queen's_University_at_Kingston |
| 348. | japanese | 31: [12, inf] | japanese japan north | Japan |
| 349. | rejects | 31: [13, inf], 35: [11, inf], 44: [10, inf] | rejects 's pres | Pre-existence |
| 350. | invasion | 31: [10, inf] | invasion iraq 's | 2003_invasion_of_Iraq |
| 351. | campus | 31: [10, inf] | campus students attack | 2020_Jawaharlal_Nehru_University_attack |
| 352. | bombers | 32: [12, inf] | bombers israeli palestinian | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 353. | christian | 32: [18, inf], 39: [12, inf], 41: [13, 6.5] | christian 's church | Christian_Church |
| 354. | loan | 32: [10, inf] | loan 's billion | Savings_and_loan_crisis |
| 355. | money | 32: [12, inf] | money 's government | Fiat_money |
| 356. | web | 32: [10, inf] | web 's px | 500px |
| 357. | historic | 33: [10, inf] | historic 's photos | Donald_Trump_photo_op_at_St._John's_Church |
| 358. | prague | 33: [21, inf], 43: [16, 5.33] | prague nato czech | Prague |
| 359. | floods | 33: [14, inf] | floods europe 's | 2002_European_floods |
| 360. | georgian | 33: [10, inf] | georgian georgia russia | Russo-Georgian_War |
| 361. | timor | 33: [13, inf] | timor east indonesia | Indonesian_invasion_of_East_Timor |
| 362. | pope | 33: [23, inf] | pope john paul | Pope_John_Paul_II |
| 363. | john | 33: [14, inf] | john pope 's | Pope_John_Paul_II |
| 364. | suarez | 33: [10, inf] | suarez united mexico | Cecilia_Suárez |
| 365. | dresden | 33: [11, inf] | dresden floods germany | Dresden |
| 366. | nidal | 34: [11, inf] | nidal abu palestinian | Abu_Nidal |
| 367. | vladimir | 34: [20, 5.0], 40: [16, 8.0], 43: [11, inf] | vladimir putin russia | Russia_under_Vladimir_Putin |
| 368. | moscow | 34: [25, inf], 43: [30, 6.0] | moscow 's russia | Moscow |
| 369. | parliament | 34: [10, inf] | parliament 's world | Parliament_of_the_World's_Religions |
| 370. | apartment | 34: [10, inf] | apartment 's say | The_Apartment |
| 371. | embassy | 34: [11, inf] | embassy american north | List_of_diplomatic_missions_of_the_United_States |
| 372. | johannesburg | 35: [19, inf] | johannesburg world summit | Earth_Summit_2002 |
| 373. | sustainable | 35: [15, inf] | sustainable world summit | World_Sustainable_Development_Summit |
| 374. | trying | 35: [14, inf] | trying 's says | The_Try_Guys |
| 375. | already | 35: [13, inf] | already 's say | It's_Already_Written |
| 376. | dispute | 35: [11, inf], 45: [10, 5.0] | dispute 's united | China–United_States_trade_war |
| 377. | approval | 35: [10, inf] | approval 's iraq | British_Parliamentary_approval_for_the_invasion_of_Iraq |
| 378. | energy | 35: [10, inf], 52: [11, inf] | energy nuclear north | Nuclear_power |
| 379. | allies | 35: [13, inf] | allies 's bush | George_H._W._Bush |
| 380. | psychiatric | 35: [10, inf] | psychiatric hospital china | Psychiatric_hospital |
| 381. | visa | 35: [10, inf] | visa europe russia | Visa_policy_of_Russia |
| 382. | ireland | 36: [22, inf] | ireland northern europe | Northern_Europe |
| 383. | immigrants | 36: [10, 5.0], 38: [12, 12.0], 49: [10, inf] | immigrants 's europe | Immigration_to_Europe |
| 384. | september | 37: [18, inf] | september attacks us | September_11_attacks |
| 385. | level | 37: [12, inf] | level 's united | Cabinet_of_the_United_States |
| 386. | equipment | 37: [11, inf], 49: [11, 5.5] | equipment 's iraq | List_of_current_equipment_of_the_Iraqi_Army |
| 387. | resolutions | 37: [14, inf], 44: [10, 5.0] | resolutions iraq bush | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 388. | al-shibh | 37: [11, inf] | al-shibh qaeda officials | Ramzi_bin_al-Shibh |
| 389. | bavaria | 37: [10, inf] | bavaria 's stoiber | Edmund_Stoiber |
| 390. | investigators | 37: [13, inf] | investigators 's american | Special_Counsel_investigation_(2017–2019) |
| 391. | karachi | 37: [16, 16.0], 44: [18, inf] | karachi pearl pakistan | Pearl-Continental_Hotels_&_Resorts |
| 392. | jordan | 37: [10, 10.0], 44: [19, inf] | jordan israel 's | Israel–Jordan_relations |
| 393. | population | 38: [10, inf] | population 's world | World_population |
| 394. | release | 38: [15, inf] | release 's arafat | Yasser_Arafat |
| 395. | maya | 38: [10, inf] | maya mexico palenque | Palenque |
| 396. | coffee | 38: [10, inf] | coffee day 's | Café_Coffee_Day |
| 397. | papon | 38: [16, inf] | papon release french | Maurice_Papon |
| 398. | hedge | 38: [10, inf] | hedge funds fund | Hedge_fund |
| 399. | foreigners | 39: [13, inf] | foreigners 's foreign | Xenophobia |
| 400. | ivory | 39: [15, inf] | ivory coast africa | Ivory_Coast |
| 401. | trapped | 39: [10, inf] | trapped israeli troops | Yom_Kippur_War |
| 402. | radar | 39: [12, inf] | radar iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 403. | complex | 39: [12, inf] | complex 's north | North_Complex_fire |
| 404. | draft | 39: [12, inf] | draft iraq 's | Iraq_War |
| 405. | hezbollah | 39: [12, inf] | hezbollah israeli israel | Iran–Israel_proxy_conflict |
| 406. | dostum | 39: [10, inf] | dostum prisoners taliban | Abdul_Rashid_Dostum |
| 407. | delay | 40: [12, inf], 49: [10, 5.0] | delay 's bush | George_W._Bush |
| 408. | ira | 40: [12, inf] | ira ireland northern | Provisional_Irish_Republican_Army |
| 409. | kurdish | 40: [10, inf] | kurdish iraq kurds | Kurds_in_Iraq |
| 410. | philippines | 40: [15, inf] | philippines american abu | Abu_Sayyaf |
| 411. | kurds | 40: [16, inf] | kurds iraq iraqi | Iraqi_Kurdistan |
| 412. | spending | 40: [10, inf] | spending 's government | Government_spending |
| 413. | sinn | 40: [13, inf] | sinn fein ireland | Sinn_Féin |
| 414. | fein | 40: [13, inf] | fein sinn ireland | Sinn_Féin |
| 415. | king | 40: [15, inf] | king 's former | Angus_King |
| 416. | deuba | 40: [11, inf] | deuba nepal rebels | Sher_Bahadur_Deuba |
| 417. | tanker | 41: [14, inf] | tanker oil spain | Prestige_oil_spill |
| 418. | blast | 41: [10, inf], 45: [11, 11.0] | blast israeli 's | Iran–Israel_proxy_conflict |
| 419. | sentences | 41: [12, inf] | sentences court years | Suspended_sentence |
| 420. | indonesia | 41: [10, inf], 45: [13, inf], 47: [12, 6.0] | indonesia 's indonesian | Indonesia |
| 421. | kuwaiti | 41: [10, inf], 47: [11, 5.5] | kuwaiti kuwait american | Demographics_of_Kuwait |
| 422. | kuwait | 41: [18, inf] | kuwait iraq 's | Invasion_of_Kuwait |
| 423. | nobel | 41: [15, inf] | nobel prize carter | Nobel_Prize |
| 424. | prize | 41: [15, inf], 50: [10, inf] | prize carter nobel | Nobel_Prize |
| 425. | committee | 41: [12, inf], 46: [14, 14.0] | committee 's says | United_States_congressional_committee |
| 426. | pinocchio | 41: [16, inf] | pinocchio italians rome | The_Adventures_of_Pinocchio |
| 427. | warnings | 42: [10, inf], 46: [12, inf] | warnings 's say | Miranda_warning |
| 428. | heavy | 42: [10, inf] | heavy 's israeli | Nuclear_weapons_and_Israel |
| 429. | iraqis | 42: [13, inf], 49: [21, 5.25] | iraqis iraq hussein | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 430. | jemaah | 42: [10, inf] | jemaah indonesian islamiyah | Christmas_Eve_2000_Indonesia_bombings |
| 431. | gerdt | 42: [11, inf] | gerdt bombing including | Myyrmanni_bombing |
| 432. | claim | 43: [10, inf] | claim 's government | Federal_government_of_the_United_States |
| 433. | mohamed | 43: [13, inf] | mohamed sept say | Mohamed_Atta |
| 434. | atta | 43: [13, inf] | atta sept attacks | September_11_attacks |
| 435. | havel | 43: [10, inf] | havel czech pres | Václav_Havel |
| 436. | prisons | 43: [14, inf] | prisons prisoners 's | Prisoner_security_categories_in_the_United_Kingdom |
| 437. | cities | 43: [11, inf] | cities 's israeli | List_of_cities_in_Israel |
| 438. | get | 43: [10, inf] | get 's photo | Google_Photos |
| 439. | theater | 43: [33, inf] | theater moscow chechen | Moscow_theater_hostage_crisis |
| 440. | formally | 43: [12, inf] | formally 's iraq | 2003_invasion_of_Iraq |
| 441. | hostages | 43: [26, inf] | hostages moscow theater | Moscow_theater_hostage_crisis |
| 442. | bedouin | 43: [11, inf] | bedouin israel israeli | Negev_Bedouin |
| 443. | silva | 44: [12, inf] | silva brazil 's | Thiago_Silva |
| 444. | foley | 44: [11, inf] | foley jordan american | Jordan_Foley |
| 445. | extremists | 44: [10, inf] | extremists 's pakistan | Tehreek-e-Labbaik_Pakistan |
| 446. | issues | 44: [15, inf] | issues 's bush | Prescott_Bush |
| 447. | girls | 44: [18, inf], 47: [16, 16.0] | girls 's two | 2_Girls_1_Cup |
| 448. | denmark | 44: [10, inf] | denmark chechen 's | Chechens |
| 449. | zakayev | 44: [12, inf] | zakayev chechen russia | Akhmed_Zakayev |
| 450. | danish | 44: [10, inf] | danish chechen zakayev | Akhmed_Zakayev |
| 451. | bombings | 44: [12, inf] | bombings palestinian israel | List_of_Palestinian_suicide_attacks |
| 452. | water | 44: [18, 9.0], 50: [15, inf] | water 's united | Water_fluoridation_in_the_United_States |
| 453. | appeals | 45: [11, inf] | appeals 's court | United_States_courts_of_appeals |
| 454. | catfish | 45: [12, inf] | catfish vietnamese fish | Basa_(fish) |
| 455. | spy | 45: [15, inf] | spy 's intelligence | Espionage |
| 456. | cod | 45: [10, inf] | cod fishing north | Atlantic_cod |
| 457. | voice | 46: [13, inf] | voice 's government | Indigenous_voice_to_government |
| 458. | gates | 46: [10, inf] | gates north asylum | Gladesville_Mental_Hospital |
| 459. | foundation | 46: [10, inf] | foundation 's india | American_India_Foundation |
| 460. | migrants | 46: [12, inf] | migrants 's north | European_migrant_crisis |
| 461. | kibbutz | 46: [10, inf] | kibbutz israeli palestinian | 1948_Arab–Israeli_War |
| 462. | setback | 46: [10, inf] | setback 's government | Setback_(land_use) |
| 463. | cyprus | 46: [10, inf] | cyprus europe union | Northern_Cyprus_and_the_European_Union |
| 464. | apartheid | 46: [11, inf] | apartheid africa south | Apartheid |
| 465. | chechnya | 46: [19, inf], 50: [10, 5.0] | chechnya russian russia | Chechnya |
| 466. | students | 46: [16, inf] | students 's school | Student |
| 467. | tape | 46: [18, inf] | tape laden 's | Videos_and_audio_recordings_of_Osama_bin_Laden |
| 468. | supporters | 46: [10, inf] | supporters 's government | Government_shutdowns_in_the_United_States |
| 469. | chancellor | 46: [10, inf] | chancellor 's schroder | Gerhard_Schröder |
| 470. | coast | 46: [11, inf] | coast 's oil | Gulf_Coast_of_the_United_States |
| 471. | fuel | 47: [18, 18.0], 50: [10, 5.0], 52: [13, inf] | fuel north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 472. | g.i | 47: [14, inf] | g.i 's american | G.I._Joe |
| 473. | sergeant | 47: [14, inf] | sergeant korea army | Republic_of_Korea_Army |
| 474. | vehicle | 47: [11, inf] | vehicle israeli two | Vehicle_registration_plates_of_Israel |
| 475. | fail | 47: [10, inf] | fail 's bush | George_W._Bush |
| 476. | andreotti | 47: [12, inf] | andreotti italy prime | Giulio_Andreotti |
| 477. | petersburg | 47: [10, inf] | petersburg bush putin | Vladimir_Putin |
| 478. | berlin | 47: [10, inf] | berlin germany 's | Berlin |
| 479. | deaths | 47: [12, inf] | deaths 's military | United_States_military_casualties_of_war |
| 480. | athomeabroad | 47: [18, inf] | athomeabroad culture 's | EMPTY MATCHING |
| 481. | detention | 48: [11, inf] | detention 's government | Indefinite_detention |
| 482. | infected | 48: [10, inf] | infected aids 's | HIV/AIDS |
| 483. | ford | 48: [14, inf] | ford 's argentina | Ford_Motor_Argentina |
| 484. | missiles | 48: [13, inf] | missiles 's israeli | Arrow_(Israeli_missile) |
| 485. | israeli-owned | 48: [13, inf] | israeli-owned kenya israeli | Israel–Kenya_relations |
| 486. | mombasa | 48: [19, inf] | mombasa kenya israeli | 2002_Mombasa_attacks |
| 487. | target | 48: [10, inf] | target 's israeli | Targeted_killings_by_Israel_Defense_Forces |
| 488. | kenyans | 48: [13, inf] | kenyans kenya qaeda | Timeline_of_Kenya |
| 489. | amber | 48: [12, inf] | amber world miners | 2015–16_ISU_World_Standings |
| 490. | scientists | 49: [12, inf] | scientists 's iraq | Iran–Iraq_War |
| 491. | afghans | 49: [10, inf] | afghans afghanistan afghan | Women_in_Afghanistan |
| 492. | luxury | 49: [14, inf] | luxury 's fashion | Italian_fashion |
| 493. | palace | 49: [11, inf] | palace 's royal | St_James's_Palace |
| 494. | asks | 49: [14, inf] | asks 's iraq | Iraq |
| 495. | warns | 50: [13, inf] | warns 's bush | George_H._W._Bush |
| 496. | rivers | 50: [10, inf] | rivers water 's | List_of_water_deities |
| 497. | negotiations | 50: [10, inf] | negotiations 's bush | George_H._W._Bush |
| 498. | norway | 51: [13, inf] | norway world 's | German_occupation_of_Norway |
| 499. | wall | 51: [10, inf] | wall pearl 's | Daniel_Pearl |
| 500. | radio | 51: [12, inf] | radio 's says | Say_Say_Say |
| 501. | neighbors | 52: [10, inf] | neighbors 's photo | America's_Next_Top_Model_(season_20) |
| 502. | plutonium | 52: [15, inf] | plutonium north korea | North_Korea_and_weapons_of_mass_destruction |
| 503. | features | 16: [42, 42.0] | features function purl | Permalink |
| 504. | women | 23: [32, 32.0], 35: [12, 12.0], 40: [10, 5.0], 48: [19, 9.5] | women 's say | SayHerName |
| 505. | economy | 5: [13, 6.5], 13: [10, 10.0], 29: [21, 21.0], 39: [15, 5.0] | economy 's government | Economy |
| 506. | bombing | 7: [16, 8.0], 19: [13, 13.0], 30: [21, 21.0], 38: [18, 6.0] | bombing 's israeli | AMIA_bombing |
| 507. | pacific | 16: [21, 21.0] | pacific function purl | Happy_Days |
| 508. | camps | 9: [20, 20.0] | camps 's refugee | Refugee_camp |
| 509. | close | 36: [20, 20.0] | close 's iraq | 2003_invasion_of_Iraq |
| 510. | african | 28: [19, 19.0], 38: [10, 5.0] | african africa south | South_Africa |
| 511. | forum | 5: [36, 18.0] | forum world 's | World_Economic_Forum |
| 512. | hong | 9: [10, 5.0], 12: [11, 5.5], 23: [14, 7.0], 25: [18, 18.0] | hong kong 's | Hong_Kong |
| 513. | terrorism | 14: [18, 18.0], 31: [18, 6.0] | terrorism 's bush | War_on_terror |
| 514. | german | 46: [18, 18.0] | german 's germany | Germany |
| 515. | system | 2: [11, 5.5], 27: [15, 7.5], 39: [17, 17.0] | system 's government | List_of_countries_by_system_of_government |
| 516. | arafat | 4: [33, 8.25], 26: [81, 16.2], 32: [16, 5.33], 44: [17, 17.0] | arafat palestinian israeli | Yasser_Arafat |
| 517. | iran | 11: [17, 17.0], 16: [15, 7.5], 35: [26, 13.0], 37: [13, 6.5] | iran 's bush | Iran–Contra_affair |
| 518. | remains | 18: [17, 17.0], 26: [10, 5.0] | remains 's says | The_Symbol_Remains |
| 519. | mission | 23: [17, 17.0] | mission 's american | American_Mission_Hospital |
| 520. | work | 48: [19, 6.33], 50: [17, 17.0] | work 's iraq | Iraq_War |
| 521. | interview | 5: [16, 16.0], 16: [10, 10.0], 36: [34, 8.5] | interview 's says | The_Interview |
| 522. | elections | 16: [10, 10.0], 40: [16, 16.0] | elections 's party | Political_party_strength_in_U.S._states |
| 523. | without | 27: [16, 16.0], 39: [16, 5.33] | without 's bush | George_W._Bush |
| 524. | roh | 51: [16, 16.0] | roh korea north | Roh_Moo-hyun |
| 525. | despite | 4: [13, 6.5], 7: [15, 15.0], 26: [11, 5.5], 47: [11, 5.5] | despite 's bush | George_H._W._Bush |
| 526. | decision | 5: [10, 5.0], 8: [12, 6.0], 37: [15, 15.0], 50: [11, 5.5] | decision 's bush | Bush_v._Gore |
| 527. | documents | 14: [15, 15.0] | documents 's says | Afghan_War_documents_leak |
| 528. | canadian | 16: [15, 15.0], 26: [11, 5.5] | canadian canada 's | Canada |
| 529. | small | 19: [15, 15.0] | small 's government | Small_government |
| 530. | china | 45: [45, 15.0] | china 's north | North_China |
| 531. | firefighters | 46: [15, 15.0] | firefighters strike britain | Reichstag_fire |
| 532. | gulf | 50: [15, 15.0] | gulf iraq 's | Gulf_War |
| 533. | state | 2: [28, 14.0] | state 's bush | Bush_family |
| 534. | arrested | 2: [14, 14.0], 20: [15, 7.5] | arrested 's say | Arrested_Development |
| 535. | blair | 2: [14, 14.0], 7: [15, 7.5], 39: [11, 11.0], 48: [13, 6.5] | blair 's prime | Premiership_of_Tony_Blair |
| 536. | department | 2: [14, 14.0], 47: [16, 8.0] | department state 's | United_States_Department_of_State |
| 537. | area | 9: [14, 14.0], 15: [16, 8.0], 27: [11, 11.0] | area 's say | Barka_Sayal_Area |
| 538. | mubarak | 10: [10, 5.0], 23: [14, 14.0] | mubarak pres 's | Shaadi_Mubarak |
| 539. | development | 11: [14, 14.0], 52: [11, 5.5] | development 's world | World_Development_Report |
| 540. | vice | 11: [14, 14.0] | vice 's pres | Vice_president |
| 541. | cheney | 11: [28, 14.0] | cheney pres bush | Liz_Cheney |
| 542. | hold | 13: [12, 6.0], 15: [16, 5.33], 30: [11, 11.0], 45: [14, 14.0] | hold 's palestinian | Israeli–Palestinian_conflict |
| 543. | reportedly | 14: [14, 14.0], 25: [20, 5.0], 35: [10, 10.0] | reportedly 's israeli | Nuclear_weapons_and_Israel |
| 544. | exports | 15: [14, 14.0] | exports 's oil | List_of_countries_by_oil_exports |
| 545. | village | 17: [21, 7.0], 22: [14, 14.0] | village 's map | Map |
| 546. | sharon | 32: [18, 9.0], 44: [28, 14.0] | sharon israeli israel | Ariel_Sharon |
| 547. | indonesian | 32: [16, 8.0], 42: [28, 14.0] | indonesian indonesia 's | Indonesia |
| 548. | soldiers | 37: [14, 14.0] | soldiers israeli 's | Israel_Defense_Forces |
| 549. | canada | 50: [14, 14.0] | canada 's canadian | Canadians |
| 550. | article | 12: [10, 5.0], 16: [27, 13.5], 36: [21, 5.25] | article function 's | Riemann_zeta_function |
| 551. | reports | 4: [12, 12.0], 8: [10, 10.0], 34: [13, 13.0] | reports 's says | U.S._News_&_World_Report |
| 552. | like | 5: [13, 13.0], 7: [13, 13.0] | like 's bush | George_H._W._Bush |
| 553. | russia | 9: [20, 5.0], 11: [13, 13.0], 17: [23, 7.67], 33: [25, 12.5] | russia 's russian | Russia |
| 554. | tanks | 11: [13, 13.0] | tanks israeli palestinian | 1948_Arab–Israeli_War |
| 555. | aid | 11: [37, 9.25], 25: [11, 11.0], 30: [13, 13.0], 47: [22, 7.33] | aid 's says | United_States_foreign_aid |
| 556. | latest | 12: [13, 13.0], 41: [10, 5.0] | latest 's israel | Israel |
| 557. | concludes | 12: [13, 13.0] | concludes 's u.s. | United_States_Senate |
| 558. | taken | 14: [13, 6.5], 29: [10, 10.0], 46: [13, 13.0] | taken 's say | Taken_3 |
| 559. | show | 14: [11, 11.0], 26: [10, 5.0], 36: [10, 10.0], 39: [13, 13.0] | show 's says | That_'70s_Show |
| 560. | commission | 21: [13, 13.0] | commission 's rights | National_Human_Rights_Commission_of_India |
| 561. | sign | 28: [15, 7.5], 35: [13, 13.0] | sign 's bush | George_W._Bush |
| 562. | militants | 31: [13, 13.0], 37: [18, 9.0] | militants 's pakistan | Tehrik-i-Taliban_Pakistan |
| 563. | poland | 33: [13, 13.0] | poland 's union | Poland_in_the_European_Union |
| 564. | villages | 34: [13, 13.0] | villages 's say | U.S._state |
| 565. | debate | 35: [13, 13.0], 42: [15, 5.0] | debate 's iraq | Iraq |
| 566. | planned | 35: [13, 13.0] | planned 's says | Plan_S |
| 567. | following | 36: [13, 13.0] | following 's bush | George_H._W._Bush |
| 568. | ever | 38: [10, 10.0], 50: [13, 13.0] | ever 's government | Federal_government_of_the_United_States |
| 569. | austria | 38: [13, 13.0] | austria 's europe | Austria |
| 570. | growth | 39: [13, 13.0] | growth 's economic | Economic_growth |
| 571. | island | 41: [13, 13.0] | island 's american | United_States_Virgin_Islands |
| 572. | authorities | 43: [13, 13.0] | authorities 's say | Certificate_authority |
| 573. | remarks | 45: [13, 13.0] | remarks 's bush | Barbara_Bush_(born_1981) |
| 574. | advocate | 45: [13, 13.0] | advocate china 's | China |
| 575. | today | 14: [25, 12.5] | today 's u.s. | Today_(American_TV_program) |
| 576. | next | 2: [12, 12.0], 17: [12, 6.0] | next 's bush | George_H._W._Bush |
| 577. | base | 2: [24, 12.0] | base 's military | Military_base |
| 578. | hospital | 5: [12, 12.0], 42: [10, 5.0] | hospital 's say | St._Jude_Children's_Research_Hospital |
| 579. | mass | 5: [10, 10.0], 31: [10, 5.0], 37: [15, 7.5], 52: [12, 12.0] | mass iraq 's | Iraq_and_weapons_of_mass_destruction |
| 580. | economic | 5: [41, 5.12], 20: [11, 11.0], 32: [12, 12.0], 39: [29, 5.8] | economic 's bush | George_W._Bush |
| 581. | central | 6: [15, 5.0], 43: [12, 12.0] | central 's government | Central_government |
| 582. | opening | 7: [10, 5.0], 43: [12, 12.0] | opening 's bush | George_W._Bush |
| 583. | charges | 7: [16, 5.33], 51: [12, 12.0] | charges 's world | Pickett's_Charge |
| 584. | crime | 7: [12, 12.0] | crime 's police | Police_and_crime_commissioner |
| 585. | become | 11: [15, 7.5], 16: [10, 10.0], 43: [12, 12.0] | become 's photo | Google_Photos |
| 586. | organization | 12: [12, 12.0], 20: [10, 5.0] | organization 's group | Group_purchasing_organization |
| 587. | news | 13: [12, 12.0], 50: [11, 5.5] | news 's says | U.S._News_&_World_Report |
| 588. | move | 14: [10, 5.0], 28: [12, 12.0] | move 's government | MOVE |
| 589. | round | 15: [12, 12.0] | round 's iraq | 2003_invasion_of_Iraq |
| 590. | philippine | 23: [12, 12.0] | philippine american philippines | Philippine–American_War |
| 591. | boeing | 27: [12, 12.0] | boeing china 's | China_Airlines_Flight_611 |
| 592. | treaty | 31: [10, 5.0], 42: [12, 12.0] | treaty bush world | George_H._W._Bush |
| 593. | farmers | 33: [24, 12.0] | farmers 's zimbabwe | Land_reform_in_Zimbabwe |
| 594. | eta | 35: [12, 12.0] | eta basque group | ETA_(separatist_group) |
| 595. | missile | 40: [12, 12.0] | missile 's north | List_of_North_Korean_missile_tests |
| 596. | rise | 50: [12, 12.0] | rise 's world | Rise_World_Tour |
| 597. | rules | 2: [23, 11.5] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 598. | security | 2: [23, 11.5] | security 's iraq | Iraqi_security_forces |
| 599. | program | 42: [23, 11.5] | program north 's | North_Korea_and_weapons_of_mass_destruction |
| 600. | gas | 44: [34, 11.33] | gas 's say | Gas_constant |
| 601. | television | 2: [10, 10.0], 15: [10, 10.0], 46: [11, 11.0] | television 's says | America_Says |
| 602. | steps | 2: [12, 6.0], 17: [11, 11.0], 19: [10, 5.0] | steps 's bush | Jonathan_S._Bush |
| 603. | linked | 2: [11, 11.0] | linked 's qaeda | Al-Qaeda |
| 604. | past | 4: [11, 11.0], 37: [10, 5.0], 47: [10, 5.0] | past 's say | List_of_past_Coronation_Street_characters |
| 605. | woman | 5: [11, 11.0], 8: [10, 5.0], 15: [10, 5.0] | woman 's israeli | Gal_Gadot |
| 606. | accused | 5: [11, 5.5], 32: [11, 11.0] | accused 's world | The_Accüsed |
| 607. | road | 5: [11, 11.0] | road 's israeli | Roads_in_Israel |
| 608. | global | 5: [11, 11.0], 39: [11, 5.5] | global 's world | Global_city |
| 609. | expected | 7: [11, 11.0], 38: [11, 11.0] | expected 's party | Democratic_Party_(United_States) |
| 610. | order | 7: [11, 11.0] | order 's says | Order_of_the_British_Empire |
| 611. | finds | 9: [11, 11.0] | finds 's world | Findability |
| 612. | commanders | 10: [11, 11.0] | commanders military american | Lists_of_military_commanders |
| 613. | bodies | 11: [10, 10.0], 16: [11, 11.0] | bodies 's says | Body_Say |
| 614. | koreans | 11: [11, 11.0], 19: [15, 7.5] | koreans north korea | North_Korea–South_Korea_relations |
| 615. | enemy | 13: [11, 11.0] | enemy 's american | Public_Enemy |
| 616. | attempt | 13: [11, 11.0], 36: [10, 10.0], 47: [10, 10.0] | attempt 's pres | List_of_coups_and_coup_attempts |
| 617. | food | 13: [11, 11.0], 22: [10, 5.0], 47: [14, 7.0] | food 's world | World_Food_Programme |
| 618. | urges | 14: [11, 11.0] | urges 's says | Urge_(film) |
| 619. | sports | 16: [22, 11.0] | sports function purl | Ski_wax |
| 620. | jean-marie | 17: [22, 11.0] | jean-marie pen french | Jean-Marie_Le_Pen |
| 621. | give | 17: [11, 11.0] | give 's iraq | Iraq_War |
| 622. | makes | 18: [10, 5.0], 46: [11, 11.0] | makes 's bush | George_W._Bush |
| 623. | third | 18: [11, 11.0] | third 's world | Third_World |
| 624. | taiwan | 22: [11, 11.0], 26: [15, 7.5] | taiwan china 's | Taiwan,_China |
| 625. | right | 25: [11, 11.0], 37: [11, 5.5] | right 's bush | Bush_family |
| 626. | five | 25: [20, 5.0], 45: [11, 11.0] | five 's israeli | Nuclear_weapons_and_Israel |
| 627. | parents | 28: [11, 11.0] | parents children 's | Parenting |
| 628. | much | 29: [11, 11.0] | much 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 629. | schroder | 33: [11, 11.0] | schroder 's german | Dennis_Schröder |
| 630. | railroad | 34: [11, 11.0] | railroad korea north | KORAIL |
| 631. | democracy | 34: [11, 11.0] | democracy 's government | Democracy |
| 632. | u.s | 35: [11, 11.0] | u.s korea u.s. | U.S._Steel |
| 633. | council | 35: [11, 11.0], 37: [31, 6.2] | council iraq 's | Council_of_Representatives_of_Iraq |
| 634. | charge | 35: [11, 11.0] | charge 's world | Pickett's_Charge |
| 635. | baghdad | 37: [11, 11.0], 43: [10, 5.0] | baghdad iraq 's | Embassy_of_the_United_States,_Baghdad |
| 636. | denies | 38: [11, 11.0] | denies 's says | Say's_law |
| 637. | companies | 38: [15, 5.0], 46: [11, 11.0] | companies 's government | List_of_government-owned_companies |
| 638. | less | 41: [11, 11.0] | less 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 639. | plan | 41: [22, 11.0] | plan 's bush | George_W._Bush |
| 640. | marine | 41: [11, 11.0] | marine 's killed | United_States_Marine_Corps |
| 641. | sentence | 46: [11, 11.0] | sentence 's world | Life_imprisonment |
| 642. | province | 48: [11, 11.0] | province 's government | Government_of_Province_No._2 |
| 643. | reactor | 52: [11, 11.0] | reactor north korea | North_Korea_and_weapons_of_mass_destruction |
| 644. | refugee | 9: [16, 5.33], 15: [21, 10.5], 22: [12, 6.0] | refugee israeli palestinian | Palestinian_refugees |
| 645. | city | 39: [52, 10.4], 52: [10, 5.0] | city 's israeli | List_of_cities_in_Israel |
| 646. | top | 2: [10, 10.0], 49: [11, 5.5] | top 's officials | The_Official_Big_Top_40 |
| 647. | four | 2: [10, 10.0] | four 's say | Say_Say_Say |
| 648. | use | 2: [11, 5.5], 28: [10, 10.0] | use 's iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 649. | behind | 3: [10, 10.0] | behind 's says | Say's_law |
| 650. | standoff | 3: [10, 10.0], 15: [10, 5.0] | standoff 's pakistan | 2019_India–Pakistan_border_skirmishes |
| 651. | inquiry | 4: [10, 10.0], 17: [14, 7.0] | inquiry 's says | Leveson_Inquiry |
| 652. | others | 4: [10, 10.0] | others 's say | Say's_law |
| 653. | six | 5: [10, 10.0], 25: [12, 6.0], 41: [11, 5.5] | six 's israeli | Six-Day_War |
| 654. | warlord | 5: [10, 10.0] | warlord 's government | Beiyang_government |
| 655. | kidnapping | 6: [10, 10.0], 17: [12, 6.0] | kidnapping pearl 's | Daniel_Pearl |
| 656. | `` | 7: [10, 5.0], 16: [25, 6.25], 29: [10, 10.0] | `` function 's | Riemann_zeta_function |
| 657. | crash | 8: [10, 10.0], 16: [20, 10.0] | crash 's air | Dunbeath_air_crash |
| 658. | americans | 9: [10, 10.0], 22: [11, 5.5] | americans american 's | Americans |
| 659. | across | 10: [10, 10.0], 14: [19, 9.5], 33: [11, 5.5] | across 's officials | Across_the_Universe_(film) |
| 660. | allow | 10: [10, 10.0], 43: [10, 5.0] | allow 's iraq | Iraq_War |
| 661. | british | 11: [14, 7.0], 25: [10, 10.0] | british 's britain | Britishness |
| 662. | found | 11: [10, 10.0], 14: [12, 6.0], 49: [14, 7.0] | found 's says | Say's_law |
| 663. | america | 11: [20, 6.67], 50: [10, 10.0] | america 's bush | Bush_family |
| 664. | dick | 11: [10, 10.0] | dick pres cheney | Liz_Cheney |
| 665. | kandahar | 12: [10, 10.0] | kandahar taliban afghanistan | United_States_invasion_of_Afghanistan |
| 666. | response | 12: [10, 10.0] | response 's bush | George_W._Bush |
| 667. | presidential | 13: [12, 6.0], 39: [10, 10.0] | presidential 's election | United_States_presidential_election |
| 668. | ukraine | 13: [10, 10.0] | ukraine kuchma 's | Leonid_Kuchma |
| 669. | center | 14: [10, 5.0], 28: [10, 10.0] | center 's world | World_Trade_Center_(1973–2001) |
| 670. | escalating | 14: [10, 10.0] | escalating 's israeli | Israel–United_States_relations |
| 671. | occupation | 14: [10, 10.0] | occupation israeli 's | Israeli-occupied_territories |
| 672. | shot | 15: [10, 10.0] | shot israeli palestinian | 2015–16_wave_of_violence_in_Israeli–Palestinian_conflict |
| 673. | times | 16: [10, 10.0] | times 's york | The_New_York_Times |
| 674. | apr | 17: [10, 10.0] | apr 's israel | Alex_Wagner |
| 675. | cash | 17: [10, 10.0] | cash 's government | Cash |
| 676. | policies | 17: [10, 10.0] | policies 's bush | George_W._Bush |
| 677. | team | 17: [30, 10.0] | team 's iraq | Iraq_national_football_team |
| 678. | bangladesh | 18: [10, 10.0] | bangladesh world asia | Bangladesh |
| 679. | civil | 18: [10, 10.0] | civil 's government | Civil_Disobedience_(Thoreau) |
| 680. | beijing | 19: [10, 10.0] | beijing china north | Beijing |
| 681. | aides | 20: [10, 10.0] | aides 's bush | George_H._W._Bush |
| 682. | tensions | 21: [10, 10.0] | tensions 's pakistan | Pakistan |
| 683. | deny | 21: [10, 10.0] | deny 's says | Say's_law |
| 684. | half | 23: [10, 10.0] | half 's government | Half_dollar_(United_States_coin) |
| 685. | back | 23: [10, 10.0] | back 's bush | George_H._W._Bush |
| 686. | yasir | 26: [35, 7.0], 44: [10, 10.0] | yasir arafat palestinian | Yasser_Arafat |
| 687. | rising | 26: [10, 10.0] | rising 's says | 88rising |
| 688. | offices | 26: [10, 10.0] | offices 's government | Quebec_Government_Offices |
| 689. | special | 27: [10, 10.0] | special 's forces | United_States_Army_Special_Forces |
| 690. | crew | 27: [10, 10.0] | crew 's says | Crew_cut |
| 691. | spanish | 29: [13, 6.5], 35: [10, 10.0] | spanish 's spain | Spain |
| 692. | emergency | 29: [10, 10.0] | emergency 's north | 9-1-1 |
| 693. | batasuna | 35: [10, 10.0] | batasuna basque party | Batasuna |
| 694. | hamburg | 35: [10, 10.0] | hamburg german attacks | Hamburg_cell |
| 695. | bid | 35: [10, 10.0] | bid 's says | 2030_FIFA_World_Cup |
| 696. | ethnic | 35: [10, 10.0] | ethnic 's government | List_of_ethnic_slurs_by_ethnicity |
| 697. | osama | 36: [10, 10.0], 46: [10, 5.0] | osama laden qaeda | Hamza_bin_Laden |
| 698. | aleksandr | 37: [10, 10.0] | aleksandr belarus europe | Alexander_Lukashenko |
| 699. | skepticism | 37: [10, 10.0] | skepticism 's bush | Presidency_of_George_W._Bush |
| 700. | join | 38: [10, 10.0] | join 's european | 2022_European_Men's_Handball_Championship_qualification |
| 701. | rich | 39: [10, 10.0] | rich world 's | Richie_Rich_(comics) |
| 702. | afghanistan | 41: [20, 10.0] | afghanistan 's taliban | Islamic_Emirate_of_Afghanistan |
| 703. | accord | 41: [10, 10.0] | accord 's russia | Honda_Accord |
| 704. | activity | 41: [10, 10.0] | activity 's says | Say's_law |
| 705. | founder | 41: [10, 10.0] | founder 's group | Founder_Group |
| 706. | defense | 42: [20, 10.0] | defense 's says | United_States_Department_of_Defense |
| 707. | failed | 42: [10, 10.0] | failed 's say | Fianna_Fáil |
| 708. | told | 43: [10, 10.0] | told 's bush | Barbara_Bush_(born_1981) |
| 709. | industry | 43: [10, 10.0] | industry 's government | State_ownership |
| 710. | prepared | 44: [10, 10.0] | prepared 's says | Beep_Prepared |
| 711. | experts | 46: [10, 10.0] | experts 's say | Expert_system |
| 712. | analysts | 46: [10, 10.0] | analysts 's say | Tiffany_Cross |
| 713. | premier | 46: [10, 10.0] | premier 's prime | Premier_of_the_People's_Republic_of_China |
| 714. | body | 47: [10, 10.0] | body 's say | Body_Say |
| 715. | prestige | 47: [10, 10.0] | prestige oil tanker | Prestige_oil_spill |
| 716. | fully | 47: [10, 10.0] | fully 's says | Kristina_Carrillo-Bucaram |
| 717. | early | 49: [10, 10.0] | early 's government | Federal_government_of_the_United_States |
| 718. | long | 50: [10, 10.0] | long 's government | Government |
| 719. | persian | 50: [10, 10.0] | persian iraq 's | Iran–Iraq_War |
| 720. | internet | 51: [10, 10.0] | internet china 's | Internet_in_China |
| 721. | bank | 14: [77, 9.62], 39: [27, 9.0], 51: [15, 5.0] | bank israeli palestinian | Israeli_West_Bank_barrier |
| 722. | terrorists | 2: [19, 9.5], 32: [15, 7.5] | terrorists 's says | FBI_Most_Wanted_Terrorists |
| 723. | could | 2: [19, 9.5] | could 's iraq | Iraq |
| 724. | proposal | 9: [19, 9.5] | proposal 's palestinian | History_of_the_State_of_Palestine |
| 725. | laden | 9: [12, 6.0], 36: [19, 9.5], 46: [21, 5.25] | laden qaeda osama | Hamza_bin_Laden |
| 726. | hebron | 14: [17, 8.5], 26: [19, 9.5] | hebron israeli palestinian | Israeli–Palestinian_conflict_in_Hebron |
| 727. | fire | 25: [13, 6.5], 44: [19, 9.5] | fire israeli 's | Yom_Kippur_War |
| 728. | hebrew | 31: [19, 9.5] | hebrew israel 's | Black_Hebrew_Israelites |
| 729. | bali | 42: [47, 9.4], 45: [23, 7.67] | bali indonesia bombing | 2002_Bali_bombings |
| 730. | rebels | 2: [18, 9.0], 17: [16, 8.0], 27: [16, 5.33], 32: [11, 5.5] | rebels 's government | List_of_Star_Wars_Rebels_characters |
| 731. | russian | 9: [18, 9.0], 26: [26, 6.5] | russian russia 's | Russia |
| 732. | leave | 21: [18, 9.0] | leave 's united | Maternity_leave_in_the_United_States |
| 733. | thailand | 35: [18, 9.0], 52: [12, 6.0] | thailand asia world | Thailand |
| 734. | hu | 46: [18, 9.0] | hu 's party | Hu_Jintao |
| 735. | national | 50: [27, 9.0] | national 's government | Federal_government_of_the_United_States |
| 736. | strip | 2: [11, 5.5], 10: [12, 6.0], 19: [17, 8.5], 49: [10, 5.0] | strip israeli gaza | Gaza_War_(2008–2009) |
| 737. | report | 9: [17, 8.5] | report 's says | U.S._News_&_World_Report |
| 738. | zubaydah | 14: [17, 8.5] | zubaydah qaeda abu | Abu_Zubaydah |
| 739. | siege | 17: [20, 5.0], 39: [17, 8.5] | siege israeli arafat | Yasser_Arafat |
| 740. | prince | 17: [17, 8.5] | prince saudi 's | Crown_Prince_of_Saudi_Arabia |
| 741. | months | 25: [17, 8.5] | months 's government | Month |
| 742. | fighting | 31: [17, 8.5], 39: [11, 5.5] | fighting 's israeli | Yom_Kippur_War |
| 743. | killing | 37: [17, 8.5] | killing 's israeli | List_of_Israeli_assassinations |
| 744. | faces | 38: [17, 8.5] | faces 's government | Government_shutdowns_in_the_United_States |
| 745. | air | 27: [25, 8.33], 38: [20, 5.0], 45: [12, 6.0], 52: [15, 5.0] | air 's american | United_States_Air_Force |
| 746. | evil | 5: [16, 8.0] | evil bush 's | Axis_of_evil |
| 747. | talks | 6: [13, 6.5], 8: [24, 8.0], 29: [15, 7.5], 40: [16, 8.0], 43: [24, 6.0] | talks 's bush | Sophia_Bush |
| 748. | u.n. | 11: [10, 5.0], 35: [11, 5.5], 37: [24, 8.0] | u.n. iraq united | 2003_invasion_of_Iraq |
| 749. | conference | 12: [11, 5.5], 18: [16, 8.0] | conference 's bush | Bush_family |
| 750. | police | 19: [24, 8.0], 32: [30, 6.0] | police 's world | Interpol |
| 751. | pressure | 38: [16, 8.0], 50: [17, 5.67] | pressure 's bush | George_H._W._Bush |
| 752. | law | 42: [16, 8.0] | law 's world | Parkinson's_law |
| 753. | washington | 49: [16, 8.0] | washington 's bush | Bush_family |
| 754. | vote | 17: [31, 7.75], 30: [11, 5.5] | vote 's party | Party-line_vote |
| 755. | party | 12: [23, 7.67], 38: [32, 6.4] | party 's government | Federal_government_of_the_United_States |
| 756. | campaign | 14: [19, 6.33], 33: [23, 7.67], 46: [11, 5.5] | campaign 's bush | Jeb_Bush_2016_presidential_campaign |
| 757. | politics | 16: [23, 7.67] | politics function 's | Politics |
| 758. | maps | 4: [15, 7.5] | maps 's photos | Google_Maps |
| 759. | rights | 5: [10, 5.0], 33: [15, 7.5] | rights 's human | Human_rights |
| 760. | control | 8: [15, 7.5], 14: [12, 6.0] | control 's government | Divided_government_in_the_United_States |
| 761. | suspected | 9: [15, 5.0], 20: [13, 6.5], 24: [15, 7.5], 29: [11, 5.5] | suspected qaeda 's | Al-Qaeda_insurgency_in_Yemen |
| 762. | helicopters | 10: [15, 7.5] | helicopters israeli palestinian | Timeline_of_the_Israeli–Palestinian_conflict |
| 763. | ramallah | 11: [15, 7.5] | ramallah arafat israeli | Ramallah |
| 764. | france | 11: [15, 7.5] | france 's french | France |
| 765. | market | 15: [15, 7.5] | market 's photo | Google_Photos |
| 766. | -- | 16: [30, 6.0], 27: [12, 6.0], 34: [12, 6.0], 43: [25, 6.25], 46: [15, 7.5] | -- 's function | Green's_function |
| 767. | ties | 17: [12, 6.0], 42: [15, 7.5] | ties 's qaeda | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 768. | myanmar | 17: [15, 7.5] | myanmar world asia | Myanmar |
| 769. | seized | 18: [15, 7.5] | seized 's officials | Harry_S._Truman |
| 770. | parties | 19: [11, 5.5], 40: [15, 7.5] | parties 's political | Political_parties_in_the_United_States |
| 771. | interim | 24: [15, 7.5] | interim 's government | Syrian_Interim_Government |
| 772. | oil | 38: [30, 7.5] | oil 's iraq | Oil_reserves_in_Iraq |
| 773. | vietnamese | 45: [15, 7.5] | vietnamese vietnam world | Flag_of_South_Vietnam |
| 774. | east | 9: [17, 5.67], 14: [52, 7.43], 48: [22, 7.33] | east middle 's | Middle_East |
| 775. | convention | 5: [22, 7.33] | convention 's united | Convention_on_the_Rights_of_the_Child |
| 776. | front | 16: [22, 7.33] | front function 's | T-front |
| 777. | plot | 37: [22, 7.33] | plot 's say | Family_Plot |
| 778. | forces | 39: [29, 7.25] | forces 's israeli | Israel_Defense_Forces |
| 779. | plans | 2: [13, 6.5], 11: [14, 7.0] | plans 's bush | George_W._Bush |
| 780. | days | 2: [12, 6.0], 44: [14, 7.0] | days 's israeli | Six-Day_War |
| 781. | germany | 2: [10, 5.0], 46: [14, 7.0] | germany 's german | Germany |
| 782. | several | 5: [14, 7.0] | several 's says | Gulliver's_Travels |
| 783. | peace | 8: [28, 7.0] | peace 's israel | Egypt–Israel_peace_treaty |
| 784. | chinese | 9: [16, 5.33], 39: [14, 7.0] | chinese china 's | China |
| 785. | middle | 14: [41, 5.86], 48: [14, 7.0] | middle east 's | Middle_East |
| 786. | taking | 14: [11, 5.5], 39: [14, 7.0] | taking 's government | Government_of_India |
| 787. | health | 16: [28, 7.0], 40: [13, 6.5] | health function 's | Mental_health |
| 788. | cabinet | 24: [14, 7.0] | cabinet 's palestinian | Palestinian_National_Authority |
| 789. | family | 25: [11, 5.5], 39: [14, 7.0], 42: [11, 5.5] | family 's says | Family_of_Donald_Trump |
| 790. | force | 29: [14, 7.0], 47: [16, 5.33] | force 's iraq | Multi-National_Force_–_Iraq |
| 791. | issue | 37: [21, 7.0] | issue 's north | The_Big_Issue |
| 792. | embassies | 37: [14, 7.0] | embassies qaeda north | Al-Qaeda |
| 793. | links | 37: [14, 7.0] | links 's qaeda | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 794. | democratic | 39: [14, 7.0] | democratic 's party | Democratic_Party_(United_States) |
| 795. | number | 46: [14, 7.0] | number 's says | Say_Say_Say |
| 796. | americas | 16: [27, 6.75] | americas world briefing | 1211_Avenue_of_the_Americas |
| 797. | attend | 13: [20, 6.67] | attend 's meeting | List_of_Bilderberg_participants |
| 798. | meet | 15: [20, 6.67] | meet 's bush | George_H._W._Bush |
| 799. | least | 2: [15, 5.0], 9: [15, 5.0], 41: [13, 6.5] | least 's israeli | Israel–United_States_relations |
| 800. | international | 2: [13, 6.5] | international 's says | International_relations |
| 801. | cases | 2: [12, 6.0], 5: [13, 6.5] | cases 's world | U.S._News_&_World_Report |
| 802. | operations | 3: [13, 6.5] | operations 's qaeda | Al-Qaeda |
| 803. | workers | 9: [13, 6.5] | workers 's strike | Strike_action |
| 804. | prosecutors | 9: [13, 6.5] | prosecutors 's milosevic | Slobodan_Milošević |
| 805. | weapons | 9: [10, 5.0], 20: [26, 6.5] | weapons iraq 's | Iraq_and_weapons_of_mass_destruction |
| 806. | little | 16: [13, 6.5], 25: [10, 5.0] | little 's bush | Prescott_Bush |
| 807. | dollars | 17: [13, 6.5] | dollars 's millions | Million_Dollar_Baby |
| 808. | authority | 19: [13, 6.5] | authority palestinian 's | Palestinian_National_Authority |
| 809. | india | 20: [21, 5.25], 37: [13, 6.5] | india pakistan 's | India–Pakistan_relations |
| 810. | win | 20: [10, 5.0], 39: [13, 6.5] | win 's party | WIN_Party |
| 811. | indian | 20: [10, 5.0], 33: [13, 6.5] | indian india pakistan | India–Pakistan_relations |
| 812. | election | 22: [13, 6.5] | election 's party | Political_party_strength_in_U.S._states |
| 813. | media | 22: [13, 6.5] | media 's news | News_media |
| 814. | criminal | 27: [19, 6.33], 35: [13, 6.5] | criminal court 's | International_Criminal_Court |
| 815. | including | 29: [13, 6.5] | including 's bush | Bush_family |
| 816. | environment | 35: [13, 6.5] | environment world 's | World_Environment_Day |
| 817. | sept. | 36: [13, 6.5] | sept. attacks 's | September_11_attacks |
| 818. | runoff | 41: [13, 6.5] | runoff 's pen | Two-round_system |
| 819. | even | 41: [13, 6.5], 52: [25, 6.25] | even 's bush | George_H._W._Bush |
| 820. | ship | 47: [13, 6.5] | ship 's north | The_North_Ship |
| 821. | life | 47: [13, 6.5] | life 's photo | Dwayne's_Photo |
| 822. | questions | 47: [13, 6.5] | questions 's bush | George_H._W._Bush |
| 823. | culture | 47: [13, 6.5] | culture 's photos | Google_Photos |
| 824. | declaration | 49: [13, 6.5] | declaration 's iraq | Declaration_of_war |
| 825. | west | 14: [77, 6.42] | west israeli palestinian | Israeli–Palestinian_conflict |
| 826. | nations | 30: [19, 6.33], 35: [52, 5.2] | nations united 's | United_Nations |
| 827. | around | 39: [19, 6.33] | around 's world | Around_the_World_in_Eighty_Days |
| 828. | foreign | 5: [25, 6.25] | foreign 's says | List_of_countries_by_foreign-exchange_reserves |
| 829. | led | 3: [11, 5.5], 13: [12, 6.0] | led 's government | LED_lamp |
| 830. | supreme | 5: [12, 6.0] | supreme court 's | Supreme_Court_of_the_United_States |
| 831. | children | 7: [18, 6.0], 9: [12, 6.0], 30: [11, 5.5], 50: [12, 6.0] | children 's world | Children_of_the_World |
| 832. | detained | 7: [12, 6.0] | detained 's says | List_of_foreign_nationals_detained_in_North_Korea |
| 833. | way | 9: [12, 6.0] | way 's says | No_Way_to_Say |
| 834. | congo | 9: [12, 6.0] | congo africa talks | Second_Congo_War |
| 835. | help | 11: [12, 6.0] | help 's american | Help! |
| 836. | army | 11: [12, 6.0] | army 's israeli | Israel_Defense_Forces |
| 837. | chief | 14: [12, 6.0] | chief 's says | Chief_executive_officer |
| 838. | secretary | 14: [18, 6.0], 42: [10, 5.0] | secretary 's powell | Colin_Powell |
| 839. | thousands | 15: [18, 6.0] | thousands 's government | Decimal_separator |
| 840. | leading | 15: [12, 6.0] | leading 's world | The_Leading_Hotels_of_the_World |
| 841. | role | 16: [18, 6.0] | role 's bush | George_H._W._Bush |
| 842. | effort | 18: [15, 5.0], 22: [12, 6.0], 40: [11, 5.5] | effort 's bush | George_H._W._Bush |
| 843. | largest | 18: [12, 6.0] | largest 's government | List_of_United_States_cities_by_population |
| 844. | away | 24: [12, 6.0] | away 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 845. | might | 27: [12, 6.0], 36: [11, 5.5] | might 's bush | Cori_Bush |
| 846. | injured | 28: [12, 6.0] | injured killed 's | Killed_or_Seriously_Injured |
| 847. | data | 28: [12, 6.0] | data 's iraq | Casualties_of_the_Iraq_War |
| 848. | public | 29: [10, 5.0], 35: [12, 6.0] | public 's says | Say's_law |
| 849. | meets | 31: [12, 6.0] | meets 's bush | George_H._W._Bush |
| 850. | paul | 33: [12, 6.0] | paul 's pope | Pope_John_Paul_II |
| 851. | prisoners | 34: [12, 6.0] | prisoners 's says | Prisoner's_dilemma |
| 852. | poverty | 35: [12, 6.0] | poverty 's world | Poverty_in_India |
| 853. | suicide | 35: [12, 6.0] | suicide israeli palestinian | List_of_Palestinian_suicide_attacks |
| 854. | struggle | 35: [12, 6.0], 43: [11, 5.5] | struggle 's us | U.S._state |
| 855. | increase | 37: [12, 6.0] | increase 's government | Increase_Mather |
| 856. | evidence | 41: [12, 6.0], 49: [18, 6.0] | evidence 's says | Hitchens's_razor |
| 857. | paramilitary | 41: [12, 6.0] | paramilitary northern ireland | Paramilitary_punishment_attacks_in_Northern_Ireland |
| 858. | destruction | 41: [12, 6.0] | destruction iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 859. | australians | 42: [12, 6.0] | australians bombing indonesia | 2002_Bali_bombings |
| 860. | explosives | 42: [12, 6.0] | explosives 's police | Police_dog |
| 861. | bashir | 42: [12, 6.0] | bashir indonesia group | Abu_Bakar_Ba'asyir |
| 862. | leadership | 43: [12, 6.0] | leadership 's party | 2020_Labour_Party_leadership_election_(UK) |
| 863. | communist | 45: [12, 6.0] | communist 's party | Chinese_Communist_Party |
| 864. | tried | 47: [12, 6.0] | tried 's says | That_'70s_Show |
| 865. | haider | 48: [12, 6.0] | haider 's austria | Jörg_Haider |
| 866. | rule | 49: [12, 6.0] | rule 's government | President's_rule |
| 867. | expansion | 50: [12, 6.0] | expansion 's european | Enlargement_of_the_European_Union |
| 868. | afghan | 51: [12, 6.0] | afghan afghanistan 's | Flag_of_Afghanistan |
| 869. | agency | 52: [12, 6.0] | agency 's says | National_Security_Agency |
| 870. | jenin | 15: [35, 5.83] | jenin israeli israel | List_of_wars_involving_Israel |
| 871. | members | 13: [15, 5.0], 50: [29, 5.8] | members 's say | Say_Say_Say |
| 872. | united | 2: [52, 5.78] | united 's states | United_States |
| 873. | arrest | 13: [10, 5.0], 19: [23, 5.75] | arrest 's police | Arrest |
| 874. | house | 41: [23, 5.75] | house 's bush | George_W._Bush |
| 875. | islamic | 41: [21, 5.25], 48: [23, 5.75] | islamic 's pakistan | Islam_in_Pakistan |
| 876. | within | 5: [17, 5.67] | within 's bush | George_H._W._Bush |
| 877. | strike | 9: [17, 5.67], 37: [10, 5.0] | strike 's government | UK_miners'_strike_(1984–85) |
| 878. | britain | 14: [17, 5.67], 39: [32, 5.33] | britain 's europe | Britain_in_Europe |
| 879. | whether | 33: [10, 5.0], 35: [17, 5.67] | whether 's says | Say's_law |
| 880. | western | 39: [17, 5.67] | western 's government | Government_of_Western_Australia |
| 881. | may | 30: [28, 5.6] | may 's say | Say's_law |
| 882. | europe | 14: [50, 5.56] | europe world briefing | BBC_World_News |
| 883. | states | 2: [44, 5.5] | states united 's | United_States |
| 884. | alive | 6: [11, 5.5] | alive laden says | Tere_Bin_Laden:_Dead_or_Alive |
| 885. | action | 7: [11, 5.5], 17: [10, 5.0] | action iraq 's | 2003_invasion_of_Iraq |
| 886. | weeks | 8: [11, 5.5], 36: [10, 5.0] | weeks 's bush | George_H._W._Bush |
| 887. | omar | 9: [11, 5.5] | omar pearl sheikh | Ahmed_Omar_Saeed_Sheikh |
| 888. | withdrawal | 11: [11, 5.5] | withdrawal israeli israel | Israel |
| 889. | agents | 12: [11, 5.5] | agents 's qaeda | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 890. | conflict | 14: [22, 5.5] | conflict 's israeli | Israeli–Palestinian_conflict |
| 891. | annan | 15: [11, 5.5] | annan kofi iraq | Kofi_Annan |
| 892. | offer | 15: [11, 5.5] | offer 's bush | George_H._W._Bush |
| 893. | removed | 16: [11, 5.5] | removed 's iraq | Iraq |
| 894. | immigrant | 17: [11, 5.5] | immigrant immigrants 's | Immigrant_Song |
| 895. | run | 20: [11, 5.5] | run 's world | Run_the_World_(Girls) |
| 896. | coalition | 20: [11, 5.5] | coalition 's government | Coalition_government |
| 897. | referendum | 20: [11, 5.5] | referendum 's government | 2020_Puerto_Rican_status_referendum |
| 898. | latin | 20: [11, 5.5] | latin 's america | Latin_America |
| 899. | hussein | 28: [11, 5.5], 31: [26, 5.2], 34: [16, 5.33] | hussein iraq 's | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 900. | senior | 28: [11, 5.5] | senior 's officials | Senior_administration_official |
| 901. | state-owned | 29: [11, 5.5] | state-owned 's government | List_of_government-owned_companies |
| 902. | account | 30: [11, 5.5] | account 's says | Transaction_account |
| 903. | site | 32: [11, 5.5] | site 's attack | Cross-site_scripting |
| 904. | eviction | 33: [11, 5.5] | eviction farmers zimbabwe | White_people_in_Zimbabwe |
| 905. | discuss | 36: [11, 5.5] | discuss 's pres | Ulysses_S._Grant |
| 906. | act | 37: [11, 5.5] | act 's says | Dirty_Sanchez_(sexual_act) |
| 907. | inspections | 38: [11, 5.5] | inspections iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 908. | compound | 38: [11, 5.5] | compound israeli arafat | Mukataa |
| 909. | using | 43: [11, 5.5] | using 's bush | George_W._Bush |
| 910. | powerful | 43: [11, 5.5] | powerful 's government | Government_of_the_United_Kingdom |
| 911. | ariel | 44: [11, 5.5] | ariel sharon israeli | Ariel_Sharon |
| 912. | corruption | 45: [11, 5.5] | corruption 's party | Anti-Corruption_Party |
| 913. | named | 46: [11, 5.5] | named 's police | United_States_Capitol_Police |
| 914. | hard-line | 46: [11, 5.5] | hard-line 's government | Hardline |
| 915. | meeting | 43: [27, 5.4] | meeting 's bush | George_H._W._Bush |
| 916. | saddam | 31: [16, 5.33] | saddam iraq hussein | Saddam's_family |
| 917. | still | 31: [16, 5.33] | still 's say | We_Still_Say_Grace |
| 918. | basque | 35: [16, 5.33] | basque group spain | Basques |
| 919. | italian | 37: [10, 5.0], 46: [16, 5.33] | italian 's italy | Demographics_of_Italy |
| 920. | netanyahu | 45: [16, 5.33] | netanyahu sharon prime | Prime_Minister_of_Israel |
| 921. | royal | 46: [16, 5.33] | royal 's saudi | Royal_Saudi_Air_Force |
| 922. | court | 2: [21, 5.25] | court 's world | International_Court_of_Justice |
| 923. | street | 5: [21, 5.25] | street 's pearl | Pearl_Street_Mall |
| 924. | korea | 11: [30, 5.0], 26: [21, 5.25] | korea north south | North_Korea–South_Korea_relations |
| 925. | second | 17: [21, 5.25] | second 's israeli | Israel |
| 926. | murder | 17: [21, 5.25] | murder 's pearl | Murder_of_Pearl_Bryan |
| 927. | administration | 30: [21, 5.25] | administration bush 's | Presidency_of_George_W._Bush |
| 928. | trade | 44: [21, 5.25] | trade 's bush | George_H._W._Bush |
| 929. | former | 50: [21, 5.25] | former 's world | Annals_of_the_Former_World |
| 930. | jihad | 2: [10, 5.0] | jihad palestinian islamic | Islamic_Jihad_Movement_in_Palestine |
| 931. | seek | 3: [10, 5.0] | seek 's iraq | Iraq |
| 932. | escape | 4: [10, 5.0] | escape 's american | Escape_Room_2 |
| 933. | try | 5: [10, 5.0] | try 's bush | George_H._W._Bush |
| 934. | find | 5: [10, 5.0], 48: [10, 5.0] | find 's american | Findability |
| 935. | orders | 5: [15, 5.0] | orders 's government | Federal_government_of_the_United_States |
| 936. | tony | 7: [10, 5.0] | tony blair 's | Tony_Blair |
| 937. | relations | 9: [10, 5.0] | relations 's says | Neorealism_(international_relations) |
| 938. | recently | 9: [10, 5.0] | recently 's american | Borat_Subsequent_Moviefilm |
| 939. | mideast | 9: [15, 5.0] | mideast bush 's | George_W._Bush |
| 940. | hard | 10: [10, 5.0] | hard 's bush | Bushism |
| 941. | toward | 10: [10, 5.0] | toward 's bush | George_H._W._Bush |
| 942. | years | 11: [25, 5.0] | years 's government | Federal_government_of_the_United_States |
| 943. | iranian | 11: [10, 5.0] | iranian iran 's | Iran–United_States_relations |
| 944. | three | 12: [20, 5.0] | three 's israeli | Nuclear_weapons_and_Israel |
| 945. | warn | 13: [10, 5.0] | warn 's bush | George_H._W._Bush |
| 946. | league | 13: [20, 5.0] | league arab 's | Arab_League |
| 947. | berlusconi | 13: [10, 5.0] | berlusconi 's italy | Paolo_Berlusconi |
| 948. | resignation | 13: [10, 5.0] | resignation 's party | Resignation |
| 949. | cooperation | 14: [10, 5.0] | cooperation 's us | India–United_States_relations |
| 950. | make | 14: [15, 5.0] | make 's bush | George_W._Bush |
| 951. | spain | 16: [10, 5.0], 35: [10, 5.0] | spain europe 's | Spain |
| 952. | chávez | 16: [10, 5.0] | chávez chavez venezuela | Hugo_Chávez |
| 953. | conservative | 16: [10, 5.0] | conservative 's party | Conservative_Party_(UK) |
| 954. | although | 16: [10, 5.0] | although 's says | Say's_law |
| 955. | uprising | 16: [10, 5.0] | uprising 's chavez | History_of_Venezuela_(1999–present) |
| 956. | demanding | 17: [10, 5.0] | demanding 's bush | Bush_shoeing_incident |
| 957. | pentagon | 17: [10, 5.0] | pentagon american 's | Pentagon |
| 958. | envoy | 17: [15, 5.0] | envoy 's bush | United_States_Special_Envoy_for_Northern_Ireland |
| 959. | biological | 20: [10, 5.0] | biological iraq weapons | Iraqi_biological_weapons_program |
| 960. | nearly | 20: [15, 5.0] | nearly 's government | Government_of_India |
| 961. | place | 20: [10, 5.0] | place 's say | Say's_law |
| 962. | re-election | 20: [10, 5.0] | re-election 's party | 1956_United_States_Senate_elections |
| 963. | soccer | 20: [10, 5.0] | soccer world cup | FIFA_World_Cup |
| 964. | among | 22: [15, 5.0] | among 's officials | Among_Us |
| 965. | libya | 22: [10, 5.0] | libya says israel | Second_Libyan_Civil_War |
| 966. | dead | 24: [10, 5.0], 34: [10, 5.0], 49: [10, 5.0] | dead 's israeli | Dead_Sea |
| 967. | southern | 27: [20, 5.0] | southern 's american | Southern_American_English |
| 968. | legislation | 30: [10, 5.0] | legislation 's government | Federal_government_of_the_United_States |
| 969. | southeast | 31: [10, 5.0] | southeast asia 's | Southeast_Asia |
| 970. | iraqi | 31: [10, 5.0] | iraqi iraq 's | Iraqi_Kurdistan |
| 971. | billion | 32: [10, 5.0] | billion 's aid | Rite_Aid |
| 972. | time | 33: [10, 5.0] | time 's says | Time_to_Say_Goodbye |
| 973. | texas | 33: [10, 5.0] | texas 's bush | George_W._Bush |
| 974. | arrests | 34: [10, 5.0] | arrests 's qaeda | Al-Qaeda |
| 975. | chechen | 34: [10, 5.0] | chechen russia russian | Chechen–Russian_conflict |
| 976. | along | 34: [10, 5.0] | along 's pakistan | Pakistan |
| 977. | hague | 35: [10, 5.0] | hague milosevic crimes | Trial_of_Slobodan_Milošević |
| 978. | problems | 35: [10, 5.0] | problems 's world | First_World_problem |
| 979. | swedish | 35: [10, 5.0] | swedish chatty sweden | Kerim_Chatty |
| 980. | kabul | 36: [10, 5.0] | kabul afghanistan afghan | Kabul |
| 981. | well | 37: [10, 5.0] | well 's says | Say's_law |
| 982. | google | 37: [10, 5.0] | google china access | Google_China |
| 983. | tells | 38: [10, 5.0] | tells 's says | Simon_Says |
| 984. | broad | 39: [10, 5.0] | broad 's bush | George_H._W._Bush |
| 985. | human | 39: [10, 5.0] | human rights 's | Human_rights |
| 986. | tribunal | 40: [10, 5.0] | tribunal crimes milosevic | Trial_of_Slobodan_Milošević |
| 987. | capital | 41: [15, 5.0] | capital 's world | World_Book_Capital |
| 988. | training | 41: [10, 5.0] | training military 's | Recruit_training |
| 989. | enforcement | 42: [10, 5.0] | enforcement law officials | Federal_law_enforcement_in_the_United_States |
| 990. | australia | 42: [10, 5.0] | australia 's government | Australian_Government |
| 991. | islamiyah | 42: [10, 5.0] | islamiyah indonesia group | Jemaah_Islamiyah |
| 992. | shift | 43: [10, 5.0] | shift 's bush | George_H._W._Bush |
| 993. | jail | 45: [10, 5.0] | jail 's years | Lumpkin's_Jail |
| 994. | probe | 45: [10, 5.0] | probe 's police | Ford_Probe |
| 995. | programs | 46: [10, 5.0] | programs 's iraq | Iraq_and_weapons_of_mass_destruction |
| 996. | tons | 47: [10, 5.0] | tons 's korea | List_of_active_ships_of_the_Korean_People's_Navy |
| 997. | disarm | 49: [10, 5.0] | disarm iraq bush | 2003_invasion_of_Iraq |
| 998. | paris | 50: [10, 5.0] | paris 's france | Paris |
| 999. | movement | 50: [10, 5.0] | movement 's says | Boogaloo_movement |
| 1000. | bases | 50: [10, 5.0] | bases military iraq | List_of_United_States_military_bases |
| 1001. | genoa | 50: [10, 5.0] | genoa italy police | Genoa |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | world | 6: [14, 7.0], 10: [11, inf] | world brief 's | World_Prison_Brief |
| 2. | guide | 6: [10, inf] | guide world news | News_of_the_World_(film) |
| 3. | pen | 17: [17, inf] | pen 's chirac | Jacques_Chirac |
| 4. | bali | 42: [28, 9.33] | bali bombing bomb | 2002_Bali_bombings |
| 5. | arafat | 13: [12, 6.0], 18: [10, 5.0] | arafat 's israel | Yasser_Arafat |
| 6. | milosevic | 7: [11, 5.5] | milosevic trial hague | Death_of_Slobodan_Milošević |
| 7. | mugabe | 9: [10, 5.0] | mugabe 's britain | Robert_Mugabe |
| 8. | israel | 13: [10, 5.0] | israel 's arafat | Yasser_Arafat |
| 9. | french | 17: [10, 5.0] | french left us | Left-wing_politics |
| 10. | pakistan | 21: [10, 5.0] | pakistan india 's | India–Pakistan_relations |
