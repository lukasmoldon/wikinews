# Keywords with the highest 'interestingness' in 2003

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
| 1. | campaign | 2: [10, inf], 43: [11, inf], 49: [10, inf] | campaign 's iraq | Iraq_Campaign_Medal |
| 2. | research | 2: [10, inf] | research 's nuclear | Bhabha_Atomic_Research_Centre |
| 3. | use | 2: [17, inf], 28: [12, 6.0] | use iraq 's | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 4. | sought | 2: [10, inf] | sought 's iraq | Iran–Iraq_War |
| 5. | trade | 2: [16, 8.0], 6: [10, inf], 12: [11, inf], 42: [22, 5.5] | trade 's world | World_Trade_Center_site |
| 6. | missiles | 2: [10, inf], 8: [14, 7.0], 12: [35, 17.5] | missiles iraq 's | Scud_missile |
| 7. | qaeda | 2: [22, 7.33], 14: [16, 5.33], 20: [40, 13.33], 24: [23, 11.5], 26: [26, inf], 32: [11, 5.5], 46: [26, 5.2] | qaeda 's iraq | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 8. | gun | 2: [12, inf] | gun iraq 's | Katharine_Gun |
| 9. | ireland | 2: [10, inf], 14: [15, 5.0], 25: [18, 9.0], 32: [16, 16.0] | ireland northern world | Northern_Ireland |
| 10. | japan | 2: [16, 8.0], 8: [16, inf], 13: [15, 5.0], 33: [27, 13.5], 41: [10, 5.0], 45: [10, 10.0] | japan north korea | Japan–North_Korea_relations |
| 11. | blair | 2: [14, inf], 17: [14, 7.0], 28: [24, 12.0], 47: [35, 5.83] | blair iraq prime | Tony_Blair |
| 12. | terror | 2: [12, 6.0], 10: [19, 19.0], 47: [11, inf] | terror 's iraq | War_on_terror |
| 13. | suspects | 2: [11, inf], 15: [10, inf], 46: [11, 11.0] | suspects american 's | The_Usual_Suspects |
| 14. | wife | 2: [10, inf] | wife 's says | The_Wife_of_Bath's_Tale |
| 15. | week | 2: [15, 5.0], 32: [10, inf] | week 's iraq | Iraq_War |
| 16. | sri | 2: [19, inf] | sri lanka world | Sri_Lanka_national_cricket_team |
| 17. | lanka | 2: [12, inf] | lanka sri world | Sri_Lanka_national_cricket_team |
| 18. | tamil | 2: [10, inf] | tamil sri lanka | Sri_Lankan_Tamils |
| 19. | taken | 2: [11, inf] | taken 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 20. | rebels | 2: [10, 5.0], 5: [16, 8.0], 17: [12, inf], 38: [11, inf] | rebels government 's | List_of_Star_Wars_Rebels_characters |
| 21. | energy | 2: [17, inf], 25: [12, 12.0] | energy nuclear iran | Nuclear_program_of_Iran |
| 22. | indonesia | 2: [16, inf], 8: [12, inf], 20: [11, inf] | indonesia indonesian 's | Indonesia |
| 23. | increases | 2: [12, inf] | increases 's iraq | Iraq |
| 24. | show | 2: [10, inf], 10: [14, inf], 13: [11, 5.5] | show 's iraq | Iraq_War |
| 25. | conference | 2: [12, inf], 10: [18, 9.0], 49: [10, inf] | conference 's iraq | Iraq_War |
| 26. | atomic | 2: [13, inf], 25: [15, 15.0] | atomic nuclear iran | Nuclear_facilities_in_Iran |
| 27. | food | 2: [11, 11.0], 5: [24, 6.0], 13: [23, inf], 20: [11, 5.5], 32: [10, inf], 47: [18, 18.0], 50: [15, 15.0] | food 's says | Food_and_Drug_Administration |
| 28. | talk | 2: [11, inf] | talk 's iraq | 2003_invasion_of_Iraq |
| 29. | giving | 2: [10, inf] | giving 's iraq | Iraq_War |
| 30. | arms | 2: [19, inf] | arms iraq 's | Coat_of_arms_of_Iraq |
| 31. | diplomats | 2: [10, inf], 20: [11, 5.5] | diplomats iraq 's | Abduction_of_Russian_diplomats_in_Iraq |
| 32. | bill | 2: [15, inf], 27: [25, 25.0], 44: [20, 5.0] | bill 's bush | George_H._W._Bush |
| 33. | richardson | 2: [19, inf] | richardson north korea | Bill_Richardson |
| 34. | jewish | 2: [13, inf], 11: [15, inf], 23: [17, 8.5] | jewish israel 's | Jewish_Agency_for_Israel |
| 35. | polish | 2: [10, inf] | polish poland 's | History_of_Jews_in_Poland |
| 36. | dutch | 2: [10, inf] | dutch 's europe | Dutch_language |
| 37. | duisenberg | 2: [10, inf] | duisenberg dutch bank | Wim_Duisenberg |
| 38. | arafat | 2: [10, 10.0], 23: [10, inf] | arafat palestinian israel | Yasser_Arafat |
| 39. | terrorist | 2: [13, inf], 12: [13, 13.0] | terrorist 's attacks | September_11_attacks |
| 40. | election | 2: [10, inf] | election 's party | 2024_United_States_presidential_election |
| 41. | nonproliferation | 2: [13, inf] | nonproliferation nuclear north | Treaty_on_the_Non-Proliferation_of_Nuclear_Weapons |
| 42. | greece | 2: [10, inf], 6: [12, inf], 50: [12, inf] | greece europe world | Greece |
| 43. | roh | 3: [13, inf], 9: [19, 9.5] | roh korea north | Roh_Moo-hyun |
| 44. | moo | 3: [11, inf], 9: [13, 6.5] | moo korea north | North_Korea–South_Korea_relations |
| 45. | hyun | 3: [11, inf], 9: [13, 6.5] | hyun korea north | Hyun_Bin |
| 46. | pope | 3: [16, inf], 23: [14, inf], 37: [16, 8.0], 52: [11, inf] | pope paul john | Pope_John_Paul_II |
| 47. | taliban | 3: [10, inf], 23: [12, 12.0], 41: [13, 6.5] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 48. | kurdish | 3: [13, inf], 6: [30, 5.0] | kurdish iraq american | Iraqi–Kurdish_conflict |
| 49. | date | 3: [10, inf] | date iraq 's | Dating |
| 50. | zimbabwe | 3: [10, inf], 5: [18, inf], 19: [14, inf], 24: [11, inf], 38: [22, 5.5] | zimbabwe mugabe africa | Robert_Mugabe |
| 51. | officer | 3: [16, inf], 6: [12, 6.0], 16: [12, 12.0] | officer 's american | Officer_(armed_forces) |
| 52. | manchester | 3: [10, inf] | manchester police officer | Murders_of_Nicola_Hughes_and_Fiona_Bone |
| 53. | officers | 3: [13, inf], 47: [11, inf] | officers 's american | List_of_active_duty_United_States_four-star_officers |
| 54. | scientists | 3: [14, inf] | scientists 's weapons | List_of_states_with_nuclear_weapons |
| 55. | cyprus | 3: [16, inf], 9: [10, inf] | cyprus europe world | Cyprus |
| 56. | vatican | 3: [15, inf], 5: [18, 18.0], 31: [10, inf] | vatican pope world | Vatican_City_in_World_War_II |
| 57. | back | 3: [10, inf], 21: [25, 5.0] | back 's iraq | Iraq |
| 58. | politicians | 3: [11, inf] | politicians 's government | List_of_foreign-born_United_States_politicians |
| 59. | comments | 3: [11, inf], 24: [11, inf], 43: [11, inf] | comments 's iraq | 2003_invasion_of_Iraq |
| 60. | votes | 3: [11, inf] | votes 's iraq | Iraq_War |
| 61. | chemical | 3: [11, inf], 33: [11, inf] | chemical iraq weapons | Iraqi_chemical_weapons_program |
| 62. | polio | 3: [12, inf] | polio india cases | Pulse_Polio |
| 63. | private | 4: [10, inf], 29: [13, inf], 45: [12, 6.0] | private 's iraq | Private_militias_in_Iraq |
| 64. | colin | 4: [13, inf], 16: [14, 14.0], 43: [10, 5.0], 49: [12, inf] | colin powell iraq | Colin_Powell |
| 65. | powell | 4: [25, inf], 16: [17, 5.67], 28: [15, 5.0], 32: [27, 13.5], 43: [21, 10.5], 49: [28, inf] | powell iraq state | Colin_Powell |
| 66. | crimes | 4: [15, 15.0], 11: [14, 7.0], 23: [10, inf], 31: [19, 9.5] | crimes 's tribunal | International_Military_Tribunal_for_the_Far_East |
| 67. | college | 4: [16, inf] | college 's students | Student |
| 68. | kuwait | 4: [13, inf] | kuwait iraq american | Invasion_of_Kuwait |
| 69. | u.n | 4: [10, 10.0], 6: [16, inf] | u.n iraq 's | Iraq_War |
| 70. | much | 4: [12, 6.0], 10: [22, 22.0], 42: [12, inf] | much 's iraq | Iraq_War |
| 71. | cleric | 4: [11, inf], 35: [25, 25.0], 41: [10, inf] | cleric 's iraq | Muqtada_al-Sadr |
| 72. | taiwan | 4: [10, inf], 18: [14, 7.0] | taiwan china sars | 2002–2004_SARS_outbreak |
| 73. | team | 4: [15, 7.5], 9: [18, inf], 23: [13, 6.5] | team iraq 's | Iraq_national_football_team |
| 74. | pilots | 4: [14, inf] | pilots iraq air | Iraqi_Air_Force |
| 75. | zones | 4: [10, inf] | zones american iraq | Iraqi_no-fly_zones_conflict |
| 76. | address | 5: [13, inf], 36: [11, inf] | address 's bush | George_W._Bush |
| 77. | signs | 5: [10, inf], 12: [13, inf], 15: [11, inf] | signs 's iraq | Iraqi_Sign_Language |
| 78. | divided | 5: [11, inf] | divided 's iraq | Iraq |
| 79. | fight | 5: [14, inf], 43: [11, 11.0] | fight 's iraq | War_in_Iraq_(2013–2017) |
| 80. | tibetan | 5: [14, inf] | tibetan chinese china | Sino-Tibetan_languages |
| 81. | monk | 5: [12, inf] | monk tibetan court | Tibetan_Buddhism |
| 82. | rebel | 5: [14, 7.0], 18: [12, inf], 26: [11, 5.5] | rebel 's government | Rebellion |
| 83. | kandahar | 5: [12, inf] | kandahar taliban afghanistan | United_States_invasion_of_Afghanistan |
| 84. | accord | 5: [17, inf], 10: [13, inf], 18: [10, 5.0], 29: [10, 5.0] | accord 's peace | Camp_David_Accords |
| 85. | letter | 5: [12, inf], 21: [10, 5.0] | letter 's iraq | Iraqi_insurgency_(2003–2011) |
| 86. | journalists | 5: [14, inf], 12: [10, inf], 14: [23, 23.0], 17: [11, inf], 19: [12, 12.0] | journalists 's american | List_of_Jewish_American_journalists |
| 87. | abuse | 5: [10, inf] | abuse children 's | Child_abuse |
| 88. | sex | 5: [11, inf] | sex 's europe | Recognition_of_same-sex_unions_in_Europe |
| 89. | explosion | 5: [13, inf], 52: [11, 11.0] | explosion killed people | 2020_Beirut_explosion |
| 90. | militant | 5: [15, inf], 32: [11, 11.0] | militant palestinian israeli | Israeli–Palestinian_conflict |
| 91. | helicopter | 5: [13, inf], 45: [28, inf] | helicopter american iraq | List_of_aviation_shootdowns_and_accidents_during_the_Iraq_War |
| 92. | operations | 5: [10, inf], 18: [14, 14.0], 50: [10, 5.0] | operations iraq 's | Iraq_War |
| 93. | prison | 5: [10, 10.0], 38: [20, inf] | prison 's years | Prison |
| 94. | christians | 5: [11, inf] | christians 's muslims | Christianity_and_Islam |
| 95. | analysts | 5: [10, inf] | analysts 's say | Tiffany_Cross |
| 96. | chechen | 5: [13, inf] | chechen russia russian | Chechen–Russian_conflict |
| 97. | freed | 5: [12, inf] | freed 's world | Free_World |
| 98. | rising | 5: [10, inf] | rising 's iraq | Iraq |
| 99. | bus | 5: [15, inf], 34: [13, 13.0] | bus israeli hamas | Hamas |
| 100. | columbia | 6: [11, inf] | columbia space canada | Canadian_Space_Agency |
| 101. | attempts | 6: [10, inf] | attempts 's american | List_of_United_States_presidential_assassination_attempts_and_plots |
| 102. | park | 6: [17, inf], 37: [16, inf] | park 's national | List_of_national_parks_of_the_United_States |
| 103. | mugabe | 6: [12, inf], 14: [14, 14.0], 19: [11, inf] | mugabe zimbabwe 's | Robert_Mugabe |
| 104. | rumsfeld | 6: [16, inf], 12: [15, 5.0], 24: [19, 19.0], 36: [10, 10.0], 41: [12, inf], 43: [13, inf], 46: [17, 17.0], 49: [32, 10.67] | rumsfeld iraq defense | Donald_Rumsfeld |
| 105. | text | 6: [12, inf], 10: [10, 5.0] | text following 's | Text_messaging |
| 106. | suicide | 6: [11, 5.5], 13: [24, 6.0], 44: [20, 5.0], 47: [15, 5.0], 52: [16, inf] | suicide 's palestinian | List_of_Palestinian_suicide_attacks |
| 107. | michigan | 6: [12, inf] | michigan mr. iraq | Gulf_War |
| 108. | congo | 7: [13, inf], 19: [10, inf], 22: [14, inf], 29: [10, inf] | congo africa force | Belgian_Congo |
| 109. | laden | 7: [18, 9.0], 21: [10, 5.0], 37: [16, inf] | laden qaeda osama | Hamza_bin_Laden |
| 110. | planning | 7: [15, 7.5], 37: [12, inf], 50: [12, inf] | planning iraq 's | 2003_invasion_of_Iraq |
| 111. | philippines | 7: [11, inf], 12: [10, 5.0] | philippines asia world | Philippines |
| 112. | major | 7: [16, inf], 27: [12, 6.0], 32: [12, inf] | major 's iraq | Iraq |
| 113. | foods | 7: [12, inf] | foods europe european | Europe |
| 114. | children | 7: [10, 10.0], 31: [14, 7.0], 34: [19, 6.33], 39: [10, inf] | children 's american | Children's_literature |
| 115. | target | 7: [10, inf] | target 's iraq | Iraqi_insurgency_(2003–2011) |
| 116. | tape | 7: [10, inf] | tape hussein 's | Qusay_Hussein |
| 117. | cia | 7: [14, inf], 40: [20, inf], 44: [11, 5.5] | cia 's intelligence | Central_Intelligence_Agency |
| 118. | tenet | 7: [14, inf], 28: [10, inf] | tenet cia iraq | George_Tenet |
| 119. | berlusconi | 7: [12, 12.0], 19: [12, 12.0], 22: [13, inf], 25: [10, 5.0], 31: [12, 6.0], 34: [10, inf], 46: [10, inf] | berlusconi italy prime | Silvio_Berlusconi |
| 120. | embassy | 8: [12, inf], 32: [19, inf], 45: [10, 10.0] | embassy american 's | 1998_United_States_embassy_bombings |
| 121. | town | 8: [15, 7.5], 12: [11, inf], 26: [18, inf] | town 's american | S-Town |
| 122. | abdullah | 8: [12, inf], 20: [11, inf] | abdullah 's american | Abdullah_Abdullah |
| 123. | training | 8: [11, inf], 27: [10, inf] | training iraq 's | NATO_Training_Mission_–_Iraq |
| 124. | hamas | 8: [22, 11.0], 10: [15, inf], 18: [18, 18.0], 49: [10, inf] | hamas palestinian israeli | Hamas |
| 125. | fire | 8: [22, 22.0], 38: [12, inf], 45: [10, 10.0] | fire 's american | St._Elmo's_fire |
| 126. | chirac | 8: [18, inf], 15: [12, 6.0], 38: [10, inf], 47: [15, 7.5] | chirac france iraq | Jacques_Chirac |
| 127. | lived | 8: [10, inf] | lived 's iraq | Iraq |
| 128. | arab | 8: [19, 19.0], 26: [11, inf], 49: [15, inf] | arab iraq 's | Arab_Federation |
| 129. | shields | 8: [11, inf] | shields iraqi american | Operation_Desert_Shield_(Iraq) |
| 130. | egypt | 8: [13, inf], 12: [20, 5.0] | egypt 's arab | Egypt |
| 131. | nigerian | 8: [10, 10.0], 17: [11, inf] | nigerian pres 's | Nigeria |
| 132. | croatia | 8: [10, inf], 23: [13, inf] | croatia 's europe | 2013_enlargement_of_the_European_Union |
| 133. | arabia | 8: [12, inf], 12: [15, inf], 18: [13, 6.5], 20: [32, 32.0] | arabia saudi 's | Saudi_Arabia |
| 134. | scotland | 8: [10, inf] | scotland libya 's | History_of_Libya_under_Muammar_Gaddafi |
| 135. | department | 9: [12, inf] | department state iraq | Islamic_State_of_Iraq_and_the_Levant |
| 136. | mideast | 9: [11, 5.5], 30: [10, inf], 45: [11, 5.5] | mideast bush palestinian | Israeli–Palestinian_conflict |
| 137. | cbs | 9: [14, inf] | cbs interview hussein | February_2003_Saddam_Hussein_interview |
| 138. | claims | 9: [11, inf] | claims 's iraq | Territory_of_the_Islamic_State |
| 139. | reactor | 9: [16, inf] | reactor nuclear north | List_of_nuclear_reactors |
| 140. | concerns | 9: [12, inf] | concerns 's iraq | Iraq |
| 141. | cabinet | 9: [17, inf], 20: [10, inf], 36: [10, inf], 39: [12, inf] | cabinet 's palestinian | Palestinian_National_Authority |
| 142. | far-right | 9: [11, inf] | far-right party 's | Far-right_politics |
| 143. | parade | 9: [11, inf] | parade 's first | Macy's_Thanksgiving_Day_Parade |
| 144. | samba | 9: [10, inf] | samba carnival parade | Brazilian_Carnival |
| 145. | labor | 9: [11, 5.5], 11: [15, 7.5], 22: [12, inf], 40: [10, inf] | labor 's blair | Battle_of_Blair_Mountain |
| 146. | netanyahu | 9: [10, inf] | netanyahu israel sharon | Benjamin_Netanyahu |
| 147. | decision | 9: [13, 13.0], 22: [11, inf], 36: [15, 7.5] | decision 's iraq | Iraq_War |
| 148. | lawmakers | 9: [10, inf] | lawmakers 's iraq | Iraq_and_weapons_of_mass_destruction |
| 149. | tobacco | 9: [10, inf], 18: [10, inf], 21: [10, inf] | tobacco treaty health | WHO_Framework_Convention_on_Tobacco_Control |
| 150. | airlines | 9: [10, inf], 14: [11, 5.5] | airlines sars taiwan | COVID-19_pandemic_in_Taiwan |
| 151. | camp | 10: [18, inf], 24: [12, 6.0], 41: [21, 5.25] | camp iraq 's | Camp_Justice_(Iraq) |
| 152. | deployment | 10: [12, inf], 14: [10, 5.0] | deployment iraq troops | Multi-National_Force_–_Iraq |
| 153. | pakistan | 10: [39, 5.57], 17: [24, 8.0], 22: [12, 12.0], 39: [10, inf] | pakistan 's india | India–Pakistan_relations |
| 154. | bank | 10: [17, inf] | bank israeli palestinian | Israeli_West_Bank_barrier |
| 155. | joint | 10: [10, inf], 13: [11, inf], 26: [12, inf] | joint iraq 's | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 156. | study | 10: [12, inf], 19: [10, 10.0], 42: [12, 6.0], 49: [10, inf] | study 's iraq | Iraq_Study_Group |
| 157. | stalin | 10: [10, inf] | stalin 's trials | Moscow_Trials |
| 158. | records | 10: [10, inf] | records 's iraq | Iraq |
| 159. | transcript | 10: [32, inf] | transcript following 's | The_Transcript |
| 160. | recorded | 10: [32, inf] | recorded 's following | Cult_following |
| 161. | zoo | 10: [10, inf] | zoo 's animals | Zoo |
| 162. | oil | 10: [20, 10.0], 12: [31, 15.5], 24: [18, inf], 26: [28, 28.0], 33: [14, 14.0], 44: [25, 6.25] | oil 's iraq | Oil_reserves_in_Iraq |
| 163. | post | 10: [10, 5.0], 44: [10, inf] | post 's palestinian | Palestinians |
| 164. | haifa | 10: [11, inf] | haifa israeli israel | Israelis |
| 165. | abbas | 10: [12, inf], 16: [36, 9.0], 27: [15, 5.0] | abbas palestinian prime | Mahmoud_Abbas |
| 166. | annan | 11: [11, inf], 13: [11, 11.0], 34: [10, inf] | annan iraq kofi | Kofi_Annan |
| 167. | hong | 11: [13, 6.5], 50: [14, inf] | hong kong sars | Hong_Kong |
| 168. | kong | 11: [13, 6.5], 50: [14, inf] | kong hong sars | 2002–2004_SARS_outbreak |
| 169. | german | 11: [15, 5.0], 42: [13, 13.0], 50: [13, inf] | german 's germany | Germany |
| 170. | mexico | 11: [21, 21.0], 47: [23, inf], 49: [12, inf] | mexico 's world | Mexico |
| 171. | gain | 11: [11, inf] | gain 's iraq | Iraq |
| 172. | border | 11: [17, 8.5], 19: [12, 12.0], 22: [10, inf], 45: [16, 8.0] | border 's american | Canada–United_States_border |
| 173. | carrier | 11: [10, inf], 18: [10, 10.0] | carrier iraq 's | Nimitz-class_aircraft_carrier |
| 174. | tribunal | 11: [10, inf], 31: [13, 13.0] | tribunal crimes united | International_Military_Tribunal_for_the_Far_East |
| 175. | island | 11: [11, inf], 28: [11, 5.5] | island 's taiwan | Geography_of_Taiwan |
| 176. | prince | 11: [12, inf], 20: [12, inf] | prince saudi 's | Salman_of_Saudi_Arabia |
| 177. | canada | 11: [10, inf], 16: [12, 6.0], 27: [11, 11.0], 30: [10, 5.0], 32: [14, inf], 45: [10, inf] | canada 's canadian | Canada |
| 178. | orgn | 12: [17, inf] | orgn health world | .uk |
| 179. | york | 12: [20, 6.67], 16: [10, inf] | york iraq 's | Iraq_War |
| 180. | sons | 12: [15, 15.0], 15: [11, inf], 30: [40, inf] | sons hussein 's | Qusay_Hussein |
| 181. | leave | 12: [25, inf], 45: [15, 15.0] | leave 's iraq | Iraq_War |
| 182. | sars | 12: [13, inf], 37: [18, inf], 43: [10, inf] | sars health cases | 2002–2004_SARS_outbreak |
| 183. | thought | 12: [11, inf] | thought 's american | Thought |
| 184. | clear | 12: [12, inf], 46: [10, 5.0] | clear 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 185. | exile | 12: [12, inf], 15: [11, 5.5] | exile iraqi 's | Exile |
| 186. | command | 12: [16, inf], 36: [14, 7.0] | command iraq american | Revolutionary_Command_Council_(Iraq) |
| 187. | farmers | 12: [10, inf] | farmers 's trade | Farmers'_Produce_Trade_and_Commerce_(Promotion_and_Facilitation)_Act,_2020 |
| 188. | train | 12: [10, inf] | train american say | 50_Ways_to_Say_Goodbye |
| 189. | missile | 12: [33, 8.25], 24: [12, inf], 45: [11, 11.0] | missile iraq 's | Scud_missile |
| 190. | cruise | 12: [14, inf] | cruise american iraq | 1996_cruise_missile_strikes_on_Iraq |
| 191. | targets | 12: [19, 9.5], 20: [14, inf] | targets american iraq | American-led_intervention_in_Iraq_(2014–present) |
| 192. | unit | 12: [12, inf] | unit iraq 's | Multi-National_Force_–_Iraq |
| 193. | saudi | 12: [24, inf], 20: [76, 25.33], 26: [10, 5.0], 38: [20, 5.0] | saudi arabia 's | Saudi_Arabia |
| 194. | bunker | 12: [10, inf] | bunker hussein officials | Mount_Weather_Emergency_Operations_Center |
| 195. | defiance | 12: [10, inf] | defiance iraqi 's | 2003_invasion_of_Iraq |
| 196. | strike | 12: [35, 17.5], 24: [14, inf], 33: [13, 13.0], 43: [12, inf] | strike 's american | 2007–08_Writers_Guild_of_America_strike |
| 197. | basra | 12: [15, inf], 33: [15, 5.0] | basra iraq city | Basra |
| 198. | constitution | 12: [10, inf], 50: [10, inf] | constitution 's iraq | Constitution_of_Iraq |
| 199. | poll | 12: [10, inf], 44: [11, inf] | poll 's iraq | Iraq_War |
| 200. | surrender | 12: [16, inf] | surrender 's iraqi | 2003_invasion_of_Iraq |
| 201. | guard | 12: [10, inf], 29: [10, inf] | guard 's iraq | Republican_Guard_(Iraq) |
| 202. | videotape | 12: [10, inf] | videotape hussein says | Uday_Hussein |
| 203. | launched | 12: [12, inf] | launched 's iraq | Iran–Iraq_War |
| 204. | red | 12: [10, 5.0], 29: [15, inf] | red 's cross | International_Red_Cross_and_Red_Crescent_Movement |
| 205. | gear | 12: [10, inf] | gear american iraq | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 206. | buildings | 12: [15, inf], 15: [23, 11.5] | buildings 's american | United_States_Capitol |
| 207. | bombardment | 12: [11, inf] | bombardment baghdad iraqi | Green_Zone |
| 208. | afghan | 12: [12, 6.0], 17: [16, 5.33], 21: [14, inf] | afghan afghanistan taliban | War_in_Afghanistan_(2001–present) |
| 209. | ruins | 12: [10, inf] | ruins 's iraq | Iraq |
| 210. | dissidents | 12: [11, inf] | dissidents 's cuba | Cuban_dissident_movement |
| 211. | patriot | 12: [10, inf] | patriot missile missiles | MIM-104_Patriot |
| 212. | fighters | 13: [22, 5.5], 46: [11, inf] | fighters iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 213. | battle | 13: [43, 8.6], 18: [10, inf] | battle 's american | List_of_American_Civil_War_battles |
| 214. | ambushes | 13: [11, inf] | ambushes american soldiers | Tongo_Tongo_ambush |
| 215. | convoy | 13: [13, inf], 26: [24, 24.0], 51: [10, inf] | convoy american iraq | 2004_Iraq_KBR_convoy_ambush |
| 216. | najaf | 13: [33, inf], 35: [13, 6.5] | najaf iraqi iraq | Najaf |
| 217. | armor | 13: [11, inf] | armor iraq baghdad | Battle_of_Baghdad_(2003) |
| 218. | inside | 13: [10, 5.0], 40: [12, inf] | inside 's iraq | 2003_invasion_of_Iraq |
| 219. | symptoms | 13: [10, inf] | symptoms sars disease | Severe_acute_respiratory_syndrome |
| 220. | relief | 13: [16, 16.0], 43: [10, inf] | relief iraq 's | Iraq_Relief_and_Reconstruction_Fund |
| 221. | tells | 13: [11, 5.5], 20: [11, inf] | tells iraq 's | Iraq_War |
| 222. | committee | 13: [12, 12.0], 25: [24, inf] | committee iraq 's | Committee_for_the_Liberation_of_Iraq |
| 223. | delays | 13: [10, inf] | delays iraq 's | 2003_invasion_of_Iraq |
| 224. | postwar | 13: [16, inf], 28: [11, 11.0], 37: [15, 7.5] | postwar iraq 's | Iran–Iraq_War |
| 225. | skirmishes | 13: [11, inf] | skirmishes iraqi baghdad | Battle_of_Baghdad_(2003) |
| 226. | thrust | 13: [12, inf] | thrust baghdad 's | 2003_Baghdad_DHL_attempted_shootdown_incident |
| 227. | paramilitary | 13: [10, inf] | paramilitary american 's | Special_Activities_Center |
| 228. | india | 13: [12, inf], 22: [15, 7.5], 26: [26, 26.0], 29: [10, 5.0], 33: [10, 10.0] | india 's world | Mister_India_World |
| 229. | passengers | 13: [14, inf], 19: [15, 7.5] | passengers 's flights | Longest_flights |
| 230. | franks | 14: [11, inf], 28: [11, inf] | franks iraq 's | Tommy_Franks |
| 231. | bombings | 14: [11, inf], 20: [17, inf], 33: [10, inf], 44: [14, 7.0], 46: [13, inf] | bombings suicide 's | Suicide_attack |
| 232. | informant | 14: [10, inf] | informant hussein 's | Uday_Hussein |
| 233. | rabin | 14: [12, inf] | rabin informant israel | USS_Liberty_incident |
| 234. | driver | 14: [10, inf] | driver iraqi american | Foreign_hostages_in_Iraq |
| 235. | complete | 14: [10, inf] | complete iraq 's | Occupation_of_Iraq_(2003–2011) |
| 236. | -- | 14: [18, 6.0], 23: [14, 14.0], 37: [13, inf], 45: [14, 7.0] | -- 's iraq | 2003_invasion_of_Iraq |
| 237. | fleeing | 14: [11, inf] | fleeing iraq hussein | Uday_Hussein |
| 238. | agrees | 14: [11, inf] | agrees 's iraq | 2003_invasion_of_Iraq |
| 239. | arrest | 14: [17, 5.67], 38: [12, inf] | arrest 's police | Arrest |
| 240. | programs | 14: [14, 14.0], 19: [21, 10.5], 21: [14, inf], 51: [11, inf] | programs 's weapons | North_Korea_and_weapons_of_mass_destruction |
| 241. | bushmen | 14: [10, inf] | bushmen san south | San_people |
| 242. | african | 14: [14, inf] | african africa 's | Africa |
| 243. | information | 14: [11, 5.5], 28: [16, inf], 40: [15, 7.5] | information 's iraq | List_of_Iraqi_Information_Ministers |
| 244. | milosevic | 14: [10, inf], 17: [10, inf] | milosevic trial former | Trial_of_Slobodan_Milošević |
| 245. | airport | 14: [42, inf] | airport 's baghdad | Baghdad_International_Airport |
| 246. | order | 15: [26, 5.2], 44: [13, inf] | order iraq 's | 2003_invasion_of_Iraq_order_of_battle |
| 247. | hits | 15: [10, inf] | hits 's iraqi | Hit,_Iraq |
| 248. | moved | 15: [10, inf], 19: [11, inf] | moved 's iraq | 2003_invasion_of_Iraq |
| 249. | palace | 15: [11, inf], 48: [10, 10.0] | palace 's hussein | Uday_Hussein |
| 250. | differences | 15: [11, inf] | differences iraq 's | 2003_invasion_of_Iraq |
| 251. | fall | 15: [25, 6.25], 21: [14, inf], 45: [12, 6.0] | fall 's iraq | Iraq_War |
| 252. | looting | 15: [37, inf] | looting 's iraq | Archaeological_looting_in_Iraq |
| 253. | fallen | 15: [10, inf] | fallen 's iraqi | Iran–Iraq_War |
| 254. | fell | 15: [13, inf] | fell 's american | Norman_Fell |
| 255. | urges | 15: [16, 8.0], 36: [11, inf] | urges 's iraq | Iran–Iraq_War |
| 256. | alert | 15: [11, inf], 21: [20, inf] | alert 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 257. | rule | 15: [27, 5.4], 21: [14, 7.0], 44: [11, 11.0], 50: [12, inf] | rule 's iraq | Ba'athist_Iraq |
| 258. | putin | 15: [11, inf], 20: [26, 13.0], 44: [25, 12.5], 49: [19, 6.33] | putin russia 's | Russia_under_Vladimir_Putin |
| 259. | grip | 15: [11, inf] | grip 's hussein | Saddam_Hussein |
| 260. | infected | 15: [12, inf], 21: [10, 10.0] | infected sars disease | 2002–2004_SARS_outbreak |
| 261. | looters | 15: [12, inf] | looters 's american | Looting |
| 262. | beijing | 15: [13, inf], 28: [10, inf] | beijing china 's | Beijing |
| 263. | tikrit | 15: [11, inf] | tikrit hussein 's | Tikrit |
| 264. | refugees | 15: [10, inf], 35: [12, inf] | refugees 's iraq | Refugees_of_Iraq |
| 265. | museum | 15: [10, inf], 18: [22, 11.0] | museum 's iraq | National_Museum_of_Iraq |
| 266. | syria | 16: [99, 7.62], 41: [31, 7.75], 49: [18, inf] | syria iraq 's | Iraq–Syria_relations |
| 267. | liberal | 16: [10, inf] | liberal 's party | Liberal_Party |
| 268. | rate | 16: [12, inf] | rate 's percent | List_of_countries_by_obesity_rate |
| 269. | jenin | 16: [14, inf] | jenin israeli palestinian | Battle_of_Jenin_(2002) |
| 270. | policy | 16: [15, inf], 41: [12, 12.0] | policy 's iraq | Foreign_policy_of_the_Barack_Obama_administration |
| 271. | sanctions | 16: [24, inf], 19: [27, 5.4], 26: [10, 10.0], 33: [12, inf], 41: [11, inf], 51: [10, inf] | sanctions iraq 's | Sanctions_against_Iraq |
| 272. | mayor | 16: [10, inf] | mayor 's city | Mayor_of_New_York_City |
| 273. | penalties | 16: [12, inf] | penalties north bush | George_H._W._Bush |
| 274. | create | 16: [10, inf] | create 's iraq | Iraq |
| 275. | families | 16: [12, 6.0], 45: [13, inf] | families 's iraq | Iraq |
| 276. | business | 16: [15, 7.5], 46: [13, inf], 49: [12, inf] | business 's iraq | Iraq_War |
| 277. | particularly | 16: [11, inf] | particularly 's iraq | Iraq_War |
| 278. | achille | 16: [11, inf] | achille american abbas | Achille_Lauro_hijacking |
| 279. | lauro | 16: [11, inf] | lauro american abbas | Achille_Lauro_hijacking |
| 280. | pipeline | 16: [11, inf] | pipeline oil iraq | Kirkuk–Ceyhan_Oil_Pipeline |
| 281. | crowd | 16: [11, inf] | crowd 's soldiers | Crowd_manipulation |
| 282. | lift | 16: [12, inf] | lift sanctions 's | United_States_sanctions |
| 283. | tariq | 17: [14, inf] | tariq 's iraqi | Tariq_Aziz |
| 284. | aziz | 17: [18, inf] | aziz 's iraqi | Tariq_Aziz |
| 285. | theft | 17: [14, inf] | theft 's former | Theft |
| 286. | opening | 17: [10, inf] | opening 's iraq | Iraq |
| 287. | scientist | 17: [10, inf] | scientist iraq 's | Iran–Iraq_War |
| 288. | percent | 17: [13, 13.0], 29: [12, 6.0], 32: [11, inf], 49: [12, 6.0] | percent 's government | Federal_government_of_the_United_States |
| 289. | fraud | 17: [25, inf] | fraud 's charges | Fraud |
| 290. | schools | 17: [15, 7.5], 21: [12, 12.0], 46: [12, inf] | schools 's children | Children's_literature |
| 291. | mandela | 17: [10, inf] | mandela south africa | Nelson_Mandela |
| 292. | visit | 17: [12, inf], 47: [25, 5.0] | visit 's bush | George_W._Bush |
| 293. | birthday | 18: [10, inf], 37: [11, inf] | birthday 's north | Washington's_Birthday |
| 294. | steps | 18: [10, inf], 33: [11, 11.0] | steps 's israel | Israel |
| 295. | vajpayee | 18: [11, inf] | vajpayee india prime | List_of_prime_ministers_of_India |
| 296. | bar | 18: [10, inf] | bar 's plan | Bar_Bar_Bar |
| 297. | italy | 18: [13, inf], 40: [14, 7.0], 43: [24, 6.0] | italy europe world | Italy |
| 298. | common | 18: [12, inf] | common 's iraq | Iraq_War |
| 299. | newspaper | 18: [11, inf], 38: [18, 9.0] | newspaper 's world | List_of_newspapers_by_circulation |
| 300. | transition | 18: [10, inf] | transition 's iraq | Iraqi_Transitional_Government |
| 301. | falluja | 18: [10, inf] | falluja american iraq | Fallujah |
| 302. | tel | 18: [12, inf] | tel aviv israeli | Tel_Aviv |
| 303. | aviv | 18: [12, inf] | aviv tel israeli | Tel_Aviv |
| 304. | rules | 18: [10, inf] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 305. | relapses | 18: [10, inf] | relapses patients sars | Gilteritinib |
| 306. | earthquake | 18: [13, inf] | earthquake people least | 2011_Sikkim_earthquake |
| 307. | u.n. | 19: [13, inf], 34: [26, 8.67], 42: [12, 6.0] | u.n. iraq united | 2003_invasion_of_Iraq |
| 308. | shortages | 19: [13, inf], 33: [13, 13.0] | shortages iraq 's | Iran–Iraq_War |
| 309. | envoy | 19: [15, 5.0], 21: [10, inf], 47: [12, 12.0] | envoy 's iraq | Brett_McGurk |
| 310. | finds | 19: [10, 10.0], 39: [11, inf], 44: [10, inf] | finds 's iraq | 2003_invasion_of_Iraq |
| 311. | resolution | 19: [21, 7.0], 31: [18, inf] | resolution iraq council | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 312. | armitage | 19: [11, inf] | armitage state bush | Richard_Armitage_(government_official) |
| 313. | fund | 19: [11, inf], 29: [10, 10.0] | fund 's iraq | Development_Fund_for_Iraq |
| 314. | youths | 19: [10, inf] | youths programs israeli | Gadna_(Israel) |
| 315. | khatami | 20: [11, inf] | khatami iran 's | Mohammad_Khatami |
| 316. | arrives | 20: [11, inf] | arrives iraq 's | 2003_invasion_of_Iraq |
| 317. | truck | 20: [12, 6.0], 34: [10, inf] | truck iraq 's | Gun_truck |
| 318. | riyadh | 20: [29, inf] | riyadh saudi arabia | Riyadh |
| 319. | membership | 20: [11, inf] | membership european 's | 2016_United_Kingdom_European_Union_membership_referendum |
| 320. | republic | 20: [18, 9.0], 24: [13, inf] | republic 's czech | Czech_Republic |
| 321. | go | 20: [11, inf] | go 's iraq | Iraq_War |
| 322. | arabs | 20: [11, inf], 45: [10, 5.0] | arabs 's iraq | Iraqis |
| 323. | menem | 20: [12, inf] | menem 's argentine | Carlos_Menem |
| 324. | bali | 20: [12, inf], 32: [14, inf] | bali indonesia islamic | Bali |
| 325. | race | 20: [11, inf] | race 's party | Republican_Party_(United_States) |
| 326. | raid | 20: [10, 10.0], 26: [10, 10.0], 50: [10, inf] | raid israeli 's | Raid_on_Entebbe_(film) |
| 327. | bomber | 20: [12, inf] | bomber suicide israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 328. | reportedly | 21: [19, 6.33], 35: [11, inf] | reportedly 's iraq | 2003_invasion_of_Iraq |
| 329. | sharply | 21: [11, inf] | sharply 's iraq | Iraq_and_weapons_of_mass_destruction |
| 330. | ban | 21: [20, 10.0], 26: [10, 10.0], 45: [10, inf] | ban 's world | Ban_Ki-moon |
| 331. | lawyers | 21: [12, inf] | lawyers 's court | Lawyer |
| 332. | companies | 21: [10, 5.0], 24: [10, inf], 26: [12, 12.0], 40: [13, inf], 49: [10, 10.0] | companies iraq 's | Iraq_Petroleum_Company |
| 333. | mad | 21: [18, inf] | mad cow disease | Bovine_spongiform_encephalopathy |
| 334. | cow | 21: [38, inf] | cow mad disease | Bovine_spongiform_encephalopathy |
| 335. | beef | 21: [14, inf] | beef cow canadian | Beef_cattle |
| 336. | afghanistan | 21: [18, 18.0], 27: [11, inf], 35: [25, 6.25] | afghanistan taliban 's | Islamic_Emirate_of_Afghanistan |
| 337. | ranch | 21: [11, inf] | ranch bush cow | Cowboy |
| 338. | technology | 21: [11, inf] | technology 's nuclear | Nuclear_technology |
| 339. | expert | 21: [10, 10.0], 29: [14, inf] | expert 's weapons | David_Kelly_(weapons_expert) |
| 340. | pole | 21: [10, inf] | pole north 's | North_Pole |
| 341. | liquor | 21: [10, inf] | liquor iraq 's | Gang_presence_in_the_United_States_military |
| 342. | costa | 21: [11, inf] | costa programs academy | Academy_at_Dundee_Ranch |
| 343. | academy | 21: [15, inf] | academy american costa | Costa-Gavras |
| 344. | send | 22: [15, 5.0], 34: [17, inf] | send iraq troops | American-led_intervention_in_Iraq_(2014–present) |
| 345. | climbers | 22: [11, inf] | climbers everest may | List_of_people_who_died_climbing_Mount_Everest |
| 346. | sherpa | 22: [10, inf] | sherpa climbers katmandu | 1953_British_Mount_Everest_expedition |
| 347. | poland | 22: [19, inf], 51: [14, 7.0] | poland 's europe | Poland_in_the_European_Union |
| 348. | arrests | 22: [11, inf], 26: [15, 7.5] | arrests police 's | Arrest |
| 349. | panel | 22: [10, inf], 28: [10, inf], 43: [13, inf] | panel iraq 's | 2003_invasion_of_Iraq |
| 350. | colombia | 22: [12, inf], 38: [19, inf] | colombia 's rebels | Revolutionary_Armed_Forces_of_Colombia |
| 351. | south | 22: [16, inf] | south korea north | North_Korea–South_Korea_relations |
| 352. | mass | 22: [14, inf] | mass iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 353. | destruction | 22: [12, inf] | destruction iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 354. | geneva | 22: [14, 14.0], 49: [12, inf] | geneva iraq would | Geneva_Conventions |
| 355. | sake | 22: [12, inf] | sake 's us | Sake |
| 356. | main | 23: [10, inf] | main 's iraq | 2003_invasion_of_Iraq |
| 357. | statements | 23: [11, inf] | statements 's korea | South_Korea |
| 358. | zone | 23: [10, inf], 29: [11, inf] | zone iraq 's | Saudi_Arabian–Iraqi_neutral_zone |
| 359. | jerusalem | 23: [14, 14.0], 34: [15, inf] | jerusalem palestinian israeli | East_Jerusalem |
| 360. | joining | 24: [12, inf] | joining 's union | Soviet_Union |
| 361. | faces | 24: [10, inf] | faces 's iraq | Iran–Iraq_War |
| 362. | chief | 24: [12, 6.0], 34: [13, inf] | chief 's iraq | Iraq_War |
| 363. | art | 24: [12, inf] | art 's museum | Museum_of_Modern_Art |
| 364. | ships | 24: [10, inf] | ships 's north | List_of_active_ships_of_the_Korean_People's_Navy |
| 365. | land | 24: [14, inf] | land 's iraq | Iraq |
| 366. | marriage | 24: [10, inf], 31: [18, inf] | marriage gay same-sex | Same-sex_marriage |
| 367. | areas | 24: [13, inf] | areas 's palestinian | West_Bank_Areas_in_the_Oslo_II_Accord |
| 368. | czech | 24: [15, inf] | czech republic europe | Czech_Republic |
| 369. | prisoner | 24: [12, inf] | prisoner prisoners israel | Palestinian_prisoners_of_Israel |
| 370. | senate | 25: [10, inf], 40: [13, 6.5], 42: [10, inf] | senate iraq 's | Senate_of_Iraq |
| 371. | rejects | 25: [10, inf], 37: [10, 5.0] | rejects 's iraq | Iraq_War |
| 372. | cease-fire | 25: [18, 6.0], 47: [10, inf] | cease-fire palestinian 's | Israeli–Palestinian_conflict |
| 373. | basque | 25: [16, inf] | basque spain spanish | Basque_Country_(autonomous_community) |
| 374. | evidence | 26: [19, 6.33], 50: [12, inf] | evidence iraq 's | Iraq_War |
| 375. | syrian | 26: [14, inf], 29: [15, 5.0], 41: [13, inf] | syrian syria iraq | Ba'ath_Party_(Syrian-dominated_faction) |
| 376. | liberia | 26: [14, inf], 47: [12, inf] | liberia taylor 's | Charles_Taylor_(Liberian_politician) |
| 377. | charles | 26: [11, inf] | charles taylor liberia | Charles_Taylor_(Liberian_politician) |
| 378. | taylor | 26: [13, inf] | taylor liberia pres | Charles_Taylor_(Liberian_politician) |
| 379. | musharraf | 26: [14, inf] | musharraf pakistan 's | Pervez_Musharraf |
| 380. | mosque | 27: [32, inf] | mosque 's shiite | Ar-Rahman_Mosque_(Pyongyang) |
| 381. | internal | 27: [15, inf] | internal 's security | Internal_security |
| 382. | spokesman | 28: [11, inf] | spokesman 's says | The_Spokesman-Review |
| 383. | congress | 28: [13, 13.0], 39: [10, 5.0], 49: [12, inf] | congress iraq 's | Iraqi_National_Congress |
| 384. | electric | 28: [10, inf] | electric power iraq | List_of_power_stations_in_Iraq |
| 385. | interim | 28: [12, inf] | interim iraq iraqi | Iraq_War |
| 386. | agreed | 28: [14, inf] | agreed iraq 's | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 387. | allied | 28: [11, 5.5], 49: [11, inf] | allied iraq forces | Iraqi_Armed_Forces |
| 388. | twins | 28: [11, inf] | twins father 's | Twin |
| 389. | mbeki | 28: [11, inf] | mbeki south pres | Thabo_Mbeki |
| 390. | uranium | 28: [24, inf] | uranium nuclear iraq | Niger_uranium_forgeries |
| 391. | body | 28: [10, inf], 33: [11, inf] | body 's iraq | Iraq_Body_Count_project |
| 392. | buy | 28: [10, inf] | buy 's iraq | Iran–Iraq_War |
| 393. | immigrants | 28: [10, inf], 43: [11, inf] | immigrants 's italy | Italian_diaspora |
| 394. | dispute | 29: [15, inf] | dispute 's iraq | Disputed_territories_of_Northern_Iraq |
| 395. | drought | 29: [10, inf] | drought 's aid | Drought |
| 396. | singapore | 29: [11, 5.5], 37: [14, inf] | singapore sars 's | 2002–2004_SARS_outbreak |
| 397. | missions | 30: [10, inf] | missions iraq forces | Multi-National_Force_–_Iraq |
| 398. | sandwich | 30: [10, inf] | sandwich 's family | Cuban_sandwich |
| 399. | uday | 30: [19, inf] | uday hussein 's | Uday_Hussein |
| 400. | qusay | 30: [19, inf] | qusay hussein 's | Qusay_Hussein |
| 401. | spain | 30: [10, inf], 45: [14, inf], 48: [15, 5.0] | spain world 's | Spain_during_World_War_II |
| 402. | tourists | 30: [11, inf] | tourists 's world | The_Tourists |
| 403. | library | 30: [10, inf] | library books oil | Oil! |
| 404. | gay | 31: [20, inf] | gay marriage 's | Same-sex_marriage |
| 405. | village | 31: [10, 10.0], 39: [12, inf], 47: [10, 5.0] | village 's map | Map |
| 406. | rwanda | 31: [16, inf] | rwanda world briefing | Healthcare_in_Rwanda |
| 407. | prosecutor | 31: [14, inf] | prosecutor 's court | Prosecutor |
| 408. | marriages | 31: [10, inf] | marriages marriage gay | Same-sex_marriage |
| 409. | jakarta | 32: [16, inf] | jakarta indonesia indonesian | COVID-19_pandemic_in_Indonesia |
| 410. | cantat | 32: [10, inf] | cantat france french | Bertrand_Cantat |
| 411. | small | 32: [11, inf], 45: [10, inf] | small 's say | Never_Say_Never_Again |
| 412. | jordanian | 32: [11, inf] | jordanian iraqi 's | Arab_Federation |
| 413. | jemaah | 32: [11, inf] | jemaah group islamiyah | Jemaah_Islamiyah |
| 414. | islamiyah | 32: [11, inf] | islamiyah group jemaah | Jemaah_Islamiyah |
| 415. | mr. | 32: [14, inf] | mr. 's president | Mr._President_(title) |
| 416. | canadian | 32: [10, inf], 40: [10, 5.0], 45: [11, inf] | canadian canada 's | Canadians |
| 417. | led | 33: [11, inf] | led 's iraq | American-led_intervention_in_Iraq_(2014–present) |
| 418. | proposal | 33: [10, inf] | proposal iraq 's | Proposals_for_Assyrian_autonomy_in_Iraq |
| 419. | incident | 33: [10, inf] | incident 's american | 1954_United_States_Capitol_shooting |
| 420. | israelis | 33: [17, 5.67], 49: [12, inf] | israelis palestinian israeli | Israeli–Palestinian_conflict |
| 421. | blow | 33: [10, inf] | blow 's iraq | Iran–Iraq_War |
| 422. | libya | 33: [25, inf], 51: [26, inf] | libya sanctions 's | Iran_and_Libya_Sanctions_Act |
| 423. | lockerbie | 33: [11, inf] | lockerbie libya sanctions | Pan_Am_Flight_103 |
| 424. | bbc | 33: [16, inf] | bbc 's blair | Lionel_Blair |
| 425. | action | 34: [12, inf] | action iraq 's | 2003_invasion_of_Iraq |
| 426. | questions | 34: [11, inf] | questions 's iraq | Iraq_War |
| 427. | cards | 34: [10, inf] | cards 's fake | Steam_Trading_Cards |
| 428. | head | 34: [12, inf] | head 's iraq | Iraq_War |
| 429. | soft | 34: [10, inf] | soft 's korean | Soft_power |
| 430. | charities | 34: [11, inf] | charities hamas 's | List_of_charities_accused_of_ties_to_terrorism |
| 431. | iran | 35: [25, 5.0], 50: [15, inf] | iran 's iraq | Iran–Iraq_War |
| 432. | bombs | 35: [11, inf] | bombs 's american | U.S._Bombs |
| 433. | al-hakim | 35: [10, inf] | al-hakim iraq shiite | Mohammad_Baqir_al-Hakim |
| 434. | shiite | 35: [20, 5.0], 41: [16, inf] | shiite iraq 's | Faisal_I_of_Iraq |
| 435. | holy | 35: [15, inf] | holy 's iraq | Iran–Iraq_War |
| 436. | lindbergh | 35: [12, inf] | lindbergh family bouteuil | Charles_Lindbergh |
| 437. | bakr | 35: [10, inf] | bakr iraq 's | Abu_Bakr_al-Baghdadi |
| 438. | submarine | 35: [10, inf] | submarine accident china | Chinese_submarine_361 |
| 439. | interview | 36: [10, inf], 38: [18, inf], 49: [10, 5.0] | interview 's says | The_Interview |
| 440. | chinese | 36: [15, inf], 38: [22, 11.0] | chinese china 's | China |
| 441. | chocolate | 36: [10, inf] | chocolate cocoa paris | Chocolate |
| 442. | qurei | 37: [23, inf] | qurei palestinian arafat | Ahmed_Qurei |
| 443. | developing | 37: [15, inf] | developing 's world | Developed_country |
| 444. | democrats | 37: [11, 11.0], 44: [10, inf] | democrats 's bush | Blue_Dog_Coalition |
| 445. | subsidies | 37: [25, inf] | subsidies trade world | Subsidy |
| 446. | swedish | 37: [10, inf] | swedish lindh foreign | Anna_Lindh |
| 447. | anna | 37: [10, inf] | anna lindh european | Anna_Lindh |
| 448. | lindh | 37: [13, inf] | lindh swedish foreign | Anna_Lindh |
| 449. | asylum | 37: [12, inf] | asylum britain world | Right_of_asylum |
| 450. | tibet | 38: [12, inf] | tibet chinese china | Annexation_of_Tibet_by_the_People's_Republic_of_China |
| 451. | tibetans | 38: [10, inf] | tibetans chinese tibet | Tibet_Autonomous_Region |
| 452. | making | 38: [10, inf] | making 's iraq | Iraq_War |
| 453. | increasingly | 38: [10, inf] | increasingly 's iraq | 2003_invasion_of_Iraq |
| 454. | robert | 38: [10, inf] | robert zimbabwe 's | Zimbabwe |
| 455. | jacques | 38: [10, inf] | jacques chirac france | Jacques_Chirac |
| 456. | big | 38: [11, inf] | big 's iraq | Iraq |
| 457. | allowed | 38: [10, inf] | allowed 's iraq | Iraq |
| 458. | divorce | 38: [12, inf] | divorce italy 's | Divorce_Italian_Style |
| 459. | compound | 39: [12, inf] | compound iraqi iraq | Iraq_War |
| 460. | bremer | 39: [17, inf], 46: [13, 6.5] | bremer iraq american | Paul_Bremer |
| 461. | aids | 39: [11, inf], 46: [24, 24.0] | aids africa bush | Barbara_Bush_(born_1981) |
| 462. | reserve | 39: [11, inf] | reserve iraq pentagon | Pentagon_Papers |
| 463. | leak | 40: [14, inf] | leak 's bush | LiveLeak |
| 464. | defectors | 40: [12, inf] | defectors north iraq | Islamic_State_of_Iraq_and_the_Levant |
| 465. | cardinal | 40: [13, inf] | cardinal pope 's | Pope_Francis |
| 466. | / | 41: [11, inf] | / 's attacks | Denial-of-service_attack |
| 467. | southeast | 41: [11, inf] | southeast 's asia | Southeast_Asia |
| 468. | harbor | 41: [12, inf] | harbor bush 's | The_New_Pearl_Harbor |
| 469. | nobel | 41: [16, inf] | nobel prize 's | Nobel_Prize_in_Literature |
| 470. | prize | 41: [17, inf] | prize 's nobel | Nobel_Prize |
| 471. | turkish | 41: [14, inf], 47: [21, 7.0] | turkish turkey iraq | Iraq–Turkey_relations |
| 472. | car | 41: [12, inf], 50: [16, 16.0] | car killed attack | Charlottesville_car_attack |
| 473. | portugal | 41: [11, inf] | portugal 's european | Portugal |
| 474. | models | 41: [10, inf] | models 's fashion | List_of_Victoria's_Secret_models |
| 475. | ebadi | 41: [11, inf] | ebadi rights prize | Shirin_Ebadi |
| 476. | protesters | 42: [11, inf], 46: [11, inf] | protesters 's iraq | Protests_against_the_Iraq_War |
| 477. | bolivia | 42: [20, inf] | bolivia 's sanchez | Gonzalo_Sánchez_de_Lozada |
| 478. | gonzalo | 42: [11, inf] | gonzalo bolivia sanchez | Gonzalo_Sánchez_de_Lozada |
| 479. | sanchez | 42: [16, inf] | sanchez 's iraq | Ricardo_Sanchez |
| 480. | nation | 42: [10, inf] | nation 's iraq | Sanctions_against_Iraq |
| 481. | lozada | 42: [14, inf] | lozada 's bolivia | Gonzalo_Sánchez_de_Lozada |
| 482. | welfare | 42: [12, inf] | welfare 's bush | George_W._Bush |
| 483. | mother | 42: [10, inf] | mother 's family | Mother's_Day |
| 484. | teresa | 42: [10, inf] | teresa mother pope | Mother_Teresa |
| 485. | sudan | 43: [15, inf] | sudan peace africa | Israel–Sudan_normalization_agreement |
| 486. | killings | 43: [10, inf] | killings 's two | ReMastered:_The_Two_Killings_of_Sam_Cooke |
| 487. | workers | 43: [11, inf] | workers 's government | Workers'_compensation |
| 488. | conservative | 44: [12, inf] | conservative 's party | Conservative_Party_(UK) |
| 489. | conservatives | 44: [11, inf] | conservatives 's iraq | Conservatism_in_the_United_States |
| 490. | iain | 44: [10, inf] | iain leader duncan | Iain_Duncan_Smith |
| 491. | duncan | 44: [15, inf] | duncan leader smith | Iain_Duncan_Smith |
| 492. | smith | 44: [15, inf] | smith leader duncan | Iain_Duncan_Smith |
| 493. | tories | 44: [10, inf] | tories party britain | Tories_(British_political_party) |
| 494. | leadership | 44: [10, inf] | leadership 's iraq | Iran–Iraq_War |
| 495. | secret | 44: [10, inf], 51: [10, inf] | secret 's iraq | Iraq_and_weapons_of_mass_destruction |
| 496. | suspends | 44: [10, inf] | suspends world briefing | Stephanie_Grisham |
| 497. | sent | 44: [11, inf] | sent 's iraq | 2003_invasion_of_Iraq |
| 498. | stock | 44: [12, inf] | stock 's us | List_of_stock_exchanges |
| 499. | sunday | 45: [10, inf] | sunday iraq 's | Iraq_War |
| 500. | cloning | 45: [12, inf] | cloning human ban | Human_cloning |
| 501. | greater | 45: [10, inf] | greater 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 502. | plant | 46: [10, inf], 50: [14, inf] | plant nuclear 's | Chernobyl_Nuclear_Power_Plant |
| 503. | generals | 46: [10, inf] | generals american 's | List_of_active_duty_United_States_four-star_officers |
| 504. | coming | 46: [12, inf] | coming 's iraq | 2003_invasion_of_Iraq |
| 505. | meets | 46: [12, inf] | meets iraq 's | Iraq_War |
| 506. | strategy | 46: [15, inf] | strategy iraq 's | U.S._kill_or_capture_strategy_in_Iraq |
| 507. | insurgency | 46: [11, inf] | insurgency american 's | Insurgency |
| 508. | elf | 46: [10, inf] | elf oil former | Elf_Aquitaine |
| 509. | botswana | 46: [10, inf] | botswana africa aids | HIV/AIDS_in_Botswana |
| 510. | church | 47: [11, inf] | church 's world | List_of_largest_church_buildings |
| 511. | aguilar | 47: [10, inf] | aguilar mexico envoy | Adolfo_Aguilar_Zínser |
| 512. | kifl | 47: [10, inf] | kifl village iraqi | Iraqi_revolt_of_1920 |
| 513. | thanksgiving | 48: [15, inf] | thanksgiving bush visit | List_of_international_presidential_trips_made_by_George_W._Bush |
| 514. | dinner | 48: [10, inf] | dinner bush iraq | Bush_shoeing_incident |
| 515. | clinton | 48: [12, inf] | clinton bush 's | Presidency_of_Bill_Clinton |
| 516. | samarra | 49: [10, inf] | samarra american says | Samarra |
| 517. | civilians | 49: [13, 6.5], 52: [10, inf] | civilians iraqi american | Casualties_of_the_Iraq_War |
| 518. | influence | 49: [10, inf] | influence 's iraq | Iraq |
| 519. | details | 49: [11, inf] | details 's iraq | Iraq |
| 520. | withdraw | 49: [11, inf] | withdraw 's iraq | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 521. | jews | 49: [14, inf] | jews 's israel | Israeli_Jews |
| 522. | ministers | 49: [10, inf] | ministers 's iraq | Prime_Minister_of_Iraq |
| 523. | media | 49: [13, inf] | media 's news | News_media |
| 524. | veto | 49: [10, inf] | veto iraq resolution | War_Powers_Resolution |
| 525. | nuclear | 50: [15, inf] | nuclear north korea | North_Korea_and_weapons_of_mass_destruction |
| 526. | contracts | 50: [20, inf] | contracts iraq companies | Private_military_company |
| 527. | wall | 50: [13, inf] | wall 's says | Trump_wall |
| 528. | judge | 50: [11, inf] | judge 's court | United_States_district_court |
| 529. | halliburton | 50: [20, inf] | halliburton iraq 's | Halliburton |
| 530. | impact | 51: [10, inf] | impact 's iraq | Impact_of_the_COVID-19_pandemic |
| 531. | impose | 51: [10, inf] | impose north would | Gun_laws_in_North_Carolina |
| 532. | inquest | 51: [10, inf] | inquest diana death | Death_of_Diana,_Princess_of_Wales |
| 533. | immigration | 52: [10, inf] | immigration 's states | Immigration_to_the_United_States |
| 534. | toll | 52: [11, inf] | toll 's death | List_of_wars_and_anthropogenic_disasters_by_death_toll |
| 535. | vote | 24: [28, 28.0], 44: [21, 7.0] | vote 's iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 536. | strikes | 12: [27, 27.0] | strikes iraq 's | Assassination_of_Qasem_Soleimani |
| 537. | bomb | 19: [21, 10.5], 24: [11, 5.5], 39: [26, 26.0] | bomb 's baghdad | 2018_Baghdad_bombings |
| 538. | court | 44: [26, 26.0], 50: [39, 6.5] | court 's world | International_Court_of_Justice |
| 539. | treaty | 2: [25, 25.0], 21: [23, 11.5] | treaty nuclear north | Treaty_on_the_Non-Proliferation_of_Nuclear_Weapons |
| 540. | london | 2: [26, 13.0], 7: [25, 5.0], 18: [13, 6.5], 47: [24, 24.0] | london 's britain | London |
| 541. | djindjic | 11: [24, 24.0] | djindjic zoran serbia | Zoran_Đinđić |
| 542. | control | 12: [20, 6.67], 21: [24, 24.0], 33: [19, 19.0], 38: [10, 5.0] | control 's iraq | Occupation_of_Iraq_(2003–2011) |
| 543. | gas | 15: [14, 14.0], 19: [24, 24.0], 52: [11, 11.0] | gas 's iraq | Petroleum_industry_in_Iraq |
| 544. | saudis | 20: [24, 24.0] | saudis saudi arabia | King_of_Saudi_Arabia |
| 545. | summit | 22: [24, 24.0] | summit meeting 's | Summit_(meeting) |
| 546. | sharon | 2: [35, 17.5], 9: [23, 23.0], 19: [14, 7.0] | sharon israel palestinian | Ariel_Sharon |
| 547. | christmas | 52: [23, 23.0] | christmas 's attacks | Robot_Unicorn_Attack |
| 548. | forum | 4: [22, 22.0] | forum world economic | World_Economic_Forum |
| 549. | indian | 13: [12, 6.0], 26: [21, 21.0] | indian india 's | Economy_of_India |
| 550. | iranian | 8: [13, 6.5], 11: [17, 8.5], 16: [10, 5.0], 22: [20, 20.0], 25: [15, 7.5] | iranian iran 's | Demographics_of_Iran |
| 551. | coalition | 9: [20, 20.0], 12: [26, 13.0], 49: [11, 5.5] | coalition 's iraq | Multi-National_Force_–_Iraq |
| 552. | talks | 2: [45, 5.0], 15: [19, 19.0], 49: [28, 5.6] | talks north korea | North_Korea–South_Korea_relations |
| 553. | subway | 8: [19, 19.0] | subway fire people | Daegu_subway_fire |
| 554. | kirkuk | 15: [38, 19.0] | kirkuk iraq american | Kirkuk |
| 555. | iraqis | 8: [14, 7.0], 34: [18, 18.0] | iraqis iraq american | Iraqis |
| 556. | killing | 22: [30, 5.0], 30: [12, 6.0], 49: [18, 18.0] | killing 's israeli | List_of_Israeli_assassinations |
| 557. | terrorism | 5: [17, 17.0], 16: [11, 5.5], 26: [11, 11.0], 49: [11, 11.0] | terrorism 's bush | War_on_terror |
| 558. | falls | 15: [17, 17.0] | falls 's iraq | Iraq_War |
| 559. | economic | 16: [20, 10.0], 38: [17, 17.0] | economic 's north | Special_economic_zone |
| 560. | opposition | 2: [16, 16.0], 19: [34, 5.67] | opposition 's iraq | Opposition_to_the_Iraq_War |
| 561. | soldier | 6: [16, 16.0], 29: [10, 5.0] | soldier american killed | Soldier_(1998_American_film) |
| 562. | pentagon | 21: [16, 16.0], 49: [14, 7.0] | pentagon iraq 's | The_Pentagon |
| 563. | efforts | 28: [16, 16.0], 38: [11, 5.5] | efforts 's iraq | Iran–Iraq_War |
| 564. | office | 36: [16, 16.0] | office 's iraq | Iraq_War |
| 565. | b | 44: [16, 16.0] | b 's american | The_B-52's |
| 566. | meet | 49: [16, 16.0] | meet iraq 's | 2003_invasion_of_Iraq |
| 567. | davos | 4: [15, 15.0] | davos forum world | World_Economic_Forum |
| 568. | bombing | 7: [15, 15.0], 34: [69, 7.67], 39: [14, 14.0] | bombing 's iraq | 1998_bombing_of_Iraq |
| 569. | southern | 7: [15, 15.0] | southern iraq american | Iraqi_Americans |
| 570. | deaths | 12: [15, 15.0], 20: [10, 10.0], 30: [17, 8.5], 46: [11, 5.5], 49: [11, 11.0] | deaths 's iraq | Casualties_of_the_Iraq_War |
| 571. | miles | 12: [15, 15.0], 26: [14, 14.0] | miles 's american | American_Pie_Presents:_The_Naked_Mile |
| 572. | billion | 12: [16, 8.0], 26: [15, 15.0], 28: [19, 9.5], 49: [12, 12.0] | billion iraq 's | Iraq_War |
| 573. | rescue | 14: [15, 15.0] | rescue 's iraqi | Jessica_Lynch |
| 574. | press | 15: [21, 5.25], 39: [15, 15.0] | press 's iraq | 2003_invasion_of_Iraq |
| 575. | revenge | 15: [15, 15.0] | revenge american hussein | Execution_of_Saddam_Hussein |
| 576. | compounds | 20: [15, 15.0] | compounds saudi says | Riyadh_compound_bombings |
| 577. | air | 39: [15, 15.0] | air iraq american | Iraqi_Air_Force |
| 578. | found | 48: [15, 15.0] | found 's iraq | Iraq |
| 579. | largest | 49: [15, 15.0] | largest 's iraq | Demographics_of_Iraq |
| 580. | company | 2: [14, 14.0], 40: [12, 12.0] | company 's oil | Shell_Oil_Company |
| 581. | conflict | 3: [14, 14.0] | conflict 's iraq | Iraqi_conflict_(2003–present) |
| 582. | early | 3: [14, 14.0], 17: [11, 11.0] | early 's iraq | Iraq_War |
| 583. | parties | 3: [14, 14.0] | parties 's government | Political_parties_in_the_United_States |
| 584. | remarks | 6: [12, 6.0], 10: [28, 14.0], 43: [14, 7.0] | remarks 's bush | Barbara_Bush_(born_1981) |
| 585. | pressure | 9: [14, 14.0] | pressure 's iraq | Iraq_War |
| 586. | protest | 9: [14, 14.0], 21: [12, 6.0] | protest 's iraq | Protests_against_the_Iraq_War |
| 587. | strip | 10: [11, 11.0], 15: [10, 10.0], 47: [14, 14.0] | strip palestinian israeli | Palestinian_territories |
| 588. | center | 10: [14, 14.0] | center 's american | America's_Center |
| 589. | must | 12: [14, 7.0], 14: [11, 5.5], 51: [14, 14.0] | must 's iraq | Iraq |
| 590. | earlier | 12: [14, 14.0] | earlier 's iraq | Iraq |
| 591. | defends | 14: [14, 14.0] | defends iraq 's | Iraq_War |
| 592. | april | 14: [14, 14.0] | april 's iraq | 2003_invasion_of_Iraq |
| 593. | school | 15: [23, 11.5], 18: [14, 14.0], 50: [10, 5.0] | school 's children | Professional_Children's_School |
| 594. | criminal | 19: [11, 5.5], 40: [14, 14.0] | criminal 's court | International_Criminal_Court |
| 595. | seized | 19: [14, 14.0] | seized 's says | Silk_Road_(marketplace) |
| 596. | indictment | 20: [14, 14.0] | indictment qaeda united | FBI_Most_Wanted_Terrorists |
| 597. | wolfowitz | 29: [14, 14.0] | wolfowitz iraq defense | Paul_Wolfowitz |
| 598. | bombers | 47: [14, 14.0] | bombers suicide 's | Female_suicide_bomber |
| 599. | clark | 51: [27, 13.5] | clark milosevic former | Slobodan_Milošević |
| 600. | agree | 2: [11, 5.5], 31: [13, 13.0] | agree iraq 's | Iraq |
| 601. | call | 2: [13, 13.0], 49: [11, 11.0] | call 's iraq | Iraq |
| 602. | trying | 3: [13, 13.0], 43: [12, 12.0] | trying 's iraq | Iraq_War |
| 603. | top | 3: [10, 5.0], 51: [13, 13.0] | top 's iraq | Iraq_War |
| 604. | leading | 3: [10, 10.0], 20: [13, 13.0], 29: [10, 10.0] | leading 's iraq | Iraq_War |
| 605. | wounded | 3: [13, 13.0], 13: [19, 9.5] | wounded killed american | List_of_United_States_Congress_members_killed_or_wounded_in_office |
| 606. | sentenced | 5: [13, 13.0] | sentenced years prison | List_of_longest_prison_sentences |
| 607. | hundreds | 5: [11, 11.0], 22: [10, 10.0], 24: [13, 13.0] | hundreds 's iraq | Iraq_War |
| 608. | going | 5: [13, 13.0] | going iraq 's | Iraq_War |
| 609. | fox | 11: [13, 13.0] | fox mexico 's | Vicente_Fox |
| 610. | reported | 12: [13, 13.0] | reported 's sars | 2002–2004_SARS_outbreak |
| 611. | cross | 12: [13, 13.0] | cross 's iraq | Iraq_War |
| 612. | plane | 13: [13, 13.0] | plane american united | United_States |
| 613. | muslim | 14: [13, 13.0], 19: [18, 6.0], 27: [10, 10.0] | muslim 's iraq | Islam_in_Iraq |
| 614. | mosul | 15: [26, 5.2], 19: [13, 13.0], 30: [15, 7.5] | mosul iraq american | Mosul |
| 615. | area | 22: [13, 13.0], 24: [13, 13.0] | area 's iraq | 2003_invasion_of_Iraq |
| 616. | yet | 26: [13, 13.0] | yet 's iraq | Iraq |
| 617. | bodies | 30: [13, 13.0] | bodies 's american | Young_American_Bodies |
| 618. | moscow | 31: [13, 13.0] | moscow 's russia | Moscow |
| 619. | thousands | 32: [10, 5.0], 52: [13, 13.0] | thousands 's iraq | Iraq_War |
| 620. | general | 41: [11, 11.0], 50: [13, 13.0] | general 's iraq | Iraq_War |
| 621. | plans | 49: [13, 13.0] | plans 's iraq | 2003_invasion_of_Iraq |
| 622. | money | 49: [13, 13.0] | money 's iraq | Iraqi_dinar |
| 623. | democratic | 50: [13, 13.0] | democratic 's iraq | Kurdistan_Democratic_Party |
| 624. | northern | 1: [13, 13.0] | northern iraq 's | Iraqi_Kurdistan |
| 625. | russia | 31: [25, 12.5], 33: [21, 5.25], 49: [26, 5.2] | russia 's iraq | Iraq–Russia_relations |
| 626. | istanbul | 47: [25, 12.5] | istanbul 's turkish | Istanbul |
| 627. | ultimatum | 12: [37, 12.33] | ultimatum bush hussein | George_W._Bush |
| 628. | suspect | 2: [11, 5.5], 21: [12, 12.0] | suspect 's say | The_Usual_Suspects |
| 629. | seoul | 3: [12, 12.0] | seoul north korea | Seoul |
| 630. | four | 3: [24, 12.0], 40: [12, 12.0] | four 's american | List_of_active_duty_United_States_four-star_officers |
| 631. | fighting | 3: [11, 5.5], 30: [12, 12.0] | fighting 's american | Fighting_American |
| 632. | others | 3: [12, 12.0], 39: [15, 5.0], 50: [13, 6.5] | others 's iraq | War_in_Iraq_(2013–2017) |
| 633. | muslims | 3: [12, 12.0], 5: [12, 6.0] | muslims 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 634. | financial | 4: [12, 12.0] | financial 's iraq | Financial_cost_of_the_Iraq_War |
| 635. | shut | 4: [12, 12.0] | shut 's oil | Shut-in_(oil_drilling) |
| 636. | diplomacy | 4: [12, 12.0] | diplomacy 's bush | George_H._W._Bush |
| 637. | commercial | 5: [12, 12.0] | commercial 's says | Say's_law |
| 638. | appeal | 5: [12, 12.0] | appeal 's world | United_States_courts_of_appeals |
| 639. | conviction | 5: [12, 12.0] | conviction 's court | Conviction |
| 640. | social | 6: [12, 12.0] | social 's government | Social_Security_number |
| 641. | dissident | 7: [12, 12.0] | dissident 's government | The_Dissident |
| 642. | problems | 8: [11, 11.0], 12: [12, 12.0] | problems 's iraq | Iraq |
| 643. | begins | 9: [12, 12.0] | begins 's iraq | Iraq |
| 644. | strong | 10: [12, 12.0], 29: [11, 11.0] | strong 's iraq | Iraq_War |
| 645. | argentina | 10: [12, 12.0], 33: [13, 6.5] | argentina 's world | Argentina_at_the_FIFA_World_Cup |
| 646. | zoran | 11: [12, 12.0] | zoran djindjic serbia | Zoran_Đinđić |
| 647. | beginning | 12: [12, 12.0] | beginning iraq 's | Iraq_War |
| 648. | allow | 12: [12, 12.0], 25: [16, 5.33], 51: [11, 5.5] | allow iraq 's | 2003_invasion_of_Iraq |
| 649. | began | 12: [12, 12.0] | began 's iraq | Iraq_War |
| 650. | field | 13: [12, 12.0] | field 's iraq | Iraq |
| 651. | jihad | 14: [12, 12.0] | jihad palestinian israel | Islamic_Jihad_Movement_in_Palestine |
| 652. | prisoners | 16: [19, 6.33], 30: [10, 10.0], 38: [12, 12.0] | prisoners palestinian israel | Palestinian_prisoners_of_Israel |
| 653. | collapse | 17: [12, 12.0] | collapse 's iraq | Iraq_War |
| 654. | confirmed | 17: [12, 12.0] | confirmed sars cases | 2002–2004_SARS_outbreak |
| 655. | offer | 18: [12, 12.0] | offer 's iraq | 2003_invasion_of_Iraq |
| 656. | along | 18: [12, 12.0] | along 's iraq | 2003_invasion_of_Iraq |
| 657. | soon | 19: [12, 12.0] | soon iraq 's | 2003_invasion_of_Iraq |
| 658. | step | 19: [12, 12.0] | step 's iraq | Iraq |
| 659. | vladimir | 20: [12, 12.0], 22: [10, 5.0], 44: [14, 7.0], 49: [10, 5.0] | vladimir putin russia | Russia_under_Vladimir_Putin |
| 660. | stop | 20: [12, 12.0], 26: [15, 5.0] | stop 's palestinian | Israeli–Palestinian_conflict |
| 661. | parliament | 25: [19, 6.33], 36: [12, 6.0], 41: [12, 12.0], 49: [12, 12.0] | parliament 's iraq | Council_of_Representatives_of_Iraq |
| 662. | saying | 26: [12, 12.0] | saying 's iraq | 2003_invasion_of_Iraq |
| 663. | responsibility | 28: [12, 12.0], 33: [12, 6.0], 47: [15, 7.5] | responsibility 's says | Single-responsibility_principle |
| 664. | david | 29: [19, 9.5], 33: [12, 12.0] | david 's iraq | Iraq_War |
| 665. | join | 33: [12, 12.0] | join 's iraq | Iraq |
| 666. | debate | 39: [12, 12.0] | debate 's iraq | Iraq |
| 667. | copter | 45: [12, 12.0] | copter helicopter iraq | Attack_helicopter |
| 668. | ground | 12: [35, 11.67] | ground iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 669. | peace | 2: [12, 6.0], 9: [46, 11.5] | peace 's palestinian | Israeli–Palestinian_peace_process |
| 670. | water | 22: [23, 11.5] | water 's iraq | Iraq |
| 671. | countries | 49: [23, 11.5] | countries 's iraq | Iraq |
| 672. | member | 2: [11, 11.0] | member 's iraq | 2003_invasion_of_Iraq |
| 673. | preparing | 4: [11, 11.0] | preparing iraq 's | Iran–Iraq_War |
| 674. | shot | 4: [11, 11.0] | shot killed american | List_of_law_enforcement_officers_killed_in_the_line_of_duty_in_the_United_States |
| 675. | question | 4: [11, 11.0] | question 's iraq | Iraq_War |
| 676. | continues | 5: [11, 11.0] | continues 's iraq | Iraq |
| 677. | shuttle | 6: [11, 11.0] | shuttle space 's | Space_Shuttle |
| 678. | prevent | 8: [11, 11.0] | prevent iraq 's | Iran–Iraq_War |
| 679. | past | 8: [11, 11.0] | past 's iraq | Iraq |
| 680. | called | 10: [10, 5.0], 23: [11, 11.0] | called 's iraq | Iraq |
| 681. | acute | 12: [11, 11.0] | acute health sars | Severe_acute_respiratory_syndrome |
| 682. | syndrome | 12: [11, 11.0] | syndrome health respiratory | Severe_acute_respiratory_syndrome |
| 683. | warplanes | 12: [11, 11.0] | warplanes american 's | World_of_Warplanes |
| 684. | hit | 12: [11, 11.0], 47: [13, 6.5] | hit american 's | A_Hit_Is_a_Hit |
| 685. | kashmir | 13: [10, 5.0], 48: [11, 11.0] | kashmir india pakistan | Kashmir |
| 686. | gen | 13: [26, 5.2], 46: [22, 11.0] | gen iraq 's | David_Petraeus |
| 687. | whose | 14: [14, 7.0], 20: [11, 11.0] | whose 's iraq | Iraq |
| 688. | try | 14: [11, 11.0] | try 's iraq | Iraq_War |
| 689. | deadly | 14: [11, 11.0], 18: [10, 5.0] | deadly 's american | The_Deadly_Companions |
| 690. | becomes | 16: [11, 11.0] | becomes 's iraq | Iraq |
| 691. | response | 17: [11, 11.0] | response 's iraq | Iraq_War |
| 692. | aircraft | 18: [11, 11.0] | aircraft iraq 's | Iraqi_Air_Force |
| 693. | changes | 19: [11, 11.0] | changes 's government | Federal_government_of_the_United_States |
| 694. | ambassador | 20: [11, 11.0] | ambassador 's iraq | List_of_ambassadors_of_the_United_States_to_Iraq |
| 695. | raises | 21: [11, 11.0] | raises 's iraq | Iraq_War |
| 696. | toronto | 22: [22, 11.0], 24: [10, 10.0] | toronto sars health | 2002–2004_SARS_outbreak |
| 697. | protests | 24: [10, 5.0], 46: [11, 11.0] | protests 's iraq | Protests_against_the_Iraq_War |
| 698. | argentine | 26: [11, 11.0] | argentine argentina 's | Argentina |
| 699. | july | 28: [11, 11.0] | july 's says | Say's_law |
| 700. | tribunals | 29: [11, 11.0] | tribunals military british | Military_tribunals_in_the_United_States |
| 701. | separate | 30: [11, 11.0] | separate 's palestinian | Palestinians |
| 702. | peru | 35: [11, 11.0] | peru 's fujimori | Alberto_Fujimori |
| 703. | near | 36: [20, 10.0], 47: [11, 11.0] | near 's american | Near-Earth_object |
| 704. | kosovo | 41: [11, 11.0] | kosovo 's serbia | Kosovo–Serbia_relations |
| 705. | islam | 43: [11, 11.0] | islam 's islamic | Islamic_fundamentalism |
| 706. | away | 43: [11, 11.0] | away 's iraq | Iraq_War |
| 707. | held | 43: [11, 11.0] | held 's world | Privately_held_company |
| 708. | continue | 47: [11, 11.0] | continue 's iraq | Iraq_War |
| 709. | debt | 51: [22, 11.0] | debt iraq 's | History_of_the_United_States_public_debt |
| 710. | defense | 12: [32, 10.67] | defense iraq 's | Iraq_War |
| 711. | khalid | 10: [21, 10.5] | khalid qaeda 's | Khalid_Sheikh_Mohammed |
| 712. | hold | 15: [21, 10.5] | hold 's iraq | Iraq |
| 713. | paul | 39: [21, 10.5] | paul iraq 's | Iraq_War |
| 714. | gaza | 10: [31, 10.33], 15: [18, 6.0], 47: [16, 5.33] | gaza palestinian israeli | Gaza–Israel_conflict |
| 715. | statement | 7: [10, 10.0], 10: [41, 10.25] | statement 's iraq | Iraqi_insurgency_(2003–2011) |
| 716. | price | 2: [10, 10.0] | price 's iraq | 1990_oil_price_shock |
| 717. | approach | 2: [10, 10.0] | approach 's iraq | Iraq |
| 718. | americas | 2: [10, 10.0], 11: [18, 9.0], 38: [13, 6.5] | americas world briefing | 1211_Avenue_of_the_Americas |
| 719. | second | 2: [10, 10.0], 29: [11, 5.5], 51: [14, 7.0] | second 's iraq | Second_Battle_of_Fallujah |
| 720. | greek | 2: [10, 10.0] | greek 's greece | Ancient_Greece |
| 721. | rejected | 3: [10, 10.0] | rejected iraq 's | Iraq_War |
| 722. | cooperation | 4: [13, 6.5], 9: [10, 10.0] | cooperation 's iraq | Iraq_and_weapons_of_mass_destruction |
| 723. | americans | 4: [10, 10.0], 7: [19, 6.33], 26: [10, 5.0], 42: [15, 5.0] | americans american iraq | Iraqi_Americans |
| 724. | prominent | 5: [10, 10.0] | prominent 's iraqi | 2003_invasion_of_Iraq |
| 725. | planes | 5: [10, 10.0] | planes iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 726. | fear | 6: [12, 6.0], 18: [10, 10.0] | fear 's iraq | Iran–Iraq_War |
| 727. | students | 8: [10, 10.0] | students 's government | Student_government_president |
| 728. | kill | 8: [10, 10.0] | kill israeli 's | List_of_Israeli_assassinations |
| 729. | radio | 10: [10, 10.0] | radio 's says | Say_Say_Say |
| 730. | kills | 10: [15, 7.5], 34: [11, 5.5], 47: [10, 10.0] | kills palestinian israeli | Timeline_of_the_Israeli–Palestinian_conflict |
| 731. | liberation | 10: [10, 10.0] | liberation 's palestinian | Palestinian_Liberation_Front |
| 732. | life | 11: [12, 6.0], 50: [10, 10.0] | life 's iraq | Iraq_War |
| 733. | get | 12: [10, 10.0] | get 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 734. | although | 12: [10, 10.0] | although 's iraq | Iraq |
| 735. | dozens | 13: [10, 10.0] | dozens 's american | The_Dozens |
| 736. | advance | 13: [16, 5.33], 17: [10, 10.0] | advance 's iraq | 2003_invasion_of_Iraq |
| 737. | supplies | 13: [20, 10.0] | supplies iraq 's | Iran–Iraq_War |
| 738. | kofi | 13: [10, 10.0] | kofi annan iraq | Kofi_Annan |
| 739. | building | 14: [24, 8.0], 17: [10, 10.0] | building 's iraq | Occupation_of_Iraq_(2003–2011) |
| 740. | limits | 14: [10, 10.0] | limits 's iraq | Iran–Iraq_War |
| 741. | sites | 14: [10, 10.0], 35: [12, 6.0] | sites 's iraq | Iraq |
| 742. | powerful | 14: [10, 10.0] | powerful 's iraq | Iran–Iraq_War |
| 743. | claim | 15: [16, 5.33], 38: [10, 10.0] | claim 's iraq | Iraq |
| 744. | chaos | 15: [10, 10.0] | chaos 's iraq | Iran–Iraq_War |
| 745. | times | 16: [10, 10.0] | times 's bush | Bush_family |
| 746. | develop | 16: [10, 10.0] | develop 's iraq | Iraq |
| 747. | release | 16: [10, 10.0] | release palestinian israel | 2013–2014_Israeli–Palestinian_peace_talks |
| 748. | dept | 17: [10, 10.0] | dept iraq 's | Ministry_of_Health_(Iraq) |
| 749. | returns | 17: [10, 10.0] | returns 's iraq | Iraq |
| 750. | women | 17: [10, 10.0] | women 's world | Women's_World_Chess_Championship |
| 751. | elections | 21: [15, 7.5], 36: [10, 10.0] | elections 's party | Political_party_strength_in_U.S._states |
| 752. | nepal | 22: [10, 10.0] | nepal world briefing | Nepalese_Civil_War |
| 753. | settlement | 23: [10, 10.0] | settlement israeli israel | Israeli_settlement |
| 754. | next | 24: [10, 10.0], 50: [12, 6.0] | next 's iraq | Iraq_War |
| 755. | voters | 24: [10, 10.0] | voters 's party | Political_party_strength_in_U.S._states |
| 756. | sign | 24: [10, 10.0] | sign 's iraq | Iraqi_Sign_Language |
| 757. | six | 26: [17, 8.5], 49: [10, 10.0] | six 's iraq | Iraq_War |
| 758. | likely | 27: [10, 10.0] | likely 's iraq | Iraq |
| 759. | delay | 27: [10, 5.0], 30: [10, 10.0] | delay iraq 's | Operation_Northern_Delay |
| 760. | blame | 28: [10, 10.0] | blame iraq 's | Iran–Iraq_War |
| 761. | costs | 28: [10, 10.0] | costs iraq 's | Financial_cost_of_the_Iraq_War |
| 762. | approved | 28: [10, 10.0] | approved 's iraq | Iraq |
| 763. | serve | 32: [10, 10.0] | serve 's iraq | Iraq_War |
| 764. | return | 33: [10, 10.0], 45: [10, 10.0], 49: [10, 5.0] | return 's iraq | Iraq_War |
| 765. | despite | 36: [10, 10.0], 49: [16, 8.0], 51: [11, 5.5] | despite 's iraq | Iran–Iraq_War |
| 766. | win | 38: [10, 10.0] | win 's iraq | Iraq_War |
| 767. | barrier | 38: [10, 10.0], 40: [10, 5.0] | barrier israel israeli | Israeli_West_Bank_barrier |
| 768. | marshall | 39: [10, 10.0] | marshall iraq plan | Marshall_Plan |
| 769. | spanish | 41: [10, 10.0] | spanish spain 's | Spain |
| 770. | takes | 42: [10, 10.0], 50: [11, 5.5] | takes 's iraq | Iraq |
| 771. | increase | 43: [10, 10.0] | increase iraq 's | Iraq |
| 772. | boykin | 43: [10, 10.0] | boykin bush says | William_G._Boykin |
| 773. | sec | 43: [10, 10.0] | sec iraq 's | Iraq_War |
| 774. | tycoon | 44: [10, 10.0] | tycoon 's russian | Tycoon_(2002_film) |
| 775. | yukos | 44: [20, 10.0] | yukos 's oil | Yukos |
| 776. | rice | 44: [10, 10.0] | rice bush iraq | Condoleezza_Rice |
| 777. | loyalists | 46: [10, 10.0] | loyalists american hussein | Operation_Red_Dawn |
| 778. | hawk | 47: [10, 10.0] | hawk american black | Black_Hawk_War |
| 779. | large | 47: [14, 7.0], 50: [10, 10.0] | large 's iraq | Iraq |
| 780. | staff | 47: [10, 10.0] | staff 's iraq | Casualties_of_the_Iraq_War |
| 781. | region | 49: [10, 10.0] | region 's iraq | Iraqi_Kurdistan |
| 782. | victims | 50: [10, 10.0] | victims 's says | List_of_serial_killers_by_number_of_victims |
| 783. | future | 50: [10, 10.0] | future 's iraq | Iraq_War |
| 784. | mubarak | 51: [10, 10.0] | mubarak egypt arab | Hosni_Mubarak |
| 785. | outposts | 1: [10, 10.0] | outposts israeli israel | Israeli_outpost |
| 786. | across | 12: [29, 9.67] | across 's iraq | Iraq_War |
| 787. | nato | 4: [19, 9.5], 6: [14, 7.0], 41: [15, 7.5], 49: [15, 5.0] | nato iraq 's | NATO_Training_Mission_–_Iraq |
| 788. | day | 7: [18, 9.0], 33: [13, 6.5], 50: [19, 9.5] | day 's iraq | Iraq |
| 789. | service | 7: [10, 5.0], 10: [38, 9.5] | service 's security | Diplomatic_Security_Service |
| 790. | become | 9: [10, 5.0], 39: [13, 6.5], 47: [19, 9.5] | become 's iraq | Iraq_War |
| 791. | shaikh | 10: [19, 9.5] | shaikh qaeda mohammed | Khalid_Sheikh_Mohammed |
| 792. | heart | 15: [19, 9.5] | heart 's iraqi | Hearts_and_minds_(Iraq) |
| 793. | another | 26: [19, 9.5], 39: [10, 5.0] | another 's iraq | Iraq_War |
| 794. | million | 12: [28, 9.33], 42: [15, 5.0] | million 's iraq | Iraq |
| 795. | help | 3: [18, 9.0] | help iraq 's | Iran–Iraq_War |
| 796. | outbreak | 12: [18, 9.0] | outbreak sars health | 2002–2004_SARS_outbreak |
| 797. | high | 12: [18, 9.0] | high 's iraq | Iraq_War |
| 798. | far | 12: [18, 9.0], 34: [10, 5.0], 49: [16, 8.0] | far 's iraq | Iraq_War |
| 799. | islamic | 32: [18, 9.0], 47: [11, 5.5] | islamic 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 800. | issue | 50: [18, 9.0] | issue 's iraq | Environmental_issues_in_Iraq |
| 801. | without | 51: [18, 9.0] | without 's iraq | Iraq_War |
| 802. | capture | 10: [11, 5.5], 51: [71, 8.88] | capture hussein 's | Operation_Red_Dawn |
| 803. | mohammed | 10: [26, 8.67] | mohammed 's qaeda | Khalid_Sheikh_Mohammed |
| 804. | city | 35: [26, 8.67] | city 's american | List_of_U.S._cities_with_large_African-American_populations |
| 805. | last | 43: [26, 8.67] | last 's iraq | Iraq |
| 806. | support | 2: [17, 8.5] | support 's iraq | United_States_support_for_Iraq_during_the_Iran–Iraq_War |
| 807. | days | 4: [15, 5.0], 42: [17, 8.5] | days 's iraq | Invasion_of_Kuwait |
| 808. | authorities | 7: [17, 8.5] | authorities 's american | American_Association_of_Port_Authorities |
| 809. | commander | 19: [11, 5.5], 46: [17, 8.5] | commander 's iraq | Assassination_of_Qasem_Soleimani |
| 810. | death | 37: [17, 8.5] | death 's says | Death |
| 811. | germany | 2: [22, 7.33], 42: [21, 5.25], 50: [25, 8.33] | germany iraq 's | Germany–Iraq_relations |
| 812. | leaders | 46: [33, 8.25] | leaders 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 813. | links | 5: [16, 8.0] | links 's iraq | Saddam_Hussein_and_al-Qaeda_link_allegations |
| 814. | seen | 5: [16, 8.0] | seen 's iraq | Iraq_War |
| 815. | following | 6: [16, 8.0], 10: [38, 6.33] | following 's council | United_Nations_Security_Council |
| 816. | speech | 12: [16, 8.0], 25: [10, 5.0], 51: [11, 5.5] | speech bush iraq | Mission_Accomplished_speech |
| 817. | authority | 15: [24, 8.0] | authority iraq palestinian | Palestinian_National_Authority |
| 818. | agents | 17: [24, 8.0] | agents iraq american | April_Fool_(spy) |
| 819. | kenya | 21: [16, 8.0] | kenya africa 's | Kenya |
| 820. | child | 26: [16, 8.0], 46: [13, 6.5] | child 's children | Child_labour |
| 821. | official | 27: [16, 8.0], 49: [11, 5.5] | official 's says | Say_Say_Say |
| 822. | report | 35: [34, 5.67], 43: [16, 8.0] | report 's iraq | Iraq_Report |
| 823. | house | 36: [16, 8.0] | house 's bush | George_W._Bush |
| 824. | british | 38: [16, 8.0], 47: [36, 7.2] | british iraq 's | Mandatory_Iraq |
| 825. | march | 9: [23, 7.67], 28: [10, 5.0] | march 's iraq | 2003_invasion_of_Iraq |
| 826. | tanks | 13: [23, 7.67] | tanks 's iraqi | Tanks_of_Iraq |
| 827. | hussein | 51: [167, 7.59] | hussein iraq 's | Saddam_Hussein |
| 828. | set | 2: [15, 7.5], 25: [18, 6.0], 27: [20, 5.0] | set 's iraq | Iraq_War |
| 829. | agreement | 3: [15, 7.5], 7: [11, 5.5], 29: [14, 7.0] | agreement 's palestinian | Israeli–Palestinian_peace_process |
| 830. | number | 5: [15, 7.5], 25: [12, 6.0] | number 's iraq | Multi-National_Force_–_Iraq |
| 831. | feb | 7: [15, 7.5] | feb 's iraq | 2003_invasion_of_Iraq |
| 832. | news | 7: [15, 7.5], 12: [21, 5.25], 49: [13, 6.5] | news 's iraq | Iraqi_News |
| 833. | within | 12: [15, 7.5] | within 's iraq | Iraq |
| 834. | equipment | 13: [15, 7.5] | equipment iraq 's | List_of_current_equipment_of_the_Iraqi_Army |
| 835. | mission | 13: [15, 7.5], 23: [11, 5.5] | mission iraq 's | Mission_Accomplished_speech |
| 836. | close | 17: [15, 7.5] | close 's iraq | Iraq |
| 837. | case | 17: [15, 7.5], 37: [24, 6.0], 50: [15, 5.0] | case 's iraq | COVID-19_pandemic_in_Iraq |
| 838. | vietnam | 18: [15, 7.5] | vietnam health cases | COVID-19_pandemic_in_Vietnam |
| 839. | anthrax | 18: [15, 7.5] | anthrax says iraq | 2001_anthrax_attacks |
| 840. | around | 19: [15, 7.5], 45: [13, 6.5], 51: [10, 5.0] | around 's iraq | Iraq |
| 841. | latest | 19: [11, 5.5], 28: [15, 7.5] | latest 's iraq | Iraq_War |
| 842. | western | 20: [15, 7.5] | western 's iraq | 2017_Western_Iraq_campaign |
| 843. | prosecutors | 20: [10, 5.0], 44: [15, 7.5] | prosecutors 's trial | Prosecutor |
| 844. | year | 33: [15, 7.5] | year 's iraq | Iraq_War |
| 845. | headquarters | 34: [15, 7.5] | headquarters 's iraq | Iraq_War |
| 846. | muhammad | 35: [15, 7.5] | muhammad 's iraq | Islam_in_Iraq |
| 847. | huge | 47: [15, 7.5] | huge 's iraq | Iraq |
| 848. | drive | 14: [22, 7.33] | drive 's iraq | 2003_invasion_of_Iraq |
| 849. | baghdad | 12: [92, 7.08] | baghdad iraq 's | Baghdad |
| 850. | turkey | 2: [14, 7.0] | turkey iraq 's | Iraq–Turkey_relations |
| 851. | warheads | 3: [14, 7.0] | warheads weapons iraq | United_Kingdom_and_weapons_of_mass_destruction |
| 852. | terrorists | 5: [14, 7.0], 44: [12, 6.0] | terrorists iraq 's | The_Terrorists_of_Iraq |
| 853. | space | 6: [24, 6.0], 19: [14, 7.0] | space 's china | Chinese_space_program |
| 854. | crops | 8: [14, 7.0] | crops europe world | Genetically_modified_crops |
| 855. | described | 10: [14, 7.0] | described 's iraq | Iraq |
| 856. | calling | 12: [14, 7.0] | calling 's iraq | Iraq |
| 857. | concern | 12: [11, 5.5], 15: [14, 7.0] | concern 's iraq | Occupation_of_Iraq_(2003–2011) |
| 858. | change | 12: [14, 7.0], 31: [10, 5.0] | change 's iraq | Occupation_of_Iraq_(2003–2011) |
| 859. | casualties | 12: [14, 7.0] | casualties american iraqi | Casualties_of_the_Iraq_War |
| 860. | warfare | 13: [14, 7.0] | warfare 's iraqi | Iraqi_biological_weapons_program |
| 861. | old | 15: [14, 7.0] | old 's iraq | Iraq |
| 862. | rocket | 15: [14, 7.0] | rocket 's israeli | Palestinian_rocket_attacks_on_Israel |
| 863. | regime | 15: [14, 7.0] | regime iraq 's | Ba'athist_Iraq |
| 864. | road | 18: [14, 7.0] | road 's palestinian | Road_map_for_peace |
| 865. | cities | 21: [14, 7.0], 32: [11, 5.5] | cities 's iraq | 2003_invasion_of_Iraq |
| 866. | representative | 21: [14, 7.0] | representative iraq 's | Council_of_Representatives_of_Iraq |
| 867. | european | 22: [17, 5.67], 36: [14, 7.0] | european 's union | European_Union |
| 868. | network | 32: [14, 7.0], 51: [14, 7.0] | network 's iraq | Iraq_War |
| 869. | fires | 32: [14, 7.0] | fires israeli 's | Israel |
| 870. | netherlands | 40: [14, 7.0] | netherlands europe world | Netherlands |
| 871. | black | 47: [14, 7.0] | black 's american | African_Americans |
| 872. | even | 49: [14, 7.0] | even 's iraq | Iraq_War |
| 873. | presidential | 51: [14, 7.0] | presidential 's pres | 1992_United_States_presidential_election_in_Georgia |
| 874. | holiday | 52: [14, 7.0] | holiday 's world | Federal_holidays_in_the_United_States |
| 875. | federal | 10: [41, 6.83] | federal 's security | Federal_Security_Service |
| 876. | part | 2: [11, 5.5], 24: [27, 6.75] | part 's iraq | Iraq |
| 877. | aid | 12: [20, 6.67] | aid iraq 's | Foreign_aid_to_Iraq |
| 878. | korean | 17: [11, 5.5], 40: [20, 6.67] | korean north korea | North_Korea–South_Korea_relations |
| 879. | russian | 44: [20, 6.67] | russian russia 's | Russia |
| 880. | israel | 2: [33, 6.6] | israel palestinian israeli | Israeli–Palestinian_conflict |
| 881. | virus | 16: [33, 6.6] | virus sars health | Severe_acute_respiratory_syndrome_coronavirus_2 |
| 882. | move | 2: [12, 6.0], 38: [13, 6.5], 45: [11, 5.5] | move 's iraq | 2003_invasion_of_Iraq |
| 883. | africa | 2: [13, 6.5] | africa world 's | South_Africa |
| 884. | white | 2: [12, 6.0], 5: [16, 5.33], 36: [13, 6.5] | white bush 's | George_W._Bush |
| 885. | visits | 3: [13, 6.5] | visits 's iraq | Gulf_War |
| 886. | carter | 4: [13, 6.5] | carter 's jimmy | Jimmy_Carter |
| 887. | critics | 5: [10, 5.0], 18: [13, 6.5] | critics 's iraq | 2003_invasion_of_Iraq |
| 888. | rights | 7: [11, 5.5], 30: [10, 5.0], 33: [13, 6.5] | rights 's human | Human_rights |
| 889. | form | 9: [13, 6.5] | form 's iraq | Iraq_War |
| 890. | combat | 9: [13, 6.5] | combat iraq 's | Iraq_War |
| 891. | accused | 11: [13, 6.5] | accused 's government | Government_of_India |
| 892. | heavy | 12: [13, 6.5] | heavy 's iraq | 2003_invasion_of_Iraq |
| 893. | artillery | 12: [13, 6.5] | artillery iraqi 's | Iran–Iraq_War |
| 894. | positions | 13: [13, 6.5] | positions 's iraq | Governmental_positions_on_the_Iraq_War_prior_to_the_2003_invasion_of_Iraq |
| 895. | prepare | 14: [13, 6.5] | prepare iraq 's | Iran–Iraq_War |
| 896. | issues | 20: [13, 6.5] | issues 's iraq | Environmental_issues_in_Iraq |
| 897. | union | 20: [12, 6.0], 22: [13, 6.5] | union 's european | European_Union |
| 898. | offers | 20: [13, 6.5] | offers 's iraq | 2003_invasion_of_Iraq |
| 899. | jordan | 22: [13, 6.5] | jordan 's palestinian | Palestinians_in_Jordan |
| 900. | supreme | 24: [13, 6.5] | supreme 's court | Supreme_Court_of_the_United_States |
| 901. | progress | 24: [13, 6.5] | progress 's iraq | 2003_invasion_of_Iraq |
| 902. | like | 27: [13, 6.5], 30: [15, 5.0] | like 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 903. | identity | 40: [13, 6.5] | identity 's israel | Israeli_identity_card |
| 904. | travel | 43: [13, 6.5] | travel 's sars | 2002–2004_SARS_outbreak |
| 905. | senior | 49: [19, 6.33] | senior iraq 's | Iraq_War |
| 906. | korea | 23: [37, 5.29], 31: [41, 5.86], 40: [25, 6.25] | korea north south | North_Korea–South_Korea_relations |
| 907. | group | 50: [50, 6.25] | group 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 908. | hours | 12: [31, 6.2] | hours 's iraq | 2003_invasion_of_Iraq |
| 909. | resistance | 13: [31, 6.2] | resistance 's american | The_Resistance_(American_political_movement) |
| 910. | open | 2: [12, 6.0], 19: [11, 5.5] | open 's iraq | Iraq_War |
| 911. | home | 3: [12, 6.0] | home 's iraq | Iraq_War |
| 912. | flights | 5: [12, 6.0], 7: [10, 5.0] | flights iraq 's | Iraqi_Airways |
| 913. | west | 5: [16, 5.33], 27: [18, 6.0] | west israeli palestinian | Israeli–Palestinian_conflict |
| 914. | laws | 5: [12, 6.0] | laws 's hong | Hong_Kong_national_security_law |
| 915. | data | 5: [12, 6.0] | data 's iraq | Casualties_of_the_Iraq_War |
| 916. | kurds | 6: [11, 5.5], 15: [42, 6.0] | kurds iraq kurdish | Kurdish_languages |
| 917. | belgium | 7: [24, 6.0] | belgium nato iraq | NATO |
| 918. | announces | 8: [12, 6.0], 33: [10, 5.0] | announces 's world | The_World's_Billionaires |
| 919. | arrested | 8: [15, 5.0], 20: [12, 6.0] | arrested 's police | Arrest |
| 920. | forces | 12: [96, 6.0] | forces american iraq | American-led_intervention_in_Iraq_(2014–present) |
| 921. | spy | 13: [12, 6.0] | spy 's north | The_Spy_Gone_North |
| 922. | carrying | 13: [12, 6.0] | carrying 's american | Wife-carrying |
| 923. | intended | 14: [12, 6.0] | intended 's iraq | Iraq_War |
| 924. | stand | 14: [12, 6.0], 47: [11, 5.5] | stand 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 925. | seven | 14: [18, 6.0] | seven 's killed | The_Red_Queen_Kills_Seven_Times |
| 926. | split | 14: [12, 6.0] | split 's iraq | Arab_Socialist_Ba'ath_Party_–_Iraq_Region |
| 927. | posts | 15: [12, 6.0] | posts 's iraqi | Occupation_of_Iraq_(2003–2011) |
| 928. | adviser | 15: [12, 6.0] | adviser bush iraq | Bush–Blair_2003_Iraq_memo |
| 929. | -year-old | 15: [12, 6.0] | -year-old 's israeli | Mossad |
| 930. | majority | 17: [12, 6.0] | majority 's iraq | Iraq |
| 931. | work | 19: [18, 6.0], 28: [11, 5.5] | work iraq 's | Iraq_War |
| 932. | law | 19: [12, 6.0] | law 's world | Parkinson's_law |
| 933. | possible | 24: [12, 6.0], 34: [12, 6.0] | possible iraq 's | Iraq_War |
| 934. | criticism | 24: [12, 6.0] | criticism 's iraq | Criticism_of_the_Iraq_War |
| 935. | yes | 24: [12, 6.0] | yes 's european | Yes |
| 936. | poor | 26: [12, 6.0] | poor 's world | S&P_Global_Ratings |
| 937. | legislation | 27: [12, 6.0], 34: [11, 5.5] | legislation 's hong | Hong_Kong_Human_Rights_and_Democracy_Act |
| 938. | rajavi | 27: [12, 6.0] | rajavi group 's | Massoud_Rajavi |
| 939. | nigeria | 28: [12, 6.0] | nigeria 's taylor | Charles_Taylor_(Liberian_politician) |
| 940. | sending | 28: [12, 6.0] | sending iraq troops | American-led_intervention_in_Iraq_(2014–present) |
| 941. | meeting | 32: [12, 6.0] | meeting 's iraq | Iraq |
| 942. | daily | 38: [18, 6.0] | daily iraq 's | Iraq_War |
| 943. | guerrilla | 46: [24, 6.0] | guerrilla iraq american | Strategy_and_tactics_of_guerrilla_warfare |
| 944. | groups | 49: [18, 6.0] | groups 's iraq | Special_Groups_(Iraq) |
| 945. | well | 51: [12, 6.0] | well 's iraq | Iraq_War |
| 946. | civilian | 13: [23, 5.75] | civilian iraq iraqi | Casualties_of_the_Iraq_War |
| 947. | urban | 13: [17, 5.67] | urban 's city | List_of_cities_in_China_by_population |
| 948. | karbala | 14: [17, 5.67] | karbala american iraqi | Karbala |
| 949. | jay | 17: [17, 5.67] | jay iraq garner | Jay_Garner |
| 950. | charges | 19: [17, 5.67], 44: [15, 5.0] | charges 's world | Pickett's_Charge |
| 951. | epidemic | 20: [17, 5.67] | epidemic sars 's | 2002–2004_SARS_outbreak |
| 952. | intelligence | 40: [28, 5.6] | intelligence iraq 's | Iraqi_Intelligence_Service |
| 953. | gulf | 2: [11, 5.5] | gulf iraq persian | Gulf_War |
| 954. | antiterror | 3: [11, 5.5] | antiterror 's effort | Omnibus_Counterterrorism_Act_of_1995 |
| 955. | health | 3: [11, 5.5] | health sars world | 2002–2004_SARS_outbreak |
| 956. | pledge | 5: [11, 5.5] | pledge 's bush | Read_my_lips:_no_new_taxes |
| 957. | appeals | 5: [11, 5.5] | appeals court 's | United_States_courts_of_appeals |
| 958. | antiwar | 7: [11, 5.5] | antiwar iraq 's | Iraqi_insurgency_(2011–2013) |
| 959. | series | 8: [11, 5.5], 20: [10, 5.0] | series 's american | The_Office_(American_TV_series) |
| 960. | system | 8: [11, 5.5] | system 's iraq | Iraq |
| 961. | aide | 10: [11, 5.5] | aide 's iraq | 2003_invasion_of_Iraq |
| 962. | significant | 12: [11, 5.5] | significant 's iraq | Iraq |
| 963. | deep | 12: [11, 5.5] | deep iraq 's | Iraqi_insurgency_(2003–2011) |
| 964. | masks | 12: [11, 5.5] | masks sars gas | Mask |
| 965. | st | 12: [11, 5.5] | st 's iraq | Iraqi_Army |
| 966. | enter | 12: [11, 5.5] | enter iraq 's | 2003_invasion_of_Iraq |
| 967. | deliver | 13: [11, 5.5] | deliver 's iraq | 2003_invasion_of_Iraq |
| 968. | tank | 14: [11, 5.5] | tank 's israeli | Tanks_of_the_Israel_Defense_Forces |
| 969. | hands | 15: [11, 5.5] | hands 's american | Hands_Across_America |
| 970. | freedom | 15: [11, 5.5] | freedom 's iraq | Iraq_War |
| 971. | deny | 16: [11, 5.5] | deny 's iraq | 2003_invasion_of_Iraq |
| 972. | considered | 16: [11, 5.5] | considered 's iraq | Iraq |
| 973. | challenge | 17: [11, 5.5] | challenge 's iraq | Iraq |
| 974. | live | 17: [11, 5.5] | live 's photo | Windows_Photo_Gallery |
| 975. | run | 19: [11, 5.5], 51: [10, 5.0] | run 's iraq | Iraq |
| 976. | ancient | 19: [11, 5.5] | ancient 's iraqi | Iraqi_cuisine |
| 977. | ariel | 19: [11, 5.5] | ariel sharon israel | Ariel_Sharon |
| 978. | closed | 19: [11, 5.5] | closed 's says | Proprietary_software |
| 979. | algeria | 21: [11, 5.5] | algeria tourists africa | Tourism_in_Algeria |
| 980. | settlers | 22: [11, 5.5] | settlers israeli palestinian | Israeli_settlement |
| 981. | petersburg | 22: [11, 5.5] | petersburg st russia | Saint_Petersburg |
| 982. | trial | 25: [20, 5.0], 50: [11, 5.5] | trial 's court | Trial_court |
| 983. | chairman | 25: [11, 5.5] | chairman 's iraq | Iraq_War |
| 984. | popular | 26: [11, 5.5] | popular 's photo | Google_Photos |
| 985. | public | 29: [22, 5.5] | public 's iraq | 2003_invasion_of_Iraq |
| 986. | time | 31: [11, 5.5] | time 's iraq | Once_Upon_a_Time_in_Iraq |
| 987. | blasts | 35: [11, 5.5] | blasts two baghdad | List_of_major_terrorist_incidents |
| 988. | working | 38: [11, 5.5] | working 's iraq | Iraq_War |
| 989. | paper | 38: [11, 5.5] | paper 's newspaper | Newspaper |
| 990. | describes | 40: [11, 5.5] | describes 's says | Say's_law |
| 991. | east | 42: [11, 5.5], 49: [15, 5.0] | east middle 's | Middle_East |
| 992. | army | 42: [11, 5.5] | army 's iraq | Iraqi_Army |
| 993. | makes | 42: [11, 5.5] | makes 's iraq | Iraq |
| 994. | toward | 43: [11, 5.5] | toward 's iraq | Iraq_War |
| 995. | deputy | 46: [11, 5.5] | deputy 's iraq | Chamber_of_Deputies_of_Iraq |
| 996. | sunni | 46: [11, 5.5] | sunni iraq american | Shia–Sunni_relations |
| 997. | administrator | 46: [11, 5.5] | administrator iraq iraqi | Coalition_Provisional_Authority |
| 998. | economy | 51: [11, 5.5] | economy 's china | Economy_of_China |
| 999. | north | 29: [54, 5.4], 49: [20, 5.0] | north korea 's | North_Korea |
| 1000. | persian | 10: [16, 5.33] | persian iraq gulf | Gulf_War |
| 1001. | cases | 12: [32, 5.33] | cases sars health | 2002–2004_SARS_outbreak |
| 1002. | capital | 12: [16, 5.33] | capital 's baghdad | Baghdad |
| 1003. | irish | 15: [16, 5.33] | irish ireland northern | Northern_Ireland |
| 1004. | several | 24: [16, 5.33] | several 's iraq | Iraq_War |
| 1005. | force | 8: [37, 5.29] | force iraq 's | Multi-National_Force_–_Iraq |
| 1006. | troops | 2: [26, 5.2] | troops iraq american | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 1007. | allies | 9: [15, 5.0], 12: [26, 5.2] | allies iraq 's | Iraq_War |
| 1008. | three | 35: [26, 5.2] | three 's iraq | Iraq_War |
| 1009. | free | 2: [10, 5.0], 30: [10, 5.0] | free 's iraq | Free_Iraqi_Army |
| 1010. | silva | 3: [10, 5.0] | silva brazil 's | Thiago_Silva |
| 1011. | ago | 4: [15, 5.0], 7: [10, 5.0] | ago 's years | All_Those_Years_Ago |
| 1012. | demand | 4: [15, 5.0] | demand 's iraq | Iraq |
| 1013. | polls | 5: [10, 5.0] | polls 's party | Democratic_Party_(United_States) |
| 1014. | need | 5: [10, 5.0] | need iraq 's | Iran–Iraq_War |
| 1015. | soviet | 5: [10, 5.0] | soviet 's russia | Russian_Soviet_Federative_Socialist_Republic |
| 1016. | scandal | 5: [10, 5.0] | scandal 's north | A_Very_English_Scandal_(TV_series) |
| 1017. | ayatollah | 5: [15, 5.0] | ayatollah iran 's | Ayatollah |
| 1018. | witness | 6: [10, 5.0] | witness 's trial | United_States_Federal_Witness_Protection_Program |
| 1019. | avert | 6: [10, 5.0] | avert iraq 's | 2003_invasion_of_Iraq |
| 1020. | warn | 8: [10, 5.0] | warn 's american | Jennifer_Warnes |
| 1021. | avoid | 8: [10, 5.0] | avoid iraq 's | 2003_invasion_of_Iraq |
| 1022. | inspector | 8: [10, 5.0] | inspector iraq weapons | Iraq_and_weapons_of_mass_destruction |
| 1023. | supporters | 8: [10, 5.0] | supporters 's american | Supporters'_Shield |
| 1024. | declared | 9: [10, 5.0] | declared 's bush | George_W._Bush |
| 1025. | destroy | 9: [10, 5.0] | destroy iraq hussein | Hussein_Kamel_al-Majid |
| 1026. | announced | 9: [10, 5.0] | announced 's iraq | Iraq |
| 1027. | hague | 9: [10, 5.0] | hague crimes world | Hague_Conventions_of_1899_and_1907 |
| 1028. | front | 10: [10, 5.0] | front 's iraq | Iraqi_Turkmen_Front |
| 1029. | prices | 10: [10, 5.0] | prices oil 's | Price_of_oil |
| 1030. | development | 11: [10, 5.0] | development 's iraq | Iraq_War |
| 1031. | attention | 11: [10, 5.0] | attention 's iraq | 2003_invasion_of_Iraq |
| 1032. | widespread | 12: [10, 5.0] | widespread 's iraq | Iraq_War |
| 1033. | legal | 12: [10, 5.0] | legal 's says | Legal_status_of_cocaine |
| 1034. | cause | 12: [10, 5.0] | cause 's iraq | Iraq_War |
| 1035. | months | 12: [15, 5.0] | months 's iraq | 2003_invasion_of_Iraq |
| 1036. | appears | 12: [10, 5.0] | appears 's iraq | Iraq |
| 1037. | seize | 12: [10, 5.0] | seize 's iraq | 2003_invasion_of_Iraq |
| 1038. | third | 12: [10, 5.0] | third 's iraq | Iraq_War |
| 1039. | modern | 12: [10, 5.0] | modern 's city | Modern_Vampires_of_the_City |
| 1040. | airspace | 12: [10, 5.0] | airspace iraq american | 2003_invasion_of_Iraq |
| 1041. | explosives | 12: [10, 5.0] | explosives american says | Improvised_explosive_device |
| 1042. | tactics | 13: [10, 5.0] | tactics iraq 's | Iran–Iraq_War |
| 1043. | good | 13: [10, 5.0] | good 's iraq | Iraq_War |
| 1044. | needed | 14: [10, 5.0] | needed iraq 's | Iraq |
| 1045. | charge | 14: [10, 5.0] | charge 's iraq | Iraq |
| 1046. | scores | 14: [10, 5.0] | scores iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 1047. | lt | 14: [10, 5.0] | lt iraq american | Lt._Dan_Band |
| 1048. | northward | 14: [10, 5.0] | northward baghdad american | Iraq_War |
| 1049. | investigation | 14: [10, 5.0], 28: [10, 5.0] | investigation 's government | Special_Counsel_investigation_(2017–2019) |
| 1050. | employees | 14: [10, 5.0] | employees iraq 's | Nisour_Square_massacre |
| 1051. | drinking | 14: [10, 5.0] | drinking africa ireland | Kings_(game) |
| 1052. | flag | 15: [10, 5.0] | flag american iraqi | Jihadist_flag |
| 1053. | moment | 15: [10, 5.0] | moment 's iraq | Iran–Iraq_War |
| 1054. | hundred | 15: [10, 5.0] | hundred iraq several | Iraq |
| 1055. | leaves | 15: [10, 5.0] | leaves 's bush | George_H._W._Bush |
| 1056. | militants | 15: [10, 5.0] | militants palestinian israeli | Palestinian_insurgency_in_South_Lebanon |
| 1057. | quebec | 16: [10, 5.0] | quebec 's premier | Premier_of_Quebec |
| 1058. | provincial | 16: [10, 5.0] | provincial 's quebec | Sûreté_du_Québec |
| 1059. | lebanese | 20: [15, 5.0] | lebanese 's american | Lebanese_Americans |
| 1060. | little | 21: [10, 5.0] | little 's iraq | Iraq_War |
| 1061. | port | 21: [10, 5.0] | port 's iraq | 2003_invasion_of_Iraq |
| 1062. | family | 22: [10, 5.0] | family 's hussein | Saddam's_family |
| 1063. | promise | 23: [10, 5.0] | promise 's bush | George_H._W._Bush |
| 1064. | crash | 23: [10, 5.0] | crash plane killed | Lynyrd_Skynyrd_plane_crash |
| 1065. | deal | 23: [10, 5.0] | deal 's north | Deal_or_No_Deal |
| 1066. | referendum | 24: [15, 5.0], 34: [10, 5.0] | referendum 's vote | 2011_United_Kingdom_Alternative_Vote_referendum |
| 1067. | possibility | 24: [10, 5.0] | possibility 's iraq | Iran–Iraq_War |
| 1068. | king | 26: [10, 5.0] | king 's jordan | Hussein_of_Jordan |
| 1069. | seems | 26: [10, 5.0] | seems 's iraq | Iraq |
| 1070. | site | 26: [10, 5.0] | site 's american | United_States |
| 1071. | missing | 26: [10, 5.0] | missing 's iraq | Foreign_hostages_in_Iraq |
| 1072. | washington | 28: [10, 5.0] | washington 's iraq | Occupation_of_Iraq_(2003–2011) |
| 1073. | remains | 28: [10, 5.0] | remains 's iraq | Iraq |
| 1074. | credibility | 29: [10, 5.0] | credibility 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 1075. | journalist | 29: [10, 5.0] | journalist 's journalists | Journalist |
| 1076. | demands | 30: [10, 5.0] | demands iraq palestinian | Israeli–Palestinian_conflict |
| 1077. | kazemi | 30: [10, 5.0] | kazemi iranian iran | Zahra_Kazemi |
| 1078. | finance | 30: [10, 5.0] | finance 's iraq | Invasion_of_Kuwait |
| 1079. | trials | 31: [10, 5.0] | trials 's british | Nuremberg_trials |
| 1080. | remain | 32: [10, 5.0] | remain 's iraq | Iraq |
| 1081. | country | 33: [40, 5.0] | country 's iraq | Iraq |
| 1082. | league | 37: [10, 5.0] | league arab iraq | Arab_League |
| 1083. | china | 38: [20, 5.0] | china 's north | North_China |
| 1084. | cleared | 38: [10, 5.0] | cleared world 's | S.T.A.L.K.E.R.:_Clear_Sky |
| 1085. | critical | 38: [10, 5.0] | critical 's iraq | Iraq_War |
| 1086. | justice | 40: [10, 5.0] | justice 's court | List_of_justices_of_the_Supreme_Court_of_the_United_States |
| 1087. | includes | 40: [10, 5.0] | includes 's iraq | Iraq |
| 1088. | settlements | 40: [10, 5.0] | settlements israel palestinian | Israeli–Palestinian_conflict |
| 1089. | made | 43: [15, 5.0] | made 's iraq | Iraq_War |
| 1090. | gunmen | 43: [10, 5.0] | gunmen israeli palestinian | 2010_Palestinian_militancy_campaign |
| 1091. | enough | 43: [10, 5.0] | enough 's iraq | Iraq |
| 1092. | khodorkovsky | 44: [20, 5.0] | khodorkovsky 's putin | Mikhail_Khodorkovsky |
| 1093. | expected | 45: [10, 5.0] | expected 's iraq | Iran–Iraq_War |
| 1094. | civil | 45: [10, 5.0] | civil 's iraq | Iraqi_Civil_War_(2006–2008) |
| 1095. | focus | 46: [10, 5.0] | focus 's iraq | Iran–Iraq_War |
| 1096. | role | 46: [10, 5.0] | role iraq 's | Israel's_role_in_the_Iran–Iraq_war |
| 1097. | fuel | 50: [10, 5.0] | fuel north korea | North_Korea_and_weapons_of_mass_destruction |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | powell | 6: [12, inf] | powell 's says | Sidney_Powell |
| 2. | path | 11: [16, inf] | path world 's | World_Trade_Center_station_(PATH) |
| 3. | hundred | 20: [32, inf] | hundred lives hamoodi | Allen_West_(politician) |
| 4. | lives | 20: [32, inf] | lives hundred hamoodi | Allen_West_(politician) |
| 5. | marine | 21: [14, inf], 23: [30, 15.0] | marine corporal sergeant | Corporal |
| 6. | st | 23: [10, inf] | st class private | Private_first_class |
| 7. | army | 21: [19, 19.0], 23: [28, 9.33] | army sergeant specialist | United_States_Army_enlisted_rank_insignia |
| 8. | north | 2: [15, 15.0] | north korea nuclear | North_Korea_and_weapons_of_mass_destruction |
| 9. | korea | 2: [14, 14.0] | korea north nuclear | North_Korea_and_weapons_of_mass_destruction |
| 10. | chile | 37: [11, 11.0] | chile voices two | The_Voice_Chile |
| 11. | killed | 13: [10, 10.0] | killed us iraq | Iraq_War |
| 12. | n't | 14: [10, 10.0] | n't us says | T-Mobile_US |
| 13. | british | 13: [11, 5.5] | british troops basra | Battle_of_Basra_(2003) |
| 14. | georgia | 48: [11, 5.5] | georgia 's takes | List_of_counties_in_Georgia |
| 15. | israel | 41: [10, 5.0] | israel 's peace | Egypt–Israel_peace_treaty |
