# Keywords with the highest 'interestingness' in 2020

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
| 1. | missile | 2: [21, inf] | missile iran military | List_of_military_equipment_manufactured_in_Iran |
| 2. | britain | 2: [10, 10.0], 5: [18, inf], 15: [10, 10.0] | britain johnson u.k. | Woody_Johnson |
| 3. | tehran | 2: [10, inf] | tehran iran missile | Iranian_missile_tests |
| 4. | animals | 2: [10, inf] | animals coronavirus australia | COVID-19_pandemic_by_country_and_territory |
| 5. | plane | 2: [15, inf] | plane crash iran | Iran_Air_Flight_277 |
| 6. | ukrainian | 2: [11, inf] | ukrainian iran plane | Ukraine_International_Airlines_Flight_752 |
| 7. | ukraine | 2: [10, inf] | ukraine president zelensky | Volodymyr_Zelensky |
| 8. | near | 2: [10, inf] | near country attack | 2021_Tillabéri_attacks |
| 9. | prince | 2: [14, inf] | prince harry meghan | Meghan,_Duchess_of_Sussex |
| 10. | harry | 2: [13, inf] | harry meghan prince | Wedding_of_Prince_Harry_and_Meghan_Markle |
| 11. | royal | 2: [10, inf] | royal prince harry | Prince_Harry,_Duke_of_Sussex |
| 12. | meghan | 2: [11, inf] | meghan harry prince | Meghan,_Duchess_of_Sussex |
| 13. | hong | 3: [10, 10.0], 21: [13, inf], 27: [17, 5.67] | hong kong china | Hong_Kong |
| 14. | kong | 3: [10, 10.0], 21: [13, inf], 27: [17, 5.67] | kong hong china | Hong_Kong |
| 15. | women | 3: [14, inf] | women president violence | Violence_against_women |
| 16. | executives | 4: [10, inf] | executives dam charges | Mariana_dam_disaster |
| 17. | coronavirus | 4: [30, inf] | coronavirus pandemic china | COVID-19_pandemic |
| 18. | outbreak | 4: [15, inf] | outbreak coronavirus china | COVID-19_pandemic_in_mainland_China |
| 19. | wuhan | 4: [10, inf] | wuhan coronavirus china | COVID-19_pandemic_in_mainland_China |
| 20. | modi | 5: [10, inf] | modi india minister | Narendra_Modi |
| 21. | european | 5: [11, inf], 23: [10, 5.0] | european union e.u | European_Union |
| 22. | union | 5: [11, inf] | union european brexit | Brexit |
| 23. | brexit | 5: [16, inf] | brexit britain european | Brexit |
| 24. | took | 6: [10, inf] | took coronavirus country | COVID-19_pandemic_cases |
| 25. | hospital | 6: [10, inf] | hospital coronavirus medical | Canberra_Coronavirus_Field_Hospital |
| 26. | epidemic | 6: [15, inf] | epidemic coronavirus china | COVID-19_pandemic_in_mainland_China |
| 27. | killed | 6: [12, 6.0], 39: [10, inf] | killed people least | List_of_people_killed_for_being_transgender |
| 28. | ship | 6: [14, inf] | ship cruise japan | COVID-19_pandemic_on_cruise_ships |
| 29. | accused | 7: [14, inf] | accused president government | Student_government_president |
| 30. | might | 7: [10, inf] | might coronavirus election | 2020_United_States_presidential_election |
| 31. | afghan | 8: [11, inf] | afghan taliban peace | Afghan_peace_process |
| 32. | talks | 8: [11, inf] | talks afghan peace | Afghan_peace_process |
| 33. | least | 8: [11, 11.0], 26: [11, 5.5], 43: [10, inf] | least people coronavirus | COVID-19_pandemic |
| 34. | korea | 8: [18, 6.0], 16: [15, 15.0], 30: [10, inf] | korea south north | North_Korea–South_Korea_relations |
| 35. | politics | 9: [12, inf] | politics much could | You_Could_Have_It_So_Much_Better |
| 36. | questions | 9: [10, inf] | questions coronavirus government | COVID-19_pandemic_in_the_United_Kingdom |
| 37. | delhi | 9: [13, inf] | delhi police india | Delhi_Police |
| 38. | migrants | 9: [10, inf] | migrants coronavirus migrant | Indian_migrant_workers_during_the_COVID-19_pandemic |
| 39. | iraq | 11: [12, inf] | iraq iran u.s. | Iran–Iraq_War |
| 40. | spread | 11: [11, inf] | spread coronavirus virus | Misinformation_related_to_the_COVID-19_pandemic |
| 41. | lockdown | 13: [16, 8.0], 28: [10, inf] | lockdown coronavirus virus | COVID-19_lockdown_in_Italy |
| 42. | killing | 13: [15, inf] | killing iran people | Assassination_of_Qasem_Soleimani |
| 43. | japan | 13: [13, inf], 35: [10, inf] | japan coronavirus country | COVID-19_pandemic_by_country_and_territory |
| 44. | leaders | 13: [10, 10.0], 16: [10, inf], 29: [10, 5.0] | leaders president coronavirus | Families_First_Coronavirus_Response_Act |
| 45. | use | 14: [15, inf] | use coronavirus trump | Families_First_Coronavirus_Response_Act |
| 46. | town | 14: [11, inf] | town residents police | The_Residents |
| 47. | court | 14: [11, inf], 24: [13, inf] | court government supreme | Supreme_Court_of_the_United_States |
| 48. | detained | 14: [10, inf] | detained hong kong | 2019–20_Hong_Kong_protests |
| 49. | first | 15: [16, inf], 25: [11, 11.0], 30: [11, inf], 35: [12, inf] | first coronavirus virus | Coronavirus |
| 50. | abuse | 15: [10, inf] | abuse sexual children | Child_sexual_abuse |
| 51. | cease-fire | 15: [10, inf] | cease-fire peace yemen | Saudi_Arabian-led_intervention_in_Yemen |
| 52. | yemen | 15: [10, inf] | yemen saudi u.n. | Saudi_Arabian-led_intervention_in_Yemen |
| 53. | last | 16: [10, inf], 32: [11, 11.0] | last year coronavirus | Coronavirus |
| 54. | north | 16: [15, inf] | north korea south | North_Korea–South_Korea_relations |
| 55. | american | 17: [10, inf], 35: [12, inf], 40: [11, 5.5] | american u.s. trump | Donald_Trump_Jr. |
| 56. | germany | 20: [13, 13.0], 23: [10, inf], 26: [11, 11.0], 40: [10, 5.0] | germany german coronavirus | COVID-19_pandemic_in_Germany |
| 57. | deal | 20: [10, inf] | deal taliban peace | Afghan_peace_process |
| 58. | leader | 21: [14, inf], 33: [10, 5.0] | leader president opposition | Leader_of_the_Opposition_(India) |
| 59. | europe | 21: [10, inf], 24: [10, 10.0] | europe coronavirus cases | COVID-19_pandemic_in_Europe |
| 60. | forces | 21: [16, inf] | forces u.s. security | United_States_Armed_Forces |
| 61. | food | 22: [10, inf] | food coronavirus people | Impact_of_the_COVID-19_pandemic_on_the_food_industry |
| 62. | girl | 23: [11, inf] | girl -year-old german | Milli_Vanilli |
| 63. | floyd | 23: [11, inf] | floyd george killing | Killing_of_George_Floyd |
| 64. | british | 23: [13, inf], 25: [10, 5.0] | british johnson coronavirus | Boris_Johnson |
| 65. | statue | 24: [13, inf] | statue trump protests | George_Floyd_protests_in_Washington,_D.C. |
| 66. | infections | 24: [12, inf] | infections coronavirus cases | COVID-19_pandemic_in_Luxembourg |
| 67. | mass | 24: [10, inf] | mass coronavirus people | COVID-19_pandemic |
| 68. | pilot | 25: [12, inf] | pilot crash air | Dunbeath_air_crash |
| 69. | security | 25: [10, inf] | security hong kong | Hong_Kong_national_security_law |
| 70. | july | 26: [10, inf] | july coronavirus u.s. | COVID-19_pandemic_in_the_United_States |
| 71. | military | 26: [11, inf] | military u.s. iran | Armed_Forces_of_the_Islamic_Republic_of_Iran |
| 72. | base | 26: [10, inf] | base military attack | Camp_Chapman_attack |
| 73. | residents | 26: [13, inf] | residents coronavirus home | Stay-at-home_order |
| 74. | bolsonaro | 28: [12, inf] | bolsonaro brazil president | Jair_Bolsonaro |
| 75. | beirut | 32: [35, inf] | beirut blast lebanon | 2020_Beirut_explosion |
| 76. | explosion | 32: [14, inf] | explosion beirut lebanon | 2020_Beirut_explosion |
| 77. | blast | 32: [19, inf] | blast beirut lebanon | 2020_Beirut_explosion |
| 78. | become | 35: [10, inf] | become coronavirus country | COVID-19_pandemic_by_country_and_territory |
| 79. | abe | 35: [10, inf] | abe japan shinzo | Akie_Abe |
| 80. | set | 36: [10, inf] | set coronavirus country | COVID-19_pandemic_in_Georgia_(country) |
| 81. | camp | 37: [12, inf] | camp auschwitz refugee | Auschwitz_concentration_camp |
| 82. | russia | 38: [10, inf] | russia putin russian | Opposition_to_Vladimir_Putin_in_Russia |
| 83. | families | 39: [10, inf] | families home coronavirus | Families_First_Coronavirus_Response_Act |
| 84. | system | 40: [10, inf] | system health coronavirus | COVID-19_pandemic_by_country_and_territory |
| 85. | positive | 40: [14, inf] | positive coronavirus tested | COVID-19_pandemic_in_Italy |
| 86. | harris | 41: [11, inf] | harris kamala canada | Family_of_Kamala_Harris |
| 87. | scientists | 42: [11, inf] | scientists coronavirus vaccine | COVID-19_vaccine |
| 88. | presidential | 43: [10, inf] | presidential election president | United_States_presidential_election |
| 89. | move | 43: [11, inf] | move coronavirus u.s. | COVID-19_pandemic_in_the_United_States |
| 90. | johnson | 42: [19, 19.0] | johnson boris minister | Boris_Johnson |
| 91. | crash | 2: [16, 16.0], 11: [12, 12.0] | crash plane iran | Iran_Air_Flight_277 |
| 92. | protests | 3: [14, 14.0] | protests hong kong | 2019–20_Hong_Kong_protests |
| 93. | iran | 8: [28, 14.0], 23: [12, 12.0] | iran iranian u.s. | Iran–United_States_relations |
| 94. | travel | 11: [14, 14.0] | travel coronavirus virus | Coronavirus |
| 95. | even | 17: [14, 14.0], 37: [11, 5.5] | even coronavirus china | COVID-19_pandemic_in_mainland_China |
| 96. | israeli | 19: [14, 14.0] | israeli israel netanyahu | Yair_Netanyahu |
| 97. | united | 23: [14, 14.0] | united states u.s. | United_States |
| 98. | india | 29: [14, 14.0] | india coronavirus modi | COVID-19_lockdown_in_India |
| 99. | restrictions | 11: [13, 13.0], 24: [10, 5.0] | restrictions coronavirus virus | COVID-19_pandemic |
| 100. | china | 2: [12, 12.0], 43: [15, 5.0] | china coronavirus beijing | COVID-19_pandemic_in_mainland_China |
| 101. | chinese | 3: [10, 10.0], 25: [12, 12.0] | chinese china coronavirus | COVID-19_pandemic_in_mainland_China |
| 102. | dead | 4: [12, 12.0] | dead least coronavirus | COVID-19_pandemic_in_Spain |
| 103. | crisis | 4: [12, 12.0], 9: [12, 6.0] | crisis coronavirus china | COVID-19_pandemic_in_mainland_China |
| 104. | record | 26: [12, 12.0] | record cases u.s. | Statistics_of_the_COVID-19_pandemic_in_the_United_States |
| 105. | kills | 8: [11, 11.0] | kills least iran | 2019–2021_Persian_Gulf_crisis |
| 106. | boris | 21: [10, 5.0], 42: [11, 11.0] | boris johnson minister | Boris_Johnson |
| 107. | -year-old | 23: [11, 11.0] | -year-old girl case | Electra_complex |
| 108. | america | 23: [11, 11.0] | america latin trump | One_America_News_Network |
| 109. | close | 41: [11, 11.0] | close coronavirus president | COVID-19_pandemic |
| 110. | case | 43: [11, 11.0] | case court coronavirus | COVID-19_pandemic_in_Italy |
| 111. | fight | 3: [10, 10.0] | fight coronavirus virus | Coronavirus |
| 112. | putin | 3: [10, 10.0] | putin president russia | Vladimir_Putin |
| 113. | brazil | 4: [10, 10.0], 17: [10, 5.0] | brazil bolsonaro president | Jair_Bolsonaro |
| 114. | deaths | 6: [11, 5.5], 8: [10, 10.0] | deaths coronavirus china | COVID-19_pandemic_in_mainland_China |
| 115. | years | 7: [10, 10.0], 9: [10, 5.0], 15: [10, 5.0], 23: [16, 5.33] | years court country | List_of_justices_of_the_Supreme_Court_of_the_United_States |
| 116. | fears | 8: [10, 10.0], 12: [11, 5.5] | fears coronavirus virus | Middle_East_respiratory_syndrome–related_coronavirus |
| 117. | measures | 11: [10, 10.0] | measures coronavirus virus | COVID-19_pandemic |
| 118. | like | 20: [10, 10.0] | like coronavirus pandemic | COVID-19_pandemic |
| 119. | west | 21: [10, 10.0] | west bank israel | Israeli_West_Bank_barrier |
| 120. | global | 30: [10, 10.0] | global coronavirus pandemic | COVID-19_pandemic |
| 121. | election | 31: [10, 10.0] | election president coronavirus | 2020_United_States_presidential_election |
| 122. | political | 39: [10, 10.0] | political coronavirus president | Impact_of_the_COVID-19_pandemic_on_politics |
| 123. | stimulus | 41: [10, 10.0] | stimulus trump coronavirus | CARES_Act |
| 124. | german | 23: [16, 8.0] | german germany merkel | Angela_Merkel |
| 125. | lebanon | 32: [16, 8.0] | lebanon beirut blast | 2020_Beirut_explosion |
| 126. | pandemic | 34: [24, 8.0] | pandemic coronavirus world | COVID-19_pandemic |
| 127. | states | 23: [15, 7.5] | states united u.s. | U.S._state |
| 128. | canada | 2: [14, 7.0], 11: [11, 5.5] | canada trudeau prime | Margaret_Trudeau |
| 129. | says | 6: [14, 7.0], 18: [11, 5.5] | says u.s. trump | Second_impeachment_of_Donald_Trump |
| 130. | u.s. | 37: [14, 7.0] | u.s. coronavirus trump | COVID-19_pandemic_in_the_United_States |
| 131. | world | 4: [20, 6.67], 17: [33, 5.5], 36: [10, 5.0] | world coronavirus pandemic | COVID-19_pandemic |
| 132. | many | 2: [13, 6.5] | many coronavirus people | COVID-19_pandemic |
| 133. | party | 7: [13, 6.5] | party china election | Elections_in_China |
| 134. | israel | 10: [13, 6.5] | israel netanyahu israeli | Yair_Netanyahu |
| 135. | two | 13: [16, 5.33], 18: [13, 6.5], 37: [16, 5.33] | two coronavirus china | COVID-19_pandemic_in_mainland_China |
| 136. | say | 40: [13, 6.5] | say coronavirus officials | Statistics_of_the_COVID-19_pandemic_in_the_United_States |
| 137. | could | 9: [19, 6.33] | could coronavirus u.s. | COVID-19_pandemic_in_the_United_States |
| 138. | police | 26: [25, 6.25] | police officers protests | George_Floyd_protests |
| 139. | city | 3: [12, 6.0] | city coronavirus hong | COVID-19_pandemic_in_Hong_Kong |
| 140. | virus | 4: [12, 6.0] | virus coronavirus cases | COVID-19_pandemic |
| 141. | would | 7: [17, 5.67], 34: [12, 6.0] | would coronavirus trump | Donald_Trump |
| 142. | rate | 20: [12, 6.0] | rate coronavirus city | COVID-19_pandemic_in_New_York_City |
| 143. | vaccine | 42: [12, 6.0] | vaccine coronavirus scientists | COVID-19_vaccine |
| 144. | coming | 3: [11, 5.5] | coming coronavirus many | COVID-19_pandemic |
| 145. | risk | 6: [11, 5.5] | risk coronavirus country | COVID-19_pandemic_by_country_and_territory |
| 146. | among | 17: [11, 5.5] | among coronavirus deaths | COVID-19_pandemic_deaths |
| 147. | judge | 26: [11, 5.5] | judge court mask | Anti-mask_law |
| 148. | health | 34: [11, 5.5] | health coronavirus virus | Severe_acute_respiratory_syndrome_coronavirus_2 |
| 149. | percent | 40: [11, 5.5] | percent coronavirus cases | COVID-19_pandemic |
| 150. | president | 7: [16, 5.33] | president trump coronavirus | Donald_Trump |
| 151. | cases | 40: [16, 5.33] | cases coronavirus virus | 2012_Middle_East_respiratory_syndrome_coronavirus_outbreak |
| 152. | prime | 5: [10, 5.0] | prime minister johnson | Boris_Johnson |
| 153. | russian | 6: [10, 5.0], 34: [10, 5.0], 38: [10, 5.0] | russian russia putin | Opposition_to_Vladimir_Putin_in_Russia |
| 154. | infected | 8: [10, 5.0] | infected coronavirus virus | Canine_coronavirus |
| 155. | worst | 9: [10, 5.0] | worst country violence | Lovecraft_Country_(TV_series) |
| 156. | time | 10: [10, 5.0] | time coronavirus first | Families_First_Coronavirus_Response_Act |
| 157. | response | 12: [10, 5.0] | response coronavirus china | COVID-19_pandemic_in_mainland_China |
| 158. | stay | 12: [10, 5.0] | stay home coronavirus | Stay-at-home_order |
| 159. | amid | 13: [10, 5.0] | amid coronavirus china | COVID-19_pandemic_in_mainland_China |
| 160. | long | 29: [10, 5.0] | long coronavirus country | COVID-19_pandemic_by_country_and_territory |
| 161. | border | 31: [10, 5.0] | border coronavirus china | COVID-19_pandemic_in_mainland_China |
| 162. | u.n. | 39: [15, 5.0] | u.n. united nations | Headquarters_of_the_United_Nations |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | crash | 2: [10, inf] | crash plane iran | Iran_Air_Flight_277 |
| 2. | pandemic | 9: [10, inf] | pandemic coronavirus us | COVID-19_pandemic_in_the_United_States |
| 3. | march | 10: [10, inf] | march coronavirus glance | Timeline_of_the_COVID-19_pandemic_in_March_2020 |
| 4. | april | 14: [19, inf] | april coronavirus glance | Timeline_of_the_COVID-19_pandemic_in_April_2020 |
| 5. | law | 27: [11, inf] | law hong kong | Hong_Kong_national_security_law |
| 6. | beirut | 32: [28, inf] | beirut explosion blast | 2020_Beirut_explosion |
| 7. | explosion | 32: [15, inf] | explosion beirut lebanon | 2020_Beirut_explosion |
| 8. | coronavirus | 4: [34, 34.0] | coronavirus glance uk | Dashboard_(business) |
| 9. | global | 19: [13, 13.0] | global report coronavirus | COVID-19_pandemic |
| 10. | security | 21: [13, 13.0] | security hong kong | Hong_Kong_national_security_law |
| 11. | hong | 21: [15, 5.0], 27: [23, 11.5], 40: [11, 5.5] | hong kong china | Hong_Kong |
| 12. | kong | 21: [15, 5.0], 27: [23, 11.5], 40: [11, 5.5] | kong hong china | Hong_Kong |
| 13. | first | 9: [10, 10.0] | first coronavirus 's | Families_First_Coronavirus_Response_Act |
| 14. | n't | 13: [10, 10.0] | n't covid- coronavirus | COVID-19_pandemic |
| 15. | cases | 21: [10, 10.0] | cases coronavirus covid- | COVID-19_pandemic_by_country_and_territory |
| 16. | deaths | 39: [10, 10.0] | deaths coronavirus covid- | List_of_deaths_due_to_COVID-19 |
| 17. | travel | 11: [19, 9.5] | travel coronavirus ban | Travel_ban |
| 18. | covid | 32: [19, 9.5] | covid uk 's | COVID-19_pandemic_in_the_United_Kingdom |
| 19. | may | 18: [18, 9.0] | may coronavirus glance | COVID-19_pandemic_in_the_Republic_of_Ireland |
| 20. | weinstein | 9: [16, 8.0] | weinstein harvey trial | Harvey_Weinstein_sexual_abuse_cases |
| 21. | latest | 11: [14, 7.0], 19: [12, 6.0] | latest coronavirus glance | COVID-19_pandemic_in_Luxembourg |
| 22. | belarus | 33: [19, 6.33] | belarus lukashenko opposition | Alexander_Lukashenko |
| 23. | christchurch | 35: [12, 6.0] | christchurch gunman mosque | Christchurch_mosque_shootings |
| 24. | outbreak | 9: [11, 5.5] | outbreak coronavirus covid- | COVID-19_pandemic |
| 25. | june | 23: [16, 5.33] | june coronavirus glance | Timeline_of_the_COVID-19_pandemic_in_the_United_Kingdom_(January–June_2020) |
| 26. | case | 9: [10, 5.0] | case coronavirus first | COVID-19_pandemic_by_country_and_territory |
| 27. | lockdown | 11: [10, 5.0] | lockdown coronavirus uk | COVID-19_lockdowns |
| 28. | johnson | 15: [10, 5.0] | johnson boris 's | Boris_Johnson |
| 29. | app | 19: [10, 5.0] | app contact-tracing coronavirus | NHS_COVID-19 |
| 30. | mask | 29: [10, 5.0] | mask coronavirus says | Face_masks_during_the_COVID-19_pandemic |
