# Keywords with the highest 'interestingness' in 2001

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
| 1. | argentine | 2: [10, inf], 44: [10, 5.0], 51: [13, inf] | argentine argentina 's | Argentina |
| 2. | european | 2: [12, inf], 33: [13, 13.0], 35: [13, inf] | european 's union | European_Union |
| 3. | navy | 2: [10, 10.0], 14: [12, inf] | navy plane 's | Doomsday_plane |
| 4. | oil | 2: [14, inf], 4: [18, 9.0], 7: [13, 13.0], 22: [11, inf], 33: [12, inf] | oil 's iraq | Oil_reserves_in_Iraq |
| 5. | bosnian | 2: [20, inf], 27: [14, 14.0] | bosnian serb crimes | Bosnian_War |
| 6. | serb | 2: [19, inf], 31: [12, 6.0] | serb bosnian crimes | Bosnian_War |
| 7. | schroder | 2: [10, 5.0], 21: [10, inf] | schroder germany chancellor | Gerhard_Schröder |
| 8. | mad | 2: [14, inf] | mad cow disease | Bovine_spongiform_encephalopathy |
| 9. | cow | 2: [14, inf], 12: [10, 10.0] | cow mad disease | Bovine_spongiform_encephalopathy |
| 10. | disease | 2: [14, 14.0], 6: [10, 5.0], 34: [10, inf] | disease foot-and-mouth 's | Foot-and-mouth_disease |
| 11. | depleted | 2: [10, inf] | depleted uranium nato | Depleted_uranium |
| 12. | kosovo | 2: [11, inf], 5: [30, 15.0], 23: [12, 6.0], 46: [13, inf] | kosovo nato 's | Kosovo_War |
| 13. | civilians | 2: [11, inf] | civilians 's photo | Civilian_casualties_in_the_war_in_Afghanistan_(2001–present) |
| 14. | turkey | 2: [15, inf], 17: [15, 5.0], 23: [22, 7.33] | turkey 's world | Turkey |
| 15. | lockerbie | 2: [20, inf], 5: [23, inf] | lockerbie trial bombing | Pan_Am_Flight_103 |
| 16. | prosecutor | 2: [10, inf] | prosecutor tribunal 's | International_Criminal_Tribunal_for_Rwanda |
| 17. | plavsic | 2: [12, inf] | plavsic serb bosnian | Biljana_Plavšić |
| 18. | pilot | 2: [10, inf], 14: [12, inf], 17: [17, 5.67] | pilot chinese plane | Hainan_Island_incident |
| 19. | quebec | 2: [10, inf], 16: [10, 5.0] | quebec trade americas | Free_Trade_Area_of_the_Americas |
| 20. | bouchard | 2: [10, inf] | bouchard quebec premier | Lucien_Bouchard |
| 21. | britain | 3: [11, inf], 8: [22, 7.33] | britain 's british | Britishness |
| 22. | airport | 3: [11, inf] | airport 's afghanistan | Kandahar_International_Airport |
| 23. | congo | 3: [30, inf] | congo kabila 's | Laurent-Désiré_Kabila |
| 24. | laurent | 3: [15, inf] | laurent kabila congo | Laurent-Désiré_Kabila |
| 25. | kabila | 3: [34, inf] | kabila congo 's | Joseph_Kabila |
| 26. | shanghai | 3: [10, inf], 42: [25, inf] | shanghai bush china | Jiang_Mianheng |
| 27. | church | 4: [11, inf], 8: [12, inf] | church pope 's | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 28. | colombia | 4: [16, inf] | colombia 's colombian | Colombians |
| 29. | despite | 4: [11, inf], 23: [13, 6.5], 42: [10, 5.0] | despite 's us | United_States |
| 30. | tanker | 4: [10, inf] | tanker oil galapagos | Galápagos_Islands |
| 31. | galapagos | 4: [10, inf] | galapagos oil tanker | Galápagos_Islands |
| 32. | india | 4: [31, 10.33], 14: [10, inf], 19: [17, 17.0], 23: [10, 5.0] | india 's pakistan | India–Pakistan_relations |
| 33. | blair | 4: [16, 16.0], 8: [18, inf], 14: [14, 14.0], 23: [16, 8.0], 40: [43, 43.0], 51: [11, 11.0] | blair 's prime | Premiership_of_Tony_Blair |
| 34. | media-most | 4: [10, inf] | media-most gusinsky 's | Vladimir_Gusinsky |
| 35. | wahid | 4: [10, inf], 22: [26, inf] | wahid indonesia 's | Abdurrahman_Wahid |
| 36. | politics | 5: [12, 6.0], 30: [10, 5.0], 41: [17, inf] | politics 's party | Political_parties_in_the_United_States |
| 37. | dead | 5: [22, 7.33], 13: [10, inf], 21: [15, 7.5] | dead 's people | Conversations_with_Dead_People |
| 38. | pinochet | 5: [11, inf] | pinochet chile augusto | Lucía_Pinochet |
| 39. | ordered | 5: [14, inf] | ordered 's american | Ordered_field |
| 40. | house | 5: [15, inf], 8: [10, inf] | house 's bush | George_W._Bush |
| 41. | found | 5: [10, inf], 14: [12, 6.0], 27: [12, inf] | found 's world | HTTP_404 |
| 42. | way | 5: [10, 5.0], 14: [10, 5.0], 38: [15, inf], 50: [14, 7.0] | way 's says | Hey,_That's_No_Way_to_Say_Goodbye |
| 43. | mexico | 5: [23, 7.67], 28: [16, 5.33], 31: [13, inf], 43: [11, 5.5] | mexico 's fox | Vicente_Fox |
| 44. | interview | 5: [10, inf], 32: [16, 5.33] | interview 's says | The_Interview |
| 45. | appears | 5: [10, 5.0], 40: [10, inf] | appears 's bush | George_H._W._Bush |
| 46. | decision | 5: [13, 6.5], 38: [11, inf] | decision 's bush | Bush_v._Gore |
| 47. | libyans | 5: [13, inf] | libyans trial lockerbie | Pan_Am_Flight_103 |
| 48. | bombing | 5: [29, inf], 8: [10, inf], 21: [17, 5.67], 30: [12, 12.0], 32: [11, 5.5] | bombing taliban american | Taliban_insurgency |
| 49. | finds | 5: [10, inf], 31: [16, 16.0], 48: [10, 10.0] | finds 's world | Findability |
| 50. | verdict | 5: [30, inf] | verdict trial guilty | Not_proven |
| 51. | guilty | 5: [18, inf] | guilty trial 's | Impeachment_of_Bill_Clinton |
| 52. | goes | 5: [11, inf] | goes 's world | The_Go-Go's |
| 53. | pan | 5: [15, inf] | pan bombing lockerbie | Pan_Am_Flight_103 |
| 54. | plant | 5: [10, inf] | plant 's nuclear | Chernobyl_Nuclear_Power_Plant |
| 55. | legislature | 5: [10, inf] | legislature 's president | President_of_the_United_States |
| 56. | growth | 5: [10, inf] | growth 's economic | Economic_growth |
| 57. | libyan | 5: [16, inf] | libyan lockerbie bombing | Pan_Am_Flight_103 |
| 58. | albanians | 5: [10, inf], 26: [10, 10.0] | albanians macedonia kosovo | Kosovo_Albanians |
| 59. | libya | 5: [18, inf] | libya bombing sanctions | Pan_Am_Flight_103 |
| 60. | democratic | 6: [10, inf], 17: [18, 6.0], 37: [11, inf] | democratic 's party | Democratic_Party_(United_States) |
| 61. | canada | 6: [13, inf], 20: [10, inf] | canada 's world | Canada_in_World_War_II |
| 62. | borders | 6: [12, inf] | borders 's says | Canada–United_States_border |
| 63. | aristide | 6: [11, inf] | aristide haiti opposition | Jean-Bertrand_Aristide |
| 64. | victory | 6: [17, inf], 31: [13, inf] | victory 's party | Victory_Party |
| 65. | unity | 6: [10, inf] | unity 's sharon | 2003_Israeli_legislative_election |
| 66. | coalition | 6: [10, inf], 17: [13, inf] | coalition 's government | Coalition_government |
| 67. | form | 6: [10, inf] | form 's government | List_of_forms_of_government |
| 68. | arsenal | 6: [10, inf] | arsenal 's nuclear | Nuclear_weapons_of_the_United_States |
| 69. | milosevic | 6: [12, inf], 13: [16, inf], 26: [45, 11.25], 31: [12, 12.0], 34: [13, inf] | milosevic tribunal crimes | Trial_of_Slobodan_Milošević |
| 70. | gaza | 7: [10, 5.0], 18: [11, inf], 47: [14, 7.0], 49: [18, 18.0] | gaza israeli palestinian | Gaza_War_(2008–2009) |
| 71. | ukraine | 7: [18, inf], 41: [20, 5.0], 43: [14, 14.0] | ukraine 's kuchma | Leonid_Kuchma |
| 72. | week | 7: [10, 10.0], 18: [10, inf] | week 's last | Last_Week_Tonight_with_John_Oliver |
| 73. | food | 7: [12, inf], 40: [20, 5.0] | food 's taliban | Taliban |
| 74. | torture | 7: [10, inf], 36: [10, inf] | torture 's rights | Torture |
| 75. | general | 7: [12, inf], 17: [11, inf], 44: [10, 5.0] | general 's united | United_States_Attorney_General |
| 76. | human | 7: [10, 5.0], 16: [13, inf], 52: [17, 8.5] | human rights 's | Human_rights |
| 77. | bus | 7: [19, inf] | bus palestinian israeli | Israeli–Palestinian_conflict |
| 78. | zone | 7: [10, inf], 9: [10, 10.0], 11: [14, 7.0] | zone 's kosovo | Kosovo–Serbia_relations |
| 79. | iraqi | 7: [12, inf], 27: [11, inf] | iraqi iraq hussein | Saddam_Hussein |
| 80. | korea | 8: [17, inf], 13: [26, 13.0], 18: [15, inf], 23: [24, inf] | korea north south | North_Korea–South_Korea_relations |
| 81. | keep | 8: [11, inf] | keep 's taliban | Taliban |
| 82. | refugees | 8: [11, 11.0], 17: [18, inf] | refugees 's taliban | Taliban |
| 83. | aid | 8: [16, 5.33], 17: [12, inf], 22: [13, 13.0] | aid 's afghanistan | Phantom_aid_in_Afghanistan |
| 84. | saddam | 8: [10, inf] | saddam iraq hussein | Saddam's_family |
| 85. | hussein | 8: [12, inf], 51: [11, 5.5] | hussein iraq saddam | Saddam's_family |
| 86. | basque | 8: [13, inf], 19: [12, inf], 44: [14, inf] | basque group eta | ETA_(separatist_group) |
| 87. | pope | 8: [10, inf], 18: [16, inf], 25: [11, inf], 38: [15, 7.5], 43: [12, 6.0] | pope paul john | Pope_John_Paul_II |
| 88. | defenses | 8: [13, inf] | defenses missile bush | Missile_defense |
| 89. | arrest | 8: [14, inf], 30: [11, inf] | arrest 's police | Arrest |
| 90. | coca | 8: [10, inf], 11: [12, inf] | coca colombia 's | Coca_production_in_Colombia |
| 91. | orthodox | 8: [11, inf] | orthodox church pope | Pope_of_the_Coptic_Orthodox_Church_of_Alexandria |
| 92. | report | 9: [13, inf], 20: [18, 9.0], 27: [10, 5.0], 36: [14, 14.0] | report 's says | U.S._News_&_World_Report |
| 93. | money | 9: [18, 9.0], 19: [10, 5.0], 39: [14, inf], 45: [16, 5.33] | money 's united | United_States_dollar |
| 94. | citibank | 9: [12, inf] | citibank bank money | Citibank_India |
| 95. | bodies | 9: [11, inf], 31: [10, inf] | bodies 's taliban | Taliban |
| 96. | buffer | 9: [10, inf] | buffer zone kosovo | Insurgency_in_the_Preševo_Valley |
| 97. | department | 9: [10, inf] | department state 's | United_States_Department_of_State |
| 98. | mexican | 9: [11, inf], 14: [12, inf], 31: [14, inf], 36: [15, 15.0] | mexican mexico fox | Mexico |
| 99. | east | 9: [13, inf], 18: [12, inf], 31: [12, 12.0] | east middle 's | Middle_East |
| 100. | private | 10: [10, inf] | private 's government | Government |
| 101. | court | 10: [16, 16.0], 14: [19, inf], 39: [15, 15.0], 44: [17, 8.5], 46: [15, 7.5] | court 's world | International_Court_of_Justice |
| 102. | election | 10: [13, inf], 18: [14, 7.0], 34: [10, 5.0], 44: [10, inf] | election 's party | 2024_United_States_presidential_election |
| 103. | drugs | 10: [14, inf], 13: [26, inf], 16: [11, inf] | drugs aids africa | HIV/AIDS_denialism |
| 104. | trial | 10: [12, 6.0], 14: [26, inf], 20: [18, 6.0], 25: [12, 6.0] | trial 's former | O._J._Simpson_murder_case |
| 105. | companies | 10: [15, 7.5], 13: [10, inf] | companies 's drugs | Pharmaceutical_industry |
| 106. | hungary | 10: [12, inf] | hungary 's european | 2019_European_Parliament_election_in_Hungary |
| 107. | faces | 10: [11, inf], 50: [14, 7.0] | faces 's government | Government_shutdowns_in_the_United_States |
| 108. | school | 10: [14, 7.0], 23: [12, inf], 36: [16, inf], 51: [15, inf] | school 's children | Professional_Children's_School |
| 109. | ruling | 10: [11, inf], 31: [14, 7.0] | ruling 's taliban | Islamic_Emirate_of_Afghanistan |
| 110. | force | 10: [12, 12.0], 25: [14, 7.0], 36: [10, inf] | force 's military | United_States_Armed_Forces |
| 111. | payments | 10: [12, inf] | payments 's united | Global_Payments |
| 112. | macedonia | 10: [12, inf], 23: [12, inf] | macedonia albanian rebels | 2001_insurgency_in_Macedonia |
| 113. | macedonian | 10: [11, inf], 12: [23, 11.5] | macedonian albanian macedonia | Macedonian_front |
| 114. | free | 11: [14, inf], 31: [10, 5.0] | free 's trade | Free_trade |
| 115. | along | 11: [10, 5.0], 52: [11, inf] | along 's border | Migrant_deaths_along_the_Mexico–United_States_border |
| 116. | health | 11: [12, 6.0], 13: [18, inf], 35: [16, 16.0] | health 's world | World_Health_Organization |
| 117. | sales | 11: [16, inf] | sales 's arms | List_of_US_arms_sales_to_Taiwan |
| 118. | iran | 11: [21, 5.25], 18: [10, inf], 23: [11, 5.5] | iran 's afghanistan | Afghanistan–Iran_relations |
| 119. | blockade | 11: [14, inf] | blockade palestinian israeli | Israeli–Palestinian_conflict |
| 120. | kuwait | 11: [12, inf] | kuwait 's iraq | Invasion_of_Kuwait |
| 121. | paris | 11: [11, inf] | paris french 's | Paris |
| 122. | return | 11: [10, inf], 14: [23, inf], 47: [14, 7.0] | return 's photo | Google_Photos |
| 123. | bristol-myers | 11: [12, inf] | bristol-myers africa price | Emcure_Pharmaceuticals |
| 124. | criticism | 11: [11, inf] | criticism 's bush | Public_image_of_George_W._Bush |
| 125. | tunnel | 11: [13, inf], 43: [35, inf], 52: [13, inf] | tunnel france channel | Channel_Tunnel |
| 126. | immigrants | 11: [13, inf], 26: [12, 6.0], 36: [12, inf] | immigrants 's illegal | Illegal_immigration_to_the_United_States |
| 127. | saudi | 11: [14, inf], 22: [12, inf] | saudi arabia 's | Saudi_Arabia |
| 128. | intelligence | 12: [10, inf], 15: [12, 6.0] | intelligence 's us | United_States_Intelligence_Community |
| 129. | issues | 12: [13, 6.5], 28: [10, inf] | issues 's bush | Prescott_Bush |
| 130. | diplomats | 12: [15, inf] | diplomats 's american | Foreign_Service_Officer |
| 131. | leaders | 12: [16, inf] | leaders 's taliban | List_of_Taliban_leaders |
| 132. | ireland | 12: [12, 12.0], 15: [12, inf], 23: [21, 10.5], 31: [10, inf] | ireland northern 's | Northern_Ireland |
| 133. | scholar | 12: [12, inf], 30: [15, 15.0] | scholar chinese china | China |
| 134. | pigs | 12: [12, inf] | pigs disease bay | Pig |
| 135. | castro | 12: [10, inf] | castro 's pres | Fidel_Castro |
| 136. | kurdish | 12: [10, inf] | kurdish britain turkey | Kurds_in_Turkey |
| 137. | effort | 13: [13, 6.5], 31: [11, inf] | effort 's photo | Google_Photos |
| 138. | brazil | 13: [14, 14.0], 18: [14, 7.0], 41: [12, 6.0], 51: [20, inf] | brazil 's world | Brazil_v_Germany_(2014_FIFA_World_Cup) |
| 139. | prices | 13: [20, inf] | prices aids 's | HIV/AIDS |
| 140. | iraq | 13: [20, 20.0], 18: [10, 5.0], 20: [12, inf], 27: [10, 5.0], 35: [11, inf], 47: [11, 5.5] | iraq iraqi 's | Iraqis |
| 141. | toward | 13: [12, inf], 36: [10, 5.0], 45: [12, 12.0] | toward 's bush | George_H._W._Bush |
| 142. | council | 13: [11, inf] | council security 's | United_Nations_Security_Council |
| 143. | belgrade | 13: [12, inf] | belgrade milosevic tribunal | Slobodan_Milošević |
| 144. | chinese | 14: [106, 7.57], 26: [11, inf], 30: [48, 12.0] | chinese china 's | China |
| 145. | spy | 14: [59, 6.56], 26: [10, inf] | spy china chinese | China |
| 146. | surveillance | 14: [10, inf] | surveillance plane china | Surveillance_aircraft |
| 147. | fighter | 14: [29, inf] | fighter plane chinese | Mitsubishi_A6M_Zero |
| 148. | landing | 14: [18, inf] | landing plane china | Hainan_Island_incident |
| 149. | hainan | 14: [21, inf] | hainan plane china | Hainan_Island_incident |
| 150. | crew | 14: [79, inf] | crew china plane | Hainan_Island_incident |
| 151. | aircraft | 14: [18, inf] | aircraft american 's | All_American_(aircraft) |
| 152. | april | 14: [40, inf] | april 's china | China |
| 153. | sunday | 14: [17, inf] | sunday 's bush | Alaskan_Bush_People |
| 154. | collision | 14: [46, inf], 43: [11, 5.5] | collision china chinese | 1990_Guangzhou_Baiyun_airport_collisions |
| 155. | incident | 14: [18, inf] | incident 's china | Hainan_Island_incident |
| 156. | crimes | 14: [21, 5.25], 16: [14, inf], 22: [12, 6.0], 46: [15, 15.0] | crimes tribunal milosevic | Trial_of_Slobodan_Milošević |
| 157. | yugoslavia | 14: [17, 8.5], 23: [10, inf] | yugoslavia milosevic 's | Slobodan_Milošević |
| 158. | colin | 14: [18, 6.0], 26: [15, 5.0], 30: [25, 6.25], 42: [15, 7.5], 46: [10, inf] | colin powell 's | Colin_Powell |
| 159. | powell | 14: [30, 6.0], 26: [31, 5.17], 30: [51, 5.67], 35: [11, inf], 42: [29, 14.5], 46: [21, inf] | powell 's colin | Colin_Powell |
| 160. | delay | 14: [11, inf] | delay 's government | Tom_DeLay |
| 161. | long | 14: [10, inf], 24: [10, 10.0] | long 's says | Say's_law |
| 162. | regret | 14: [10, inf] | regret 's chinese | Chinese_Exclusion_Act |
| 163. | jiang | 14: [11, inf], 32: [27, inf], 42: [11, inf] | jiang china 's | Jiang_Zemin |
| 164. | apology | 14: [19, inf] | apology china chinese | Band_in_China |
| 165. | aides | 14: [13, 13.0], 41: [10, inf] | aides bush 's | George_H._W._Bush |
| 166. | letter | 14: [12, inf] | letter 's bush | Mahmoud_Ahmadinejad's_letter_to_George_W._Bush |
| 167. | network | 14: [12, inf], 25: [10, inf], 38: [18, inf] | network 's laden | Bin_Laden_family |
| 168. | ntv | 14: [16, inf] | ntv 's gazprom | Gazprom-Media |
| 169. | gazprom | 14: [13, inf] | gazprom 's ntv | Gazprom-Media |
| 170. | bhutto | 14: [10, inf] | bhutto pakistan court | Zulfikar_Ali_Bhutto |
| 171. | remains | 15: [10, inf] | remains 's say | The_Remains_of_the_Day |
| 172. | heroes | 15: [14, inf] | heroes 's welcome | Heroes_Welcome_UK |
| 173. | use | 15: [10, inf], 38: [19, 6.33], 44: [13, 13.0] | use 's military | Authorization_for_Use_of_Military_Force_of_2001 |
| 174. | home | 15: [20, 10.0], 21: [11, inf] | home 's photo | Photo_Booth |
| 175. | water | 15: [14, inf], 18: [13, inf] | water 's says | Flint_water_crisis |
| 176. | gusinsky | 16: [19, inf] | gusinsky 's vladimir | Vladimir_Gusinsky |
| 177. | known | 16: [10, inf], 46: [10, 10.0] | known 's say | There_are_known_knowns |
| 178. | calling | 16: [14, inf] | calling 's china | China |
| 179. | withdraw | 16: [10, inf], 35: [10, 10.0] | withdraw 's bush | George_H._W._Bush |
| 180. | lebanon | 16: [14, inf] | lebanon israeli israel | Israeli–Lebanese_conflict |
| 181. | arab | 16: [15, inf], 47: [21, 5.25] | arab 's israeli | Arab–Israeli_conflict |
| 182. | sharon | 16: [15, inf], 25: [13, 6.5] | sharon israeli israel | Ariel_Sharon |
| 183. | japan | 16: [23, 5.75], 37: [30, 7.5], 43: [11, 11.0], 51: [13, inf] | japan 's japanese | Japan |
| 184. | helms | 16: [10, inf] | helms mexico 's | Jesse_Helms |
| 185. | mr. | 16: [23, 7.67], 18: [23, 11.5], 24: [12, inf], 27: [17, inf], 30: [14, 14.0], 46: [14, 7.0] | mr. 's president | Mr._President_(title) |
| 186. | americas | 16: [15, 15.0], 31: [14, inf], 39: [11, inf], 45: [12, 6.0] | americas world briefing | 1211_Avenue_of_the_Americas |
| 187. | industry | 16: [10, inf] | industry 's government | State_ownership |
| 188. | aids | 16: [11, inf], 25: [16, 8.0] | aids africa 's | HIV/AIDS_in_Africa |
| 189. | beirut | 16: [10, inf] | beirut 's chtaura | Chtaura |
| 190. | protest | 17: [10, inf], 40: [10, inf] | protest 's world | Protest |
| 191. | chechnya | 17: [12, inf] | chechnya russian 's | Chechnya |
| 192. | koizumi | 17: [20, 10.0], 30: [15, inf] | koizumi 's japan | Junichiro_Koizumi |
| 193. | communist | 17: [10, inf], 48: [10, 10.0] | communist 's party | Chinese_Communist_Party |
| 194. | agency | 17: [10, inf] | agency 's says | National_Security_Agency |
| 195. | show | 17: [11, inf], 49: [10, 5.0], 51: [13, 6.5] | show 's government | That_'70s_Show |
| 196. | campaign | 17: [11, inf] | campaign 's afghanistan | Afghanistan_Campaign_Medal |
| 197. | cabinet | 17: [10, inf], 22: [11, 11.0], 36: [11, 5.5] | cabinet 's government | Cabinet_(government) |
| 198. | labor | 17: [10, 5.0], 19: [11, inf], 49: [12, inf] | labor 's party | Minnesota_Democratic–Farmer–Labor_Party |
| 199. | missile | 18: [54, 13.5], 46: [13, inf], 50: [25, 8.33] | missile bush 's | 1993_cruise_missile_strikes_on_Iraq |
| 200. | system | 18: [31, inf], 22: [12, 6.0] | system 's missile | S-500_missile_system |
| 201. | indonesia | 18: [14, 7.0], 22: [23, inf], 30: [33, 8.25] | indonesia 's wahid | Abdurrahman_Wahid |
| 202. | change | 18: [14, 7.0], 20: [11, inf] | change 's photo | Google_Photos |
| 203. | speech | 18: [16, inf], 40: [10, inf] | speech 's bush | Mission_Accomplished_speech |
| 204. | treaty | 18: [21, 10.5], 27: [15, 5.0], 36: [18, inf], 50: [30, 15.0] | treaty bush missile | Anti-Ballistic_Missile_Treaty |
| 205. | zambia | 18: [13, inf], 52: [11, inf] | zambia 's party | List_of_political_parties_in_Zambia |
| 206. | chiluba | 18: [11, inf] | chiluba zambia 's | Frederick_Chiluba |
| 207. | citizens | 18: [16, inf] | citizens 's china | Visa_requirements_for_Chinese_citizens |
| 208. | korean | 18: [12, inf], 33: [43, 6.14], 41: [14, inf] | korean north korea | North_Korea–South_Korea_relations |
| 209. | gloria | 18: [10, inf] | gloria philippines arroyo | Gloria_Macapagal_Arroyo |
| 210. | macapagal | 18: [10, inf] | macapagal philippines arroyo | Jose_Miguel_Arroyo |
| 211. | arroyo | 18: [11, inf] | arroyo philippines gloria | Gloria_Macapagal_Arroyo |
| 212. | days | 18: [12, 6.0], 26: [10, 5.0], 35: [10, 5.0], 38: [10, inf] | days 's taliban | Taliban |
| 213. | liberia | 18: [10, inf] | liberia 's united | Liberia–United_States_relations |
| 214. | bishops | 18: [10, inf] | bishops pope catholic | Bishops_in_the_Catholic_Church |
| 215. | commission | 18: [14, inf], 32: [14, inf], 50: [10, 5.0] | commission 's rights | National_Human_Rights_Commission_of_India |
| 216. | berlusconi | 19: [24, 12.0], 22: [10, inf], 39: [13, 13.0] | berlusconi italy 's | Silvio_Berlusconi |
| 217. | dues | 19: [12, inf] | dues us united | United_States_dollar |
| 218. | loss | 19: [10, inf] | loss 's american | Hearing_loss |
| 219. | history | 19: [11, inf] | history 's photo | Google_Photos |
| 220. | shipman | 19: [12, inf] | shipman harold doctor | Harold_Shipman |
| 221. | german | 19: [10, 5.0], 34: [14, 7.0], 36: [12, inf], 39: [15, inf] | german germany 's | Germany |
| 222. | women | 20: [13, 13.0], 22: [10, 5.0], 24: [13, inf], 30: [15, 7.5], 33: [10, 10.0] | women 's taliban | Taliban_treatment_of_women |
| 223. | slaughter | 20: [10, inf] | slaughter disease 's | Animal_slaughter |
| 224. | chickens | 20: [13, inf] | chickens hong kong | Hong_Kong_Soya_Sauce_Chicken_Rice_and_Noodle |
| 225. | flu | 20: [11, inf] | flu hong kong | Hong_Kong_flu |
| 226. | suicide | 20: [10, inf], 32: [14, inf], 37: [13, 6.5], 39: [10, 5.0] | suicide palestinian israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 227. | sudan | 21: [10, inf] | sudan 's government | South_Sudan |
| 228. | rajoub | 21: [11, inf] | rajoub palestinian 's | Jibril_Rajoub |
| 229. | cable | 21: [14, inf] | cable american german | Cable_television |
| 230. | pakistan | 21: [14, inf], 25: [10, 5.0], 33: [10, 10.0], 37: [11, 5.5] | pakistan 's taliban | Tehrik-i-Taliban_Pakistan |
| 231. | chad | 22: [12, inf] | chad candidates africa | 2021_Chadian_presidential_election |
| 232. | wants | 22: [16, inf] | wants 's bush | Cori_Bush |
| 233. | union | 22: [10, inf] | union european 's | European_Union |
| 234. | arafat | 22: [17, inf], 26: [11, 5.5], 34: [14, 14.0], 48: [15, 15.0] | arafat palestinian israeli | Yasser_Arafat |
| 235. | special | 22: [10, inf], 42: [25, 12.5] | special taliban 's | Taliban |
| 236. | indonesian | 22: [10, inf] | indonesian indonesia wahid | Indonesian_Democratic_Party_of_Struggle |
| 237. | abdurrahman | 22: [13, inf] | abdurrahman wahid indonesia | Abdurrahman_Wahid |
| 238. | vote | 22: [21, 7.0], 28: [13, inf], 44: [11, 11.0] | vote 's party | Party-line_vote |
| 239. | republic | 22: [14, inf] | republic 's world | South_Korea |
| 240. | jakarta | 22: [10, inf] | jakarta 's indonesia | Jakarta |
| 241. | company | 22: [10, inf] | company 's oil | Shell_Oil_Company |
| 242. | elf | 22: [10, inf], 25: [11, inf] | elf former dumas | Elf_Aquitaine |
| 243. | nepal | 22: [12, inf], 45: [11, inf], 48: [10, 5.0] | nepal 's world | Nepal |
| 244. | zimbabwe | 22: [10, 5.0], 32: [16, inf], 36: [10, inf] | zimbabwe 's government | Hyperinflation_in_Zimbabwe |
| 245. | rumsfeld | 23: [21, inf], 40: [18, 9.0] | rumsfeld defense taliban | Donald_Rumsfeld |
| 246. | donald | 23: [11, inf], 40: [13, 6.5] | donald rumsfeld defense | Donald_Rumsfeld |
| 247. | khatami | 23: [10, inf], 32: [10, 5.0] | khatami iran 's | Mohammad_Khatami |
| 248. | tiananmen | 23: [10, inf] | tiananmen gong falun | Tiananmen_Square_self-immolation_incident |
| 249. | massacre | 23: [15, inf] | massacre 's nepal | Nepalese_royal_massacre |
| 250. | favor | 23: [10, inf] | favor 's powell | Colin_Powell |
| 251. | catholic | 23: [10, inf], 25: [11, inf] | catholic 's church | Catholic_Church |
| 252. | potato | 23: [10, inf] | potato irish famines | Great_Famine_(Ireland) |
| 253. | warming | 24: [15, inf] | warming bush global | Global_warming_controversy |
| 254. | northern | 25: [10, inf], 36: [10, 5.0] | northern taliban alliance | Northern_Alliance |
| 255. | koreans | 26: [10, inf] | koreans north korea | North_Korea–South_Korea_relations |
| 256. | transfer | 26: [12, inf] | transfer milosevic government | Slobodan_Milošević |
| 257. | kofi | 26: [10, inf] | kofi annan united | Kofi_Annan |
| 258. | annan | 26: [12, inf], 41: [19, inf], 50: [19, 19.0] | annan united kofi | Kofi_Annan |
| 259. | already | 26: [13, inf] | already 's government | Federal_government_of_the_United_States |
| 260. | seven | 26: [12, inf], 50: [16, 5.33] | seven 's israeli | Israel–United_States_relations |
| 261. | making | 26: [11, 11.0], 44: [11, inf] | making 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 262. | reported | 27: [10, inf] | reported 's world | U.S._News_&_World_Report |
| 263. | fuat | 27: [12, inf] | fuat turkey muslim | Mehmet_Fuat_Köprülü |
| 264. | followers | 27: [10, inf] | followers 's gong | Falun_Gong |
| 265. | germany | 27: [12, inf], 29: [12, inf] | germany 's german | Germany |
| 266. | test | 27: [11, inf] | test 's treaty | Comprehensive_Nuclear-Test-Ban_Treaty |
| 267. | sri | 28: [11, inf] | sri lanka rebels | Sri_Lankan_Civil_War |
| 268. | strategy | 28: [10, inf], 41: [12, 6.0], 51: [12, inf] | strategy 's bush | Bush_Doctrine |
| 269. | agreement | 29: [11, 5.5], 34: [12, inf] | agreement 's us | Comprehensive_and_Progressive_Agreement_for_Trans-Pacific_Partnership |
| 270. | salmon | 29: [10, inf] | salmon invercreran fish | EMPTY MATCHING |
| 271. | blood | 29: [16, inf] | blood 's aids | HIV/AIDS |
| 272. | protesters | 29: [14, inf] | protesters 's police | George_Floyd_protests |
| 273. | industrialized | 29: [11, inf] | industrialized leaders nations | Newly_industrialized_country |
| 274. | monitors | 29: [19, inf] | monitors rights human | Human_rights |
| 275. | eight | 29: [11, inf] | eight 's israel | Israel |
| 276. | whether | 30: [11, inf] | whether 's bush | George_W._Bush |
| 277. | shrine | 30: [17, inf], 33: [13, 6.5] | shrine 's japan | Yasukuni_Shrine |
| 278. | past | 30: [14, inf] | past 's photo | Google_Photos |
| 279. | devi | 30: [11, inf] | devi india 's | Shakuntala_Devi |
| 280. | racism | 31: [12, inf], 35: [11, inf] | racism conference israel | World_Conference_against_Racism_2001 |
| 281. | trucks | 31: [13, inf] | trucks tunnel 's | Eisenhower_Tunnel |
| 282. | boys | 31: [10, inf] | boys two israeli | Our_Boys_(miniseries) |
| 283. | block | 31: [11, inf], 41: [10, 5.0] | block 's bush | Bush–Breyman_Block |
| 284. | ministry | 31: [10, inf] | ministry 's foreign | Ministry_of_Foreign_Affairs_of_the_People's_Republic_of_China |
| 285. | investigation | 31: [10, inf], 40: [10, 10.0] | investigation 's american | Special_Counsel_investigation_(2017–2019) |
| 286. | farrakhan | 31: [10, inf] | farrakhan britain ban | R_(on_the_application_of_Farrakhan)_v_Secretary_of_State_for_the_Home_Department |
| 287. | bosnia | 31: [10, inf] | bosnia bosnian crimes | Bosnian_War |
| 288. | golf | 32: [10, inf] | golf 's journal | Men's_major_golf_championships |
| 289. | break | 32: [10, 5.0], 46: [10, inf] | break 's bush | Barbara_Bush_(born_1981) |
| 290. | zemin | 32: [18, inf] | zemin china 's | Jiang_Zemin |
| 291. | bomber | 32: [11, inf] | bomber palestinian suicide | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 292. | vatican | 32: [10, inf] | vatican 's pope | Pope_John_Paul_I_conspiracy_theories |
| 293. | armed | 33: [14, inf] | armed 's forces | United_States_Armed_Forces |
| 294. | signed | 33: [11, inf] | signed 's peace | Peace_symbols |
| 295. | th | 33: [11, inf] | th 's us | Thnks_fr_th_Mmrs |
| 296. | nato | 33: [28, inf], 49: [10, inf] | nato 's macedonia | North_Macedonia–NATO_relations |
| 297. | coins | 33: [10, inf] | coins euro european | Euro_coins |
| 298. | rice | 33: [12, inf] | rice bush 's | Condoleezza_Rice |
| 299. | epidemic | 34: [14, inf] | epidemic aids 's | Epidemiology_of_HIV/AIDS |
| 300. | neighboring | 35: [11, inf] | neighboring 's says | Says |
| 301. | myanmar | 35: [16, inf] | myanmar 's world | Myanmar |
| 302. | town | 35: [28, 28.0], 37: [12, inf] | town 's israeli | List_of_cities_in_Israel |
| 303. | beit | 35: [24, inf] | beit israeli palestinian | 2006_Israeli_operation_in_Beit_Hanoun |
| 304. | jala | 35: [26, inf] | jala israeli palestinian | Beit_Jala |
| 305. | stop | 35: [10, inf] | stop 's says | My_Brain_Says_Stop,_But_My_Heart_Says_Go! |
| 306. | gilo | 35: [15, inf] | gilo israeli palestinian | Gilo |
| 307. | euro | 35: [12, inf], 52: [14, 7.0] | euro european currency | Euro |
| 308. | islamic | 36: [10, 5.0], 38: [26, inf] | islamic 's taliban | Islamic_Emirate_of_Afghanistan |
| 309. | african | 36: [11, inf] | african africa south | South_Africa |
| 310. | grant | 36: [10, inf] | grant 's bush | U.S._Presidential_IQ_hoax |
| 311. | `` | 37: [13, 13.0], 46: [13, inf] | `` 's today | Today_(American_TV_program) |
| 312. | around | 37: [12, inf], 46: [24, 12.0] | around 's world | Around_the_World_in_a_Day |
| 313. | timor | 37: [15, inf] | timor east world | East_Timor |
| 314. | center | 37: [15, 7.5], 50: [10, inf] | center 's world | World_Trade_Center_(1973–2001) |
| 315. | pakistani | 38: [12, inf] | pakistani taliban pakistan | Tehrik-i-Taliban_Pakistan |
| 316. | afghans | 38: [11, 11.0], 46: [10, inf], 51: [25, 6.25] | afghans taliban afghanistan | War_in_Afghanistan_(2001–present) |
| 317. | top | 38: [13, inf] | top 's laden | Killing_of_Osama_bin_Laden |
| 318. | action | 38: [13, inf], 48: [11, 5.5] | action 's bush | Presidency_of_George_W._Bush |
| 319. | militant | 38: [11, inf], 49: [12, inf] | militant 's pakistan | Pakistan_and_state-sponsored_terrorism |
| 320. | cease-fire | 38: [19, inf] | cease-fire palestinian israel | Israeli–Palestinian_conflict |
| 321. | targets | 38: [17, inf], 44: [10, 5.0] | targets taliban 's | Taliban |
| 322. | changes | 38: [11, inf] | changes 's american | United_States_involvement_in_regime_change |
| 323. | clerics | 38: [17, inf] | clerics taliban laden | Taliban |
| 324. | demands | 38: [11, inf] | demands 's says | Say's_law |
| 325. | congress | 38: [12, 6.0], 51: [10, inf] | congress 's bush | Presidency_of_George_H._W._Bush |
| 326. | information | 39: [12, inf] | information 's says | Say's_law |
| 327. | american-led | 39: [10, inf], 41: [15, 7.5] | american-led afghanistan 's | War_in_Afghanistan_(2001–present) |
| 328. | havel | 39: [10, inf] | havel czech vaclav | Václav_Havel_Airport_Prague |
| 329. | persuade | 39: [10, inf] | persuade 's taliban | Tehrik-i-Taliban_Pakistan |
| 330. | hijackers | 39: [13, inf] | hijackers laden attacks | Responsibility_for_the_September_11_attacks |
| 331. | quetta | 39: [16, inf] | quetta pakistan taliban | Quetta_Shura |
| 332. | king | 39: [12, inf] | king 's bush | Kate_Bush |
| 333. | milan— | 39: [10, inf] | milan— 's fashion | Fashion_in_Milan |
| 334. | discuss | 40: [11, inf] | discuss 's bush | George_H._W._Bush |
| 335. | nuclear | 40: [26, inf], 44: [33, 16.5], 49: [20, 10.0] | nuclear 's bush | India–United_States_Civil_Nuclear_Agreement |
| 336. | short | 40: [13, inf] | short 's us | Short_Empire |
| 337. | september | 40: [14, inf] | september 's attacks | September_11_attacks |
| 338. | asia/pacific | 40: [24, inf] | asia/pacific world briefing | Trans-Pacific_Partnership |
| 339. | abortion | 40: [10, inf] | abortion 's ireland | Abortion_in_the_Republic_of_Ireland |
| 340. | involved | 40: [11, inf] | involved 's military | Military |
| 341. | crash | 40: [10, inf] | crash 's tunnel | Eisenhower_Tunnel |
| 342. | separatist | 41: [11, inf] | separatist 's basque | Basque_nationalism |
| 343. | georgia | 41: [11, 5.5], 44: [10, inf] | georgia world abkhazia | List_of_cities_and_towns_in_Georgia_(country) |
| 344. | bombers | 41: [10, inf] | bombers says 's | Tupolev_Tu-160 |
| 345. | broadcast | 41: [10, inf] | broadcast 's laden | Bin_Laden_family |
| 346. | night | 41: [10, inf] | night 's taliban | Taliban |
| 347. | us-led | 41: [10, inf] | us-led 's says | Saudi_Arabian-led_intervention_in_Yemen |
| 348. | chirac | 41: [10, inf], 46: [10, 5.0] | chirac pres jacques | Jacques_Chirac |
| 349. | sites | 41: [10, inf] | sites 's taliban | Tehrik-i-Taliban_Pakistan |
| 350. | airstrikes | 41: [41, inf] | airstrikes taliban 's | Kunduz_hospital_airstrike |
| 351. | boat | 41: [10, inf], 52: [15, inf] | boat 's south | E-boat |
| 352. | jazeera | 41: [10, inf] | jazeera laden 's | Videos_and_audio_recordings_of_Osama_bin_Laden |
| 353. | prepare | 41: [10, inf] | prepare 's says | Si_vis_pacem,_para_bellum |
| 354. | service | 41: [13, 6.5], 44: [13, inf] | service 's bush | George_W._Bush_military_service_controversy |
| 355. | honey | 41: [11, inf] | honey 's laden | Caucasian_honey_bee |
| 356. | challenged | 41: [10, inf] | challenged 's afghanistan | United_States_invasion_of_Afghanistan |
| 357. | prayer | 41: [14, inf] | prayer 's thousands | Prayer |
| 358. | mosques | 41: [12, inf] | mosques 's afghanistan | List_of_mosques_in_Afghanistan |
| 359. | mosque | 41: [12, inf] | mosque 's islam | Holiest_sites_in_Islam |
| 360. | nobel | 41: [18, inf], 50: [16, inf] | nobel prize 's | Nobel_Prize_in_Literature |
| 361. | prize | 41: [13, inf], 50: [12, inf] | prize nobel 's | Nobel_Prize |
| 362. | moderate | 42: [11, inf] | moderate 's taliban | Taliban |
| 363. | dr. | 42: [10, inf] | dr. world 's | Dr._Mario_World |
| 364. | marcos | 42: [10, inf] | marcos philippines 's | History_of_the_Philippines_(1965–1986) |
| 365. | zeevi | 42: [12, inf] | zeevi palestinian israeli | Timeline_of_the_Israeli–Palestinian_conflict |
| 366. | raid | 42: [18, 9.0], 48: [16, inf] | raid 's israeli | 1968_Israeli_raid_on_Lebanon |
| 367. | sinn | 43: [10, inf] | sinn fein ireland | Sinn_Féin |
| 368. | fein | 43: [10, inf] | fein sinn ireland | Sinn_Féin |
| 369. | dismantling | 43: [11, inf] | dismantling plane immigrants | Digital_native |
| 370. | alps | 43: [11, inf] | alps tunnel killed | Alps |
| 371. | gotthard | 43: [11, inf] | gotthard tunnel swiss | Gotthard_Tunnel |
| 372. | haq | 43: [19, inf] | haq taliban afghanistan | Taliban |
| 373. | b- | 44: [12, inf] | b- taliban afghanistan | Islamic_Emirate_of_Afghanistan |
| 374. | wheat | 44: [10, inf] | wheat afghanistan aid | Economy_of_Afghanistan |
| 375. | bases | 45: [14, inf] | bases military 's | List_of_United_States_military_bases |
| 376. | strike | 45: [12, inf] | strike 's taliban | Taliban |
| 377. | tajikistan | 45: [16, inf] | tajikistan taliban uzbekistan | Islamic_Movement_of_Uzbekistan |
| 378. | leadership | 45: [12, inf] | leadership 's taliban | Taliban |
| 379. | patents | 45: [12, inf] | patents aids drugs | Prizes_as_an_alternative_to_patents |
| 380. | capture | 45: [11, inf] | capture taliban american | Taliban |
| 381. | describes | 45: [10, inf] | describes 's says | Say's_law |
| 382. | red | 45: [10, inf] | red 's cross | International_Red_Cross_and_Red_Crescent_Movement |
| 383. | order | 46: [14, inf] | order 's says | Order_of_the_British_Empire |
| 384. | pashtuns | 46: [10, inf] | pashtuns taliban alliance | Northern_Alliance |
| 385. | quickly | 46: [10, inf] | quickly 's taliban | Taliban |
| 386. | lives | 46: [10, inf] | lives 's photo | Black_Lives_Matter |
| 387. | omar | 46: [25, inf] | omar taliban 's | Mohammed_Omar |
| 388. | wars | 46: [10, inf] | wars milosevic 's | Slobodan_Milošević |
| 389. | cuba | 46: [10, inf] | cuba 's pres | Cuba–United_States_relations |
| 390. | construction | 46: [10, inf] | construction 's world | Construction_of_the_World_Trade_Center |
| 391. | kunduz | 46: [17, inf] | kunduz taliban alliance | Kunduz_airlift |
| 392. | mountains | 46: [10, inf], 50: [16, 8.0] | mountains 's taliban | Taliban |
| 393. | envoys | 47: [11, inf] | envoys peace 's | United_States_Special_Envoy_for_Northern_Ireland |
| 394. | mandela | 47: [10, inf] | mandela africa 's | Nelson_Mandela |
| 395. | madikizela-mandela | 47: [10, inf] | madikizela-mandela 's mandela | Winnie_Madikizela-Mandela |
| 396. | hamas | 47: [10, inf], 49: [31, 15.5] | hamas palestinian israeli | Hamas |
| 397. | predator | 47: [10, inf] | predator air aircraft | General_Atomics_MQ-1_Predator |
| 398. | sports | 47: [12, inf] | sports job find | Dave_Holmes_(sportscaster) |
| 399. | yemen | 47: [10, inf] | yemen cole attack | USS_Cole_bombing |
| 400. | wounded | 48: [13, inf] | wounded killed 's | List_of_United_States_Congress_members_killed_or_wounded_in_office |
| 401. | uncertain | 48: [10, inf] | uncertain 's taliban | Taliban_insurgency |
| 402. | fortress | 48: [12, inf] | fortress prisoners alliance | Battle_of_Qala-i-Jangi |
| 403. | zinni | 48: [12, inf] | zinni palestinian israeli | List_of_Israeli_assassinations |
| 404. | prisoner | 48: [12, inf] | prisoner taliban prisoners | Bagram_torture_and_prisoner_abuse |
| 405. | fort | 48: [16, inf] | fort taliban prisoners | Bowe_Bergdahl |
| 406. | belgian | 48: [10, inf] | belgian belgium 's | Belgian_chocolate |
| 407. | chile | 48: [10, inf] | chile pinochet augusto | Lucía_Pinochet |
| 408. | delegation | 48: [10, inf] | delegation 's world | Delegation_(band) |
| 409. | vietnam | 48: [16, inf] | vietnam 's asia | Vietnam |
| 410. | meets | 48: [11, inf] | meets 's bush | George_H._W._Bush |
| 411. | extremists | 49: [15, inf] | extremists 's arafat | Raymonda_Tawil |
| 412. | draft | 49: [12, inf] | draft 's would | 2012_NFL_Draft |
| 413. | parliamentary | 49: [13, inf] | parliamentary 's elections | General_election |
| 414. | hamid | 49: [11, inf] | hamid karzai taliban | Hamid_Karzai |
| 415. | karzai | 49: [18, inf] | karzai taliban afghanistan | Afghanistan_conflict_(1978–present) |
| 416. | violent | 49: [10, inf] | violent 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 417. | yemeni | 49: [10, inf] | yemeni yemen us | Yemeni_Civil_War_(2014–present) |
| 418. | continued | 50: [11, inf] | continued 's says | To_Be_Continued..._(box_set) |
| 419. | videotape | 50: [16, inf] | videotape laden says | Bin_Laden_family |
| 420. | tape | 50: [24, inf], 52: [12, 6.0] | tape laden 's | Videos_and_audio_recordings_of_Osama_bin_Laden |
| 421. | antiballistic | 50: [12, inf] | antiballistic missile treaty | Anti-Ballistic_Missile_Treaty |
| 422. | contact | 50: [10, inf] | contact 's arafat | Yasser_Arafat |
| 423. | orders | 50: [11, inf] | orders 's world | Superior_orders |
| 424. | prodi | 50: [10, inf] | prodi european commission | Prodi_Commission |
| 425. | peacekeeping | 51: [15, inf] | peacekeeping nato troops | List_of_NATO_operations |
| 426. | agents | 51: [10, inf] | agents 's officials | Agents_of_S.H.I.E.L.D. |
| 427. | recalls | 51: [10, inf] | recalls india pakistan | Indo-Pakistani_War_of_1971 |
| 428. | brought | 51: [10, inf] | brought 's says | Brought_by_the_Sea |
| 429. | buildup | 52: [10, inf] | buildup china 's | China–United_States_relations |
| 430. | reid | 52: [23, inf] | reid northern 's | Harry_Reid |
| 431. | plane | 14: [107, 53.5], 21: [11, 5.5], 33: [10, 10.0] | plane china chinese | Chinese_zodiac |
| 432. | living | 44: [37, 37.0] | living 's photo | Living_presidents_of_the_United_States |
| 433. | surrender | 47: [38, 19.0], 49: [33, 33.0] | surrender taliban 's | List_of_Taliban_leaders |
| 434. | argentina | 31: [18, 9.0], 51: [28, 28.0] | argentina 's argentine | Argentina |
| 435. | meeting | 5: [20, 6.67], 24: [24, 24.0], 32: [10, 5.0] | meeting 's bush | George_H._W._Bush |
| 436. | last | 18: [24, 24.0] | last 's taliban | Taliban |
| 437. | megawati | 30: [24, 24.0] | megawati 's indonesia | Megawati_Sukarnoputri |
| 438. | tony | 40: [24, 24.0] | tony blair 's | Tony_Blair |
| 439. | africa | 6: [23, 23.0], 27: [21, 7.0] | africa world 's | South_Africa |
| 440. | north | 3: [19, 9.5], 8: [25, 8.33], 13: [38, 9.5], 18: [22, 22.0], 20: [15, 5.0] | north korea 's | North_Korea |
| 441. | mullah | 46: [22, 22.0], 49: [20, 6.67] | mullah taliban 's | Mohammed_Omar |
| 442. | osama | 38: [41, 20.5] | osama laden 's | Killing_of_Osama_bin_Laden |
| 443. | party | 17: [40, 20.0] | party 's government | Federal_government_of_the_United_States |
| 444. | space | 19: [40, 20.0] | space 's russian | Russian_Space_Forces |
| 445. | french | 22: [11, 11.0], 36: [20, 20.0], 52: [15, 7.5] | french france 's | France |
| 446. | july | 27: [20, 20.0] | july 's police | 2016_shooting_of_Dallas_police_officers |
| 447. | bank | 29: [20, 20.0] | bank israeli palestinian | Israeli_West_Bank_barrier |
| 448. | uzbekistan | 40: [20, 20.0] | uzbekistan afghanistan 's | Afghanistan–Uzbekistan_border |
| 449. | may | 17: [11, 5.5], 38: [19, 19.0] | may 's says | Say's_law |
| 450. | muhammad | 39: [10, 5.0], 46: [19, 19.0], 49: [16, 5.33] | muhammad taliban 's | Muhammad_Rasul |
| 451. | revolt | 48: [19, 19.0] | revolt 's prisoners | Sobibor_extermination_camp |
| 452. | joseph | 3: [18, 18.0] | joseph 's president | Joe_Biden |
| 453. | rights | 4: [14, 14.0], 16: [18, 18.0], 18: [35, 11.67] | rights human 's | Human_rights |
| 454. | administration | 10: [18, 18.0] | administration bush 's | Presidency_of_George_W._Bush |
| 455. | peru | 17: [24, 6.0], 21: [18, 18.0] | peru peruvian 's | Japanese_Peruvians |
| 456. | putin | 20: [14, 7.0], 24: [36, 18.0] | putin russia 's | Russia_under_Vladimir_Putin |
| 457. | bonn | 48: [18, 18.0] | bonn afghan government | Bonn_Agreement_(Afghanistan) |
| 458. | manila | 3: [10, 10.0], 18: [17, 17.0] | manila estrada president | Joseph_Estrada |
| 459. | members | 14: [32, 16.0], 17: [17, 17.0], 23: [18, 6.0] | members 's china | China |
| 460. | genoa | 29: [34, 17.0] | genoa italy summit | 27th_G8_summit |
| 461. | sukarnoputri | 30: [17, 17.0] | sukarnoputri 's indonesia | Indonesian_Democratic_Party_of_Struggle |
| 462. | summit | 32: [10, 5.0], 42: [17, 17.0] | summit 's bush | Malta_Summit |
| 463. | afghan | 38: [17, 17.0] | afghan taliban afghanistan | Taliban |
| 464. | assets | 39: [17, 17.0], 44: [10, 5.0] | assets 's groups | Asset |
| 465. | linked | 39: [17, 17.0], 48: [10, 10.0] | linked 's laden | Osama_bin_Laden's_compound_in_Abbottabad |
| 466. | former | 2: [33, 16.5] | former 's pres | Saint-Germain-des-Prés |
| 467. | jerusalem | 6: [16, 16.0], 13: [10, 5.0], 32: [26, 5.2], 35: [13, 13.0] | jerusalem palestinian israeli | East_Jerusalem |
| 468. | british | 7: [15, 5.0], 15: [16, 16.0], 50: [30, 7.5] | british 's britain | Britishness |
| 469. | poor | 26: [16, 16.0] | poor 's world | S&P_Global_Ratings |
| 470. | terrorism | 37: [16, 16.0] | terrorism 's bush | War_on_terror |
| 471. | sept | 38: [16, 16.0] | sept attacks 's | September_11_attacks |
| 472. | plot | 40: [16, 16.0] | plot 's laden | Killing_of_Osama_bin_Laden |
| 473. | stronghold | 46: [16, 16.0] | stronghold taliban afghanistan | Islamic_Emirate_of_Afghanistan |
| 474. | power | 3: [15, 15.0] | power 's taliban | Taliban's_rise_to_power |
| 475. | case | 5: [12, 6.0], 12: [15, 15.0] | case 's court | Supreme_Court_of_the_United_States |
| 476. | palestinians | 6: [16, 8.0], 10: [15, 15.0], 29: [16, 5.33] | palestinians israeli palestinian | Israeli–Palestinian_conflict |
| 477. | fashion | 11: [18, 6.0], 41: [15, 15.0] | fashion 's paris— | Paris_Fashion_Week |
| 478. | english | 12: [15, 15.0] | english 's world | World_Englishes |
| 479. | nation | 17: [12, 6.0], 22: [16, 5.33], 33: [15, 15.0] | nation 's says | 'No_Way_To_Prevent_This,'_Says_Only_Nation_Where_This_Regularly_Happens |
| 480. | virus | 20: [15, 15.0] | virus aids disease | HIV/AIDS |
| 481. | prison | 25: [13, 6.5], 46: [11, 5.5], 48: [15, 15.0] | prison 's years | Prison |
| 482. | role | 39: [15, 15.0] | role 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 483. | london | 41: [15, 15.0] | london 's britain | London |
| 484. | laws | 49: [15, 15.0] | laws 's government | Federal_government_of_the_United_States |
| 485. | get | 51: [15, 15.0] | get 's says | Say's_law |
| 486. | even | 2: [13, 6.5], 8: [14, 14.0], 38: [11, 5.5] | even 's says | Say's_law |
| 487. | bhuj | 5: [14, 14.0] | bhuj india rubble | 2001_Gujarat_earthquake |
| 488. | russia | 6: [30, 10.0], 9: [27, 6.75], 11: [28, 14.0] | russia 's putin | Vladimir_Putin |
| 489. | france | 11: [14, 14.0] | france 's french | France |
| 490. | countries | 13: [14, 14.0], 33: [12, 6.0] | countries 's us | Comparison_between_U.S._states_and_countries_by_GDP_(PPP) |
| 491. | demand | 14: [11, 5.5], 38: [14, 14.0] | demand 's china | Price_elasticity_of_demand |
| 492. | welcome | 15: [14, 14.0] | welcome 's china | Welcome_Chinese |
| 493. | open | 19: [14, 14.0] | open 's says | Say's_law |
| 494. | office | 20: [14, 14.0] | office 's pres | History_of_Microsoft_Office |
| 495. | range | 30: [14, 14.0] | range 's bush | George_H._W._Bush |
| 496. | switzerland | 39: [14, 14.0] | switzerland swiss world | Demographics_of_Switzerland |
| 497. | kandahar | 41: [14, 14.0], 46: [23, 5.75] | kandahar taliban afghanistan | United_States_invasion_of_Afghanistan |
| 498. | radio | 41: [14, 14.0] | radio 's taliban | Taliban |
| 499. | post-taliban | 48: [14, 14.0] | post-taliban afghanistan taliban | Islamic_Emirate_of_Afghanistan |
| 500. | escape | 50: [14, 14.0] | escape taliban 's | Escape_from_Taliban |
| 501. | three | 5: [13, 13.0] | three 's world | Popper's_three_worlds |
| 502. | months | 10: [13, 13.0], 14: [11, 5.5] | months 's photo | Google_Photos |
| 503. | away | 11: [13, 13.0] | away 's world | Away_from_the_World |
| 504. | politicians | 12: [13, 13.0] | politicians 's government | List_of_foreign-born_United_States_politicians |
| 505. | charges | 16: [13, 13.0] | charges 's former | Electric_charge |
| 506. | missionary | 17: [13, 13.0] | missionary plane peruvian | 2001_Peru_shootdown |
| 507. | program | 17: [13, 13.0], 20: [10, 5.0], 43: [14, 7.0] | program 's world | "Hello,_World!"_program |
| 508. | meet | 20: [13, 13.0], 23: [10, 5.0] | meet 's bush | Barbara_Bush_(born_1981) |
| 509. | urges | 24: [13, 13.0] | urges 's bush | George_H._W._Bush |
| 510. | conference | 26: [10, 10.0], 28: [13, 13.0], 31: [14, 7.0], 35: [18, 9.0] | conference 's bush | Bush_family |
| 511. | panel | 26: [13, 13.0] | panel 's commission | Presidential_Advisory_Commission_on_Election_Integrity |
| 512. | york | 31: [13, 13.0], 37: [11, 5.5] | york 's attacks | September_11_attacks |
| 513. | anniversary | 33: [13, 13.0] | anniversary 's south | S.E.S._(group) |
| 514. | laden | 38: [78, 13.0] | laden 's osama | Killing_of_Osama_bin_Laden |
| 515. | six | 39: [13, 13.0], 42: [11, 5.5] | six 's months | Six_Months_in_a_Leaky_Boat |
| 516. | line | 41: [13, 13.0] | line 's taliban | Taliban |
| 517. | default | 44: [13, 13.0] | default debt argentina | Default_(finance) |
| 518. | winter | 45: [13, 13.0] | winter afghanistan taliban | Taliban |
| 519. | qatar | 45: [13, 13.0] | qatar trade world | Qatar |
| 520. | jet | 14: [25, 12.5] | jet plane chinese | Hainan_Island_incident |
| 521. | swiss | 3: [12, 12.0], 43: [18, 6.0] | swiss tunnel switzerland | Switzerland |
| 522. | policy | 3: [11, 11.0], 33: [17, 8.5], 35: [12, 12.0] | policy 's bush | Foreign_policy_of_the_George_W._Bush_administration |
| 523. | development | 5: [10, 5.0], 29: [12, 12.0] | development 's bush | George_H._W._Bush |
| 524. | colombian | 5: [12, 12.0] | colombian colombia 's | Colombians |
| 525. | killing | 7: [12, 12.0], 13: [10, 5.0] | killing israeli 's | List_of_Israeli_assassinations |
| 526. | recent | 8: [11, 5.5], 13: [12, 12.0], 39: [12, 6.0], 50: [21, 7.0] | recent 's photo | Google_Photos |
| 527. | west | 11: [20, 5.0], 18: [10, 10.0], 35: [36, 12.0], 49: [19, 6.33] | west israeli palestinian | Israeli–Palestinian_conflict |
| 528. | area | 11: [12, 12.0] | area 's photo | Dwayne's_Photo |
| 529. | conflict | 12: [12, 12.0] | conflict 's says | List_of_ongoing_armed_conflicts |
| 530. | held | 12: [20, 6.67], 33: [12, 12.0], 48: [24, 6.0] | held 's american | List_of_American_sportsperson-politicians |
| 531. | brazilian | 13: [12, 12.0] | brazilian brazil 's | Brazilian_Senate |
| 532. | americans | 14: [10, 10.0], 36: [12, 12.0] | americans 's american | Americans |
| 533. | big | 18: [10, 10.0], 22: [12, 12.0], 46: [12, 6.0] | big 's photo | Google_Photos |
| 534. | roman | 18: [12, 12.0] | roman catholic 's | Catholic_Church |
| 535. | coast | 19: [12, 12.0] | coast 's china | China_Coast_Guard |
| 536. | fire | 19: [11, 5.5], 32: [12, 12.0] | fire israeli 's | Yom_Kippur_War |
| 537. | region | 20: [11, 5.5], 31: [12, 12.0], 43: [10, 5.0] | region 's american | South_America |
| 538. | well | 21: [12, 6.0], 45: [10, 5.0], 50: [12, 12.0] | well 's american | American_Well |
| 539. | jail | 22: [12, 12.0] | jail 's world | Men's_Central_Jail |
| 540. | illegal | 26: [12, 12.0], 45: [13, 6.5] | illegal 's immigrants | Illegal_immigration_to_the_United_States |
| 541. | spying | 30: [12, 12.0] | spying china american | List_of_American_spies |
| 542. | sentenced | 30: [12, 12.0] | sentenced 's years | Sentenced |
| 543. | southern | 31: [12, 12.0] | southern taliban 's | Islamic_Emirate_of_Afghanistan |
| 544. | province | 32: [12, 12.0] | province 's china | Taiwan_Province,_People's_Republic_of_China |
| 545. | brunei | 33: [12, 12.0] | brunei 's wahid | Abdurrahman_Wahid |
| 546. | taken | 35: [10, 5.0], 39: [10, 5.0], 46: [12, 12.0] | taken 's says | Taken_(film) |
| 547. | retaliation | 38: [12, 12.0] | retaliation israeli israel | History_of_Israel |
| 548. | kenya | 44: [12, 12.0] | kenya 's nairobi | Nairobi |
| 549. | might | 46: [12, 12.0] | might 's says | Some_Might_Say |
| 550. | princess | 49: [12, 12.0] | princess japan 's | Aiko,_Princess_Toshi |
| 551. | failed | 49: [12, 12.0] | failed 's government | Failed_state |
| 552. | oslo | 50: [12, 12.0] | oslo 's peace | Oslo_Accords |
| 553. | explosives | 52: [12, 12.0] | explosives 's us | Plastic_explosive |
| 554. | arms | 11: [23, 11.5], 17: [16, 8.0] | arms 's bush | Samuel_P._Bush |
| 555. | federal | 3: [12, 6.0], 41: [11, 11.0] | federal 's government | Federal_government_of_the_United_States |
| 556. | time | 4: [11, 11.0], 10: [16, 8.0] | time 's first | First_Time |
| 557. | officer | 7: [11, 11.0] | officer 's police | Police_officer |
| 558. | secretary | 7: [12, 6.0], 42: [11, 11.0] | secretary powell 's | Colin_Powell |
| 559. | charged | 8: [11, 11.0] | charged 's world | Fully_Charged |
| 560. | asia | 9: [11, 11.0], 18: [18, 6.0] | asia world briefing | BBC_World_News |
| 561. | less | 11: [11, 5.5], 40: [11, 11.0] | less 's american | Self/less |
| 562. | trade | 13: [16, 5.33], 19: [32, 6.4], 22: [15, 7.5], 26: [22, 7.33], 36: [11, 11.0], 44: [12, 6.0] | trade 's world | World_Trade_Center_site |
| 563. | set | 13: [20, 5.0], 21: [11, 11.0] | set 's government | Federal_government_of_the_United_States |
| 564. | lawyers | 19: [11, 11.0] | lawyers 's court | Lawyer |
| 565. | air | 23: [10, 5.0], 30: [11, 11.0], 37: [15, 5.0] | air taliban 's | Taliban |
| 566. | truce | 24: [11, 11.0] | truce israeli cease-fire | Ceasefire |
| 567. | thousands | 29: [11, 11.0] | thousands 's people | Decimal_separator |
| 568. | middle | 31: [11, 11.0], 40: [11, 11.0] | middle east 's | Middle_East |
| 569. | measure | 33: [11, 11.0] | measure 's would | Measure_for_Measure |
| 570. | front | 35: [11, 11.0] | front taliban 's | Taliban |
| 571. | slavery | 36: [11, 11.0] | slavery conference nations | Reparations_for_slavery |
| 572. | clear | 38: [11, 11.0] | clear 's bush | George_H._W._Bush |
| 573. | led | 39: [11, 11.0] | led 's government | LED_lamp |
| 574. | bombs | 40: [11, 11.0] | bombs taliban 's | Taliban |
| 575. | demonstrations | 41: [11, 11.0] | demonstrations 's police | Demonstrations_in_support_of_Donald_Trump |
| 576. | reportedly | 46: [11, 11.0] | reportedly 's taliban | Taliban–ISIL_conflict_in_Afghanistan |
| 577. | setback | 46: [11, 11.0] | setback 's world | Setback_(land_use) |
| 578. | link | 47: [11, 11.0] | link 's says | Say's_law |
| 579. | ministers | 49: [11, 11.0] | ministers 's government | Minister_(government) |
| 580. | foundation | 49: [11, 11.0] | foundation 's groups | Foundation_series |
| 581. | old | 51: [11, 11.0] | old 's photo | Google_Photos |
| 582. | street | 51: [11, 11.0] | street 's police | Siege_of_Sidney_Street |
| 583. | carrying | 51: [11, 11.0] | carrying 's american | Wife-carrying |
| 584. | largest | 4: [10, 10.0] | largest 's world | Largest_airlines_in_the_world |
| 585. | western | 4: [12, 6.0], 32: [10, 10.0] | western 's china | China_Western_Development |
| 586. | control | 4: [10, 10.0] | control 's taliban | Islamic_Emirate_of_Afghanistan |
| 587. | arrested | 5: [10, 10.0] | arrested 's police | Arrest |
| 588. | entire | 5: [10, 10.0] | entire 's india | List_of_towns_in_India_by_population |
| 589. | business | 5: [10, 10.0] | business 's china | China |
| 590. | without | 6: [14, 7.0], 24: [10, 10.0] | without 's taliban | Taliban_treatment_of_women |
| 591. | white | 8: [10, 10.0], 11: [17, 8.5], 21: [10, 5.0], 30: [10, 5.0], 36: [12, 6.0] | white 's bush | George_W._Bush |
| 592. | made | 8: [10, 5.0], 14: [17, 8.5], 27: [10, 10.0] | made 's bush | George_H._W._Bush |
| 593. | village | 10: [10, 5.0], 49: [10, 10.0] | village 's photo | Colour_Photo |
| 594. | tribunal | 11: [10, 10.0], 30: [12, 6.0] | tribunal crimes milosevic | Trial_of_Slobodan_Milošević |
| 595. | weapons | 13: [10, 10.0], 17: [10, 5.0] | weapons 's bush | Presidency_of_George_W._Bush |
| 596. | china | 14: [160, 10.0] | china 's chinese | China |
| 597. | istanbul | 17: [10, 10.0] | istanbul turkey 's | Istanbul |
| 598. | seeks | 20: [10, 10.0], 33: [11, 5.5] | seeks 's bush | Prescott_Bush |
| 599. | team | 24: [10, 10.0] | team 's bush | Bush_family |
| 600. | soviet | 24: [13, 6.5], 51: [10, 10.0] | soviet 's russia | Russian_Soviet_Federative_Socialist_Republic |
| 601. | suspected | 27: [10, 10.0] | suspected 's american | Prime_Suspect_(American_TV_series) |
| 602. | trafficking | 28: [10, 10.0] | trafficking 's united | Human_trafficking_in_the_United_Kingdom |
| 603. | squatters | 28: [10, 10.0] | squatters land zimbabwe | White_people_in_Zimbabwe |
| 604. | gao | 30: [20, 10.0] | gao china chinese | China |
| 605. | lankan | 33: [10, 10.0] | lankan sri rebels | Sri_Lankan_Civil_War |
| 606. | remain | 36: [10, 10.0] | remain 's taliban | Islamic_Emirate_of_Afghanistan |
| 607. | later | 36: [10, 10.0] | later 's bush | Bush_family |
| 608. | trying | 38: [10, 10.0] | trying 's taliban | Taliban |
| 609. | efforts | 39: [10, 10.0] | efforts 's bush | Efforts_to_impeach_George_W._Bush |
| 610. | secure | 40: [10, 10.0] | secure 's taliban | Taliban_treatment_of_women |
| 611. | ground | 41: [20, 10.0], 48: [15, 7.5] | ground taliban 's | Taliban |
| 612. | began | 41: [12, 6.0], 48: [10, 10.0] | began 's military | Military |
| 613. | leave | 42: [10, 10.0] | leave 's taliban | Taliban |
| 614. | cross | 42: [16, 8.0], 45: [10, 10.0] | cross red taliban | International_Red_Cross_and_Red_Crescent_Movement |
| 615. | intended | 43: [10, 10.0] | intended 's bush | George_W._Bush |
| 616. | base | 43: [10, 10.0] | base 's american | Baseball |
| 617. | bid | 44: [11, 5.5], 51: [10, 10.0] | bid 's photo | Bids_for_the_2008_Summer_Olympics |
| 618. | personnel | 45: [10, 10.0] | personnel military american | Military_personnel |
| 619. | soldier | 45: [10, 10.0] | soldier israeli american | Israeli_Americans |
| 620. | put | 46: [10, 10.0] | put 's government | Copyright_status_of_works_by_the_federal_government_of_the_United_States |
| 621. | miles | 46: [10, 10.0] | miles 's taliban | Taliban_insurgency |
| 622. | homes | 47: [10, 10.0] | homes 's israeli | Israeli_demolition_of_Palestinian_property |
| 623. | hiding | 48: [10, 10.0] | hiding 's taliban | Taliban |
| 624. | trip | 48: [10, 10.0] | trip 's bush | George_H._W._Bush |
| 625. | talk | 50: [10, 10.0] | talk 's says | Talk_Talk |
| 626. | ethnic | 50: [10, 10.0] | ethnic macedonia rebels | 2001_insurgency_in_Macedonia |
| 627. | believe | 50: [10, 10.0] | believe 's say | Ripley's_Believe_It_or_Not! |
| 628. | review | 50: [10, 10.0] | review 's bush | George_H._W._Bush |
| 629. | begin | 51: [10, 10.0] | begin 's world | Menachem_Begin |
| 630. | rua | 51: [10, 10.0] | rua argentina pres | Fernando_de_la_Rúa |
| 631. | sex | 51: [10, 10.0] | sex 's women | Women_who_have_sex_with_women |
| 632. | briefing | 18: [68, 9.71] | briefing world 's | World_Briefing |
| 633. | military | 2: [29, 9.67] | military 's american | Military_history_of_the_United_States |
| 634. | forces | 6: [18, 6.0], 38: [19, 9.5] | forces 's taliban | Taliban_insurgency |
| 635. | island | 14: [19, 9.5] | island china 's | List_of_islands_of_China |
| 636. | debate | 16: [19, 9.5] | debate 's american | Debate |
| 637. | black | 40: [19, 9.5] | black 's white | Black_and_white |
| 638. | standoff | 14: [18, 9.0] | standoff 's china | 2020_China–India_skirmishes |
| 639. | peruvian | 17: [27, 9.0] | peruvian peru plane | COVID-19_pandemic_in_Peru |
| 640. | slobodan | 26: [18, 9.0] | slobodan milosevic tribunal | Trial_of_Slobodan_Milošević |
| 641. | troops | 38: [18, 9.0] | troops 's taliban | Afghan_peace_process |
| 642. | aboard | 41: [18, 9.0] | aboard american plane | Money_Plane |
| 643. | much | 46: [18, 9.0] | much 's bush | George_H._W._Bush |
| 644. | estrada | 3: [17, 8.5] | estrada philippines joseph | Joseph_Estrada |
| 645. | visit | 11: [21, 7.0], 16: [17, 8.5], 30: [27, 5.4] | visit 's bush | George_W._Bush |
| 646. | release | 14: [17, 8.5] | release 's china | China |
| 647. | junichiro | 17: [17, 8.5] | junichiro 's japan | Japanese_war_crimes |
| 648. | experts | 23: [10, 5.0], 44: [17, 8.5] | experts 's say | Expert_system |
| 649. | proof | 40: [17, 8.5] | proof laden says | Hamza_bin_Laden |
| 650. | retreat | 46: [17, 8.5] | retreat taliban 's | Taliban |
| 651. | israel | 13: [25, 8.33], 35: [28, 7.0] | israel palestinian israeli | Israeli–Palestinian_conflict |
| 652. | taiwan | 2: [10, 5.0], 20: [24, 8.0] | taiwan china 's | Taiwan,_China |
| 653. | defense | 2: [16, 8.0], 16: [10, 5.0] | defense 's bush | Bush_family |
| 654. | rubble | 5: [24, 8.0] | rubble india 's | Islam_in_India |
| 655. | u.s. | 5: [16, 8.0] | u.s. 's american | U.S._state |
| 656. | vladimir | 9: [11, 5.5], 24: [16, 8.0] | vladimir putin russia | Russia_under_Vladimir_Putin |
| 657. | fox | 22: [10, 5.0], 34: [16, 8.0], 36: [33, 5.5], 41: [11, 5.5] | fox mexico 's | Vicente_Fox |
| 658. | commanders | 42: [17, 5.67], 46: [16, 8.0] | commanders taliban afghanistan | Taliban_insurgency |
| 659. | group | 4: [21, 7.0], 17: [23, 7.67], 25: [15, 7.5] | group 's says | Say_Say_Say |
| 660. | least | 8: [15, 7.5], 47: [21, 5.25] | least 's world | Least_developed_countries |
| 661. | month | 16: [15, 7.5] | month 's american | American_Heart_Month |
| 662. | part | 20: [15, 7.5] | part 's government | Federal_government_of_the_United_States |
| 663. | back | 21: [10, 5.0], 26: [15, 7.5], 46: [11, 5.5] | back 's photo | Google_Photos |
| 664. | irish | 23: [15, 7.5] | irish ireland 's | Great_Famine_(Ireland) |
| 665. | global | 24: [22, 5.5], 26: [15, 7.5] | global 's bush | Barbara_Bush_(born_1981) |
| 666. | sec | 26: [15, 7.5], 28: [11, 5.5] | sec 's says | U.S._Securities_and_Exchange_Commission |
| 667. | italian | 39: [15, 7.5] | italian 's berlusconi | Silvio_Berlusconi |
| 668. | avoid | 44: [15, 7.5] | avoid 's american | United_States |
| 669. | corruption | 46: [15, 7.5] | corruption 's former | Corruption |
| 670. | largely | 49: [15, 7.5] | largely 's force | United_States_Space_Force |
| 671. | prisoners | 48: [37, 7.4] | prisoners taliban 's | Afghan_peace_process |
| 672. | soldiers | 5: [10, 5.0], 11: [14, 7.0] | soldiers taliban 's | Taliban_insurgency |
| 673. | public | 5: [15, 5.0], 39: [14, 7.0] | public 's photo | Google_Photos |
| 674. | far | 9: [14, 7.0] | far 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 675. | work | 18: [14, 7.0] | work 's says | Say's_law |
| 676. | billion | 19: [14, 7.0] | billion 's world | World_population |
| 677. | votes | 22: [14, 7.0] | votes 's pres | United_States_Electoral_College |
| 678. | make | 24: [14, 7.0] | make 's photo | Google_Photos |
| 679. | talks | 32: [21, 7.0] | talks 's peace | 2013–2014_Israeli–Palestinian_peace_talks |
| 680. | minister | 33: [14, 7.0] | minister 's prime | List_of_prime_ministers_of_the_United_Kingdom |
| 681. | including | 35: [14, 7.0] | including 's bush | Bush_family |
| 682. | hear | 41: [14, 7.0] | hear 's world | Hear_the_World_Foundation |
| 683. | weeks | 43: [14, 7.0], 50: [11, 5.5] | weeks 's two | Two_Weeks_Notice |
| 684. | -- | 50: [28, 7.0] | -- 's world | U.S._News_&_World_Report |
| 685. | bomb | 52: [14, 7.0] | bomb taliban 's | Taliban_insurgency |
| 686. | anthrax | 42: [41, 6.83] | anthrax 's attacks | 2001_anthrax_attacks |
| 687. | parliament | 22: [27, 6.75], 28: [17, 5.67] | parliament 's india | Parliament_of_India |
| 688. | day | 4: [10, 5.0], 41: [20, 6.67] | day 's government | Valentine's_Day |
| 689. | hundreds | 37: [11, 5.5], 51: [20, 6.67] | hundreds 's taliban | Islamic_Emirate_of_Afghanistan |
| 690. | uranium | 2: [13, 6.5] | uranium depleted kosovo | Depleted_uranium |
| 691. | foreign | 3: [26, 6.5] | foreign 's bush | Foreign_policy_of_the_George_W._Bush_administration |
| 692. | deaths | 12: [13, 6.5] | deaths 's palestinian | List_of_Palestinian_suicide_attacks |
| 693. | farm | 12: [13, 6.5] | farm disease 's | Chronic_wasting_disease |
| 694. | economy | 15: [13, 6.5], 26: [13, 6.5] | economy 's world | World_economy |
| 695. | religious | 22: [13, 6.5] | religious 's afghanistan | Soviet–Afghan_War |
| 696. | marijuana | 31: [13, 6.5] | marijuana american russia | Legality_of_cannabis |
| 697. | rules | 36: [13, 6.5] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 698. | identified | 39: [13, 6.5] | identified 's says | Identifier |
| 699. | together | 44: [13, 6.5] | together 's bush | George_H._W._Bush |
| 700. | see | 46: [13, 6.5], 50: [10, 5.0] | see 's bush | George_H._W._Bush |
| 701. | areas | 46: [13, 6.5] | areas taliban 's | Taliban |
| 702. | uprising | 48: [13, 6.5] | uprising israeli taliban | Taliban_treatment_of_women |
| 703. | allies | 48: [13, 6.5] | allies 's bush | George_H._W._Bush |
| 704. | list | 52: [13, 6.5] | list 's bush | Bush_family |
| 705. | economic | 42: [25, 5.0], 44: [19, 6.33] | economic 's bush | George_W._Bush |
| 706. | groups | 44: [25, 6.25] | groups 's taliban | Taliban |
| 707. | marines | 48: [25, 6.25] | marines taliban afghanistan | War_in_Afghanistan_(2001–present) |
| 708. | ariel | 6: [31, 6.2], 40: [10, 5.0] | ariel sharon israeli | Ariel_Sharon |
| 709. | nations | 16: [27, 5.4], 35: [31, 6.2] | nations united 's | United_Nations |
| 710. | afghanistan | 18: [10, 5.0], 38: [68, 6.18] | afghanistan taliban 's | Islamic_Emirate_of_Afghanistan |
| 711. | officials | 2: [30, 6.0] | officials 's say | Say_Say_Say |
| 712. | death | 3: [12, 6.0] | death 's world | Death_to_the_World |
| 713. | indian | 5: [18, 6.0], 40: [11, 5.5] | indian india 's | Economy_of_India |
| 714. | workers | 8: [25, 5.0], 17: [12, 6.0], 46: [17, 5.67] | workers 's aid | David_Haines_(aid_worker) |
| 715. | go | 11: [12, 6.0] | go 's says | The_Go-Go's |
| 716. | emergency | 14: [18, 6.0] | emergency 's china | List_of_emergency_telephone_numbers |
| 717. | station | 15: [12, 6.0] | station 's space | Space_station |
| 718. | plans | 15: [12, 6.0] | plans 's bush | George_W._Bush |
| 719. | liberal | 17: [12, 6.0] | liberal 's party | Liberal_Party |
| 720. | killings | 23: [12, 6.0] | killings palestinian 's | List_of_Israeli_assassinations |
| 721. | ending | 26: [12, 6.0] | ending 's pres | Happy_Ending_(film) |
| 722. | second | 28: [12, 6.0] | second 's government | Second_Kurz_government |
| 723. | tobin | 31: [12, 6.0] | tobin russia russian | Taxation_in_Russia |
| 724. | i.r.a | 32: [12, 6.0] | i.r.a irish ireland | Ireland |
| 725. | majority | 32: [12, 6.0] | majority 's party | Party_leaders_of_the_United_States_Senate |
| 726. | reports | 33: [12, 6.0] | reports 's taliban | Taliban |
| 727. | every | 38: [12, 6.0] | every 's says | Every_Time_You_Say_Goodbye |
| 728. | missiles | 40: [12, 6.0] | missiles 's missile | Missile |
| 729. | sheik | 41: [12, 6.0] | sheik 's says | Duncan_Sheik |
| 730. | rejects | 42: [12, 6.0] | rejects 's says | Say's_law |
| 731. | republican | 43: [12, 6.0] | republican 's irish | Irish_Republican_Army |
| 732. | wake | 44: [12, 6.0] | wake 's attacks | Wake_Island |
| 733. | ortega | 45: [12, 6.0] | ortega nicaragua former | Daniel_Ortega |
| 734. | residents | 46: [12, 6.0] | residents 's photo | The_Residents |
| 735. | saying | 48: [12, 6.0] | saying 's bush | George_W._Bush |
| 736. | study | 48: [12, 6.0] | study 's china | The_China_Study |
| 737. | governing | 49: [12, 6.0] | governing 's party | Ruling_party |
| 738. | number | 50: [12, 6.0] | number 's american | North_American_Numbering_Plan |
| 739. | decades | 51: [12, 6.0] | decades 's government | Federal_government_of_the_United_States |
| 740. | christmas | 52: [12, 6.0] | christmas 's refugees | Royal_Christmas_Message |
| 741. | abroad | 44: [23, 5.75] | abroad 's american | America_Abroad |
| 742. | four | 11: [17, 5.67] | four 's israeli | Israel–United_States_relations |
| 743. | yugoslav | 11: [17, 5.67] | yugoslav milosevic crimes | Slobodan_Milošević |
| 744. | target | 41: [17, 5.67] | target 's taliban | Islamic_Emirate_of_Afghanistan |
| 745. | mazar-i-sharif | 45: [17, 5.67] | mazar-i-sharif taliban northern | Mazar-i-Sharif |
| 746. | interim | 51: [28, 5.6] | interim government afghan | Afghan_Interim_Administration |
| 747. | kabul | 46: [105, 5.53] | kabul taliban afghanistan | Taliban_insurgency |
| 748. | march | 9: [11, 5.5] | march 's today | Today_(American_TV_program) |
| 749. | elections | 10: [11, 5.5] | elections 's party | Political_party_strength_in_U.S._states |
| 750. | like | 11: [11, 5.5] | like 's photo | Google_Photos |
| 751. | israeli | 13: [33, 5.5] | israeli palestinian israel | Israeli–Palestinian_conflict |
| 752. | crisis | 20: [11, 5.5], 51: [15, 5.0] | crisis 's government | 2020_Thuringian_government_crisis |
| 753. | five | 20: [11, 5.5] | five 's years | The_Last_Five_Years |
| 754. | ban | 20: [11, 5.5] | ban 's world | Ban_Ki-moon |
| 755. | spread | 20: [11, 5.5] | spread 's aids | HIV/AIDS |
| 756. | gen | 21: [11, 5.5] | gen 's pakistan | Military_coups_in_Pakistan |
| 757. | referendum | 23: [11, 5.5] | referendum 's vote | 2011_United_Kingdom_Alternative_Vote_referendum |
| 758. | u.n. | 26: [22, 5.5], 41: [10, 5.0] | u.n. united nations | Headquarters_of_the_United_Nations |
| 759. | give | 28: [11, 5.5] | give 's would | The_Hate_U_Give_(film) |
| 760. | released | 30: [11, 5.5] | released 's world | The_World's_Billionaires |
| 761. | fighting | 32: [11, 5.5] | fighting 's taliban | Taliban |
| 762. | notes | 33: [11, 5.5] | notes 's says | Say's_law |
| 763. | growing | 36: [11, 5.5] | growing 's china | China |
| 764. | evidence | 38: [11, 5.5] | evidence 's laden | Osama_bin_Laden_death_conspiracy_theories |
| 765. | joint | 38: [11, 5.5] | joint 's bush | Bush_family |
| 766. | japanese | 39: [11, 5.5] | japanese japan 's | Japan |
| 767. | warning | 40: [11, 5.5] | warning 's us | Without_Warning_(21_Savage,_Offset,_and_Metro_Boomin_album) |
| 768. | good | 41: [11, 5.5] | good 's says | Say's_law |
| 769. | bethlehem | 43: [11, 5.5] | bethlehem israeli palestinian | Palestinian_Christians |
| 770. | agree | 46: [11, 5.5] | agree 's us | Agree_to_disagree |
| 771. | soon | 46: [11, 5.5] | soon 's bush | George_W._Bush |
| 772. | mideast | 50: [11, 5.5] | mideast palestinian bush | George_W._Bush |
| 773. | seek | 51: [11, 5.5] | seek 's says | Hide-and-seek |
| 774. | suspect | 52: [11, 5.5] | suspect 's laden | Killing_of_Osama_bin_Laden |
| 775. | sides | 2: [10, 5.0], 24: [16, 5.33] | sides 's says | Say's_law |
| 776. | percent | 15: [15, 5.0], 22: [16, 5.33] | percent 's photo | Five-Percent_Nation |
| 777. | high | 17: [16, 5.33], 48: [15, 5.0] | high 's united | United_States |
| 778. | russian | 19: [16, 5.33] | russian russia 's | Russia |
| 779. | calls | 24: [16, 5.33] | calls 's bush | Bush_family |
| 780. | durban | 36: [16, 5.33] | durban conference racism | World_Conference_against_Racism_2001 |
| 781. | near | 37: [16, 5.33] | near 's taliban | Taliban_insurgency |
| 782. | fight | 39: [16, 5.33] | fight 's taliban | Taliban |
| 783. | ties | 43: [16, 5.33], 49: [10, 5.0] | ties 's us | Family_Ties |
| 784. | organization | 45: [16, 5.33], 50: [16, 5.33] | organization 's world | World_Health_Organization |
| 785. | family | 49: [16, 5.33] | family 's photo | Autobiography_of_a_Family_Photo |
| 786. | country | 2: [15, 5.0], 10: [21, 5.25] | country 's government | List_of_countries_by_government_budget |
| 787. | rebels | 4: [21, 5.25] | rebels 's macedonia | 2001_insurgency_in_Macedonia |
| 788. | albanian | 5: [10, 5.0], 10: [21, 5.25] | albanian macedonia rebels | 2001_insurgency_in_Macedonia |
| 789. | foot-and-mouth | 11: [21, 5.25] | foot-and-mouth disease britain | Foot-and-mouth_disease |
| 790. | central | 22: [21, 5.25] | central 's american | Central_America |
| 791. | first | 33: [21, 5.25] | first 's bush | Bush_family |
| 792. | bombings | 49: [21, 5.25] | bombings israeli arafat | Yasser_Arafat |
| 793. | state | 30: [36, 5.14] | state 's powell | Colin_Powell |
| 794. | envoy | 2: [10, 5.0] | envoy 's says | Kelly_Craft |
| 795. | kong | 2: [10, 5.0], 23: [10, 5.0] | kong hong 's | Hong_Kong |
| 796. | ehud | 4: [10, 5.0] | ehud barak sharon | Ehud_Barak |
| 797. | rescue | 5: [15, 5.0] | rescue american 's | The_Rescuers |
| 798. | law | 5: [10, 5.0] | law 's world | Parkinson's_law |
| 799. | whose | 11: [10, 5.0] | whose 's bush | Bush_family |
| 800. | animal | 11: [10, 5.0] | animal disease foot-and-mouth | Foot-and-mouth_disease |
| 801. | rural | 11: [10, 5.0] | rural 's people | Rural_People's_Movement |
| 802. | hague | 14: [20, 5.0] | hague tribunal crimes | International_Criminal_Tribunal_for_the_former_Yugoslavia |
| 803. | expected | 14: [10, 5.0] | expected 's american | Expected_value |
| 804. | us | 17: [35, 5.0] | us 's says | Say_Us |
| 805. | impeachment | 18: [10, 5.0] | impeachment 's wahid | Abdurrahman_Wahid |
| 806. | flights | 19: [10, 5.0] | flights plane china | Air_China_Flight_129 |
| 807. | authority | 19: [10, 5.0] | authority palestinian 's | Palestinian_National_Authority |
| 808. | deputy | 19: [10, 5.0] | deputy 's bush | White_House_Deputy_Chief_of_Staff |
| 809. | million | 22: [10, 5.0], 39: [20, 5.0] | million 's world | Mega_Millions |
| 810. | judge | 22: [10, 5.0] | judge 's world | Clark_S._Judge |
| 811. | june | 22: [10, 5.0] | june 's bush | Bush_family |
| 812. | re-election | 23: [10, 5.0] | re-election 's pres | 2018_United_States_Senate_elections |
| 813. | hong | 23: [10, 5.0] | hong kong 's | Hong_Kong |
| 814. | since | 24: [15, 5.0] | since 's photo | Google_Photos |
| 815. | shield | 24: [20, 5.0] | shield missile bush | United_States_national_missile_defense |
| 816. | civilian | 25: [10, 5.0] | civilian 's military | Civilian_control_of_the_military |
| 817. | moscow | 29: [10, 5.0], 50: [10, 5.0] | moscow russia 's | Moscow |
| 818. | italy | 29: [10, 5.0] | italy 's berlusconi | Silvio_Berlusconi |
| 819. | grants | 29: [10, 5.0] | grants world aid | Student_financial_aid_(United_States) |
| 820. | thailand | 31: [10, 5.0] | thailand 's prime | Prime_Minister_of_Thailand |
| 821. | among | 32: [10, 5.0] | among 's taliban | Taliban |
| 822. | prince | 33: [10, 5.0] | prince 's saudi | Crown_Prince_of_Saudi_Arabia |
| 823. | people | 35: [40, 5.0] | people 's world | People's_World |
| 824. | land | 36: [10, 5.0] | land 's photo | Photo_finish |
| 825. | army | 37: [10, 5.0] | army 's israeli | Israel_Defense_Forces |
| 826. | attack | 37: [25, 5.0] | attack 's american | Attack_Attack!_(American_band) |
| 827. | taliban | 38: [55, 5.0] | taliban afghanistan 's | Islamic_Emirate_of_Afghanistan |
| 828. | russians | 39: [10, 5.0] | russians 's russia | Russia |
| 829. | missions | 39: [10, 5.0] | missions 's says | Mission:_Impossible_(film_series) |
| 830. | win | 40: [10, 5.0] | win 's bush | George_W._Bush |
| 831. | destroy | 41: [10, 5.0] | destroy 's says | Destroy_Boys |
| 832. | warplanes | 41: [10, 5.0] | warplanes taliban american | War_in_Afghanistan_(2001–present) |
| 833. | suggests | 42: [10, 5.0] | suggests 's taliban | Taliban |
| 834. | local | 42: [10, 5.0] | local 's officials | Official |
| 835. | cnn | 42: [10, 5.0] | cnn laden foreign | Allegations_of_CIA_assistance_to_Osama_bin_Laden |
| 836. | berlin | 42: [10, 5.0] | berlin 's germany | Berlin |
| 837. | ira | 43: [10, 5.0] | ira ireland northern | Provisional_Irish_Republican_Army |
| 838. | raids | 43: [15, 5.0] | raids taliban afghanistan | Taliban_insurgency |
| 839. | saudis | 43: [10, 5.0] | saudis saudi arabia | King_of_Saudi_Arabia |
| 840. | abdullah | 47: [10, 5.0] | abdullah 's alliance | Abdullah_Abdullah |
| 841. | ahmed | 48: [10, 5.0] | ahmed 's alliance | Rafi_Ahmed |
| 842. | protestant | 48: [10, 5.0] | protestant ireland northern | Protestantism_in_Ireland |
| 843. | final | 48: [10, 5.0] | final 's taliban | Afghan_peace_process |
| 844. | crucial | 49: [10, 5.0] | crucial 's us | Micron_Technology |
| 845. | islam | 49: [10, 5.0] | islam 's afghanistan | Islam_in_Afghanistan |
| 846. | agreed | 49: [10, 5.0] | agreed 's taliban | Islamic_Emirate_of_Afghanistan |
| 847. | warns | 50: [10, 5.0] | warns 's says | Battle_of_Warns |
| 848. | television | 51: [10, 5.0] | television 's laden | Killing_of_Osama_bin_Laden |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | kabila | 3: [12, inf] | kabila 's congo | Laurent-Désiré_Kabila |
| 2. | spy | 14: [13, inf] | spy plane us | Hainan_Island_incident |
| 3. | plane | 14: [12, inf] | plane spy us | Hainan_Island_incident |
| 4. | anthrax | 41: [19, inf] | anthrax us case | 2001_anthrax_attacks |
| 5. | aid | 46: [16, inf] | aid workers taliban | Taliban_treatment_of_women |
| 6. | workers | 46: [12, inf] | workers aid taliban | Taliban_treatment_of_women |
| 7. | kunduz | 47: [10, inf] | kunduz surrender alliance | Siege_of_Kunduz |
| 8. | arafat | 49: [12, inf] | arafat 's israel | Yasser_Arafat |
| 9. | letters | 39: [23, 23.0] | letters 's capital | Capital_Letters_(song) |
| 10. | terror | 37: [11, 11.0] | terror us 's | Great_Purge |
| 11. | strikes | 41: [11, 11.0] | strikes air us | Drone_strike |
| 12. | kabul | 41: [15, 5.0], 46: [21, 10.5] | kabul taliban 's | Taliban's_rise_to_power |
| 13. | nepal | 23: [10, 10.0] | nepal 's royal | Nepalese_royal_massacre |
| 14. | laden | 50: [13, 6.5] | laden 's us | Osama_bin_Laden's_compound_in_Abbottabad |
| 15. | world | 37: [12, 6.0] | world brief 's | World_Prison_Brief |
| 16. | bombing | 41: [11, 5.5] | bombing us suicide | Suicide_attack |
| 17. | bush | 37: [10, 5.0] | bush 's china | Neil_Bush |
