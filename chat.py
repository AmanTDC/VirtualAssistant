import csv
rows=[]
columns=[]
length=0
data=" "
f_name="brain/knowledge/knowledge.csv"
with open(f_name,'r') as knowledge:
    csvreader=csv.reader(knowledge)
    coloumns=next(csvreader)
    for row in csvreader:
        rows.append(row)
    length=csvreader.line_num

def chat(question,to_exec=0,exec_command=""):
    
    answer=""
    question=question.lower()
    for i in range(length-1):
        a=rows[i][1].split(", ")
        for j in a:
            #print("checking: "+rows[i][0] +" in "+ question +" or "+ j +" in "+ question)
            if rows[i][0] in question or j in question:
                answer=rows[i][2]
                to_exec=rows[i][5]
                try:
                    data=rows[i][6]
                except:
                    print('data error')
                print(to_exec)
                exec_command=rows[i][3]
                break
            if(len(answer)>0):
                break
        if(len(answer)>0):
                break
    if(len(answer)==0):
        answer="I can't understand you, can you be more specific"
        data=""
    print([answer,to_exec,exec_command,data])
    
    return [answer,to_exec,exec_command,data]
#while(1):
#    chat(input("I:"))
        
