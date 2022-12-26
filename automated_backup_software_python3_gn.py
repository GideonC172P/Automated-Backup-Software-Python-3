# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:53:09 2022

@author: Gideon Nebelsick

"""

"""

src_dir=source directory
tgt_dir= target directory
"""

def getListOfFiles(dirName):
    import os
    #note not own work, geeks for geeks is the source 
    from os import walk
    g=0
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def Placeholder(dirName0): 
    #the purpose of this function is to make a placeholder file
    #in case the source directory is empty
    #on the fact of it this is completly pointless 
    #it is more of an insurance policy to avoid unessesary erros in testing
    g=0
    a2=getListOfFiles(dirName0)
    try:
      a3=a2[0]
      #this looks into the list and says
      #hey does the list acutally contain anything
      
      #if not result is an idex error which then leads to the placeholder
      #creation below (yay :)
    except IndexError:
          print("creating placeholder file")
          print(dirName0+'/placeholder.txt')
          import numpy as np
          n1=[1,2,3]
          n2=np.array(n1)
          np.savetxt(dirName0+'/placeholder.txt', n2, delimiter=',') 
          #del(b2)


          
def ComdirGet(dirName1):
    com_dir="C:/com_dir"
    Placeholder(dirName1)
    g=0
    # create a list of file and sub directories 
    # names in the given directory 
    #the r0 is to replace the backslashes from the 
      
    #this down there does (and it strikes me that I could do that )
    #converts file paths from "crazy/backslash" windows
    #to civilized i.e. forward slash thereby being actually usable 

    #let us experiment with the idea of making the function and then shitting it
    #through for loops 
    #future me here that acutally works and is pretty awesome
    #it also fakes the directories so it replaces both 
    #src and tgt dir with a fake yet unfiorm directory
    #to allow comparision of the files 
    a2=getListOfFiles(dirName1)
    
    Placeholder(dirName1)
    
    a3=a2[0]
    r0="\\\\"

    string = a3 
    r1=r0[0]
    r2=str('/')
    listName1=list()
    a2a0=list()
    for g in a2:
        a4a=g.replace(r1,r2)
        a2a0.append(a4a)
        a4=a4a.replace(dirName1, com_dir)
        listName1.append(a4)
    return listName1



def tgtpathfill(tgt_pf_path):
    #this function tgtpathfill
    #is to recreate the file tree for any given file in the source directory
    #said recreation obvioiusly has to and has to take palce in the target directory
    
    
    g=0
    import os
    wordlist=list()
    b2t=tgt_pf_path.split("/")
    
    r1=range(0,len(b2t)-1)
    
        
    
    word1=str()
    for g in r1:
        #print(b2t[g])
            
        if g==len(b2t)-1:
            word1=word1+str(b2t[g])
        else:
            word1=word1+str(b2t[g]+"/")
        wordlist.append(word1)
        for g3 in wordlist:
            os.makedirs(g3, exist_ok=True) 





 

def moving1(src,tgt):
    # this function is quite possiblly in-elegant 
    #or just plain bad on the count of doing to much at once
    #any way
    #This fucntion does everything 
    # it compares just o a list file basis if the stuff is 
    #is in the both the src and tgt directory or not 
    #if it isnt or is (which makes it a big backwards)
    #it is appended to a list
    #then it asks well does file from source exisit in tgt
    #if yes it  compares the time if src time>tgt time the file is moved
    #tgt pathfill is not nessesary since it is already there 
    #if it isnt in tgt_dir with tgt pathfill the dirs in the middle
    #are backfilled
    #then the doozie follows and hte file is simply moved 
    com_dir="C:/com_dir"
    g=0
    m1a=ComdirGet(src)
    m1b=ComdirGet(tgt)
    listm1=list()
    for g in m1a:
        g1=g
        if g1 in m1a and m1b:
            listm1.append(g1)
        else:
            listm1.append(g1)
        del(g1)
    movelist=list()
    g=0
    rangem1=range(0, len(listm1))
    
    for g in rangem1:
        t1=listm1[g]
        t1a=t1.replace(com_dir,src)
        t1b=t1.replace(com_dir,tgt)
        t_src=t1a
        t_tgt=t1b
        
        r2=(0, len(listm1))
        import shutil
        import pathlib
        import os.path
        isp1=os.path.exists(t_tgt)
        if isp1==True:
            #hi

            t_src
            t_tgt
            mt1=pathlib.Path(t_src).stat().st_mtime
            mt2=pathlib.Path(t_tgt).stat().st_mtime
            if mt1>mt2:
                os.remove(t_tgt)
                shutil.copy(t_src, t_tgt) 
        else:
            tgtpathfill(t_tgt)
            shutil.copy(t_src, t_tgt)
                



#code below merely imports os and shutil the packages needed
import shutil
import os
#this print a empty line to hopefully at any rate make the interfact more
#appealing
print(" ")
#these variables below
# set the default values for the Source and target directories 
src_dir = 'D:/everything'
day_dir = 'X:/Daily_Backup'
week_dir = 'X:/Weekly_Backup'
month_dir = 'X:/Monthly_Backup'


#this is the first line of the interface 
#interface code goes from Line 209 to Line 329
#The idea is it shows you the default directory
#and asks is this ok
#if yes (y) then it moves on to the next directory (after asking for conformation)
#if no (n or anything else than y) than the program for allows 
#for a new directory to be input
#should a mistake be made, there is a conformation followed by a 2nd Attempt
#after which the Programm moves on to the next directory
print('Default Source Directory '+str(src_dir)+' is that ok (y/n) ')
i1 = input()

if i1=="y":
    src_dir = src_dir
else:
    print("Input new source directory")
    src_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(src_dir)
    print(" ")

print('Changed Source Directory to')
print(src_dir)
print('is that ok (y/n)')
i2 = input()
print("  ")
if i2=="y":
    src_dir = src_dir
else:
    print("Input new source directory")
    src_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(src_dir)
    print(" ")


print('Default Target Daily Directory '+str(day_dir)+' is that ok (y/n) ')
i1a = input()

if i1a=="y":
    day_dir = day_dir
else:
    print("Input new Daily directory")
    day_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(day_dir)
    print(" ")

print('Changed Daily Directory to')
print(day_dir)
print('is that ok (y/n)')
i2a = input()
print("  ")
if i2a=="y":
    day_dir = day_dir
else:
    print("Input new Daily directory")
    day_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(day_dir)
    print(" ")

print('Default Target Weekly Directory '+str(week_dir)+' is that ok (y/n) ')
i1b = input()

if i1b=="y":
    week_dir = week_dir
else:
    print("Input new Weekly directory")
    day_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(week_dir)
    print(" ")

print('Changed Weekly Directory to')
print(week_dir)
print('is that ok (y/n)')
i2b = input()
print("  ")
if i2b=="y":
    week_dir = week_dir
else:
    print("Input new Weekly directory")
    week_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(week_dir)
    print(" ")


print('Default Target Monthly Directory '+str(month_dir)+' is that ok (y/n) ')
i1c = input()

if i1c=="y":
    month_dir = month_dir
else:
    print("Input new Monthly directory")
    day_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(month_dir)
    print(" ")

print('Changed Monthly Directory to')
print(month_dir)
print('is that ok (y/n)')
i2c = input()
print("  ")
if i2c=="y":
    month_dir = month_dir
else:
    print("Input new Monthly directory")
    month_dir=str(input())
    print(" ")    
    print("Change Sucessfule to:")
    print(month_dir)
    print(" ")



"""
convention i.e. switch position
4=False
7=TRUE

