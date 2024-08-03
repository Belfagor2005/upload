# -*- coding: UTF-8 -*-

from enigma import eTimer, ePicLoad, gPixmapPtr, getPrevAsciiCode
from Tools.Directories import fileExists
from Tools.Directories import fileExists, pathExists
from Components.Pixmap import Pixmap
from Components.Input import Input
from Screens.InputBox import InputBox
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Components.AVSwitch import AVSwitch
from Components.Label import Label
from Components.ConfigList import ConfigList
from Components.Sources.StaticText import StaticText
from Components.ActionMap import NumberActionMap, ActionMap, HelpableActionMap
from Components.config import ConfigText, KEY_0, KEY_DELETE, KEY_BACKSPACE, config
from enigma import getDesktop, eListboxPythonMultiContent, eListbox, eTimer, gFont, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_WRAP, loadPNG
#from Plugins.Extensions.FreeServer.outils.InputBox import InputBox
from Plugins.Extensions.FreeServer.outils.Console3 import Console3
from Plugins.Extensions.FreeServer.outils.compat import compat_urlopen
from shutil import copyfile
import sys, time, os, shutil, re, requests, json, os, shutil, fileinput, warnings
from os import system as os_system
from PIL import Image
import re
import sys,os

dwidth = getDesktop(0).size().width()

###########################################################################
import requests , json, re,random,string,time,warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
N=9
rnd=''.join(random.choice(string.digits) for _ in range(N))
N=4
rnd2=''.join(random.choice(string.digits) for _ in range(N))
import os, os.path
import glob
import requests, re
import requests , json, re,random,string,time,warnings
from random import choice
RND_NAME=['Hisham','Pakita','Kristina','Lyna','Roberto','Lynch','Julia','Adams','Zakaria','Zinou','Cristina','Garza','Bethany','Cook','Clifton','Hunt','Austin','Estrada','Preston','Ruiz','Alfonso','Hodges',
          'Bombastic','Sackbut','Decaudate','RajaatHod','Luminous','Chronography','Abattoir','Cascer1Verily','Angelus','Lautitious','XxmiranSitar','Luminous','Aphicide','RichmitcSeton','RappelZizz','Luminous',
          'Rose','Franks','Mcknight','Murillo','Seymour','Sterling','Branch','Shepherd','Casey','Foreman','Stevens','Mock','Clinton','Franco','Means','Painter','Otero','Thacker','Glenn','Trent','Johns','Dupree',
          'Gagne','Fuentes','Fleming','Warren','Carpenter','Parham','Mclean','Snell','Nicholas','Jacobsen','Buck','Lambert','Fuller','Lanier','Wagner','Stevens','Everett','Gagnon','Piper','Faulkner','Vera','Shea',
          'Askew','Polk','Woodward','Wang','Carmichael','Cobb','Cannon','Marino','Granger','Hartley','Seymour','Warren','Stinson','Boyer','Cano','Lusk','King','Bruno','Fletcher','Tabor','Mcleod','Cornell','Phipps', 
          'Elliot','Lockhart','Britt','Downing','Cates','Rivera','Valentin','Jernigan','Henderson','Oneil','Riddle','Joiner','Riley','Rock','Ledbetter','Mercado','Felix','Ricks','Henley','Blanchard','Pierre','Meade',
          'Barron','Dawsonn','Lawson','Spencer','Andersen','Copeland','Shaw','Costa','Manley','Cooley','Cameron','Bridges','Crockett','Fitzpatrick','Jewell','Bruner','Whitman','Schroeder','Fountain','Brewster','Rhodes',
          'Mclean','Porter','Jimenez','Underwood','Sanchez','Galvan','Murillo','Childress','Covingto','Mcclure','Espinosa','Mathews','Thompson','Boudreaux','Samuel','Teague','Wesley','Grover','Gibson','Horton','Herring']

RND_LAST=['Huynh','Walker,''Henry','Kennedy','Joyce','Baxter','Gonzalez','Jimenez','Wise','Bass','Long','Chandler','Davila','Johns','Stark','Berry','Jackson','Cain','Aguirre','Shelton','Goodman','Colon','Hicks','Drake','Bradley','Curtis','McKenzie','James',
          'Hancock','Munoz','Mann','Crawford','Lutz','Rojas','Acevedo','Kramer','Hester','Blanchard','Zuniga','Shields','Gordon','Abbott','Gonzales','Stephenson','Wise','King','Nelson','Moore','Maldonado','Joseph','Mays','Brady','Foster','Goldman','Morton',
          'Ritter','Roach','Taylor','Finley','Lewis','Adkins','Briggs','Ramirez','Wallace','Alexander','Chung','Gentry','Lam','Bean','Duffy','Lawson','Owen','Washington','Hicks','Mosley','Pitts','Pham','May','Huang','Fernandez','Bradley','Lucas','Marshall',
          'Peterson','Walker','Garcia','Mcdaniel','Lowe','Marquez','Kemp','Owen','Erickson','Wilkinson','Montgomery','Rogers','Lewis','Sampson','Jenkins','Martin','Moody','Levy','Greer','Roy','Maynard','Perry','Riley','Burch','Guerra','Lester','Barker',
          'Stokes','Jones','Sheppard','Torres','Gross','Erickson','Montgomery','Jackson','Schroeder','Stephens','Wilson','Morales','Singleton','Clarke','Duncan','Perez','Rivers','Mcguire','Rosales','Mcknight','Daniels','Marino','Sanchez','Carlson',
          'Morrison','Smith','Johnson','Hamilton','Brown','Salas','Russo','Hartman','Holloway','Swanson','Stafford','Valverde','Waters','Briggs','Herrera','Booker','Stevens','Blevins','Vargas','Holder','Santos','Lewis','Davis','Harrison','Bruno',
          'Stevenson','Ellison','Harvey','Cruz','Huerta','Leblanc','Romero','Hudson','Bowers','Gonzales','Bowen','Mejia','Ortega','Baldwin','Aguilar','Orellana','Williamson','Benjamin','Robles','Taylor','Ramos','Salazar','Sparks','Perry','Young',
          'Guerrero','Bautista','Lozano','Joseph','Espinoza','Decker','Kirby','Harrington','Silva','Phillips','Holmes','Mathews','Harvey','Gomez','Stewart','Pennington','Hampton','Pineda','Scott','Mccarty','Mccormick','Miranda','Brown','Schmitt']

