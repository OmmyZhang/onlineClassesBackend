# onlineClassesBackend
Part of online classes, work for sjx.

[关于获取openid](https://www.jianshu.com/p/9b5b80ae301b)

环境: Python3.5

依赖: django , rest_framework

调试模式下运行方式: `python3 manager.py runserver`

新增管理员: `python3 manager.py createsuperuser`

进入后台: `/admin`

浏览器下访问接口如果想看到json格式请加`?format=json`(或者手动选一下某个按钮)

**实际部署时请把要用来下载的文件或图片放到/media**

**实际部署时请在onlineClass/setting.py中把`DEBUG`设为False，`ALLOWED_HOST`中添加实际部署的域名。**

## 接口描述

+ /getid
  + /getid/ [get] 获取openid
    - appid: string
    - secret: string
    - js_code: string
    - 返回:  原样返回api.wx.qq.com给的东西


+ /student
  + /student/ [post] 创建新用户
    + openid: string
    + invite_code: string
    + username: string
  + /student/ [get] 所有用户列表
    + 返回: [{openid, username}]
  + /student/{openid}/ [get] 查询某人的所有课程及进度
    + 返回: [{course_name, process}]
+ /course
  + /course/ [post] 设置某人的某门课进度
    + course_name： string
    + openid： string
    + process: int
  + /course [get] 查看所有记录


  + /course/file/{fileName}/ [get] 下载文件，如果选了这门课
    + openid: string



## 数据库(models)

+ Student
  + openid
  + username
+ CourseRecord
  + openid
  + course_name
  + process
+ File (可下载的文件列表)
  + name
  + available_time
  + course_name
+ InviteCode (可用邀请码池,每次注册自动删除)
  + code
