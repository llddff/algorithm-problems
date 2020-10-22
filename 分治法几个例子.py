class Arrange:         # 全排列问题
    def main(self,args):
        self.fullSort(args,0,len(args)-1)
    def fullSort(self,arr,start,end):
        if start == end:
            print(arr)
        for i in range(start,end+1):
            arr[i],arr[start]=arr[start],arr[i]
            self.fullSort(arr,start+1,end)
            arr[i],arr[start]=arr[start],arr[i]

# a=Arrange()
# a.main([1,2,3,4,5])


class hanoTower:     # 汉诺塔
    def hanoi(self,n,source,temp,target):
        if n == 1:
            self.move(n,source,target)
        else:
            self.hanoi(n-1,source,target,temp)
            self.move(n,source,target)
            self.hanoi(n-1,temp,source,target)
    def move(self,n,source,target):
        print(f'{n}'+'号盘子移动：'+source+'->'+target)

a=hanoTower()
a.hanoi(4,'A','B','C')