#import file from MEFF
import csv
import pandas as pd
novoptions=pd.read_csv("/users/jorge/downloads/nov14opt.csv")
#filer Call American options with volume
nov_opt=novoptions[(novoptions["VOLUME"]!=0)]
nov_opt=nov_opt[nov_opt['CODE'].str.contains("AM")]
nov_opt=nov_opt[nov_opt['CODE'].str.startswith("C")]

#save first version
nov_opt.to_csv("nov_clean14.csv")

#import pandas and load first version

import csv
import pandas as pd
novoptions=pd.read_csv("/users/jorge/nov_clean14.csv")

#convert to datetime the date and strike date
nov_opt=novoptions
import datetime
fecha=nov_opt["DATE"]
nov_opt["DATE"] = pd.to_datetime(nov_opt["DATE"],format='%Y%m%d')
nov_opt["STRIKE_DATE"] = pd.to_datetime(nov_opt["STRIKE_DATE"],format='%Y%m%d')

# load stock prices from yahoo finance and create variables combining prices and strikes


abbmc=pd.read_csv("/users/jorge/downloads/abbmc.csv")

abbmc["Date"] = pd.to_datetime(abbmc["Date"],format='%Y-%m-%d')

abbmc_options=nov_opt[nov_opt['CODE'].str.contains("ABB")]
abbmc_options["money"]= abbmc_options["STRIKE"] - abbmc_options["LIQ"]

