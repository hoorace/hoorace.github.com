---
comments: true
date: 2015-07-21 11:42:30
layout: post
slug: patch-ubuntu-Heartbledd-with-V14
title: HeartBleed Ubuntu 修复问题记录
categories:
- linux
tag:
- ubuntu
- heartbleed
- openssl

---
<p>&nbsp;&nbsp;&nbsp;&nbsp;在安装某linux软件的时候，提示我们的服务器上的openssl是有漏洞的版本，需要重新安装一下。到linuxe服务器上查看一下：
<pre><code class="bash lineNumbers">
dpkg -l | grep "openssl”
openssl                                  1.0.1f-1ubuntu2.8                amd64
</code></pre>
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;1.0.1f 是HeartBleed的版本之一，需要修复问题。</p>
<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 1：卸载旧版本的openssl</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">

<pre><code class="bash lineNumbers">
apt-get purge openssl
rm -rf /etc/ssl
</code></pre>

</div>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 2：安装新版本的openssl</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp; 安装版本</p>
<div>

<pre><code class="bash lineNumbers">
wget https://www.openssl.org/source/openssl-1.0.2d.tar.gz 
tar zxvf openssl-1.0.2d.tar.gz
./config  --prefix=/usr/local --openssldir=/usr/local/ssl
make && make install
./config shared --prefix=/usr/local --openssldir=/usr/local/ssl
make clean
make && make install
</code></pre>

</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;链接openssl <br />
<pre><code class="bash lineNumbers">
ln -sf /usr/local/bin/openssl `which openssl`
</code></pre>
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;查看openssl版本 <br />

<pre><code class="bash lineNumbers">
openssl version
</code></pre>
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;安装openssl之后，有些以前编译的软件会出现无法使用的情况，报错为：/usr/local/lib/libssl.so.1.0.0: no version information available
需要重新编译一下。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;</p>
</div>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 3：OR 打patch的方式来处理</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp;patch地址：<a href="https://launchpad.net/ubuntu/+source/openssl/1.0.1-4ubuntu5.12" target="_blank">https://launchpad.net/ubuntu/+source/openssl/1.0.1-4ubuntu5.12</a> </p>
<pre><code class="bash lineNumbers">
wget http://www.openssl.org/source/openssl-1.0.1f.tar.gz
tar -xvf openssl-1.0.1f.tar.gz
wget https://launchpad.net/ubuntu/+archive/primary/+files/openssl_1.0.1f-1ubuntu1.debian.tar.gz
tar -xvf openssl_1.0.1f-1ubuntu1.debian.tar.gz
mv debian openssl_1.0.1f-1ubuntu1
cd openssl-1.0.1f/
patch -p1 < ../openssl_1.0.1f-1ubuntu1/patches/version-script.patch
./config
make
make test
sudo make install
</code></pre>

</div>

<p style="background-color: rgb(230, 230, 250); height: 25px; width: 100%; padding-top: 9px; font-family: arial,helvetica,sans-serif; font-size: 14px; color: rgb(0, 0, 0);"><span style="font-size:14px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp; 4: FAQ</strong></span></p>
<div style="border-left: 2px solid rgb(204, 204, 204); padding-left: 6px; margin-left: 6px; margin-bottom: 10px;">
<p>&nbsp;&nbsp;&nbsp;&nbsp; <b>3.1 启动应用报错：</b></>
<p><pre>/usr/local/sbin/xxxx: /usr/local/lib/libssl.so.1.0.0: no version information available (required by /usr/local/sbin/xxxx)
/usr/local/sbin/xxxx: /usr/local/lib/libcrypto.so.1.0.0: no version information available (required by /usr/local/sbin/xxxx)
/usr/local/sbin/xxxx: /usr/local/lib/libcrypto.so.1.0.0: no version information available (required by /usr/local/lib/xxxx-server.so)
/usr/local/sbin/xxxx: /usr/local/lib/libcrypto.so.1.0.0: no version information available (required by /usr/local/lib/xxxx-radius.so)
</pre> </p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; 解决方案：</>
<pre><code class="bash lineNumbers">
cd /opt/update/openssl-1.0.2d
make clean
vim openssl.ld
//文件内容
OPENSSL_1.0.0 {
    global:
    *;
};

//编译注意备份 /usr/local/lib/libssl.so.1.0.0 和 /usr/local/lib/libcrypto.so.1.0.0
./config --prefix=/usr/local --openssldir=/usr/local/ssl shared -Wl,--version-script=/opt/update/openssl-1.0.2d/openssl.ld -Wl,-Bsymbolic-functions
make
make test
make install
ldconfig
</code></pre>
<p>&nbsp;&nbsp;提示：编译之后有些系统会导致ssh无法登陆，需要更新把/usr/local/lib/libcrypto.so.1.0.0文件覆盖回原来的版本。</>
</div>

<p>&nbsp;&nbsp;&nbsp;&nbsp; </p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;参考文档： </p>
- [x] <a href="http://askubuntu.com/questions/444702/how-to-patch-the-heartbleed-bug-cve-2014-0160-in-openssl" target="_blank">How to patch the Heartbleed bug (CVE-2014-0160) in OpenSSL?</a>
- [x] <a href="http://wangyan.org/blog/install-openssl-from-source.html" target="_blank">Linux 从源码编译安装 OpenSSL</a>
- [x] <a href="http://heartbleed.com" target="_blank">http://heartbleed.com</a>