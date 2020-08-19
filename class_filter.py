import os

if __name__=="__main__":
    human = 0
    load_path = "labels/"
    save_path = "labels_person/"
    file_list = os.listdir(load_path)
    txt_file_list = [file for file in file_list if file.endswith(".txt")]

   # print("file_list:{}".format(txt_file_list))

    for file in txt_file_list:
        l_f = open(load_path+file,"r+")
        lines = l_f.readlines()
        #print(file)
        #print(yolo_class)
        s_f = open(save_path+file,mode = "w")
        empty_flag = True
        for i in range(len(lines)):
            parse = lines[i].split(" ")
            yolo_class = float(parse[0])
            if(yolo_class==human):
                empty_flag = False
               # print(yolo_class)
                s_f.write(lines[i])
        s_f.close()
        if(empty_flag ==True):
            os.remove(save_path+file)
            print("file deleted due to absence of human class")
           
            
