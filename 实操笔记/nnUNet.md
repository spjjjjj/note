## 参数初始化 
参数名前加`--`，如`--dataset_name_or_id`，表示该参数是可选的参数，使用时可以不提供该参数，程序会使用默认值。  
调试代码时通过设置默认值来修改此参数。
```py
parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name_or_id', type=str, required=False, default='392',
                        help="Dataset name or ID to train with")
    parser.add_argument('--configuration', type=str,default='3d_fullres',
                        help="Configuration that should be trained")
    parser.add_argument('--fold', type=str, default='0',
                        help='Fold of the 5-fold cross-validation. Should be an int between 0 and 4.')
```

## ERROR：One or more background workers are no longer alive.
~~Windows系统训练时，一般是由于多线程引起的，可以尝试将多线程关闭，设置`num_threads=0`，或者使用单线程训练。~~  
一般是由于多线程引起的，具体原因可能是设置的线程数（？）大于cpu核心数，可以尝试减少线程数，设置`num_threads`。  
查看 *nnunetv2/configuration.py* 或 *nnunetv2/utilities/default_n_proc_DA.py* 文件中线程设定。
```py
    else:
        use_this = 5  # default value
```
在此处设置默认值。

---
---
## 调试

使用qt5后端进行数据可视化
```py
import matplotlib 
matplotlib.use('Qt5Agg') 
import matplotlib.pyplot as plt  
plt.plot([1, 2, 3], [4, 5, 1]) 
plt.show(block=True) # 此时应弹出窗口显示图像
```