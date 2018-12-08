# portal-list

## 如果上传自己的坐标信息

1. 首先找到一张带坐标的图片
2. 到https://www.conversion-tool.com/imagetoheic/  把图片转换成.heic后缀的
3. 复制一个目录。（比如 **0. 小樽运河**）

然后把刚才转好的图片丢进去,把之前的图片给删了

然后就是修改 ```meta.json```文件了

```
{
	"creator": "minakokojima",
	"id": 9,
	"parent": 111,
	"creator_fee": 20,
	"ref_fee": 50,
	"k": 350,
	"price": 1000,
	"st": 0
}
```

creator 改成你的eos用户名

id 是累加的，你可以查看最后一个的id是啥,然后+1

parent 该portal属于land的id，假设该地标在中国，中国该land的id是111，那么该字段填111

creator_fee 该地标创建者费用，（即以后该地标每笔转手产生的delta盈利，20 / 1000归地标创建者）这段规则可能会改。

ref_fee 该地标推广者费用，即以后该地标产生交易，而买者A是通过玩家B的邀请链接来的，那么该笔转手产生的delta盈利， 50 / 1000 归玩家B，这段规则可能会改。

k 该地标每产生一笔交易（转手），价格增长幅度，这里为下次价格 = 当前价格 * (1000 + 350) / 1000

price 是初始价格 1000则是0.1 eos

st 为0 则表示立马可以买了（目前合约没有用到