RND_ADRS=['777 Brockton Avenue, Abington MA 2351','30 Memorial Drive, Avon MA 2322','250 Hartford Avenue, Bellingham MA 2019',
          '700 Oak Street, Brockton MA 2301','66-4 Parkhurst Rd, Chelmsford MA 1824','591 Memorial Dr, Chicopee MA 1020','55 Brooksby Village Way, Danvers MA 1923',
          '137 Teaticket Hwy, East Falmouth MA 2536','42 Fairhaven Commons Way, Fairhaven MA 2719','374 William S Canning Blvd, Fall River MA 2721','121 Worcester Rd, Framingham MA 1701',
          '677 Timpany Blvd, Gardner MA 1440','337 Russell St, Hadley MA 1035','295 Plymouth Street, Halifax MA 2338','1775 Washington St, Hanover MA 2339','280 Washington Street, Hudson MA 1749',
          '20 Soojian Dr, Leicester MA 1524','11 Jungle Road, Leominster MA 1453','301 Massachusetts Ave, Lunenburg MA 1462','780 Lynnway, Lynn MA 1905','70 Pleasant Valley Street, Methuen MA 1844',
          '830 Curran Memorial Hwy, North Adams MA 1247','1470 S Washington St, North Attleboro MA 2760','506 State Road, North Dartmouth MA 2747','742 Main Street, North Oxford MA 1537','72 Main St, North Reading MA 1864',
          '200 Otis Street, Northborough MA 1532','180 North King Street, Northhampton MA 1060','555 East Main St, Orange MA 1364','555 Hubbard Ave-Suite 12, Pittsfield MA 1201','300 Colony Place, Plymouth MA 2360',
          '301 Falls Blvd, Quincy MA 2169','36 Paramount Drive, Raynham MA 2767','450 Highland Ave, Salem MA 1970','1180 Fall River Avenue, Seekonk MA 2771','1105 Boston Road, Springfield MA 1119','100 Charlton Road, Sturbridge MA 1566',
          '262 Swansea Mall Dr, Swansea MA 2777','333 Main Street, Tewksbury MA 1876','550 Providence Hwy, Walpole MA 2081','352 Palmer Road, Ware MA 1082','3005 Cranberry Hwy Rt 6 28, Wareham MA 2538',
          '250 Rt 59, Airmont NY 10901','141 Washington Ave Extension, Albany NY 12205','13858 Rt 31 W, Albion NY 14411','2055 Niagara Falls Blvd, Amherst NY 14228','101 Sanford Farm Shpg Center, Amsterdam NY 12010',
          '297 Grant Avenue, Auburn NY 13021','4133 Veterans Memorial Drive, Batavia NY 14020','6265 Brockport Spencerport Rd, Brockport NY 14420','5399 W Genesse St, Camillus NY 13031','3191 County rd 10, Canandaigua NY 14424',
          '30 Catskill, Catskill NY 12414','161 Centereach Mall, Centereach NY 11720','3018 East Ave, Central Square NY 13036','100 Thruway Plaza, Cheektowaga NY 14225','8064 Brewerton Rd, Cicero NY 13039',
          '5033 Transit Road, Clarence NY 14031','3949 Route 31, Clay NY 13041','139 Merchant Place, Cobleskill NY 12043','85 Crooked Hill Road, Commack NY 11725','872 Route 13, Cortlandville NY 13045',
          '279 Troy Road, East Greenbush NY 12061','2465 Hempstead Turnpike, East Meadow NY 11554','6438 Basile Rowe, East Syracuse NY 13057','25737 US Rt 11, Evans Mills NY 13637','901 Route 110, Farmingdale NY 11735',
          '2400 Route 9, Fishkill NY 12524','10401 Bennett Road, Fredonia NY 14063','1818 State Route 3, Fulton NY 13069','4300 Lakeville Road, Geneseo NY 14454','990 Route 5 20, Geneva NY 14456',
          '311 RT 9W, Glenmont NY 12077','200 Dutch Meadows Ln, Glenville NY 12302','100 Elm Ridge Center Dr, Greece NY 14626','1549 Rt 9, Halfmoon NY 12065','5360 Southwestern Blvd, Hamburg NY 14075',
          '103 North Caroline St, Herkimer NY 13350','1000 State Route 36, Hornell NY 14843','1400 County Rd 64, Horseheads NY 14845','135 Fairgrounds Memorial Pkwy, Ithaca NY 14850','2 Gannett Dr, Johnson City NY 13790',
          '233 Ave Ext, Johnstown NY 12095','601 Frank Stottile Blvd, Kingston NY 12401','350 E Fairmount Ave, Lakewood NY 14750','4975 Transit Rd, Lancaster NY 14086','579 Troy-Schenectady Road, Latham NY 12110',
          '5783 So Transit Road, Lockport NY 14094','7155 State Rt 12 S, Lowville NY 13367','425 Route 31, Macedon NY 14502','3222 State Rt 11, Malone NY 12953','200 Sunrise Mall, Massapequa NY 11758',
          '43 Stephenville St, Massena NY 13662','750 Middle Country Road, Middle Island NY 11953','470 Route 211 East, Middletown NY 10940','3133 E Main St, Mohegan Lake NY 10547','288 Larkin, Monroe NY 10950',
          '41 Anawana Lake Road, Monticello NY 12701','4765 Commercial Drive, New Hartford NY 13413','1201 Rt 300, Newburgh NY 12550','255 W Main St, Avon CT 6001','120 Commercial Parkway, Branford CT 6405',
          '1400 Farmington Ave, Bristol CT 6010','161 Berlin Road, Cromwell CT 6416','67 Newton Rd, Danbury CT 6810','656 New Haven Ave, Derby CT 6418','69 Prospect Hill Road, East Windsor CT 6088',
          '150 Gold Star Hwy, Groton CT 6340','900 Boston Post Road, Guilford CT 6437','2300 Dixwell Ave, Hamden CT 6514','495 Flatbush Ave, Hartford CT 6106','180 River Rd, Lisbon CT 6351',
          '420 Buckland Hills Dr, Manchester CT 6040','1365 Boston Post Road, Milford CT 6460','1100 New Haven Road, Naugatuck CT 6770','315 Foxon Blvd, New Haven CT 6513','164 Danbury Rd, New Milford CT 6776',
          '3164 Berlin Turnpike, Newington CT 6111','474 Boston Post Road, North Windham CT 6256','650 Main Ave, Norwalk CT 6851','680 Connecticut Avenue, Norwalk CT 6854','220 Salem Turnpike, Norwich CT 6360',
          '655 Boston Post Rd, Old Saybrook CT 6475','625 School Street, Putnam CT 6260','80 Town Line Rd, Rocky Hill CT 6067','465 Bridgeport Avenue, Shelton CT 6484','235 Queen St, Southington CT 6489',
          '150 Barnum Avenue Cutoff, Stratford CT 6614','970 Torringford Street, Torrington CT 6790','844 No Colony Road, Wallingford CT 6492','910 Wolcott St, Waterbury CT 6705','155 Waterford Parkway No, Waterford CT 6385',
          '515 Sawmill Road, West Haven CT 6516','2473 Hackworth Road, Adamsville AL 35005','630 Coonial Promenade Pkwy, Alabaster AL 35007','2643 Hwy 280 West, Alexander City AL 35010','540 West Bypass, Andalusia AL 36420',
          '5560 Mcclellan Blvd, Anniston AL 36206','1450 No Brindlee Mtn Pkwy, Arab AL 35016','1011 US Hwy 72 East, Athens AL 35611','973 Gilbert Ferry Road Se, Attalla AL 35954','1717 South College Street, Auburn AL 36830',
          '701 Mcmeans Ave, Bay Minette AL 36507','750 Academy Drive, Bessemer AL 35022','312 Palisades Blvd, Birmingham AL 35209','1600 Montclair Rd, Birmingham AL 35210','5919 Trussville Crossings Pkwy, Birmingham AL 35235',
          '9248 Parkway East, Birmingham AL 35206','1972 Hwy 431, Boaz AL 35957','10675 Hwy 5, Brent AL 35034','2041 Douglas Avenue, Brewton AL 36426','5100 Hwy 31, Calera AL 35040',
          '1916 Center Point Rd, Center Point AL 35215','1950 W Main St, Centre AL 35960','16077 Highway 280, Chelsea AL 35043','1415 7Th Street South, Clanton AL 35045','626 Olive Street Sw, Cullman AL 35055',
          '27520 Hwy 98, Daphne AL 36526','2800 Spring Avn SW, Decatur AL 35603','969 Us Hwy 80 West, Demopolis AL 36732','3300 South Oates Street, Dothan AL 36301','4310 Montgomery Hwy, Dothan AL 36303',
          '600 Boll Weevil Circle, Enterprise AL 36330','3176 South Eufaula Avenue, Eufaula AL 36027','7100 Aaron Aronov Drive, Fairfield AL 35064','10040 County Road 48, Fairhope AL 36533','3186 Hwy 171 North, Fayette AL 35555',
          '3100 Hough Rd, Florence AL 35630','2200 South Mckenzie St, Foley AL 36535','2001 Glenn Bldv Sw, Fort Payne AL 35968','340 East Meighan Blvd, Gadsden AL 35903','890 Odum Road, Gardendale AL 35071',
          '1608 W Magnolia Ave, Geneva AL 36340','501 Willow Lane, Greenville AL 36037','170 Fort Morgan Road, Gulf Shores AL 36542','11697 US Hwy 431, Guntersville AL 35976','42417 Hwy 195, Haleyville AL 35565',
          '1706 Military Street South, Hamilton AL 35570','1201 Hwy 31 NW, Hartselle AL 35640','209 Lakeshore Parkway, Homewood AL 35209','2780 John Hawkins Pkwy, Hoover AL 35244','5335 Hwy 280 South, Hoover AL 35242',
          '1007 Red Farmer Drive, Hueytown AL 35023','2900 S Mem PkwyDrake Ave, Huntsville AL 35801','11610 Memorial Pkwy South, Huntsville AL 35803','2200 Sparkman Drive, Huntsville AL 35810','330 Sutton Rd, Huntsville AL 35763',
          '6140 Univ Drive, Huntsville AL 35806','4206 N College Ave, Jackson AL 36545,''1625 Pelham South, Jacksonville AL 36265','1801 Hwy 78 East, Jasper AL 35501','8551 Whitfield Ave, Leeds AL 35094',
          '8650 Madison Blvd, Madison AL 35758','145 Kelley Blvd, Millbrook AL 36054','1970 S University Blvd, Mobile AL 36609','6350 Cottage Hill Road, Mobile AL 36609','101 South Beltline Highway, Mobile AL 36606',
          '2500 Dawes Road, Mobile AL 36695','5245 Rangeline Service Rd, Mobile AL 36619','685 Schillinger Rd, Mobile AL 36695','3371 S Alabama Ave, Monroeville AL 36460','10710 Chantilly Pkwy, Montgomery AL 36117',
          '3801 Eastern Blvd, Montgomery AL 36116','6495 Atlanta Hwy, Montgomery AL 36117','851 Ann St, Montgomery AL 36107','15445 Highway 24, Moulton AL 35650','517 West Avalon Ave, Muscle Shoals AL 35661',
          '5710 Mcfarland Blvd, Northport AL 35476','2453 Avenue East, Oneonta AL 35121  205-625-647','2900 Pepperrell Pkwy, Opelika AL 36801','92 Plaza Lane, Oxford AL 36203','1537 Hwy 231 South, Ozark AL 36360',
          '2181 Pelham Pkwy, Pelham AL 35124','165 Vaughan Ln, Pell City AL 35125','3700 Hwy 280-431 N, Phenix City AL 36867','1903 Cobbs Ford Rd, Prattville AL 36066','4180 Us Hwy 431, Roanoke AL 36274',
          '13675 Hwy 43, Russellville AL 35653','1095 Industrial Pkwy, Saraland AL 36571','24833 Johnt Reidprkw, Scottsboro AL 35768','1501 Hwy 14 East, Selma AL 36703','7855 Moffett Rd, Semmes AL 36575',
          '150 Springville Station Blvd, Springville AL 35146','690 Hwy 78, Sumiton AL 35148','41301 US Hwy 280, Sylacauga AL 35150','214 Haynes Street, Talladega AL 35160','1300 Gilmer Ave, Tallassee AL 36078',
          '34301 Hwy 43, Thomasville AL 36784','1420 Us 231 South, Troy AL 36081','1501 Skyland Blvd E, Tuscaloosa AL 35405','3501 20th Av, Valley AL 36854','2575 Us Hwy 43, Winfield AL 35594']

