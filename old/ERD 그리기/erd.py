import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 불러오기
data = pd.read_csv('c:/erd.csv')

# 데이터 확인하기
print(data.head())

# 바 차트 그리기
fig, ax = plt.subplots()
bar_width = 0.35

# LSL, USL 범위 표시
ax.bar(data.index, data['USL'] - data['LSL'], bar_width, data['LSL'], color='r', alpha=0.5, label='Range')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_title('Range Bar Chart')
ax.legend()

# Value 좌표로 그리기
ax.scatter(data.index, data['Value'], color='b', label='Value')

# X 축 레이블 설정
ax.set_xticks(data.index)
ax.set_xticklabels(data['NAME'])

plt.tight_layout()
plt.show()
