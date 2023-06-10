from PIL import Image
import Legend
import Ref
import os
import json
import statistics
from datetime import datetime
import openpyxl

# 이미지 파일 열기
root_path = "D:\\@temp\\열영상분석\\1.강원도농산물원종장\\1.누에_백견\\2.애벌레\\"

image_folder_name = root_path + "Thermal\\"
json_folder_name = root_path +  "annotation\\"
image_file_list = os.listdir(image_folder_name)

wb = openpyxl.Workbook()
sheet = wb.active

progress_count = 1
print(datetime.today())
for item in image_file_list:
    target_file = image_folder_name + item
    img = Image.open(target_file)

    #이미지 exif에서 최소온도, 최대온도를 가져온다.
    min_max = Ref.get_min_max(img)

    #최소온도와 최대온도에 따라 스케일바를 생성한다.
    legend_value = Ref.make_legend_value(min_max[0], min_max[1])

    json_file = item.rsplit('.')[0] + ".json"
    coodrs_list = Ref.getCoorsFromJsonFile(json_folder_name + json_file)
    temperature_mean_list = ""

    #json에서 가져온 객체들의 좌표목록을 루프 돌린다.
    for coords in coodrs_list:
        #각 각체들의 좌표목록을 RGB값 목록으로 바꾼다.
        try:
            rgb_list = Ref.getPolygonInnerRgb(target_file, coords)
        except:
            temperature_mean_list = temperature_mean_list + "|" + str(0)
            continue

        
        #각 객체들의 RGB값 목록을 루프를 돌린다.
        temperature_list = []
        for rgb in rgb_list:
            #RGB 값을 온도값으로 바꿔 준다.
            temperature_list.append(Ref.getTempature(rgb, legend_value))

        mean = statistics.mean(temperature_list)
        temperature_mean_list = temperature_mean_list + "|" + str(mean)


    sheet['A'+str(progress_count)] = target_file
    sheet['B'+str(progress_count)] = temperature_mean_list

    progress_count = progress_count + 1
    print("진행 : " + str(progress_count))

wb.save(image_folder_name.replace("\\", "__") + ".xlsx")
print(datetime.today())