RND_ADRS2=['777 Brockton Avenue, Abington MA 2351','30 Memorial Drive, Avon MA 2322','250 Hartford Avenue, Bellingham MA 2019',
          '700 Oak Street, Brockton MA 2301','66-4 Parkhurst Rd, Chelmsford MA 1824','591 Memorial Dr, Chicopee MA 1020','55 Brooksby Village Way, Danvers MA 1923',
          '137 Teaticket Hwy, East Falmouth MA 2536','42 Fairhaven Commons Way, Fairhaven MA 2719','374 William S Canning Blvd, Fall River MA 2721','121 Worcester Rd, Framingham MA 1701',
          '677 Timpany Blvd, Gardner MA 1440','337 Russell St, Hadley MA 1035','295 Plymouth Street, Halifax MA 2338','1775 Washington St, Hanover MA 2339','280 Washington Street, Hudson MA 1749',
          '20 Soojian Dr, Leicester MA 1524','11 Jungle Road, Leominster MA 1453','301 Massachusetts Ave, Lunenburg MA 1462','780 Lynnway, Lynn MA 1905','70 Pleasant Valley Street, Methuen MA 1844',
          '830 Curran Memorial Hwy, North Adams MA 1247','1470 S Washington St, North Attleboro MA 2760','506 State Road, North Dartmouth MA 2747','742 Main Street, North Oxford MA 1537','72 Main St, North Reading MA 1864',
          '200 Otis Street, Northborough MA 1532','180 North King Street, Northhampton MA 1060','555 East Main St, Orange MA 1364','555 Hubbard Ave-Suite 12, Pittsfield MA 1201','300 Colony Place, Plymouth MA 2360',
          '301 Falls Blvd, Quincy MA 2169','36 Paramount Drive, Raynham MA 2767','450 Highland Ave, Salem MA 1970','1180 Fall River Avenue, Seekonk MA 2771','1105 Boston Road, Springfield MA 1119','100 Charlton Road, Sturbridge MA 1566',
          '262 Swansea Mall Dr, Swansea MA 2777','333 Main Street, Tewksbury MA 1876','550 Providence Hwy, Walpole MA 2081','352 Palmer Road, Ware MA 1082','3005 Cranberry Hwy Rt 6 28, Wareham MA 2538',
          '250 Rt 59, Airmont NY 10901','141 Washington Ave Extension, Albany NY 12205','13858 Rt 31 W, Albion NY 14411','2055 Niagara Falls Blvd, Amherst NY 14228','101 Sanford Farm Shpg Center, Amsterdam NY 12010',
          '297 Grant Avenue, Auburn NY 13021','4133 Veterans Memorial Drive, Batavia NY 14020','6265 Brockport Spencerport Rd, Brockport NY 14420','5399 W Genesse St, Camillus NY 13031','3191 County rd 10, Canandaigua NY 14424',
          '30 Catskill, Catskill NY 12414','161 Centereach Mall, Centereach NY 11720','3018 East Ave, Central Square NY 13036','100 Thruway Plaza, Cheektowaga NY 14225','8064 Brewerton Rd, Cicero NY 13039',
          '5033 Transit Road, Clarence NY 14031','3949 Route 31, Clay NY 13041','139 Merchant Place, Cobleskill NY 12043','85 Crooked Hill Road, Commack NY 11725','872 Route 13, Cortlandville NY 13045',
          '279 Troy Road, East Greenbush NY 12061','2465 Hempstead Turnpike, East Meadow NY 11554','6438 Basile Rowe, East Syracuse NY 13057','25737 US Rt 11, Evans Mills NY 13637','901 Route 110, Farmingdale NY 11735',
          '2400 Route 9, Fishkill NY 12524','10401 Bennett Road, Fredonia NY 14063','1818 State Route 3, Fulton NY 13069','4300 Lakeville Road, Geneseo NY 14454','990 Route 5 20, Geneva NY 14456',
          '311 RT 9W, Glenmont NY 12077','200 Dutch Meadows Ln, Glenville NY 12302','100 Elm Ridge Center Dr, Greece NY 14626','1549 Rt 9, Halfmoon NY 12065','5360 Southwestern Blvd, Hamburg NY 14075',
          '103 North Caroline St, Herkimer NY 13350','1000 State Route 36, Hornell NY 14843','1400 County Rd 64, Horseheads NY 14845','135 Fairgrounds Memorial Pkwy, Ithaca NY 14850','2 Gannett Dr, Johnson City NY 13790',
          '233 Ave Ext, Johnstown NY 12095','601 Frank Stottile Blvd, Kingston NY 12401','350 E Fairmount Ave, Lakewood NY 14750','4975 Transit Rd, Lancaster NY 14086','579 Troy-Schenectady Road, Latham NY 12110',
          '5783 So Transit Road, Lockport NY 14094','7155 State Rt 12 S, Lowville NY 13367','425 Route 31, Macedon NY 14502','3222 State Rt 11, Malone NY 12953','200 Sunrise Mall, Massapequa NY 11758',
          '43 Stephenville St, Massena NY 13662','750 Middle Country Road, Middle Island NY 11953','470 Route 211 East, Middletown NY 10940','3133 E Main St, Mohegan Lake NY 10547','288 Larkin, Monroe NY 10950',
          '41 Anawana Lake Road, Monticello NY 12701','4765 Commercial Drive, New Hartford NY 13413','1201 Rt 300, Newburgh NY 12550','255 W Main St, Avon CT 6001','120 Commercial Parkway, Branford CT 6405',
          '1400 Farmington Ave, Bristol CT 6010','161 Berlin Road, Cromwell CT 6416','67 Newton Rd, Danbury CT 6810','656 New Haven Ave, Derby CT 6418','69 Prospect Hill Road, East Windsor CT 6088',
          '150 Gold Star Hwy, Groton CT 6340','900 Boston Post Road, Guilford CT 6437','2300 Dixwell Ave, Hamden CT 6514','495 Flatbush Ave, Hartford CT 6106','180 River Rd, Lisbon CT 6351',
          '420 Buckland Hills Dr, Manchester CT 6040','1365 Boston Post Road, Milford CT 6460','1100 New Haven Road, Naugatuck CT 6770','315 Foxon Blvd, New Haven CT 6513','164 Danbury Rd, New Milford CT 6776',
          '3164 Berlin Turnpike, Newington CT 6111','474 Boston Post Road, North Windham CT 6256','650 Main Ave, Norwalk CT 6851','680 Connecticut Avenue, Norwalk CT 6854','220 Salem Turnpike, Norwich CT 6360',
          '655 Boston Post Rd, Old Saybrook CT 6475','625 School Street, Putnam CT 6260','80 Town Line Rd, Rocky Hill CT 6067','465 Bridgeport Avenue, Shelton CT 6484','235 Queen St, Southington CT 6489',
          '150 Barnum Avenue Cutoff, Stratford CT 6614','970 Torringford Street, Torrington CT 6790','844 No Colony Road, Wallingford CT 6492','910 Wolcott St, Waterbury CT 6705','155 Waterford Parkway No, Waterford CT 6385',
          '515 Sawmill Road, West Haven CT 6516','2473 Hackworth Road, Adamsville AL 35005','630 Coonial Promenade Pkwy, Alabaster AL 35007','2643 Hwy 280 West, Alexander City AL 35010','540 West Bypass, Andalusia AL 36420',
          '5560 Mcclellan Blvd, Anniston AL 36206','1450 No Brindlee Mtn Pkwy, Arab AL 35016','1011 US Hwy 72 East, Athens AL 35611','973 Gilbert Ferry Road Se, Attalla AL 35954','1717 South College Street, Auburn AL 36830',
          '701 Mcmeans Ave, Bay Minette AL 36507','750 Academy Drive, Bessemer AL 35022','312 Palisades Blvd, Birmingham AL 35209','1600 Montclair Rd, Birmingham AL 35210','5919 Trussville Crossings Pkwy, Birmingham AL 35235',
          '9248 Parkway East, Birmingham AL 35206','1972 Hwy 431, Boaz AL 35957','10675 Hwy 5, Brent AL 35034','2041 Douglas Avenue, Brewton AL 36426','5100 Hwy 31, Calera AL 35040',
          '1916 Center Point Rd, Center Point AL 35215','1950 W Main St, Centre AL 35960','16077 Highway 280, Chelsea AL 35043','1415 7Th Street South, Clanton AL 35045','626 Olive Street Sw, Cullman AL 35055',
          '27520 Hwy 98, Daphne AL 36526','2800 Spring Avn SW, Decatur AL 35603','969 Us Hwy 80 West, Demopolis AL 36732','3300 South Oates Street, Dothan AL 36301','4310 Montgomery Hwy, Dothan AL 36303',
          '600 Boll Weevil Circle, Enterprise AL 36330','3176 South Eufaula Avenue, Eufaula AL 36027','7100 Aaron Aronov Drive, Fairfield AL 35064','10040 County Road 48, Fairhope AL 36533','3186 Hwy 171 North, Fayette AL 35555',
          '3100 Hough Rd, Florence AL 35630','2200 South Mckenzie St, Foley AL 36535','2001 Glenn Bldv Sw, Fort Payne AL 35968','340 East Meighan Blvd, Gadsden AL 35903','890 Odum Road, Gardendale AL 35071',
          '1608 W Magnolia Ave, Geneva AL 36340','501 Willow Lane, Greenville AL 36037','170 Fort Morgan Road, Gulf Shores AL 36542','11697 US Hwy 431, Guntersville AL 35976','42417 Hwy 195, Haleyville AL 35565',
          '1706 Military Street South, Hamilton AL 35570','1201 Hwy 31 NW, Hartselle AL 35640','209 Lakeshore Parkway, Homewood AL 35209','2780 John Hawkins Pkwy, Hoover AL 35244','5335 Hwy 280 South, Hoover AL 35242',
          '1007 Red Farmer Drive, Hueytown AL 35023','2900 S Mem PkwyDrake Ave, Huntsville AL 35801','11610 Memorial Pkwy South, Huntsville AL 35803','2200 Sparkman Drive, Huntsville AL 35810','330 Sutton Rd, Huntsville AL 35763',
          '6140 Univ Drive, Huntsville AL 35806','4206 N College Ave, Jackson AL 36545,''1625 Pelham South, Jacksonville AL 36265','1801 Hwy 78 East, Jasper AL 35501','8551 Whitfield Ave, Leeds AL 35094',
          '8650 Madison Blvd, Madison AL 35758','145 Kelley Blvd, Millbrook AL 36054','1970 S University Blvd, Mobile AL 36609','6350 Cottage Hill Road, Mobile AL 36609','101 South Beltline Highway, Mobile AL 36606',
          '2500 Dawes Road, Mobile AL 36695','5245 Rangeline Service Rd, Mobile AL 36619','685 Schillinger Rd, Mobile AL 36695','3371 S Alabama Ave, Monroeville AL 36460','10710 Chantilly Pkwy, Montgomery AL 36117',
          '3801 Eastern Blvd, Montgomery AL 36116','6495 Atlanta Hwy, Montgomery AL 36117','851 Ann St, Montgomery AL 36107','15445 Highway 24, Moulton AL 35650','517 West Avalon Ave, Muscle Shoals AL 35661',
          '5710 Mcfarland Blvd, Northport AL 35476','2453 Avenue East, Oneonta AL 35121  205-625-647','2900 Pepperrell Pkwy, Opelika AL 36801','92 Plaza Lane, Oxford AL 36203','1537 Hwy 231 South, Ozark AL 36360',
          '2181 Pelham Pkwy, Pelham AL 35124','165 Vaughan Ln, Pell City AL 35125','3700 Hwy 280-431 N, Phenix City AL 36867','1903 Cobbs Ford Rd, Prattville AL 36066','4180 Us Hwy 431, Roanoke AL 36274',
          '13675 Hwy 43, Russellville AL 35653','1095 Industrial Pkwy, Saraland AL 36571','24833 Johnt Reidprkw, Scottsboro AL 35768','1501 Hwy 14 East, Selma AL 36703','7855 Moffett Rd, Semmes AL 36575',
          '150 Springville Station Blvd, Springville AL 35146','690 Hwy 78, Sumiton AL 35148','41301 US Hwy 280, Sylacauga AL 35150','214 Haynes Street, Talladega AL 35160','1300 Gilmer Ave, Tallassee AL 36078',
          '34301 Hwy 43, Thomasville AL 36784','1420 Us 231 South, Troy AL 36081','1501 Skyland Blvd E, Tuscaloosa AL 35405','3501 20th Av, Valley AL 36854','2575 Us Hwy 43, Winfield AL 35594']

