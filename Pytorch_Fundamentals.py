import torch



device='cuda' if torch.cuda.is_available() else 'cpu'


a=torch.randn(3,2)
b=torch.randn(2,3)

print('a',a)
print('b',b)


c=a@b 
print('c',c)

d=a+torch.ones_like(a)
print(d)