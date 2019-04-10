def save_file(wo,ni,count):
    file_name_wo='wo_'+str(count)+'.txt'
    file_name_ni='ni_'+str(count)+'.txt'
        
    wo_file=open(file_name_wo,'w')
    ni_file=open(file_name_ni,'w')
        
    ni_file.writelines(ni)
    wo_file.writelines(wo)
        
    
    wo_file.close()
    ni_file.close()
def split_file(file_name):
    f=open('D://talk.txt')
    wo=[]
    ni=[]
    count=1
    for each_lines in f:
        if each_lines[:6]!='======':
            (role,lines_spoken)=each_lines.split(':',1)
            if role=='我':
               wo.append(lines_spoken)
            if role=='你':
               ni.append(lines_spoken)
        else:
            save_file(wo,ni,count)
            
            wo=[]
            ni=[]
            count+=1
    file_name_wo='wo_'+str(count)+'.txt'
    file_name_ni='ni_'+str(count)+'.txt'
            
    wo_file=open(file_name_wo,'w')
    ni_file=open(file_name_ni,'w')

    ni_file.writelines(ni)
    wo_file.writelines(wo)
            
    wo_file.close()
    ni_file.close()        
    f.close()
split_file('talk.txt')
        
