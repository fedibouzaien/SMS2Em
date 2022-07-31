
phone_numbersf = open('namesms.txt', mode='r', encoding='utf-8').read().split('\n')
outF = open("myOutFile.txt", "a")



Providersa={"TMobile":["10160","10200","10210","10220","10230","10240","10250","10260","10270","10310","10490","10660","10800","TMobile"],
"Att":["10016","10030","10070","10080","10090","10150","10170","10280","10380","10410","10560","10670","10680","10950","11070","11090","11180","11190","12090","12680","13210"],
"Bluegrass":["11440","11800","11810"],
"Boost":"11870",
"CSpire":["11230","11630"],
"CarolinaWest":["10130","12470"],
"CellularOne":["10320","10390","10570"],
"CharitonValley":["11010","11020","11920","12010","12220"],
"CricketWireless":["10016"],
"Globalstar":["10970"],
"Metro":["11660"],
"sprint":["10120","11490"],
"Tracfone":["10999"],
"UnionTelephone":["10020"],
"UsCellular":["10066","10730","11220","11580"],
"Verizon":["310004","10005","10006","10010","10012","10013","10350","10590","10820","10890","10910","11012","11110","11270","11271","11272","11273","11274","11275","11276","11277","11278","11279","11280","11281","11282","11283","11284","11285","11286","11287","11288","11289","11390","11480","11481","11482","11483","11484","11485","11486","11487","11488","11489","11590","12770"],
"Viaero":["10450","10740"],
"Virgin":["10053"],
"WestCentralWireless":["10180"],

# "Ting":["10260"],
# "PlateauWireless":["10100","10960"],
# "PineCellular":["11080"],
# "CommnetWireless":["11040","11320","12370"],
# "IndigoWireless":["11030"],
# "IWireless":["10530","10770"],
# "LimitlessMobile":["10340","10690","11600","12180"],
# "Lycamobile":["11960"],



}


keys_list=list(Providersa)
def chakel(pro, num):
	if(pro) == "TMobile":
		return num+"@tmomail.net";
	elif(pro) == "Att":
		return num+"@txt.att.net";
	elif(pro) == "Bluegrass":
		return num+"@sms.bluecell.com";
	elif(pro) == "Boost":
		return num+"@myboostmobile.com";
	elif(pro) == "CSpire":
		return num+"@cspire1.com";
	elif(pro) == "CarolinaWest":
		return num+"@cwwsms.com";
	elif(pro) == "CellularOne":
		return num+"@mobile.celloneusa.com";
	elif(pro) == "CharitonValley":
		return num+"@sms.cvalley.net";
	elif(pro) == "Globalstar":
		return num+"@g2smsc.globalstar.com";
	elif(pro) == "Metro":
		return num+"@metropcs.sms.us";
	elif(pro) == "sprint":
		return num+"@messaging.sprintpcs.com";
	elif(pro) == "Tracfone":
		return num+"@txt.att.net";
	elif(pro) == "UnionTelephone":
		return num+"@union-tel.com";
	elif(pro) == "UsCellular":
		return num+"@email.uscc.net";
	elif(pro) == "Verizon":
		return num+"@vtext.com";
	elif(pro) == "Viaero":
		return num+"@viaerosms.com";
	elif(pro) == "Virgin":
		return num+"@vmobl.com";
	elif(pro) == "WestCentralWireless":
		return num+"@sms.wcc.net";
	elif(pro) == "CricketWireless":
		return num+"@mms.mycricket.com";
	

def extract(x):
	res=x[x.find(":")+1:]
	return res;
    
	# match (pro): 
 #        case "TMobile":
 #            return num+"@tmomail.net"
 #        case "Att":
 #            return num+"@txt.att.net"
    
    	




for number in phone_numbersf:
	ch=extract(number)
	number=ch
	if (len(number) == 10):
		number="1"+number
	if (len(number) == 11):
		nb=-1
		cn=str(number[2:7])
		# print(cn)
		# if any (cn in Provider for Provider in Providers):
		for Provider in Providersa.values():
			nb=nb+1
			# print(Providersa.keys())
			if cn in Provider:
				cn=str(number[:])
				email=chakel(keys_list[nb],cn)
				print(email)
				
		
	# elif (len(number) == 10):
	# 	cn=number[1:6]
	# 	print(cn)
	# if len(cn) == 10:
	# 	cn="1"+cn
	