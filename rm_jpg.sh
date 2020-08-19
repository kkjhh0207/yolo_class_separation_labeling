for file in *
do
    if [ ${file: -4} == ".jpg" ];
    then
       # name=$file | cut -d'.' -f1
       # name=echo $file | cut -d'.' -f1 
       fileName="${file%.*}"
        echo $fileName
       # echo $name 
        main="$fileName.txt"
       # echo $main
        if [ -e $main ];
        then
           echo "file exists"
        else
           echo "file doesn't exits"
           rm -rf $file
        fi
    fi
done


