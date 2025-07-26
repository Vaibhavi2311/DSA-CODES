book_borrowed={
    "MEM1":['c programming','cpp','python','java'],
    "MEM2":['java','python'],
    "MEM3":['c programming','java'],
    "MEM4":[],
    "MEM5":['java','python'],
    "MEM6":['cpp']
    

}
total_members=len(book_borrowed)
print("members",total_members)
total_values=sum(len(books) for books in book_borrowed.values())
print("total books",total_values)
average_values=total_values/total_members
print("average is",average_values)
all_values=[]
for books in book_borrowed.values():
 all_values.extend(books)
print(all_values)
count={}
for books in all_values:
  if books in count:
    count[books]+=1
  else:
    count[books]=1
print(count)
most_borrowed=""
max_count=0
for books in count:
  if count[books]>max_count:
   most_borrowed=books
   max_count=count[books]
   print(most_borrowed)
   print(max_count)
least_borrowed=min(count,key=count.get)
least_count=count[least_borrowed]
print(least_borrowed)
print(least_count)