简单来说：

标准盒模型：盒子宽度 = 左右外边距 + 左右边框宽度 + 左右内边距 + 内容宽度；

比如说，一个width=200px，height=200px的盒子，它的宽高分别为200px和200px，但是给它加了padding=10px之后，盒子的宽高就变成了220px，也就是说内外边距和边框的宽度不会影响内容的宽度，只会撑大盒子，让盒子越来越大。

但是，如果该盒模型设置了box-sizing：‘border-box’，那么，一个width=200px，height=200px的盒子添加了10px的padding之后，盒子的宽高依然是200px，变的是内容的宽高，内容的宽高被挤为180px，也就是说，border-box的盒模型是向内扩展的，内边距不会影响盒模型的宽高，只会挤压内容，让内容越来越小。

或者可以说：box-sizing: content-box为标准盒模型；box-sizing: box-sizing为IE盒模型。

IE8`及以上版本支持该属性，`Firefox` 需要加上浏览器厂商前缀`-moz-，`对于低版本的`IOS`和`Android`浏览器也需要加上`-webkit-`。实际上，很多`reset.css`或者`normal.css`里都包含如下`CSS`语句，也是比较赞成的用法：