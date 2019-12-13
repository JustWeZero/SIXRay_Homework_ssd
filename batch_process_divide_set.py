import os
import numpy
import random, shutil

def moveSomeFileToNewDir(fileDir, tarDir):
    #sonDirPath = []
    allDir = os.listdir(fileDir)  # 列出指定路径下的全部文件夹，以列表的方式保存
    for dir in allDir:  # 遍历指定路径下的全部文件和文件夹
        sonDirName = os.path.join(fileDir, dir)  # 子文件夹的路径名称
        if os.path.isdir(sonDirName):
            #sonDirPath.append(sonDirName)

            pathDir = os.listdir(sonDirName)  # 取图片的原始路径

            annoDir = os.path.join(sonDirName,pathDir[0])
            imgDir = os.path.join(sonDirName,pathDir[1])
            annoItem = os.listdir(annoDir)

            for name in annoItem:
                filenumber = len(annoItem)
                # print(filenumber)
                rate = 0.8  # 自定义抽取图片的比例，比方说100张抽15张，那就是0.15
                picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
                sample = random.sample(annoItem, picknumber)  # 随机选取picknumber数量的样本图片
                # print(len(sample))
                # print(sample)
                imageName = name.split('.')[0] + '.jpg'
                if name in sample:
                    oldTxtDir = annoDir + '\\' + name
                    oldImgDir = imgDir + '\\' + imageName
                    newAnnoDir = os.path.join(tarDir +'\\train\\',dir+'\\Annotation\\')
                    newImgDir = os.path.join(tarDir + '\\train\\', dir+'\\Image\\')

                    if not os.path.exists(newAnnoDir):
                        os.makedirs(newAnnoDir)
                    if not os.path.exists(newImgDir):
                        os.makedirs(newImgDir)

                    # newTarDir = tarDir + '\\' + dir + '\\' + name
                    newTarTxtDir = os.path.join(newAnnoDir, name)
                    newTarImgDir = os.path.join(newImgDir, imageName)

                    print(oldTxtDir, newTarTxtDir)
                    shutil.copy(oldTxtDir, newTarTxtDir)
                    shutil.copy(oldImgDir, newTarImgDir)
                else:
                    oldTxtDir = annoDir + '\\' + name
                    oldImgDir = imgDir + '\\' + imageName
                    newAnnoDir = os.path.join(tarDir + '\\validation\\', dir + '\\Annotation\\')
                    newImgDir = os.path.join(tarDir + '\\validation\\', dir + '\\Image\\')

                    if not os.path.exists(newAnnoDir):
                        os.makedirs(newAnnoDir)
                    if not os.path.exists(newImgDir):
                        os.makedirs(newImgDir)

                    # newTarDir = tarDir + '\\' + dir + '\\' + name
                    newTarTxtDir = os.path.join(newAnnoDir, name)
                    newTarImgDir = os.path.join(newImgDir, imageName)

                    print(oldTxtDir, newTarTxtDir)
                    shutil.copy(oldTxtDir, newTarTxtDir)
                    shutil.copy(oldImgDir, newTarImgDir)

fileDir = r"D:\样本不均航"      #源图片文件夹路径
valDir = r'D:\Python_Project\ssd.pytorch-master\battery_dataset_unbalance'       #移动到目录路径
moveSomeFileToNewDir(fileDir, valDir)
# testDir = r'E:\test_data'     #移动到测试集目录路径
# moveSomeFileToNewDir(fileDir, testDir)
