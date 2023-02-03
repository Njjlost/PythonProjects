class Vector:
    def __init__(self,vec1):
        self.vec1=vec1

    def __str__(self):
        str1=""
        index=0      
        for i in self.vec1:
            str1 += f"{i}a{index}+"
            index +=1
        return str1[:-1]
        #-------> creation of vector tak!!!
    def __add__(self, vec2):
        new_list=[]
        for i in range (len(self.vec1)):
            new_list.append(self.vec1[i]+vec2.vec1[i])
        return Vector(new_list)

    def __mul__(self, vec2):
        sum=0
        for i in range (len(self.vec1)):
            sum+= self.vec1[i]*vec2.vec1[i]
        return sum
    def __len__(self,vec1):
        return (len(self.vec1))
v1=Vector([3,4,5])
v2=Vector([3,8,9])                         #Example
print(v1+v2)
print(v1*v2)
print(len(v1.vec1))                        #it prints the length of vector
