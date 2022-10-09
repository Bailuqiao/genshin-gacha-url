# 获取原神抽卡记录链接
# 功能&用途
- mhy提高了获取抽卡记录链接的难度，目前有些app可以帮我们获取，部分人担心不开源app的安全问题，故有此项目
- 用米游社的cookie去获取原神抽卡记录url的authkey
# 支持的原神服务器
- 目前仅支持官服和渠道服(B服、小米服)，**不支持**国际服
# 使用方法

1.首先米游社要绑定对应的原神账号，官服默认绑定，渠道服要先**自行绑定**，具体方法百度

2.获取米游社cookie

- 浏览器**无痕模式**打开`http://user.mihoyo.com/`
- 登录好后按下键盘`F12`或者鼠标右键`检查`，打开开发者工具，点击`Console`（中文版为`控制台`）
- 输入
```javascript
var cookie=document.cookie;var ask=confirm('Cookie:'+cookie+'\n\nDo you want to copy the cookie to the clipboard?');if(ask==true){copy(cookie);msg=cookie}else{msg='Cancel'}
```

3.回车执行，点击确定，此时cookie已经复制剪贴板里了

4.执行main.py，粘贴cookie，回车，若有多个账号，按提示输入序号即可，程序执行完毕后，会打印出`https://…#log`的链接，将它复制粘贴到别人的抽卡分析程序里就可以记录抽卡信息了

## 我想说的
- 手机端也是可以操作的，用kiwi浏览器，这个浏览器有开发者工具，可以获取cookie。运行python的话可以用Turmux之类的软件
- 那些获取抽卡记录链接的app也是能用的，挑选自己信得过的用
- 代码写得很乱，因为我目前没有电脑，用手机Turmux的vim手撸的，写得很痛苦，等以后再优化吧，就这几个api和参数，很容易看懂自己重写的

## 代码参考
- ds的获取参考[Womsxd/AutoMihoyoBBS](https://github.com/Womsxd/AutoMihoyoBBS)
