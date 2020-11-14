# _*_ coding:utf-8 _*_

cd src
pyinstaller \
            --clean\
            --noconfirm\
            -w\
            --distpath=../dist\
            --workpath=../\
            build.spec
cd ..
