# Keywords with the highest 'interestingness' in 2010

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
| 1. | two | 1: [10, inf] | two killed officials | American_fatalities_and_injuries_of_the_2012_Benghazi_attack |
| 2. | prime | 1: [10, 5.0], 29: [10, inf] | prime minister government | Prime_minister |
| 3. | leader | 1: [20, 10.0], 4: [10, inf], 18: [20, 5.0], 31: [10, 10.0], 34: [17, 8.5], 50: [12, 6.0] | leader president minister | Minister-president |
| 4. | three | 1: [10, inf] | three killed officials | Threatening_government_officials_of_the_United_States |
| 5. | suicide | 1: [10, 5.0], 20: [10, inf] | suicide attack bomber | Suicide_attack |
| 6. | haiti | 2: [22, inf] | haiti earthquake aid | 2010_Haiti_earthquake |
| 7. | google | 2: [16, inf] | google china u.s. | Google_China |
| 8. | relief | 2: [11, inf] | relief aid haiti | 2010_Haiti_earthquake |
| 9. | elections | 3: [10, inf] | elections party iraq | Elections_in_Iraq |
| 10. | gates | 3: [12, inf], 10: [12, inf] | gates defense secretary | Robert_Gates |
| 11. | shiite | 5: [10, inf] | shiite iraq iraqi | Sons_of_Iraq |
| 12. | pakistan | 5: [13, 6.5], 39: [11, 11.0], 42: [11, inf] | pakistan u.s. taliban | Tehrik-i-Taliban_Pakistan |
| 13. | candidates | 5: [11, inf] | candidates election iraq | Elections_in_Iraq |
| 14. | clinton | 7: [16, 8.0], 48: [11, inf] | clinton state secretary | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 15. | women | 7: [10, inf] | women rights afghan | Women_in_Afghanistan |
| 16. | vote | 9: [15, 15.0], 18: [11, inf], 37: [15, inf] | vote election minister | Prime_Minister_of_Spain |
| 17. | obama | 10: [11, inf] | obama president u.s. | Barack_Obama |
| 18. | report | 10: [11, 5.5], 50: [14, inf] | report says u.n. | Woodbury_matrix_identity |
| 19. | north | 12: [12, inf], 16: [24, 6.0] | north korea south | North_Korea–South_Korea_relations |
| 20. | korea | 12: [11, 11.0], 20: [11, 11.0], 31: [12, inf], 45: [16, 8.0] | korea north south | North_Korea–South_Korea_relations |
| 21. | polish | 14: [11, inf] | polish poland crash | Smolensk_air_disaster |
| 22. | iraqi | 16: [10, 5.0], 36: [11, inf] | iraqi iraq government | Iraqi_Kurdistan |
| 23. | nato | 16: [13, inf], 26: [11, 5.5], 46: [10, 5.0] | nato afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 24. | jong-il | 18: [10, inf] | jong-il north korea | Kim_Jong-il |
| 25. | monaco | 19: [10, inf] | monaco schumacher grand | Michael_Schumacher |
| 26. | sanctions | 20: [14, inf], 23: [14, 7.0] | sanctions iran nuclear | Sanctions_against_Iran |
| 27. | europe | 20: [10, inf] | europe european u.s. | European_Union |
| 28. | base | 20: [16, inf] | base u.s. afghanistan | United_States_invasion_of_Afghanistan |
| 29. | accused | 21: [10, inf] | accused u.s. government | Zionist_Occupation_Government_conspiracy_theory |
| 30. | gang | 21: [10, inf] | gang leader jamaica | Shower_Posse |
| 31. | turkey | 22: [21, 10.5], 26: [11, inf] | turkey israel raid | Gaza_flotilla_raid |
| 32. | effort | 23: [12, 6.0], 26: [10, inf] | effort u.s. iran | Iran–United_States_relations |
| 33. | kyrgyz | 24: [10, inf] | kyrgyz president violence | Kyrgyz_Revolution_of_2010 |
| 34. | abuse | 25: [10, inf] | abuse pope church | Catholic_Church_sexual_abuse_cases |
| 35. | gas | 25: [14, inf] | gas police belarus | 2020–2021_Belarusian_protests |
| 36. | belarus | 25: [14, inf] | belarus russia gas | Belarus–Russia_relations |
| 37. | whaling | 25: [10, inf] | whaling japan japanese | Whaling_in_Japan |
| 38. | mcchrystal | 25: [13, inf] | mcchrystal gen. stanley | Stanley_A._McChrystal |
| 39. | church | 25: [10, inf] | church abuse pope | Catholic_Church_sexual_abuse_cases |
| 40. | japan | 27: [10, inf] | japan minister party | Liberal_Democratic_Party_(Japan) |
| 41. | uganda | 28: [13, inf] | uganda attacks bombings | 2010_Kampala_bombings |
| 42. | south | 31: [10, 5.0], 45: [11, inf] | south korea north | North_Korea–South_Korea_relations |
| 43. | election | 32: [17, 8.5], 44: [12, inf], 47: [11, 5.5] | election vote president | List_of_United_States_presidential_elections_in_which_the_winner_lost_the_popular_vote |
| 44. | ramadan | 32: [10, inf] | ramadan iraqi kashmir | India–Iraq_relations |
| 45. | former | 34: [14, inf] | former president minister | List_of_presidents_of_India |
| 46. | weekend | 34: [10, inf] | weekend killed grand | 1994_San_Marino_Grand_Prix |
| 47. | miners | 34: [10, inf] | miners trapped chile | 2010_Copiapó_mining_accident |
| 48. | states | 35: [11, inf] | states united u.s. | U.S._state |
| 49. | iran | 36: [12, inf] | iran nuclear sanctions | Sanctions_against_Iran |
| 50. | ferrari | 36: [10, inf] | ferrari team alonso | Scuderia_Ferrari |
| 51. | roma | 37: [14, inf] | roma france european | Romani_people |
| 52. | pope | 37: [12, inf] | pope abuse benedict | The_Two_Popes |
| 53. | sludge | 40: [10, inf] | sludge red hungary | Ajka_alumina_plant_accident |
| 54. | prize | 40: [11, inf], 49: [13, inf] | prize nobel peace | Nobel_Peace_Prize |
| 55. | european | 42: [10, inf] | european union europe | European_Union |
| 56. | cities | 42: [10, inf] | cities india attacks | 2008_Mumbai_attacks |
| 57. | results | 47: [10, inf] | results election president | Attempts_to_overturn_the_2020_United_States_presidential_election |
| 58. | view | 48: [11, inf] | view many reports | Mountain_View,_California |
| 59. | nobel | 49: [16, inf] | nobel prize china | Nobel_Prize_in_Literature |
| 60. | use | 51: [10, inf] | use north korea | North_Korea |
| 61. | raid | 22: [23, 23.0] | raid israel killed | Operation_Entebbe |
| 62. | wikileaks | 48: [18, 18.0] | wikileaks founder assange | Indictment_and_arrest_of_Julian_Assange |
| 63. | friday | 44: [16, 16.0] | friday china killed | Friday_the_13th_(2009_film) |
| 64. | u.n. | 7: [15, 15.0] | u.n. iran report | Iran_and_weapons_of_mass_destruction |
| 65. | american | 1: [14, 14.0], 36: [25, 6.25] | american u.s. officials | List_of_states_and_territories_of_the_United_States |
| 66. | government | 1: [14, 14.0] | government u.s. president | Federal_government_of_the_United_States |
| 67. | afghanistan | 1: [26, 13.0], 49: [14, 7.0] | afghanistan afghan u.s. | Soviet–Afghan_War |
| 68. | ban | 5: [13, 13.0] | ban u.n. secretary | Ban_Ki-moon |
| 69. | gaza | 22: [26, 13.0] | gaza israel israeli | Gaza–Israel_conflict |
| 70. | official | 1: [12, 12.0] | official pakistan says | Pakistan |
| 71. | attack | 8: [10, 10.0], 31: [12, 12.0], 47: [10, 10.0] | attack killed police | 2016_shooting_of_Dallas_police_officers |
| 72. | party | 11: [12, 12.0] | party minister prime | Prime_Minister_of_the_United_Kingdom |
| 73. | moscow | 13: [12, 12.0] | moscow russia russian | Moscow |
| 74. | russian | 26: [12, 12.0] | russian russia spy | Illegals_Program |
| 75. | china | 2: [34, 11.33], 15: [16, 5.33], 29: [17, 8.5], 38: [22, 11.0] | china chinese u.s. | China |
| 76. | military | 1: [11, 11.0], 44: [15, 7.5] | military u.s. american | United_States_Armed_Forces |
| 77. | killing | 7: [11, 11.0], 14: [11, 5.5] | killing least people | Mass_killings_under_communist_regimes |
| 78. | opposition | 7: [10, 5.0], 11: [11, 11.0] | opposition iran party | Political_parties_in_Iran |
| 79. | police | 9: [22, 11.0] | police officers attack | 2016_shooting_of_Dallas_police_officers |
| 80. | top | 9: [11, 11.0] | top u.s. pakistan | Pakistan–United_States_relations |
| 81. | taliban | 10: [11, 11.0] | taliban afghan afghanistan | War_in_Afghanistan_(2001–present) |
| 82. | ship | 20: [11, 11.0], 28: [11, 5.5] | ship korea north | North_Korean_ghost_ships |
| 83. | bank | 35: [22, 11.0] | bank west israel | Israeli_West_Bank_barrier |
| 84. | year | 36: [11, 11.0] | year last iran | Iran |
| 85. | talks | 37: [11, 11.0] | talks peace u.s. | Afghan_peace_process |
| 86. | may | 2: [10, 10.0] | may president u.s. | President_of_the_United_States |
| 87. | leaders | 3: [10, 5.0], 35: [10, 10.0], 45: [13, 6.5] | leaders president political | Party_leaders_of_the_United_States_Senate |
| 88. | defense | 3: [10, 10.0] | defense gates secretary | Robert_Gates |
| 89. | nation | 9: [10, 10.0] | nation president first | First_Nations |
| 90. | hamas | 9: [10, 10.0] | hamas gaza israel | Gaza_War_(2008–2009) |
| 91. | israel | 9: [10, 10.0] | israel gaza israeli | Gaza–Israel_conflict |
| 92. | first | 10: [12, 6.0], 12: [10, 10.0], 25: [13, 6.5], 28: [10, 5.0] | first since president | George_Washington |
| 93. | still | 14: [10, 10.0] | still u.s. government | U.S._state |
| 94. | forces | 15: [10, 10.0] | forces afghan security | Afghan_National_Security_Forces |
| 95. | labour | 17: [10, 10.0] | labour party brown | Labour_Party_(UK) |
| 96. | tuesday | 26: [10, 10.0] | tuesday president officials | Super_Tuesday |
| 97. | public | 28: [10, 10.0] | public minister obama | Barack_Obama |
| 98. | grand | 29: [10, 10.0] | grand prix race | 2020_Formula_One_World_Championship |
| 99. | team | 36: [10, 10.0] | team ferrari formula | Scuderia_Ferrari |
| 100. | fire | 48: [10, 10.0] | fire israel killed | Israeli–Lebanese_conflict |
| 101. | killed | 1: [16, 8.0], 5: [19, 9.5], 13: [17, 5.67], 40: [17, 5.67], 44: [12, 6.0] | killed people least | Persecution_of_Hazara_people_in_Quetta |
| 102. | court | 2: [17, 8.5], 13: [12, 6.0], 27: [10, 5.0] | court charges supreme | Supreme_Court_of_the_United_States |
| 103. | israeli | 22: [17, 8.5], 30: [11, 5.5] | israeli israel gaza | Gaza–Israel_conflict |
| 104. | india | 38: [16, 8.0] | india indian kashmir | Kashmir |
| 105. | near | 4: [15, 7.5] | near korea north | List_of_leaders_of_North_Korea |
| 106. | cables | 48: [29, 7.25] | cables u.s. diplomatic | United_States_diplomatic_cables_leak |
| 107. | capital | 4: [14, 7.0] | capital president attack | 2020_Aden_attacks |
| 108. | country | 1: [13, 6.5] | country president u.s. | List_of_presidents_of_the_United_States |
| 109. | rights | 2: [13, 6.5] | rights human court | European_Court_of_Human_Rights |
| 110. | aid | 2: [13, 6.5] | aid u.s. haiti | Foreign_aid_to_Haiti |
| 111. | nuclear | 6: [11, 5.5], 10: [13, 6.5], 28: [11, 5.5], 51: [11, 5.5] | nuclear iran program | Nuclear_program_of_Iran |
| 112. | vatican | 12: [13, 6.5] | vatican abuse pope | Catholic_Church_sexual_abuse_cases |
| 113. | iraq | 16: [10, 5.0], 42: [17, 5.67], 50: [13, 6.5] | iraq iraqi u.s. | Occupation_of_Iraq_(2003–2011) |
| 114. | activists | 22: [13, 6.5] | activists israeli israel | History_of_Israel |
| 115. | uzbeks | 24: [13, 6.5] | uzbeks kyrgyzstan ethnic | Uzbeks |
| 116. | russia | 44: [10, 5.0], 48: [13, 6.5] | russia russian president | President_of_Russia |
| 117. | group | 15: [12, 6.0] | group says militant | Lehi_(militant_group) |
| 118. | british | 17: [17, 5.67], 27: [12, 6.0] | british britain minister | Prime_Minister_of_the_United_Kingdom |
| 119. | flotilla | 22: [12, 6.0] | flotilla israel gaza | Gaza_flotilla_raid |
| 120. | last | 50: [12, 6.0] | last week month | ISO_week_date |
| 121. | tensions | 2: [17, 5.67] | tensions china north | China–North_Korea_border |
| 122. | secretary | 3: [17, 5.67] | secretary clinton state | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 123. | afghan | 1: [11, 5.5] | afghan taliban afghanistan | Taliban |
| 124. | people | 1: [11, 5.5], 44: [11, 5.5] | people killed least | List_of_people_killed_for_being_transgender |
| 125. | would | 2: [11, 5.5], 47: [10, 5.0] | would president u.s. | President_of_the_United_States |
| 126. | plan | 9: [11, 5.5] | plan president u.s. | President_of_the_United_States |
| 127. | security | 15: [11, 5.5] | security forces u.s. | United_States_Armed_Forces |
| 128. | korean | 16: [11, 5.5] | korean north south | North_Korea–South_Korea_relations |
| 129. | german | 29: [11, 5.5] | german germany church | Germany |
| 130. | peace | 34: [10, 5.0], 49: [11, 5.5] | peace talks israel | 2013–2014_Israeli–Palestinian_peace_talks |
| 131. | border | 5: [16, 5.33] | border korea pakistan | North_Korea–Pakistan_relations |
| 132. | attacks | 13: [16, 5.33] | attacks killed u.s. | 2012_Benghazi_attack |
| 133. | monday | 3: [10, 5.0] | monday president u.s. | Vice_President_of_the_United_States |
| 134. | thursday | 6: [15, 5.0] | thursday police china | Tommy_(TV_series) |
| 135. | part | 6: [10, 5.0] | part u.s. effort | Georgia_(U.S._state) |
| 136. | state | 9: [10, 5.0] | state clinton secretary | Hillary_Clinton's_tenure_as_Secretary_of_State |
| 137. | even | 12: [10, 5.0] | even president u.s. | List_of_presidents_of_the_United_States |
| 138. | thai | 14: [10, 5.0] | thai protesters bangkok | 2020_Thai_protests |
| 139. | say | 16: [10, 5.0] | say officials u.s. | Threatening_government_officials_of_the_United_States |
| 140. | aids | 19: [10, 5.0] | aids u.s. american | HIV/AIDS_in_the_United_States |
| 141. | crisis | 21: [10, 5.0] | crisis abuse political | Crisis |
| 142. | death | 21: [10, 5.0] | death toll president | List_of_wars_by_death_toll |
| 143. | law | 26: [10, 5.0] | law enforcement president | List_of_law_enforcement_agencies_in_the_District_of_Columbia |
| 144. | city | 31: [10, 5.0] | city people killed | List_of_people_killed_for_being_transgender |
| 145. | says | 32: [10, 5.0] | says u.s. iran | United_States_sanctions_against_Iran |
| 146. | parliament | 42: [10, 5.0] | parliament president vote | Casting_vote |

