---
comments: true
date: 2013-08-26 16:52:19
layout: post
slug: something-about-linux-terminal-improve-efficiency
title: 记住linux terminal下的快捷键，提高操作效率!
categories:
- linux
tag:
- linux
- terminal
- mac

---
 
<p> &nbsp;&nbsp;&nbsp;&nbsp; 不少程序员操作linux就如同他们操作vim是一样的，会用的就是移动键，前后左右移动，输入内容，使用backspace删除相关的内容，然后号称自己会vim。而随便问几个简单的问题，就不知道了。而vim的命令甚多，需要不断积累，不是一朝一日可以操作熟练的。而linux的terminal的快捷键较少，掌握起来较为方便，所以值得快速传播一下。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; <b style="color:#cc0000;">0：搜索操作</b> </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; 搜索历史命令的快捷键： <b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + r</b> 当然，不是你想要的命令的时候，你可以继续 <b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + r</b> ，搜索到相关命令，请按<i style="border:1px #ccc solid;padding:3px 8px;"><b>Enter</b></i>。如果想增加命令记录保存的数量，请到.bash_profile下面去设置 HISTFILESIZE 和 HISTSIZE 两个参数。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; <b style="color:#cc0000;">1：移动操作</b>
	<ul>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + f</b> -- 向右移动一个字符，当然多数人用 <b style="border:1px #ccc solid;padding:3px 5px;">→</b></li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + b</b> -- 向左移动一个字符， 多数人用 <b style="border:1px #ccc solid;padding:3px 5px;">←</b></li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">ESC + f</b> -- 向右移动一个单词，MAC下建议用 <b style="border:1px #ccc solid;padding:3px 8px;">ALT + →</b></li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">ESC + b</b> -- 向左移动一个单词，MAC下建议用 <b style="border:1px #ccc solid;padding:3px 8px;">ALT + ←</b></li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + a</b> -- 跳到行首</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + e</b> -- 跳到行尾</li>
	</ul>
</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; <b style="color:#cc0000;">2：删除操作</b>
	<ul>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + d</b> -- 向右删除一个字符</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + h</b> -- 向左删除一个字符</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + u</b> -- 删除当前位置字符至行首（<b style="color:#cc0000;">输入密码错误的时候多用下这个</b>）</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + k</b> -- 删除当前位置字符至行尾</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + w</b> -- 删除从光标到当前单词开头</li>
	</ul>
</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; <b style="color:#cc0000;">3：命令切换操作</b>
	<ul>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + p</b> -- 上一个命令，也可以用 <b style="border:1px #ccc solid;padding:3px 5px;">↑</b></li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + n</b> -- 下一个命令，也可以用 <b style="border:1px #ccc solid;padding:3px 5px;">↓</b></li>
	</ul>
</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; <b style="color:#cc0000;">4：其他操作</b>
	<ul>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + y</b> -- 插入最近删除的单词</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + c</b> -- 终止操作</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + d</b> -- 当前操作转到后台</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Ctrl + l</b> -- 清屏 （有时候为了好看）</li>
		<li style="padding-bottom:10px;"><b style="border:1px #ccc solid;padding:3px 8px;">Tab</b> -- 你懂的，不懂自己去查</li>
	</ul>
</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; 以上的命令是适用于linux和mac下的terminal，还有各种mac或者是linux的差异命令，暂时没有写出来，等到后续自己再研究一下后补充。平时工作中，习惯了简单的操作，其实工作前2年我也就知道3，4个快捷键，一方面是自己缺少总结，二是没有看到高人操作，所以进步会慢很多，如果想更好的学习linux操作，多到高手后面站一下，探讨一下，会短平快的提升自己的操作水平。</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; 欢迎大家补充，^_^</p>
<p> &nbsp;&nbsp;&nbsp;&nbsp; </p>



