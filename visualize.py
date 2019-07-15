import pandas as pd, matplotlib.pyplot as plt, seaborn as sb
import os, glob

def visualize():
	df = pd.read_csv(os.path.join(os.getcwd(), "Extracted\\Pivoted_Data.txt"), index_col=[0,1], skiprows=3, header=None)
	df.columns = ["Temp Min", "Temp Mean", "Temp Max", "DewTemp Min","DewTemp Mean","DewTemp Max","WindSpeed Min","WindSpeed Mean","WindSpeed Max"]
	df.index.names = ["Station Name","Year"]
	# print(df.head())

	fig, axes = plt.subplots()
	axes.tick_params(labelsize=5)
	sb.heatmap(df, ax=axes)
	fig.savefig(os.path.join(os.getcwd(), "Extracted\\Heatmap.png"),dpi=300)

	return


if __name__ == '__main__':
	print('Start')

	visualize()

	print('Finish')