## Results - The Guardian:
|row|Keyword|week: [ total , changerate ]| computed query (advanced)  | matching result (advanced) |
|---|---|---|---|---|
| 1. | earthquake | 2: [15, inf], 15: [10, 5.0] | earthquake haiti chile | 2010_Haiti_earthquake |
| 2. | haiti | 2: [32, inf] | haiti earthquake 's | 2010_Haiti_earthquake |
| 3. | dubai | 7: [14, inf] | dubai killing murder | Assassination_of_Mahmoud_Al-Mabhouh |
| 4. | moscow | 13: [13, inf] | moscow 's mayor | Mayor_of_Moscow |
| 5. | volcano | 15: [10, inf] | volcano iceland ash | Eyjafjallajökull |
| 6. | attack | 22: [14, inf], 47: [10, 10.0] | attack gaza flotilla | Gaza_flotilla_raid |
| 7. | g | 25: [11, inf] | g summit aid | Group_of_Eight |
| 8. | spy | 26: [23, inf] | spy russian ring | Illegals_Program |
| 9. | ring | 26: [16, inf] | ring russian spy | Illegals_Program |
| 10. | anna | 26: [10, inf] | anna chapman spy | Anna_Chapman |
| 11. | chapman | 26: [10, inf] | chapman anna spy | Anna_Chapman |
| 12. | taliban | 29: [10, 10.0], 47: [10, inf] | taliban us afghanistan | War_in_Afghanistan_(2001–present) |
| 13. | logs | 29: [18, inf], 42: [15, inf] | logs afghanistan iraq | Iraq_War_documents_leak |
| 14. | peace | 35: [12, inf], 49: [11, 5.5] | peace talks middle | List_of_Middle_East_peace_proposals |
| 15. | roma | 37: [10, inf] | roma france 's | A.S._Roma |
| 16. | korean | 47: [10, inf] | korean north south | North_Korea–South_Korea_relations |
| 17. | embassy | 47: [62, inf] | embassy us cables | United_States_diplomatic_cables_leak |
| 18. | cables | 47: [61, inf] | cables us embassy | United_States_diplomatic_cables_leak |
| 19. | iranian | 47: [15, inf] | iranian us embassy | Iranian_Embassy_siege |
| 20. | russia | 48: [11, inf] | russia us 's | Russia–United_States_relations |
| 21. | president | 48: [20, inf] | president 's cables | United_States_diplomatic_cables_leak |
| 22. | berlusconi | 48: [11, inf], 50: [12, 6.0] | berlusconi silvio 's | Pier_Silvio_Berlusconi |
| 23. | pakistan | 48: [40, inf] | pakistan us cables | United_States_diplomatic_cables_leak |
| 24. | nicolas | 48: [10, inf] | nicolas sarkozy 's | Nicolas_Sarkozy |
| 25. | army | 48: [11, inf] | army us pakistan | Pakistan_Army |
| 26. | karzai | 48: [11, inf] | karzai hamid us | Hamid_Karzai |
| 27. | putin | 48: [17, inf] | putin vladimir cables | Public_image_of_Vladimir_Putin |
| 28. | nobel | 49: [10, inf] | nobel prize peace | Nobel_Peace_Prize |
| 29. | prize | 49: [10, inf] | prize nobel peace | Nobel_Peace_Prize |
| 30. | kosovo | 49: [11, inf] | kosovo us cables | Contents_of_the_United_States_diplomatic_cables_leak_(Europe) |
| 31. | wikileaks | 48: [56, 28.0] | wikileaks cables 's | United_States_diplomatic_cables_leak |
| 32. | gaza | 22: [43, 21.5] | gaza flotilla israel | Gaza_flotilla_raid |
| 33. | flotilla | 22: [40, 20.0] | flotilla gaza israel | Gaza_flotilla_raid |
| 34. | miners | 34: [15, 15.0] | miners chilean trapped | 2010_Copiapó_mining_accident |
| 35. | us | 47: [89, 14.83] | us cables embassy | United_States_diplomatic_cables_leak |
| 36. | talks | 35: [14, 14.0] | talks peace east | 2013–2014_Israeli–Palestinian_peace_talks |
| 37. | russian | 26: [27, 13.5], 48: [10, 10.0] | russian spy ring | Illegals_Program |
| 38. | afghanistan | 25: [12, 12.0], 29: [26, 13.0] | afghanistan us logs | Afghan_War_documents_leak |
| 39. | chilean | 34: [13, 13.0] | chilean miners trapped | 2010_Copiapó_mining_accident |
| 40. | middle | 35: [13, 13.0] | middle east peace | List_of_Middle_East_peace_proposals |
| 41. | sarkozy | 48: [13, 13.0] | sarkozy nicolas 's | Nicolas_Sarkozy |
| 42. | indian | 50: [13, 13.0] | indian us embassy | Foreign_relations_of_India |
| 43. | trapped | 34: [12, 12.0] | trapped miners chilean | 2010_Copiapó_mining_accident |
| 44. | israel | 22: [24, 8.0], 47: [11, 11.0] | israel gaza us | 2014_Gaza_War |
| 45. | chile | 41: [11, 11.0] | chile miners earthquake | 1960_Valdivia_earthquake |
| 46. | china | 15: [10, 10.0] | china 's us | China–United_States_relations |
| 47. | spanish | 48: [10, 10.0] | spanish us embassy | Embassy_of_the_United_States,_London |
| 48. | iran | 47: [33, 8.25] | iran us nuclear | Nuclear_program_of_Iran |
| 49. | benedict | 37: [15, 7.5] | benedict pope 's | Pope_Benedict_XVI |
| 50. | aung | 45: [15, 7.5] | aung san kyi | Aung_San_Suu_Kyi |
| 51. | san | 45: [15, 7.5] | san aung kyi | Aung_San_Suu_Kyi |
| 52. | suu | 45: [15, 7.5] | suu aung san | Aung_San_Suu_Kyi |
| 53. | kyi | 45: [15, 7.5] | kyi aung san | Aung_San_Suu_Kyi |
| 54. | pope | 37: [47, 6.71] | pope 's visit | Pope_Francis's_2015_visit_to_North_America |
| 55. | east | 35: [13, 6.5] | east middle peace | List_of_Middle_East_peace_proposals |
| 56. | north | 47: [16, 5.33] | north korea korean | North_Korea |
| 57. | korea | 47: [16, 5.33] | korea north south | North_Korea–South_Korea_relations |
| 58. | catholic | 11: [10, 5.0] | catholic church abuse | Catholic_Church_sexual_abuse_cases |
| 59. | british | 31: [10, 5.0] | british afghanistan killed | British_Forces_casualties_in_Afghanistan_since_2001 |
| 60. | uk | 48: [10, 5.0] | uk us cables | United_States_diplomatic_cables_leak |
| 61. | india | 50: [15, 5.0] | india us 's | India–United_States_relations |
