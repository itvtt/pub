import pandas as pd

# 엑셀 데이터를 DataFrame으로 읽어옵니다.
df = pd.read_excel("c:/b.xlsx")

# 모듈과 슬롯을 저장할 변수 초기화
module_slot_ids = {}

# 데이터를 순회하며 모듈과 슬롯 정보 추출
for index, row in df.iterrows():
    module = row['id']
    item = row['Module']
    slot = row['slot']

    # 모듈과 슬롯을 조합하여 식별자 생성
    identifier = f"{module} {slot}"

    # 식별자가 이미 존재하는 경우
    if identifier in module_slot_ids:
        module_slot_ids[identifier].append(item)
    else:
        module_slot_ids[identifier] = [item]

# 결과 저장을 위한 DataFrame 생성
result_df = pd.DataFrame(columns=['Items', 'Module', 'Slot'])

# 결과 DataFrame에 데이터 추가
for identifier, items in module_slot_ids.items():
    module_label, slot_label = identifier.split()
    items_line = '-'.join(items)
    result_df = pd.concat([result_df, pd.DataFrame({'Items': [items_line], 'Module': [module_label], 'Slot': [slot_label]})])

# 결과를 Excel 파일로 저장
result_df.to_excel("result.xlsx", index=False)

# 결과 출력
print(result_df)
