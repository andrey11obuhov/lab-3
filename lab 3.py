import json
f=[]
def addt():
    t1=input("Write a task ")
    t2=input("Write a category of the task ")
    t3 = input("Write a time for a task ")
    f.append(["task: ", t1, "category: ", t2, "time: ", t3])
    return print('')
def writer(filename):
    try:
        with open(filename, 'w') as f_obj:
            json.dump(f , f_obj)
    except Exception as e:
        print(e)
def com():
    q="Y"
    i=1
    while(q!='N'):
        q=input("Do you want to add task?(Y/N) ")
        q.upper()
        if q=="Y" or q=="y":
            f.append(i)
            addt()
            i+=1
    return print(f)
com()
if __name__=="__main__":
    writer('lab3.json')