"""
#this gets the current date
from datetime import date

today = date.today()
print("Today's date:", today)
t2=str(today)
s1=t2.split("-")

#this and the split above it, does things, mainly it has a list,
#with the dates of the month at which a weekly backup takes place
dates=[1,7,14,21,28]
#this makes the split date in to a integer 
s2=int(s1[2])

#this at least for q1 is the question will a weekly backup take place
#this is what the if question below is for
#the q1 variable is the "switch" that if it is in position 4 (see convention above)
#means No weekly backup today
#position 7 means Yes Today we are doing a weekly backup
#q2 is the switch that says will there be a monthly backup
#Simple boolean True and False value
q1=4
q2=s2==1

if s2==dates[0]:
    q1=7
elif s2==dates[1]:
    q1=7
elif s2==dates[2]:
    q1=7
elif s2==dates[3]:
    q1=7
elif s2==dates[4]:
    q1=7
else:
    pass



 
#All of this does the Daily backup, the dirs_exist_ok=True means
#all exsisiting files will be overwritten
#thereby even if there is a change in a file whose name is left the same
#it will be backed up
files = os.listdir(src_dir)
print(" ")
print("Daily Backup starting") 
print("Daily Backup working....") 
moving1(src_dir, day_dir)
print(" ")
print("Daily Backup done")
# this does the weekly backup only when the q1 is in the 7 position
if q1==7:
    print(" ")
    print("Weekly Backup starting") 
    print("Weekly Backup working....") 
    moving1(src_dir, week_dir)
    print(" ")
    print("Weekly Backup done")
else:
    print("No Weekly Backup today happens on the:")
    print("1st, 7th, 14th, 21st and 28th")
    print("of the month")
    print(" ")
    pass

#this does the montly backup when q2=TRUE i.e. on the first of the Month

if q2==True:
    print(" ")
    print("Monthly Backup starting")
    print("Monthly Backup working....")
    moving1(src_dir, month_dir)
    print(" ")
    print("Monthly Backup done")
else:
    print("No Monthly Backup only on the 1st of the month")
    pass


print("  ")
print("All done, See you next time :)")
