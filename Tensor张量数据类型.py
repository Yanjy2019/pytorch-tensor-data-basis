import torch
a=torch.randn([1,2,3,4])
print(a)
print(a.dim())  #输出张量数据的层数，即长度
print(a.dim()==len(a.shape))
print(a.numel())  #输出张量数据的总个数，即数据大小，占内存的个数
print(a.shape)   #输出数据的形状
print(a.size())
print(a.size(3))   #输出size和shape的其中元素
print(a.shape[3])
x=torch.empty(2,2,3)
print(x)
print(torch.IntTensor(2,3))
print(torch.FloatTensor(1,2,3))
print(torch.Tensor(1,2,10))                        #未初始化tensor数据，占据一定的内存区间
print(x.type())                                    #输出tensor数据类型
#torch.set_default_tensor_type(torch.DoubleTensor)  #设置tensor的数据类型为doubletensor
x=torch.empty(2,2,3)
print(x)
print(x.type())                                    #重新输出tensor数据类型
#随机初始化的方式
a=torch.rand(3,3)            #产生0-1的shape为[3,3]的tensor数据
print(a)
b=torch.rand_like(a)           #产生一个和a的tensor数据类型相同的tensor数据，其数据大小也在0-1之间，如果变大可以利用一定的数据处理
print(b)
c=torch.randint(0,10,[3,5])
print(c)

a=torch.randn(2,5)  #产生一个标准正态分布的数据
print(a)
a=torch.normal(mean=torch.full([10],0),std=torch.arange(1,0,-0.1)) #产生一般自定义的正态分布数据大小
b=a.reshape(2,5)
print(a)
print(b)
#torch.full
a=torch.full([2,3],3)
print(a)
b=torch.full([],1) #生成一个标量
print(b)
c=torch.full([1],1)  #生成一个dim=1的tensor张量数据
print(c)
print(a.type(),b.type(),c.type())
a=torch.arange(0,10,2)  #半开区间，左闭右开,不包含右边的最大值
print(a)
b=torch.range(0,10) #包含右端数据10,全闭区间
print(b)

#linspace/logspace
#(1)torch.linspace(min,max,steps=data number)：返回的是等间距的数据，其中左右数据均包括，数据个数为steps，数据间隔为(max-min)/(steps-1)
#(2)torch.logspace(min,max,steps=data number):返回的是10的各个线性空间次方的数值
a=torch.linspace(0,10,steps=10)
print(a)
b=torch.linspace(0,10,steps=11)
print(b)
c=torch.logspace(0,10,steps=11)
print(c)
d=torch.logspace(-1,0,steps=10)
print(d)
#Ones/zeros/eyes
print(torch.zeros(3,4))     #零张量数据
print(torch.ones(3,4))      #1张量数据
print(torch.eye(4,5))       #单位张量数据
#randperm产生随机的索引值
a=torch.rand(2,3)
b=torch.rand(2,2)
print(a,b)
idx=torch.randperm(2)
print(idx)
a=a[idx]
b=b[idx]
print(a,b)
