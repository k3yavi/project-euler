from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# fig = plt.gcf()
# fig.set_size_inches(20, 11)

font0 = FontProperties()
font = font0.copy()
font.set_family('sans-serif')
font.set_name('Helvetica')
font.set_weight('bold')

font1 = font0.copy()
font1.set_family('sans-serif')
font1.set_name('Helvetica')
# hfont = {'fontname':'Helvetica'}

a=[17.27,15.88,13.68,14.34,14.16,16.65,20.61,14.17,16.23,17.77,17.72,18.02,18.34,14.14,16.22,20.46,14.68,12.62,13.53,12.25]
sns.set_style('white')
sns.set_context('poster')
plt.plot(range(1, 21), np.sort(np.array(a))[::-1],  'b^', label='Individual sample time', )
plt.plot(range(1, 21), np.sort(np.array(a))[::-1] )
plt.plot([1], [4.25], 'ro', label='time to learn prior')

sns.despine()
plt.ylim([0, 50])
plt.xlim([0, 21])
plt.ylabel('Time (seconds)', fontsize=45, fontproperties=font1)
plt.xlabel('Sample Id', fontsize=45, fontproperties=font1)
plt.xticks(fontsize=35, fontproperties=font1)
plt.yticks(fontsize=35, fontproperties=font1)
plt.legend(loc='upper right', fontsize=25)
sns.despine()
plt.tight_layout()
# plt.savefig("timing.pdf")
plt.show()
# ###################################
#
# nopriorA=[0.739618129755, 0.742662427614, 0.743988916088, 0.739114961732, 0.737171342788, 0.743270815566, 0.737072701716, 0.737752670863]
# adaptA=[0.823498873931, 0.825427764655, 0.826203296197, 0.823116807919, 0.822794513227, 0.826109179251, 0.822135268821, 0.822217148894]
# # estA=[0.767029865951, 0.76974524823, 0.771039904812, 0.766818857008, 0.764899816997, 0.770491104009, 0.764896056941, 0.765086920029]
#
# nopriorB=[0.742920644252, 0.73810050717, 0.743324495726, 0.7376387085, 0.738492243428, 0.743160508206, 0.744067441266, 0.741875364738]
# adaptB=[0.825180078755, 0.823030969897, 0.825520471767, 0.822325816092, 0.82262851408, 0.825406487565, 0.826186284414, 0.8239865205]
# # estB=[0.770085708375, 0.765805047635, 0.770795207343, 0.765209058631, 0.76609142915, 0.770314185298, 0.771111721126, 0.768771054923]
#
# np=[0.739410232929,0.742476291877,0.743805183309,0.738907591716,0.736974013408,0.743073143836,0.736862244909,0.737552401873,0.742920644252,0.73810050717,0.743324495726,0.7376387085,0.738492243428,0.743160508206,0.744067441266,0.741875364738]
# adpt=[0.870995510085,0.872119714682,0.872075887868,0.870050761674,0.870072120307,0.87258517025,0.869465191361,0.869597258491,0.871306763549,0.86961455133,0.87221151435,0.869602457515,0.86911419582,0.87097740633,0.872526846918,0.871038534748]
# # np=nopriorA+nopriorB
# # adpt=adaptA+adaptB
# # est=estA+estB
#
# data=[np, adpt]#, est]
# sns.set_style('white')
#
# sns.set_context('poster')
#
# box = plt.boxplot(data, patch_artist=True)
# sns.despine()
# colors = ['lightblue', 'pink', 'lightgreen']
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
#
# plt.xticks([1,2], ['Flat Prior', 'Adaptive Prior'], fontsize=40, fontproperties=font)#, 'Adaptive-est Prior'])
# plt.ylabel('Spearman Correlation',  fontsize=40, fontproperties=font1)
# plt.xlabel('Method',  fontsize=40, fontproperties=font1)
# plt.yticks(fontsize=30, fontproperties=font)
# plt.tight_layout()
# plt.savefig("corr.pdf")

# from matplotlib.font_manager import FontProperties
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# font0 = FontProperties()
# font = font0.copy()
# font.set_family('sans-serif')
# font.set_name('Helvetica')
# font.set_weight('bold')
#
# font1 = font0.copy()
# font1.set_family('cursive')
#
# import pandas as pd
#
# np=[0.739410232929,0.742476291877,0.743805183309,0.738907591716,0.736974013408,0.743073143836,0.736862244909,0.737552401873,0.742920644252,0.73810050717,0.743324495726,0.7376387085,0.738492243428,0.743160508206,0.744067441266,0.741875364738]
# adpt=[0.870995510085,0.872119714682,0.872075887868,0.870050761674,0.870072120307,0.87258517025,0.869465191361,0.869597258491,0.871306763549,0.86961455133,0.87221151435,0.869602457515,0.86911419582,0.87097740633,0.872526846918,0.871038534748]
#
# dat  = []
# for x in np:
#     dat.append(("flat prior", x))
# for x in adpt:
#     dat.append(("adaptive prior", x))
#
# D = pd.DataFrame(dat, columns=['method', 'Spearman correlation'])
#
# data=[np, adpt]
#
# sns.set_context('poster')
# sns.set(style="ticks", font_scale=2,
#         rc={'font.family' : 'sans-serif',
#             'font.sans-serif' : ['Helvetica'],
#             'font.weight' : 'bold'})
# ax = sns.boxplot(x="method", y="Spearman correlation", data=D)
# sns.despine(offset=2, trim=False)
# plt.tight_layout()
# # plt.show()
# plt.savefig("corr.pdf")