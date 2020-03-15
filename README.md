# little-pyinstaller-platform
pyinstaller发布python程序的问题
* 打包后的文件比较大
* 由于开发机不具备生成环境的数据，调试需要在生产环境进行，增加调试代码需要重新打包，rz上传很没有效率
* 临时写个小脚本，生产环境python可能缺少库

这个小框架仅把main.py进行打包，在main.py中动态加载模块并执行
