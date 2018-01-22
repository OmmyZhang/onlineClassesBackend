# onlineClassesBackend
Part of online classes, work for sjx.

[关于获取openid](https://www.jianshu.com/p/9b5b80ae301b)

## 接口描述

+ /student
  + /student/ [get] 获取openid
    + appid: string
    + secret: string
    + loginCode.code : string
    + 返回{openid}
  + /student/ [post] 创建新用户
    + openid: string
    + invite code: string
    + username: string
  + /student/ [get] 所有用户列表(限管理员)
    + 返回: [{openid, username}]
  + /student/{openid}/ [get] 查询某人的所有课程及进度
    + 返回: [{courseName, process}]
+ /course
  + /course/process/ [post] 设置某人的某门课进度
    + courseName： string
    + openid： string
    + process: int
+ /file
  + /file/{fileName}/ [get] 下载文件
    + openid: string



## 数据库(models)

+ Student
  + openid
  + username
+ CourseRecord
  + openid
  + process
+ File (可下载的文件列表)
  + fileName
  + availableTime
  + courseName
+ InviteCode (可用邀请码池)
  + code
