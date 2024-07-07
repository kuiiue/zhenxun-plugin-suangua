# zhenxun-plugin-suangua
zhenxun-bot真寻机器人的算卦插件
## 文件说明
* `suangua/`  
插件文件夹，直接放到plugin文件夹里就好
* `suangua/gua/`  
卦象图片文件夹
* `suangua/64.json`  
64卦辞json
* `suanguan/__init__.py`  
插件主文件
## 使用方法
- `算卦`  
随机
- `算卦[文字/图片]`  
也是随机，而且文字/图片并没有用
- `算卦[0-64]`  
0显示算卦标语，1-64显示对应的卦
## 一些说明
- 卦象和卦辞均是百度搜索得来
- 因为群友想要运势类小游戏，在[真寻插件目录](https://github.com/zhenxun-org/nonebot_plugins_zhenxun_bot)中找到了[@AkashiCoin](https://github.com/AkashiCoin)大佬的[随机塔罗牌](https://github.com/AkashiCoin/nonebot_plugins_zhenxun_bot/tree/master/tarot)插件，受此启发捣鼓了一个算卦插件，其中抄了大佬塔罗牌插件的两行代码。~~程序员的事怎么能说是扌（啪~~
- **算卦不算命，求己胜求人。**
## 使用例
![suangua](https://user-images.githubusercontent.com/30593961/229328373-ff1a9dd8-df80-43a7-96a8-7883b28ef9ef.png)
## 更新记录
- 2023-02-15: 应[@kuai364354200](https://github.com/kuai364354200)的[issue](https://github.com/kuiiue/zhenxun-plugin-suangua/issues/1)建议，返回算卦结果时at发起人，防止多人算卦时搞混。
- 2024-07-07: 重新生成了统一样式的卦辞图片，返回时直接返回图片。新的例图如下所示。甚至这些图片的尺寸挺适合做成卡牌，还有牌背...
