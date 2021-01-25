"""
coding: utf-8
Created on Tue Jan 19 2021 18:56:44 
@author: gorisof
"""

#%% HOUSEKEEPING

import os
import squarify
import folderstats
import openpyxl
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#%% SETUP

# Set your personal folder file
path_zone   = "C:\user\..."

# Set the folder where you want to store the zone analysis results
path_output = "C:\user\..."

#%% FUNCTION FOR TREE FOLDER VISUALIZATION

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

# DO NOT RUN (RECOMMENDED).
# It might take a very long time if you have many files in your folder.
# x = list_files(path_zone)
            
#%% CREATE THE TREE FOLDER WITH FILES AND FOLDERS

path_list = []

for root, d_names, f_names in os.walk(path_zone):
    for f in f_names:
        path_list.append(os.path.join(root,f))
        
#%% CREATE THE TREE FOLDER WITH FOLDERS ONLY

path_folder_list = []

for root, d_names, f_names in os.walk(path_zone):
    for d in d_names:
        path_folder_list.append(os.path.join(root))
        
path_folders = list(set(path_folder_list))

#%% EXPORT THE TWO TREE FOLDERS IN EXCEL/CSV FILES

os.chdir(path_output)
        
pd.DataFrame(path_list).to_csv('Zone_tree_folder_files.csv', header=True, index=False)
pd.DataFrame(path_folders).to_excel('Zone_tree_folder.xlsx', header=True, index=False)

#%% STATISTICS ON YOUR FOLDER

df = folderstats.folderstats(path_zone, ignore_hidden=True)

#%% PLOTS ON FOLDER STATISTICS

# Plot 1: number of files by extension
with plt.style.context('ggplot'):
    df['extension'].value_counts().plot(
        kind='bar', color='C1', title='Numbers of files by extension')
    
    plt.savefig('Zone_number_files.png', bbox_inches='tight');

#______________________________________________________________________________

# Plot 2: size of files by extension   
with plt.style.context('ggplot'):
    # Group by extension and sum all sizes for each extension 
    extension_sizes = df.groupby('extension')['size'].sum()
    # Sort elements by size
    extension_sizes = extension_sizes.sort_values(ascending=False)
    
    extension_sizes.plot(
        kind='bar', color='C1', title='Size of files by extension')
    
    plt.savefig('Zone_size_files.png', bbox_inches='tight');
#______________________________________________________________________________

# Plot 3: number of files by extension - square 
extension_counts = df['extension'].value_counts()

squarify.plot(sizes=extension_counts.values, label=extension_counts.index.values)
plt.title('Extension Treemap by Size')
plt.axis('off')

plt.savefig('Zone_number_files_square.png', bbox_inches='tight');
#______________________________________________________________________________

# PLot 4: size of folders
with plt.style.context('ggplot'):
    # Filter the data set to only folders
    df_folders = df[df['folder']]
    # Set the name to be the index (so we can use it as a label later)
    df_folders.set_index('name', inplace=True)
    # Sort the folders by size
    df_folders = df_folders.sort_values(by='size', ascending=False)
    
    # Show the size of the largest 50 folders as a bar plot
    df_folders['size'][:50].plot(kind='bar', color='C0', title='Folder Sizes')
    
    plt.savefig('Zone_size_folders.png', bbox_inches='tight');


#%% Plot 5: hierarchical charts - you need to manually install graphviz

# Sort the index
df_sorted = df.sort_values(by='id')

G = nx.Graph()
for i, row in df_sorted.iterrows():
    if row.parent:
        G.add_edge(row.id, row.parent)
    
# Print some additional information
print(nx.info(G))

# pip install graphviz
# pip install pydot
# from networkx.drawing.nx_pydot import graphviz_layout

# pos_dot = graphviz_layout(G, prog='dot')

# fig = plt.figure(figsize=(16, 8))
# nodes = nx.draw_networkx_nodes(G, node_size=2, node_color='C0')
# edges = nx.draw_networkx_edges(G, edge_color='C0', width=0.5)
# plt.axis('off');
