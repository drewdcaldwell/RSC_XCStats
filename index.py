"""

River States Conference Cross Country Results Puller

"""


teams = {
    "Alice Lloyd"             :  "https://www.tfrrs.org/teams/xc/KY_college_m_Alice_Lloyd.html",
    "Brescia"                 :  "https://www.tfrrs.org/teams/xc/KY_college_m_Brescia.html",
    "IU Columbus"             :  "https://www.tfrrs.org/teams/xc/IN_college_m_IUPUC.html",
    "Indiana East"            :  "https://www.tfrrs.org/teams/xc/IN_college_m_Indiana_East.html",
    "Indiana Kokomo"          :  "https://www.tfrrs.org/teams/xc/IN_college_m_Indiana_Kokomo.html",
    "Midway"                  :  "https://www.tfrrs.org/teams/xc/KY_college_m_Midway.html",
    "Oakland City"            :  "https://www.tfrrs.org/teams/xc/IN_college_m_Oakland_City.html",
    "Rio Grande"              :  "https://www.tfrrs.org/teams/xc/OH_college_m_Rio_Grande.html",
    "Shawnee State"           :  "https://www.tfrrs.org/teams/xc/OH_college_m_Shawnee_State.html",
    "St. Mary-of-the-Woods"   :  "https://www.tfrrs.org/teams/xc/IN_college_m_St_Mary-of-the-Woods.html",
    "WVU Tech"                :  "https://www.tfrrs.org/teams/xc/WV_college_m_West_Virginia_Tech.html"
}


for team in teams:
    print (teams[team])