RND_PHON=['205-200-7434','205-201-3301','205-202-0866','205-203-5471','205-206-7076','205-207-0174','205-208-3035','205-209-3671','205-210-1154','205-212-4554',
          '205-213-3119','205-214-6804','205-215-9709','205-216-8742','205-217-8781','205-218-4525','205-219-6801','205-220-4557','205-221-7773','205-222-5784',
          '205-223-5944','205-224-7875','205-225-6571','205-226-1968','205-227-8692','205-228-2509','205-229-2737','205-230-5220','205-231-1748','205-232-5232',
          '205-233-7038','205-234-0069','205-235-7619','205-237-1194','205-238-8314','205-239-5446','205-240-1947','205-241-1809','205-242-9380','205-243-4591',
          '205-244-1013','205-245-2171','205-246-4950','205-247-3065','205-248-9131','205-249-0310','205-250-7901','205-251-4025','205-252-1493','205-253-5649',
          '205-254-5099','205-255-0650','205-257-8829','205-258-2390','205-259-2016','205-260-0421','205-261-9144','205-262-8943','205-263-0431','205-264-1819',
          '205-265-7499','205-266-7909','205-267-9169','205-268-6915','205-269-1509','205-270-5436','205-271-8679','205-272-5992','205-273-3920','205-274-8207',
          '205-275-4770','205-276-7869','205-277-4799','205-278-1260','205-279-9394','205-280-2966','205-281-8877','205-282-1845','205-283-5263','205-284-0324',
          '205-285-0241','205-286-5024','205-287-4297','205-288-1630','205-289-5086','205-290-8314','205-291-5885','205-292-1001','205-294-3438','205-295-5529',
          '205-296-8270','205-297-8003','205-298-1909','205-299-2147','205-300-0231','205-301-3336','205-302-8743','205-303-3731','205-304-9018','205-305-1212',
          '205-306-1123','256-573-7200','256-574-7322','256-575-5705','256-576-4932','256-577-7441','256-578-9364','256-579-1605','256-580-1949','256-581-1409',
          '256-582-8213','256-583-0185','256-584-1278','256-585-7206','256-586-6718','256-587-3135','256-588-1843','256-589-2421','256-590-7347','256-591-5226',
          '256-592-5052','256-593-3589','256-594-3987','256-595-1122','256-596-0753','256-597-1849','256-598-1877','256-599-1036','256-600-0994','256-601-4748',
          '256-602-7259','256-603-4814','256-604-5777','256-605-5267','256-606-1342','256-607-3894','256-608-7892','256-609-6304','256-610-5630','256-612-4550',
          '256-613-2278','256-614-5366','256-615-7091','256-616-9856','256-617-7494','256-618-8083','256-619-6140','256-620-6919','256-621-2877','256-622-2339',
          '256-623-4304','256-624-2619','256-625-0038','256-626-0226','256-646-4935','256-647-9721','256-648-6644','256-649-5933','256-650-3754','256-651-6910',
          '256-652-2161','256-653-3667','256-654-5925','256-655-7563','256-656-2188','256-657-0214','256-658-9796','256-659-6069','256-660-1315','256-661-9725',
          '256-662-7514','256-663-1873','256-664-9610','256-665-8348','256-667-0347','256-668-4175','256-669-5904','256-670-6304','256-671-8189','256-672-9639',
          '256-673-2491','256-674-8399','256-695-0336','256-704-1876','256-709-6899','256-710-9074','256-712-1212','256-713-1897','256-714-9033','256-715-6675',
          '256-724-3401','256-725-8595','256-726-6496','256-727-7362','256-728-4088','256-729-6731','256-730-5554','256-731-1294','256-732-6065','256-733-6513',
          '256-734-0107','256-735-5700','256-736-8884','256-737-6261','256-738-7169','256-739-3640','256-740-6053','256-741-6666','256-743-7642','256-744-3521',
          '256-745-3160','256-746-3321','256-747-4808','256-748-4481','256-749-5342','256-750-0187','256-751-7301','256-752-8332','256-753-4028','256-754-3497',
          '256-755-3068','256-756-5491','256-757-8438','256-758-5263','256-759-5754','256-760-0865','256-761-9942','256-762-4407','256-763-4650','256-764-1519',
          '256-765-0485','256-766-6492','256-767-1472','256-768-3472','256-769-3158','256-770-6560','256-771-1213','256-772-7228','256-773-7044','256-774-5376',
          '256-775-8482','256-776-8642','256-777-8904','256-778-5657','256-779-8606','256-781-9346','256-782-3919','256-783-2851','256-784-2430','256-785-1829',
          '256-786-8343','256-787-9908','256-788-6055','256-789-3027','256-790-9362','256-791-2234','256-792-7658','256-793-5883','256-794-1261','256-795-2708',
          '256-796-8542','256-797-6705','256-798-0773','256-799-9177','256-801-7363','256-802-1463','256-803-7359','256-804-0589','256-805-1217','256-806-0130',
          '256-807-8148','256-808-2150','256-809-5136','256-810-6903','256-812-2533','256-813-1123','256-814-4404','256-815-5454','256-816-5937','256-817-1976',
          '256-818-0037','256-819-0303','205-563-3382','205-566-9856','205-564-9499','205-567-3284','205-568-1813','205-571-3483','256-820-9470','256-821-5030',
          '256-822-4440','256-823-9054','256-824-9821','256-825-7078','256-827-1051','256-828-4654','256-829-0256','256-830-2966','256-831-3073','256-832-1281',
          '256-834-0027','256-835-0961','256-837-0135','256-838-8898','256-839-1453','256-840-3107','256-841-2713','256-842-9940','256-843-9780','256-844-7427',
          '256-845-6634','256-846-4335','256-847-8892','256-848-0992','256-849-6166','256-850-0060','256-851-7404','256-852-9325','256-853-9604','256-854-9408',
          '256-855-3903','256-856-8065','256-857-1211','256-858-3811','256-859-3262','256-861-5975','256-864-5895','256-867-2935','256-868-8397','256-869-3534',
          '256-871-7561','256-872-3726','256-873-0885','256-874-7602','256-876-4086','256-878-9128','256-879-5168','256-880-6934','256-881-5958','256-882-7757',
          '256-883-6433','256-885-0464','256-886-4414','256-887-6331','256-890-5091','256-891-9364','256-892-2130','256-893-9875','256-894-2083','256-895-5489',
          '256-896-9945','256-898-3769','256-899-7607','256-901-9722','256-902-8628','256-903-5938','256-905-0215','256-906-6956','256-908-9913','256-909-7825',
          '256-912-4334','256-914-0569','256-917-2877','256-919-8158','256-920-3630','256-922-6966','256-923-8805','256-924-6311','256-925-6457','256-926-0172',
          '256-927-0598','256-929-6569','256-931-1098','256-933-9658','256-934-4541','256-935-8525','256-937-9820','256-943-9029','256-945-5281','256-947-7418',
          '256-952-5174','256-955-7231','256-957-7736','256-960-2512','256-961-3323','256-962-3539','256-963-7104','256-964-6131','256-966-3060','256-970-3921',
          '256-971-7579','256-972-1825','256-974-2485','256-975-9257','256-977-4510','256-978-7420','256-979-5919','256-985-9306','256-987-8769','256-990-5848',
          '256-995-3343','256-996-5900','256-997-4202','256-998-6332','256-999-2411','334-889-3350','334-892-3767','334-894-6603','334-896-0337','334-897-3406',
          '334-898-8315','334-899-3786','334-905-0604','334-908-9552','334-918-3209','334-937-8139','334-944-4668','334-945-1659','334-953-0643','334-954-3204',
          '334-956-8098','334-957-6419','334-963-7195','334-973-2247','334-975-8060','334-977-7197','334-982-7311','334-983-6265','334-984-2638','334-986-1588',
          '334-991-6739','334-992-9878','334-994-9386','334-995-4842','334-996-2648','334-997-8131','938-223-7798','938-223-7798','334-996-2648','938-238-2779']


