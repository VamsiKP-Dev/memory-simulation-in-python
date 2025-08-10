# human Fundementals

#1. Data Structure -Dict
#2. Memory Acessing
#3. Memory Overwrite
#4. Methods and add more data
#5. Communication
#6. Conditions
#7. Transformation (storing the data in another way of copying)
#8. Loops
#9. Functions, class methods


#step1 : store

movietrailer = ("introduction-person","problem","emotions","fightscenes","Heroiene introduction")
movietrailer1={"story":"unpridictablescreenplay","category":"thriller","gudiovanrassum":"college student","emotions":"rejections","seetha":"job working girl","father":"dennis rechie"}


#step2: read or get
print(movietrailer[0])
print(movietrailer1["gudiovanrassum"])

#step3: overwrite

print(movietrailer1["category"])
movietrailer1["category"] = "fantasy & thriller"
print(movietrailer1["category"])


#step4: growing data is adding data to brain more

movietrailer1.update({"radha":"mother"})
print(movietrailer1)

#step5: Communication copy data from one human brain to another human brain

friend={}
friend.update(movietrailer1)
print("friend communications",friend)

#step6: Conditions

#unpridictablescreenplay
if movietrailer1["story"] == "slow & emotional":
    tickets=1000
    smilingface="avarage"

elif movietrailer1["story"] == "unpridictablescreenplay":
    smilingface="hit"
    print(smilingface,"movie hit")

else: #routine story
    donationhero=200
    fans="gudio van rassum"


room1="brother1"
room2 = "brother2"
if room1 == "brother1":
    bed=2
    bathroom="attached"
    facility="ac"
    print(bathroom,facility)

elif room2 == "brother2":
     bed=1



hotel="sunstar"
facility="normal sitting"
facility2="seated space with great ambious"

coustomer1="normal sitting"
coustomer2="seated space with great ambious"

if coustomer1 == "normal sitting":
    spacetoeat="tables"
    drinkingwater="filter water"
    selfservice = True
    paymorebill=250
    print("first condition")


if coustomer2 == "seated space with great ambious":
    waitertoserve=True
    placeorder=["2 Idly","1 Dosa"]
    placeorder.append("Ghee roast")
    tiptoservant=20
    paymorebill=500

    print(placeorder, paymorebill)
    print("second condition")


# Transformation
fatherearned=("house1","house2","land")

fatherfamily = 2
son1="venkat"
son2="krishna"

#data in truple got copied in to dict
fathersettlement ={"venkat":"house2","krishna":"house1","seetha":"land"}

print("transformation",fatherearned,fathersettlement)

count=0
for i in fatherearned:
    print(i)   #it will execute based on properties
    count=count+1
print("loop count", count)

for i in fathersettlement.keys():
    print("sons",i)


