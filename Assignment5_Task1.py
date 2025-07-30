s_dict={'Rahul':85,'Samit':91,'Subrata':69,'Bhagirath':87,'Prosenjit':96}
s_name=input("Enter Student name to see their marks : ")
if(s_name in s_dict):
    print(f"Student Name : {s_name} \nMarks : {s_dict[s_name]}")
else:
    print(f"The name {s_name} is not in the student list")