RND_CITY=['Acmar','Moody','Adamsville','Adger','Alabaster','Alexander City','Alexander City','Allgood','Alton','Baileyton','Bessemer','Hueytown','Blountsville','Bon Air','Bremen','Brent',
          'Burnwell','Calera','Cardiff','Centreville','Chelsea','Coosa Pines','Clanton','Clay','Cleveland','Columbiana','Cook Springs','Crane Hill','Cropwell','Cullman','Docena','Dolomite',
          'Brierfield','Brookside','Dora','Empire','Fairfield','Coalburg','Garden City','Gardendale','Graysville','Green Pond','Hanceville','Harpersville','Hayden','Branford','Holly Pond','Joppa',
          'Kellyton','Kimberly','Leeds','Lincoln','Locust Fork','New York','Knickerbocker','Bowling Green','Peck Slip','Trinity','Princetown','Canal Street','Chinatown','Roosevelt Island','Bell','Bell Gardens',
          'Bloomfield','Bristol','Burlington','East Granby','Farmington','Glastonbury','Plainville','Rocky Hill','Hartford','Cromwell','Higganum','Middletown','Southington','Shelton','North Haven','Bridgeport',
          'Denver','Aurora','Thornton','Arvada','Loveland','Bloomfield','Bristol','Unionville','Newark','Claymont','Delaware City','Alexandria','Ponte Vedra Beach','Fleming Island','Bostwick','Bridgeport','Bellevue',
          'Avondale Estates','Norcross','Alpharetta','Aberdeen','American Falls','Arbon','Ackworth','Adair','Adel','Kansas City','Louisville','Metairie','Baltimore','Annapolis','Boston','Detroit','Sioux Falls',
          'Lansing city','Warren','Sterling Heights','Ann Arbor','Clinton','Twin Cities Amf','Fort Snelling','St. Paul','Hopkins','Abbeville','Arkabutla','Ashland','Helena','Bozeman','Billings','Missoula','Bellevue',
          'Abie','Arlington','Ashland','Bancroft','Albuquerque','Compton','Culver City','Fargo','Watford City','Carrington','McClusky','Carson','Minnewaukan','Medora','Amidon','Stanley','Fairfax','Fairfax Station','Falls Church',
          'Groveport','Columbus','Portland','Salem','Eugene','Gresham','Hillsboro','Bend','Beaverton','Aliquippa','Ambridge','Albion','Ashaway','Barrington','Block Island','Chattanooga','Gatlinburg','Memphis','Knoxville',
          'Houston','San Antonio','McKinney','Pasadena','McAllen','League City','Victoria','Port Arthur','Lancaster','Caney City','Burlington','Rutland','Bluefield','Athens','Beeson','Atlantic City','Spring Creek','Tuscarora','Schurz']
                    
