# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style = "darkgrid", color_codes=True)

# titanic = sns.load_dataset("titanic")
# sns.catplot(x="sex",y="survived",hue="class",kind="bar",data=titanic)
# plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "darkgrid", color_codes=True)
Pangora = sns.load_dataset("titanic")

p= sns.countplot(x="sex", data=Pangora, hue="class")
p.set_title("Zayn da DATA")

plt.show()

# print(Pangora)