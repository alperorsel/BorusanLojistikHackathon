import sys
from heapq import heapify, heappush 
from idealrota import idealrota

def dijkstra(grafik,src,dest):
    inf=sys.maxsize
    dugum_veri={'A':{'girdi':inf,'pred':[]},
    'AD1':{'girdi':inf,'pred':[]},
    'B':{'girdi':inf,'pred':[]},
    'C':{'girdi':inf,'pred':[]},
    'D':{'girdi':inf,'pred':[]},
    'AB1':{'girdi':inf,'pred':[]},
    'AB2':{'girdi':inf,'pred':[]},
    'AC2':{'girdi':inf,'pred':[]},
    'AC3':{'girdi':inf,'pred':[]},
    'BC1':{'girdi':inf,'pred':[]},
    'BC2':{'girdi':inf,'pred':[]},
    'DC1':{'girdi':inf,'pred':[]},
    'DC2':{'girdi':inf,'pred':[]}
    }
    dugum_veri[src]['girdi']=0
    visited=[]
    temp=src
    for j in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap=[]
            for j in grafik[temp]:
                if j not in visited:
                    girdi=dugum_veri[temp]['girdi']+ grafik[temp][j]
                    if girdi< dugum_veri[j]['girdi']:
                        dugum_veri[j]['girdi']=girdi
                        dugum_veri[j]['pred']=dugum_veri[temp]['pred']+list(temp)
                    heappush(min_heap,(dugum_veri[j]['girdi'],j))
        heapify(min_heap)
        temp=min_heap[0][1]
    dijkstra.a=dugum_veri[dest]['girdi']
    dijkstra.b=dugum_veri[dest]['pred']
    dijkstra.list=list(dest)
        
source=input('Başlangıç Şehri')
destination=input('Bitiş Şehri')
comparison=[0,0,0,0,0,0]


idealrota(1)
dijkstra(idealrota.grafik,source,destination)
comparison[0]=dijkstra.a
first=comparison[0]
idealrota(2)
dijkstra(idealrota.grafik,source,destination)
comparison[1]=dijkstra.a
second=comparison[1]
idealrota(3)
dijkstra(idealrota.grafik,source,destination)
comparison[2]=dijkstra.a
third=comparison[2]
idealrota(4)
dijkstra(idealrota.grafik,source,destination)
comparison[3]=dijkstra.a
fourth=comparison[3]
idealrota(5)
dijkstra(idealrota.grafik,source,destination)
comparison[4]=dijkstra.a
fifth=comparison[4]
idealrota(6)
dijkstra(idealrota.grafik,source,destination)
comparison[5]=dijkstra.a
sixth=comparison[5]
comparison.sort()
if(comparison[0]==first):
    print("6.00-9.00 SAATLERİ ARASINDA")
    idealrota(1)
    dijkstra(idealrota.grafik,source,destination)
    print(dijkstra.b)
    print(dijkstra.list)
elif(comparison[0]==second):
    print("9.00-12.00 SAATLERİ ARASINDA")
    idealrota(2)
    dijkstra(idealrota.grafik,source,destination)
    print(dijkstra.b)
    print(dijkstra.list)
elif(comparison[0]==third):
    print("12.00-15.00 SAATLERİ ARASINDA")
    idealrota(3)
    dijkstra(idealrota.grafik,source,destination)
    print(dijkstra.b)
    print(dijkstra.list)
elif(comparison[0]==fourth):
    print("15.00-18.00 SAATLERİ ARASINDA")
    idealrota(4)
    dijkstra(idealrota.grafik,source,destination)
    print(dijkstra.b)
    print(dijkstra.list)
elif(comparison[0]==fifth):
    print("18.00-21.00 SAATLERİ ARASINDA")
    idealrota(5)
    dijkstra(idealrota.grafik,source,destination)
    print(dijkstra.b)
    print(dijkstra.list)
elif(comparison[0]==sixth):
    print("21.00-24.00 SAATLERİ ARASINDA")
    idealrota(6)
    dijkstra(idealrota.grafik,source,destination)
    print(dijkstra.b+dijkstra.grafike)
