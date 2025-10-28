# Dictionary containing every station in a given line and their order going north and south
# Only red, orange, green, and blue lines were completed as this was performed manually and
# those were the only lines of interest. Feel free to update for additional lines.
#
# This is only needed if you want the train tracker on the sides
#
# Order starts at 0

stations = {
    "40830": {
        "name": "18th"
    },
    "41120": {
        "name": "35th-Bronzeville-IIT",
        "green_order_north": 7,
        "green_order_south": 21
    },
    "40120": {
        "name": "35th/Archer",
        "orange_order_north": 4,
        "orange_order_south": 7
    },
    "41270": {
        "name": "43rd",
        "green_order_north": 5,
        "green_order_south": 23
    },
    "41080": {
        "name": "47th (Green Line)",
        "green_order_north": 4,
        "green_order_south": 24
    },
    "41230": {
        "name": "47th (Red Line)",
        "red_order_north": 6,
        "red_order_south": 26
    },
    "40130": {
        "name": "51st",
        "green_order_north": 4,
        "green_order_south": 24
    },
    "40580": {
        "name": "54th/Cermak"
    },
    "40910": {
        "name": "63rd",
        "red_order_north": 4,
        "red_order_south": 28
    },
    "40990": {
        "name": "69th",
        "red_order_north": 3,
        "red_order_south": 29
    },
    "40240": {
        "name": "79th",
        "red_order_north": 2,
        "red_order_south": 30
    },
    "41430": {
        "name": "87th",
        "red_order_north": 1,
        "red_order_south": 31
    },
    "40450": {
        "name": "95th",
        "red_order_north": 0,
        "red_order_south": 32
    },
    "40680": {
        "name": "Adams/Wabash",
        "orange_order_north": 15,
        "orange_order_south": 3,
        "green_order_north": 10,
        "green_order_south": 18
    },
    "41240": {
        "name": "Addison (Blue Line)",
        "blue_order_north": 25,
        "blue_order_south": 7
    },
    "41440": {
        "name": "Addison (Brown Line)"
    },
    "41420": {
        "name": "Addison (Red Line)",
        "red_order_north": 20,
        "red_order_south": 12
    },
    "41200": {
        "name": "Argyle",
        "red_order_north": 24,
        "red_order_south": 8
    },
    "40660": {
        "name": "Armitage"
    },
    "40290": {
        "name": "Ashland/63rd",
        "green_order_north": 0,
        "green_order_south": 28
    },
    "40170": {
        "name": "Ashland (Green, Pink Lines)",
        "green_order_north": 16,
        "green_order_south": 12
    },
    "41060": {
        "name": "Ashland (Orange Line)",
        "orange_order_north": 5,
        "orange_order_south": 6
    },
    "40010": {
        "name": "Austin (Blue Line)",
        "blue_order_north": 3,
        "blue_order_south": 29
    },
    "41260": {
        "name": "Austin (Green Line)",
        "green_order_north": 25,
        "green_order_south": 3
    },
    "41320": {
        "name": "Belmont (Red, Brown, Purple Lines)",
        "red_order_north": 19,
        "red_order_south": 13
    },
    "40060": {
        "name": "Belmont (Blue Line)",
        "blue_order_north": 24,
        "blue_order_south": 8
    },
    "40340": {
        "name": "Berwyn",
        "red_order_north": 25,
        "red_order_south": 7
    },
    "41380": {
        "name": "Bryn Mawr",
        "red_order_north": 26,
        "red_order_south": 6
    },
    "40440": {
        "name": "California (Pink Line)"
    },
    "41360": {
        "name": "California (Green Line)",
        "green_order_north": 18,
        "green_order_south": 10
    },
    "40570": {
        "name": "California (Blue Line-O'Hare Branch)",
        "blue_order_north": 22,
        "blue_order_south": 10
    },
    "40780": {
        "name": "Central Park"
    },
    "40280": {
        "name": "Central (Green Line)",
        "green_order_north": 24,
        "green_order_south": 4
    },
    "41250": {
        "name": "Central (Purple Line)"
    },
    "41000": {
        "name": "Cermak-Chinatown",
        "red_order_north": 8,
        "red_order_south": 24
    },
    "41690": {
        "name": "Cermak-McCormick Place",
        "green_order_north": 8,
        "green_order_south": 20
    },
    "41410": {
        "name": "Chicago (Blue Line)",
        "blue_order_north": 18,
        "blue_order_south": 14
    },
    "40710": {
        "name": "Chicago (Brown Line)"
    },
    "41450": {
        "name": "Chicago (Red Line)",
        "red_order_north": 15,
        "red_order_south": 17
    },
    "40420": {
        "name": "Cicero (Pink Line)"
    },
    "40970": {
        "name": "Cicero (Blue Line-Forest Park Branch)",
        "blue_order_north": 4,
        "blue_order_south": 28
    },
    "40480": {
        "name": "Cicero (Green Line)",
        "green_order_north": 21,
        "green_order_south": 7
    },
    "40630": {
        "name": "Clark/Division",
        "red_order_north": 16,
        "red_order_south": 16
    },
    "40380": {
        "name": "Clark/Lake",
        "blue_order_north": 14,
        "blue_order_south": 18,
        "orange_order_north": 12,
        "orange_order_south": 0,
        "green_order_north": 13,
        "green_order_south": 15
    },
    "40430": {
        "name": "Clinton (Blue Line)",
        "blue_order_north": 11,
        "blue_order_south": 21
    },
    "41160": {
        "name": "Clinton (Green Line)",
        "green_order_north": 14,
        "green_order_south": 14
    },
    "41670": {
        "name": "Conservatory",
        "green_order_north": 20,
        "green_order_south": 8
    },
    "40230": {
        "name": "Cumberland",
        "blue_order_north": 30,
        "blue_order_south": 2
    },
    "40090": {
        "name": "Damen (Brown Line)"
    },
    "41710": {
        "name": "Damen (Green Line)",
        "green_order_north": 17,
        "green_order_south": 11
    },
    "40210": {
        "name": "Damen (Pink Line)"
    },
    "40590": {
        "name": "Damen (Blue Line-O'Hare Branch)",
        "blue_order_north": 20,
        "blue_order_south": 12
    },
    "40050": {
        "name": "Davis"
    },
    "40690": {
        "name": "Dempster"
    },
    "40140": {
        "name": "Dempster-Skokie"
    },
    "40530": {
        "name": "Diversey"
    },
    "40320": {
        "name": "Division",
        "blue_order_north": 19,
        "blue_order_south": 13
    },
    "40720": {
        "name": "Cottage Grove",
        "green_order_north": 0,
        "green_order_south": 28
    },
    "40390": {
        "name": "Forest Park",
        "blue_order_north": 0,
        "blue_order_south": 32
    },
    "40520": {
        "name": "Foster"
    },
    "40870": {
        "name": "Francisco"
    },
    "41220": {
        "name": "Fullerton",
        "red_order_north": 18,
        "red_order_south": 14
    },
    "40510": {
        "name": "Garfield (Green Line)",
        "green_order_north": 2,
        "green_order_south": 26
    },
    "41170": {
        "name": "Garfield (Red Line)",
        "red_order_north": 5,
        "red_order_south": 27
    },
    "40490": {
        "name": "Grand (Blue Line)",
        "blue_order_north": 15,
        "blue_order_south": 17
    },
    "40330": {
        "name": "Grand (Red Line)",
        "red_order_north": 14,
        "red_order_south": 18
    },
    "40760": {
        "name": "Granville",
        "red_order_north": 28,
        "red_order_south": 4
    },
    "40940": {
        "name": "Halsted (Green Line)",
        "green_order_north": 1,
        "green_order_south": 27
    },
    "41130": {
        "name": "Halsted (Orange Line)",
        "orange_order_north": 4,
        "orange_order_south": 7
    },
    "40980": {
        "name": "Harlem (Blue Line-Forest Park Branch)",
        "blue_order_north": 1,
        "blue_order_south": 31
    },
    "40020": {
        "name": "Harlem (Green Line)",
        "green_order_north": 28,
        "green_order_south": 0
    },
    "40750": {
        "name": "Harlem (Blue Line-O'Hare Branch)",
        "blue_order_north": 29,
        "blue_order_south": 3
    },
    "40850": {
        "name": "Harold Washington Library-State/Van Buren",
        "orange_order_north": 6,
        "orange_order_south": 0
    },
    "41490": {
        "name": "Harrison",
        "red_order_north": 10,
        "red_order_south": 22
    },
    "40900": {
        "name": "Howard",
        "red_order_north": 32,
        "red_order_south": 0
    },
    "40810": {
        "name": "Illinois Medical District",
        "blue_order_north": 8,
        "blue_order_south": 24
    },
    "40300": {
        "name": "Indiana",
        "green_order_north": 6,
        "green_order_south": 22
    },
    "40550": {
        "name": "Irving Park (Blue Line)",
        "blue_order_north": 26,
        "blue_order_south": 6
    },
    "41460": {
        "name": "Irving Park (Brown Line)"
    },
    "40070": {
        "name": "Jackson (Blue Line)",
        "blue_order_north": 13,
        "blue_order_south": 19
    },
    "40560": {
        "name": "Jackson (Red Line)",
        "red_order_north": 11,
        "red_order_south": 21
    },
    "41190": {
        "name": "Jarvis",
        "red_order_north": 31,
        "red_order_south": 1
    },
    "41280": {
        "name": "Jefferson Park",
        "blue_order_north": 28,
        "blue_order_south": 4
    },
    "41180": {
        "name": "Kedzie (Brown Line)"
    },
    "41040": {
        "name": "Kedzie (Pink Line)"
    },
    "41070": {
        "name": "Kedzie (Green Line)",
        "green_order_north": 19,
        "green_order_south": 9
    },
    "40250": {
        "name": "Kedzie-Homan (Blue Line)",
        "blue_order_north": 6,
        "blue_order_south": 26
    },
    "41150": {
        "name": "Kedzie (Orange Line)",
        "orange_order_north": 2,
        "orange_order_south": 9
    },
    "41290": {
        "name": "Kimball"
    },
    "41140": {
        "name": "King Drive",
        "green_order_north": 1,
        "green_order_south": 27
    },
    "40600": {
        "name": "Kostner"
    },
    "41660": {
        "name": "Lake",
        "red_order_north": 13,
        "red_order_south": 19
    },
    "40700": {
        "name": "Laramie",
        "green_order_north": 23,
        "green_order_south": 5
    },
    "41340": {
        "name": "LaSalle",
        "blue_order_north": 12,
        "blue_order_south": 20
    },
    "40160": {
        "name": "LaSalle/Van Buren",
        "orange_order_north": 7,
        "orange_order_south": 0
    },
    "40770": {
        "name": "Lawrence",
        "red_order_north": 23,
        "red_order_south": 9
    },
    "41050": {
        "name": "Linden"
    },
    "41020": {
        "name": "Logan Square",
        "blue_order_north": 23,
        "blue_order_south": 9
    },
    "41300": {
        "name": "Loyola",
        "red_order_north": 29,
        "red_order_south": 3
    },
    "40270": {
        "name": "Main"
    },
    "40930": {
        "name": "Midway",
        "orange_order_north": 0,
        "orange_order_south": 11
    },
    "40790": {
        "name": "Monroe (Blue Line)",
        "blue_order_north": 14,
        "blue_order_south": 18
    },
    "41090": {
        "name": "Monroe (Red Line)",
        "red_order_north": 12,
        "red_order_south": 20
    },
    "41330": {
        "name": "Montrose (Blue Line)",
        "blue_order_north": 27,
        "blue_order_south": 5
    },
    "41500": {
        "name": "Montrose (Brown Line)"
    },
    "41510": {
        "name": "Morgan",
        "green_order_north": 15,
        "green_order_south": 13
    },
    "40100": {
        "name": "Morse",
        "red_order_north": 30,
        "red_order_south": 2
    },
    "40650": {
        "name": "North/Clybourn",
        "red_order_north": 17,
        "red_order_south": 15
    },
    "40400": {
        "name": "Noyes"
    },
    "40180": {
        "name": "Oak Park (Blue Line)",
        "blue_order_north": 2,
        "blue_order_south": 30
    },
    "41350": {
        "name": "Oak Park (Green Line)",
        "green_order_north": 27,
        "green_order_south": 1
    },
    "41680": {
        "name": "Oakton-Skokie"
    },
    "40890": {
        "name": "O'Hare",
        "blue_order_north": 32,
        "blue_order_south": 0
    },
    "41310": {
        "name": "Paulina"
    },
    "41030": {
        "name": "Polk"
    },
    "40150": {
        "name": "Pulaski (Pink Line)"
    },
    "40920": {
        "name": "Pulaski (Blue Line-Forest Park Branch)",
        "blue_order_north": 5,
        "blue_order_south": 27
    },
    "40030": {
        "name": "Pulaski (Green Line)",
        "green_order_north": 21,
        "green_order_south": 7
    },
    "40960": {
        "name": "Pulaski (Orange Line)",
        "orange_order_north": 1,
        "orange_order_south": 10
    },
    "40040": {
        "name": "Quincy/Wells",
        "orange_order_north": 8,
        "orange_order_south": 0
    },
    "40470": {
        "name": "Racine",
        "blue_order_north": 9,
        "blue_order_south": 23
    },
    "40610": {
        "name": "Ridgeland",
        "green_order_north": 26,
        "green_order_south": 2
    },
    "41010": {
        "name": "Rockwell"
    },
    "41400": {
        "name": "Roosevelt",
        "red_order_north": 9,
        "red_order_south": 23,
        "orange_order_north": 7,
        "orange_order_south": 4,
        "green_order_north": 9,
        "green_order_south": 19
    },
    "40820": {
        "name": "Rosemont",
        "blue_order_north": 31,
        "blue_order_south": 1
    },
    "40800": {
        "name": "Sedgwick"
    },
    "40080": {
        "name": "Sheridan",
        "red_order_north": 19,
        "red_order_south": 13
    },
    "40840": {
        "name": "South Boulevard"
    },
    "40360": {
        "name": "Southport"
    },
    "40190": {
        "name": "Sox-35th",
        "red_order_north": 7,
        "red_order_south": 25
    },
    "40260": {
        "name": "State/Lake",
        "orange_order_north": 12,
        "orange_order_south": 1,
        "green_order_north": 12,
        "green_order_south": 16
    },
    "40880": {
        "name": "Thorndale",
        "red_order_north": 27,
        "red_order_south": 5
    },
    "40350": {
        "name": "UIC-Halsted",
        "blue_order_north": 10,
        "blue_order_south": 22
    },
    "41700": {
        "name": "Washington/Wabash",
        "orange_order_north": 12,
        "orange_order_south": 2,
        "green_order_north": 11,
        "green_order_south": 17
    },
    "40730": {
        "name": "Washington/Wells",
        "orange_order_north": 11,
        "orange_order_south": 0
    },
    "40370": {
        "name": "Washington (Blue Line)",
        "blue_order_north": 13,
        "blue_order_south": 19
    },
    "41210": {
        "name": "Wellington"
    },
    "41480": {
        "name": "Western (Brown Line)"
    },
    "40740": {
        "name": "Western (Pink Line)"
    },
    "40220": {
        "name": "Western (Blue Line-Forest Park Branch)",
        "blue_order_north": 1,
        "blue_order_south": 31
    },
    "40670": {
        "name": "Western (Blue Line-O'Hare Branch)",
        "blue_order_north": 7,
        "blue_order_south": 25
    },
    "40310": {
        "name": "Western (Orange Line)",
        "orange_order_north": 3,
        "orange_order_south": 8
    },
    "40540": {
        "name": "Wilson",
        "red_order_north": 20,
        "red_order_south": 12
    }
}
