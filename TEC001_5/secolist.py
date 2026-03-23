def oddremover(flist):
    slist = []
    for i in flist:
        if i % 2 == 0:
            slist.append(i)
        else:
            continue
    return print(slist)
flist = [1,2,3,4,5,6,7,8,9]
oddremover(flist)
print(flist)
