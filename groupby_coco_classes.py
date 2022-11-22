import matplotlib.pyplot as plt
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

 
classes=['person',
 'bicycle',
 'car',
 'motorcycle',
 'airplane',
 'bus',
 'train',
 'truck',
 'boat',
 'traffic light',
 'fire hydrant',
 'stop sign',
 'parking meter',
 'bench',
 'bird',
 'cat',
 'dog',
 'horse',
 'sheep',
 'cow',
 'elephant',
 'bear',
 'zebra',
 'giraffe',
 'backpack',
 'umbrella',
 'handbag',
 'tie',
 'suitcase',
 'frisbee',
 'skis',
 'snowboard',
 'sports ball',
 'kite',
 'baseball bat',
 'baseball glove',
 'skateboard',
 'surfboard',
 'tennis racket',
 'bottle',
 'wine glass',
 'cup',
 'fork',
 'knife',
 'spoon',
 'bowl',
 'banana',
 'apple',
 'sandwich',
 'orange',
 'broccoli',
 'carrot',
 'hot dog',
 'pizza',
 'donut',
 'cake',
 'chair',
 'couch',
 'potted plant',
 'bed',
 'dining table',
 'toilet',
 'tv',
 'laptop',
 'mouse',
 'remote',
 'keyboard',
 'cell phone',
 'microwave',
 'oven',
 'toaster',
 'sink',
 'refrigerator',
 'book',
 'clock',
 'vase',
 'scissors',
 'teddy bear',
 'hair drier',
 'toothbrush']
print(classes)
 
class_dict = {i: 0 for i in classes}
print("total number of classes",len(class_dict))
 
def main(base_path):    
    FileList=os.listdir(base_path)
    for file in FileList:
        if file == "classes.txt":
            continue
        with open(base_path+file,'r') as f:
            for i in f.readlines():
                i = i.split(' ')            
                class_dict[classes[int(i[0])]]+=1 #i[0] is the first element
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.title('classes')
    plt.xticks(rotation=90)              
    bars = plt.bar(class_dict.keys(), class_dict.values())
    for b in bars:
        height = b.get_height()
        ax.annotate(f'{height}',
                    xy=(b.get_x() + b.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",  
                    va='bottom', ha='center'  
                    )
    plt.savefig('./labels.jpg', # save into file：png、jpg、pdf
                dpi = 100, # 
                bbox_inches = 'tight')#
    plt.show()
 
if __name__ == '__main__':
    base_path=r"C:\Users\zhang\Desktop\yolov5\data\coco_dataset\traffic_val_coco\labels\\"         
    main(base_path)
