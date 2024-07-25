
#  sinking-land-simulator  

[Access Online Deployed App](https://sinking-land-simulator-bv9otrkkljgsnnllioxbph.streamlit.app/)


#### "Simulate how a land sinks"

There is an island of size H×W, surrounded by the sea.

The island is divided into H rows and W columns of 1×1 sections, and the elevation of the section at the i-th row from the top and the j-th column from the left (relative to the current sea level) is Ai,j​.

Starting from now, the sea level rises by 1 each year.

Here, a section that is vertically or horizontally adjacent to the sea or a section sunk into the sea and has an elevation not greater than the sea level will sink into the sea.

Here, when a section newly sinks into the sea, any vertically or horizontally adjacent section with an elevation not greater than the sea level will also sink into the sea simultaneously, and this process repeats for the newly sunk sections.

For each i=1,2,…,Y, find the area of the island that remains above sea level i years from now.

# Libraries

1.Python 

2.Image Sequence Clip

3.Streamlit for deployment

4.And other basic python library for image creation, file reading and numpy.

# Requirements.txt

The requirements.txt has been given in the repository.which are required for deployment during the deploy phase.

# Demo  



![App Screenshot](https://github.com/RinkeshKumarSinha/sinking-land-simulator/blob/main/snaps/simulate.gif?raw=true)


## Run Locally

Clone the project

```bash
  git clone https://github.com/RinkeshKumarSinha/sinking-land-simulator.git
```

Go to the project directory

```bash
  cd sinking-land-simulator
```

Install dependencies

```bash
  pip install streamlit
```

Start the server

```bash
  streamlit run main.py
```


## Deployment

Deployment can be done on streamlit io and necessary dependencies have been written in requirements.txt so no need to include anything extra.

