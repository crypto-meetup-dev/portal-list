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

parent 是啥。。。不太清楚，等待小岛补充

creator_fee 应该是创建者抽水？

ref_fee 是邀请者抽水？

k 是下次价格的倍率。。。350是1.35倍

price 是初始价格 1000则是0.1 eos

st 为0 则表示立马可以买了。。。应该可以设置为时间戳，则表示在某个时间后才可以够吗
