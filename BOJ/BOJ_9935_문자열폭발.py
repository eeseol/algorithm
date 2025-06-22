# data = list(map(str, input()))
# target = list(map(str, input()))
#
# check_start_index = 0
# check_end_index = len(target) - 1
# new_data = []
# flag = 0
# while True:
#     # 끝에 점이 같아
#     if data[check_end_index] == target[-1]:
#         for target_index in range(len(target) - 1, -1, -1):
#             # 체크하는게 틀려
#             if data[check_end_index] != target[target_index]:
#                 new_data = new_data + data[check_start_index:check_end_index + 1]  # new_data에 밀기
#                 check_start_index = check_end_index + 1  # start, end index 업데이트
#                 check_end_index = check_start_index + len(target) - 1
#                 break
#             check_end_index -= 1
#         else:
#             check_start_index = check_start_index + len(target)
#             check_end_index = check_start_index + len(target) - 1
#             flag = 1
#     else:
#         temp_index = check_start_index
#         check_start_index += 1
#         for index in range(len(target) - 1):
#             if data[check_start_index] == target[0]:
#                 new_data = new_data + data[temp_index:check_start_index]
#                 check_end_index = check_start_index + len(target) - 1
#                 break
#             check_start_index += 1
#         else:
#             check_end_index = check_start_index + len(target) - 1
#             new_data = new_data + data[temp_index:check_start_index]
#
#     # new_data = new_data + data[check_start_index:check_end_index+1]
#
#     if check_end_index >= len(data):
#         new_data = new_data + data[check_start_index:]
#         # 폭탄 없었다
#         if flag == 0:
#             break
#         else:
#             data = []
#             for i in range(len(new_data)):
#                 data.append(new_data[i])
#             flag = 0
#             check_start_index = 0
#             check_end_index = len(target) - 1
#             new_data.clear()
#
#             if len(data) < len(target):
#                 break
#
# if len(data) == 0:
#     print("FRULA")
# else:
#     for i in range(len(data)):
#         print(data[i], end="")
#


data = input()
target = input()
stack = []

target_len = len(target)

for ch in data:
    stack.append(ch)

    if len(stack) >= target_len:
        # 끝이 폭탄과 일치하는지 확인
        if ''.join(stack[-target_len:]) == target:
            for _ in range(target_len):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
