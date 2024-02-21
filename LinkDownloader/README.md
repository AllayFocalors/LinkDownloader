#LinkDownloader链接下载器
__（理论上网速多快，下载速度就能飙到多快）__
######开发者：悦灵Allay<br>Github@AllayFocalors<br>Bilibili@Allay-LtWiB
（在下是一个13岁的初中生诶嘿）
Verision: Pre-0.1.0.0

##基本原理
利用Python的requests库，请求资源后直接下载，所以下载速度应该特别快ｂ(￣▽￣)ｄ
可是 main.py line92 的 iter_content() 中的 chunk_size 参数鄙人不太清楚这个含义（哭）这个参数我赋值为buffer_size（网上抄的）
经过查阅资料，得知，这个参数越大，下载速度越快，可是我并没有感受到下载速度随着chunk_size的变化啊（哭）有没有大佬来给我解释一下(*^▽^*)

##How to use?
界面简单吧，字面意思:）