RND_ZIP=['35004','35004','35005','35006','35007','35010','35011','35013','35014','35015','35016','35017','35018','35019','35020','35021','35022','35023','35024','35025','35026','35027','35028',
          '35029','35030','35031','35032','35033','35034','35035','35036','35037','35038','35039','35040','35041','35042','35043','35044','35045','35046','35047','35048','35049','35050','35051','35052',
          '35053','35054','35055','35056','35057','35058','35059','35060','35061','35062','35063','35064','35065','35066','35067','35068','35069','35070','35071','35072','35073','35074','35075','35076','35077',
          '35078','35079','35080','35081','35082','35083','35084','35085','35086','35087','35088','35079','35090','35091','35092','35093','35094','10001','10002','10003','10004','10005','10006','10007','10008',
          '10009','10010','06002','06010','06016','06032','06033','06040','06062','06070','06074','06102','06134','06354','06472','06489','06507','06670','06676','06822','06922','06937','06064','06085','06989',
          '99501','99503','85006','85007','85008','71601','71603','90224','90230','90231','90232','80203','80204','80205','06002','06010','06011','06013','19702','19703','19706','20001','20016','20017','20026',
          '30002','30003','30004','96719','83210','83211','83212','61348','46001','46011','46012','50001','50002','50003','66102','66103','66104','40213','40214','40215','70003','70004','70005','04401','04240', 
          '20906','20878','21740','01001','01002','01003','01004','55111','55305','38601','38602','38603','65083','65201','65211','59007','59010','68001','68002','68003','68004','89041','89067','89147','89703', 
          '03032','07303','07304','07305','07306','87196','87196','87197','87198','90224','90230','90231','90232','58102','58103','58104','58105','43199','43201','43202','73007','73017','73021','73024','73026', 
          '97002','97005','15001','15003','15004','02802','02804','02806','02807','90202','90202','90209','90210','57101','57103','57104','37641','37743','37745','75007','75008','75010','75011','75014','75015', 
          '84095','05030','05031','22038','22039','22040','98003','98004','98005','24701','24712','24714','53002','53003','53004','53005','82001','82009','82901','82601','89883','89835','89834','89024','88901'] 
                                                            
RND_STATE=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine',
           'Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota',
           'Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'] 

NAME_TARGET=random.choice(RND_NAME)
LAST_TARGET=random.choice(RND_LAST)
ADRS_TARGET=random.choice(RND_ADRS)
ADRS2_TARGET=random.choice(RND_ADRS2)
PHON_TARGET=random.choice(RND_PHON)
CITY_TARGET=random.choice(RND_CITY)
STATE_TARGET=random.choice(RND_STATE)
ZIP_TARGET=random.choice(RND_ZIP)
LINE="*************************************************************************"
################################################################################
PAD='3'
IPTVTMPPATH='/tmp/IPTV'
LINKFILE0= '/tmp/test'
LINKFILE= '/tmp/link'
LINKFILE2= '/tmp/code'
LINKFILE2_1= '/tmp/post_token'
LINKFILE3_1= '/tmp/myPic1.png'
LINKFILE3= '/tmp/myPic.png'
TMPOUTPUTDATA= '/tmp/dateoutTMP'
BFNAME= 'userbouquet.IPTVWORLD54.tv'
LastScanned= 'userbouquet.LastScanned.tv'
M3UPATH= '/tmp/IPTVWORLD54.m3u'
m3ufile= 'IPTVWORLD54'
WGET='wget --no-check-certificate'
BOUQUETSPATH='/etc/enigma2/bouquets.tv'
E2SETTINGSPATH='/etc/enigma2'
url2="https://solaris-tv.com/clientarea.php?action=productdetails"
url22='https://solaris-tv.com/includes/verifyimage.php'
services_url='https://solaris-tv.com/clientarea.php?action=services'
################################################################################

s = requests.Session()

HDR= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:85.0) Gecko/20100101 Firefox/85.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
      'Upgrade-Insecure-Requests':'1',
      'Connection': 'keep-alive',
      'Accept-Encoding':'gzip, deflate'}

RND_EMAIL=['@harakirimail.com','@harakirimail.com']     
chars = string.digits
RND_ID  =  ''.join(choice(chars) for _ in range(5))
RND_PASS=  ''.join(choice(chars) for _ in range(9))
#EMAIL_TARGET=str(RND_ID)+random.choice(RND_EMAIL)
EMAIL_TARGET=NAME_TARGET+rnd2+'@gmail.com'
RND_TARGET=str(RND_ID)
host_url='https://harakirimail.com/inbox/'+RND_TARGET
import shutil
print("Password:",RND_PASS)
print("EMail Target:",EMAIL_TARGET)
#print("EMail Target:",NAME_TARGET+rnd2+'@gmail.com')
#print "PHONE Target:",PHON_TARGET
#print "CITY Target:",CITY_TARGET
#print "ZIP Target:",STATE_TARGET
#print "LAST NAME Target:",LAST_TARGET
Post_Hdr={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Content-Type':'application/x-www-form-urlencoded',
          #'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',    
          'Referer':'https://solaris-tv.com/cart.php',
          'Accept-Encoding':'gzip'}#, deflate, br'}

def cleanTMP():
    print("Clean tmp folder")
    print(LINE)
    os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (M3UPATH, LINKFILE))

