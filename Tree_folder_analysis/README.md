# Tree folder analysis

The script makes recursive analyses on a specific folder. 


## Getting Started

The function `list_files(startpath)` allows you to visualise the folder tree. 

You can export the tree with all folders and files (`path_list`), or just with folders (`path_folder_list`).

The package `folderstats` computes statistics on the folder to be analysed. 
`folderstats`'s statistics can be coupled with nice data visualization.

### Prerequisites

The Python script requires a few packages installation.

With regards to folder statistics, please write in the Anaconda Prompt:
```python
conda activate your_env
pip install filelock
pip install folderstats
```

With regards to data visualization, please write in the Anaconda Prompt:
```python
pip install squarify
pip install networkx
pip install graphviz
conda install python-graphviz
pip install pydot
```

You will also need to manually install `graphviz` locally.
I leave this article for further information regarding the `graphviz` installation: https://graphviz.gitlab.io/doc/winbuild.html


## Deployment

The file has been further extended to identify old files in a folder, based on the date creation and last time of access. 
Based on words contained in the files, the files have been catalogued as confidential files or not.
These modifications to the code have not been included in the file.

## Built With

  - Spyder


## Authors

  - [Sofia Gori](https://github.com/SofiaGori)

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - Thanks to Jana Kiev for the wonderful article about [`folderstats`](https://janakiev.com/blog/python-filesystem-analysis/)
  
