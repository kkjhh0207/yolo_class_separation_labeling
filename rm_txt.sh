for file in *
do
    if [ ${file: -4} == ".txt" ];
    then
        fileName="${file%.*}"
        echo $fileName
        main="$fileName.jpg"
        if [ -e $main ];
        then
           echo "file exists"
        else
           echo "file doesn't exits"
           rm -rf $file
        fi
    fi
done