class myInput2(Screen):
    skinfhd = '''
<screen position="center,center" size="856,556" title="" flags="wfNoBorder">
<widget source="Title" position="5,5" size="845,100" render="Label" font="Regular;28" foregroundColor="#00ffffff" transparent="1" halign="center"/>
<widget name="icon" render="Pixmap" pixmap="/tmp/myPic.png" zPosition="5" position="250,170" size="350,100" alphatest="blend" borderWidth="2" borderColor="#00ffffff" backgroundColor="#00000000" />
<widget name="input" position="276,290" size="470,50" font="Regular;40" transparent="0" itemHeight="40" foregroundColor="#00ffffff" backgroundColor="#b30000" zPosition="7"/>
<eLabel text="Code =" position="100,290" size="180,50" font="Regular; 40" transparent="0" foregroundColor="#00ffffff" backgroundColor="#b30000" halign="center" zPosition="5" />
<widget source="key_green" render="Label" position="65,480" size="200,40" zPosition="2"  valign="center" halign="center" font="Regular;28" transparent="0" foregroundColor="#00ffffff" backgroundColor="#00389416"/>
<widget name="HelpWindow" position="200,370" size="1,1" alphatest="on" foregroundColor="#00ffffff" transparent="1" zPosition="6" />
</screen>'''
    skinhd = '''
<screen position="center,center" size="856,556" title="" flags="wfNoBorder">
<widget source="Title" position="5,5" size="845,100" render="Label" font="Regular;28" foregroundColor="#00ffffff" transparent="1" halign="center"/>
<widget name="icon" render="Pixmap" pixmap="/tmp/myPic.png" zPosition="5" position="250,170" size="350,100" alphatest="blend" borderWidth="2" borderColor="#00ffffff" backgroundColor="#00000000" />
<widget name="input" position="276,290" size="470,50" font="Regular;40" transparent="0" itemHeight="40" foregroundColor="#00ffffff" backgroundColor="#b30000" zPosition="7"/>
<eLabel text="Code =" position="100,290" size="180,50" font="Regular; 40" transparent="0" foregroundColor="#00ffffff" backgroundColor="#b30000" halign="center" zPosition="5" />
<widget source="key_green" render="Label" position="65,480" size="200,40" zPosition="2"  valign="center" halign="center" font="Regular;28" transparent="0" foregroundColor="#00ffffff" backgroundColor="#00389416"/>
<widget name="HelpWindow" position="200,370" size="1,1" alphatest="on" foregroundColor="#00ffffff" transparent="1" zPosition="6" />
</screen>'''  

  
    def __init__(self, session, useableChars=None, **kwargs):
        self.session = session
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = myInput2.skinhd
        else:
            self.skin = myInput2.skinfhd
        #self["myActionMap"] = ActionMap(["SetupActions"],{"ok": self.myInput,"cancel": self.cancel}, -1)
        self["myActionMap"] = NumberActionMap(["WizardActions", "InputBoxActions", "InputAsciiActions", "KeyboardInputActions", "ColorActions"],
        	{           		
           		"gotAsciiCode": self.gotAsciiCode,
			"back": self.cancel,
			"green": self.save,
			"left": self.keyLeft,
			"right": self.keyRight,
			"deleteForward": self.keyDelete,
			"deleteBackward": self.keyBackspace,
			"tab": self.keyTab,
			"toggleOverwrite": self.keyInsert,
			"1": self.keyNumberGlobal,
			"2": self.keyNumberGlobal,
			"3": self.keyNumberGlobal,
			"4": self.keyNumberGlobal,
			"5": self.keyNumberGlobal,
			"6": self.keyNumberGlobal,
			"7": self.keyNumberGlobal,
			"8": self.keyNumberGlobal,
			"9": self.keyNumberGlobal,
			"0": self.keyNumberGlobal
           	}, -1)

### EDit By RAED To DreamOS OE2.5/2.6
        #if fileExists('/var/lib/dpkg/status'):
        #     self.wget = "/usr/bin/wget2 --no-check-certificate"
        #else:
        #     self.wget = "/usr/bin/wget"
        self.wget = "wget --no-check-certificate"
