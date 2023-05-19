# %%
# p1.py
import csv

filename = 'cwurData_4years.csv'
#headr는 선택하는 헤더값
header = 'year'
# 2012를 선택해서 넣기
# 원래는 입력 받아야 함
filter_value = '2012'
A = []
B = []

# A 행렬에 years 로 필터링 된 데이터를 입력 
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row[header] == filter_value:
            A.append(row)

# 이제 A에는 필터링된 데이터 행이 포함됩니다.
# 예를 들어 인덱싱을 사용하여 A의 데이터에 액세스할 수 있습니다: A[0]을 사용하여 첫 번째 행을 가져옵니다.


# B 행렬에 A 행렬에서 연도별로 걸러진 데이터를 다시, 국가별로 거른다 
header = 'country'
filter_value = 'USA'
for row in A:
    if row[header] == filter_value:
        B.append(row)

sorted_data = sorted(B, key=lambda x:int( x['world_rank']))

for row in sorted_data:
    print(row['world_rank'], row['institution'], row['score'], sep=',')



# %%
