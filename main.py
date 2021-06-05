import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# 导入np、plt

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
# 中文设置

FULL_SCORES = [150, 150, 150, 100, 100, 100]
CLASS_NUMBER = 58
GRADE_NUMBER = 300
# 常量


scores = [113,135,125,62,68,49]
class_rankings = [8, 10, 10, 50, 25, 25]
grade_rankings = [80, 20, 50, 200, 50, 100]
"""
scores = FULL_SCORES
class_rankings = [1,1,1,1,1,1]
grade_rankings = [1,1,1,1,1,1]
# 六边形战士的梦想
"""
k = 2 # 班级系数
# 获取数据(数据顺序均为：语数英物化生)

mark = []
for i in range(0,6):
    mark.append( 100 * ((scores[i]/FULL_SCORES[i])**(1/4)) * (1-(class_rankings[i]/CLASS_NUMBER)**(1/k)) * (1-(grade_rankings[i]/GRADE_NUMBER)**(k)) )
# 计算

plt.style.use('ggplot')
# 启用主题

labels = np.array(['语文','数学','英语','物理','化学','生物'])
nAttr = 6
mark = np.array(mark)
#
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
#
mark = np.concatenate((mark ,[mark [0]]))
angles = np.concatenate((angles,[angles[0]]))
labels = np.concatenate((labels,[labels[0]]))
#
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, mark, '-',color='m', linewidth=2)
plt.fill(angles, mark, facecolor='m', alpha=0.2)
plt.thetagrids(angles*180/np.pi, labels)


plt.figtext(0.38, 0.95, '余绍缘成绩(转化后)分析图')

plt.grid(True)
plt.savefig('acculate.JPG')
plt.show()