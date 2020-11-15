# ES6-regexp（）——笔记

正则----作用于字符串，用来校验，提取元素。

### 编写正则

#### 	创建正则：

​		JS风格： new RegExp();  --比较麻烦

​		perl风格： /  ... /

#### 	正则中的方法

​		search() ：类似于indexof()， 返回所查找元素在字符串中第一次出现的位置

​		match()：用来匹配，返回一个arr，包含所匹配的元素

​		replace()：替换 （被换的项，换成的项）两个参数

#### 	正则中的选项

​		i   IgnorCase   忽略大小写

​		g  Globle   全局匹配

​		m  mutiple  允许多行匹配

#### 	转义

​		\d  digit 的简写  用于查找数字

#### 	量词

​		\d\d  \d{3}  + 若干

​		{n}  固定为n位数

​		{n, m}  最少n位，最多m位

​		{n, }  最少n位，最多不限

​		{0, m} 最少0位，最多m位

​		+ -->{1, } 的简写

​		* -->{0, } 的简写    （相较于+更容易出错，比如任何非数字的元素都是0个数字，会返回一个空字符串）

​		? -->{0,1} 的简写 （可有可无，但只能有1个）

#### 	元字符

​		1、或： /[abc]/ --> a或b或c其中的一个

​		2、范围： /[a-z]/ /[0-9]/  /a-z0-9/(可以混写)   \d就是/[0-9]/的简写

​		3、排除： ^ 除了  \[^abc]-->除了a或b或c

#### 	修饰符（谓语）

​		^   行首

​		$   行尾

#### 	单行模式

​		^ $ 指的是每一行的开头和结尾，不会识别字符串里面的换行

#### 	多行模式

​		^ $ 指的是每一行的开头和结尾，识别字符串中的\n

### 特别注意

​	^符号在[]里面是表示  非  ，在[]外面表示行首！！！

### *

*是一个限定符，用来修饰前一个字符或分组，限定匹配重复的数量为任意数量。
例如：
[正则表达式](http://www.baidu.com/s?wd=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)  a\*  可以匹配 a   aa   aaa  aaaa aaaaaaa等等
[正则表达式](http://www.baidu.com/s?wd=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)   (ab)\*   可以匹配  ab  abababab   ababababababab等等

需要注意个是，\*与+不同，+要求重复数量至少为1，*则可以为0，所以字符串为空也是可以匹配的。

以下是常用的限定符代码：
*重复零次或更多次
+重复一次或更多次
?重复零次或一次
{n}重复n次
{n,}重复n次或更多次
{n,m}重复n到m次

### .

任意单个字符