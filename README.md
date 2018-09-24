## python.Hello-World-Computer-Programming-for-Kids-and-Other-Beginners
## 学习python，关于《与孩子一起学编程》的代码
===============================================================================================
    这个项目的初衷是实践极客时间陈皓的《左耳听风》专栏中[***“程序员练级攻略（2018）”***](http://gk.link/a/100HQ)

    由此接触到了一门现在热火朝天的脚本语言python，这本书也很有意思，书名也叫做与孩子一起学编程，于是想到可以和一起在学这本书的小伙伴一起学习和进步，也学着用一下github来管理项目

    下面我列出一些使用这本书的一些资源
    Python Releases for Windows：
        python有2和3两个版本，初学建议从2开始学起，后面可以转3，这本书用的是2
        目前2最新版本地址：
          （64位）https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi
          （32位）https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi

        其中用到了Pygame、PythonCard和EasyGui三个模块，使用pip管理模块，但是有一些早期的模块还没加入pip，那么可以把下载来的模块放在C:\Python27\Lib\site-packages，如果你也和我一样没有改安装目录的话，另外在下载的时候一定要注意与python对应的版本，不同的版本可能不起作用，我在使用PythonCard的时候就遇到了这个问题，这个模块还要使用另外一个模块wxPython，开始的时候我把这个模块下错了版本，结果PythonCard无法正常使用，能启动，但是会报错，在折腾许久之后，终于找到了问题，是wxPython版本太高和PythonCard匹配不上，最后是根据它们两个发布的时间相近下载了wxPython。