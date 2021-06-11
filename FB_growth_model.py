from sympy import *
import matplotlib.pyplot as plt
import math
import networkx as nx
import random
import numpy as np
from sklearn.linear_model import LinearRegression

FB_user_dict = {'2010Q1': 431,'2010Q2': 482,'2010Q3': 550,'2010Q4': 608,'2011Q1': 680,'2011Q2': 680,'2011Q3': 739, '2011Q4': 800, \
    '2012Q1': 901,'2012Q2': 955,'2012Q3': 1007,'2012Q4': 1056,'2013Q1': 1110,'2013Q2': 1155,'2013Q3': 1189, '2013Q4': 1228,\
    '2014Q1': 1276,'2014Q2': 1317,'2014Q3': 1350,'2014Q4': 1393,'2015Q1': 1441,'2015Q2': 1490,'2015Q3': 1545,'2015Q4': 1591, \
    '2016Q1': 1654,'2016Q2': 1712,'2016Q3': 1788,'2016Q4': 1860,'2017Q1': 1936,'2017Q2': 2006,'2017Q3': 2072,'2017Q4': 2129, \
    '2018Q1': 2196,'2018Q2': 2234,'2018Q3': 2271,'2018Q4': 2320,'2019Q1': 2375,'2019Q2': 2414,'2019Q3': 2449,'2019Q4': 2498, \
    '2020Q1': 2603,'2020Q2': 2701,'2020Q3': 2740,'2020Q4': 2797}

users_list = list(FB_user_dict.values())

for i in range(2):
    N0 = users_list[i]
    new_nodes = users_list[i+1]-users_list[i]
    p=0.6
    G=nx.gnp_random_graph(N0, p)
    num_edges = G.number_of_edges()

    for eti in range(new_nodes):
        print("ITERATION: " + str(eti))
        m=3
        new_eti="_"+str(eti)
        target_nodes=[]
        while m!=0:
            part_sum=0.0
            rn=random.random()
            for n in G.nodes():
                base=part_sum
                step=part_sum+G.degree(n)/(G.number_of_edges()*2.0)
                part_sum=part_sum+G.degree(n)/(G.number_of_edges()*2.0)
                if rn>=base and rn<step:
                    if n in target_nodes:
                        break
                    target_nodes.append(n)
                    m=m-1
                    break
        for n_tar in target_nodes:
            G.add_edge(new_eti,n_tar)

# graphs from 2nd iteration
for i in range(2,3):
    N0 = users_list[i]
    new_nodes = users_list[i+1]-users_list[i]
    p=0.6
    G=nx.Graph(G)
    num_edges = G.number_of_edges()

    for eti in range(new_nodes):
        print("ITERATION: " + str(eti))
        m=3
        new_eti="_"+str(eti)
        target_nodes=[]
        while m!=0:
            part_sum=0.0
            rn=random.random()
            for n in G.nodes():
                base=part_sum
                step=part_sum+G.degree(n)/(G.number_of_edges()*2.0)
                part_sum=part_sum+G.degree(n)/(G.number_of_edges()*2.0)
                if rn>=base and rn<step:
                    if n in target_nodes:
                        break
                    target_nodes.append(n)
                    m=m-1
                    break
        for n_tar in target_nodes:
            G.add_edge(new_eti,n_tar)


degree = [val for (node, val) in nx.degree(G)]
degree_sequence=sorted(degree,reverse=True)
print(degree_sequence)


# # Model to predict the increment of nodes coming into the system
# FB_new_dict = {}
# for i in range(len(users_list)):
#     FB_new_dict[i+1] = users_list[i]
#
# X = np.array(list(FB_new_dict.keys())).reshape(-1,1)
# Y = np.array(list(FB_new_dict.values()))
#
# # #fit the points in the model
# modelH1 = LinearRegression().fit(X, Y)
#
# print(modelH1.intercept_) #
# print(modelH1.coef_) # slope -m

