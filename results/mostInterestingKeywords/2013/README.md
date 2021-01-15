# Keywords with the highest 'interestingness' in 2013

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
| 1. | group | 2: [10, inf], 19: [21, 5.25], 30: [12, inf] | group syrian attack | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 2. | censorship | 2: [10, inf] | censorship china film | Film_censorship_in_China |
| 3. | newspaper | 2: [12, inf] | newspaper china chinese | List_of_newspapers_in_China |
| 4. | karzai | 2: [12, 6.0], 47: [14, inf] | karzai president hamid | Hamid_Karzai |
| 5. | chávez | 2: [11, inf], 10: [30, 10.0] | chávez hugo president | Death_of_Hugo_Chávez |
| 6. | held | 2: [13, 13.0], 16: [11, inf], 37: [11, 5.5], 47: [16, 5.33] | held american years | List_of_American_sportsperson-politicians |
| 7. | mali | 2: [11, inf] | mali french france | France–Mali_relations |
| 8. | arab | 3: [10, inf], 35: [10, inf] | arab emirates spring | United_Arab_Emirates |
| 9. | fighting | 3: [10, 5.0], 21: [14, inf] | fighting rebels syria | Belligerents_in_the_Syrian_Civil_War |
| 10. | forces | 3: [12, inf], 30: [10, inf], 50: [14, 14.0] | forces security government | Rhodesian_Security_Forces |
| 11. | prime | 3: [23, 5.75], 8: [13, inf] | prime minister former | List_of_prime_ministers_of_India |
| 12. | since | 3: [13, inf] | since first president | George_Washington |
| 13. | myanmar | 3: [12, inf], 12: [13, inf] | myanmar violence muslims | Persecution_of_Muslims_in_Myanmar |
| 14. | cameron | 3: [13, inf], 20: [12, inf] | cameron minister prime | David_Cameron |
| 15. | panetta | 3: [12, inf] | panetta defense secretary | Leon_Panetta |
| 16. | secretary | 3: [10, 5.0], 9: [11, inf], 21: [12, 12.0], 29: [14, 7.0], 35: [12, inf], 49: [10, 10.0] | secretary kerry state | John_Kerry |
| 17. | algerian | 3: [16, inf] | algerian hostage attack | In_Amenas_hostage_crisis |
| 18. | algeria | 3: [24, inf] | algeria hostage gas | In_Amenas_hostage_crisis |
| 19. | five | 4: [11, inf] | five years attack | Attack_on_Titan |
| 20. | -year-old | 4: [11, inf] | -year-old rape death | David_Carpenter |
| 21. | arts | 4: [10, inf] | arts week liberal | Liberal_arts_education |
| 22. | changes | 4: [10, inf] | changes china india | 2020_China–India_skirmishes |
| 23. | jaipur | 4: [15, inf] | jaipur literature festival | Jaipur_Literature_Festival |
| 24. | nuclear | 4: [17, inf], 14: [13, inf], 21: [11, 5.5] | nuclear iran north | Nuclear_program_of_Iran |
| 25. | south | 4: [10, inf], 7: [12, 6.0], 22: [12, 12.0], 26: [31, 15.5], 43: [14, inf] | south korea north | North_Korea–South_Korea_relations |
| 26. | fire | 4: [10, inf] | fire killed factory | Triangle_Shirtwaist_Factory_fire |
| 27. | protests | 4: [12, inf], 23: [18, 6.0] | protests government president | 2018–2021_Arab_protests |
| 28. | deadly | 4: [11, inf] | deadly people killed | Police_use_of_deadly_force_in_the_United_States |
| 29. | intelligence | 5: [10, inf], 28: [14, 7.0] | intelligence u.s. snowden | Edward_Snowden |
| 30. | allies | 5: [12, inf] | allies united states | Major_non-NATO_ally |
| 31. | bulgaria | 6: [10, inf] | bulgaria hezbollah european | 2012_Burgas_bus_bombing |
| 32. | ahmadinejad | 6: [10, inf] | ahmadinejad president mahmoud | Mahmoud_Ahmadinejad |
| 33. | berlusconi | 6: [10, inf], 31: [10, inf] | berlusconi silvio minister | Pier_Silvio_Berlusconi |
| 34. | year | 7: [11, 5.5], 25: [13, inf] | year last china | Chinese_New_Year |
| 35. | scotland | 7: [12, inf] | scotland yard britain | Scotland_Yard |
| 36. | foreign | 7: [11, inf], 36: [12, 6.0] | foreign minister syria | Ministry_of_Foreign_Affairs_and_Expatriates_(Syria) |
| 37. | pope | 7: [34, inf], 30: [15, 7.5] | pope francis vatican | Pope_Francis |
| 38. | benedict | 7: [21, inf] | benedict pope xvi | Resignation_of_Pope_Benedict_XVI |
| 39. | church | 7: [12, 12.0], 38: [13, inf] | church pope catholic | Catholic_Church |
| 40. | xvi | 7: [16, inf] | xvi pope benedict | Resignation_of_Pope_Benedict_XVI |
| 41. | korea | 7: [26, 13.0], 43: [10, 5.0], 47: [12, inf] | korea north south | North_Korea–South_Korea_relations |
| 42. | accused | 8: [11, inf] | accused rape case | Ajmer_rape_case |
| 43. | family | 8: [12, 6.0], 46: [10, 5.0], 50: [10, inf] | family china says | China |
| 44. | kerry | 9: [18, inf], 21: [22, 22.0], 29: [13, inf], 31: [11, 5.5], 44: [12, 6.0], 49: [14, inf] | kerry state secretary | John_Kerry |
| 45. | aid | 9: [12, 6.0], 41: [14, 7.0], 46: [22, inf] | aid syria syrian | Syrian_civil_war |
| 46. | cardinals | 10: [14, inf] | cardinals pope conclave | 2013_papal_conclave |
| 47. | filipino | 10: [10, inf] | filipino malaysian borneo | North_Borneo_dispute |
| 48. | sanctions | 10: [11, inf] | sanctions iran nuclear | Sanctions_against_Iran |
| 49. | river | 11: [15, 7.5], 18: [10, inf] | river china brahmaputra | Brahmaputra_River |
| 50. | rape | 11: [10, inf] | rape gang india | 2012_Delhi_gang_rape_and_murder |
| 51. | dead | 11: [12, inf], 46: [10, 5.0] | dead people least | List_of_rampage_killers |
| 52. | jail | 11: [10, inf] | jail court years | Supreme_Court_of_the_United_States |
| 53. | conclave | 11: [16, inf] | conclave pope vatican | 2013_papal_conclave |
| 54. | francis | 11: [17, inf] | francis pope vatican | Pope_Francis |
| 55. | visit | 11: [14, 14.0], 21: [10, 5.0], 23: [10, 5.0], 26: [25, inf], 30: [13, 13.0] | visit president obama | Barack_Obama |
| 56. | prison | 12: [15, 5.0], 17: [10, inf] | prison years former | Larry_Nassar |
| 57. | cyprus | 12: [22, inf] | cyprus bailout iht | List_of_largest_mergers_and_acquisitions |
| 58. | living | 12: [10, inf] | living people country | List_of_the_oldest_people_by_country |
| 59. | sri | 12: [10, inf] | sri lanka india | India–Sri_Lanka_relations |
| 60. | lanka | 12: [10, inf] | lanka sri government | Government_of_Sri_Lanka |
| 61. | even | 12: [11, 11.0], 44: [11, 11.0], 52: [11, inf] | even china syria | Syrian_civil_war |
| 62. | bill | 12: [11, inf] | bill parliament would | Fixed-term_Parliaments_Act_2011 |
| 63. | reported | 12: [10, inf] | reported killed least | Saudi_Arabian-led_intervention_in_Yemen |
| 64. | last | 13: [14, 7.0], 18: [15, 15.0], 25: [12, 6.0], 29: [11, inf] | last week year | ISO_week_date |
| 65. | berezovsky | 13: [13, inf] | berezovsky death boris | Boris_Berezovsky_(businessman) |
| 66. | hong | 13: [12, inf] | hong kong china | Hong_Kong |
| 67. | kong | 13: [12, inf] | kong hong china | Hong_Kong |
| 68. | election | 13: [12, 12.0], 24: [22, 7.33], 29: [10, inf], 31: [14, 7.0] | election vote president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 69. | debt | 14: [10, inf] | debt daughter crisis | 2012–2013_Cypriot_financial_crisis |
| 70. | daughter | 14: [12, inf] | daughter death chinese | The_Chinese_Botanist's_Daughters |
| 71. | april | 14: [21, inf] | april iht quick | Indigenous_peoples_of_the_Americas |
| 72. | workers | 14: [12, inf] | workers china killed | 2014_Vietnam_anti-China_protests |
| 73. | thatcher | 15: [22, inf] | thatcher margaret british | Premiership_of_Margaret_Thatcher |
| 74. | margaret | 15: [13, inf] | margaret thatcher british | Premiership_of_Margaret_Thatcher |
| 75. | germany | 15: [10, inf] | germany merkel chancellor | Angela_Merkel |
| 76. | opposition | 15: [12, inf] | opposition syrian president | Syrian_opposition |
| 77. | boston | 16: [23, inf] | boston marathon attack | Boston_Marathon_bombing |
| 78. | marathon | 16: [14, inf] | marathon boston bombings | Boston_Marathon_bombing |
| 79. | show | 17: [10, inf], 37: [10, inf] | show china government | List_of_countries_by_system_of_government |
| 80. | cases | 17: [10, inf] | cases rape india | Rape_in_India |
| 81. | building | 17: [10, inf] | building collapse bangladesh | 2013_Dhaka_garment_factory_collapse |
| 82. | bomb | 18: [10, 5.0], 44: [12, inf] | bomb killed attack | 1993_World_Trade_Center_bombing |
| 83. | irish | 18: [12, inf] | irish woman abortion | Abortion_in_the_Republic_of_Ireland |
| 84. | trying | 18: [10, inf], 38: [10, 5.0] | trying china president | President_pro_tempore_of_the_United_States_Senate |
| 85. | putin | 19: [12, inf], 23: [14, inf], 29: [13, inf], 51: [13, 6.5] | putin president vladimir | Vladimir_Putin |
| 86. | embassy | 19: [10, inf] | embassy american u.s. | 1998_United_States_embassy_bombings |
| 87. | union | 20: [11, inf] | union european europe | European_Union |
| 88. | middle | 20: [10, inf] | middle east class | Middle_East |
| 89. | class | 20: [10, inf] | class middle poor | Middle_class |
| 90. | lebanon | 21: [11, inf] | lebanon syrian hezbollah | Hezbollah |
| 91. | soldier | 21: [10, inf] | soldier attack killed | 2020_Camp_Taji_attacks |
| 92. | plans | 22: [10, inf] | plans china israel | China–Israel_relations |
| 93. | time | 22: [10, inf] | time first president | President_of_East_Timor |
| 94. | charges | 23: [12, inf] | charges court former | Impeachment |
| 95. | children | 23: [11, 11.0], 43: [13, inf] | children india killed | Navy_Day_(India) |
| 96. | plant | 23: [10, inf] | plant nuclear fukushima | Fukushima_Daiichi_Nuclear_Power_Plant |
| 97. | according | 24: [10, inf], 39: [13, 6.5] | according china people | China |
| 98. | sudan | 24: [13, inf], 51: [16, inf] | sudan south president | Vice_President_of_South_Sudan |
| 99. | mandela | 24: [14, 7.0], 26: [47, 23.5], 49: [42, inf] | mandela nelson south | Presidency_of_Nelson_Mandela |
| 100. | broadcaster | 24: [12, inf] | broadcaster state government | Public_broadcasting |
| 101. | crimes | 24: [11, inf] | crimes court humanity | Crimes_against_humanity |
| 102. | obama | 25: [30, 7.5], 35: [28, 5.6], 43: [13, inf] | obama president syria | Barack_Obama |
| 103. | britain | 25: [11, 11.0], 35: [18, inf] | britain cameron minister | David_Cameron |
| 104. | nelson | 26: [22, 22.0], 49: [24, inf] | nelson mandela south | Nelson_Mandela_Bay_Metropolitan_Municipality |
| 105. | mr. | 26: [12, inf] | mr. president conversation | Abraham_Lincoln |
| 106. | senegal | 26: [14, inf] | senegal obama president | List_of_international_presidential_trips_made_by_Barack_Obama |
| 107. | talks | 29: [16, 16.0], 37: [25, inf], 39: [11, 5.5] | talks iran peace | List_of_Middle_East_peace_proposals |
| 108. | bangladesh | 29: [10, inf] | bangladesh factory building | 2013_Dhaka_garment_factory_collapse |
| 109. | peace | 29: [14, inf], 37: [11, inf] | peace talks kerry | 2013–2014_Israeli–Palestinian_peace_talks |
| 110. | effort | 30: [11, inf] | effort syria president | Syrian_civil_war |
| 111. | least | 30: [16, inf], 51: [10, 10.0] | least people killed | List_of_people_killed_for_being_transgender |
| 112. | biden | 30: [11, inf], 49: [23, inf] | biden president vice | Joe_Biden |
| 113. | train | 30: [12, inf] | train driver rodman | Dennis_Rodman |
| 114. | attack | 30: [15, inf] | attack killed police | 2016_shooting_of_Dallas_police_officers |
| 115. | mugabe | 31: [12, inf] | mugabe zimbabwe president | Robert_Mugabe |
| 116. | zimbabwe | 31: [12, inf] | zimbabwe mugabe election | Robert_Mugabe |
| 117. | photojournalist | 34: [10, inf] | photojournalist rape mumbai | Shakti_Mills_gang_rape |
| 118. | among | 35: [11, inf] | among chinese china | China |
| 119. | administration | 35: [14, inf] | administration obama u.s. | Presidency_of_Barack_Obama |
| 120. | plan | 35: [12, inf], 37: [16, 8.0], 50: [10, 5.0] | plan syria president | American-led_intervention_in_the_Syrian_Civil_War |
| 121. | efforts | 36: [10, inf], 40: [11, inf], 46: [17, 8.5] | efforts president u.s. | President_of_the_United_States |
| 122. | agreement | 37: [10, inf] | agreement iran talks | Joint_Comprehensive_Plan_of_Action |
| 123. | may | 37: [11, inf] | may china day | May_Day |
| 124. | deal | 37: [11, inf], 39: [10, 5.0] | deal iran nuclear | Iran_nuclear_deal_framework |
| 125. | tuesday | 37: [10, inf] | tuesday iran north | Oliver_North |
| 126. | raid | 38: [11, inf] | raid killed officials | Killing_of_Osama_bin_Laden |
| 127. | holocaust | 39: [10, inf] | holocaust president iran | International_Conference_to_Review_the_Global_Vision_of_the_Holocaust |
| 128. | human | 41: [15, inf], 43: [11, inf] | human rights u.n. | United_Nations_Human_Rights_Council |
| 129. | professor | 42: [10, inf] | professor university china | Renmin_University_of_China |
| 130. | communist | 42: [12, inf] | communist party china | Chinese_Communist_Party |
| 131. | mayor | 42: [11, inf] | mayor toronto police | Mayor_of_Toronto |
| 132. | beijing | 42: [16, inf], 49: [10, 10.0] | beijing china chinese | Beijing |
| 133. | case | 43: [12, inf] | case rape court | 2012_Delhi_gang_rape_and_murder |
| 134. | reporter | 43: [11, inf] | reporter detained news | Journalist |
| 135. | tacloban | 46: [14, inf] | tacloban typhoon philippine | Tacloban |
| 136. | next | 47: [10, inf] | next minister year | List_of_prime_ministers_of_India |
| 137. | north | 47: [14, inf], 49: [18, 9.0] | north korea south | North_Korea–South_Korea_relations |
| 138. | protesters | 48: [11, inf] | protesters president police | List_of_police_violence_incidents_during_George_Floyd_protests |
| 139. | army | 48: [10, inf] | army military rebels | Military_of_Chad |
| 140. | vice | 49: [12, inf] | vice president biden | Joe_Biden |
| 141. | r. | 49: [10, inf] | r. biden president | Joe_Biden |
| 142. | memories | 49: [14, inf] | memories mandela nelson | Makgatho_Mandela |
| 143. | johannesburg | 49: [13, inf] | johannesburg mandela nelson | Makgatho_Mandela |
| 144. | bureau | 49: [12, inf] | bureau chief memories | Chief_of_the_Secret_Intelligence_Service |
| 145. | warned | 51: [11, inf] | warned president korea | 2009_imprisonment_of_American_journalists_by_North_Korea |
| 146. | aircraft | 51: [10, inf] | aircraft china air | Air_China |
| 147. | diplomat | 51: [12, inf] | diplomat united indian | Indian_Foreign_Service |
| 148. | rodman | 51: [12, inf] | rodman north korea | Dennis_Rodman |
| 149. | prosecutor | 51: [10, inf] | prosecutor case charges | Prosecutor |
| 150. | christmas | 52: [15, inf] | christmas holiday liu | Kung_Fu_Panda_Holiday |
| 151. | africa | 8: [10, 5.0], 26: [25, 25.0], 50: [15, 5.0] | africa south mandela | Nelson_Mandela |
| 152. | hugo | 10: [19, 19.0] | hugo chávez president | Hugo_Chávez |
| 153. | russia | 15: [10, 10.0], 25: [19, 19.0], 36: [15, 5.0], 51: [13, 6.5] | russia putin syria | Vladimir_Putin |
| 154. | relief | 46: [19, 19.0] | relief aid philippines | Typhoon_Haiyan |
| 155. | rights | 41: [16, 16.0], 43: [18, 18.0] | rights human china | Human_rights_in_China |
| 156. | say | 2: [18, 6.0], 14: [17, 17.0], 51: [14, 7.0] | say officials syria | Syrian_civil_war |
| 157. | hostages | 3: [17, 17.0] | hostages algerian algeria | Algerian_War |
| 158. | chinese | 42: [33, 16.5] | chinese china u.s. | China |
| 159. | hostage | 3: [16, 16.0] | hostage algeria french | In_Amenas_hostage_crisis |
| 160. | party | 8: [11, 5.5], 42: [16, 16.0] | party communist minister | Nepal_Communist_Party |
| 161. | international | 2: [11, 11.0], 10: [11, 5.5], 18: [15, 15.0] | international court syria | Syria |
| 162. | literature | 4: [15, 15.0] | literature jaipur festival | Jaipur_Literature_Festival |
| 163. | meeting | 5: [11, 5.5], 23: [15, 15.0], 41: [10, 10.0] | meeting president obama | Barack_Obama |
| 164. | many | 10: [11, 5.5], 45: [15, 15.0] | many people china | Chinese_people |
| 165. | air | 14: [15, 15.0] | air china defense | Republic_of_China_Air_Force |
| 166. | xi | 23: [15, 15.0] | xi china president | Xi_Jinping |
| 167. | brazil | 25: [13, 6.5], 30: [15, 15.0] | brazil protests president | 2013_protests_in_Brazil |
| 168. | israel | 16: [14, 14.0], 23: [13, 13.0] | israel syria iran | Iran–Israel_proxy_conflict |
| 169. | turkish | 23: [14, 14.0] | turkish turkey protests | Gezi_Park_protests |
| 170. | philippines | 46: [28, 14.0] | philippines typhoon china | Typhoon_Haiyan |
| 171. | venezuela | 10: [16, 8.0], 16: [13, 13.0] | venezuela chávez president | Hugo_Chávez |
| 172. | attacks | 16: [13, 13.0] | attacks killed least | List_of_Islamist_terrorist_attacks |
| 173. | jinping | 23: [13, 13.0] | jinping china xi | Xi_Jinping_Thought |
| 174. | world | 31: [10, 5.0], 47: [13, 13.0] | world china around | Around_the_World_in_Eighty_Days |
| 175. | argentina | 5: [12, 12.0] | argentina islands falkland | Falkland_Islands_sovereignty_dispute |
| 176. | security | 16: [12, 12.0], 41: [10, 5.0] | security forces officials | Rhodesian_Security_Forces |
| 177. | sexual | 18: [12, 12.0] | sexual india rape | Rape_in_India |
| 178. | june | 23: [24, 12.0] | june iht quick | Indigenous_peoples_of_the_Americas |
| 179. | tourists | 24: [12, 12.0] | tourists hezbollah india | Hezbollah |
| 180. | proposal | 37: [12, 12.0] | proposal syria would | Syrian_peace_process |
| 181. | near | 41: [12, 12.0] | near killed syria | Israeli–Syrian_ceasefire_line_incidents_during_the_Syrian_Civil_War |
| 182. | detained | 43: [12, 12.0] | detained china north | List_of_foreign_nationals_detained_in_North_Korea |
| 183. | chancellor | 44: [12, 12.0] | chancellor merkel angela | Angela_Merkel |
| 184. | iraq | 12: [23, 11.5] | iraq killed violence | Casualties_of_the_Iraq_War |
| 185. | activists | 2: [11, 11.0] | activists government greenpeace | Greenpeace |
| 186. | set | 5: [11, 11.0] | set government president | Student_government_president |
| 187. | crisis | 10: [10, 5.0], 19: [10, 5.0], 37: [11, 11.0] | crisis syria europe | European_migrant_crisis |
| 188. | delhi | 11: [10, 10.0], 30: [11, 11.0] | delhi rape india | 2012_Delhi_gang_rape_and_murder |
| 189. | chemical | 17: [22, 11.0], 34: [19, 9.5] | chemical syria weapons | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 190. | region | 18: [11, 11.0], 26: [15, 5.0] | region china security | Hong_Kong_national_security_law |
| 191. | coalition | 19: [11, 11.0] | coalition government minister | Coalition_government |
| 192. | free | 19: [11, 11.0] | free rebels president | Free_Syrian_Army |
| 193. | hezbollah | 21: [22, 11.0] | hezbollah syria syrian | Hezbollah |
| 194. | john | 21: [11, 11.0] | john kerry state | John_Kerry |
| 195. | used | 23: [11, 11.0] | used syria chemical | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 196. | china | 33: [11, 11.0] | china chinese north | North_China |
| 197. | xilai | 34: [11, 11.0] | xilai trial chinese | Bo_Xilai |
| 198. | angela | 44: [11, 11.0] | angela merkel chancellor | Angela_Merkel |
| 199. | tried | 44: [11, 11.0] | tried government president | President_(government_title) |
| 200. | economic | 45: [11, 11.0] | economic china president | China–Pakistan_Economic_Corridor |
| 201. | system | 46: [11, 11.0] | system china india | 2020_China–India_skirmishes |
| 202. | storm | 46: [11, 11.0] | storm china people | China |
| 203. | tendulkar | 46: [11, 11.0] | tendulkar final sachin | Sachin_Tendulkar |
| 204. | third | 48: [11, 11.0] | third north korea | North_Korea |
| 205. | journalists | 7: [10, 10.0] | journalists china news | Journalist |
| 206. | water | 11: [10, 10.0] | water plant nuclear | Nuclear_power_plant |
| 207. | growing | 11: [10, 10.0], 44: [10, 5.0] | growing china chinese | China |
| 208. | central | 12: [10, 10.0] | central african republic | Central_African_Republic |
| 209. | despite | 15: [10, 10.0] | despite says president | President_of_the_United_States |
| 210. | life | 18: [10, 10.0] | life china years | China_Life_Insurance_Company |
| 211. | still | 26: [10, 5.0], 46: [10, 10.0] | still syria president | Syria |
| 212. | relations | 29: [10, 10.0] | relations china north | China–North_Korea_relations |
| 213. | crackdown | 39: [10, 10.0] | crackdown egypt government | LGBT_rights_in_Egypt |
| 214. | another | 41: [10, 10.0] | another killed former | A_View_to_a_Kill |
| 215. | weeks | 47: [10, 10.0] | weeks two president | Two_Weeks_(The_Office) |
| 216. | open | 48: [10, 10.0] | open china president | President_of_the_Republic_of_China |
| 217. | west | 49: [10, 10.0] | west bank palestinian | Palestinian_territories |
| 218. | thousands | 50: [10, 10.0] | thousands people tens | Ten_thousand_years |
| 219. | power | 18: [19, 9.5] | power president china | President_of_the_Republic_of_China |
| 220. | court | 12: [25, 5.0], 43: [18, 9.0] | court supreme former | Supreme_Court_of_the_United_States |
| 221. | strike | 35: [27, 9.0] | strike syria drone | Drone_strike |
| 222. | public | 7: [12, 6.0], 25: [17, 8.5] | public president china | President_of_the_People's_Republic_of_China |
| 223. | philippine | 46: [17, 8.5] | philippine typhoon city | Typhoon_Haiyan |
| 224. | program | 47: [17, 8.5] | program nuclear iran | Nuclear_program_of_Iran |
| 225. | afghan | 14: [16, 8.0], 16: [11, 5.5], 47: [16, 5.33] | afghan afghanistan taliban | War_in_Afghanistan_(2001–present) |
| 226. | timbuktu | 5: [15, 7.5] | timbuktu mali french | Timbuktu |
| 227. | official | 9: [11, 5.5], 34: [10, 5.0], 49: [15, 7.5] | official chinese china | History_of_China |
| 228. | home | 12: [15, 7.5], 37: [10, 5.0], 44: [11, 5.5] | home president china | List_of_presidents_of_China |
| 229. | violence | 17: [15, 7.5] | violence killed people | List_of_people_killed_for_being_transgender |
| 230. | brotherhood | 27: [15, 7.5] | brotherhood muslim egypt | Muslim_Brotherhood_in_Egypt |
| 231. | killed | 33: [15, 7.5], 44: [14, 7.0] | killed people least | Persecution_of_Hazara_people_in_Quetta |
| 232. | former | 34: [15, 7.5] | former president minister | List_of_presidents_of_India |
| 233. | europe | 43: [15, 7.5] | europe european iht | Free_trade_areas_in_Europe |
| 234. | haiyan | 46: [15, 7.5] | haiyan typhoon philippines | Typhoon_Haiyan |
| 235. | typhoon | 46: [36, 7.2] | typhoon philippines haiyan | Typhoon_Haiyan |
| 236. | woman | 2: [14, 7.0] | woman rape death | Rape_in_India |
| 237. | afghanistan | 7: [14, 7.0], 37: [20, 5.0] | afghanistan afghan taliban | Taliban |
| 238. | says | 17: [21, 7.0], 31: [24, 6.0] | says president syria | Syrian_civil_war |
| 239. | mohamed | 27: [21, 7.0] | mohamed morsi president | Mohamed_Morsi |
| 240. | site | 34: [14, 7.0] | site nuclear attack | Nuclear_football |
| 241. | four | 37: [14, 7.0] | four people years | Gettysburg_Address |
| 242. | european | 6: [13, 6.5], 27: [10, 5.0] | european union europe | European_Union |
| 243. | indian | 7: [13, 6.5], 33: [10, 5.0] | indian india day | Republic_Day_(India) |
| 244. | iran | 11: [13, 6.5] | iran nuclear president | Nuclear_program_of_Iran |
| 245. | mubarak | 34: [13, 6.5] | mubarak president hosni | Hosni_Mubarak |
| 246. | trial | 34: [13, 6.5], 49: [10, 5.0] | trial court former | Nuremberg_trials |
| 247. | capital | 49: [13, 6.5] | capital city people | Capital_city |
| 248. | gang | 2: [12, 6.0] | gang rape delhi | 2012_Delhi_gang_rape_and_murder |
| 249. | found | 22: [12, 6.0] | found bodies officials | Bog_body |
| 250. | surveillance | 24: [12, 6.0], 43: [10, 5.0] | surveillance snowden u.s. | Edward_Snowden |
| 251. | taliban | 25: [20, 5.0], 30: [12, 6.0], 36: [10, 5.0] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 252. | killing | 30: [12, 6.0] | killing people least | Mass_killings_under_communist_regimes |
| 253. | weapons | 34: [12, 6.0] | weapons syria chemical | Syria_chemical_weapons_program |
| 254. | could | 41: [12, 6.0] | could syria iran | Russia–Syria–Iran–Iraq_coalition |
| 255. | jr. | 49: [12, 6.0] | jr. biden joseph | Joe_Biden |
| 256. | military | 50: [18, 6.0] | military syria u.s. | American-led_intervention_in_the_Syrian_Civil_War |
| 257. | merkel | 44: [17, 5.67] | merkel chancellor angela | Angela_Merkel |
| 258. | protest | 2: [11, 5.5] | protest government day | 1971_May_Day_protests |
| 259. | dozens | 5: [11, 5.5] | dozens killed people | The_Dozens |
| 260. | months | 11: [11, 5.5], 45: [11, 5.5] | months two government | Month |
| 261. | damascus | 13: [11, 5.5] | damascus syria syrian | Damascus |
| 262. | flu | 14: [11, 5.5] | flu china bird | Avian_influenza |
| 263. | america | 22: [11, 5.5] | america latin u.s. | Latin_America–United_States_relations |
| 264. | vote | 24: [11, 5.5] | vote election president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 265. | political | 34: [11, 5.5] | political president party | Political_parties_in_the_United_States |
| 266. | arrested | 34: [11, 5.5] | arrested police leader | Violence_and_controversies_during_the_George_Floyd_protests |
| 267. | nations | 34: [11, 5.5] | nations united u.n. | Headquarters_of_the_United_Nations |
| 268. | militants | 36: [11, 5.5] | militants pakistan mali | Mali_War |
| 269. | part | 39: [11, 5.5] | part effort united | Effort |
| 270. | german | 44: [11, 5.5] | german merkel chancellor | Angela_Merkel |
| 271. | gay | 50: [11, 5.5] | gay marriage rights | Same-sex_marriage |
| 272. | leaders | 52: [11, 5.5] | leaders president egypt | List_of_presidents_of_Egypt |
| 273. | states | 47: [16, 5.33] | states united u.s. | U.S._state |
| 274. | u.s. | 51: [21, 5.25] | u.s. united american | United_States |
| 275. | amid | 4: [10, 5.0] | amid korea china | COVID-19_pandemic_in_North_Korea |
| 276. | egypt | 5: [15, 5.0], 25: [10, 5.0] | egypt morsi president | Mohamed_Morsi |
| 277. | veterans | 5: [10, 5.0] | veterans military veteran | Veteran |
| 278. | sentenced | 5: [10, 5.0] | sentenced years court | List_of_longest_prison_sentences |
| 279. | control | 7: [10, 5.0] | control government president | Divided_government_in_the_United_States |
| 280. | wednesday | 7: [10, 5.0] | wednesday government nuclear | Black_Wednesday |
| 281. | state | 9: [15, 5.0] | state kerry secretary | John_Kerry |
| 282. | province | 9: [10, 5.0] | province killed china | Yunnan |
| 283. | papal | 11: [10, 5.0] | papal conclave pope | Papal_conclave |
| 284. | israelis | 12: [10, 5.0] | israelis israel obama | Israel–United_States_relations |
| 285. | monday | 13: [10, 5.0] | monday president china | Black_Monday |
| 286. | editor | 14: [10, 5.0] | editor marcus mabry | Filles_de_Kilimanjaro |
| 287. | ethnic | 14: [10, 5.0] | ethnic myanmar china | Chinese_people_in_Myanmar |
| 288. | charged | 15: [10, 5.0] | charged former president | President_of_the_United_States |
| 289. | morsi | 27: [35, 5.0] | morsi president mohamed | Mohamed_Morsi |
| 290. | thursday | 34: [10, 5.0] | thursday president day | Black_Friday_(shopping) |
| 291. | way | 36: [10, 5.0] | way north korea | North_Korea |
| 292. | ban | 37: [10, 5.0] | ban government russia | Kaspersky_bans_and_allegations_of_Russian_government_ties |
| 293. | away | 46: [10, 5.0] | away women chinese | Women_in_China |
| 294. | civil | 48: [10, 5.0] | civil syria syrian | Syrian_civil_war |
| 295. | role | 49: [10, 5.0] | role military president | Powers_of_the_president_of_the_United_States |
| 296. | death | 49: [10, 5.0] | death killed attack | Crocodile_attack |
| 297. | joseph | 49: [10, 5.0] | joseph biden jr. | Joe_Biden |
| 298. | forced | 51: [10, 5.0] | forced government china | Forced_evictions_in_China |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | algeria | 3: [19, inf] | algeria hostage crisis | In_Amenas_hostage_crisis |
| 2. | algerian | 3: [13, inf] | algerian hostage crisis | In_Amenas_hostage_crisis |
| 3. | benedict | 7: [17, inf] | benedict pope 's | Pope_Benedict_XVI |
| 4. | oscar | 7: [14, inf] | oscar pistorius murder | Oscar_Pistorius |
| 5. | pistorius | 7: [14, inf] | pistorius oscar murder | Oscar_Pistorius |
| 6. | francis | 11: [29, inf] | francis pope 's | Pope_Francis |
| 7. | bank | 12: [10, inf] | bank west 's | West_Bank |
| 8. | boris | 12: [11, inf] | boris berezovsky 's | Boris_Berezovsky_(businessman) |
| 9. | berezovsky | 12: [11, inf] | berezovsky boris death | Boris_Berezovsky_(businessman) |
| 10. | rudd | 26: [10, inf] | rudd kevin 's | Kevin_Rudd |
| 11. | crash | 30: [13, inf] | crash train spanish | List_of_rail_accidents_in_Spain |
| 12. | gibraltar | 32: [12, inf] | gibraltar spain row | Status_of_Gibraltar |
| 13. | miranda | 34: [23, inf] | miranda david detention | David_Miranda_(politician) |
| 14. | detention | 34: [15, inf] | detention miranda david | David_Miranda_(politician) |
| 15. | chemical | 34: [12, inf] | chemical weapons syria | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 16. | weapons | 34: [10, inf] | weapons chemical syria | Use_of_chemical_weapons_in_the_Syrian_Civil_War |
| 17. | g | 36: [11, inf] | g summit tax | 45th_G7_summit |
| 18. | nuclear | 45: [13, inf] | nuclear iran deal | Iran_nuclear_deal_framework |
| 19. | typhoon | 45: [12, inf] | typhoon haiyan philippines | Typhoon_Haiyan |
| 20. | haiyan | 45: [12, inf] | haiyan typhoon philippines | Typhoon_Haiyan |
| 21. | indonesia | 47: [12, inf] | indonesia spying australia | Australia–Indonesia_spying_scandal |
| 22. | nelson | 49: [34, inf] | nelson mandela 's | Death_of_Nelson_Mandela |
| 23. | mandela | 49: [50, inf] | mandela nelson 's | Nelson_Mandela |
| 24. | memorial | 50: [13, inf] | memorial mandela nelson | Death_of_Nelson_Mandela |
| 25. | mikhail | 51: [10, inf] | mikhail khodorkovsky putin | Mikhail_Khodorkovsky |
| 26. | khodorkovsky | 51: [10, inf] | khodorkovsky mikhail putin | Mikhail_Khodorkovsky |
| 27. | pope | 7: [30, 30.0], 11: [39, 6.5] | pope francis 's | Pope_Francis |
| 28. | egypt | 27: [32, 5.33], 33: [23, 23.0] | egypt 's morsi | Mohamed_Morsi |
| 29. | hugo | 10: [17, 17.0] | hugo chávez venezuela | Hugo_Chávez |
| 30. | crisis | 3: [16, 16.0] | crisis syria hostage | Iran_hostage_crisis |
| 31. | syria | 22: [27, 6.75], 30: [16, 16.0], 34: [16, 16.0] | syria 's chemical | 2018_missile_strikes_against_Syria |
| 32. | refugees | 30: [16, 16.0] | refugees 's syrian | Refugees_of_the_Syrian_Civil_War |
| 33. | british | 35: [13, 13.0] | british woman 's | The_Leech_Woman |
| 34. | kenya | 39: [13, 13.0] | kenya 's attack | Westgate_shopping_mall_attack |
| 35. | police | 49: [13, 13.0] | police 's arrest | Arrest |
| 36. | iran | 24: [12, 6.0], 45: [12, 12.0] | iran nuclear 's | Nuclear_program_of_Iran |
| 37. | train | 30: [12, 12.0] | train crash spanish | Santiago_de_Compostela_derailment |
| 38. | intervention | 35: [12, 12.0] | intervention syria 's | Russian_military_intervention_in_the_Syrian_Civil_War |
| 39. | putin | 51: [12, 12.0] | putin vladimir 's | Vladimir_Putin |
| 40. | chávez | 10: [23, 11.5] | chávez hugo venezuela | Hugo_Chávez |
| 41. | gay | 13: [11, 11.0] | gay marriage rights | Same-sex_marriage |
| 42. | marriage | 13: [11, 11.0] | marriage gay same-sex | Same-sex_marriage_in_the_United_States |
| 43. | bangladesh | 17: [11, 11.0] | bangladesh factory collapse | 2013_Dhaka_garment_factory_collapse |
| 44. | peace | 25: [11, 11.0] | peace talks middle | List_of_Middle_East_peace_proposals |
| 45. | south | 49: [10, 10.0] | south africa african | South_Africa |
| 46. | hostage | 3: [18, 9.0] | hostage crisis algerian | In_Amenas_hostage_crisis |
| 47. | bailout | 12: [17, 8.5] | bailout cyprus 's | 2012–2013_Cypriot_financial_crisis |
| 48. | david | 34: [21, 7.0] | david cameron miranda | Lin-Manuel_Miranda |
| 49. | iraq | 11: [11, 5.5] | iraq years still | Iraq |
| 50. | deal | 47: [16, 5.33] | deal iran nuclear | Iran_nuclear_deal_framework |
| 51. | cyprus | 12: [37, 5.29] | cyprus bailout crisis | 2012–2013_Cypriot_financial_crisis |
| 52. | maduro | 16: [10, 5.0] | maduro nicolás venezuela | Nicolás_Maduro_Guerra |
| 53. | protests | 23: [10, 5.0] | protests turkey 's | Gezi_Park_protests |
| 54. | court | 34: [10, 5.0] | court supreme 's | Supreme_Court_of_the_United_States |
