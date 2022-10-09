# genshin-gacha-url
# 功能
## 用米游社的cookie去获取原神抽卡记录url的authkey
# 支持的原神服务器
## 目前仅支持官服和渠道服(B服、小米服)
# 使用方法
## 首先米游社要绑定对应的原神账号，官服默认绑定，渠道服绑定方法如下：
## 获取米游社cookie
- 浏览器**无痕模式**打开`http://user.mihoyo.com/`
- 登录好后按下键盘`F12`或者鼠标右键`检查`，打开开发者工具，点击`Console`（中文版为`控制台`）
- 输入
`var cookie=document.cookie;var ask=confirm('Cookie:'+cookie+'\n\nDo you want to copy the cookie to the clipboard?');if(ask==true){copy(cookie);msg=cookie}else{msg='Cancel'}`
回车执行，点击确定，此时cookie已经复制剪贴板里了
## 执行main.py，粘贴cookie，回车，若有多个账号，按提示输入序号即可，程序执行完毕后，会打印出`https://…#log`的链接，将它复制粘贴到别人的抽卡分析程序里就可以记录抽卡信息了
#代码参考
-ds的获取参考`https://github.com/Womsxd/AutoMihoyoBBS`
