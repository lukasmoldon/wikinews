# Keywords with the highest 'interestingness' in 2014

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
| 1. | syrian | 2: [10, inf], 35: [13, 13.0] | syrian syria government | Syrian_Interim_Government |
| 2. | oil | 2: [11, inf], 49: [11, inf] | oil china south | South_China_Sea |
| 3. | foreign | 2: [10, inf] | foreign minister china | Foreign_Minister_of_the_People's_Republic_of_China |
| 4. | north | 2: [11, inf], 6: [16, 8.0], 17: [10, 5.0], 36: [11, inf] | north korea south | North_Korea–South_Korea_relations |
| 5. | including | 3: [12, inf] | including people killed | List_of_people_killed_for_being_transgender |
| 6. | human | 3: [10, 10.0], 12: [15, inf] | human rights united | Universal_Declaration_of_Human_Rights |
| 7. | least | 3: [10, inf], 31: [10, 10.0], 35: [13, 13.0] | least people killed | List_of_people_killed_for_being_transgender |
| 8. | olympics | 6: [11, inf] | olympics sochi winter | 2014_Winter_Olympics |
| 9. | round | 7: [11, inf] | round talks first | Polish_Round_Table_Agreement |
| 10. | many | 8: [13, 6.5], 17: [12, inf], 28: [11, 5.5], 48: [13, 6.5] | many china government | Politics_of_China |
| 11. | young | 8: [10, 10.0], 21: [15, inf] | young people hong | Hong_Jin-young |
| 12. | crimea | 9: [22, inf] | crimea russia ukraine | Annexation_of_Crimea_by_the_Russian_Federation |
| 13. | saturday | 10: [12, inf] | saturday people least | Saturday_Night_Massacre |
| 14. | john | 10: [11, inf], 28: [13, inf] | john kerry state | John_Kerry |
| 15. | women | 10: [18, inf], 39: [14, 7.0] | women rights sexual | Women's_rights |
| 16. | last | 10: [12, inf], 32: [12, 6.0], 49: [11, 5.5] | last week month | ISO_week_date |
| 17. | secretary | 10: [11, 5.5], 28: [14, inf] | secretary kerry state | John_Kerry |
| 18. | kerry | 10: [17, 8.5], 28: [19, inf] | kerry state secretary | John_Kerry |
| 19. | plane | 11: [18, 6.0], 29: [14, inf] | plane malaysia airlines | Malaysia_Airlines_Flight_370 |
| 20. | nuclear | 12: [13, inf], 45: [11, 11.0] | nuclear iran talks | Joint_Comprehensive_Plan_of_Action |
| 21. | run | 13: [10, inf] | run party president | Cory_Booker_2020_presidential_campaign |
| 22. | israel | 14: [14, inf], 28: [27, 5.4] | israel gaza israeli | Gaza–Israel_conflict |
| 23. | series | 14: [10, inf] | series china attacks | School_attacks_in_China |
| 24. | beijing | 15: [15, inf], 40: [20, 5.0] | beijing china hong | Time_in_China |
| 25. | girlfriend | 15: [10, inf] | girlfriend pistorius oscar | Trial_of_Oscar_Pistorius |
| 26. | top | 15: [15, inf], 24: [10, inf] | top china official | China |
| 27. | days | 16: [11, inf] | days two ukraine | Ukraine_International_Airlines_Flight_752 |
| 28. | sanctions | 16: [11, inf] | sanctions russia ukraine | International_sanctions_during_the_Ukrainian_crisis |
| 29. | ferry | 16: [18, inf] | ferry south korean | Sinking_of_MV_Sewol |
| 30. | sinking | 16: [11, inf] | sinking ferry south | Sinking_of_MV_Sewol |
| 31. | putin | 16: [16, 5.33], 49: [10, inf] | putin president russia | Vladimir_Putin |
| 32. | xinjiang | 18: [12, inf] | xinjiang region china | Xinjiang |
| 33. | train | 18: [12, inf] | train station kunming | 2014_Kunming_attack |
| 34. | vietnam | 19: [14, inf] | vietnam china chinese | China–Vietnam_relations |
| 35. | deal | 21: [10, inf] | deal iran nuclear | Iran_nuclear_deal_framework |
| 36. | possible | 21: [11, inf] | possible china iran | China–Iran_relations |
| 37. | law | 21: [10, 10.0], 43: [12, inf] | law china court | Chinese_law |
| 38. | thai | 21: [12, inf] | thai thailand military | Royal_Thai_Armed_Forces |
| 39. | thailand | 21: [10, inf] | thailand military thai | Royal_Thai_Armed_Forces |
| 40. | pakistan | 21: [11, inf], 41: [12, 12.0] | pakistan pakistani taliban | Tehrik-i-Taliban_Pakistan |
| 41. | pope | 21: [11, 11.0], 28: [10, inf], 33: [10, 10.0] | pope francis vatican | Pope_Francis |
| 42. | union | 22: [14, inf] | union european ukraine | Ukraine–European_Union_relations |
| 43. | plan | 23: [10, inf] | plan would government | United_States_federal_government_continuity_of_operations |
| 44. | sgt | 23: [15, inf] | sgt bergdahl bowe | Bowe_Bergdahl |
| 45. | assault | 24: [19, inf] | assault sexual militants | Harvey_Weinstein_sexual_abuse_cases |
| 46. | woman | 24: [10, 10.0], 26: [11, inf], 49: [15, 15.0] | woman death women | Trans_woman |
| 47. | mosul | 24: [13, inf] | mosul iraq militants | Battle_of_Mosul_(2016–17) |
| 48. | japan | 24: [14, inf] | japan china minister | China–Japan_relations |
| 49. | baghdad | 24: [16, inf], 26: [10, 5.0] | baghdad iraq iraqi | Baghdad |
| 50. | abdullah | 25: [12, inf] | abdullah afghan candidate | Abdullah_Abdullah |
| 51. | suspect | 25: [12, inf] | suspect killing benghazi | 2012_Benghazi_attack |
| 52. | benghazi | 25: [11, inf] | benghazi attack libya | 2012_Benghazi_attack |
| 53. | helped | 26: [11, inf] | helped president putin | Vladimir_Putin |
| 54. | french | 27: [10, inf], 30: [10, inf], 47: [11, 5.5] | french france president | President_of_France |
| 55. | home | 28: [11, inf], 49: [11, 11.0] | home china return | Mainland_Travel_Permit_for_Hong_Kong_and_Macao_Residents |
| 56. | troops | 28: [11, 5.5], 34: [11, 5.5], 38: [11, inf] | troops ukraine u.s. | Internal_Troops_of_Ukraine |
| 57. | gaza | 28: [23, inf] | gaza israel israeli | Gaza–Israel_conflict |
| 58. | shot | 29: [14, inf] | shot israeli killed | List_of_Israeli_assassinations |
| 59. | downing | 29: [13, inf] | downing ukraine russia | Russo-Ukrainian_War |
| 60. | malaysia | 29: [22, inf] | malaysia airlines flight | Malaysia_Airlines_Flight_370 |
| 61. | airlines | 29: [19, inf] | airlines malaysia flight | Malaysia_Airlines_Flight_370 |
| 62. | jet | 29: [21, inf] | jet malaysia search | Search_for_Malaysia_Airlines_Flight_370 |
| 63. | food | 30: [10, inf] | food china aid | Aid |
| 64. | site | 30: [21, 21.0], 44: [15, 15.0], 50: [10, inf] | site crash police | Germanwings_Flight_9525 |
| 65. | corruption | 31: [13, inf] | corruption china former | Corruption_in_China |
| 66. | head | 31: [11, inf] | head china former | Head_of_the_former_Chinese_imperial_clan |
| 67. | african | 32: [11, inf] | african south central | Central_Africa |
| 68. | premier | 32: [10, inf] | premier minister prime | Prime_minister |
| 69. | children | 32: [11, inf] | children killed china | 1994_Karamay_fire |
| 70. | convoy | 33: [13, inf] | convoy ukraine aid | Aid_Convoy |
| 71. | opposition | 33: [10, inf] | opposition leader government | Leader_of_the_Opposition_(India) |
| 72. | foley | 34: [12, inf] | foley james journalist | James_Foley_(journalist) |
| 73. | northern | 35: [10, inf] | northern iraq militants | Northern_Iraq_offensive_(June_2014) |
| 74. | europe | 35: [10, inf] | europe russia european | European_Russia |
| 75. | scotland | 37: [10, inf] | scotland independence vote | 2014_Scottish_independence_referendum |
| 76. | nearly | 37: [10, inf] | nearly two years | I'll_Be_Gone_in_the_Dark |
| 77. | arab | 37: [11, 5.5], 39: [10, inf], 47: [13, inf] | arab united spring | Arab_Spring |
| 78. | – | 38: [10, inf] | – general assembly | United_Nations_General_Assembly |
| 79. | general | 38: [20, inf] | general united nations | Secretary-General_of_the_United_Nations |
| 80. | assembly | 38: [19, inf] | assembly general united | United_Nations_General_Assembly |
| 81. | life | 39: [15, inf] | life china chinese | China_Life_Insurance_Company |
| 82. | reported | 39: [10, inf] | reported china news | Fox_News |
| 83. | protesters | 40: [38, 7.6], 47: [11, inf] | protesters hong kong | 2019–20_Hong_Kong_protests |
| 84. | demonstrations | 40: [18, inf] | demonstrations hong kong | 1967_Hong_Kong_riots |
| 85. | communist | 40: [13, inf] | communist party china | Chinese_Communist_Party |
| 86. | water | 40: [10, inf] | water china iraq | Iraq |
| 87. | kobani | 41: [10, inf] | kobani syrian islamic | Siege_of_Kobanî |
| 88. | nurse | 41: [13, inf] | nurse ebola spanish | Ebola_virus_cases_in_the_United_States |
| 89. | might | 41: [10, inf] | might china american | Chinese_Americans |
| 90. | toll | 42: [11, inf] | toll death killed | List_of_wars_by_death_toll |
| 91. | tunisia | 43: [10, inf] | tunisia arab country | Tunisia |
| 92. | soldier | 43: [10, inf] | soldier killed american | Soldier_(1998_American_film) |
| 93. | ottawa | 43: [10, inf] | ottawa gunman police | 2014_shootings_at_Parliament_Hill,_Ottawa |
| 94. | criticism | 44: [10, inf] | criticism president government | Criticism_of_the_Israeli_government |
| 95. | burkina | 44: [11, inf] | burkina faso president | List_of_heads_of_state_of_Burkina_Faso |
| 96. | faso | 44: [11, inf] | faso burkina president | COVID-19_pandemic_in_Burkina_Faso |
| 97. | camp | 48: [10, inf], 50: [10, inf] | camp hong kong | Pro-Beijing_camp_(Hong_Kong) |
| 98. | internet | 49: [10, inf] | internet chinese china | Internet_censorship_in_China |
| 99. | fight | 49: [11, inf] | fight state isis | Islamic_State_of_Iraq_and_the_Levant |
| 100. | iranian | 49: [10, inf] | iranian iran nuclear | Nuclear_program_of_Iran |
| 101. | typhoon | 49: [11, inf] | typhoon storm haiyan | Typhoon_Haiyan |
| 102. | senate | 50: [10, inf] | senate report committee | Senate_Intelligence_Committee_report_on_CIA_torture |
| 103. | c.i.a | 50: [22, inf] | c.i.a report torture | Senate_Intelligence_Committee_report_on_CIA_torture |
| 104. | climate | 50: [13, inf] | climate china change | Climate_change_in_China |
| 105. | sydney | 51: [11, inf] | sydney gunman cafe | Lindt_Cafe_siege |
| 106. | sony | 51: [14, inf] | sony north korea | Sony_Pictures_hack |
| 107. | cuba | 51: [31, inf] | cuba u.s. relations | Cuba–United_States_relations |
| 108. | relations | 51: [13, inf] | relations president china | China–United_States_relations |
| 109. | christmas | 52: [19, inf] | christmas international herald | Christmas |
| 110. | government | 2: [22, 22.0] | government minister officials | Minister_(government) |
| 111. | rights | 3: [11, 11.0], 12: [20, 6.67], 30: [10, 5.0], 37: [13, 6.5], 39: [21, 10.5], 43: [22, 22.0] | rights human united | Human_rights |
| 112. | could | 5: [14, 14.0], 25: [12, 6.0], 29: [14, 14.0], 41: [18, 18.0], 46: [18, 18.0] | could president china | President_of_China |
| 113. | recent | 8: [10, 5.0], 26: [16, 16.0] | recent china years | China |
| 114. | speech | 38: [16, 16.0] | speech president united | United_States_free_speech_exceptions |
| 115. | health | 14: [15, 15.0], 31: [11, 5.5] | health ebola world | Western_African_Ebola_virus_epidemic |
| 116. | charged | 8: [12, 6.0], 49: [14, 14.0] | charged court president | Impeachment |
| 117. | among | 12: [14, 14.0] | among china officials | List_of_Righteous_Among_the_Nations_by_country |
| 118. | hong | 17: [13, 6.5], 23: [14, 7.0], 35: [14, 14.0], 39: [16, 8.0], 40: [99, 6.19] | hong kong protests | 2019–20_Hong_Kong_protests |
| 119. | security | 18: [14, 14.0] | security council united | United_Nations_Security_Council |
| 120. | aid | 20: [13, 6.5], 37: [10, 10.0], 49: [14, 14.0] | aid ukraine syria | Wagner_Group |
| 121. | britain | 38: [14, 14.0], 47: [11, 11.0] | britain british minister | Prime_Minister_of_the_United_Kingdom |
| 122. | missing | 11: [27, 13.5] | missing search malaysia | Malaysia_Airlines_Flight_370 |
| 123. | ukraine | 8: [26, 13.0] | ukraine russia president | President_of_Ukraine |
| 124. | kong | 17: [13, 6.5], 35: [13, 13.0], 39: [16, 8.0], 40: [93, 5.81] | kong hong protests | 2019–20_Hong_Kong_protests |
| 125. | years | 32: [13, 13.0] | years china ago | China |
| 126. | another | 3: [12, 12.0] | another former president | Living_presidents_of_the_United_States |
| 127. | afghanistan | 5: [10, 5.0], 14: [12, 12.0], 34: [10, 5.0] | afghanistan afghan taliban | Taliban |
| 128. | hagel | 15: [12, 12.0] | hagel secretary defense | Chuck_Hagel |
| 129. | crackdown | 23: [12, 12.0] | crackdown china tiananmen | 1989_Tiananmen_Square_protests |
| 130. | found | 30: [12, 12.0] | found police china | People's_Armed_Police |
| 131. | near | 35: [10, 10.0], 38: [12, 12.0] | near border officials | United_States_Border_Patrol_interior_checkpoints |
| 132. | support | 43: [12, 12.0] | support president hong | Hong_Kong_Human_Rights_and_Democracy_Act |
| 133. | militants | 49: [12, 12.0] | militants iraq syria | Islamic_State_of_Iraq_and_the_Levant |
| 134. | held | 3: [10, 10.0], 8: [11, 11.0] | held american u.s. | United_States |
| 135. | accused | 4: [11, 11.0], 34: [12, 6.0] | accused trial government | Trial |
| 136. | politics | 8: [11, 11.0] | politics party former | Political_parties_in_the_United_States |
| 137. | mexico | 8: [11, 11.0] | mexico students police | 2014_Iguala_mass_kidnapping |
| 138. | u.n. | 10: [11, 11.0], 30: [11, 11.0], 35: [12, 6.0], 38: [28, 7.0] | u.n. united nations | United_Nations |
| 139. | amid | 11: [11, 11.0] | amid government minister | Government_of_Maharashtra |
| 140. | malaysian | 11: [22, 11.0] | malaysian search malaysia | Malaysia |
| 141. | dead | 12: [11, 11.0] | dead people left | Left_4_Dead |
| 142. | political | 15: [13, 6.5], 36: [11, 11.0] | political president party | Political_party |
| 143. | british | 24: [10, 5.0], 26: [11, 11.0] | british britain minister | Prime_Minister_of_the_United_Kingdom |
| 144. | cup | 28: [11, 11.0] | cup world brazil | 2014_FIFA_World_Cup |
| 145. | cases | 39: [11, 11.0] | cases ebola health | Ebola_virus_cases_in_the_United_States |
| 146. | west | 48: [11, 11.0] | west bank israeli | Israeli_West_Bank_barrier |
| 147. | bank | 48: [11, 11.0] | bank west israeli | Israeli_West_Bank_barrier |
| 148. | elections | 49: [11, 11.0] | elections party minister | Janata_Party |
| 149. | world | 2: [10, 10.0], 28: [18, 6.0], 52: [13, 6.5] | world health china | World_Health_Organization |
| 150. | western | 3: [10, 10.0], 39: [10, 5.0] | western china russia | China–Russia_border |
| 151. | islamist | 5: [10, 10.0] | islamist militants group | Islamic_extremism |
| 152. | part | 5: [10, 10.0], 14: [11, 5.5] | part government state | State_governments_of_the_United_States |
| 153. | region | 9: [10, 10.0] | region xinjiang china | Xinjiang |
| 154. | council | 10: [10, 10.0], 38: [10, 5.0] | council security united | United_Nations_Security_Council |
| 155. | made | 12: [10, 10.0], 39: [11, 5.5] | made president china | President_of_the_People's_Republic_of_China |
| 156. | oscar | 15: [10, 10.0] | oscar pistorius trial | Trial_of_Oscar_Pistorius |
| 157. | egypt | 18: [12, 6.0], 44: [10, 10.0] | egypt president government | President_of_Egypt |
| 158. | sunday | 21: [10, 10.0] | sunday ukraine election | Next_Ukrainian_parliamentary_election |
| 159. | army | 21: [11, 5.5], 31: [10, 10.0] | army soldiers military | United_States_Army |
| 160. | show | 23: [10, 10.0] | show china says | China |
| 161. | iraqi | 24: [20, 10.0] | iraqi iraq militants | Islamic_State_of_Iraq_and_the_Levant |
| 162. | nations | 27: [10, 10.0] | nations united u.n. | Headquarters_of_the_United_Nations |
| 163. | hamas | 28: [10, 10.0] | hamas israel gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 164. | appeared | 28: [10, 10.0] | appeared president syria | Syria |
| 165. | press | 36: [10, 10.0] | press china prime | Premier_of_the_People's_Republic_of_China |
| 166. | nato | 36: [20, 10.0] | nato ukraine russia | Ukraine–NATO_relations |
| 167. | national | 40: [10, 10.0] | national party security | National_security |
| 168. | reports | 42: [10, 10.0] | reports chinese news | Fox_News |
| 169. | afghan | 48: [10, 10.0] | afghan afghanistan election | War_in_Afghanistan_(2001–present) |
| 170. | election | 51: [10, 10.0] | election presidential president | United_States_presidential_election |
| 171. | prime | 17: [19, 9.5], 24: [20, 5.0], 42: [11, 5.5] | prime minister leader | Prime_Minister_of_the_United_Kingdom |
| 172. | attacks | 18: [11, 5.5], 43: [19, 9.5] | attacks killed state | List_of_fatal_cougar_attacks_in_North_America |
| 173. | highlights | 30: [19, 9.5] | highlights herald international | Seoul_International_Drama_Awards |
| 174. | pistorius | 15: [18, 9.0] | pistorius oscar trial | Trial_of_Oscar_Pistorius |
| 175. | groups | 39: [18, 9.0] | groups rights syria | Human_rights_in_Syria |
| 176. | group | 49: [18, 9.0] | group militant state | Militant_tendency |
| 177. | bowe | 23: [17, 8.5] | bowe bergdahl sgt | Bowe_Bergdahl |
| 178. | flight | 29: [17, 8.5] | flight malaysia airlines | Malaysia_Airlines_Flight_370 |
| 179. | islamic | 38: [41, 8.2] | islamic state iraq | Islamic_State_of_Iraq_and_the_Levant |
| 180. | iraq | 24: [47, 7.83], 32: [40, 8.0] | iraq syria militants | Islamic_State_of_Iraq_and_the_Levant |
| 181. | case | 41: [10, 5.0], 49: [16, 8.0] | case court trial | Trial_court |
| 182. | people | 3: [15, 7.5], 40: [25, 6.25] | people killed china | China |
| 183. | sunni | 24: [15, 7.5] | sunni iraq militants | Islamic_State_of_Iraq_and_the_Levant |
| 184. | france | 34: [15, 7.5] | france french herald | France |
| 185. | delhi | 4: [14, 7.0] | delhi india day | New_Delhi |
| 186. | public | 5: [14, 7.0], 8: [10, 5.0] | public china government | Government_of_China |
| 187. | search | 11: [28, 7.0] | search missing malaysia | Malaysia_Airlines_Flight_370 |
| 188. | response | 36: [14, 7.0] | response ebola obama | Responses_to_the_West_African_Ebola_virus_epidemic |
| 189. | hassan | 39: [14, 7.0] | hassan president rouhani | Hassan_Rouhani |
| 190. | border | 41: [20, 6.67] | border ukraine syria | Russia–Turkey_proxy_conflict |
| 191. | korean | 16: [13, 6.5] | korean south korea | North_Korea–South_Korea_relations |
| 192. | palestinian | 17: [10, 5.0], 23: [13, 6.5], 35: [11, 5.5] | palestinian israel israeli | Israeli–Palestinian_conflict |
| 193. | disaster | 17: [13, 6.5] | disaster ferry south | Sinking_of_MV_Sewol |
| 194. | candidate | 19: [13, 6.5] | candidate party abdullah | Abdullah_Gül |
| 195. | video | 23: [11, 5.5], 44: [13, 6.5] | video state group | Video_Coding_Experts_Group |
| 196. | set | 26: [13, 6.5] | set would ukraine | Ukraine_International_Airlines_Flight_752 |
| 197. | ground | 38: [13, 6.5] | ground troops u.s. | Personnel_Armor_System_for_Ground_Troops |
| 198. | york | 39: [19, 6.33] | york times united | The_New_York_Times |
| 199. | country | 47: [19, 6.33] | country china president | President_of_the_Republic_of_China |
| 200. | tiananmen | 23: [37, 6.17] | tiananmen square anniversary | Tiananmen_Square |
| 201. | next | 3: [12, 6.0] | next minister prime | List_of_prime_ministers_of_the_United_Kingdom |
| 202. | killing | 5: [11, 5.5], 29: [12, 6.0] | killing death people | Mass_killings_under_communist_regimes |
| 203. | sochi | 6: [12, 6.0] | sochi olympics russia | 2014_Winter_Olympics |
| 204. | died | 12: [12, 6.0] | died death people | List_of_deaths_due_to_COVID-19 |
| 205. | obama | 16: [10, 5.0], 44: [10, 5.0], 51: [24, 6.0] | obama president u.s. | Barack_Obama |
| 206. | week | 19: [12, 6.0], 23: [11, 5.5] | week last china | Last_Week_Tonight_with_John_Oliver |
| 207. | attack | 21: [18, 6.0] | attack killed people | Crocodile_attack |
| 208. | rebels | 24: [12, 6.0] | rebels ukraine government | War_in_Donbass |
| 209. | call | 25: [12, 6.0] | call president officials | Trump–Raffensperger_phone_call |
| 210. | east | 27: [12, 6.0] | east ukraine middle | Middle_East |
| 211. | pakistani | 35: [12, 6.0] | pakistani pakistan taliban | Tehrik-i-Taliban_Pakistan |
| 212. | efforts | 35: [12, 6.0] | efforts china government | China |
| 213. | seen | 38: [12, 6.0] | seen china president | President_of_the_People's_Republic_of_China |
| 214. | modi | 39: [18, 6.0] | modi narendra minister | Narendra_Singh_Tomar |
| 215. | change | 50: [12, 6.0] | change climate china | Climate_change_in_China |
| 216. | peace | 50: [12, 6.0] | peace talks president | 2013–2014_Israeli–Palestinian_peace_talks |
| 217. | agency | 50: [12, 6.0] | agency news says | Yonhap_News_Agency |
| 218. | parliament | 21: [17, 5.67] | parliament party minister | First_Minister_of_Scotland |
| 219. | india | 2: [11, 5.5] | india minister modi | Narendra_Modi |
| 220. | taliban | 3: [10, 5.0], 13: [11, 5.5] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 221. | leave | 5: [11, 5.5] | leave city president | President_of_the_United_States |
| 222. | european | 6: [11, 5.5], 36: [10, 5.0] | european union ukraine | Ukraine–European_Union_relations |
| 223. | south | 12: [11, 5.5], 40: [10, 5.0] | south korea china | China–South_Korea_relations |
| 224. | killed | 25: [15, 5.0], 29: [22, 5.5] | killed people least | List_of_people_killed_for_being_transgender |
| 225. | russia | 28: [11, 5.5] | russia ukraine putin | Russo-Ukrainian_War |
| 226. | year | 32: [10, 5.0], 34: [11, 5.5] | year china last | Chinese_New_Year |
| 227. | back | 32: [10, 5.0], 37: [11, 5.5], 42: [10, 5.0] | back government president | President_(government_title) |
| 228. | campaign | 37: [22, 5.5] | campaign president china | President_of_the_People's_Republic_of_China |
| 229. | seeking | 40: [11, 5.5] | seeking president hong | Hong_Kong |
| 230. | inquiry | 45: [11, 5.5] | inquiry investigation security | First_impeachment_inquiry_against_Donald_Trump |
| 231. | crimes | 45: [11, 5.5] | crimes court u.n. | Mass_atrocity_crimes |
| 232. | thousands | 47: [11, 5.5] | thousands people tens | Ten_thousand_years |
| 233. | news | 11: [16, 5.33] | news media india | Media_of_India |
| 234. | violence | 8: [21, 5.25] | violence people ukraine | 2014_pro-Russian_unrest_in_Ukraine |
| 235. | airport | 3: [10, 5.0] | airport capital ebola | Ebola_virus_cases_in_the_United_States |
| 236. | ink | 4: [10, 5.0] | ink india conversation | Lakshmi_Pratury |
| 237. | crisis | 5: [10, 5.0], 23: [10, 5.0] | crisis ukraine russia | Ukrainian_crisis |
| 238. | journalists | 5: [10, 5.0] | journalists egypt jazeera | 2013–15_detention_of_Al_Jazeera_journalists_by_Egypt |
| 239. | jinping | 8: [10, 5.0] | jinping xi president | Xi_Jinping |
| 240. | taiwan | 12: [10, 5.0] | taiwan china trade | Taiwan |
| 241. | vote | 13: [10, 5.0] | vote election independence | Proposed_second_Scottish_independence_referendum |
| 242. | voters | 14: [15, 5.0] | voters election elections | 2020_United_States_elections |
| 243. | marine | 14: [10, 5.0] | marine iran former | Iran_hostage_crisis |
| 244. | cast | 15: [10, 5.0] | cast election vote | List_of_United_States_presidential_elections_by_popular_vote_margin |
| 245. | role | 15: [10, 5.0] | role president iran | Vice_President_of_Iran |
| 246. | help | 19: [10, 5.0] | help u.s. united | United_States_House_of_Representatives |
| 247. | talks | 20: [20, 5.0] | talks peace iran | List_of_Middle_East_peace_proposals |
| 248. | coast | 21: [10, 5.0] | coast korea south | Korea_Coast_Guard |
| 249. | korea | 21: [10, 5.0] | korea north south | North_Korea–South_Korea_relations |
| 250. | girls | 22: [10, 5.0] | girls women nigerian | Chibok_schoolgirls_kidnapping |
| 251. | student | 23: [10, 5.0] | student hong kong | City_University_of_Hong_Kong |
| 252. | bergdahl | 23: [20, 5.0] | bergdahl bowe sgt | Bowe_Bergdahl |
| 253. | company | 23: [10, 5.0] | company chinese china | List_of_companies_of_China |
| 254. | report | 24: [10, 5.0] | report says china | 2020_China–India_skirmishes |
| 255. | militant | 24: [10, 5.0] | militant group iraq | Islamic_State_of_Iraq_and_the_Levant |
| 256. | work | 25: [10, 5.0] | work china government | Government_of_China |
| 257. | despite | 26: [10, 5.0] | despite china ukraine | Ukraine |
| 258. | protests | 26: [10, 5.0] | protests hong kong | 2019–20_Hong_Kong_protests |
| 259. | tuesday | 27: [10, 5.0] | tuesday hong kong | Chief_Executive_of_Hong_Kong |
| 260. | intelligence | 28: [10, 5.0] | intelligence american u.s. | United_States_Intelligence_Community |
| 261. | germany | 30: [10, 5.0] | germany german international | Germany |
| 262. | yazidis | 33: [10, 5.0] | yazidis iraq iraqi | Yazidis |
| 263. | isis | 34: [20, 5.0], 49: [10, 5.0] | isis iraq state | Islamic_State_of_Iraq_and_the_Levant |
| 264. | james | 34: [10, 5.0] | james foley american | James_Foley_(journalist) |
| 265. | since | 35: [10, 5.0] | since first china | China |
| 266. | three | 36: [10, 5.0] | three years killed | Great_Chinese_Famine |
| 267. | action | 37: [10, 5.0] | action military syria | American-led_intervention_in_the_Syrian_Civil_War |
| 268. | independence | 37: [10, 5.0] | independence vote party | Alaskan_Independence_Party |
| 269. | pressure | 38: [10, 5.0] | pressure russia president | Atmospheric_pressure |
| 270. | paris | 38: [10, 5.0] | paris herald international | The_New_York_Times_International_Edition |
| 271. | narendra | 39: [15, 5.0] | narendra modi minister | Narendra_Singh_Tomar |
| 272. | democracy | 40: [20, 5.0] | democracy hong kong | Pro-democracy_camp_(Hong_Kong) |
| 273. | states | 46: [10, 5.0] | states united u.s. | U.S._state |
| 274. | capital | 48: [10, 5.0] | capital attack government | 2020_Aden_attacks |
| 275. | first | 49: [15, 5.0] | first time president | President_of_East_Timor |
| 276. | russian | 51: [15, 5.0] | russian ukraine russia | Ukrainians_in_Russia |
| 277. | trial | 51: [10, 5.0] | trial pistorius case | Trial_of_Oscar_Pistorius |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | ukraine | 4: [10, inf], 8: [22, inf] | ukraine russia 's | Ukrainians_in_Russia |
| 2. | voices | 4: [15, inf] | voices brazil 's | Voice_acting |
| 3. | brazil | 4: [14, inf] | brazil 's voices | Voice_acting |
| 4. | manus | 8: [15, inf] | manus island asylum | Manus_Island |
| 5. | island | 8: [11, inf] | island manus asylum | Manus_Island |
| 6. | crimea | 9: [12, inf] | crimea ukraine russia | Russo-Ukrainian_War |
| 7. | flight | 11: [22, 5.5], 29: [14, inf] | flight mh malaysia | Malaysia_Airlines_Flight_370 |
| 8. | mh | 11: [27, 27.0], 29: [63, inf] | mh flight search | Malaysia_Airlines_Flight_370 |
| 9. | audit | 18: [13, inf] | audit commission says | Election_audit |
| 10. | cuts | 20: [10, inf] | cuts budget 's | Budget_Cuts |
| 11. | post-soviet | 24: [19, inf] | post-soviet world need | Post-Soviet_states |
| 12. | know | 24: [18, inf] | know need world | GMA3:_What_You_Need_To_Know |
| 13. | isis | 24: [16, inf], 32: [15, 15.0] | isis us iraq | Islamic_State_of_Iraq_and_the_Levant |
| 14. | iraq | 24: [24, inf], 32: [10, inf] | iraq us isis | Islamic_State_of_Iraq_and_the_Levant |
| 15. | malaysia | 29: [16, inf] | malaysia airlines mh | Malaysia_Airlines_Flight_370 |
| 16. | airlines | 29: [15, inf] | airlines malaysia mh | Malaysia_Airlines_Flight_17 |
| 17. | strikes | 32: [11, inf], 39: [13, 13.0] | strikes air isis | International_military_intervention_against_ISIL |
| 18. | ferguson | 33: [16, inf] | ferguson police brown | Shooting_of_Michael_Brown |
| 19. | james | 34: [10, inf] | james foley 's | James_Foley_(journalist) |
| 20. | foley | 34: [12, inf] | foley james us | James_Foley_(journalist) |
| 21. | pistorius | 37: [12, inf] | pistorius oscar trial | Trial_of_Oscar_Pistorius |
| 22. | ottawa | 43: [10, inf] | ottawa shooting soldier | 2014_shootings_at_Parliament_Hill,_Ottawa |
| 23. | sudan | 50: [10, inf] | sudan south 's | South_Sudan |
| 24. | crash | 29: [22, 22.0] | crash mh site | Malaysia_Airlines_Flight_17 |
| 25. | need | 24: [17, 17.0] | need know world | GMA3:_What_You_Need_To_Know |
| 26. | state | 5: [16, 16.0] | state islamic 's | Islamic_state |
| 27. | union | 5: [14, 14.0] | union 's state | State_of_the_Union |
| 28. | ceasefire | 29: [14, 14.0] | ceasefire gaza hamas | 2014_Gaza_War |
| 29. | european | 21: [13, 13.0] | european elections commission | President_of_the_European_Commission |
| 30. | budget | 20: [38, 12.67] | budget cuts 's | Budget_Cuts |
| 31. | putin | 12: [11, 11.0] | putin ukraine vladimir | Putin_khuylo! |
| 32. | nigeria | 19: [11, 11.0] | nigeria 's boko | Boko_Haram |
| 33. | australia | 30: [11, 11.0] | australia 's asylum | Asylum_in_Australia |
| 34. | referendum | 11: [10, 10.0] | referendum 's ukraine | 2014_Crimean_status_referendum |
| 35. | government | 18: [10, 10.0] | government 's says | Say's_law |
| 36. | ebola | 31: [10, 10.0] | ebola sierra leone | Ebola_virus_epidemic_in_Sierra_Leone |
| 37. | gaza | 28: [18, 9.0] | gaza israel ceasefire | Gaza_War_(2008–2009) |
| 38. | world | 31: [17, 8.5] | world 's first | First_World |
| 39. | hong | 40: [24, 8.0] | hong kong protests | 2019–20_Hong_Kong_protests |
| 40. | kong | 40: [24, 8.0] | kong hong protests | 2019–20_Hong_Kong_protests |
| 41. | d-day | 23: [15, 7.5] | d-day anniversary 's | Normandy_landings |
| 42. | violence | 8: [11, 5.5] | violence manus 's | Manusmriti |
| 43. | protests | 40: [11, 5.5] | protests 's hong | 2019–20_Hong_Kong_protests |
| 44. | kobani | 41: [11, 5.5] | kobani isis turkey | Kobanî |
| 45. | first | 3: [10, 5.0], 31: [16, 5.33] | first world 's | First_World |
| 46. | nato | 36: [16, 5.33] | nato ukraine russia | Ukraine–NATO_relations |
| 47. | us | 24: [21, 5.25] | us isis iraq | Islamic_State_of_Iraq_and_the_Levant |
| 48. | elections | 21: [10, 5.0] | elections european india | 1937_Indian_provincial_elections |
| 49. | hamas | 29: [10, 5.0] | hamas gaza israel | 2012_Israeli_operation_in_the_Gaza_Strip |
| 50. | british | 36: [10, 5.0] | british isis hostage | ISIL_beheading_incidents |
