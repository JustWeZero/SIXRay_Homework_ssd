import os.path


names = [name.split('.')[0] for name in os.listdir(r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance\validation\core_500\Annotation')
         if os.path.isfile(os.path.join(r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance\validation\\core_500\\Annotation', name))]

names_coreless = [name.split('.')[0] for name in os.listdir(r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance\validation\coreless_5000\Annotation')
         if os.path.isfile(os.path.join(r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance\validation\coreless_5000\Annotation', name))]


names.extend(names_coreless)

file = open(r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance\validation\sub_train_core_coreless.txt','w',encoding='UTF-8')
file.writelines(i+'\n' for i in names if i!=names[-1])
file.writelines(names[-1])

