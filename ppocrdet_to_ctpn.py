'''
paddleocr标签转ctpn要求格式
'''
import os

xy_str = ""
label_dir = "D:\project\ocr\ocr.pytorch-master\ctpndata\labels"
with open("Label.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line.split("[")[0][2:-1]) #image_name
        label_name = line.split("[")[0][2:-1].split(".")[0]
        print(line.split("\"")[3]) #labels
        # print(line.split("[[")[1].split("]]")[0].split("], [")[::-1])
        xy_list = line.split("[[")[1].split("]]")[0].split("], [")[::-1]   #['586, 479', '585, 525', '116, 529', '118, 478']
        for xy in xy_list:
            xy_str += xy
            xy_str += ","
            xy_str = xy_str.replace(" ","")
        xy_str += "0,"
        xy_str += str(line.split("\"")[3])
        print(xy_str)
        label_path = os.path.join(label_dir, label_name)
        label_path += ".txt"
        with open(label_path, "w") as file:
            file.write(xy_str)

        xy_str = ""

