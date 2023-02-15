# zhenxun-plugin-suangua
zhenxun-bot真寻机器人的算卦插件
## 文件说明
* suangua —— 插件文件夹，直接放到plugin文件夹里就好
* gua —— 卦象图片文件夹
* 64.json —— 64卦辞json
* \_\_init\_\_.py —— 插件主文件
## 使用方法
- 算卦 —— 随机
- 算卦+文字/图片 —— 也是随机，而且文字/图片并没有用
- 算卦+0-64之间（包含）的数字 —— 0显示算卦标语，1-64显示对应的卦
## 一些说明
- 卦象和卦辞均是百度搜索得来
- 我使用插件的时候有些卦象图片会莫名其妙地处罚风控，我的解决办法是加try-except，另一种办法是用新的卦象图片对应替换原来的。
- 有些卦辞文本也会莫名其妙风控
- 因为群友想要运势类小游戏，在[真寻插件目录](https://github.com/zhenxun-org/nonebot_plugins_zhenxun_bot)中找到了[@AkashiCoin](https://github.com/AkashiCoin)大佬的[随机塔罗牌](https://github.com/AkashiCoin/nonebot_plugins_zhenxun_bot/tree/master/tarot)插件，受此启发捣鼓了一个算卦插件，其中抄了大佬塔罗牌插件的两行代码。~~程序员的事怎么能说是扌（啪~~
- **算卦不算命，求己胜求人。**
## 更新记录
- 2023-02-15: 应[@kuai364354200](https://github.com/kuai364354200)的[issue](https://github.com/kuiiue/zhenxun-plugin-suangua/issues/1)建议，返回算卦结果时at发起人，防止多人算卦时搞混。
