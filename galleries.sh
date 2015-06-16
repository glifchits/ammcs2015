initdir=$(pwd)

cd ./pictures
for dir in *; do
  cd $dir
  echo $dir
  ls
  sigal build
  echo "\n"
  cd ..
done

cd $initdir
