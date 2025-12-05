将新的conda路径文件覆盖到原有的文件
```
cp /workspace/.condarc /root/
```

安装本地bz2包
```
conda install --use-local path/to/file.tar.bz2
```

zip命令压缩指定文件下的全部文件
```
zip -r name.zip path/to/folder/
# 压缩包存放在当前路径（不是原文件夹的路径）
```

无视版本匹配，直接安装指定包
```
python -m pip install chumpy --no-build-isolation
```