sanvrai=[]
n=abbmc_options.shape[0]
for i in range(0,n):
    san=abbmc[(abbmc["Date"] > abbmc_options["DATE"].iloc[i]) & (abbmc["Date"] < abbmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

abbmc_options["MAX"]=sanvrai
abbmc_optionsdate= abbmc_options[abbmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=abbmc_optionsdate.shape[0]
for i in range(0,n):
    sant=abbmc[(abbmc["Date"] > abbmc_optionsdate["DATE"].iloc[i]) & (abbmc["Date"] < abbmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
abbmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=abbmc[abbmc["Date"] == abbmc_optionsdate["DATE"].iloc[i]]
    santo=abbmc[abbmc["Date"] == abbmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

abbmc_optionsdate["GAIN"]=sanper






old=abbmc[(abbmc["Date"]>"2013-11-01") & (abbmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




abbmc_optionsdate["1ySTD"]=oldie


old6=abbmc[(abbmc["Date"]>"2014-05-01") & (abbmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
abbmc_optionsdate["6mSTD"]=oldie6

old3=abbmc[(abbmc["Date"]>"2014-08-01") & (abbmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
abbmc_optionsdate["3mSTD"]=oldie3


abemc=pd.read_csv("/users/jorge/downloads/abemc.csv")

abemc["Date"] = pd.to_datetime(abemc["Date"],format='%Y-%m-%d')

abemc_options=nov_opt[nov_opt['CODE'].str.contains("ABE")]
abemc_options["money"]= abemc_options["STRIKE"] - abemc_options["LIQ"]

sanvrai=[]
n=abemc_options.shape[0]
for i in range(0,n):
    san=abemc[(abemc["Date"] > abemc_options["DATE"].iloc[i]) & (abemc["Date"] < abemc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

abemc_options["MAX"]=sanvrai
abemc_optionsdate= abemc_options[abemc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=abemc_optionsdate.shape[0]
for i in range(0,n):
    sant=abemc[(abemc["Date"] > abemc_optionsdate["DATE"].iloc[i]) & (abemc["Date"] < abemc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
abemc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=abemc[abemc["Date"] == abemc_optionsdate["DATE"].iloc[i]]
    santo=abemc[abemc["Date"] == abemc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

abemc_optionsdate["GAIN"]=sanper






old=abemc[(abemc["Date"]>"2013-11-01") & (abemc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




abemc_optionsdate["1ySTD"]=oldie


old6=abemc[(abemc["Date"]>"2014-05-01") & (abemc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
abemc_optionsdate["6mSTD"]=oldie6

old3=abemc[(abemc["Date"]>"2014-08-01") & (abemc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
abemc_optionsdate["3mSTD"]=oldie3

acsmc=pd.read_csv("/users/jorge/downloads/acsmc.csv")

acsmc["Date"] = pd.to_datetime(acsmc["Date"],format='%Y-%m-%d')

acsmc_options=nov_opt[nov_opt['CODE'].str.contains("ACS")]
acsmc_options["money"]= acsmc_options["STRIKE"] - acsmc_options["LIQ"]

sanvrai=[]
n=acsmc_options.shape[0]
for i in range(0,n):
    san=acsmc[(acsmc["Date"] > acsmc_options["DATE"].iloc[i]) & (acsmc["Date"] < acsmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

acsmc_options["MAX"]=sanvrai
acsmc_optionsdate= acsmc_options[acsmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=acsmc_optionsdate.shape[0]
for i in range(0,n):
    sant=acsmc[(acsmc["Date"] > acsmc_optionsdate["DATE"].iloc[i]) & (acsmc["Date"] < acsmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
acsmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=acsmc[acsmc["Date"] == acsmc_optionsdate["DATE"].iloc[i]]
    santo=acsmc[acsmc["Date"] == acsmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

acsmc_optionsdate["GAIN"]=sanper






old=acsmc[(acsmc["Date"]>"2013-11-01") & (acsmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




acsmc_optionsdate["1ySTD"]=oldie


old6=acsmc[(acsmc["Date"]>"2014-05-01") & (acsmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
acsmc_optionsdate["6mSTD"]=oldie6

old3=acsmc[(acsmc["Date"]>"2014-08-01") & (acsmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
acsmc_optionsdate["3mSTD"]=oldie3

acxmc=pd.read_csv("/users/jorge/downloads/acxmc.csv")

acxmc["Date"] = pd.to_datetime(acxmc["Date"],format='%Y-%m-%d')

acxmc_options=nov_opt[nov_opt['CODE'].str.contains("ACX")]
acxmc_options["money"]= acxmc_options["STRIKE"] - acxmc_options["LIQ"]

sanvrai=[]
n=acxmc_options.shape[0]
for i in range(0,n):
    san=acxmc[(acxmc["Date"] > acxmc_options["DATE"].iloc[i]) & (acxmc["Date"] < acxmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

acxmc_options["MAX"]=sanvrai
acxmc_optionsdate= acxmc_options[acxmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=acxmc_optionsdate.shape[0]
for i in range(0,n):
    sant=acxmc[(acxmc["Date"] > acxmc_optionsdate["DATE"].iloc[i]) & (acxmc["Date"] < acxmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
acxmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=acxmc[acxmc["Date"] == acxmc_optionsdate["DATE"].iloc[i]]
    santo=acxmc[acxmc["Date"] == acxmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

acxmc_optionsdate["GAIN"]=sanper






old=acxmc[(acxmc["Date"]>"2013-11-01") & (acxmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




acxmc_optionsdate["1ySTD"]=oldie


old6=acxmc[(acxmc["Date"]>"2014-05-01") & (acxmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
acxmc_optionsdate["6mSTD"]=oldie6

old3=acxmc[(acxmc["Date"]>"2014-08-01") & (acxmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
acxmc_optionsdate["3mSTD"]=oldie3

amsmc=pd.read_csv("/users/jorge/downloads/amsmc.csv")

amsmc["Date"] = pd.to_datetime(amsmc["Date"],format='%Y-%m-%d')

amsmc_options=nov_opt[nov_opt['CODE'].str.contains("AMS")]
amsmc_options["money"]= amsmc_options["STRIKE"] - amsmc_options["LIQ"]

sanvrai=[]
n=amsmc_options.shape[0]
for i in range(0,n):
    san=amsmc[(amsmc["Date"] > amsmc_options["DATE"].iloc[i]) & (amsmc["Date"] < amsmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

amsmc_options["MAX"]=sanvrai
amsmc_optionsdate= amsmc_options[amsmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=amsmc_optionsdate.shape[0]
for i in range(0,n):
    sant=amsmc[(amsmc["Date"] > amsmc_optionsdate["DATE"].iloc[i]) & (amsmc["Date"] < amsmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
amsmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=amsmc[amsmc["Date"] == amsmc_optionsdate["DATE"].iloc[i]]
    santo=amsmc[amsmc["Date"] == amsmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

amsmc_optionsdate["GAIN"]=sanper






old=amsmc[(amsmc["Date"]>"2013-11-01") & (amsmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




amsmc_optionsdate["1ySTD"]=oldie


old6=amsmc[(amsmc["Date"]>"2014-05-01") & (amsmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
amsmc_optionsdate["6mSTD"]=oldie6

old3=amsmc[(amsmc["Date"]>"2014-08-01") & (amsmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
amsmc_optionsdate["3mSTD"]=oldie3

anamc=pd.read_csv("/users/jorge/downloads/anamc.csv")

anamc["Date"] = pd.to_datetime(anamc["Date"],format='%Y-%m-%d')

anamc_options=nov_opt[nov_opt['CODE'].str.contains("CANA")]
anamc_options["money"]= anamc_options["STRIKE"] - anamc_options["LIQ"]

sanvrai=[]
n=anamc_options.shape[0]
for i in range(0,n):
    san=anamc[(anamc["Date"] > anamc_options["DATE"].iloc[i]) & (anamc["Date"] < anamc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

anamc_options["MAX"]=sanvrai
anamc_optionsdate= anamc_options[anamc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=anamc_optionsdate.shape[0]
for i in range(0,n):
    sant=anamc[(anamc["Date"] > anamc_optionsdate["DATE"].iloc[i]) & (anamc["Date"] < anamc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
anamc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=anamc[anamc["Date"] == anamc_optionsdate["DATE"].iloc[i]]
    santo=anamc[anamc["Date"] == anamc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

anamc_optionsdate["GAIN"]=sanper






old=anamc[(anamc["Date"]>"2013-11-01") & (anamc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




anamc_optionsdate["1ySTD"]=oldie


old6=anamc[(anamc["Date"]>"2014-05-01") & (anamc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
anamc_optionsdate["6mSTD"]=oldie6

old3=anamc[(anamc["Date"]>"2014-08-01") & (anamc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
anamc_optionsdate["3mSTD"]=oldie3

bbvamc=pd.read_csv("/users/jorge/downloads/bbvamc.csv")

bbvamc["Date"] = pd.to_datetime(bbvamc["Date"],format='%Y-%m-%d')

bbvamc_options=nov_opt[nov_opt['CODE'].str.contains("BBV")]
bbvamc_options["money"]= bbvamc_options["STRIKE"] - bbvamc_options["LIQ"]

sanvrai=[]
n=bbvamc_options.shape[0]
for i in range(0,n):
    san=bbvamc[(bbvamc["Date"] > bbvamc_options["DATE"].iloc[i]) & (bbvamc["Date"] < bbvamc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

bbvamc_options["MAX"]=sanvrai
bbvamc_optionsdate= bbvamc_options[bbvamc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=bbvamc_optionsdate.shape[0]
for i in range(0,n):
    sant=bbvamc[(bbvamc["Date"] > bbvamc_optionsdate["DATE"].iloc[i]) & (bbvamc["Date"] < bbvamc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
bbvamc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=bbvamc[bbvamc["Date"] == bbvamc_optionsdate["DATE"].iloc[i]]
    santo=bbvamc[bbvamc["Date"] == bbvamc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

bbvamc_optionsdate["GAIN"]=sanper






old=bbvamc[(bbvamc["Date"]>"2013-11-01") & (bbvamc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




bbvamc_optionsdate["1ySTD"]=oldie


old6=bbvamc[(bbvamc["Date"]>"2014-05-01") & (bbvamc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
bbvamc_optionsdate["6mSTD"]=oldie6

old3=bbvamc[(bbvamc["Date"]>"2014-08-01") & (bbvamc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
bbvamc_optionsdate["3mSTD"]=oldie3

bkiamc=pd.read_csv("/users/jorge/downloads/bkiamc.csv")

bkiamc["Date"] = pd.to_datetime(bkiamc["Date"],format='%Y-%m-%d')

bkiamc_options=nov_opt[nov_opt['CODE'].str.contains("BKIA")]
bkiamc_options["money"]= bkiamc_options["STRIKE"] - bkiamc_options["LIQ"]

sanvrai=[]
n=bkiamc_options.shape[0]
for i in range(0,n):
    san=bkiamc[(bkiamc["Date"] > bkiamc_options["DATE"].iloc[i]) & (bkiamc["Date"] < bkiamc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

bkiamc_options["MAX"]=sanvrai
bkiamc_optionsdate= bkiamc_options[bkiamc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=bkiamc_optionsdate.shape[0]
for i in range(0,n):
    sant=bkiamc[(bkiamc["Date"] > bkiamc_optionsdate["DATE"].iloc[i]) & (bkiamc["Date"] < bkiamc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
bkiamc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=bkiamc[bkiamc["Date"] == bkiamc_optionsdate["DATE"].iloc[i]]
    santo=bkiamc[bkiamc["Date"] == bkiamc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

bkiamc_optionsdate["GAIN"]=sanper






old=bkiamc[(bkiamc["Date"]>"2013-11-01") & (bkiamc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




bkiamc_optionsdate["1ySTD"]=oldie


old6=bkiamc[(bkiamc["Date"]>"2014-05-01") & (bkiamc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
bkiamc_optionsdate["6mSTD"]=oldie6

old3=bkiamc[(bkiamc["Date"]>"2014-08-01") & (bkiamc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
bkiamc_optionsdate["3mSTD"]=oldie3

bktmc=pd.read_csv("/users/jorge/downloads/bktmc.csv")

bktmc["Date"] = pd.to_datetime(bktmc["Date"],format='%Y-%m-%d')

bktmc_options=nov_opt[nov_opt['CODE'].str.contains("BTK")]
bktmc_options["money"]= bktmc_options["STRIKE"] - bktmc_options["LIQ"]

sanvrai=[]
n=bktmc_options.shape[0]
for i in range(0,n):
    san=bktmc[(bktmc["Date"] > bktmc_options["DATE"].iloc[i]) & (bktmc["Date"] < bktmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

bktmc_options["MAX"]=sanvrai
bktmc_optionsdate= bktmc_options[bktmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=bktmc_optionsdate.shape[0]
for i in range(0,n):
    sant=bktmc[(bktmc["Date"] > bktmc_optionsdate["DATE"].iloc[i]) & (bktmc["Date"] < bktmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
bktmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=bktmc[bktmc["Date"] == bktmc_optionsdate["DATE"].iloc[i]]
    santo=bktmc[bktmc["Date"] == bktmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

bktmc_optionsdate["GAIN"]=sanper






old=bktmc[(bktmc["Date"]>"2013-11-01") & (bktmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




bktmc_optionsdate["1ySTD"]=oldie


old6=bktmc[(bktmc["Date"]>"2014-05-01") & (bktmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
bktmc_optionsdate["6mSTD"]=oldie6

old3=bktmc[(bktmc["Date"]>"2014-08-01") & (bktmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
bktmc_optionsdate["3mSTD"]=oldie3

bmemc=pd.read_csv("/users/jorge/downloads/bmemc.csv")

bmemc["Date"] = pd.to_datetime(bmemc["Date"],format='%Y-%m-%d')

bmemc_options=nov_opt[nov_opt['CODE'].str.contains("BME")]
bmemc_options["money"]= bmemc_options["STRIKE"] - bmemc_options["LIQ"]

sanvrai=[]
n=bmemc_options.shape[0]
for i in range(0,n):
    san=bmemc[(bmemc["Date"] > bmemc_options["DATE"].iloc[i]) & (bmemc["Date"] < bmemc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

bmemc_options["MAX"]=sanvrai
bmemc_optionsdate= bmemc_options[bmemc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=bmemc_optionsdate.shape[0]
for i in range(0,n):
    sant=bmemc[(bmemc["Date"] > bmemc_optionsdate["DATE"].iloc[i]) & (bmemc["Date"] < bmemc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
bmemc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=bmemc[bmemc["Date"] == bmemc_optionsdate["DATE"].iloc[i]]
    santo=bmemc[bmemc["Date"] == bmemc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

bmemc_optionsdate["GAIN"]=sanper






old=bmemc[(bmemc["Date"]>"2013-11-01") & (bmemc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




bmemc_optionsdate["1ySTD"]=oldie


old6=bmemc[(bmemc["Date"]>"2014-05-01") & (bmemc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
bmemc_optionsdate["6mSTD"]=oldie6

old3=bmemc[(bmemc["Date"]>"2014-08-01") & (bmemc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
bmemc_optionsdate["3mSTD"]=oldie3

cabmc=pd.read_csv("/users/jorge/downloads/cabmc.csv")

cabmc["Date"] = pd.to_datetime(cabmc["Date"],format='%Y-%m-%d')

cabmc_options=nov_opt[nov_opt['CODE'].str.contains("CCAB")]
cabmc_options["money"]= cabmc_options["STRIKE"] - cabmc_options["LIQ"]

sanvrai=[]
n=cabmc_options.shape[0]
for i in range(0,n):
    san=cabmc[(cabmc["Date"] > cabmc_options["DATE"].iloc[i]) & (cabmc["Date"] < cabmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["Adj Close"].max())

cabmc_options["MAX"]=sanvrai
cabmc_optionsdate= cabmc_options[cabmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=cabmc_optionsdate.shape[0]
for i in range(0,n):
    sant=cabmc[(cabmc["Date"] > cabmc_optionsdate["DATE"].iloc[i]) & (cabmc["Date"] < cabmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["Adj Close"].std())
cabmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=cabmc[cabmc["Date"] == cabmc_optionsdate["DATE"].iloc[i]]
    santo=cabmc[cabmc["Date"] == cabmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Adj Close"].iloc[1] - gain["Adj Close"].iloc[0]) / gain["Adj Close"].iloc[0]
    sanper.append(income)

cabmc_optionsdate["GAIN"]=sanper






old=cabmc[(cabmc["Date"]>"2013-11-01") & (cabmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["Adj Close"].std())




cabmc_optionsdate["1ySTD"]=oldie


old6=cabmc[(cabmc["Date"]>"2014-05-01") & (cabmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["Adj Close"].std())
cabmc_optionsdate["6mSTD"]=oldie6

old3=cabmc[(cabmc["Date"]>"2014-08-01") & (cabmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["Adj Close"].std())
cabmc_optionsdate["3mSTD"]=oldie3

ebrmc=pd.read_csv("/users/jorge/downloads/ebrmc.csv")

ebrmc["Date"] = pd.to_datetime(ebrmc["Date"],format='%Y-%m-%d')

ebrmc_options=nov_opt[nov_opt['CODE'].str.contains("EBR")]
ebrmc_options["money"]= ebrmc_options["STRIKE"] - ebrmc_options["LIQ"]

sanvrai=[]
n=ebrmc_options.shape[0]
for i in range(0,n):
    san=ebrmc[(ebrmc["Date"] > ebrmc_options["DATE"].iloc[i]) & (ebrmc["Date"] < ebrmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

ebrmc_options["MAX"]=sanvrai
ebrmc_optionsdate= ebrmc_options[ebrmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=ebrmc_optionsdate.shape[0]
for i in range(0,n):
    sant=ebrmc[(ebrmc["Date"] > ebrmc_optionsdate["DATE"].iloc[i]) & (ebrmc["Date"] < ebrmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
ebrmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=ebrmc[ebrmc["Date"] == ebrmc_optionsdate["DATE"].iloc[i]]
    santo=ebrmc[ebrmc["Date"] == ebrmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

ebrmc_optionsdate["GAIN"]=sanper






old=ebrmc[(ebrmc["Date"]>"2013-11-01") & (ebrmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




ebrmc_optionsdate["1ySTD"]=oldie


old6=ebrmc[(ebrmc["Date"]>"2014-05-01") & (ebrmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
ebrmc_optionsdate["6mSTD"]=oldie6

old3=ebrmc[(ebrmc["Date"]>"2014-08-01") & (ebrmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
ebrmc_optionsdate["3mSTD"]=oldie3

elemc=pd.read_csv("/users/jorge/downloads/elemc.csv")

elemc["Date"] = pd.to_datetime(elemc["Date"],format='%Y-%m-%d')

elemc_options=nov_opt[nov_opt['CODE'].str.contains("ELE")]
elemc_options["money"]= elemc_options["STRIKE"] - elemc_options["LIQ"]

sanvrai=[]
n=elemc_options.shape[0]
for i in range(0,n):
    san=elemc[(elemc["Date"] > elemc_options["DATE"].iloc[i]) & (elemc["Date"] < elemc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

elemc_options["MAX"]=sanvrai
elemc_optionsdate= elemc_options[elemc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=elemc_optionsdate.shape[0]
for i in range(0,n):
    sant=elemc[(elemc["Date"] > elemc_optionsdate["DATE"].iloc[i]) & (elemc["Date"] < elemc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
elemc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=elemc[elemc["Date"] == elemc_optionsdate["DATE"].iloc[i]]
    santo=elemc[elemc["Date"] == elemc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

elemc_optionsdate["GAIN"]=sanper






old=elemc[(elemc["Date"]>"2013-11-01") & (elemc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




elemc_optionsdate["1ySTD"]=oldie


old6=elemc[(elemc["Date"]>"2014-05-01") & (elemc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
elemc_optionsdate["6mSTD"]=oldie6

old3=elemc[(elemc["Date"]>"2014-08-01") & (elemc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
elemc_optionsdate["3mSTD"]=oldie3

enamc=pd.read_csv("/users/jorge/downloads/enamc.csv")

enamc["Date"] = pd.to_datetime(enamc["Date"],format='%Y-%m-%d')

enamc_options=nov_opt[nov_opt['CODE'].str.contains("CENA")]
enamc_options["money"]= enamc_options["STRIKE"] - enamc_options["LIQ"]

sanvrai=[]
n=enamc_options.shape[0]
for i in range(0,n):
    san=enamc[(enamc["Date"] > enamc_options["DATE"].iloc[i]) & (enamc["Date"] < enamc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

enamc_options["MAX"]=sanvrai
enamc_optionsdate= enamc_options[enamc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=enamc_optionsdate.shape[0]
for i in range(0,n):
    sant=enamc[(enamc["Date"] > enamc_optionsdate["DATE"].iloc[i]) & (enamc["Date"] < enamc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
enamc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=enamc[enamc["Date"] == enamc_optionsdate["DATE"].iloc[i]]
    santo=enamc[enamc["Date"] == enamc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

enamc_optionsdate["GAIN"]=sanper






old=enamc[(enamc["Date"]>"2013-11-01") & (enamc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




enamc_optionsdate["1ySTD"]=oldie


old6=enamc[(enamc["Date"]>"2014-05-01") & (enamc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
enamc_optionsdate["6mSTD"]=oldie6

old3=enamc[(enamc["Date"]>"2014-08-01") & (enamc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
enamc_optionsdate["3mSTD"]=oldie3

fccmc=pd.read_csv("/users/jorge/downloads/fccmc.csv")

fccmc["Date"] = pd.to_datetime(fccmc["Date"],format='%Y-%m-%d')

fccmc_options=nov_opt[nov_opt['CODE'].str.contains("FCC")]
fccmc_options["money"]= fccmc_options["STRIKE"] - fccmc_options["LIQ"]

sanvrai=[]
n=fccmc_options.shape[0]
for i in range(0,n):
    san=fccmc[(fccmc["Date"] > fccmc_options["DATE"].iloc[i]) & (fccmc["Date"] < fccmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

fccmc_options["MAX"]=sanvrai
fccmc_optionsdate= fccmc_options[fccmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=fccmc_optionsdate.shape[0]
for i in range(0,n):
    sant=fccmc[(fccmc["Date"] > fccmc_optionsdate["DATE"].iloc[i]) & (fccmc["Date"] < fccmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
fccmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=fccmc[fccmc["Date"] == fccmc_optionsdate["DATE"].iloc[i]]
    santo=fccmc[fccmc["Date"] == fccmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

fccmc_optionsdate["GAIN"]=sanper






old=fccmc[(fccmc["Date"]>"2013-11-01") & (fccmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




fccmc_optionsdate["1ySTD"]=oldie


old6=fccmc[(fccmc["Date"]>"2014-05-01") & (fccmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
fccmc_optionsdate["6mSTD"]=oldie6

old3=fccmc[(fccmc["Date"]>"2014-08-01") & (fccmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
fccmc_optionsdate["3mSTD"]=oldie3

fermc=pd.read_csv("/users/jorge/downloads/fermc.csv")

fermc["Date"] = pd.to_datetime(fermc["Date"],format='%Y-%m-%d')

fermc_options=nov_opt[nov_opt['CODE'].str.contains("FER")]
fermc_options["money"]= fermc_options["STRIKE"] - fermc_options["LIQ"]

sanvrai=[]
n=fermc_options.shape[0]
for i in range(0,n):
    san=fermc[(fermc["Date"] > fermc_options["DATE"].iloc[i]) & (fermc["Date"] < fermc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

fermc_options["MAX"]=sanvrai
fermc_optionsdate= fermc_options[fermc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=fermc_optionsdate.shape[0]
for i in range(0,n):
    sant=fermc[(fermc["Date"] > fermc_optionsdate["DATE"].iloc[i]) & (fermc["Date"] < fermc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
fermc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=fermc[fermc["Date"] == fermc_optionsdate["DATE"].iloc[i]]
    santo=fermc[fermc["Date"] == fermc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

fermc_optionsdate["GAIN"]=sanper






old=fermc[(fermc["Date"]>"2013-11-01") & (fermc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




fermc_optionsdate["1ySTD"]=oldie


old6=fermc[(fermc["Date"]>"2014-05-01") & (fermc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
fermc_optionsdate["6mSTD"]=oldie6

old3=fermc[(fermc["Date"]>"2014-08-01") & (fermc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
fermc_optionsdate["3mSTD"]=oldie3

gammc=pd.read_csv("/users/jorge/downloads/gammc.csv")

gammc["Date"] = pd.to_datetime(gammc["Date"],format='%Y-%m-%d')

gammc_options=nov_opt[nov_opt['CODE'].str.contains("CGAM")]
gammc_options["money"]= gammc_options["STRIKE"] - gammc_options["LIQ"]

sanvrai=[]
n=gammc_options.shape[0]
for i in range(0,n):
    san=gammc[(gammc["Date"] > gammc_options["DATE"].iloc[i]) & (gammc["Date"] < gammc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

gammc_options["MAX"]=sanvrai
gammc_optionsdate= gammc_options[gammc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=gammc_optionsdate.shape[0]
for i in range(0,n):
    sant=gammc[(gammc["Date"] > gammc_optionsdate["DATE"].iloc[i]) & (gammc["Date"] < gammc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
gammc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=gammc[gammc["Date"] == gammc_optionsdate["DATE"].iloc[i]]
    santo=gammc[gammc["Date"] == gammc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

gammc_optionsdate["GAIN"]=sanper






old=gammc[(gammc["Date"]>"2013-11-01") & (gammc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




gammc_optionsdate["1ySTD"]=oldie


old6=gammc[(gammc["Date"]>"2014-05-01") & (gammc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
gammc_optionsdate["6mSTD"]=oldie6

old3=gammc[(gammc["Date"]>"2014-08-01") & (gammc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
gammc_optionsdate["3mSTD"]=oldie3

gasmc=pd.read_csv("/users/jorge/downloads/gasmc.csv")

gasmc["Date"] = pd.to_datetime(gasmc["Date"],format='%Y-%m-%d')

gasmc_options=nov_opt[nov_opt['CODE'].str.contains("GAS")]
gasmc_options["money"]= gasmc_options["STRIKE"] - gasmc_options["LIQ"]

sanvrai=[]
n=gasmc_options.shape[0]
for i in range(0,n):
    san=gasmc[(gasmc["Date"] > gasmc_options["DATE"].iloc[i]) & (gasmc["Date"] < gasmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

gasmc_options["MAX"]=sanvrai
gasmc_optionsdate= gasmc_options[gasmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=gasmc_optionsdate.shape[0]
for i in range(0,n):
    sant=gasmc[(gasmc["Date"] > gasmc_optionsdate["DATE"].iloc[i]) & (gasmc["Date"] < gasmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
gasmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=gasmc[gasmc["Date"] == gasmc_optionsdate["DATE"].iloc[i]]
    santo=gasmc[gasmc["Date"] == gasmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

gasmc_optionsdate["GAIN"]=sanper






old=gasmc[(gasmc["Date"]>"2013-11-01") & (gasmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




gasmc_optionsdate["1ySTD"]=oldie


old6=gasmc[(gasmc["Date"]>"2014-05-01") & (gasmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
gasmc_optionsdate["6mSTD"]=oldie6

old3=gasmc[(gasmc["Date"]>"2014-08-01") & (gasmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
gasmc_optionsdate["3mSTD"]=oldie3

grfmc=pd.read_csv("/users/jorge/downloads/grfmc.csv")

grfmc["Date"] = pd.to_datetime(grfmc["Date"],format='%Y-%m-%d')

grfmc_options=nov_opt[nov_opt['CODE'].str.contains("GFR")]
grfmc_options["money"]= grfmc_options["STRIKE"] - grfmc_options["LIQ"]

sanvrai=[]
n=grfmc_options.shape[0]
for i in range(0,n):
    san=grfmc[(grfmc["Date"] > grfmc_options["DATE"].iloc[i]) & (grfmc["Date"] < grfmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

grfmc_options["MAX"]=sanvrai
grfmc_optionsdate= grfmc_options[grfmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=grfmc_optionsdate.shape[0]
for i in range(0,n):
    sant=grfmc[(grfmc["Date"] > grfmc_optionsdate["DATE"].iloc[i]) & (grfmc["Date"] < grfmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
grfmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=grfmc[grfmc["Date"] == grfmc_optionsdate["DATE"].iloc[i]]
    santo=grfmc[grfmc["Date"] == grfmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

grfmc_optionsdate["GAIN"]=sanper






old=grfmc[(grfmc["Date"]>"2013-11-01") & (grfmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




grfmc_optionsdate["1ySTD"]=oldie


old6=grfmc[(grfmc["Date"]>"2014-05-01") & (grfmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
grfmc_optionsdate["6mSTD"]=oldie6

old3=grfmc[(grfmc["Date"]>"2014-08-01") & (grfmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
grfmc_optionsdate["3mSTD"]=oldie3

iagmc=pd.read_csv("/users/jorge/downloads/iagmc.csv")

iagmc["Date"] = pd.to_datetime(iagmc["Date"],format='%Y-%m-%d')

iagmc_options=nov_opt[nov_opt['CODE'].str.contains("IAG")]
iagmc_options["money"]= iagmc_options["STRIKE"] - iagmc_options["LIQ"]

sanvrai=[]
n=iagmc_options.shape[0]
for i in range(0,n):
    san=iagmc[(iagmc["Date"] > iagmc_options["DATE"].iloc[i]) & (iagmc["Date"] < iagmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

iagmc_options["MAX"]=sanvrai
iagmc_optionsdate= iagmc_options[iagmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=iagmc_optionsdate.shape[0]
for i in range(0,n):
    sant=iagmc[(iagmc["Date"] > iagmc_optionsdate["DATE"].iloc[i]) & (iagmc["Date"] < iagmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
iagmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=iagmc[iagmc["Date"] == iagmc_optionsdate["DATE"].iloc[i]]
    santo=iagmc[iagmc["Date"] == iagmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

iagmc_optionsdate["GAIN"]=sanper






old=iagmc[(iagmc["Date"]>"2013-11-01") & (iagmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




iagmc_optionsdate["1ySTD"]=oldie


old6=iagmc[(iagmc["Date"]>"2014-05-01") & (iagmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
iagmc_optionsdate["6mSTD"]=oldie6

old3=iagmc[(iagmc["Date"]>"2014-08-01") & (iagmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
iagmc_optionsdate["3mSTD"]=oldie3

idrmc=pd.read_csv("/users/jorge/downloads/idrmc.csv")

idrmc["Date"] = pd.to_datetime(idrmc["Date"],format='%Y-%m-%d')

idrmc_options=nov_opt[nov_opt['CODE'].str.contains("IDR")]
idrmc_options["money"]= idrmc_options["STRIKE"] - idrmc_options["LIQ"]

sanvrai=[]
n=idrmc_options.shape[0]
for i in range(0,n):
    san=idrmc[(idrmc["Date"] > idrmc_options["DATE"].iloc[i]) & (idrmc["Date"] < idrmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

idrmc_options["MAX"]=sanvrai
idrmc_optionsdate= idrmc_options[idrmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=idrmc_optionsdate.shape[0]
for i in range(0,n):
    sant=idrmc[(idrmc["Date"] > idrmc_optionsdate["DATE"].iloc[i]) & (idrmc["Date"] < idrmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
idrmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=idrmc[idrmc["Date"] == idrmc_optionsdate["DATE"].iloc[i]]
    santo=idrmc[idrmc["Date"] == idrmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

idrmc_optionsdate["GAIN"]=sanper






old=idrmc[(idrmc["Date"]>"2013-11-01") & (idrmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




idrmc_optionsdate["1ySTD"]=oldie


old6=idrmc[(idrmc["Date"]>"2014-05-01") & (idrmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
idrmc_optionsdate["6mSTD"]=oldie6

old3=idrmc[(idrmc["Date"]>"2014-08-01") & (idrmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
idrmc_optionsdate["3mSTD"]=oldie3

itxmc=pd.read_csv("/users/jorge/downloads/itxmc.csv")

itxmc["Date"] = pd.to_datetime(itxmc["Date"],format='%y-%m-%d')

itxmc_options=nov_opt[nov_opt['CODE'].str.contains("ITX")]
itxmc_options["money"]= itxmc_options["STRIKE"] - itxmc_options["LIQ"]

sanvrai=[]
n=itxmc_options.shape[0]
for i in range(0,n):
    san=itxmc[(itxmc["Date"] > itxmc_options["DATE"].iloc[i]) & (itxmc["Date"] < itxmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

itxmc_options["MAX"]=sanvrai
itxmc_optionsdate= itxmc_options[itxmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=itxmc_optionsdate.shape[0]
for i in range(0,n):
    sant=itxmc[(itxmc["Date"] > itxmc_optionsdate["DATE"].iloc[i]) & (itxmc["Date"] < itxmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
itxmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=itxmc[itxmc["Date"] == itxmc_optionsdate["DATE"].iloc[i]]
    santo=itxmc[itxmc["Date"] == itxmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

itxmc_optionsdate["GAIN"]=sanper






old=itxmc[(itxmc["Date"]>"2013-11-01") & (itxmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




itxmc_optionsdate["1ySTD"]=oldie


old6=itxmc[(itxmc["Date"]>"2014-05-01") & (itxmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
itxmc_optionsdate["6mSTD"]=oldie6

old3=itxmc[(itxmc["Date"]>"2014-08-01") & (itxmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
itxmc_optionsdate["3mSTD"]=oldie3

mapmc=pd.read_csv("/users/jorge/downloads/mapmc.csv")

mapmc["Date"] = pd.to_datetime(mapmc["Date"],format='%Y-%m-%d')

mapmc_options=nov_opt[nov_opt['CODE'].str.contains("MAP")]
mapmc_options["money"]= mapmc_options["STRIKE"] - mapmc_options["LIQ"]

sanvrai=[]
n=mapmc_options.shape[0]
for i in range(0,n):
    san=mapmc[(mapmc["Date"] > mapmc_options["DATE"].iloc[i]) & (mapmc["Date"] < mapmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

mapmc_options["MAX"]=sanvrai
mapmc_optionsdate= mapmc_options[mapmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=mapmc_optionsdate.shape[0]
for i in range(0,n):
    sant=mapmc[(mapmc["Date"] > mapmc_optionsdate["DATE"].iloc[i]) & (mapmc["Date"] < mapmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
mapmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=mapmc[mapmc["Date"] == mapmc_optionsdate["DATE"].iloc[i]]
    santo=mapmc[mapmc["Date"] == mapmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

mapmc_optionsdate["GAIN"]=sanper






old=mapmc[(mapmc["Date"]>"2013-11-01") & (mapmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




mapmc_optionsdate["1ySTD"]=oldie


old6=mapmc[(mapmc["Date"]>"2014-05-01") & (mapmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
mapmc_optionsdate["6mSTD"]=oldie6

old3=mapmc[(mapmc["Date"]>"2014-08-01") & (mapmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
mapmc_optionsdate["3mSTD"]=oldie3

mtsmc=pd.read_csv("/users/jorge/downloads/mtsmc.csv")

mtsmc["Date"] = pd.to_datetime(mtsmc["Date"],format='%Y-%m-%d')

mtsmc_options=nov_opt[nov_opt['CODE'].str.contains("MTS")]
mtsmc_options["money"]= mtsmc_options["STRIKE"] - mtsmc_options["LIQ"]

sanvrai=[]
n=mtsmc_options.shape[0]
for i in range(0,n):
    san=mtsmc[(mtsmc["Date"] > mtsmc_options["DATE"].iloc[i]) & (mtsmc["Date"] < mtsmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

mtsmc_options["MAX"]=sanvrai
mtsmc_optionsdate= mtsmc_options[mtsmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=mtsmc_optionsdate.shape[0]
for i in range(0,n):
    sant=mtsmc[(mtsmc["Date"] > mtsmc_optionsdate["DATE"].iloc[i]) & (mtsmc["Date"] < mtsmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
mtsmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=mtsmc[mtsmc["Date"] == mtsmc_optionsdate["DATE"].iloc[i]]
    santo=mtsmc[mtsmc["Date"] == mtsmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

mtsmc_optionsdate["GAIN"]=sanper






old=mtsmc[(mtsmc["Date"]>"2013-11-01") & (mtsmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




mtsmc_optionsdate["1ySTD"]=oldie


old6=mtsmc[(mtsmc["Date"]>"2014-05-01") & (mtsmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
mtsmc_optionsdate["6mSTD"]=oldie6

old3=mtsmc[(mtsmc["Date"]>"2014-08-01") & (mtsmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
mtsmc_optionsdate["3mSTD"]=oldie3

ohlmc=pd.read_csv("/users/jorge/downloads/ohlmc.csv")

ohlmc["Date"] = pd.to_datetime(ohlmc["Date"],format='%Y-%m-%d')

ohlmc_options=nov_opt[nov_opt['CODE'].str.contains("OHL")]
ohlmc_options["money"]= ohlmc_options["STRIKE"] - ohlmc_options["LIQ"]

sanvrai=[]
n=ohlmc_options.shape[0]
for i in range(0,n):
    san=ohlmc[(ohlmc["Date"] > ohlmc_options["DATE"].iloc[i]) & (ohlmc["Date"] < ohlmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

ohlmc_options["MAX"]=sanvrai
ohlmc_optionsdate= ohlmc_options[ohlmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=ohlmc_optionsdate.shape[0]
for i in range(0,n):
    sant=ohlmc[(ohlmc["Date"] > ohlmc_optionsdate["DATE"].iloc[i]) & (ohlmc["Date"] < ohlmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
ohlmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=ohlmc[ohlmc["Date"] == ohlmc_optionsdate["DATE"].iloc[i]]
    santo=ohlmc[ohlmc["Date"] == ohlmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

ohlmc_optionsdate["GAIN"]=sanper






old=ohlmc[(ohlmc["Date"]>"2013-11-01") & (ohlmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




ohlmc_optionsdate["1ySTD"]=oldie


old6=ohlmc[(ohlmc["Date"]>"2014-05-01") & (ohlmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
ohlmc_optionsdate["6mSTD"]=oldie6

old3=ohlmc[(ohlmc["Date"]>"2014-08-01") & (ohlmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
ohlmc_optionsdate["3mSTD"]=oldie3

popmc=pd.read_csv("/users/jorge/downloads/popmc.csv")

popmc["Date"] = pd.to_datetime(popmc["Date"],format='%Y-%m-%d')

popmc_options=nov_opt[nov_opt['CODE'].str.contains("POP")]
popmc_options["money"]= popmc_options["STRIKE"] - popmc_options["LIQ"]

sanvrai=[]
n=popmc_options.shape[0]
for i in range(0,n):
    san=popmc[(popmc["Date"] > popmc_options["DATE"].iloc[i]) & (popmc["Date"] < popmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

popmc_options["MAX"]=sanvrai
popmc_optionsdate= popmc_options[popmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=popmc_optionsdate.shape[0]
for i in range(0,n):
    sant=popmc[(popmc["Date"] > popmc_optionsdate["DATE"].iloc[i]) & (popmc["Date"] < popmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
popmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=popmc[popmc["Date"] == popmc_optionsdate["DATE"].iloc[i]]
    santo=popmc[popmc["Date"] == popmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

popmc_optionsdate["GAIN"]=sanper






old=popmc[(popmc["Date"]>"2013-11-01") & (popmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




popmc_optionsdate["1ySTD"]=oldie


old6=popmc[(popmc["Date"]>"2014-05-01") & (popmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
popmc_optionsdate["6mSTD"]=oldie6

old3=popmc[(popmc["Date"]>"2014-08-01") & (popmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
popmc_optionsdate["3mSTD"]=oldie3

reemc=pd.read_csv("/users/jorge/downloads/reemc.csv")

reemc["Date"] = pd.to_datetime(reemc["Date"],format='%Y-%m-%d')

reemc_options=nov_opt[nov_opt['CODE'].str.contains("REE")]
reemc_options["money"]= reemc_options["STRIKE"] - reemc_options["LIQ"]

sanvrai=[]
n=reemc_options.shape[0]
for i in range(0,n):
    san=reemc[(reemc["Date"] > reemc_options["DATE"].iloc[i]) & (reemc["Date"] < reemc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

reemc_options["MAX"]=sanvrai
reemc_optionsdate= reemc_options[reemc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=reemc_optionsdate.shape[0]
for i in range(0,n):
    sant=reemc[(reemc["Date"] > reemc_optionsdate["DATE"].iloc[i]) & (reemc["Date"] < reemc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
reemc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=reemc[reemc["Date"] == reemc_optionsdate["DATE"].iloc[i]]
    santo=reemc[reemc["Date"] == reemc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

reemc_optionsdate["GAIN"]=sanper






old=reemc[(reemc["Date"]>"2013-11-01") & (reemc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




reemc_optionsdate["1ySTD"]=oldie


old6=reemc[(reemc["Date"]>"2014-05-01") & (reemc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
reemc_optionsdate["6mSTD"]=oldie6

old3=reemc[(reemc["Date"]>"2014-08-01") & (reemc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
reemc_optionsdate["3mSTD"]=oldie3

repmc=pd.read_csv("/users/jorge/downloads/repmc.csv")

repmc["Date"] = pd.to_datetime(repmc["Date"],format='%Y-%m-%d')

repmc_options=nov_opt[nov_opt['CODE'].str.contains("REP")]
repmc_options["money"]= repmc_options["STRIKE"] - repmc_options["LIQ"]

sanvrai=[]
n=repmc_options.shape[0]
for i in range(0,n):
    san=repmc[(repmc["Date"] > repmc_options["DATE"].iloc[i]) & (repmc["Date"] < repmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

repmc_options["MAX"]=sanvrai
repmc_optionsdate= repmc_options[repmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=repmc_optionsdate.shape[0]
for i in range(0,n):
    sant=repmc[(repmc["Date"] > repmc_optionsdate["DATE"].iloc[i]) & (repmc["Date"] < repmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
repmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=repmc[repmc["Date"] == repmc_optionsdate["DATE"].iloc[i]]
    santo=repmc[repmc["Date"] == repmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

repmc_optionsdate["GAIN"]=sanper






old=repmc[(repmc["Date"]>"2013-11-01") & (repmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




repmc_optionsdate["1ySTD"]=oldie


old6=repmc[(repmc["Date"]>"2014-05-01") & (repmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
repmc_optionsdate["6mSTD"]=oldie6

old3=repmc[(repmc["Date"]>"2014-08-01") & (repmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
repmc_optionsdate["3mSTD"]=oldie3

sabmc=pd.read_csv("/users/jorge/downloads/sabmc.csv")

sabmc["Date"] = pd.to_datetime(sabmc["Date"],format='%Y-%m-%d')

sabmc_options=nov_opt[nov_opt['CODE'].str.contains("SAB")]
sabmc_options["money"]= sabmc_options["STRIKE"] - sabmc_options["LIQ"]

sanvrai=[]
n=sabmc_options.shape[0]
for i in range(0,n):
    san=sabmc[(sabmc["Date"] > sabmc_options["DATE"].iloc[i]) & (sabmc["Date"] < sabmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

sabmc_options["MAX"]=sanvrai
sabmc_optionsdate= sabmc_options[sabmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=sabmc_optionsdate.shape[0]
for i in range(0,n):
    sant=sabmc[(sabmc["Date"] > sabmc_optionsdate["DATE"].iloc[i]) & (sabmc["Date"] < sabmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
sabmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=sabmc[sabmc["Date"] == sabmc_optionsdate["DATE"].iloc[i]]
    santo=sabmc[sabmc["Date"] == sabmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

sabmc_optionsdate["GAIN"]=sanper






old=sabmc[(sabmc["Date"]>"2013-11-01") & (sabmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




sabmc_optionsdate["1ySTD"]=oldie


old6=sabmc[(sabmc["Date"]>"2014-05-01") & (sabmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
sabmc_optionsdate["6mSTD"]=oldie6

old3=sabmc[(sabmc["Date"]>"2014-08-01") & (sabmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
sabmc_optionsdate["3mSTD"]=oldie3

sanmc=pd.read_csv("/users/jorge/downloads/sanmc.csv")

sanmc["Date"] = pd.to_datetime(sanmc["Date"],format='%Y-%m-%d')

sanmc_options=nov_opt[nov_opt['CODE'].str.contains("CSAN")]
sanmc_options["money"]= sanmc_options["STRIKE"] - sanmc_options["LIQ"]

sanvrai=[]
n=sanmc_options.shape[0]
for i in range(0,n):
    san=sanmc[(sanmc["Date"] > sanmc_options["DATE"].iloc[i]) & (sanmc["Date"] < sanmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

sanmc_options["MAX"]=sanvrai
sanmc_optionsdate= sanmc_options[sanmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=sanmc_optionsdate.shape[0]
for i in range(0,n):
    sant=sanmc[(sanmc["Date"] > sanmc_optionsdate["DATE"].iloc[i]) & (sanmc["Date"] < sanmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
sanmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=sanmc[sanmc["Date"] == sanmc_optionsdate["DATE"].iloc[i]]
    santo=sanmc[sanmc["Date"] == sanmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

sanmc_optionsdate["GAIN"]=sanper






old=sanmc[(sanmc["Date"]>"2013-11-01") & (sanmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




sanmc_optionsdate["1ySTD"]=oldie


old6=sanmc[(sanmc["Date"]>"2014-05-01") & (sanmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
sanmc_optionsdate["6mSTD"]=oldie6

old3=sanmc[(sanmc["Date"]>"2014-08-01") & (sanmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
sanmc_optionsdate["3mSTD"]=oldie3

svomc=pd.read_csv("/users/jorge/downloads/svomc.csv")

svomc["Date"] = pd.to_datetime(svomc["Date"],format='%Y-%m-%d')

svomc_options=nov_opt[nov_opt['CODE'].str.contains("SVO")]
svomc_options["money"]= svomc_options["STRIKE"] - svomc_options["LIQ"]

sanvrai=[]
n=svomc_options.shape[0]
for i in range(0,n):
    san=svomc[(svomc["Date"] > svomc_options["DATE"].iloc[i]) & (svomc["Date"] < svomc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

svomc_options["MAX"]=sanvrai
svomc_optionsdate= svomc_options[svomc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=svomc_optionsdate.shape[0]
for i in range(0,n):
    sant=svomc[(svomc["Date"] > svomc_optionsdate["DATE"].iloc[i]) & (svomc["Date"] < svomc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
svomc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=svomc[svomc["Date"] == svomc_optionsdate["DATE"].iloc[i]]
    santo=svomc[svomc["Date"] == svomc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

svomc_optionsdate["GAIN"]=sanper






old=svomc[(svomc["Date"]>"2013-11-01") & (svomc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




svomc_optionsdate["1ySTD"]=oldie


old6=svomc[(svomc["Date"]>"2014-05-01") & (svomc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
svomc_optionsdate["6mSTD"]=oldie6

old3=svomc[(svomc["Date"]>"2014-08-01") & (svomc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
svomc_optionsdate["3mSTD"]=oldie3

tefmc=pd.read_csv("/users/jorge/downloads/tefmc.csv")

tefmc["Date"] = pd.to_datetime(tefmc["Date"],format='%Y-%m-%d')

tefmc_options=nov_opt[nov_opt['CODE'].str.contains("TEF")]
tefmc_options["money"]= tefmc_options["STRIKE"] - tefmc_options["LIQ"]

sanvrai=[]
n=tefmc_options.shape[0]
for i in range(0,n):
    san=tefmc[(tefmc["Date"] > tefmc_options["DATE"].iloc[i]) & (tefmc["Date"] < tefmc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

tefmc_options["MAX"]=sanvrai
tefmc_optionsdate= tefmc_options[tefmc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=tefmc_optionsdate.shape[0]
for i in range(0,n):
    sant=tefmc[(tefmc["Date"] > tefmc_optionsdate["DATE"].iloc[i]) & (tefmc["Date"] < tefmc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
tefmc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=tefmc[tefmc["Date"] == tefmc_optionsdate["DATE"].iloc[i]]
    santo=tefmc[tefmc["Date"] == tefmc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

tefmc_optionsdate["GAIN"]=sanper






old=tefmc[(tefmc["Date"]>"2013-11-01") & (tefmc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




tefmc_optionsdate["1ySTD"]=oldie


old6=tefmc[(tefmc["Date"]>"2014-05-01") & (tefmc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
tefmc_optionsdate["6mSTD"]=oldie6

old3=tefmc[(tefmc["Date"]>"2014-08-01") & (tefmc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
tefmc_optionsdate["3mSTD"]=oldie3

tremc=pd.read_csv("/users/jorge/downloads/tremc.csv")

tremc["Date"] = pd.to_datetime(tremc["Date"],format='%Y-%m-%d')

tremc_options=nov_opt[nov_opt['CODE'].str.contains("TRE")]
tremc_options["money"]= tremc_options["STRIKE"] - tremc_options["LIQ"]

sanvrai=[]
n=tremc_options.shape[0]
for i in range(0,n):
    san=tremc[(tremc["Date"] > tremc_options["DATE"].iloc[i]) & (tremc["Date"] < tremc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

tremc_options["MAX"]=sanvrai
tremc_optionsdate= tremc_options[tremc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=tremc_optionsdate.shape[0]
for i in range(0,n):
    sant=tremc[(tremc["Date"] > tremc_optionsdate["DATE"].iloc[i]) & (tremc["Date"] < tremc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
tremc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=tremc[tremc["Date"] == tremc_optionsdate["DATE"].iloc[i]]
    santo=tremc[tremc["Date"] == tremc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

tremc_optionsdate["GAIN"]=sanper






old=tremc[(tremc["Date"]>"2013-11-01") & (tremc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




tremc_optionsdate["1ySTD"]=oldie


old6=tremc[(tremc["Date"]>"2014-05-01") & (tremc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
tremc_optionsdate["6mSTD"]=oldie6

old3=tremc[(tremc["Date"]>"2014-08-01") & (tremc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
tremc_optionsdate["3mSTD"]=oldie3


vismc=pd.read_csv("/users/jorge/downloads/vismc.csv")

vismc["Date"] = pd.to_datetime(vismc["Date"],format='%Y-%m-%d')

vismc_options=nov_opt[nov_opt['CODE'].str.contains("VIS")]
vismc_options["money"]= vismc_options["STRIKE"] - vismc_options["LIQ"]

sanvrai=[]
n=vismc_options.shape[0]
for i in range(0,n):
    san=vismc[(vismc["Date"] > vismc_options["DATE"].iloc[i]) & (vismc["Date"] < vismc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["High"].max())

vismc_options["MAX"]=sanvrai
vismc_optionsdate= vismc_options[vismc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=vismc_optionsdate.shape[0]
for i in range(0,n):
    sant=vismc[(vismc["Date"] > vismc_optionsdate["DATE"].iloc[i]) & (vismc["Date"] < vismc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["High"].std())
vismc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=vismc[vismc["Date"] == vismc_optionsdate["DATE"].iloc[i]]
    santo=vismc[vismc["Date"] == vismc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Open"].iloc[1] - gain["Close"].iloc[0]) / gain["Close"].iloc[0]
    sanper.append(income)

vismc_optionsdate["GAIN"]=sanper






old=vismc[(vismc["Date"]>"2013-11-01") & (vismc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["High"].std())




vismc_optionsdate["1ySTD"]=oldie


old6=vismc[(vismc["Date"]>"2014-05-01") & (vismc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["High"].std())
vismc_optionsdate["6mSTD"]=oldie6

old3=vismc[(vismc["Date"]>"2014-08-01") & (vismc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["High"].std())
vismc_optionsdate["3mSTD"]=oldie3




ibemc=pd.read_csv("/users/jorge/downloads/ibemc.csv")

ibemc["Date"] = pd.to_datetime(ibemc["Date"],format='%Y-%m-%d')

ibemc_options=nov_opt[nov_opt['CODE'].str.contains("IBE")]
ibemc_options["money"]= ibemc_options["STRIKE"] - ibemc_options["LIQ"]

sanvrai=[]
n=ibemc_options.shape[0]
for i in range(0,n):
    san=ibemc[(ibemc["Date"] > ibemc_options["DATE"].iloc[i]) & (ibemc["Date"] < ibemc_options["STRIKE_DATE"].iloc[i])]
    sanvrai.append(san["Adj Close"].max())

ibemc_options["MAX"]=sanvrai
ibemc_optionsdate= ibemc_options[ibemc_options["STRIKE_DATE"]<"2016-11-30"]

sanai=[]
n=ibemc_optionsdate.shape[0]
for i in range(0,n):
    sant=ibemc[(ibemc["Date"] > ibemc_optionsdate["DATE"].iloc[i]) & (ibemc["Date"] < ibemc_optionsdate["STRIKE_DATE"].iloc[i])]
    sanai.append(sant["Adj Close"].std())
ibemc_optionsdate["STD"]=sanai




sanper=[]

for i in range(0,n):
    santi=ibemc[ibemc["Date"] == ibemc_optionsdate["DATE"].iloc[i]]
    santo=ibemc[ibemc["Date"] == ibemc_optionsdate["STRIKE_DATE"].iloc[i]]
    frames=[santi,santo]
    gain = pd.concat(frames)
    income= (gain["Adj Close"].iloc[1] - gain["Adj Close"].iloc[0]) / gain["Adj Close"].iloc[0]
    sanper.append(income)

ibemc_optionsdate["GAIN"]=sanper






old=ibemc[(ibemc["Date"]>"2013-11-01") & (ibemc["Date"]<"2014-11-01")]
oldie=[]
for i in range(0,n):
    oldie.append(old["Adj Close"].std())




ibemc_optionsdate["1ySTD"]=oldie


old6=ibemc[(ibemc["Date"]>"2014-05-01") & (ibemc["Date"]<"2014-11-01")]

oldie6=[]
for i in range(0,n):
    oldie6.append(old6["Adj Close"].std())
ibemc_optionsdate["6mSTD"]=oldie6

old3=ibemc[(ibemc["Date"]>"2014-08-01") & (ibemc["Date"]<"2014-11-01")]

oldie3=[]
for i in range(0,n):
    oldie3.append(old3["Adj Close"].std())
ibemc_optionsdate["3mSTD"]=oldie3

# concatenate all tables and add new agg categories and variables

frames = [abbmc_optionsdate, abemc_optionsdate, acsmc_optionsdate, acxmc_optionsdate, amsmc_optionsdate, anamc_optionsdate, anamc_optionsdate, bbvamc_optionsdate, bkiamc_optionsdate, bktmc_optionsdate, bmemc_optionsdate, cabmc_optionsdate, ebrmc_optionsdate, elemc_optionsdate, enamc_optionsdate, fccmc_optionsdate, fermc_optionsdate, gammc_optionsdate, gasmc_optionsdate, grfmc_optionsdate, iagmc_optionsdate, ibemc_optionsdate, idrmc_optionsdate, itxmc_optionsdate, mapmc_optionsdate, mtsmc_optionsdate, ohlmc_optionsdate, popmc_optionsdate, reemc_optionsdate, repmc_optionsdate, sabmc_optionsdate, sanmc_optionsdate, svomc_optionsdate, tefmc_optionsdate, tremc_optionsdate, vismc_optionsdate]

result14 = pd.concat(frames)


final_clean=result14[["DATE", "CODE", "STRIKE", "STRIKE_DATE", "LIQ", "VOLATILITY", "DELTA", "VOLUME","GAIN", "money", "MAX", "STD","1ySTD","6mSTD","3mSTD"]]

new_final = final_clean.dropna()

company=new_final["CODE"]

comp=[]
for row in company:
    name=row[1:4]
    comp.append(name)

    
new_final["TARGET"]=new_final["STRIKE"]+ new_final["LIQ"]   

new_final["COMPANY"]=comp

new_final["PREMIUM"]=new_final["LIQ"]/ (new_final["STRIKE"])


put_final = new_final.dropna()

success=[]
n=put_final.shape[0]
for i in range(0,n) :
    if put_final["TARGET"].iloc[i]< put_final["MAX"].iloc[i]:
        success.append(1)
    else:
        success.append(0)
put_final["TRIGGER"]=success

net=[]
n=put_final.shape[0]
for i in range(0,n) :
    if put_final["TRIGGER"].iloc[i]==1:
        net.append(put_final["MAX"].iloc[i]-put_final["TARGET"].iloc[i])
    else:
        net.append((put_final["LIQ"].iloc[i])*(-1))
put_final["NET"]=net

put_final["ROI"]=put_final["NET"] / put_final["LIQ"] 





diff=put_final["STRIKE_DATE"]-put_final["DATE"]

days=diff.astype(int)/86400000000000
days=days.astype(int)
put_final["DAYS"]=days

put=put_final[["COMPANY","DATE", "CODE", "STRIKE", "STRIKE_DATE", "DAYS","LIQ", "VOLATILITY", "DELTA", "VOLUME", "TARGET", "MAX", "GAIN", "TRIGGER", "NET","ROI", "PREMIUM", "STD", "1ySTD","6mSTD","3mSTD"]]

deltas=[]
n=put.shape[0]
for i in range(0,n) :
    if put["DELTA"].iloc[i]<(0.2):
        deltas.append(1)
    elif (put["DELTA"].iloc[i]>=(0.2)) & (put["DELTA"].iloc[i]<(0.4)):
        deltas.append(2)
    elif (put["DELTA"].iloc[i]>=(0.4)) & (put["DELTA"].iloc[i]<(0.6)):
        deltas.append(3)
    elif (put["DELTA"].iloc[i]>=(0.6)) & (put["DELTA"].iloc[i]<(0.8)):
        deltas.append(4)
    else:
        deltas.append(5)


put["HIGH DELTA"]=deltas

vols=[]
n=put.shape[0]
for i in range(0,n) :
    if put["VOLATILITY"].iloc[i]<(20):
        vols.append(1)
    elif (put["VOLATILITY"].iloc[i]>=(20)) & (put["VOLATILITY"].iloc[i]<(25)):
        vols.append(2)
    elif (put["VOLATILITY"].iloc[i]>=(25)) & (put["VOLATILITY"].iloc[i]<(30)):
        vols.append(3)
    elif (put["VOLATILITY"].iloc[i]>=(30)) & (put["VOLATILITY"].iloc[i]<(35)):
        vols.append(4)
    else:
        vols.append(5)
put["HIGH VOL"]=vols

prem=[]
n=put.shape[0]
for i in range(0,n) :
    if put["PREMIUM"].iloc[i]<(0.01):
        prem.append(1)
    elif (put["PREMIUM"].iloc[i]>=(0.01)) & (put["PREMIUM"].iloc[i]<(0.02)):
        prem.append(2)
    elif (put["PREMIUM"].iloc[i]>=(0.02)) & (put["PREMIUM"].iloc[i]<(0.04)):
        prem.append(3)
    elif (put["PREMIUM"].iloc[i]>=(0.04)) & (put["PREMIUM"].iloc[i]<(0.07)):
        prem.append(4)
    else:
        prem.append(5)


put["HIGH PREM"]=prem

day=[]
n=put.shape[0]
for i in range(0,n) :
    if put["DAYS"].iloc[i]<(30):
        day.append(1)
    elif (put["DAYS"].iloc[i]>=(30)) & (put["DAYS"].iloc[i]<(60)):
        day.append(2)
    elif (put["DAYS"].iloc[i]>=(60)) & (put["DAYS"].iloc[i]<(90)):
        day.append(3)
    elif (put["DAYS"].iloc[i]>=(90)) & (put["DAYS"].iloc[i]<(120)):
        day.append(4)
    else:
        day.append(5)

put["DURATION"]=day

put_novdet=put[["COMPANY", "CODE","DATE", "STRIKE", "STRIKE_DATE", "DAYS", "LIQ", "VOLUME","DELTA", "VOLATILITY", "MAX","TARGET", "TRIGGER", "NET", "ROI", "PREMIUM", "GAIN","STD", "1ySTD","6mSTD", "3mSTD", "HIGH DELTA", "HIGH VOL", "HIGH PREM", "DURATION" ]]

# save version 
put_novdet.to_csv("/users/jorge/calloptgainstd.csv")
#load version
put=pd.read_csv("/users/jorge/calloptgainstd.csv")
put=put[['COMPANY', 'CODE', 'DATE', 'STRIKE', 'STRIKE_DATE',
       'DAYS', 'LIQ', 'VOLUME', 'DELTA', 'VOLATILITY', 'MAX', 'TARGET',
       'TRIGGER', 'NET', 'ROI', 'PREMIUM', 'GAIN', 'STD', '1ySTD', '6mSTD',
       '3mSTD', 'HIGH DELTA', 'HIGH VOL', 'HIGH PREM', 'DURATION']]
       
#create table by company
from pandas import Series
companies=Series(put["NET"].values, index=put["COMPANY"])
put_table=put.pivot_table(index="COMPANY", values="NET")

import numpy as np
put_net=put.pivot_table(index="COMPANY", values="NET", aggfunc=np.sum)

put_trigger=put.pivot_table(index="COMPANY", values="TRIGGER")

put_vol=put.pivot_table(index="COMPANY", values="VOLATILITY")
put_prem=put.pivot_table(index="COMPANY", values="PREMIUM")
put_std=put.pivot_table(index="COMPANY", values="STD")
put_1std=put.pivot_table(index="COMPANY", values="1ySTD")
put_6mstd=put.pivot_table(index="COMPANY", values="6mSTD")
put_3mstd=put.pivot_table(index="COMPANY", values="3mSTD")
put_gain=put.pivot_table(index="COMPANY", values="GAIN")


put_df=pd.DataFrame(put_table)

put_df["sumNET"]=put_net
put_df["TRIGGER"]=put_trigger

put_df["VOLATILITY"]=put_vol
put_df["PREMIUM"]=put_prem
put_df["STD"]=put_std
put_df["1ySTD"]=put_1std
put_df["6mSTD"]=put_6mstd
put_df["3mSTD"]=put_3mstd
put_df["GAIN"]=put_gain
put_count=put.pivot_table(index="COMPANY", values="NET", aggfunc=np.count_nonzero)
put_count=put_count.astype(int)

put_df["COUNT"]=put_count

#save company table
put_df=put_df.drop("GAIN", axis=1)
put_df=put_df.drop("STD", axis=1)
put_df.to_csv("ciascallnov14.csv")
put.to_csv("finalcallnov14.csv")

#identify sectors
banks=put[(put["COMPANY"]=="BBV") | (put["COMPANY"]=="SAN") |(put["COMPANY"]=="POP")|(put["COMPANY"]=="BKI")|(put["COMPANY"]=="SAB") |(put["COMPANY"]=="CAB")]
energy=put[(put["COMPANY"]=="ELE") | (put["COMPANY"]=="ENA") |(put["COMPANY"]=="GAS")|(put["COMPANY"]=="IBE")|(put["COMPANY"]=="REE")|(put["COMPANY"]=="REP")]
industry=put[(put["COMPANY"]=="ABE") | (put["COMPANY"]=="ACS") |(put["COMPANY"]=="ACX")|(put["COMPANY"]=="ANA")|(put["COMPANY"]=="FCC")|(put["COMPANY"]=="FER")|(put["COMPANY"]=="GAM")|(put["COMPANY"]=="MTS")|(put["COMPANY"]=="OHL")|(put["COMPANY"]=="SVO")|(put["COMPANY"]=="TRE")]
consumer=put[(put["COMPANY"]=="ABB") | (put["COMPANY"]=="EBR") |(put["COMPANY"]=="ITX")|(put["COMPANY"]=="VIS")]
services=put[(put["COMPANY"]=="BME") | (put["COMPANY"]=="IAG")|(put["COMPANY"]=="MAP")]
tech=put[(put["COMPANY"]=="AMS") | (put["COMPANY"]=="IDR") |(put["COMPANY"]=="TEF")]

#add sector id to general table
energia=energy["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("ENERGY")
energy["SECTOR"]=comp

energia=banks["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("BANKS")
banks["SECTOR"]=comp

energia=industry["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("INDUSTRY")
industry["SECTOR"]=comp

energia=services["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("SERVICES")
services["SECTOR"]=comp

energia=consumer["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("CONSUMER")
consumer["SECTOR"]=comp

energia=tech["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("TECH")
tech["SECTOR"]=comp

frames = [banks, energy, tech, consumer, industry, services]
industries = pd.concat(frames)
industries=industries[["DATE", "CODE", "COMPANY", "SECTOR", "STRIKE", "STRIKE_DATE","DAYS", "LIQ", "VOLATILITY", "DELTA", "PREMIUM" ,"VOLUME","GAIN","TARGET", "TRIGGER", "NET", "ROI", "MAX","HIGH DELTA", "HIGH PREM", "HIGH VOL", "DURATION", "STD","1ySTD","6mSTD","3mSTD"]]

#save main file to be used from now on

industries.to_csv("sectorcall1114.csv")
sectores=pd.read_csv("/users/jorge/sectorcall1114.csv")

#create sectors table

from pandas import Series
sectors=Series(industries["NET"].values, index=industries["SECTOR"])
put_table=industries.pivot_table(index="SECTOR", values="NET")

import numpy as np
put_net=industries.pivot_table(index="SECTOR", values="NET", aggfunc=np.sum)

put_trigger=industries.pivot_table(index="SECTOR", values="TRIGGER")

put_vol=industries.pivot_table(index="SECTOR", values="VOLATILITY")
put_prem=industries.pivot_table(index="SECTOR", values="PREMIUM")
put_std=industries.pivot_table(index="SECTOR", values="STD")
put_1std=industries.pivot_table(index="SECTOR", values="1ySTD")
put_6mstd=industries.pivot_table(index="SECTOR", values="6mSTD")
put_3mstd=industries.pivot_table(index="SECTOR", values="3mSTD")

put_roi=industries.pivot_table(index="SECTOR", values="ROI")
put_roiagg=industries.pivot_table(index="SECTOR", values="ROI", aggfunc=np.sum)
put_sector=pd.DataFrame(put_table)

put_sector["sumNET"]=put_net
put_sector["TRIGGER"]=put_trigger
put_sector["ROI"]=put_roi
put_sector["sumROI"]=put_roiagg
put_sector["VOLATILITY"]=put_vol
put_sector["PREMIUM"]=put_prem
put_sector["STD"]=put_std
put_sector["1ySTD"]=put_1std
put_sector["6mSTD"]=put_6mstd
put_sector["3mSTD"]=put_3mstd

put_count=industries.pivot_table(index="SECTOR", values="NET", aggfunc=np.count_nonzero)
put_count=put_count.astype(int)

put_sector["COUNT"]=put_count

#save sector table

put_sector.to_csv("aggsectorcall14.csv")

#create sector id column to cias table
put=put_df
banks=put[(put["COMPANY"]=="BBV") | (put["COMPANY"]=="SAN") |(put["COMPANY"]=="POP")|(put["COMPANY"]=="BKI")|(put["COMPANY"]=="SAB") |(put["COMPANY"]=="CAB")]
energy=put[(put["COMPANY"]=="ELE") | (put["COMPANY"]=="ENA") |(put["COMPANY"]=="GAS")|(put["COMPANY"]=="IBE")|(put["COMPANY"]=="REE")|(put["COMPANY"]=="REP")]
industry=put[(put["COMPANY"]=="ABE") | (put["COMPANY"]=="ACS") |(put["COMPANY"]=="ACX")|(put["COMPANY"]=="ANA")|(put["COMPANY"]=="FCC")|(put["COMPANY"]=="FER")|(put["COMPANY"]=="GAM")|(put["COMPANY"]=="MTS")|(put["COMPANY"]=="OHL")|(put["COMPANY"]=="SVO")|(put["COMPANY"]=="TRE")]
consumer=put[(put["COMPANY"]=="ABB") | (put["COMPANY"]=="EBR") |(put["COMPANY"]=="ITX")|(put["COMPANY"]=="VIS")]
services=put[(put["COMPANY"]=="BME") | (put["COMPANY"]=="IAG")|(put["COMPANY"]=="MAP")]
tech=put[(put["COMPANY"]=="AMS") | (put["COMPANY"]=="IDR") |(put["COMPANY"]=="TEF")]
energia=energy["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("ENERGY")
energy["SECTOR"]=comp

energia=banks["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("BANKS")
banks["SECTOR"]=comp

energia=industry["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("INDUSTRY")
industry["SECTOR"]=comp

energia=services["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("SERVICES")
services["SECTOR"]=comp

energia=consumer["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("CONSUMER")
consumer["SECTOR"]=comp

energia=tech["COMPANY"]
comp=[]
for row in energia:
    
    comp.append("TECH")
tech["SECTOR"]=comp

frames = [banks, energy, tech, consumer, industry, services]
industries = pd.concat(frames)

sectors=industries[['COMPANY','SECTOR', 'NET', 'sumNET', 'TRIGGER', 'VOLATILITY', 'PREMIUM', '1ySTD',
       '6mSTD', '3mSTD', 'COUNT']]
#save cias table with sector id
sectors.to_csv("ciassectors.csv")
sect=pd.read_csv("/users/jorge/ciassectors.csv")

#add roi column to cias table

industries=pd.read_csv("/users/jorge/sectorcall1114.csv")
from pandas import Series
import numpy as np
put_roi=industries.pivot_table(index="COMPANY", values="ROI")

sectors=sectors.sort_values("COMPANY", ascending=True)

put_roi=pd.DataFrame(put_roi)
put_roi.to_csv('temporary.csv')
put_roi=pd.read_csv("/users/jorge/temporary.csv")
sectors["ROI"]=put_roi["ROI"]

#save final cias table
sectors.to_csv("finalcias.csv")
companias=pd.read_csv("/users/jorge/finalcias.csv")
companias=companias[['COMPANY', 'SECTOR','COUNT', 'NET','TRIGGER','ROI',
       'VOLATILITY', 'PREMIUM', '1ySTD' ]]



#load general table 
import pandas as pd
totals=pd.read_csv("/users/jorge/sectorcall1114.csv")

#clean premium quoted at 0

put=totals
put=put[put["LIQ"]!=0]
put.shape[0]

# sectors to numerical 

col = pd.Categorical.from_array(put["SECTOR"])
col.codes
put["SECTOR_CODE"]=col.codes

#efficiency measures

n=put.shape[0]
maxo=[]


for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.9):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety=put["MAX90"].mean() 

maxo=[] 
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.91):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety1=put["MAX90"].mean()

maxo=[]
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.92):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety2=put["MAX90"].mean()


maxo=[]
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.93):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety3=put["MAX90"].mean()

maxo=[]

for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.94):
        maxo.append(1)
    else:
        maxo.append(0)
put["MAX90"]=maxo
ninety4=put["MAX90"].mean() 
maxo=[]
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.95):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety5=put["MAX90"].mean()

maxo=[]
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.96):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety6=put["MAX90"].mean()

maxo=[]

for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.97):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
ninety7=put["MAX90"].mean()

maxo=[]
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.98):
        maxo.append(1)
    else:
        maxo.append(0)
      

put["MAX90"]=maxo
ninety8=put["MAX90"].mean()

maxo=[]
for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i])*(0.99):
        maxo.append(1)
    else:
        maxo.append(0)
put["MAX90"]=maxo
ninety9=put["MAX90"].mean()     

maxo=[]

for i in range(0,n):
    if put["TARGET"].iloc[i]< (put["MAX"].iloc[i]):
        maxo.append(1)
    else:
        maxo.append(0)
      
put["MAX90"]=maxo
hundred=put["MAX90"].mean()

#concatenate table of efficiency
frames=[ninety,ninety1,ninety2,ninety3, ninety4,ninety5,ninety6,ninety7,ninety8,ninety9, hundred]

# descriptive measures

print("number of options:",put.shape[0])
print(put["TRIGGER"].mean())
print(put["NET"].mean())
print(put["NET"].sum())
print(put["ROI"].mean())
print(put["ROI"].sum())

#filter black swans

winners=put[put["TRIGGER"]==1]
winners["ROI"].quantile([0.2,0.4,0.6,0.8])

blackswans=put[put["ROI"]>2.65]
not_blackswans=winners[winners["ROI"]<=2.65]


blackswans["ROI"].sum()

blackswans["NET"].sum()

not_blackswans["NET"].sum()
not_blackswans["ROI"].sum()

#relative frequencies of cias and sectors
print(put["COMPANY"].value_counts())
print(put["COMPANY"].value_counts(normalize=True))
print(blackswans["COMPANY"].value_counts(normalize=True))
print(not_blackswans["COMPANY"].value_counts(normalize=True))    

print(put["SECTOR"].value_counts())
print(put["SECTOR"].value_counts(normalize=True))
print(blackswans["SECTOR"].value_counts(normalize=True))
print(not_blackswans["SECTOR"].value_counts(normalize=True))

#correlations
import numpy as np
correlations= put.corr()


correlations=correlations[["NET","ROI", "TRIGGER","STD", "PREMIUM"]]

corrblack= blackswans.corr()


corrblack=corrblack[["NET","ROI", "STD","PREMIUM"]]

corrnotblack= not_blackswans.corr()


corrnotblack=corrnotblack[["NET","ROI", "STD","PREMIUM"]]


# GRAPHS

import matplotlib.pyplot as plt
import seaborn as sns

#scatterplots
plt.style.use("fivethirtyeight")
plt.scatter(put["GAIN"], put["ROI"])
plt.axis([-0.5,0.5,-1.3,20])
plt.xlabel("GAIN")
plt.ylabel("ROI")

plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(put["1ySTD"], put["PREMIUM"])

plt.xlabel("VOLATILITY")
plt.ylabel("PREMIUM")

plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(put["DAYS"], put["NET"])

plt.xlabel("DAYS")
plt.ylabel("NET")

plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(winners["VOLATILITY"], winners["ROI"])
plt.axis([10,50,-0.1,20])
plt.xlabel("VOLATILITY")
plt.ylabel("ROI")

plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(winners["PREMIUM"], winners["ROI"])
plt.axis([-0.01,0.2,-2.4,18])
plt.xlabel("PREMIUM")
plt.ylabel("ROI")

plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(put["DELTA"], put["PREMIUM"])

plt.xlabel("DELTA")
plt.ylabel("PREMIUM")

plt.axis([-0.1,1.1,-0.1,0.6])
plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(winners["GAIN"],winners["ROI"])

plt.xlabel("GAIN")
plt.ylabel("ROI")

plt.axis([-0.5,1, -0.1,20])
plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(winners["DAYS"],winners["ROI"])

plt.xlabel("DAYS")
plt.ylabel("ROI")
plt.axis([0,700,-0.1,20])

plt.show()

# histograms

plt.style.use("fivethirtyeight")
plt.hist(put["NET"],bins=40)
plt.axis([-2, 6, 0, 600])
plt.xlabel("NET")
plt.ylabel("COUNT")
plt.axvline(x=0)
plt.show()

plt.style.use("fivethirtyeight")
plt.hist(winners["ROI"],bins=40)
plt.axis([-1, 10, 0, 250])
plt.xlabel("ROI")
plt.ylabel("COUNT")
plt.axvline(x=0)
plt.show()

#boxplots

sns.set_style("ticks")
sns.boxplot(x=put["TRIGGER"], y= put["DELTA"], linewidth=1)
sns.plt.show()

sns.boxplot(x=put["TRIGGER"], y= put["3mSTD"],linewidth=1)
sns.plt.show()

sns.boxplot(x=put["TRIGGER"], y= put["VOLATILITY"],linewidth=1)
sns.plt.show()
sns.boxplot(x=put["TRIGGER"], y= put["DAYS"],linewidth=1)
sns.boxplot(x=put["TRIGGER"], y= put["STD"],linewidth=1)
sns.boxplot(x=put["TRIGGER"], y= put["1ySTD"],linewidth=1)
sns.boxplot(x=put["TRIGGER"], y= put["6mSTD"],linewidth=1)
sns.boxplot(x=put["TRIGGER"], y= put["3mSTD"],linewidth=1)
sns.boxplot(x=put["TRIGGER"], y= put["PREMIUM"],linewidth=1)
plt.ylim(0, 0.3)
sns.plt.show()
sns.boxplot(x=put["TRIGGER"], y= put["GAIN"],linewidth=1)
sns.boxplot(x=put["HIGH DELTA"], y= put["NET"],linewidth=1)
sns.boxplot(x=put["HIGH DELTA"], y= put["ROI"],linewidth=1)
sns.boxplot(x=put["HIGH VOL"], y= put["NET"],linewidth=1)
sns.boxplot(x=put["HIGH VOL"], y= put["ROI"],linewidth=1)
sns.boxplot(x=put["HIGH PREM"], y= put["NET"],linewidth=1)
sns.boxplot(x=put["HIGH PREM"], y= put["ROI"],linewidth=1)
sns.boxplot(x=put["DURATION"], y= put["NET"],linewidth=1)
sns.boxplot(x=put["DURATION"], y= put["ROI"],linewidth=1)
sns.boxplot(x=put["SECTOR_CODE"], y= put["NET"],linewidth=1)
sns.boxplot(x=put["SECTOR_CODE"], y= put["ROI"],linewidth=1)

#FORECAST MODELS

#load table
put_novdet=put
put_novdet.dropna()
put_novdet=put_novdet[['COMPANY', 'SECTOR', 'CODE', 'DATE', 'STRIKE', 'STRIKE_DATE',
       'DAYS', 'LIQ', 'VOLUME', 'DELTA', 'VOLATILITY', 'MAX', 'TARGET',
       'TRIGGER', 'NET', 'ROI', 'PREMIUM', 'GAIN', 'STD', '1ySTD', '6mSTD',
       '3mSTD', 'HIGH DELTA', 'HIGH VOL', 'HIGH PREM', 'DURATION', 'SECTOR_CODE']]
#normalize variables
put["DELTAnorm"]=(put["DELTA"]-put["DELTA"].mean()) /put["DELTA"].mean()
put["DAYSnorm"]=(put["DAYS"]-put["DAYS"].mean()) /put["DAYS"].mean()
put["VOLATnorm"]=(put["VOLATILITY"]-put["VOLATILITY"].mean()) /put["VOLATILITY"].mean()
put["PREMIUMnorm"]=(put["PREMIUM"]-put["PREMIUM"].mean()) /put["PREMIUM"].mean()
put["1ySTDnorm"]=(put["1ySTD"]-put["1ySTD"].mean()) /put["1ySTD"].mean()

#logistic regression

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

cols = put_novdet.columns
train_cols = cols.drop(["COMPANY", "CODE", "SECTOR", "DATE", "STRIKE", "STRIKE_DATE","TARGET", "LIQ","VOLUME", "TRIGGER","GAIN", "HIGH DELTA", "HIGH VOL", "HIGH VOL", "DURATION", "HIGH PREM", "STD","MAX", "NET", "ROI" ])
features = put_novdet[train_cols]
target = put_novdet["TRIGGER"]
lr.fit(features, target)
predictions = lr.predict(features)
put_novdet["PREDICT"]=predictions



# False positives.
fp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 0)]
tn= len(tn_filter)

# Rates


sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / put_novdet.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#logistic with cross val and kfold

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict, KFold
lr = LogisticRegression()
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)
put_novdet["PREDICT"]=predictions

# False positives.
fp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 0)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / put_novdet.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#balanced logistic with cross val

lr = LogisticRegression(class_weight="balanced")
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)
put_novdet["PREDICT"]=predictions

# False positives.
fp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 0)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / put_novdet.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#cross val with penalty 
penalty = {
    0: 4,
    1: 1
}

lr = LogisticRegression(class_weight=penalty)
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)
put_novdet["PREDICT"]=predictions

# False positives.
fp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 0)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / put_novdet.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#random forest

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict
rf = RandomForestClassifier(class_weight="balanced", random_state=1)
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(rf, features, target, cv=kf)
predictions = pd.Series(predictions)
put_novdet["PREDICT"]=predictions

# False positives.
fp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(put_novdet["PREDICT"] == 1) & (put_novdet["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(put_novdet["PREDICT"] == 0) & (put_novdet["TRIGGER"] == 0)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / put_novdet.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#TRAINING THE DATA

import math
import random
from numpy.random import permutation
random_indices=permutation(put_novdet.index)
test_cutoff=math.floor(len(put_novdet)/3)
test=put_novdet.loc[random_indices[1:test_cutoff]]
train=put_novdet.loc[random_indices[test_cutoff:]]

#train and test with only volatility
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(train[["VOLATILITY"]], train["TRIGGER"])
labels=model.predict(test[["VOLATILITY"]])
test["predicted_TRIGGER"]=labels
matches=test["predicted_TRIGGER"]==test["TRIGGER"]
correct_predictions=test[matches]
accuracy=len(correct_predictions)/len(test)
true_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 1)
true_positives = len(test[true_positive_filter])
false_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 1)
false_negatives = len(test[false_negative_filter])
true_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 0)
true_negatives = len(test[true_negative_filter])
false_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 0)
false_positives = len(test[false_positive_filter])
sensitivity = true_positives / (true_positives + false_negatives)
specificity= true_negatives / (false_positives + true_negatives) 

accuracy=(true_positives + true_negatives) / test.shape[0]


fpr = false_positives / (false_positives + true_negatives)
ppv=true_positives/ (true_positives + false_positives)
npv= true_negatives/ (true_negatives + false_negatives)

print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#train and test with delta

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(train[["DELTA"]], train["TRIGGER"])
labels=model.predict(test[["DELTA"]])
test["predicted_TRIGGER"]=labels
matches=test["predicted_TRIGGER"]==test["TRIGGER"]
correct_predictions=test[matches]
accuracy=len(correct_predictions)/len(test)
true_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 1)
true_positives = len(test[true_positive_filter])
false_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 1)
false_negatives = len(test[false_negative_filter])
true_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 0)
true_negatives = len(test[true_negative_filter])
false_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 0)
false_positives = len(test[false_positive_filter])
sensitivity = true_positives / (true_positives + false_negatives)
specificity= true_negatives / (false_positives + true_negatives) 

accuracy=(true_positives + true_negatives) / test.shape[0]


fpr = false_positives / (false_positives + true_negatives)
ppv=true_positives/ (true_positives + false_positives)
npv= true_negatives/ (true_negatives + false_negatives)

print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#train and test with premium

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(train[["PREMIUM"]], train["TRIGGER"])
labels=model.predict(test[["PREMIUM"]])
test["predicted_TRIGGER"]=labels
matches=test["predicted_TRIGGER"]==test["TRIGGER"]
correct_predictions=test[matches]
accuracy=len(correct_predictions)/len(test)
true_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 1)
true_positives = len(test[true_positive_filter])
false_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 1)
false_negatives = len(test[false_negative_filter])
true_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 0)
true_negatives = len(test[true_negative_filter])
false_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 0)
false_positives = len(test[false_positive_filter])
sensitivity = true_positives / (true_positives + false_negatives)
specificity= true_negatives / (false_positives + true_negatives) 

accuracy=(true_positives + true_negatives) / test.shape[0]


fpr = false_positives / (false_positives + true_negatives)
ppv=true_positives/ (true_positives + false_positives)


print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)

#roc auc_score
from sklearn.metrics import roc_auc_score
probabilities = model.predict_proba(test[["VOLATILITY"]])


auc_score = roc_auc_score(test["TRIGGER"], probabilities[:,1])
print(auc_score)
probabilities = model.predict_proba(test[["DELTA"]])


auc_score = roc_auc_score(test["TRIGGER"], probabilities[:,1])
print(auc_score)

#logistic reg train and test with delta and volatility
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(train[["DELTA", "VOLATILITY"]], train["TRIGGER"])
labels=model.predict(test[["DELTA", "VOLATILITY"]])
test["predicted_TRIGGER"]=labels
matches=test["predicted_TRIGGER"]==test["TRIGGER"]
correct_predictions=test[matches]
accuracy=len(correct_predictions)/len(test)
true_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 1)
true_positives = len(test[true_positive_filter])
false_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 1)
false_negatives = len(test[false_negative_filter])
true_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 0)
true_negatives = len(test[true_negative_filter])
false_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 0)
false_positives = len(test[false_positive_filter])
sensitivity = true_positives / (true_positives + false_negatives)
specificity= true_negatives / (false_positives + true_negatives) 

accuracy=(true_positives + true_negatives) / test.shape[0]


fpr = false_positives / (false_positives + true_negatives)
ppv=true_positives/ (true_positives + false_positives)
npv= true_negatives/ (true_negatives + false_negatives)

print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print(npv)

#logistic reg train and test with delta, premium and volatility
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(train[["DELTA", "VOLATILITY", "PREMIUM"]], train["TRIGGER"])
labels=model.predict(test[["DELTA", "VOLATILITY", "PREMIUM"]])
test["predicted_TRIGGER"]=labels
matches=test["predicted_TRIGGER"]==test["TRIGGER"]
correct_predictions=test[matches]
accuracy=len(correct_predictions)/len(test)
true_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 1)
true_positives = len(test[true_positive_filter])
false_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 1)
false_negatives = len(test[false_negative_filter])
true_negative_filter = (test["predicted_TRIGGER"] == 0) & (test["TRIGGER"] == 0)
true_negatives = len(test[true_negative_filter])
false_positive_filter = (test["predicted_TRIGGER"] == 1) & (test["TRIGGER"] == 0)
false_positives = len(test[false_positive_filter])
sensitivity = true_positives / (true_positives + false_negatives)
specificity= true_negatives / (false_positives + true_negatives) 
accuracy=(true_positives + true_negatives) / test.shape[0]


fpr = false_positives / (false_positives + true_negatives)
ppv=true_positives/ (true_positives + false_positives)
npv= true_negatives/ (true_negatives + false_negatives)

print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print(npv)



#linear regression (not useful)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
admissions = put

col = admissions.columns
train_cols = col.drop(["COMPANY", "SECTOR","CODE", "DATE", "STRIKE", "LIQ","VOLUME", "TRIGGER", "STRIKE_DATE", "GAIN", "STD","MAX", "ROI"])
admissions = admissions[train_cols]
def train_and_test(cols):
    # Split into features & target.
    features = admissions[cols]
    target = admissions["NET"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(admissions["NET"], predictions)
    variance = np.var(predictions)
    return(mse, variance)
    
del_mse, del_var = train_and_test(["DELTA"])

vol_mse, vol_var = train_and_test(["VOLATILITY"])
pre_mse, pre_var = train_and_test(["PREMIUM"])
day_mse, day_var = train_and_test(["DAYS"])
yst_mse, yst_var = train_and_test(["1ySTD"])
print(del_mse, del_var)
print(vol_mse, vol_var)
print(pre_mse,pre_var)
print(day_mse, day_var)
print(yst_mse, yst_var)

#ENTROPY

import numpy

def calc_entropy(column):
    
    counts = numpy.bincount(column)
    
    probabilities = counts / len(column)
    
    
    entropy = 0
   
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# calculate information gain
def calc_information_gain(data, split_name, target_name):
   
    original_entropy = calc_entropy(data[target_name])
    
    
    column = data[split_name]
    median = column.median()
    
    
    left_split = data[column <= median]
    right_split = data[column > median]
    
    
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    
    return original_entropy - to_subtract


print(calc_information_gain(put, "VOLATILITY", "TRIGGER"))
print(calc_information_gain(put, "DELTA", "TRIGGER"))
print(calc_information_gain(put, "PREMIUM", "TRIGGER"))
print(calc_information_gain(put, "NET", "HIGH VOL"))
print(calc_information_gain(put, "NET", "HIGH DELTA"))
print(calc_information_gain(put, "NET", "HIGH PREM"))
print(calc_information_gain(put, "NET", "DURATION"))
print(calc_information_gain(put, "NET", "SECTOR_CODE"))
print(calc_information_gain(put, "ROI", "HIGH VOL"))
print(calc_information_gain(put, "ROI", "HIGH DELTA"))
print(calc_information_gain(put, "ROI", "HIGH PREM"))
print(calc_information_gain(put, "ROI", "DURATION"))
print(calc_information_gain(put, "ROI", "SECTOR_CODE"))
print(calc_information_gain(put, "DAYS", "TRIGGER"))
print(calc_information_gain(put, "VOLUME", "TRIGGER"))
print(calc_information_gain(put, "1ySTD", "TRIGGER"))
print(calc_information_gain(put, "GAIN", "TRIGGER"))
print(calc_information_gain(put, "STD", "TRIGGER"))
print(calc_information_gain(put, "3mSTD", "TRIGGER"))
print(calc_information_gain(put, "6mSTD", "TRIGGER"))
print(calc_information_gain(put, "SECTOR_CODE", "TRIGGER"))


#my own algorithm
#create new net categories

prem=[]


n=put.shape[0]
for i in range(0,n) :
    if put["NET"].iloc[i]<=(0):
        prem.append(1)
    elif (put["NET"].iloc[i]>(0)) & (put["NET"].iloc[i]<(0.6)):
        prem.append(2)
    elif (put["NET"].iloc[i]>=(0.6)):
        prem.append(3)
put["NETcat"]=prem

#check the information gain
print(calc_information_gain(put, "VOLATILITY", "NETcat"))
print(calc_information_gain(put, "DELTA", "NETcat"))
print(calc_information_gain(put, "PREMIUM", "NETcat"))
print(calc_information_gain(put, "DAYS", "NETcat"))
print(calc_information_gain(put, "VOLUME", "NETcat"))
print(calc_information_gain(put, "1ySTD", "NETcat"))
print(calc_information_gain(put, "GAIN", "NETcat"))
print(calc_information_gain(put, "STD", "NETcat"))
print(calc_information_gain(put, "3mSTD", "NETcat"))
print(calc_information_gain(put, "6mSTD", "NETcat"))

#create new roi cat for succesful options(not to be used)
prem=[]


n=winners.shape[0]
for i in range(0,n) :
    if winners["ROI"].iloc[i]<(0.5):
        prem.append(1)
    elif (winners["ROI"].iloc[i]>=(0.5)) & (winners["ROI"].iloc[i]<(2)):
        prem.append(2)
    elif (winners["ROI"].iloc[i]>=(2)) :
        prem.append(3)
   


winners["ROIcat"]=prem
print(calc_information_gain(winners, "VOLATILITY", "ROIcat"))
print(calc_information_gain(winners, "DELTA", "ROIcat"))
print(calc_information_gain(winners, "PREMIUM", "ROIcat"))
print(calc_information_gain(winners, "DAYS", "ROIcat"))
print(calc_information_gain(winners, "VOLUME", "ROIcat"))
print(calc_information_gain(winners, "1ySTD", "ROIcat"))
print(calc_information_gain(winners, "GAIN", "ROIcat"))
print(calc_information_gain(winners, "STD", "ROIcat"))
print(calc_information_gain(winners, "3mSTD", "ROIcat"))
print(calc_information_gain(winners, "6mSTD", "ROIcat"))

#filter variables for logarithm
puto=put[["CODE", "COMPANY", "SECTOR_CODE", "DAYS", "DELTA", "VOLATILITY", "PREMIUM", "1ySTD","DURATION", "HIGH PREM","HIGH DELTA", "HIGH VOL", "TRIGGER", "NET", "ROI", "NETcat"]]
#normalize variables
puto["DELTAnorm"]=(puto["DELTA"]-puto["DELTA"].mean()) /puto["DELTA"].mean()
puto["DAYSnorm"]=(puto["DAYS"]-puto["DAYS"].mean()) /puto["DAYS"].mean()
puto["VOLATnorm"]=(puto["VOLATILITY"]-puto["VOLATILITY"].mean()) /puto["VOLATILITY"].mean()
puto["PREMIUMnorm"]=(puto["PREMIUM"]-puto["PREMIUM"].mean()) /puto["PREMIUM"].mean()
puto["1ySTDnorm"]=(puto["1ySTD"]-puto["1ySTD"].mean()) /puto["1ySTD"].mean()
#create roi cat
prem=[]


n=puto.shape[0]
for i in range(0,n) :
    if puto["ROI"].iloc[i]<(0):
        prem.append(1)
    elif (puto["ROI"].iloc[i]>=(0)) & (puto["ROI"].iloc[i]<(1)):
        prem.append(2)
    elif (puto["ROI"].iloc[i]>=(1)) :
        prem.append(3)
   


puto["ROIcat"]=prem

#create new variable for medium deltas
n=puto.shape[0]
pros=[]
for i in range(0,n):
    if (puto["HIGH DELTA"].iloc[i]==2) | puto["HIGH DELTA"].iloc[i]==3 :
        pros.append(1)
    elif (puto["HIGH DELTA"].iloc[i]==1) | puto["HIGH DELTA"].iloc[i]==5:
        pros.append(-1)
    else:
        pros.append(0)
puto["DELTA_roi"]=pros

#other new variable for medium deltas
n=puto.shape[0]
pros=[]
for i in range(0,n):
    if (puto["HIGH DELTA"].iloc[i]==3) :
        pros.append(1)
   
    else:
        pros.append(0)
puto["DELTA_net"]=pros

#variable for medium volatility
n=puto.shape[0]
pros=[]
for i in range(0,n):
    if (puto["HIGH VOL"].iloc[i]==2) :
        pros.append(1)
   
    else:
        pros.append(0)
puto["VOL_net"]=pros

#variable for medium premium
n=puto.shape[0]
pros=[]
for i in range(0,n):
    if (puto["HIGH PREM"].iloc[i]==4) | puto["HIGH PREM"].iloc[i]==5 :
        pros.append(-1)
    elif  (puto["HIGH PREM"].iloc[i]==2) | puto["HIGH PREM"].iloc[i]==3:
        pros.append(1)
    else:
        pros.append(0)

puto["PREM_roi"]=pros
    

#algorithm to maximize net
money=(puto["DELTAnorm"]*2)+ (puto["DELTA_net"]*2) + (puto["VOL_net"]*2)+ (puto["PREMIUMnorm"]*3) + (puto["DAYSnorm"]*3) + (puto["1ySTDnorm"]*2) + (puto["VOLATnorm"]*(1))

#estimate quantiles (this used as a reference)
money.quantile([0.8])
prene=[]
for i in money:
    if i<=(5.911):
        prene.append(0)
    
    else:
        prene.append(1)
puto["PRENET"]=prene
#money strategy results

fp_filter = put_novdet[(puto["PRENET"] == 1) & (puto["NETcat"] != 3)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(puto["PRENET"] == 1) & (puto["NETcat"] == 3)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(puto["PRENET"] ==0 ) & (puto["NETcat"] == 3)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(puto["PRENET"]== 0) & (puto["NETcat"] != 3)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / puto.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#safe strategy (aim for trigger) algorithm
safe=(puto["DELTAnorm"]*5) + (puto["PREMIUMnorm"]*3) + (puto["DAYSnorm"]*2) + (puto["1ySTDnorm"]*0) + (puto["VOLATnorm"]*(-2))
safe.quantile([0.7])
prene=[]
for i in safe:
    if i<=(1.58):
        prene.append(0)
   
    else:
        prene.append(1)
puto["PRETRIGGER"]=prene
fp_filter = put_novdet[(puto["PRETRIGGER"] == 1) & (puto["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(puto["PRETRIGGER"] == 1) & (puto["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(puto["PRETRIGGER"] == 0) & (puto["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(puto["PRETRIGGER"]== 0) & (puto["TRIGGER"] == 0)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / puto.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#algorithm for roi strategy (failed)
preroi=(puto["DELTAnorm"]*(2)) + (puto["DELTA_roi"]*3)+(puto["PREM_roi"]*1)+(puto["PREMIUMnorm"]*(-4)) + (puto["DAYSnorm"]*(-1)) + (puto["1ySTDnorm"]*(-1)) + (puto["VOLATnorm"]*(-2))
preroi.quantile([0.4,0.8])
prene=[]
for i in preroi:
    if i<=(6.7):
        prene.append(0)
    
    else:
        prene.append(1)
puto["PREROI"]=prene
fp_filter = puto[(puto["PREROI"] == 1) & (puto["ROIcat"] != 3)]
fp = len(fp_filter)

# True positives.
tp_filter = puto[(puto["PREROI"] == 1) & (puto["ROIcat"] == 3)]
tp = len(tp_filter)

# False negatives.
fn_filter = puto[(puto["PREROI"] == 0) & (puto["ROIcat"] == 3)]
fn= len(fn_filter)
# True negatives
tn_filter = puto[(puto["PREROI"]== 0) & (puto["ROIcat"] != 3)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / puto.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#create random predictions as benchmark
import numpy as np
testo=pd.DataFrame(np.random.randint(1,100,size=(1517)))
testo[0].quantile([0.7])
proba=testo[0]
preni=[]
for i in proba:
    if i<=(69):
        preni.append(0)
    
    else:
        preni.append(1)
puto["TESTtri"]=preni
fp_filter = put_novdet[(puto["TESTtri"] == 1) & (puto["TRIGGER"] == 0)]
fp = len(fp_filter)

# True positives.
tp_filter = put_novdet[(puto["TESTtri"] == 1) & (puto["TRIGGER"] == 1)]
tp = len(tp_filter)

# False negatives.
fn_filter = put_novdet[(puto["TESTtri"] == 0) & (puto["TRIGGER"] == 1)]
fn= len(fn_filter)
# True negatives
tn_filter = put_novdet[(puto["TESTtri"]== 0) & (puto["TRIGGER"] ==0)]
tn= len(tn_filter)

sensitivity = tp / (tp + fn)
fpr = fp / (fp + tn)
ppv=tp/ (tp + fp)
npv= tn/ (tn + fn)
specificity= tn /(fp + tn)
accuracy=(tp + tn) / puto.shape[0]
print(sensitivity)
print(fpr)
print( specificity)
print(accuracy)
print( ppv)
print( npv)

#compare all final results for each strategy
putes=puto[puto["PRENET"]==1]
print(putes["TRIGGER"].mean())
print(putes["NET"].mean())
print(putes["ROI"].mean())
putes=puto[puto["PREROI"]==1]
print(putes["TRIGGER"].mean())
print(putes["NET"].mean())
print(putes["ROI"].mean())
putes=puto[puto["PRETRIGGER"]==1]
print(putes["TRIGGER"].mean())
print(putes["NET"].mean())
print(putes["ROI"].mean())
putes=puto[puto["TESTtri"]==1]
print(putes["TRIGGER"].mean())
print(putes["NET"].mean())
print(putes["ROI"].mean())