### End
        #import sys,os  
        #os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/pictureimage.sh'")
        self['key_green'] = StaticText(_('Save'))
        self['Password'] = Label()
        self['icon'] = Pixmap()
        self["HelpWindow"] = Pixmap()
        self["HelpWindow"].show()
        self["input"] = Input(**kwargs)
        if useableChars is not None:
            self["input"].setUseableChars(useableChars)
        self.timer = eTimer()
        try:
            self.timer.callback.append(self.Confirm)
        except:
            self.timer_conn = self.timer.timeout.connect(self.Confirm)
        #self.onLayoutFinish.append(self.setWindowTitle)
        self.onExecBegin.append(self.setKeyboardModeAscii)
        self.setTitle("Please enter the characters you see in the image below into the text box provided. This is required to prevent automated submissions.")
        #post_data2='configure=true&i=0&submit=Continue'                             
        #post_data2='configure=true&i=0&submit=Continue'                                             
        post_data='firstname='+NAME_TARGET+'&lastname='+LAST_TARGET+'&email='+NAME_TARGET+rnd2+'@gmail.com&country-calling-code-phonenumber=1&phonenumber='+PHON_TARGET+'&address1='+ADRS_TARGET+'&city='+CITY_TARGET+'&state='+STATE_TARGET+'&postcode='+ZIP_TARGET+'&country=US&customfield[120]='+PHON_TARGET+'&customfield[121]=Evet&customfield[301]= Burcu Kahraman&securityqid=10&securityqans=bmw&password='+RND_PASS+'&password2='+RND_PASS+'&paymentmethod=banktransfer&accepttos=I have read and agree to the&submit=Complete Order'
        post_account=s.post('https://solaris-tv.com/cart.php?a=add&pid=1',headers=Post_Hdr,data=post_data,verify=False,allow_redirects=True).content
        #post_account=s.post('https://hitfiretv.com/billing/cart.php?a=confproduct&i=0',headers=Post_Hdr,data=post_data,verify=False,allow_redirects=True).content
        data=s.get('https://solaris-tv.com/cart.php?a=view',verify=False,allow_redirects=True).text
        regx='token" value="(.*?)"'
        try:post_token=re.findall(regx,data, re.M|re.I)[0]
        except:pass
        print("POST TOKEN:",post_token)
        s.headers.update({'token': post_token})
        with open(LINKFILE2_1, "a") as f: f.write(post_token)
        #os.system('wget --no-check-certificate -q -O- --trust-server-names %s > %s' % (url22, LINKFILE3))
        #data=s.post('https://ssdvpshosting.xyz/store/includes/verifyimage.php',headers=Post_Hdr,verify=False,allow_redirects=True).text
        #with open(LINKFILE3, "a") as f: 
        #f.write(data)
        r = s.get(url22, stream = True)
        with open(LINKFILE3_1,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        image = Image.open(LINKFILE3_1)
        new_image = image.resize((350, 100))
        new_image.save(LINKFILE3)
 

    def askForWord(self, code):
        if code is None:
            pass
        elif code == '':
            pass
        else:
            if os.path.exists(LINKFILE2):
                #with open(LINKFILE2, "a") as f: f.write(code)
                #self.wget = "wget --no-check-certificate"
                #os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/cccam48h.sh -qO - | /bin/sh" % self.wget)
                #with open('/tmp/freeservre77', "a") as f: f.write(word)
                #f = open('/tmp/freeservre77', 'r')
                #for line in f.readlines():
                    #id = line.strip('\n')
                    #try:cfg_line='C: storesat.tk 1455 storesat {0}'.format(id)
                    #except:pass
                    #with open('/etc/CCcam.cfg', "a") as f: f.write("\n"+cfg_line)
                    #self.convert
                #self.session.open(MessageBox,_('Your Code is '+code+'\n Press 1 to Exite'), MessageBox.TYPE_INFO, timeout=5) 
                f = open(LINKFILE2, 'r')
                for line in f.readlines():
                    id = line.strip('\n')
                    try:code = "{0}".format(id)
                    except:pass 
                    
    def gotAsciiCode(self):
        self["input"].handleAscii(getPrevAsciiCode())

    #def save(self):
        #self.close
        #self.askForWord()
        #(self["input"].getText())
        #print("capture Keys ********** : %s" % self["input"].getText())

    def save(self):
        Password = self['input'].getText()
        if Password == '':
            self.session.open(MessageBox, '\xd8\xb1\xd8\xa7\xd9\x83 \xd8\xaa\xd8\xaa\xd9\x85\xd8\xb3\xd8\xae\xd8\xb1 \xd9\x87\xd9\x87\xd9\x87\xd9\x87\xd9\x87\xd9\x87\xd9\x87', type=MessageBox.TYPE_INFO)
            return
        milef = ''
        Distnt = '/tmp/'
        Path = '/tmp/code'
        if pathExists(Distnt):
            Password = self['input'].getText()
            if Password != '':
                file = open(Path, 'w')
                file.write(Password.replace(' ', ''))
                file.close()
                #self.session.open(MessageBox, self['input'].getText() + 'Is Copied Successfully\n', type=MessageBox.TYPE_INFO)
                self.askForWord()
                cmdlist = []
                cmdlist.append("%s -qO - '" % self.wget + "'")
                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD54.sh -qO - | /bin/sh" % self.wget)
                self.session.open(Console3, title='IPTVWORLD54', cmdlist=cmdlist, finishedCallback=None)
                self.close(True)
                
        else:
            self.session.open(MessageBox, Path + ' Not Found\n Or Empty', type=MessageBox.TYPE_INFO)

    def keyLeft(self):
        self["input"].left()

    def keyRight(self):
        self["input"].right()

    def keyTab(self):
        self["input"].tab()

    def keyInsert(self):
        self["input"].toggleOverwrite()

    def keyNumberGlobal(self, number):
        self["input"].number(number)

    def keyDelete(self):
        self["input"].delete()

    def keyBackspace(self):
        self["input"].deleteBackward()

    def keyEnd(self):
        self["input"].end()

    def cancel(self):
        self.close(None)

    def Confirm(self):
        self.timer.stop()
        self.showPic(picobject=self['icon'])
        

    def showPic(self, picobject=None, picfile=None):
        picobject.instance.setPixmap(gPixmapPtr())
        self.scale = AVSwitch().getFramebufferScale()
        self.picload = ePicLoad()
        size = picobject.instance.size()
        self.picload.setPara((size.width(), size.height(), self.scale[0], self.scale[0], False, 1, '#80000000'))
        value = self.picload.startDecode(picfile, 0, 0, False)
        if value == 0:
            ptr = self.picload.getData()
            if ptr != None:
                picobject.instance.setPixmap(ptr)
                picobject.show()
                del self.picload
        return

    def askForWord(self):

            #if not os.path.exists(LINKFILE2):
                #with open(LINKFILE2, "a") as f: f.write(code)
                #self.wget = "wget --no-check-certificate"
                #os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/cccam48h.sh -qO - | /bin/sh" % self.wget)
                #with open('/tmp/freeservre77', "a") as f: f.write(word)
                #f = open('/tmp/freeservre77', 'r')
                #for line in f.readlines():
                    #id = line.strip('\n')
                    #try:cfg_line='C: storesat.tk 1455 storesat {0}'.format(id)
                    #except:pass
                    #with open('/etc/CCcam.cfg', "a") as f: f.write("\n"+cfg_line)
                    #self.convert
                #self.session.open(MessageBox,_('Your Code is '+code+'\n Press 1 to Exite'), MessageBox.TYPE_INFO, timeout=5) 
             if os.path.exists(LINKFILE2_1):
                f = open(LINKFILE2_1, 'r')
                for line in f.readlines():
                    id = line.strip('\n')
                    try:post_token = "{0}".format(id)
                    except:pass 
             if os.path.exists(LINKFILE2):
                f = open(LINKFILE2, 'r')
                for line in f.readlines():
                    id = line.strip('\n')
                    try:code = "{0}".format(id)
                    except:pass 
                s.headers.update({'code': code})   
                s.headers.update({'token': post_token})   
                checkout_data='token='+post_token+'&submit=true&custtype=new&loginemail=&loginpassword=&firstname='+NAME_TARGET+'&lastname='+LAST_TARGET+'&email='+EMAIL_TARGET+'&country-calling-code-phonenumber=1&phonenumber='+PHON_TARGET+'&companyname=&address1='+ADRS_TARGET+'&address2='+ADRS2_TARGET+'&city='+CITY_TARGET+'&state='+STATE_TARGET+'&postcode='+ZIP_TARGET+'&country=US&password='+RND_PASS+'&password2='+RND_PASS+'&applycredit=1&paymentmethod=banktransfer&ccinfo=new&ccnumber=&ccexpirydate=&cccvv=&ccdescription=&notes=&marketingoptin=1&code='+code+''
                post_account=s.post('https://solaris-tv.com/cart.php?a=checkout',headers=Post_Hdr,data=checkout_data,verify=False,allow_redirects=True).text
                data=s.get(services_url,verify=False).text
                regx='data-element-id="(.*?)"' 
                service_id=re.findall(regx, data, re.M|re.I)[0]
                post_data=s.get('https://solaris-tv.com/clientarea.php?action=productdetails&id=%s'%service_id,allow_redirects=True,verify=False).text
                #regx='token" value="(.*?)"'
                #try:token_=re.findall(regx,data, re.M|re.I)[0]
                #except:pass
                #params='token='+token_+'&id='+service_id+'&customAction=manage'
                SRV_HDR={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:86.0) Gecko/20100101 Firefox/86.0',
                         'Host': 'solaris-tv.com',
                         'Connection': 'keep-alive',
                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                         'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                         'Referer': 'https://solaris-tv.com/clientarea.php?action=productdetails&id=%s'%service_id,
                         'Content-Type':'application/x-www-form-urlencoded; text/html; charset=utf-8',
                         'DNT': '1',
                         'Upgrade-Insecure-Requests': '1',
                         'Accept-Encoding': 'gzip'}#gzip, deflate, br'
                #post_data=s.post('https://guerrillahosting.net/billing/clientarea.php?action=productdetails&id=%s'%service_id,headers=SRV_HDR,data=params,verify=False,allow_redirects=True).text
                #data=s.get('https://host-store.me/clientarea.php?action=productdetails&id=%s'%service_id,verify=False,allow_redirects=True).content
                #print post_data
                if "M3U" in post_data:
                    print("Target Found !!!")
                    #for email in html_data:
                    regx = '''<a id="m3u_output" data-url="(.*?)"  href'''                                           
                    regx2 = '''id="iptv_username" value="(.*?)"'''                                          
                    regx3 = '''id="iptv_password" value="(.*?)"'''
                    LINE = "APK Androit TV: The Solaris App /tmp/link2"+'\n'+'download >>>>>> https://aftv.news/934986'+'\n'+'Username : '+re.findall(regx2, post_data, re.M|re.I)[0]+'\n'+'Password : '+re.findall(regx3, post_data, re.M|re.I)[0]
                    link="'"+re.findall(regx, post_data, re.M|re.I)[0].replace('type=','type=m3u_plus')+"'"
                    #link = link.decode('utf-8')
                    if link:
                       print(("LINE :", LINE))
                       print(("link :", link))
                       with open(LINKFILE, "a") as f: f.write(link)
                       with open(LINKFILE2, "a") as f: f.write(LINE)
                    else:
                       print('nada_link')
                       return('nada_link')
        
                return

             #else:
                #self.session.open(MessageBox,_('Your Code is '+code+''), MessageBox.TYPE_INFO, timeout=5)
                #f = open(LINKFILE2, 'r')
                #for line in f.readlines():
                    #id = line.strip('\n')
                    #try:code = "{0}".format(id)
                    #except:pass 
                #checkout_data='token='+post_token+'&submit=true&custtype=new&loginemail=&loginpassword=&firstname='+NAME_TARGET+'&lastname='+LAST_TARGET+'&email='+NAME_TARGET+rnd2+'@gmail.com&country-calling-code-phonenumber=1&phonenumber='+PHON_TARGET+'&address1=&city=&state=&postcode=&country=US&password='+RND_PASS+'&password2='+RND_PASS+'&applycredit=1&cccvv=&paymentmethod=paypal&ccinfo=new&ccnumber=&ccexpirydate=&cccvv=&ccdescription=&code='+code+''
                #post_account=s.post('https://ssdvpshosting.xyz/store/cart.php?a=checkout',headers=Post_Hdr,data=checkout_data,verify=False,allow_redirects=True).text
                #with open(LINKFILE, "a") as f: f.write(post_account)
                

    def myInput(self):
        self.session.openWithCallback(self.askForWord, InputBox, title=_("Please Enter Password (Pass) and Press green button (Save)"), text="", maxSize=False, type=Input.TEXT)        
        

    def cancel(self):
        self.close(True)
#******************************************************************************                     
