# py_project
airport_massage_mail

这个代码用于爬取飞猪机票信息 然后将信息事实发送给目标账户</br>
如果你使用它请修改发送邮箱的相关信息和目标邮箱 起飞地点和降落地点</br>
  
11.20.2017
又要开始一年一度的春运了，对于我们这些在远方上学的孩子来说回家真的不容易啊。</br>
更新记录：</br>
对请求飞猪的页面进行了解耦，但是看上去效果没那么好</br>
下一步的改进：</br>
- 1.发送邮件页面消息太乱，许多变量是公有变量。期望下一次回家能够把这个修改过来。</br>
- 2.部署问题：a.第一次采用了Linux corn/corntab 没有部署成功，不会定时执行.这次准备用uwsgi试试</br>
- 3.应该要让这个东西服务于很多人，可以写一个页面来为更多人服务。</br>
- 4.期待这个东西能够形成一个网页，动态提醒用户机票的最低价格</br>
  


