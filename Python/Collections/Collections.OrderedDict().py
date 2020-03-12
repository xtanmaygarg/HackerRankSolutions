from collections import OrderedDict

Items = OrderedDict()
N = int(input())
for i in range(N):
    In = input().split()
    Item = " ".join(In[: -1])
    Price = int(In[-1])
    if Item in Items:
        Items[Item] += Price
    else:
        Items[Item] = Price
for Item in Items:
    print(Item, Items[Item])
