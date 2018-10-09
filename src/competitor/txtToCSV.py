import csv

seeker=0
def textfilter(File):
    i=0
    with open("./files/txt/"+File+".txt","r") as f:
        line=f.readlines()        
        for line in line:
            if(i==0 or i==1 or i==2):
                i+=1
                continue
            tuples=seperateStrings(line)
            toCSV(tuples[0],tuples[1],File)


def toCSV(title,path,File): 
    global seeker   
    mode="a"
    if(seeker==0):
        mode="w"    
    with open("./files/csv/"+File+".csv",mode) as csvfile:
        fieldnames=['Title','path']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        if(seeker==0):
            writer.writeheader()
            seeker+=1                
        writer.writerow({'Title':title,'path':path})

def seperateStrings(line): 
    lastIndex=0;title="";path=""  
    index=line.find("/")
    if(index!=-1):  
        for i in range(1,len(line)):
            if(line[-i]=='/'):
                lastIndex=-i+1
                break    
        path=line[index:lastIndex]
        title=line[:index-1]
    else:
        index=line.find("1")
        title=line[:index-1]        
    return title,path

if __name__=="__main__":       
    file_list=['titlekwr','sizekwr','sharekwr','globalkwr','forecastkwr']
    for File in file_list:
        seeker=0
        textfilter(File)
    
    

