# Keywords with the highest 'interestingness' in 2004

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
| 1. | region | 2: [23, inf], 11: [12, 12.0], 22: [17, 8.5] | region 's sudan | South_Sudan |
| 2. | forces | 2: [15, inf], 15: [44, 6.29], 39: [11, 5.5] | forces 's american | American_Forces_Network |
| 3. | even | 2: [10, inf], 9: [18, 18.0], 49: [11, 11.0] | even 's iraq | Iraq_War |
| 4. | foreign | 2: [22, inf] | foreign 's iraq | Foreign_hostages_in_Iraq |
| 5. | taliban | 2: [21, inf], 8: [10, 5.0], 23: [14, inf], 41: [12, inf] | taliban afghanistan afghan | War_in_Afghanistan_(2001–present) |
| 6. | seen | 2: [12, 12.0], 49: [11, inf] | seen 's government | Divided_government_in_the_United_States |
| 7. | cats | 2: [11, inf] | cats sars civet | Asian_palm_civet |
| 8. | found | 2: [11, inf] | found 's iraq | Iraq_War |
| 9. | harvard | 2: [10, inf] | harvard bells 's | Harvard_of_the_South_(band) |
| 10. | bells | 2: [12, inf] | bells harvard 's | Harvard_of_the_South_(band) |
| 11. | civet | 2: [13, inf] | civet sars china | SARS_conspiracy_theory |
| 12. | west | 2: [12, inf], 16: [28, 14.0], 22: [16, 8.0] | west 's bank | West_Bank |
| 13. | secretary | 2: [12, inf], 4: [10, 5.0], 26: [10, 5.0] | secretary 's iraq | 2003_invasion_of_Iraq |
| 14. | european | 2: [25, inf] | european 's union | European_Union |
| 15. | georgia | 2: [20, inf], 15: [14, 7.0], 32: [11, inf] | georgia world saakashvili | Mikheil_Saakashvili |
| 16. | saakashvili | 2: [11, inf] | saakashvili georgia mikhail | Mikheil_Saakashvili |
| 17. | deal | 2: [12, inf], 35: [10, inf] | deal 's iraqi | Iraq |
| 18. | europe | 2: [32, inf] | europe world briefing | BBC_World_News |
| 19. | schools | 2: [10, inf] | schools 's public | Public_school_(United_Kingdom) |
| 20. | general | 2: [16, inf], 24: [15, 15.0], 35: [13, 6.5], 49: [11, 11.0] | general 's iraq | Iraq_War |
| 21. | jewish | 2: [10, 10.0], 30: [10, 10.0], 33: [10, inf] | jewish gaza israeli | Israeli_disengagement_from_Gaza |
| 22. | powell | 2: [11, inf], 12: [23, 11.5], 26: [13, 13.0] | powell colin state | Colin_Powell |
| 23. | africa | 2: [11, inf] | africa world 's | South_Africa |
| 24. | occupation | 2: [11, inf], 19: [10, 10.0], 21: [17, 5.67], 27: [14, inf] | occupation iraq american | Occupation_of_Iraq_(2003–2011) |
| 25. | proposed | 2: [10, inf] | proposed 's government | List_of_proposed_amendments_to_the_United_States_Constitution |
| 26. | mexico | 2: [14, 7.0], 19: [10, 10.0], 28: [11, 11.0], 36: [10, 10.0], 44: [12, inf], 48: [11, inf] | mexico 's mexican | Crime_in_Mexico |
| 27. | eggs | 2: [10, inf] | eggs world 's | World_egg |
| 28. | putin | 2: [10, 5.0], 30: [10, inf], 47: [10, 5.0] | putin 's russia | Russia_under_Vladimir_Putin |
| 29. | without | 3: [15, 5.0], 14: [19, inf] | without 's government | Federal_government_of_the_United_States |
| 30. | swedish | 3: [12, inf] | swedish minister foreign | Minister_for_Foreign_Affairs_(Sweden) |
| 31. | woman | 3: [12, inf] | woman 's two | Two-Faced_Woman |
| 32. | parmalat | 3: [12, inf] | parmalat italian tanzi | Parmalat |
| 33. | companies | 3: [12, 12.0], 33: [10, inf] | companies 's iraq | Iraq_Petroleum_Company |
| 34. | large | 3: [11, 5.5], 15: [10, 5.0], 36: [10, inf] | large 's american | List_of_U.S._cities_with_large_African-American_populations |
| 35. | fox | 3: [12, inf], 50: [11, inf] | fox mexico 's | Vicente_Fox |
| 36. | known | 3: [12, inf] | known 's iraq | There_are_known_knowns |
| 37. | bomber | 3: [11, 5.5], 5: [19, inf] | bomber suicide israeli | Use_of_child_suicide_bombers_by_Palestinian_militant_groups |
| 38. | gaza | 3: [20, inf], 9: [10, 5.0], 12: [26, 5.2], 16: [33, 33.0] | gaza israeli palestinian | Gaza–Israel_conflict |
| 39. | israelis | 3: [10, 10.0], 40: [12, 6.0], 47: [11, inf] | israelis israeli palestinians | Israeli–Palestinian_conflict |
| 40. | aids | 3: [10, 10.0], 7: [18, inf], 20: [12, 6.0] | aids africa drugs | HIV/AIDS_denialism |
| 41. | hamas | 3: [11, inf], 13: [41, 20.5], 17: [27, 6.75], 39: [15, 7.5], 47: [11, 5.5] | hamas israeli israel | Gaza–Israel_conflict |
| 42. | bremer | 3: [10, 10.0], 17: [14, 14.0], 27: [10, inf] | bremer american iraq | Paul_Bremer |
| 43. | sudan | 3: [12, 6.0], 19: [13, 6.5], 26: [18, inf], 30: [23, 5.75], 44: [13, inf], 52: [10, inf] | sudan darfur government | War_in_Darfur |
| 44. | japan | 3: [11, inf], 12: [10, 5.0], 20: [10, inf], 42: [12, 12.0] | japan 's japanese | Japan |
| 45. | hicks | 4: [10, inf] | hicks australian guantanamo | David_Hicks |
| 46. | khan | 4: [10, 5.0], 32: [10, inf] | khan nuclear 's | Abdul_Qadeer_Khan |
| 47. | father | 4: [10, inf] | father 's israeli | Law_of_Return |
| 48. | infected | 4: [11, inf] | infected aids people | List_of_countries_by_HIV/AIDS_adult_prevalence_rate |
| 49. | hezbollah | 4: [18, inf] | hezbollah israeli israel | 2006_Lebanon_War |
| 50. | missile | 4: [12, inf], 10: [10, inf] | missile israeli 's | Arrow_(Israeli_missile) |
| 51. | lebanon | 4: [12, inf] | lebanon hezbollah syria | Hezbollah |
| 52. | vatican | 4: [14, inf], 26: [10, 5.0] | vatican pope john | Pope_John_Paul_I_conspiracy_theories |
| 53. | pope | 4: [12, inf] | pope john paul | Pope_John_Paul_II |
| 54. | john | 4: [13, 6.5], 10: [12, inf], 14: [11, 5.5], 29: [12, 6.0] | john iraq 's | Iraq_War |
| 55. | movie | 4: [10, inf] | movie 's vatican | The_Vatican_Tapes |
| 56. | economic | 4: [24, 6.0], 6: [10, inf], 49: [11, 5.5] | economic 's government | Chief_Economic_Advisor_to_the_Government_of_India |
| 57. | paramilitary | 4: [10, inf] | paramilitary colombia 's | Right-wing_paramilitarism_in_Colombia |
| 58. | scientists | 4: [11, inf], 10: [11, inf] | scientists 's nuclear | Assassination_of_Iranian_nuclear_scientists |
| 59. | davos | 4: [30, inf] | davos forum economic | World_Economic_Forum |
| 60. | forum | 4: [24, inf] | forum davos world | World_Economic_Forum |
| 61. | food | 4: [10, inf], 14: [13, 6.5] | food 's united | Food_and_Drug_Administration |
| 62. | virus | 4: [18, inf] | virus health spread | 2015–2016_Zika_virus_epidemic |
| 63. | thailand | 4: [10, 5.0], 40: [16, inf] | thailand avian flu | Avian_influenza |
| 64. | cheney | 4: [13, 6.5], 16: [23, inf], 25: [21, 21.0] | cheney 's pres | Liz_Cheney |
| 65. | mugabe | 4: [12, inf] | mugabe zimbabwe 's | Robert_Mugabe |
| 66. | lebanese | 5: [11, inf] | lebanese hezbollah lebanon | 2006_Lebanon_War |
| 67. | white | 5: [18, 18.0], 12: [11, 11.0], 28: [10, 10.0], 32: [11, inf], 42: [10, inf] | white bush 's | George_W._Bush |
| 68. | image | 5: [10, inf] | image 's photo | Photo_manipulation |
| 69. | blair | 5: [29, 5.8], 9: [11, 5.5], 13: [11, 5.5], 28: [10, inf], 40: [22, 7.33] | blair prime tony | Tony_Blair |
| 70. | scientist | 5: [12, 6.0], 22: [10, inf] | scientist nuclear 's | Assassination_of_Iranian_nuclear_scientists |
| 71. | guerrilla | 5: [11, inf] | guerrilla 's group | People's_Guerrilla_Group |
| 72. | taiwan | 5: [15, inf], 12: [12, inf], 37: [10, inf], 50: [12, inf], 53: [12, inf] | taiwan china 's | Taiwan,_China |
| 73. | sec | 5: [17, 8.5], 12: [18, 6.0], 19: [20, inf] | sec iraq says | Iraq_War |
| 74. | chirac | 5: [14, 7.0], 23: [19, inf] | chirac france jacques | Jacques_Chirac |
| 75. | resigns | 5: [11, inf] | resigns 's minister | Union_Council_of_Ministers |
| 76. | network | 5: [10, inf], 25: [11, inf] | network 's nuclear | Nuclear_weapons_of_the_United_States |
| 77. | gilligan | 5: [10, inf] | gilligan bbc 's | Mo_Gilligan |
| 78. | jerusalem | 5: [12, inf], 9: [10, 10.0] | jerusalem israeli palestinian | East_Jerusalem |
| 79. | bus | 5: [10, inf], 51: [13, inf] | bus attack bomb | 2012_Burgas_bus_bombing |
| 80. | expert | 5: [10, inf] | expert 's khan | Jiah_Khan |
| 81. | settlers | 6: [14, inf], 38: [14, 7.0], 42: [12, inf] | settlers gaza sharon | Israeli_disengagement_from_Gaza |
| 82. | strip | 6: [11, inf], 16: [11, 11.0], 20: [15, 5.0] | strip gaza israeli | Gaza_War_(2008–2009) |
| 83. | musharraf | 6: [21, 7.0], 22: [10, inf] | musharraf pakistan pakistani | Pervez_Musharraf |
| 84. | groups | 6: [16, 8.0], 15: [12, 6.0], 18: [10, 10.0], 41: [13, inf] | groups 's government | Federal_government_of_the_United_States |
| 85. | panel | 6: [14, 14.0], 25: [11, inf], 30: [21, 5.25], 35: [21, inf] | panel 's intelligence | Robertson_Panel |
| 86. | injured | 6: [10, inf] | injured people killed | Killed_or_Seriously_Injured |
| 87. | run | 6: [10, inf] | run 's iraq | Iraq |
| 88. | spain | 6: [20, 6.67], 11: [27, inf] | spain 's spanish | Spain |
| 89. | cities | 6: [11, inf], 15: [25, 25.0], 19: [16, 16.0] | cities 's american | List_of_U.S._cities_with_large_African-American_populations |
| 90. | terror | 6: [10, inf], 32: [22, 5.5] | terror 's attacks | 2008_Mumbai_attacks |
| 91. | liberia | 6: [10, inf] | liberia million united | Liberia–United_States_relations |
| 92. | rumsfeld | 6: [14, 7.0], 9: [10, inf], 19: [41, inf], 33: [16, 8.0] | rumsfeld iraq defense | Donald_Rumsfeld |
| 93. | tenet | 6: [10, 5.0], 23: [25, inf], 28: [11, inf] | tenet intelligence 's | George_Tenet |
| 94. | subway | 6: [12, inf], 36: [10, inf] | subway moscow bombing | 2010_Moscow_Metro_bombings |
| 95. | raid | 7: [14, 7.0], 21: [21, 5.25], 26: [11, inf], 46: [10, inf] | raid israeli 's | Raid_on_Entebbe_(film) |
| 96. | months | 7: [13, inf] | months 's iraq | 2003_invasion_of_Iraq |
| 97. | militias | 7: [13, inf] | militias sudan government | Slavery_in_Sudan |
| 98. | barrier | 7: [10, 5.0], 27: [24, inf] | barrier israel west | Israeli_West_Bank_barrier |
| 99. | faces | 7: [10, 10.0], 44: [12, inf] | faces 's iraq | Iran–Iraq_War |
| 100. | rybkin | 7: [14, inf] | rybkin 's putin | Ivan_Rybkin |
| 101. | station | 7: [10, inf] | station police iraqi | Iraqi_Police |
| 102. | haitian | 7: [12, inf] | haitian aristide haiti | Haiti |
| 103. | aristide | 7: [24, inf] | aristide haiti 's | Jean-Bertrand_Aristide |
| 104. | candidate | 7: [10, inf], 22: [11, 5.5] | candidate 's election | Perennial_candidate |
| 105. | middle | 7: [10, 5.0], 26: [11, inf] | middle east 's | Middle_East |
| 106. | centrifuge | 7: [10, inf] | centrifuge nuclear iran | Iran_nuclear_deal_framework |
| 107. | haiti | 8: [21, 7.0], 14: [14, 7.0], 22: [11, inf], 43: [11, 11.0] | haiti aristide 's | Jean-Bertrand_Aristide |
| 108. | zimbabwe | 9: [20, 10.0], 11: [10, 5.0], 41: [12, 6.0], 44: [14, inf] | zimbabwe 's africa | Zimbabweans_in_South_Africa |
| 109. | stele | 9: [10, inf] | stele antiquities egypt | Merneptah_Stele |
| 110. | agents | 9: [10, inf], 33: [10, 10.0] | agents 's american | U.S._Agent |
| 111. | hearing | 9: [18, inf] | hearing 's court | Hearing_(law) |
| 112. | land | 9: [16, inf] | land 's government | Federal_government_of_the_United_States |
| 113. | mines | 9: [10, inf] | mines land bombs | Land_mine |
| 114. | nato | 9: [10, inf], 14: [14, 14.0], 21: [14, inf], 26: [27, 6.75] | nato iraq 's | NATO_Training_Mission_–_Iraq |
| 115. | fashion | 9: [15, 7.5], 27: [12, inf] | fashion 's paris— | Paris_Fashion_Week |
| 116. | short | 9: [13, inf] | short 's says | Say's_law |
| 117. | space | 9: [12, inf] | space 's world | Space_World |
| 118. | port-au-prince | 9: [11, inf] | port-au-prince aristide haiti | Port-au-Prince |
| 119. | protest | 9: [11, 5.5], 35: [12, inf] | protest 's government | Protest |
| 120. | qatar | 9: [10, inf] | qatar russian 's | Qatar–Russia_relations |
| 121. | province | 10: [13, inf], 29: [13, inf] | province 's killed | Islamic_State_of_Iraq_and_the_Levant_–_Khorasan_Province |
| 122. | week | 10: [10, inf], 51: [13, 6.5] | week 's iraq | Iraq_War |
| 123. | coalition | 10: [14, inf], 33: [10, 5.0] | coalition 's party | National_Coalition_Party |
| 124. | restore | 10: [10, inf] | restore 's iraq | 2003_invasion_of_Iraq |
| 125. | system | 10: [12, inf], 13: [12, 6.0] | system 's government | List_of_countries_by_system_of_government |
| 126. | amb | 10: [10, inf] | amb says american | Pa_amb_tomàquet |
| 127. | roma | 10: [12, inf] | roma cuts slovakia | Antiziganism |
| 128. | march | 10: [21, 5.25], 23: [12, inf], 27: [11, 5.5] | march 's government | Federal_government_of_the_United_States |
| 129. | departure | 10: [10, inf], 23: [15, inf] | departure 's government | Constitution_of_the_United_States |
| 130. | seek | 10: [12, inf] | seek 's says | Asylum_seeker |
| 131. | holy | 10: [10, inf], 33: [10, inf] | holy american shiite | Holy_Shiite |
| 132. | shiites | 10: [22, 11.0], 15: [18, inf] | shiites iraq shiite | Faisal_I_of_Iraq |
| 133. | gunfire | 10: [11, inf] | gunfire palestinian killed | Timeline_of_the_Israeli–Palestinian_conflict |
| 134. | paris— | 10: [10, inf] | paris— fashion 's | Paris_Fashion_Week |
| 135. | ice | 10: [10, inf] | ice says arctic | Arctic |
| 136. | plane | 11: [15, 7.5], 35: [10, inf], 42: [13, inf] | plane 's crash | Lynyrd_Skynyrd_plane_crash |
| 137. | ford | 11: [11, inf] | ford 's gucci | Tom_Ford |
| 138. | madrid | 11: [36, inf] | madrid spain bombings | 2004_Madrid_train_bombings |
| 139. | impeachment | 11: [17, inf] | impeachment 's south | Impeachment |
| 140. | iran | 11: [28, 7.0], 14: [11, 11.0], 25: [30, 30.0], 37: [10, inf], 41: [10, 5.0] | iran nuclear 's | Nuclear_program_of_Iran |
| 141. | syria | 11: [14, inf], 20: [10, inf] | syria 's israel | Israel–Syria_relations |
| 142. | spanish | 11: [17, inf] | spanish spain 's | Spain |
| 143. | civilians | 11: [11, inf], 14: [12, 12.0], 21: [11, inf] | civilians american killed | Civilian_casualties_in_the_war_in_Afghanistan_(2001–present) |
| 144. | information | 11: [10, inf], 30: [13, 6.5] | information 's intelligence | Intelligence_assessment |
| 145. | visit | 11: [10, 10.0], 20: [19, 9.5], 52: [10, inf] | visit 's says | Conjugal_visit |
| 146. | eta | 11: [12, inf] | eta spain basque | ETA_(separatist_group) |
| 147. | washington | 12: [10, 5.0], 23: [12, inf] | washington 's iraq | Iraq_War |
| 148. | suspect | 12: [15, 5.0], 15: [11, inf] | suspect 's attacks | List_of_fatal_alligator_attacks_in_the_United_States |
| 149. | zougam | 12: [12, inf] | zougam madrid attacks | Jamal_Zougam |
| 150. | kosovo | 12: [14, inf] | kosovo united nations | United_Nations_Interim_Administration_Mission_in_Kosovo |
| 151. | pakistani | 12: [29, inf], 16: [13, 13.0], 22: [16, 16.0], 30: [10, inf] | pakistani pakistan nuclear | Pakistan_and_weapons_of_mass_destruction |
| 152. | chen | 12: [13, inf], 21: [13, 6.5] | chen taiwan china | Chen_Shui-bian |
| 153. | serbs | 12: [12, inf] | serbs 's bosnian | Serbs_of_Bosnia_and_Herzegovina |
| 154. | zambia | 12: [10, inf] | zambia 's zimbabwe | Tonga_language_(Zambia_and_Zimbabwe) |
| 155. | sheik | 13: [21, inf] | sheik 's israel | Israeli–Palestinian_conflict |
| 156. | yassin | 13: [44, inf] | yassin hamas israel | Ahmed_Yassin |
| 157. | demands | 13: [11, inf] | demands 's iraq | Iraq |
| 158. | organization | 13: [10, inf] | organization 's world | World_Health_Organization |
| 159. | russian | 13: [14, inf] | russian russia 's | Russia |
| 160. | far | 13: [17, 8.5], 21: [12, 6.0], 35: [10, inf] | far 's says | Spider-Man:_Far_From_Home |
| 161. | confirm | 13: [10, inf] | confirm 's officials | Resistbot |
| 162. | egypt | 13: [11, inf], 41: [11, inf] | egypt israel israeli | Egypt–Israel_peace_treaty |
| 163. | gandhi | 13: [10, inf], 20: [10, inf] | gandhi india prime | Rajiv_Gandhi |
| 164. | resolution | 13: [10, 5.0], 30: [13, inf] | resolution united iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 165. | loves | 13: [10, inf] | loves 's british | Everybody_Loves_a_Happy_Ending |
| 166. | threats | 13: [11, inf] | threats 's bush | Security_incidents_involving_George_W._Bush |
| 167. | korea | 13: [10, inf], 16: [33, 16.5], 26: [40, inf], 30: [16, 16.0], 34: [22, 22.0] | korea north south | North_Korea–South_Korea_relations |
| 168. | medical | 13: [12, inf] | medical 's health | Medical_officer_of_health |
| 169. | journalists | 14: [12, 6.0], 46: [11, inf] | journalists 's iraq | Media_coverage_of_the_Iraq_War |
| 170. | explosion | 14: [11, inf] | explosion killed people | 2020_Beirut_explosion |
| 171. | orders | 14: [16, inf] | orders 's court | Superior_orders |
| 172. | muslim | 14: [17, inf], 27: [13, 6.5] | muslim 's iraq | Islam_in_Iraq |
| 173. | uzbekistan | 14: [31, inf] | uzbekistan killed world | Uzbekistan |
| 174. | deaths | 14: [10, inf], 21: [14, 7.0], 42: [10, inf] | deaths killed 's | Killed_by_Death |
| 175. | building | 14: [12, inf], 27: [16, 16.0] | building 's american | United_States_Capitol |
| 176. | rules | 14: [11, inf], 18: [10, inf] | rules 's court | Merrick_Garland_Supreme_Court_nomination |
| 177. | mexicans | 14: [10, inf] | mexicans court mexico | Mexico |
| 178. | courts | 14: [12, inf] | courts court 's | United_States_courts_of_appeals |
| 179. | lithuania | 14: [15, inf] | lithuania nato russia | Russia–NATO_relations |
| 180. | falluja | 14: [23, 11.5], 22: [11, inf], 28: [11, 11.0], 45: [10, 5.0] | falluja american iraqi | Fallujah |
| 181. | grisly | 14: [10, inf] | grisly american iraq | Sabrina_Harman |
| 182. | bodies | 14: [13, inf] | bodies american found | Mermaids:_The_Body_Found |
| 183. | / | 15: [12, inf], 30: [44, 44.0] | / 's qaeda | Al-Qaeda |
| 184. | sadr | 15: [33, inf], 33: [43, 7.17] | sadr american 's | Muqtada_al-Sadr |
| 185. | shiite | 15: [63, 12.6], 50: [11, inf] | shiite american iraqi | January_2005_Iraqi_parliamentary_election |
| 186. | militia | 15: [23, inf], 19: [13, inf] | militia american 's | American_militia_movement |
| 187. | american-led | 15: [10, inf] | american-led iraq american | American-led_intervention_in_Iraq_(2014–present) |
| 188. | militiamen | 15: [11, inf], 33: [11, 11.0] | militiamen american najaf | Peace_Companies |
| 189. | followers | 15: [13, inf] | followers american sadr | Muqtada_al-Sadr |
| 190. | control | 15: [21, inf] | control 's government | Divided_government_in_the_United_States |
| 191. | small | 15: [12, inf] | small 's iraq | Iraq_War |
| 192. | karzai | 15: [10, 5.0], 19: [12, 6.0], 39: [11, 5.5], 41: [19, inf] | karzai afghan hamid | Hamid_Karzai |
| 193. | abu | 15: [12, inf], 19: [49, 7.0], 35: [31, 7.75] | abu iraq prison | Abu_Ghraib_torture_and_prisoner_abuse |
| 194. | insurgents | 15: [26, 26.0], 51: [10, inf] | insurgents american iraq | Iraqi_insurgency_(2003–2011) |
| 195. | sayyaf | 15: [11, inf] | sayyaf abu philippines | Abu_Sayyaf |
| 196. | project | 15: [10, inf] | project 's photos | Google_Photos |
| 197. | philippines | 15: [10, 5.0], 49: [14, inf] | philippines iraq philippine | Philippine_passport |
| 198. | japanese | 15: [17, inf], 33: [12, 6.0] | japanese japan 's | Japan |
| 199. | archaeologists | 15: [10, inf] | archaeologists ancient bc | Ancient_history_of_Afghanistan |
| 200. | african | 16: [20, inf], 46: [11, 5.5] | african africa south | South_Africa |
| 201. | standoff | 16: [10, inf] | standoff 's american | Bundy_standoff |
| 202. | negotiations | 16: [11, inf], 33: [11, inf] | negotiations 's american | Negotiation |
| 203. | judge | 16: [13, inf], 51: [14, inf] | judge 's court | United_States_district_court |
| 204. | vice | 16: [16, inf] | vice 's cheney | Dick_Cheney |
| 205. | dick | 16: [10, inf] | dick cheney 's | Dick_Cheney |
| 206. | press | 16: [11, 11.0], 24: [10, inf] | press 's iraq | 2003_invasion_of_Iraq |
| 207. | halliburton | 16: [12, inf] | halliburton iraq says | Halliburton |
| 208. | settlements | 16: [17, inf], 44: [16, inf] | settlements sharon gaza | Israeli_disengagement_from_Gaza |
| 209. | palestinian | 16: [29, 29.0], 24: [13, inf], 38: [15, inf] | palestinian israeli gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 210. | training | 16: [12, 6.0], 35: [10, inf] | training iraq 's | NATO_Training_Mission_–_Iraq |
| 211. | italian | 16: [11, inf], 40: [12, inf] | italian italy 's | Demographics_of_Italy |
| 212. | gave | 17: [10, inf] | gave 's iraq | Iraq_War |
| 213. | begins | 17: [10, inf] | begins 's iraqi | Iran–Iraq_War |
| 214. | museum | 17: [10, inf] | museum 's germany | German_Museum_of_Technology |
| 215. | jordanian | 17: [18, 18.0], 33: [10, inf] | jordanian iraq iraqi | Iraq_War |
| 216. | river | 17: [11, inf] | river 's world | List_of_rivers_by_length |
| 217. | disappearance | 17: [12, inf] | disappearance military marine | Disappearance_of_Royal_Marine_Alan_Addis |
| 218. | car | 17: [12, inf], 22: [13, 6.5], 31: [16, 8.0], 40: [10, inf] | car killed bomb | Car_bomb |
| 219. | arafat | 17: [13, inf], 19: [10, inf], 34: [12, inf], 44: [26, 8.67] | arafat palestinian 's | Yasser_Arafat |
| 220. | basra | 17: [15, inf] | basra iraq iraqi | Iraqi_Navy |
| 221. | anger | 17: [10, inf] | anger 's iraq | Iran–Iraq_War |
| 222. | norad | 17: [10, inf] | norad commission pentagon | Criticism_of_the_9/11_Commission |
| 223. | mosque | 18: [10, inf] | mosque 's american | Mosque |
| 224. | hong | 18: [15, 7.5], 27: [23, inf], 37: [11, inf] | hong kong 's | Hong_Kong |
| 225. | kong | 18: [15, 7.5], 27: [23, inf], 37: [11, inf] | kong hong 's | Hong_Kong |
| 226. | positions | 18: [12, inf] | positions 's american | American_football_positions |
| 227. | photographs | 18: [11, inf] | photographs iraq prisoners | Abu_Ghraib_torture_and_prisoner_abuse |
| 228. | commander | 19: [14, inf], 22: [12, 6.0] | commander iraq 's | Assassination_of_Qasem_Soleimani |
| 229. | criminal | 19: [11, inf] | criminal 's iraqi | Supreme_Iraqi_Criminal_Tribunal |
| 230. | rights | 19: [20, 10.0], 25: [15, 5.0], 43: [10, inf] | rights 's human | Human_rights |
| 231. | cuba | 19: [18, inf] | cuba 's mexico | Cuba–Mexico_relations |
| 232. | contractors | 19: [16, inf] | contractors iraq american | List_of_defense_contractors |
| 233. | oil | 19: [14, 7.0], 25: [29, 7.25], 42: [14, inf] | oil 's iraq | Oil_reserves_in_Iraq |
| 234. | prisons | 19: [11, inf] | prisons iraq abuse | Iraq_prison_abuse_scandals |
| 235. | inquiry | 19: [10, inf] | inquiry 's iraq | Iraq_Inquiry |
| 236. | scandal | 19: [12, 6.0], 32: [10, inf] | scandal abuse 's | Catholic_Archdiocese_of_Boston_sex_abuse_scandal |
| 237. | family | 19: [10, inf] | family 's american | An_American_Family |
| 238. | statement | 19: [11, inf] | statement 's iraq | Iraqi_insurgency_(2003–2011) |
| 239. | mistreatment | 19: [11, inf] | mistreatment prisoners abuse | Prisoner_abuse |
| 240. | donald | 19: [15, inf] | donald rumsfeld iraq | Donald_Rumsfeld |
| 241. | king | 19: [11, inf] | king 's world | King_World_Productions |
| 242. | karbala | 19: [14, inf] | karbala american 's | Karbala |
| 243. | interviews | 19: [14, inf] | interviews 's iraq | 2003_invasion_of_Iraq |
| 244. | kadyrov | 20: [11, inf] | kadyrov 's chechnya | Ramzan_Kadyrov |
| 245. | municipal | 20: [10, inf] | municipal elections palestinian | 2004–05_Palestinian_local_elections |
| 246. | later | 20: [10, 5.0], 24: [20, 5.0], 26: [10, inf] | later 's iraq | Iraq_War |
| 247. | drugs | 20: [10, inf], 27: [12, inf] | drugs aids health | Epidemiology_of_HIV/AIDS |
| 248. | beheading | 20: [14, inf] | beheading iraq american | Beheading_video |
| 249. | nicholas | 20: [11, inf] | nicholas berg american | Nick_Berg |
| 250. | berg | 20: [17, inf] | berg american beheading | Nick_Berg |
| 251. | canada | 20: [11, inf], 49: [17, inf] | canada canadian 's | Canadians |
| 252. | release | 20: [16, 16.0], 24: [10, inf], 34: [13, inf], 40: [14, 7.0] | release 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 253. | document | 20: [10, 10.0], 26: [10, inf] | document 's iraq | Iraq_War_documents_leak |
| 254. | unclear | 21: [11, inf] | unclear 's american | United_States |
| 255. | target | 21: [13, inf] | target 's iraq | Iraqi_insurgency_(2003–2011) |
| 256. | airport | 21: [12, inf], 25: [14, inf] | airport 's world | List_of_busiest_airports_by_passenger_traffic |
| 257. | approval | 21: [12, inf] | approval 's government | Federal_government_of_the_United_States |
| 258. | homes | 21: [10, inf] | homes 's israeli | Israeli_demolition_of_Palestinian_property |
| 259. | provided | 21: [11, inf] | provided 's officials | Threatening_government_officials_of_the_United_States |
| 260. | cast | 21: [12, inf] | cast 's iraq | Iraq_War |
| 261. | singh | 21: [17, inf] | singh india prime | List_of_prime_ministers_of_India |
| 262. | path | 21: [10, inf] | path 's israel | Israel |
| 263. | payments | 21: [10, inf] | payments 's government | Transfer_payment |
| 264. | letter | 21: [10, inf] | letter 's bush | Mahmoud_Ahmadinejad's_letter_to_George_W._Bush |
| 265. | strike | 21: [11, 11.0], 25: [10, inf] | strike 's american | 2007–08_Writers_Guild_of_America_strike |
| 266. | chalabi | 21: [19, inf], 23: [21, 7.0], 33: [49, inf] | chalabi 's iraqi | Ahmed_Chalabi |
| 267. | korean | 22: [11, 5.5], 26: [23, inf] | korean north korea | North_Korea–South_Korea_relations |
| 268. | envoy | 22: [12, inf] | envoy iraq united | Brett_McGurk |
| 269. | lakhdar | 22: [10, inf] | lakhdar iraq brahimi | Lakhdar_Brahimi |
| 270. | brahimi | 22: [15, inf] | brahimi iraq government | Lakhdar_Brahimi |
| 271. | largest | 22: [13, inf] | largest 's world | Largest_airlines_in_the_world |
| 272. | dam | 22: [10, inf] | dam 's project | Hoover_Dam |
| 273. | mahdi | 22: [10, inf], 36: [10, inf] | mahdi 's american | Mahdi |
| 274. | dr | 22: [11, inf] | dr 's says | Dr._Dre |
| 275. | choice | 22: [12, inf] | choice 's iraq | Iraq |
| 276. | iyad | 22: [11, inf] | iyad iraq iraqi | Politics_of_Iraq |
| 277. | alawi | 22: [12, inf] | alawi iraqi minister | Alawi_(name) |
| 278. | enough | 23: [11, inf] | enough 's says | Enough_(film) |
| 279. | internet | 23: [10, 5.0], 26: [10, 5.0], 36: [10, inf] | internet 's government | Internet |
| 280. | crackdown | 23: [12, inf] | crackdown 's government | 709_crackdown |
| 281. | step | 23: [13, inf] | step 's says | List_of_Step_by_Step_episodes |
| 282. | sierra | 23: [12, inf] | sierra leone court | Special_Court_for_Sierra_Leone |
| 283. | leone | 23: [12, inf] | leone sierra court | Special_Court_for_Sierra_Leone |
| 284. | code | 23: [11, inf] | code 's turkey | Telephone_numbers_in_Turkey |
| 285. | like | 24: [12, inf] | like 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 286. | schroder | 24: [10, inf] | schroder 's german | Dennis_Schröder |
| 287. | officer | 24: [11, inf], 28: [10, 5.0] | officer iraq 's | Iraq_War |
| 288. | mohammed | 25: [11, inf] | mohammed qaeda 's | Khalid_Sheikh_Mohammed |
| 289. | johnson | 25: [21, inf] | johnson saudi american | Paul_Marshall_Johnson_Jr. |
| 290. | good | 25: [10, inf] | good 's iraq | Iraq_War |
| 291. | jr | 25: [11, inf] | jr american saudi | Vanessa_Trump |
| 292. | web | 25: [10, inf] | web site 's | Website |
| 293. | martin | 25: [10, inf] | martin 's canada | Mae_Martin |
| 294. | finds | 25: [10, inf] | finds 's report | U.S._News_&_World_Report |
| 295. | body | 26: [10, inf] | body 's iraq | Iraq_Body_Count_project |
| 296. | send | 26: [10, inf] | send iraq 's | American-led_intervention_in_Iraq_(2014–present) |
| 297. | demonstrations | 26: [10, inf] | demonstrations 's government | Government-organized_demonstration |
| 298. | guantanamo | 26: [11, inf] | guantanamo bay military | Guantanamo_Bay_detention_camp |
| 299. | seized | 26: [13, inf] | seized 's american | American_Civil_War |
| 300. | boats | 26: [13, inf] | boats iran british | Anglo-Soviet_invasion_of_Iran |
| 301. | techniques | 26: [10, inf] | techniques interrogation iraq | Enhanced_interrogation_techniques |
| 302. | switzerland | 26: [10, inf] | switzerland world 's | Switzerland_during_the_World_Wars |
| 303. | prosecution | 26: [11, inf] | prosecution 's court | Prosecutor |
| 304. | memo | 26: [20, inf] | memo bush pres | George_H._W._Bush |
| 305. | torture | 26: [13, inf] | torture 's report | Senate_Intelligence_Committee_report_on_CIA_torture |
| 306. | exhibit | 26: [14, inf] | exhibit germany corpses | Soap_made_from_human_corpses |
| 307. | rockets | 27: [14, inf] | rockets israeli gaza | 2014_Gaza_War |
| 308. | decision | 27: [17, 17.0], 41: [11, inf], 49: [13, inf] | decision 's iraq | Iraq_War |
| 309. | rocket | 27: [13, inf] | rocket israeli gaza | 2012_Israeli_operation_in_the_Gaza_Strip |
| 310. | custody | 27: [15, 7.5], 46: [10, inf] | custody 's american | Custody |
| 311. | camp | 27: [10, inf] | camp 's israeli | 2000_Camp_David_Summit |
| 312. | families | 28: [14, inf] | families 's government | Federal_government_of_the_United_States |
| 313. | bahrain | 28: [10, inf] | bahrain families attacks | Bahrain |
| 314. | embassy | 28: [10, inf], 37: [10, 5.0], 41: [10, 5.0] | embassy american says | Embassy_of_the_United_States,_Baghdad |
| 315. | wahed | 28: [10, inf] | wahed afghan 's | Second_Anglo-Afghan_War |
| 316. | paris | 28: [10, inf], 35: [29, 5.8], 41: [38, 6.33] | paris france 's | Paris |
| 317. | c.i.a | 28: [12, inf] | c.i.a intelligence 's | Director_of_the_Central_Intelligence_Agency |
| 318. | committee | 28: [21, inf] | committee intelligence iraq | United_States_Senate_Select_Committee_on_Intelligence |
| 319. | concrete | 28: [10, inf] | concrete 's iraqi | Concrete_bomb |
| 320. | defectors | 28: [10, inf] | defectors north korea | North_Korean_defectors |
| 321. | idema | 28: [12, inf], 30: [14, inf] | idema american afghan | Jonathan_Idema |
| 322. | agencies | 28: [12, inf] | agencies intelligence 's | Intelligence_agency |
| 323. | company | 29: [10, inf], 39: [15, inf] | company 's iraq | Iraq_Petroleum_Company |
| 324. | anti-semitic | 29: [10, inf] | anti-semitic france jewish | Antisemitic_canard |
| 325. | france | 29: [15, 5.0], 40: [12, inf], 43: [26, 5.2], 50: [24, 12.0] | france 's french | France |
| 326. | donors | 29: [13, inf] | donors aids million | The_Global_Fund_to_Fight_AIDS,_Tuberculosis_and_Malaria |
| 327. | lord | 29: [11, inf] | lord 's intelligence | Joint_Intelligence_Committee_(United_Kingdom) |
| 328. | tuberculosis | 29: [10, inf] | tuberculosis aids fund | The_Global_Fund_to_Fight_AIDS,_Tuberculosis_and_Malaria |
| 329. | seminary | 29: [10, 5.0], 33: [11, inf] | seminary st polten | Catholic_Church_sexual_abuse_scandal_in_Austria |
| 330. | school | 29: [17, 8.5], 36: [40, inf], 42: [10, inf] | school 's children | Professional_Children's_School |
| 331. | area | 30: [10, inf], 35: [10, 10.0] | area 's american | American_Viticultural_Area |
| 332. | running | 30: [17, inf] | running 's government | Federal_government_of_the_United_States |
| 333. | directly | 30: [10, inf] | directly 's report | Mueller_report |
| 334. | pentagon | 30: [12, 12.0], 33: [11, inf] | pentagon iraq 's | The_Pentagon |
| 335. | captured | 30: [12, inf] | captured american 's | Captured_Tracks |
| 336. | bureau | 30: [12, inf] | bureau intelligence 's | Intelligence_Bureau_(India) |
| 337. | genocide | 30: [14, inf] | genocide sudan 's | Darfur_genocide |
| 338. | city | 30: [17, 8.5], 48: [16, 8.0], 52: [13, inf] | city 's american | List_of_U.S._cities_with_large_African-American_populations |
| 339. | abuses | 30: [11, inf], 35: [26, 6.5] | abuses military prison | Abu_Ghraib_torture_and_prisoner_abuse |
| 340. | pledge | 30: [10, inf] | pledge 's says | Pledge_of_Allegiance |
| 341. | passengers | 30: [10, inf] | passengers plane airport | Dulles_International_Airport |
| 342. | wine | 30: [10, inf] | wine france food | French_wine |
| 343. | assesses | 30: [10, inf] | assesses looking panel | Cohort_study |
| 344. | opportunities | 30: [10, inf] | opportunities 's looking | Career_Opportunities_(film) |
| 345. | prosecutor | 30: [10, inf] | prosecutor 's court | Prosecutor |
| 346. | york | 30: [10, inf], 32: [19, inf] | york 's officials | List_of_U.S._statewide_elected_officials |
| 347. | fahim | 31: [10, inf] | fahim karzai president | Mohammed_Fahim |
| 348. | embassies | 31: [10, inf] | embassies say officials | Diplomatic_mission |
| 349. | appeals | 31: [12, inf] | appeals 's court | United_States_courts_of_appeals |
| 350. | durban | 31: [10, inf] | durban south africa | Durban |
| 351. | mr. | 31: [10, inf], 41: [11, inf], 50: [12, inf] | mr. 's president | Mr._President_(title) |
| 352. | paraguay | 32: [10, inf] | paraguay fire people | Ycuá_Bolaños_supermarket_fire |
| 353. | store | 32: [10, inf] | store 's people | People's_store |
| 354. | christians | 32: [17, inf] | christians 's iraq | Christianity_in_Iraq |
| 355. | financial | 32: [16, inf] | financial 's says | Say's_law |
| 356. | institutions | 32: [12, inf] | institutions 's iraq | Iraq |
| 357. | federal | 32: [12, inf] | federal 's officials | Threatening_government_officials_of_the_United_States |
| 358. | plant | 33: [17, inf] | plant nuclear 's | Chernobyl_Nuclear_Power_Plant |
| 359. | ahmad | 33: [10, inf] | ahmad chalabi 's | Ahmed_Chalabi |
| 360. | soccer | 33: [10, inf] | soccer 's stadium | Soccer-specific_stadium |
| 361. | chinese | 33: [10, inf] | chinese china 's | China |
| 362. | dept | 33: [14, inf] | dept 's iraq | Ministry_of_Health_(Iraq) |
| 363. | immigration | 33: [11, inf] | immigration 's illegal | Illegal_immigration |
| 364. | immigrants | 33: [12, inf] | immigrants europe illegal | Illegal_immigration_to_the_United_States |
| 365. | singapore | 33: [13, inf] | singapore 's lee | Lee_family_(Singapore) |
| 366. | lee | 33: [13, inf] | lee 's singapore | Lee_family_(Singapore) |
| 367. | shrine | 33: [13, inf] | shrine najaf 's | Imam_Ali_Shrine |
| 368. | carter | 34: [10, inf] | carter chavez recall | 2004_Venezuelan_recall_referendum |
| 369. | journalist | 34: [10, inf] | journalist 's american | Michael_Tracey_(American_journalist) |
| 370. | garen | 34: [11, inf] | garen sadr american | Micah_Garen |
| 371. | koreans | 34: [11, inf] | koreans korea north | North_Korea–South_Korea_relations |
| 372. | james | 35: [10, inf] | james 's military | John_E._James |
| 373. | munch | 35: [10, inf] | munch museum oslo | Munch_Museum |
| 374. | interrogations | 35: [11, inf] | interrogations military iraq | Interrogation |
| 375. | guilty | 35: [10, inf] | guilty prison 's | Larry_Nassar |
| 376. | sistani | 35: [11, inf] | sistani 's iraqi | Ali_al-Sistani |
| 377. | politics | 36: [10, inf] | politics 's photo | Donald_Trump_photo_op_at_St._John's_Church |
| 378. | shift | 36: [10, inf] | shift 's bush | George_H._W._Bush |
| 379. | beslan | 36: [15, inf] | beslan school russian | Beslan_school_siege |
| 380. | ahern | 38: [10, inf] | ahern irish prime | Cecelia_Ahern |
| 381. | adultery | 38: [11, inf] | adultery turkey union | Adultery |
| 382. | greece | 39: [11, inf] | greece athens greek | Athens |
| 383. | peru | 40: [10, inf] | peru 's toledo | Alejandro_Toledo |
| 384. | urges | 40: [10, inf] | urges 's says | Urge_(film) |
| 385. | four | 40: [10, inf], 50: [19, inf] | four 's american | List_of_active_duty_United_States_four-star_officers |
| 386. | islamic | 41: [12, inf] | islamic 's group | Islamic_State_of_Iraq_and_the_Levant |
| 387. | khmer | 41: [10, inf] | khmer rouge leaders | Khmer_Rouge |
| 388. | rouge | 41: [10, inf] | rouge khmer leaders | Khmer_Rouge |
| 389. | next | 41: [10, inf] | next 's iraq | Iraq_War |
| 390. | prize | 41: [12, inf] | prize nobel 's | Nobel_Prize |
| 391. | rejects | 42: [12, inf] | rejects 's says | Say's_law |
| 392. | indians | 42: [10, inf] | indians 's india | Indian_independence_movement |
| 393. | finish | 42: [10, inf] | finish 's projects | Works_Progress_Administration |
| 394. | counting | 42: [10, inf] | counting election votes | Vote_counting |
| 395. | hassan | 43: [11, inf] | hassan 's iran | Hassan_Rouhani |
| 396. | myanmar | 43: [10, inf] | myanmar 's government | Politics_of_Myanmar |
| 397. | typhoon | 43: [14, inf] | typhoon japan 's | Typhoon_Hagibis |
| 398. | dead | 44: [12, inf] | dead 's people | Conversations_with_Dead_People |
| 399. | dogs | 44: [12, inf] | dogs 's prison | War_Dogs_(2016_film) |
| 400. | thatcher | 44: [12, inf] | thatcher africa south | Mark_Thatcher |
| 401. | tests | 44: [11, inf] | tests 's says | Student's_t-test |
| 402. | irregularities | 45: [10, inf] | irregularities election 's | 2004_United_States_election_voting_controversies |
| 403. | agreement | 45: [10, 5.0], 48: [16, inf] | agreement 's iraq | U.S.–Iraq_Status_of_Forces_Agreement |
| 404. | appeal | 45: [10, inf] | appeal 's court | United_States_courts_of_appeals |
| 405. | annan | 45: [11, inf], 49: [17, inf] | annan united kofi | Kofi_Annan |
| 406. | dutch | 45: [10, inf] | dutch netherlands police | Law_enforcement_in_the_Netherlands |
| 407. | abbas | 45: [10, inf] | abbas palestinian arafat | Mahmoud_Abbas |
| 408. | newmont | 46: [10, inf] | newmont indonesian bay | Newmont_Corporation |
| 409. | discussed | 46: [12, inf] | discussed 's officials | United_States_Senate |
| 410. | cyprus | 46: [10, inf] | cyprus turkey european | Turkish_Cypriots |
| 411. | ukraine | 48: [28, inf] | ukraine 's election | 2019_Ukrainian_presidential_election |
| 412. | captain | 48: [10, inf] | captain army military | Captain_(armed_forces) |
| 413. | viktor | 48: [17, inf] | viktor 's election | Viktor_Yushchenko |
| 414. | yushchenko | 48: [12, inf] | yushchenko viktor election | Viktor_Yushchenko |
| 415. | southeast | 49: [10, inf] | southeast 's nations | ASEAN |
| 416. | lure | 49: [12, inf] | lure 's luxury | Maurice_Lacroix |
| 417. | law | 49: [15, inf] | law 's government | Constitutional_law |
| 418. | kojo | 49: [10, inf] | kojo 's annan | Kojo_Annan |
| 419. | hospital | 50: [10, inf] | hospital 's american | American_Mission_Hospital |
| 420. | monday | 50: [22, inf] | monday 's iraq | Occupation_of_Iraq_(2003–2011) |
| 421. | students | 50: [10, inf] | students school 's | Student |
| 422. | village | 50: [10, inf] | village 's government | Government_of_Kerala |
| 423. | salinas | 50: [14, inf] | salinas 's mexico | Carlos_Salinas_de_Gortari |
| 424. | old | 51: [10, inf] | old 's iraq | Iraq_War |
| 425. | turks | 51: [10, inf] | turks 's turkey | Turkish_people |
| 426. | congo | 51: [10, inf] | congo world briefing | Second_Congo_War |
| 427. | christian | 52: [10, inf] | christian 's iraq | Christianity_in_Iraq |
| 428. | darfur | 52: [10, inf] | darfur sudan government | War_in_Darfur |
| 429. | waves | 53: [11, inf] | waves 's indian | 2004_Indian_Ocean_earthquake_and_tsunami |
| 430. | indian | 53: [20, inf] | indian india 's | Economy_of_India |
| 431. | ocean | 53: [13, inf] | ocean indian tsunami | 2004_Indian_Ocean_earthquake_and_tsunami |
| 432. | earthquake | 53: [21, inf] | earthquake 's iran | 2003_Bam_earthquake |
| 433. | struck | 53: [11, inf] | struck 's say | Gloria_Struck |
| 434. | disaster | 53: [21, inf] | disaster 's people | Disaster |
| 435. | tsunami | 53: [37, inf] | tsunami indian indonesia | 2004_Indian_Ocean_earthquake_and_tsunami |
| 436. | cost | 53: [11, inf] | cost 's iraq | Financial_cost_of_the_Iraq_War |
| 437. | hussein | 2: [24, 24.0], 21: [19, 9.5], 24: [13, 6.5], 27: [57, 9.5], 32: [11, 5.5], 51: [17, 5.67] | hussein 's iraq | Human_rights_in_Saddam_Hussein's_Iraq |
| 438. | palestinians | 16: [24, 24.0], 40: [27, 9.0] | palestinians israeli gaza | Israeli–Palestinian_conflict |
| 439. | cia | 28: [24, 24.0] | cia 's intelligence | Central_Intelligence_Agency |
| 440. | fire | 29: [20, 5.0], 32: [22, 22.0] | fire 's american | St._Elmo's_fire |
| 441. | qaeda | 4: [10, 10.0], 15: [15, 5.0], 25: [64, 21.33] | qaeda 's attacks | Timeline_of_Al-Qaeda_attacks |
| 442. | french | 2: [21, 21.0], 23: [15, 5.0], 33: [10, 10.0], 49: [12, 6.0] | french france 's | France |
| 443. | saudi | 17: [21, 21.0], 23: [31, 10.33], 30: [11, 5.5] | saudi arabia american | Saudi_Arabia–United_States_relations |
| 444. | briefing | 2: [41, 20.5] | briefing world europe | BBC_World_News |
| 445. | held | 2: [20, 20.0] | held 's iraq | Iraq |
| 446. | justice | 14: [20, 20.0], 31: [11, 5.5] | justice 's court | List_of_justices_of_the_Supreme_Court_of_the_United_States |
| 447. | prisoner | 19: [20, 20.0] | prisoner says abuse | Prisoner_abuse |
| 448. | turkey | 37: [20, 20.0], 51: [27, 5.4] | turkey 's european | Accession_of_Turkey_to_the_European_Union |
| 449. | german | 10: [19, 19.0], 24: [21, 10.5], 52: [15, 15.0] | german germany 's | Germany |
| 450. | aid | 18: [19, 19.0], 40: [15, 7.5] | aid 's iraq | Foreign_aid_to_Iraq |
| 451. | anniversary | 23: [19, 19.0] | anniversary th 's | Wedding_anniversary |
| 452. | military | 37: [21, 7.0], 48: [19, 19.0] | military 's iraq | Iraqi_Armed_Forces |
| 453. | six | 2: [19, 6.33], 15: [18, 18.0] | six 's says | Say_Say_Say |
| 454. | plans | 2: [18, 18.0], 22: [11, 5.5] | plans 's iraq | 2003_invasion_of_Iraq |
| 455. | germany | 2: [14, 14.0], 10: [10, 5.0], 14: [17, 17.0], 18: [10, 10.0], 33: [18, 18.0] | germany europe 's | German-occupied_Europe |
| 456. | marines | 15: [18, 18.0] | marines american falluja | Fallujah |
| 457. | friday | 31: [18, 18.0] | friday 's american | Next_Friday |
| 458. | sri | 53: [18, 18.0] | sri lanka world | Sri_Lanka_national_cricket_team |
| 459. | women | 8: [17, 17.0], 16: [10, 5.0], 26: [20, 5.0], 29: [10, 5.0] | women 's two | Two_Women |
| 460. | britain | 2: [16, 16.0], 50: [10, 5.0] | britain 's british | Britishness |
| 461. | suicide | 3: [27, 9.0], 36: [10, 5.0], 42: [16, 16.0], 45: [10, 5.0] | suicide killed 's | Suicide |
| 462. | capital | 9: [16, 16.0], 43: [16, 5.33] | capital 's government | Capital_city |
| 463. | sunni | 10: [10, 5.0], 15: [32, 16.0], 23: [13, 6.5] | sunni iraq american | Shia–Sunni_relations |
| 464. | fighting | 12: [16, 5.33], 15: [32, 16.0], 32: [15, 7.5] | fighting 's american | Fighting_American |
| 465. | images | 14: [16, 16.0], 20: [34, 11.33] | images american iraq | Iraqi_Americans |
| 466. | najaf | 15: [16, 16.0], 22: [26, 8.67], 33: [49, 5.44] | najaf american 's | Najaf |
| 467. | italy | 16: [16, 16.0], 19: [13, 13.0], 30: [11, 5.5], 40: [10, 10.0] | italy 's europe | Italy |
| 468. | sharon | 22: [17, 8.5], 29: [10, 5.0], 34: [20, 10.0], 42: [32, 8.0], 49: [16, 16.0] | sharon gaza israeli | Israeli_disengagement_from_Gaza |
| 469. | staff | 25: [16, 16.0] | staff 's iraq | Casualties_of_the_Iraq_War |
| 470. | vows | 33: [16, 16.0] | vows 's iraq | Iran–Iraq_War |
| 471. | vote | 33: [16, 16.0] | vote 's election | Electoral_fraud |
| 472. | pinochet | 51: [16, 16.0] | pinochet chile 's | Augusto_Pinochet |
| 473. | peace | 2: [15, 15.0], 13: [14, 14.0], 16: [13, 6.5], 41: [20, 10.0] | peace 's israel | Egypt–Israel_peace_treaty |
| 474. | saddam | 2: [15, 15.0], 21: [11, 5.5] | saddam 's iraq | Saddam_Hussein |
| 475. | republic | 10: [15, 15.0] | republic 's aristide | Jean-Bertrand_Aristide |
| 476. | kufa | 15: [15, 15.0], 22: [15, 7.5] | kufa american najaf | Peace_Companies |
| 477. | kill | 15: [10, 5.0], 23: [15, 15.0], 44: [10, 10.0] | kill 's israeli | List_of_Israeli_assassinations |
| 478. | go | 16: [15, 15.0], 41: [10, 10.0] | go 's iraq | Iraq_War |
| 479. | commission | 17: [15, 15.0], 25: [22, 5.5], 30: [39, 13.0] | commission 's report | Rogers_Commission_Report |
| 480. | withdrawal | 30: [15, 15.0] | withdrawal sharon gaza | Israeli_disengagement_from_Gaza |
| 481. | public | 32: [15, 15.0] | public 's iraq | 2003_invasion_of_Iraq |
| 482. | home | 2: [14, 14.0], 4: [10, 5.0], 17: [16, 5.33] | home 's iraq | Iraq_War |
| 483. | least | 2: [14, 14.0], 53: [10, 5.0] | least 's killed | Least_weasel |
| 484. | move | 6: [14, 14.0], 15: [11, 5.5], 19: [13, 6.5], 33: [10, 5.0] | move 's iraq | 2003_invasion_of_Iraq |
| 485. | still | 6: [11, 11.0], 10: [17, 8.5], 19: [11, 5.5], 45: [14, 14.0] | still 's iraq | Iraq_War |
| 486. | electoral | 10: [14, 14.0] | electoral 's election | List_of_United_States_presidential_elections_by_Electoral_College_margin |
| 487. | help | 12: [14, 14.0] | help 's iraq | Iran–Iraq_War |
| 488. | colin | 12: [14, 14.0] | colin powell state | Colin_Powell |
| 489. | israeli | 16: [25, 12.5], 47: [28, 14.0] | israeli gaza israel | Gaza–Israel_conflict |
| 490. | employees | 19: [14, 14.0] | employees 's iraq | Nisour_Square_massacre |
| 491. | ghraib | 19: [49, 9.8], 35: [28, 14.0] | ghraib prison abu | Abu_Ghraib_prison |
| 492. | interrogation | 19: [14, 14.0], 35: [13, 6.5] | interrogation military iraq | Interrogation |
| 493. | tiananmen | 23: [14, 14.0] | tiananmen china square | Tiananmen_Square |
| 494. | free | 26: [11, 11.0], 35: [14, 14.0], 52: [14, 14.0] | free 's government | Government_of_Free_Vietnam |
| 495. | trial | 27: [15, 5.0], 50: [14, 14.0] | trial 's court | Trial_court |
| 496. | senate | 28: [28, 14.0] | senate intelligence iraq | Senate_Report_on_Pre-war_Intelligence_on_Iraq |
| 497. | alert | 32: [14, 14.0] | alert say security | 2018_Hawaii_false_missile_alert |
| 498. | norodom | 42: [14, 14.0] | norodom king 's | Norodom_Sihamoni |
| 499. | tsunamis | 53: [14, 14.0] | tsunamis hit tsunami | Tsunami |
| 500. | iraq | 2: [88, 5.18], 47: [13, 13.0] | iraq 's iraqi | Iraqi_Kurdistan |
| 501. | accused | 3: [13, 13.0] | accused 's government | Government_of_India |
| 502. | trying | 5: [13, 13.0] | trying 's iraq | 2003_invasion_of_Iraq |
| 503. | nation | 6: [13, 13.0], 13: [10, 5.0] | nation 's government | Federal_government_of_the_United_States |
| 504. | roh | 11: [13, 13.0] | roh south 's | Roh_Jeong-eui |
| 505. | zapatero | 12: [13, 13.0] | zapatero spain 's | José_Luis_Rodríguez_Zapatero |
| 506. | libya | 13: [26, 13.0], 42: [15, 5.0] | libya nuclear 's | Libya_and_weapons_of_mass_destruction |
| 507. | al-sadr | 15: [26, 13.0] | al-sadr american 's | Muqtada_al-Sadr |
| 508. | call | 18: [13, 13.0], 34: [12, 6.0] | call 's iraq | 2003_invasion_of_Iraq |
| 509. | poor | 18: [13, 13.0] | poor 's world | S&P_Global_Ratings |
| 510. | allawi | 23: [13, 13.0], 33: [22, 7.33] | allawi iraqi iraq | Ayad_Allawi |
| 511. | sept | 25: [26, 13.0] | sept 's attacks | September_11_attacks |
| 512. | congress | 26: [13, 13.0] | congress 's iraq | Authorization_for_Use_of_Military_Force_Against_Iraq_Resolution_of_2002 |
| 513. | relatives | 28: [13, 13.0] | relatives 's iraq | Iraq_War |
| 514. | treaty | 40: [13, 13.0] | treaty 's nuclear | Treaty_on_the_Non-Proliferation_of_Nuclear_Weapons |
| 515. | americans | 2: [12, 12.0] | americans american 's | Americans |
| 516. | days | 2: [12, 12.0], 12: [12, 6.0], 27: [27, 6.75] | days 's iraq | Invasion_of_Kuwait |
| 517. | kashmir | 2: [12, 12.0] | kashmir india pakistan | 2014_India–Pakistan_floods |
| 518. | kills | 3: [12, 12.0] | kills israeli bomb | List_of_Israeli_assassinations |
| 519. | illicit | 4: [12, 12.0] | illicit iraq intelligence | Rationale_for_the_Iraq_War |
| 520. | force | 5: [11, 11.0], 30: [11, 11.0], 35: [12, 12.0] | force 's iraq | Multi-National_Force_–_Iraq |
| 521. | illegal | 5: [12, 12.0] | illegal 's government | Federal_government_of_the_United_States |
| 522. | birds | 5: [12, 12.0] | birds influenza avian | Avian_influenza |
| 523. | speech | 6: [11, 5.5], 22: [12, 12.0] | speech 's iraq | Mission_Accomplished_speech |
| 524. | number | 9: [11, 5.5], 15: [12, 12.0], 26: [12, 6.0] | number 's says | Say_Say_Say |
| 525. | wednesday | 10: [12, 12.0] | wednesday 's iraq | Wednesday |
| 526. | moktada | 15: [24, 12.0] | moktada american 's | Muqtada_al-Sadr |
| 527. | threatening | 15: [12, 12.0] | threatening 's american | Politeness_theory |
| 528. | remarks | 17: [12, 12.0], 49: [10, 10.0] | remarks 's says | Say's_law |
| 529. | opens | 23: [12, 12.0] | opens 's american | United_States |
| 530. | heart | 24: [12, 12.0] | heart 's american | America_Is_in_the_Heart |
| 531. | arroyo | 26: [12, 12.0] | arroyo philippines iraq | Jose_Miguel_Arroyo |
| 532. | mission | 27: [12, 12.0], 31: [12, 6.0] | mission iraq 's | Mission_Accomplished_speech |
| 533. | special | 30: [12, 12.0], 35: [11, 5.5] | special 's iraq | Special_Groups_(Iraq) |
| 534. | chapel | 30: [12, 12.0] | chapel icon roslin | List_of_In_Our_Time_programmes |
| 535. | children | 36: [20, 10.0], 50: [12, 12.0] | children 's world | Children_of_the_World |
| 536. | marriage | 38: [12, 12.0] | marriage gay canada | Same-sex_marriage_in_Canada |
| 537. | correct | 40: [12, 12.0] | correct iraq intelligence | Rationale_for_the_Iraq_War |
| 538. | yasir | 44: [12, 12.0] | yasir arafat palestinian | Yasser_Arafat |
| 539. | lanka | 53: [12, 12.0] | lanka sri world | Sri_Lanka_national_cricket_team |
| 540. | back | 2: [13, 6.5], 41: [11, 11.0] | back 's iraq | Iraq |
| 541. | soldiers | 2: [15, 5.0], 10: [16, 8.0], 47: [10, 5.0], 50: [11, 11.0] | soldiers american iraq | Iraqi_Army |
| 542. | among | 2: [11, 11.0], 10: [10, 5.0], 12: [10, 5.0], 33: [11, 5.5] | among 's iraq | Iraq |
| 543. | ayatollah | 3: [11, 11.0], 35: [11, 11.0] | ayatollah 's shiite | Ali_Khamenei |
| 544. | murder | 3: [11, 11.0], 29: [11, 11.0] | murder 's court | Sister_Abhaya_murder_case |
| 545. | head | 3: [11, 11.0] | head 's iraq | Iraq_War |
| 546. | brazil | 3: [17, 5.67], 20: [11, 11.0] | brazil 's silva | Thiago_Silva |
| 547. | using | 5: [11, 11.0] | using 's says | Say's_law |
| 548. | probably | 5: [11, 11.0] | probably 's says | Probably_Racist |
| 549. | jordan | 9: [10, 5.0], 19: [11, 11.0] | jordan 's iraq | Arab_Federation |
| 550. | hiv | 9: [11, 11.0] | hiv aids africa | HIV/AIDS_in_Africa |
| 551. | north | 9: [42, 8.4], 13: [11, 11.0] | north korea 's | North_Korea |
| 552. | venezuelan | 10: [11, 11.0] | venezuelan chavez recall | Hugo_Chávez |
| 553. | signatures | 10: [11, 11.0] | signatures recall chavez | 2004_Venezuelan_recall_referendum |
| 554. | venezuela | 10: [11, 11.0] | venezuela chavez recall | 2004_Venezuelan_recall_referendum |
| 555. | terrorists | 11: [11, 11.0], 22: [10, 10.0] | terrorists 's says | FBI_Most_Wanted_Terrorists |
| 556. | luis | 12: [11, 11.0] | luis 's spain | Luis_Alberto_(footballer,_born_1992) |
| 557. | rodriguez | 12: [11, 11.0] | rodriguez spain 's | Spain_Rodriguez |
| 558. | holds | 13: [11, 11.0] | holds 's world | The_World's_Billionaires |
| 559. | diplomats | 13: [11, 11.0] | diplomats 's government | Diplomat |
| 560. | money | 13: [11, 11.0], 36: [11, 5.5] | money 's says | Say's_law |
| 561. | announces | 15: [11, 11.0], 32: [11, 11.0] | announces 's world | The_World's_Billionaires |
| 562. | authority | 15: [11, 11.0] | authority 's iraq | Coalition_Provisional_Authority |
| 563. | missing | 16: [18, 9.0], 49: [11, 11.0] | missing 's american | Missing_in_America |
| 564. | ariel | 16: [11, 11.0] | ariel sharon gaza | Ariel_Sharon |
| 565. | earlier | 19: [11, 11.0] | earlier 's iraq | Iraq |
| 566. | return | 21: [18, 9.0], 27: [11, 11.0] | return 's iraq | Iraq_War |
| 567. | events | 23: [11, 11.0] | events iraq update | Iraqi_Special_Operations_Forces |
| 568. | crimes | 23: [11, 11.0] | crimes 's court | International_Criminal_Court |
| 569. | ireland | 24: [13, 6.5], 26: [11, 11.0] | ireland europe irish | Republic_of_Ireland |
| 570. | contractor | 25: [11, 11.0] | contractor american iraq | List_of_private_contractor_deaths_in_Iraq |
| 571. | population | 26: [11, 11.0] | population 's government | List_of_states_and_territories_of_the_United_States_by_population |
| 572. | reports | 28: [22, 11.0], 41: [10, 5.0] | reports 's world | U.S._News_&_World_Report |
| 573. | sites | 33: [11, 11.0] | sites 's american | American_Tower |
| 574. | nearly | 35: [11, 11.0] | nearly 's government | Government_of_India |
| 575. | second | 35: [11, 11.0] | second 's iraq | Iraq_War |
| 576. | suspected | 41: [11, 11.0] | suspected 's officials | Suspect |
| 577. | suspects | 41: [11, 11.0] | suspects police 's | Suspect |
| 578. | hold | 49: [11, 11.0] | hold 's iraq | Iraq_War |
| 579. | arrested | 52: [11, 11.0] | arrested 's police | Arrest |
| 580. | reach | 53: [11, 11.0] | reach 's iraq | Iraq |
| 581. | ahmed | 13: [21, 10.5] | ahmed 's palestinian | Ahmed_Jibril |
| 582. | paul | 25: [21, 10.5] | paul iraq american | Paul_Bremer |
| 583. | supreme | 27: [21, 10.5], 49: [18, 6.0] | supreme court 's | Supreme_Court_of_the_United_States |
| 584. | countries | 53: [21, 10.5] | countries 's iraq | Iraq |
| 585. | troops | 2: [26, 6.5], 15: [58, 7.25], 26: [31, 10.33] | troops iraq american | Withdrawal_of_U.S._troops_from_Iraq_(2020–21) |
| 586. | democracy | 2: [10, 10.0], 31: [10, 5.0], 38: [12, 6.0] | democracy 's hong | Pro-democracy_camp_(Hong_Kong) |
| 587. | fought | 2: [10, 10.0] | fought troops 's | Shock_troops |
| 588. | chickens | 4: [10, 10.0] | chickens flu avian | Avian_influenza |
| 589. | arms | 5: [28, 7.0], 9: [10, 10.0], 13: [10, 5.0], 20: [13, 6.5], 47: [10, 5.0] | arms 's iraq | Coat_of_arms_of_Iraq |
| 590. | central | 5: [10, 10.0], 19: [11, 5.5], 38: [10, 5.0] | central 's intelligence | Central_Intelligence |
| 591. | hutton | 5: [10, 10.0] | hutton bbc 's | Alan_Hutton |
| 592. | attackers | 7: [10, 10.0] | attackers police iraqi | Iraqi_Police |
| 593. | resign | 9: [10, 10.0] | resign 's sharon | Ariel_Sharon |
| 594. | unless | 10: [10, 10.0] | unless iraq 's | 2003_invasion_of_Iraq |
| 595. | past | 11: [10, 5.0], 15: [10, 10.0] | past 's photo | Google_Photos |
| 596. | action | 11: [10, 10.0] | action 's says | Simon_Says |
| 597. | killings | 11: [10, 10.0] | killings 's police | Encounter_killings_by_police |
| 598. | demand | 13: [10, 10.0] | demand 's iraq | Iraq |
| 599. | although | 14: [10, 10.0], 30: [10, 5.0] | although 's american | United_States |
| 600. | review | 14: [10, 10.0] | review 's iraq | Iraq_War |
| 601. | others | 15: [10, 10.0] | others 's iraq | War_in_Iraq_(2013–2017) |
| 602. | replace | 16: [10, 10.0] | replace 's palestinian | Palestinians |
| 603. | fighters | 17: [12, 6.0], 30: [10, 10.0] | fighters 's american | Foo_Fighters |
| 604. | local | 18: [12, 6.0], 52: [10, 10.0] | local 's officials | Official |
| 605. | human | 19: [18, 9.0], 33: [11, 5.5], 50: [10, 10.0] | human rights 's | Human_rights |
| 606. | parliament | 19: [10, 10.0] | parliament 's prime | Prime_Minister_of_the_United_Kingdom |
| 607. | hopes | 21: [10, 10.0] | hopes 's says | Bob_Hope |
| 608. | governing | 22: [10, 10.0] | governing 's iraqi | Iraqi_Governing_Council |
| 609. | arabia | 23: [10, 10.0] | arabia saudi 's | Saudi_Arabia |
| 610. | atomic | 25: [10, 10.0] | atomic nuclear iran | Nuclear_facilities_in_Iran |
| 611. | energy | 25: [10, 10.0] | energy nuclear iran | Nuclear_program_of_Iran |
| 612. | recently | 25: [10, 10.0] | recently 's iraq | Iran–Iraq_War |
| 613. | probing | 25: [10, 10.0] | probing attacks 's | 2012_Benghazi_attack |
| 614. | detainee | 25: [10, 10.0] | detainee abuse officials | Guantanamo_Bay_detention_camp |
| 615. | summit | 26: [20, 10.0] | summit meeting 's | Summit_(meeting) |
| 616. | ordered | 27: [10, 10.0] | ordered 's government | Ordered_logit |
| 617. | elbaradei | 28: [10, 10.0] | elbaradei nuclear iran | Joint_Comprehensive_Plan_of_Action |
| 618. | focus | 28: [10, 10.0] | focus 's nuclear | Bhabha_Atomic_Research_Centre |
| 619. | halt | 28: [10, 10.0] | halt 's israeli | Nuclear_weapons_and_Israel |
| 620. | counterterrorism | 32: [10, 10.0] | counterterrorism 's bush | George_W._Bush |
| 621. | aug | 33: [10, 10.0] | aug 's says | United_States |
| 622. | expected | 33: [10, 10.0] | expected 's iraq | Iran–Iraq_War |
| 623. | town | 34: [10, 10.0] | town 's map | Map |
| 624. | acts | 35: [10, 10.0] | acts 's says | Sadomasochism |
| 625. | al-sistani | 35: [10, 10.0] | al-sistani iraq 's | Ali_al-Sistani |
| 626. | gives | 41: [10, 10.0] | gives 's iraq | Iraq |
| 627. | year | 43: [17, 8.5], 49: [10, 10.0] | year 's iraq | Iraq_War |
| 628. | become | 49: [10, 10.0] | become 's government | Federal_government_of_the_United_States |
| 629. | membership | 51: [10, 10.0] | membership turkey 's | Accession_of_Turkey_to_the_European_Union |
| 630. | east | 52: [10, 10.0] | east middle 's | Middle_East |
| 631. | day | 52: [10, 10.0] | day 's iraq | Iraq_War |
| 632. | russia | 2: [19, 6.33], 43: [19, 9.5] | russia 's russian | Russia |
| 633. | meet | 4: [10, 5.0], 7: [19, 9.5] | meet 's iraq | 2003_invasion_of_Iraq |
| 634. | india | 8: [11, 5.5], 16: [10, 5.0], 29: [19, 9.5] | india 's world | Mister_India_World |
| 635. | laden | 25: [19, 9.5], 51: [14, 7.0] | laden qaeda 's | Osama_bin_Laden |
| 636. | conference | 29: [14, 7.0], 31: [19, 9.5] | conference 's says | Big_Ten_Conference |
| 637. | outside | 14: [18, 9.0] | outside 's iraq | Iraq_War |
| 638. | d-day | 23: [18, 9.0] | d-day bush pres | George_W._Bush |
| 639. | program | 33: [18, 9.0], 52: [10, 5.0] | program 's nuclear | Nuclear_program_of_Iran |
| 640. | northern | 38: [18, 9.0] | northern 's iraq | American-led_intervention_in_Iraq_(2014–present) |
| 641. | may | 53: [18, 9.0] | may 's iraq | May_2007_abduction_of_U.S._soldiers_in_Iraq |
| 642. | south | 2: [12, 6.0], 16: [51, 7.29], 26: [35, 8.75] | south 's korea | South_Korea |
| 643. | iraqi | 2: [34, 8.5], 47: [11, 5.5], 51: [20, 6.67], 53: [11, 5.5] | iraqi iraq 's | Iraqi_Kurdistan |
| 644. | bombings | 11: [17, 8.5], 21: [10, 5.0] | bombings 's madrid | 2004_Madrid_train_bombings |
| 645. | violence | 12: [16, 8.0], 38: [17, 8.5] | violence 's iraq | Iraqi_Civil_War_(2006–2008) |
| 646. | made | 14: [17, 8.5] | made 's iraq | Iraq_War |
| 647. | nuclear | 20: [12, 6.0], 33: [34, 8.5], 47: [21, 5.25] | nuclear 's iran | Nuclear_program_of_Iran |
| 648. | court | 27: [88, 6.29], 41: [17, 8.5] | court 's world | International_Court_of_Justice |
| 649. | chechnya | 35: [17, 8.5] | chechnya 's putin | Anti-gay_purges_in_Chechnya |
| 650. | afghanistan | 2: [15, 7.5], 30: [16, 8.0], 51: [12, 6.0] | afghanistan 's afghan | Flag_of_Afghanistan |
| 651. | vietnam | 3: [16, 8.0] | vietnam flu avian | Avian_influenza |
| 652. | council | 8: [16, 8.0], 16: [23, 5.75] | council 's iraq | Council_of_Representatives_of_Iraq |
| 653. | progress | 9: [16, 8.0] | progress 's iraq | 2003_invasion_of_Iraq |
| 654. | bombs | 10: [32, 8.0] | bombs iraq killed | List_of_bombings_during_the_Iraq_War |
| 655. | authorities | 14: [16, 8.0] | authorities 's say | Certificate_authority |
| 656. | militant | 15: [16, 8.0], 20: [16, 8.0] | militant 's group | Militant_tendency |
| 657. | terrorist | 35: [16, 8.0] | terrorist 's attacks | September_11_attacks |
| 658. | toll | 53: [16, 8.0] | toll death 's | List_of_wars_and_anthropogenic_disasters_by_death_toll |
| 659. | map | 2: [23, 7.67] | map 's photos | Google_Maps |
| 660. | opposition | 7: [23, 7.67] | opposition 's party | Opposition_Party_(Southern_U.S.) |
| 661. | israel | 19: [26, 6.5], 47: [23, 7.67] | israel israeli 's | Israeli_Jews |
| 662. | crash | 2: [15, 7.5] | crash killed plane | Lynyrd_Skynyrd_plane_crash |
| 663. | pay | 2: [15, 7.5] | pay 's iraq | Invasion_of_Kuwait |
| 664. | near | 10: [14, 7.0], 12: [17, 5.67], 37: [15, 7.5], 51: [10, 5.0] | near 's american | Near-Earth_object |
| 665. | abuse | 18: [15, 7.5], 19: [86, 5.73] | abuse military iraq | Abu_Ghraib_torture_and_prisoner_abuse |
| 666. | expel | 20: [15, 7.5] | expel 's times | Expulsion_from_the_United_States_Congress |
| 667. | terminal | 22: [15, 7.5] | terminal airport paris | Charles_de_Gaulle_Airport |
| 668. | cabinet | 22: [15, 7.5], 40: [11, 5.5] | cabinet 's prime | Cabinet_(government) |
| 669. | hope | 27: [15, 7.5] | hope 's iraq | Iraq_War |
| 670. | terrorism | 30: [15, 7.5], 35: [17, 5.67] | terrorism 's says | Domestic_terrorism |
| 671. | hostages | 36: [15, 7.5] | hostages iraq group | Foreign_hostages_in_Iraq |
| 672. | power | 44: [15, 7.5], 49: [10, 5.0] | power 's iraq | Iraq |
| 673. | officials | 2: [52, 7.43] | officials 's iraq | Iraq_War |
| 674. | us | 8: [44, 7.33], 23: [66, 5.5] | us 's iraq | 2003_invasion_of_Iraq |
| 675. | world | 2: [50, 7.14] | world briefing 's | World_Briefing |
| 676. | kurdish | 2: [14, 7.0] | kurdish iraq iraqi | Kurdistan_Region |
| 677. | life | 3: [14, 7.0], 8: [13, 6.5] | life 's photo | Dwayne's_Photo |
| 678. | prison | 3: [13, 6.5], 16: [15, 5.0], 19: [77, 7.0] | prison military abu | Abu_Ghraib_prison |
| 679. | religious | 3: [14, 7.0], 27: [11, 5.5] | religious 's iraq | Demographics_of_Iraq |
| 680. | since | 4: [36, 5.14], 10: [30, 5.0], 40: [14, 7.0] | since 's iraq | Iraq_War |
| 681. | chief | 4: [14, 7.0] | chief 's says | Chief_executive_officer |
| 682. | budget | 7: [14, 7.0] | budget 's iraq | Military_budget_of_the_United_States |
| 683. | fuel | 7: [21, 7.0] | fuel nuclear 's | Nuclear_fuel |
| 684. | center | 7: [10, 5.0], 9: [14, 7.0] | center 's iraq | Iraq_War |
| 685. | prisoners | 7: [14, 7.0], 19: [76, 6.33] | prisoners iraq iraqi | Iraq_War |
| 686. | including | 8: [14, 7.0], 17: [21, 7.0] | including 's iraq | 2003_invasion_of_Iraq |
| 687. | legal | 9: [14, 7.0], 26: [14, 7.0] | legal 's court | Court_dress |
| 688. | policy | 9: [14, 7.0], 16: [10, 5.0], 30: [17, 5.67] | policy 's iraq | Foreign_policy_of_the_Barack_Obama_administration |
| 689. | ethnic | 12: [14, 7.0] | ethnic 's iraq | Demographics_of_Iraq |
| 690. | tribal | 12: [14, 7.0] | tribal pakistani militants | Tehrik-i-Taliban_Pakistan |
| 691. | seems | 15: [14, 7.0] | seems 's iraq | Iraq |
| 692. | already | 19: [14, 7.0], 30: [10, 5.0] | already 's iraq | Iraq |
| 693. | transfer | 27: [28, 7.0] | transfer iraq iraqi | Iraq_War |
| 694. | athens | 35: [14, 7.0] | athens olympics olympic | 2004_Summer_Olympics |
| 695. | hit | 53: [14, 7.0] | hit 's israeli | Israel |
| 696. | state | 2: [20, 6.67], 12: [20, 5.0] | state 's powell | Colin_Powell |
| 697. | campaign | 7: [20, 6.67], 26: [12, 6.0] | campaign 's bush | Jeb_Bush_2016_presidential_campaign |
| 698. | fight | 7: [13, 6.5], 15: [11, 5.5], 33: [20, 6.67] | fight 's american | Fighting_American |
| 699. | looking | 30: [20, 6.67] | looking 's iraq | Iraq_War |
| 700. | time | 2: [13, 6.5] | time 's iraq | Once_Upon_a_Time_in_Iraq |
| 701. | killing | 5: [22, 5.5], 13: [39, 6.5] | killing 's two | Spree_killer |
| 702. | recount | 13: [13, 6.5] | recount chen election | 2004_Taiwanese_presidential_election |
| 703. | given | 14: [13, 6.5] | given 's iraq | Iraq–United_States_relations |
| 704. | mob | 14: [13, 6.5] | mob american iraq | 2003_invasion_of_Iraq |
| 705. | largely | 15: [13, 6.5] | largely 's iraq | ISIL_insurgency_in_Iraq_(2017–present) |
| 706. | critics | 17: [13, 6.5] | critics 's government | Critic |
| 707. | intelligence | 19: [26, 6.5], 28: [59, 5.36], 38: [17, 5.67] | intelligence 's iraq | Iraqi_Intelligence_Service |
| 708. | rafah | 21: [13, 6.5] | rafah israeli gaza | Rafah |
| 709. | early | 21: [13, 6.5] | early 's iraq | Iraq_War |
| 710. | sent | 21: [13, 6.5] | sent 's iraq | 2003_invasion_of_Iraq |
| 711. | times | 22: [13, 6.5] | times 's says | The_New_York_Times |
| 712. | square | 23: [13, 6.5] | square 's tiananmen | Tiananmen_Square |
| 713. | base | 23: [13, 6.5] | base 's american | Baseball |
| 714. | jones | 23: [13, 6.5] | jones 's indonesia | Prostitution_in_Indonesia |
| 715. | evidence | 25: [13, 6.5], 33: [26, 6.5] | evidence 's iraq | Iraq_War |
| 716. | service | 26: [13, 6.5] | service 's iraq | Iraqi_Intelligence_Service |
| 717. | charges | 33: [26, 6.5] | charges 's says | Electric_charge |
| 718. | ban | 36: [13, 6.5] | ban 's world | Ban_Ki-moon |
| 719. | militants | 38: [13, 6.5] | militants 's israeli | List_of_Israeli_assassinations |
| 720. | irish | 38: [13, 6.5] | irish ireland northern | Northern_Ireland |
| 721. | luxury | 49: [13, 6.5] | luxury lure asia | Marco_Bizzarri |
| 722. | residents | 52: [13, 6.5] | residents 's american | The_Residents |
| 723. | relief | 53: [26, 6.5] | relief aid 's | CARES_Act |
| 724. | police | 2: [11, 5.5], 29: [23, 5.75], 50: [19, 6.33] | police 's iraqi | Iraqi_Police |
| 725. | indonesia | 23: [10, 5.0], 53: [19, 6.33] | indonesia 's indonesian | Indonesia |
| 726. | rebel | 33: [19, 6.33] | rebel 's american | Rowdy_Rebel |
| 727. | kay | 5: [25, 6.25] | kay weapons iraq | David_Kay |
| 728. | say | 32: [61, 6.1] | say 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 729. | iraqis | 2: [24, 6.0], 31: [23, 5.75] | iraqis iraq iraqi | Islamic_State_of_Iraq |
| 730. | meeting | 2: [15, 5.0], 14: [12, 6.0], 19: [15, 5.0] | meeting 's bush | George_H._W._Bush |
| 731. | mikhail | 2: [12, 6.0] | mikhail 's russia | Michael_of_Russia |
| 732. | cases | 3: [12, 6.0] | cases 's court | Lists_of_United_States_Supreme_Court_cases |
| 733. | material | 3: [12, 6.0] | material says 's | Say's_law |
| 734. | wrong | 5: [12, 6.0] | wrong 's intelligence | LessWrong |
| 735. | tony | 5: [12, 6.0] | tony blair prime | Tony_Blair |
| 736. | across | 5: [12, 6.0], 13: [16, 5.33] | across 's american | Hands_Across_America |
| 737. | trade | 7: [12, 6.0], 17: [10, 5.0], 21: [16, 5.33], 31: [12, 6.0] | trade 's china | China–United_States_trade_war |
| 738. | air | 9: [12, 6.0], 21: [10, 5.0] | air 's says | United_States_Air_Force |
| 739. | convicted | 10: [10, 5.0], 15: [12, 6.0] | convicted 's prison | List_of_American_federal_politicians_convicted_of_crimes |
| 740. | role | 15: [12, 6.0], 24: [16, 5.33] | role 's iraq | Israel's_role_in_the_Iran–Iraq_war |
| 741. | heavy | 17: [12, 6.0] | heavy 's american | Heavy_metal_music |
| 742. | hostage | 19: [10, 5.0], 36: [12, 6.0] | hostage iraq american | Foreign_hostages_in_Iraq |
| 743. | rice | 19: [12, 6.0] | rice 's bush | Condoleezza_Rice |
| 744. | refugee | 21: [12, 6.0] | refugee israeli gaza | Palestinian_refugees |
| 745. | clear | 21: [12, 6.0] | clear 's iraq | List_of_Congressional_opponents_of_the_Iraq_War |
| 746. | pappas | 21: [12, 6.0] | pappas military prison | Thomas_Pappas |
| 747. | create | 23: [12, 6.0] | create 's iraq | Iraq |
| 748. | egyptian | 24: [12, 6.0] | egyptian egypt israeli | Egypt–Israel_peace_treaty |
| 749. | claims | 26: [12, 6.0], 28: [18, 6.0] | claims 's says | Say's_law |
| 750. | invasion | 27: [12, 6.0] | invasion iraq 's | 2003_invasion_of_Iraq |
| 751. | bombing | 29: [12, 6.0], 36: [22, 5.5], 45: [12, 6.0] | bombing killed 's | USS_Cole_bombing |
| 752. | responsible | 30: [12, 6.0] | responsible 's says | Shooting_of_Jacob_Blake |
| 753. | five | 30: [12, 6.0], 35: [15, 5.0] | five 's killed | Five_Nights_at_Freddy's |
| 754. | presidential | 31: [12, 6.0] | presidential 's election | United_States_presidential_election |
| 755. | continues | 31: [12, 6.0] | continues 's iraq | Iraq |
| 756. | appear | 33: [12, 6.0] | appear 's american | United_States |
| 757. | r | 35: [12, 6.0] | r military 's | R&R_(military) |
| 758. | lt | 35: [12, 6.0] | lt military gen | Rashtriya_Indian_Military_College |
| 759. | pakistan | 35: [12, 6.0] | pakistan 's pakistani | Pakistanis |
| 760. | former | 41: [12, 6.0] | former 's iraq | List_of_former_equipment_of_the_Iraqi_Army |
| 761. | set | 47: [12, 6.0] | set 's iraq | Iraq_War |
| 762. | kuchma | 49: [30, 6.0] | kuchma 's ukraine | Leonid_Kuchma |
| 763. | -year-old | 50: [12, 6.0] | -year-old 's israeli | Mossad |
| 764. | american | 50: [12, 6.0] | american iraq 's | American-led_intervention_in_Iraq_(2014–present) |
| 765. | report | 28: [53, 5.89], 35: [50, 5.0], 41: [11, 5.5] | report 's iraq | Iraq_Report |
| 766. | weapons | 17: [22, 5.5], 28: [29, 5.8] | weapons 's iraq | Iraq_and_weapons_of_mass_destruction |
| 767. | pres | 32: [23, 5.75] | pres 's bush | George_H._W._Bush |
| 768. | helicopter | 33: [17, 5.67] | helicopter israeli american | Israel–United_States_relations |
| 769. | official | 43: [17, 5.67] | official 's says | Say_Say_Say |
| 770. | democratic | 2: [11, 5.5], 11: [11, 5.5] | democratic 's party | Democratic_Party_(United_States) |
| 771. | party | 2: [11, 5.5] | party 's prime | List_of_prime_ministers_of_India |
| 772. | nations | 2: [11, 5.5] | nations united 's | United_Nations |
| 773. | interim | 3: [11, 5.5], 22: [20, 5.0] | interim iraqi iraq | Iraq_War |
| 774. | fingerprinting | 3: [11, 5.5] | fingerprinting us brazil | DNA_profiling |
| 775. | programs | 5: [11, 5.5] | programs 's nuclear | Nuclear_program_of_Iran |
| 776. | house | 5: [22, 5.5], 43: [11, 5.5] | house 's bush | George_W._Bush |
| 777. | afghan | 5: [11, 5.5], 44: [10, 5.0] | afghan afghanistan 's | Flag_of_Afghanistan |
| 778. | less | 7: [11, 5.5] | less 's says | Say_Less_(album) |
| 779. | produce | 7: [11, 5.5] | produce nuclear 's | Nuclear_electromagnetic_pulse |
| 780. | greek | 7: [15, 5.0], 17: [11, 5.5] | greek cyprus 's | Greek_Cypriots |
| 781. | train | 8: [11, 5.5] | train madrid 's | 2004_Madrid_train_bombings |
| 782. | greater | 12: [11, 5.5] | greater 's hong | Guangdong-Hong_Kong-Macau_Greater_Bay_Area |
| 783. | ago | 12: [11, 5.5] | ago 's years | All_Those_Years_Ago |
| 784. | chemical | 13: [11, 5.5] | chemical weapons 's | Chemical_weapon |
| 785. | carried | 13: [11, 5.5] | carried 's says | The_Things_They_Carried |
| 786. | southern | 15: [11, 5.5] | southern 's american | Southern_American_English |
| 787. | loyal | 15: [11, 5.5] | loyal american najaf | Peace_Companies |
| 788. | leading | 16: [11, 5.5] | leading 's american | United_States |
| 789. | must | 16: [11, 5.5] | must 's says | Say's_law |
| 790. | voting | 18: [11, 5.5] | voting 's elections | Elections_in_the_United_States |
| 791. | red | 19: [11, 5.5] | red military cross | International_Red_Cross_and_Red_Crescent_Movement |
| 792. | pictures | 20: [11, 5.5] | pictures images photos | ICloud_leaks_of_celebrity_photos |
| 793. | calls | 20: [11, 5.5], 23: [11, 5.5], 44: [11, 5.5] | calls 's says | Say's_law |
| 794. | th | 21: [11, 5.5] | th 's anniversary | Anniversary |
| 795. | g.i | 23: [11, 5.5] | g.i american 's | G.I._Joe |
| 796. | continue | 24: [11, 5.5] | continue 's iraq | Iraq |
| 797. | summer | 24: [11, 5.5] | summer 's iraq | Iraq_War |
| 798. | around | 25: [11, 5.5] | around 's iraq | Iraq |
| 799. | osama | 25: [11, 5.5] | osama laden qaeda | Hamza_bin_Laden |
| 800. | keep | 26: [11, 5.5] | keep 's iraq | 2003_invasion_of_Iraq |
| 801. | hundreds | 27: [11, 5.5] | hundreds 's iraq | Iraq_War |
| 802. | study | 27: [11, 5.5] | study iraq 's | Iraq_Study_Group |
| 803. | operative | 32: [11, 5.5] | operative qaeda officials | Al-Qaeda |
| 804. | experts | 32: [11, 5.5] | experts 's say | Expert_system |
| 805. | results | 34: [11, 5.5] | results 's election | Attempts_to_overturn_the_2020_United_States_presidential_election |
| 806. | attack | 35: [33, 5.5] | attack 's killed | List_of_fatal_cougar_attacks_in_North_America |
| 807. | wounded | 35: [11, 5.5] | wounded killed american | List_of_United_States_Congress_members_killed_or_wounded_in_office |
| 808. | sept. | 37: [11, 5.5] | sept. united iraq | 2003_invasion_of_Iraq |
| 809. | uranium | 39: [11, 5.5] | uranium nuclear iran | Enriched_uranium |
| 810. | parliamentary | 44: [11, 5.5] | parliamentary 's elections | General_election |
| 811. | fatah | 49: [11, 5.5] | fatah palestinian arafat | Yasser_Arafat |
| 812. | sovereignty | 27: [27, 5.4] | sovereignty iraq iraqi | Islamic_State_of_Iraq_and_the_Levant |
| 813. | border | 12: [16, 5.33] | border 's israeli | Borders_of_Israel |
| 814. | kidnappings | 31: [16, 5.33] | kidnappings iraq american | Foreign_hostages_in_Iraq |
| 815. | states | 43: [16, 5.33] | states united 's | United_States |
| 816. | possible | 46: [16, 5.33] | possible 's says | Say_It's_Possible |
| 817. | threat | 32: [21, 5.25] | threat 's iraq | Iraq_War |
| 818. | debate | 2: [10, 5.0] | debate 's says | Debate |
| 819. | sentenced | 3: [10, 5.0] | sentenced prison years | List_of_longest_prison_sentences |
| 820. | rift | 3: [10, 5.0] | rift 's iraq | Iraqi_insurgency_(2003–2011) |
| 821. | guerrillas | 3: [10, 5.0] | guerrillas 's american | American_Guerrilla_in_the_Philippines |
| 822. | addresses | 4: [10, 5.0] | addresses iraq 's | 2003_invasion_of_Iraq |
| 823. | group | 5: [30, 5.0] | group 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 824. | bbc | 5: [25, 5.0] | bbc 's blair | Lionel_Blair |
| 825. | p | 7: [10, 5.0] | p 's iraq | Iraq_War |
| 826. | equipment | 7: [10, 5.0] | equipment nuclear 's | Nuclear_Suppliers_Group |
| 827. | eight | 9: [10, 5.0] | eight 's american | Ocean's_8 |
| 828. | documents | 9: [10, 5.0] | documents 's intelligence | Five_Eyes |
| 829. | issues | 9: [15, 5.0] | issues 's iraq | Environmental_issues_in_Iraq |
| 830. | secret | 9: [10, 5.0] | secret 's iraq | Iraq_and_weapons_of_mass_destruction |
| 831. | b | 10: [10, 5.0] | b 's russian | Sukhoi_S-70_Okhotnik-B |
| 832. | baghdad | 10: [10, 5.0] | baghdad iraq iraqi | Baghdad |
| 833. | sentence | 10: [10, 5.0] | sentence years prison | List_of_longest_prison_sentences |
| 834. | search | 10: [10, 5.0] | search 's iraq | Iraq_War |
| 835. | jamaica | 11: [10, 5.0] | jamaica aristide 's | Jean-Bertrand_Aristide |
| 836. | british | 12: [10, 5.0] | british 's iraq | Mandatory_Iraq |
| 837. | response | 12: [10, 5.0] | response 's says | Classical_conditioning |
| 838. | battle | 12: [10, 5.0] | battle 's american | List_of_American_Civil_War_battles |
| 839. | malaysia | 13: [10, 5.0] | malaysia nuclear 's | Nuclear_energy_in_Malaysia |
| 840. | corruption | 14: [10, 5.0] | corruption 's government | Corruption_in_local_government |
| 841. | bill | 14: [10, 5.0] | bill 's parliament | Fixed-term_Parliaments_Act_2011 |
| 842. | almost | 15: [10, 5.0] | almost 's iraq | Iraq |
| 843. | concerns | 15: [10, 5.0] | concerns 's iraq | Occupation_of_Iraq_(2003–2011) |
| 844. | blackwater | 15: [10, 5.0] | blackwater iraqi defense | Nisour_Square_massacre |
| 845. | offer | 16: [10, 5.0] | offer 's american | Vince_Offer |
| 846. | soldier | 16: [10, 5.0] | soldier american iraq | Iraqi_Army |
| 847. | month | 17: [10, 5.0] | month 's iraq | 2003_invasion_of_Iraq |
| 848. | weeks | 17: [10, 5.0] | weeks 's iraq | Iraq_War |
| 849. | linked | 17: [10, 5.0] | linked 's two | Linked_list |
| 850. | maj | 19: [10, 5.0] | maj gen military | Major_general |
| 851. | holding | 20: [10, 5.0] | holding 's iraq | Iraq_War |
| 852. | might | 20: [15, 5.0] | might 's iraq | Iraq |
| 853. | sivits | 20: [10, 5.0] | sivits abuse specialist | Abu_Ghraib_torture_and_prisoner_abuse |
| 854. | moscow | 21: [10, 5.0] | moscow russia 's | Moscow |
| 855. | place | 22: [10, 5.0] | place 's iraq | List_of_places_in_Iraq |
| 856. | assassination | 22: [10, 5.0] | assassination 's pakistani | Assassination_of_Benazir_Bhutto |
| 857. | withdraw | 23: [10, 5.0] | withdraw 's gaza | Gaza–Israel_conflict |
| 858. | appears | 24: [10, 5.0] | appears 's iraq | Iraq |
| 859. | well | 25: [10, 5.0] | well 's iraq | Iraq_War |
| 860. | details | 25: [10, 5.0] | details 's iraq | Iraq |
| 861. | colombia | 25: [10, 5.0] | colombia 's colombian | Colombians |
| 862. | philippine | 26: [10, 5.0] | philippine philippines arroyo | Gloria_Macapagal_Arroyo |
| 863. | wolfowitz | 26: [10, 5.0] | wolfowitz iraq sec | Paul_Wolfowitz |
| 864. | increase | 27: [10, 5.0] | increase 's says | Say's_law |
| 865. | western | 27: [10, 5.0] | western 's government | Government_of_Western_Australia |
| 866. | working | 28: [10, 5.0], 30: [10, 5.0] | working 's iraq | Iraq_War |
| 867. | private | 29: [10, 5.0] | private 's american | Privatization |
| 868. | fund | 29: [10, 5.0] | fund 's world | World_Wide_Fund_for_Nature |
| 869. | provide | 30: [10, 5.0] | provide 's iraq | Iraq_War |
| 870. | operations | 30: [10, 5.0] | operations iraq 's | Iraq_War |
| 871. | asia | 32: [15, 5.0] | asia world briefing | BBC_World_News |
| 872. | little | 32: [10, 5.0] | little 's iraq | Iraq_War |
| 873. | announce | 33: [10, 5.0] | announce 's iraq | Iraq |
| 874. | ayad | 33: [15, 5.0] | ayad iraqi allawi | Ayad_Allawi |
| 875. | homeland | 33: [10, 5.0] | homeland 's security | United_States_Secretary_of_Homeland_Security |
| 876. | kenya | 33: [10, 5.0] | kenya 's say | Kenya |
| 877. | audit | 34: [10, 5.0] | audit 's president | Election_audit |
| 878. | released | 35: [10, 5.0] | released 's iraq | Islamic_State_of_Iraq_and_the_Levant |
| 879. | shot | 35: [10, 5.0] | shot killed 's | List_of_murdered_hip_hop_musicians |
| 880. | bank | 40: [10, 5.0] | bank west israel | Israeli_West_Bank_barrier |
| 881. | top | 41: [10, 5.0] | top 's iraq | Iraq_War |
| 882. | cleric | 42: [10, 5.0] | cleric american iraqi | Muqtada_al-Sadr |
| 883. | agrees | 42: [10, 5.0] | agrees 's gaza | Gaza_War_(2008–2009) |
| 884. | saturday | 42: [10, 5.0] | saturday american 's | Saturday_Night_Live |
| 885. | country | 43: [20, 5.0] | country 's iraq | 2003_invasion_of_Iraq |
| 886. | `` | 43: [15, 5.0] | `` 's iraq | 2003_invasion_of_Iraq |
| 887. | chechen | 43: [10, 5.0] | chechen russian 's | Chechen–Russian_conflict |
| 888. | calling | 44: [10, 5.0] | calling 's iraq | Iraq |
| 889. | members | 44: [10, 5.0] | members 's iraq | 2003_invasion_of_Iraq |
| 890. | winner | 45: [10, 5.0] | winner election 's | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 891. | plan | 50: [15, 5.0] | plan 's sharon | Sharon_Carter |
| 892. | warning | 53: [10, 5.0] | warning 's iraq | 1993_cruise_missile_strikes_on_Iraq |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | voices | 12: [21, inf] | voices iraq geoff | Gulf_War |
| 2. | hamas | 13: [10, inf] | hamas israel leader | Hamas |
| 3. | hostage | 39: [10, inf] | hostage us 's | Iran_hostage_crisis |
| 4. | arafat | 44: [11, inf] | arafat 's yasser | Cause_of_Yasser_Arafat's_death |
| 5. | ukraine | 48: [18, inf] | ukraine poll 's | Languages_of_Ukraine |
| 6. | turkey | 51: [12, 12.0] | turkey 's press | Turkey |
| 7. | south | 16: [11, 11.0] | south africa korea | Koreans_in_South_Africa |
| 8. | blair | 6: [10, 10.0] | blair 's iraq | Tony_Blair |
| 9. | cold | 15: [10, 10.0] | cold jonathan steele | Jonathan_Steele |
| 10. | inquiry | 6: [17, 8.5] | inquiry 's wmd | Iraq_and_weapons_of_mass_destruction |
| 11. | madrid | 11: [17, 8.5] | madrid bomb bombings | 2004_Madrid_train_bombings |
| 12. | iraq | 2: [13, 6.5], 20: [15, 5.0], 38: [14, 7.0] | iraq us 's | 2003_invasion_of_Iraq |
| 13. | wmd | 6: [16, 5.33] | wmd bush iraq | Iraq_and_weapons_of_mass_destruction |
| 14. | saddam | 27: [16, 5.33] | saddam 's trial | Trial_of_Saddam_Hussein |
| 15. | kerry | 31: [10, 5.0] | kerry bush 's | 2004_United_States_presidential_election |
