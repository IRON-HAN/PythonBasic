1. bytes.decode(encoding="utf-8",errors="strict")
* 使用bytes对象的decode方法来解码给定的bytes对象,这个bytes对象可以由str.encode()来编码返回

2. encode(encoding="utf-8",errors="strict")
* 用encoding指定的格式编码字符串,如果出错则默认抛出ValueError异常,除非errors="ignore"或者"replace"

3. isalnum() 字符串length>=1且全是字母或者数字

4. isalpha() 字符串length>=1且全是字母

5. isnumeric() 字符串只包含数字

6. join(seq) 以指定字符串作为分隔符, 将seq中所有的元素(的字符串表示)合并为一个新的字符串

7. istrip() 截掉字符串左边的空格或者指定字符

8. rstrip() 删除字符串末尾的空格

9. split(str="",num=string.count(str)) 以str为分隔符截取字符串, 如果Num有指定值,则仅截取num+1个字符串
