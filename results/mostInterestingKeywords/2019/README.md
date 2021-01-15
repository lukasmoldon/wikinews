# Keywords with the highest 'interestingness' in 2019

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
| 1. | charges | 2: [12, inf], 4: [12, 6.0] | charges former court | Impeachment |
| 2. | officials | 2: [14, inf], 43: [11, 11.0] | officials say u.s. | Utah_Data_Center |
| 3. | court | 2: [10, inf], 51: [16, inf] | court supreme former | Supreme_Court_of_the_United_States |
| 4. | venezuela | 4: [20, 10.0], 18: [16, inf] | venezuela maduro opposition | Nicolás_Maduro |
| 5. | maduro | 4: [16, 8.0], 8: [19, inf], 18: [10, inf] | maduro venezuela president | Nicolás_Maduro |
| 6. | help | 5: [10, inf], 25: [10, 5.0] | help american trump | Ivanka_Trump |
| 7. | election | 7: [12, 12.0], 11: [10, 10.0], 13: [14, 14.0], 25: [10, inf] | election minister prime | Prime_Minister_of_the_United_Kingdom |
| 8. | report | 10: [10, inf] | report says government | Mueller_report |
| 9. | black | 10: [11, inf] | black south africa | South_Africa |
| 10. | border | 11: [10, 10.0], 14: [12, inf], 46: [12, 12.0] | border trump migrants | Trump_administration_migrant_detentions |
| 11. | vote | 11: [11, inf], 37: [10, 5.0], 50: [10, inf] | vote brexit election | Causes_of_the_vote_in_favour_of_Brexit |
| 12. | christchurch | 11: [14, inf] | christchurch zealand mosques | Christchurch_mosque_shootings |
| 13. | mosques | 11: [14, inf] | mosques zealand two | Christchurch_mosque_shootings |
| 14. | massacre | 11: [11, inf] | massacre zealand christchurch | Christchurch_mosque_shootings |
| 15. | erdogan | 14: [10, inf] | erdogan president turkey | Recep_Tayyip_Erdoğan |
| 16. | leaders | 14: [11, 5.5], 49: [10, inf] | leaders president trump | Donald_Trump |
| 17. | india | 15: [15, 7.5], 18: [11, inf], 20: [10, 10.0], 51: [17, 5.67] | india modi pakistan | 2014_India–Pakistan_floods |
| 18. | assange | 15: [10, inf] | assange julian wikileaks | Indictment_and_arrest_of_Julian_Assange |
| 19. | north | 16: [13, 6.5], 25: [26, inf], 40: [11, 11.0] | north korea trump | North_Korea–United_States_relations |
| 20. | notre-dame | 16: [33, inf] | notre-dame cathedral fire | Notre-Dame_de_Paris_fire |
| 21. | cathedral | 16: [32, inf] | cathedral notre-dame fire | Notre-Dame_de_Paris_fire |
| 22. | paris | 16: [14, inf], 40: [10, inf] | paris police fire | Paris_Police_Prefecture |
| 23. | sri | 16: [16, inf] | sri lanka attacks | 2019_Sri_Lanka_Easter_bombings |
| 24. | lanka | 16: [12, inf] | lanka sri attacks | 2019_Sri_Lanka_Easter_bombings |
| 25. | attacks | 17: [32, 8.0], 38: [10, inf] | attacks sri lanka | 2019_Sri_Lanka_Easter_bombings |
| 26. | sunday | 17: [17, inf] | sunday sri lanka | 2019_Sri_Lanka_Easter_bombings |
| 27. | putin | 17: [10, inf] | putin russia president | Vladimir_Putin |
| 28. | protest | 18: [11, inf], 27: [10, 5.0], 30: [10, inf] | protest hong kong | 2019–20_Hong_Kong_protests |
| 29. | opposition | 18: [12, inf] | opposition leader venezuela | Juan_Guaidó |
| 30. | guaidó | 18: [12, inf] | guaidó venezuela juan | Juan_Guaidó |
| 31. | crisis | 18: [12, inf] | crisis political venezuela | Crisis_in_Venezuela_during_the_Bolivarian_Revolution |
| 32. | fani | 18: [10, inf] | fani cyclone india | Cyclone_Fani |
| 33. | iraq | 19: [11, inf] | iraq iran u.s. | Iran–Iraq_War |
| 34. | last | 19: [10, inf] | last year month | The_Last_Month_of_the_Year |
| 35. | forces | 21: [10, 5.0], 31: [10, inf] | forces u.s. syria | Syrian_Democratic_Forces |
| 36. | union | 21: [12, 6.0], 42: [10, inf] | union european brexit | Brexit |
| 37. | political | 22: [10, 5.0], 29: [14, 14.0], 42: [10, 5.0], 51: [12, inf] | political minister president | Minister_President_of_Prussia |
| 38. | boat | 22: [13, inf] | boat fishing people | Traditional_fishing_boat |
| 39. | wife | 22: [10, inf] | wife former husband | Trophy_wife |
| 40. | iran | 24: [13, inf] | iran u.s. trump | Iran–United_States_relations |
| 41. | shooting | 25: [12, inf] | shooting police zealand | Christchurch_mosque_shootings |
| 42. | must | 25: [11, inf] | must court former | Supreme_Court_of_the_United_States |
| 43. | climate | 25: [10, inf] | climate change president | United_Nations_Climate_Change_conference |
| 44. | mexico | 25: [10, 10.0], 45: [10, inf] | mexico president trump | Donald_Trump |
| 45. | around | 25: [10, inf] | around world china | Around_the_World_in_Eighty_Days |
| 46. | g | 26: [11, inf] | g trump president | Donald_Trump |
| 47. | japan | 26: [10, inf], 41: [12, 6.0] | japan korea south | Japan–South_Korea_relations |
| 48. | kashmir | 32: [13, inf] | kashmir india pakistan | 2014_India–Pakistan_floods |
| 49. | iranian | 33: [10, inf], 39: [10, 10.0] | iranian iran u.s. | Iran–United_States_relations |
| 50. | prince | 34: [11, inf] | prince saudi andrew | Prince_Andrew,_Duke_of_York |
| 51. | fires | 34: [23, inf] | fires amazon brazil | 2019_Amazon_rainforest_wildfires |
| 52. | amazon | 34: [14, inf] | amazon fires brazil | 2019_Amazon_rainforest_wildfires |
| 53. | residents | 36: [10, inf] | residents government island | Norfolk_Island |
| 54. | pope | 36: [10, inf] | pope francis church | Pope_Francis |
| 55. | francis | 36: [11, inf] | francis pope abuse | Catholic_Church_sexual_abuse_cases |
| 56. | australia | 37: [12, inf] | australia china australian | Chinese_Australians |
| 57. | netanyahu | 37: [13, inf], 47: [10, inf] | netanyahu israel prime | Benjamin_Netanyahu |
| 58. | israel | 37: [14, inf] | israel netanyahu minister | Sara_Netanyahu |
| 59. | gantz | 38: [10, inf] | gantz netanyahu benny | Benny_Gantz |
| 60. | trudeau | 38: [15, inf] | trudeau minister justin | Justin_Trudeau |
| 61. | peru | 40: [12, inf] | peru president congress | President_of_Peru |
| 62. | kurds | 41: [12, inf] | kurds syria turkey | Kurds_in_Syria |
| 63. | kurdish | 41: [11, inf] | kurdish syria turkey | Kurds_in_Syria |
| 64. | turkey | 41: [15, inf] | turkey erdogan president | Recep_Tayyip_Erdoğan |
| 65. | troops | 41: [10, inf] | troops u.s. trump | Foreign_policy_of_the_Donald_Trump_administration |
| 66. | syrian | 41: [13, inf] | syrian syria isis | Syrian_civil_war |
| 67. | militia | 41: [11, inf] | militia syria turkey | Turkish_involvement_in_the_Syrian_civil_war |
| 68. | turkish | 41: [10, inf] | turkish syria turkey | Syria–Turkey_relations |
| 69. | typhoon | 41: [16, inf] | typhoon japan storm | 2020_Pacific_typhoon_season |
| 70. | amid | 42: [11, inf] | amid president country | List_of_presidents_who_did_not_win_reelection |
| 71. | lawmakers | 42: [19, inf] | lawmakers brexit parliament | Brexit_withdrawal_agreement |
| 72. | al-baghdadi | 43: [10, inf] | al-baghdadi leader isis | Abu_Bakr_al-Baghdadi |
| 73. | mining | 45: [10, inf] | mining dam company | Vale_S.A. |
| 74. | macron | 49: [12, inf] | macron president france | Emmanuel_Macron |
| 75. | eruption | 50: [11, inf] | eruption zealand white | 2019_Whakaari_/_White_Island_eruption |
| 76. | white | 50: [10, inf] | white house iran | White_House_Down |
| 77. | nobel | 50: [10, inf] | nobel prize peace | Nobel_Peace_Prize |
| 78. | base | 50: [10, inf] | base afghan u.s. | War_in_Afghanistan_(2001–present) |
| 79. | christmas | 52: [18, inf] | christmas holiday first | Christmas_and_holiday_season |
| 80. | trump | 12: [12, 6.0], 25: [44, 44.0] | trump president u.s. | Donald_Trump |
| 81. | taliban | 4: [23, 23.0] | taliban afghan talks | Afghan_peace_process |
| 82. | korea | 12: [13, 6.5], 25: [22, 22.0] | korea north south | North_Korea–South_Korea_relations |
| 83. | american | 9: [19, 19.0] | american u.s. trump | Donald_Trump |
| 84. | would | 4: [18, 18.0] | would president trump | Donald_Trump |
| 85. | could | 2: [10, 10.0], 9: [13, 6.5], 20: [12, 6.0], 33: [17, 17.0] | could trump president | Donald_Trump |
| 86. | u.s. | 9: [24, 6.0], 31: [17, 8.5], 50: [16, 16.0] | u.s. american trump | Presidency_of_Donald_Trump |
| 87. | parliament | 35: [16, 8.0], 42: [16, 16.0] | parliament brexit minister | Timeline_of_Brexit |
| 88. | people | 51: [16, 16.0] | people killed least | List_of_people_killed_for_being_transgender |
| 89. | zealand | 11: [30, 15.0], 50: [11, 5.5] | zealand christchurch minister | Christchurch_mosque_shootings |
| 90. | deal | 33: [15, 15.0], 42: [35, 5.83] | deal brexit iran | Boris_Johnson |
| 91. | syria | 2: [11, 11.0], 37: [11, 5.5], 41: [28, 14.0] | syria isis u.s. | Islamic_State_of_Iraq_and_the_Levant |
| 92. | family | 23: [12, 6.0], 45: [14, 14.0] | family members royal | British_royal_family |
| 93. | canada | 9: [13, 13.0] | canada trudeau minister | Justin_Trudeau |
| 94. | visit | 13: [13, 13.0], 23: [21, 5.25] | visit trump president | Donald_Trump |
| 95. | fire | 16: [26, 13.0], 46: [11, 5.5] | fire notre-dame cathedral | Notre-Dame_de_Paris_fire |
| 96. | many | 18: [10, 10.0], 31: [13, 13.0], 37: [10, 10.0], 44: [11, 5.5] | many say country | COVID-19_pandemic_by_country_and_territory |
| 97. | group | 26: [13, 13.0] | group isis attack | Islamic_State_of_Iraq_and_the_Levant_–_Khorasan_Province |
| 98. | day | 37: [13, 13.0] | day hong kong | Governor_of_Hong_Kong |
| 99. | abuse | 8: [12, 12.0] | abuse sexual pope | Catholic_Church_sexual_abuse_cases |
| 100. | state | 12: [12, 12.0], 29: [10, 5.0] | state islamic isis | Islamic_State_of_Iraq_and_the_Levant |
| 101. | protests | 27: [12, 12.0], 36: [20, 10.0] | protests hong kong | 2019–20_Hong_Kong_protests |
| 102. | national | 38: [12, 12.0] | national security president | National_Security_Advisor_(United_States) |
| 103. | ukraine | 39: [12, 12.0] | ukraine president zelensky | Volodymyr_Zelensky |
| 104. | bolivia | 46: [12, 12.0] | bolivia morales president | Evo_Morales |
| 105. | peace | 9: [11, 5.5], 38: [11, 11.0] | peace taliban talks | Afghan_peace_process |
| 106. | attack | 11: [15, 5.0], 48: [10, 5.0], 52: [11, 11.0] | attack police killed | 2016_shooting_of_Dallas_police_officers |
| 107. | britain | 21: [15, 7.5], 30: [11, 11.0] | britain brexit minister | Brexit |
| 108. | days | 41: [11, 11.0] | days two president | List_of_presidents_of_the_United_States_by_time_in_office |
| 109. | media | 50: [11, 11.0] | media social news | Social_media_as_a_news_source |
| 110. | faces | 2: [10, 5.0], 11: [10, 10.0] | faces china minister | China |
| 111. | woman | 2: [11, 5.5], 14: [10, 10.0] | woman accused police | 2020_Hathras_gang_rape_and_murder |
| 112. | cyclone | 12: [12, 6.0], 17: [10, 10.0] | cyclone mozambique storm | Tropical_Storm_Chalane |
| 113. | storm | 12: [11, 5.5], 41: [10, 10.0] | storm cyclone bahamas | 2019_Atlantic_hurricane_season |
| 114. | head | 13: [10, 10.0] | head former state | Head_of_state |
| 115. | brunei | 14: [10, 10.0] | brunei stoning gay | LGBT_rights_in_Brunei |
| 116. | police | 16: [10, 10.0] | police hong kong | Hong_Kong_Police_Force |
| 117. | easter | 17: [20, 10.0] | easter sri lanka | 2019_Sri_Lanka_Easter_bombings |
| 118. | came | 20: [10, 10.0] | came trump president | Donald_Trump |
| 119. | queen | 23: [10, 10.0] | queen elizabeth brexit | Elizabeth_II |
| 120. | bill | 24: [20, 10.0] | bill hong kong | 2019–20_Hong_Kong_protests |
| 121. | top | 29: [10, 10.0], 39: [10, 5.0] | top officials u.s. | List_of_former_Trump_administration_officials_who_endorsed_Joe_Biden |
| 122. | johnson | 34: [10, 10.0], 39: [24, 6.0], 50: [15, 5.0] | johnson boris brexit | Premiership_of_Boris_Johnson |
| 123. | island | 50: [10, 10.0] | island nation people | Algonquin_people |
| 124. | labour | 50: [10, 10.0] | labour party corbyn | Jeremy_Corbyn |
| 125. | ethiopian | 11: [29, 9.67] | ethiopian airlines crash | Ethiopian_Airlines_Flight_302 |
| 126. | two | 19: [18, 9.0] | two people killed | List_of_people_killed_for_being_transgender |
| 127. | first | 24: [17, 8.5], 46: [10, 5.0] | first time president | List_of_presidents_of_the_United_States_by_age |
| 128. | africa | 36: [17, 8.5] | africa south african | South_Africa |
| 129. | victims | 11: [16, 8.0] | victims zealand police | Christchurch_mosque_shootings |
| 130. | isis | 12: [10, 5.0], 43: [16, 8.0] | isis syria state | Islamic_State_of_Iraq_and_the_Levant |
| 131. | leader | 11: [14, 7.0], 24: [15, 7.5] | leader president trump | Donald_Trump |
| 132. | say | 2: [14, 7.0] | say officials police | SayHerName |
| 133. | talks | 9: [21, 7.0] | talks taliban peace | Afghan_peace_process |
| 134. | time | 40: [14, 7.0] | time first trump | Melania_Trump |
| 135. | corruption | 40: [14, 7.0] | corruption president former | Corruption_in_South_Korea |
| 136. | hong | 24: [40, 6.67] | hong kong protesters | 2019–20_Hong_Kong_protests |
| 137. | kong | 24: [40, 6.67] | kong hong protesters | 2019–20_Hong_Kong_protests |
| 138. | law | 33: [11, 5.5], 51: [20, 6.67] | law government would | Martial_law |
| 139. | plane | 11: [13, 6.5] | plane crash flight | Germanwings_Flight_9525 |
| 140. | flight | 11: [13, 6.5] | flight airlines ethiopian | Ethiopian_Airlines_Flight_302 |
| 141. | sudan | 15: [13, 6.5] | sudan al-bashir protesters | Sudanese_Revolution |
| 142. | country | 36: [13, 6.5] | country president minister | Minister-president |
| 143. | brexit | 3: [22, 5.5], 42: [30, 6.0] | brexit johnson prime | Boris_Johnson |
| 144. | military | 4: [10, 5.0], 29: [12, 6.0] | military u.s. president | List_of_presidents_of_the_United_States_by_military_service |
| 145. | made | 8: [12, 6.0] | made president india | President_of_India |
| 146. | max | 11: [12, 6.0] | max crash boeing | Boeing_737_MAX_groundings |
| 147. | russia | 13: [10, 5.0], 46: [12, 6.0] | russia russian putin | Opposition_to_Vladimir_Putin_in_Russia |
| 148. | extradition | 24: [24, 6.0] | extradition hong kong | 2019_Hong_Kong_extradition_bill |
| 149. | party | 27: [18, 6.0], 50: [10, 5.0] | party election minister | List_of_chief_ministers_of_Uttar_Pradesh |
| 150. | russian | 38: [12, 6.0], 51: [11, 5.5] | russian russia putin | Vladimir_Putin |
| 151. | france | 49: [12, 6.0] | france president macron | Emmanuel_Macron |
| 152. | crash | 11: [23, 5.75] | crash plane ethiopian | Ethiopian_Airlines_Flight_302 |
| 153. | vatican | 8: [11, 5.5] | vatican abuse church | Catholic_Church_sexual_abuse_cases |
| 154. | second | 9: [11, 5.5] | second president term | List_of_presidents_of_the_United_States_by_time_in_office |
| 155. | even | 9: [11, 5.5] | even country could | COVID-19_pandemic_by_country_and_territory |
| 156. | protesters | 23: [11, 5.5] | protesters hong kong | 2019–20_Hong_Kong_protests |
| 157. | world | 23: [16, 5.33], 47: [11, 5.5] | world leaders around | Around_the_World_in_Eighty_Days |
| 158. | former | 35: [11, 5.5] | former president minister | List_of_presidents_of_India |
| 159. | nuclear | 45: [11, 5.5] | nuclear iran north | Nuclear_program_of_Iran |
| 160. | prime | 20: [16, 5.33] | prime minister brexit | Timeline_of_Brexit |
| 161. | car | 3: [10, 5.0] | car crash woman | Charlottesville_car_attack |
| 162. | europe | 7: [10, 5.0] | europe european president | President_of_the_European_Union |
| 163. | south | 7: [10, 5.0] | south korea north | North_Korea–South_Korea_relations |
| 164. | airlines | 11: [20, 5.0] | airlines ethiopian flight | Ethiopian_Airlines_Flight_302 |
| 165. | campaign | 13: [10, 5.0] | campaign election minister | Political_campaign |
| 166. | british | 13: [10, 5.0] | british brexit minister | Brexit |
| 167. | investigation | 13: [10, 5.0] | investigation found u.s. | Special_Counsel_investigation_(2017–2019) |
| 168. | gay | 14: [10, 5.0] | gay rights brunei | LGBT_rights_in_Brunei |
| 169. | another | 15: [10, 5.0] | another president election | List_of_presidents_of_the_United_States |
| 170. | al-bashir | 15: [10, 5.0] | al-bashir sudan omar | Omar_al-Bashir |
| 171. | violence | 16: [10, 5.0] | violence police hong | 2019–20_Hong_Kong_protests |
| 172. | workers | 20: [10, 5.0] | workers aid people | Humanitarian_aid |
| 173. | chinese | 22: [10, 5.0] | chinese china hong | China_Unicom |
| 174. | accused | 22: [15, 5.0] | accused president former | Andrew_Johnson |
| 175. | rights | 28: [10, 5.0] | rights human women | Women's_rights_are_human_rights |
| 176. | killed | 31: [10, 5.0], 45: [10, 5.0] | killed people least | List_of_people_killed_for_being_transgender |
| 177. | tanker | 33: [10, 5.0] | tanker iran oil | National_Iranian_Tanker_Company |
| 178. | boris | 39: [20, 5.0] | boris johnson brexit | Premiership_of_Boris_Johnson |
| 179. | says | 44: [10, 5.0] | says president trump | Donald_Trump |
| 180. | evo | 46: [10, 5.0] | evo morales president | Evo_Morales |
| 181. | mr. | 46: [10, 5.0] | mr. trump president | Donald_Trump |
| 182. | government | 49: [15, 5.0] | government minister president | Minister-president |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | venezuela | 4: [18, inf] | venezuela maduro 's | Nicolás_Maduro |
| 2. | christchurch | 11: [26, inf] | christchurch attack zealand | Christchurch_mosque_shootings |
| 3. | dame | 16: [29, inf] | dame fire cathedral | Notre-Dame_de_Paris_fire |
| 4. | fire | 16: [14, inf] | fire dame police | Notre-Dame_de_Paris_fire |
| 5. | mugabe | 36: [10, inf] | mugabe robert 's | Robert_Mugabe |
| 6. | kurds | 41: [11, inf] | kurds syria trump | Autonomous_Administration_of_North_and_East_Syria |
| 7. | turkish | 41: [15, inf] | turkish syria us | Turkish_involvement_in_the_Syrian_civil_war |
| 8. | white | 50: [16, inf] | white island volcano | 2019_Whakaari_/_White_Island_eruption |
| 9. | island | 50: [16, inf] | island white volcano | Whakaari_/_White_Island |
| 10. | volcano | 50: [14, inf] | volcano white island | 2019_Whakaari_/_White_Island_eruption |
| 11. | zealand | 11: [13, 13.0], 45: [11, 5.5] | zealand 's ardern | Jacinda_Ardern |
| 12. | pacific | 33: [12, 12.0] | pacific australia climate | Oceania |
| 13. | g | 34: [11, 11.0] | g leaders trump | 46th_G7_summit |
| 14. | catalan | 42: [11, 11.0] | catalan independence trial | Trial_of_Catalonia_independence_leaders |
| 15. | syria | 41: [17, 8.5] | syria isis us | American-led_intervention_in_the_Syrian_Civil_War |
| 16. | attack | 11: [13, 6.5] | attack christchurch zealand | Christchurch_mosque_shootings |
| 17. | hong | 24: [17, 5.67] | hong kong protests | 2019–20_Hong_Kong_protests |
| 18. | kong | 24: [17, 5.67] | kong hong protests | 2019–20_Hong_Kong_protests |
| 19. | australia | 33: [11, 5.5] | australia 's says | Australia |
| 20. | – | 16: [10, 5.0] | – briefing 's | James_S._Brady_Press_Briefing_Room |
| 21. | hurricane | 36: [15, 5.0] | hurricane dorian 's | Hurricane_Dorian |
| 22. | dorian | 36: [15, 5.0] | dorian hurricane bahamas | Effects_of_Hurricane_Dorian_in_The_Bahamas |
