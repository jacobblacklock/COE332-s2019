import matplotlib.pyplot as plt
import geopandas


def plot_map(d):

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    world.plot(ax=ax, color='white', edgecolor='black')
    x = []
    y = []
    for data in d.data:
        y.append(data['lat'])
        x.append(data['lng'])

    plt.scatter(x, y)
    return plt